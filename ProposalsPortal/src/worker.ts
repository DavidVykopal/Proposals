import { chat } from './chat';
import { mcp, tokensApi } from './mcp';
import type { Env } from './tools';

const SESSION_COOKIE = 'np_s';
const WHO_COOKIE = 'np_who';
const SESSION_DAYS = 30;
const enc = new TextEncoder();

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    const p = url.pathname;

    if (p.startsWith('/_p/')) return env.ASSETS.fetch(req);
    if (p === '/mcp' || p === '/mcp/') return mcp(req, env, url);
    if (p === '/robots.txt') return new Response('User-agent: *\nDisallow: /\n');

    if (p === '/login' || p === '/login/') {
      if (req.method === 'POST') return login(req, env, url);
      if (!env.SITE_PASSWORD && !url.searchParams.get('e')) return redirect('/login/?e=nopw');
      return asset(env, url, '/_p/login');
    }
    if (p === '/logout' || p === '/logout/') {
      return redirect('/login/', [cookie(SESSION_COOKIE, '', 0), cookie(WHO_COOKIE, '', 0, false)]);
    }

    const authed = await validSession(req, env);
    if (!authed) {
      if (p.startsWith('/api/')) return json({ error: 'auth' }, 401);
      return redirect(`/login/?next=${encodeURIComponent(p + url.search)}`);
    }

    if (p === '/who' || p === '/who/') {
      if (req.method === 'POST') return setWho(req, env, url);
      return asset(env, url, '/_p/who');
    }

    if (p.startsWith('/api/')) {
      try {
        return await api(req, env, url, whoFrom(req));
      } catch (e) {
        console.error(e);
        return json({ error: 'server', message: 'Něco se pokazilo na serveru. Zkuste to znovu.' }, 500);
      }
    }

    const isPage = !p.startsWith('/raw/') && (req.headers.get('accept') || '').includes('text/html');
    if (isPage && !whoFrom(req)) return redirect(`/who/?next=${encodeURIComponent(p + url.search)}`);

    const res = await env.ASSETS.fetch(req);
    return privateCopy(res);
  },
} satisfies ExportedHandler<Env>;

// ---------- auth ----------
async function hmac(secret: string, data: string): Promise<string> {
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(data));
  return btoa(String.fromCharCode(...new Uint8Array(sig))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function sameSecret(a: string, b: string): Promise<boolean> {
  const [ha, hb] = await Promise.all([crypto.subtle.digest('SHA-256', enc.encode(a)), crypto.subtle.digest('SHA-256', enc.encode(b))]);
  return crypto.subtle.timingSafeEqual(ha, hb);
}

async function validSession(req: Request, env: Env): Promise<boolean> {
  if (!env.SITE_PASSWORD) return false;
  const raw = readCookie(req, SESSION_COOKIE);
  if (!raw) return false;
  const [v, exp, sig] = raw.split('.');
  if (v !== 'v1' || !exp || !sig || Number(exp) < Date.now() / 1000) return false;
  return sameSecret(sig, await hmac(env.SITE_PASSWORD, `v1.${exp}`));
}

async function login(req: Request, env: Env, url: URL): Promise<Response> {
  const form = await req.formData();
  const next = safeNext(String(form.get('next') || '/'));
  if (!env.SITE_PASSWORD) return redirect('/login/?e=nopw');
  const ok = await sameSecret(String(form.get('password') || ''), env.SITE_PASSWORD);
  if (!ok) {
    await new Promise((r) => setTimeout(r, 700));
    return redirect(`/login/?e=1&next=${encodeURIComponent(next)}`);
  }
  const exp = Math.floor(Date.now() / 1000) + SESSION_DAYS * 86400;
  const token = `v1.${exp}.${await hmac(env.SITE_PASSWORD, `v1.${exp}`)}`;
  const target = whoFrom(req) ? next : `/who/?next=${encodeURIComponent(next)}`;
  return redirect(target, [cookie(SESSION_COOKIE, token, SESSION_DAYS * 86400)]);
}

async function setWho(req: Request, env: Env, url: URL): Promise<Response> {
  const form = await req.formData();
  const roster: { id: string; name: string }[] = await (await env.ASSETS.fetch(new Request(new URL('/_p/roster.json', url.origin)))).json();
  const pick = String(form.get('who') || '');
  let name = roster.find((v) => v.id === pick)?.name || '';
  if (!name) name = String(form.get('other') || '').replace(/\s+/g, ' ').trim().slice(0, 40);
  const next = safeNext(String(form.get('next') || '/'));
  if (!name) return redirect(`/who/?next=${encodeURIComponent(next)}`);
  return redirect(next, [cookie(WHO_COOKIE, encodeURIComponent(name), 365 * 86400, false)]);
}

function whoFrom(req: Request): string {
  const raw = readCookie(req, WHO_COOKIE);
  if (!raw) return '';
  try {
    return decodeURIComponent(raw).slice(0, 40);
  } catch {
    return '';
  }
}

// ---------- api ----------
async function api(req: Request, env: Env, url: URL, who: string): Promise<Response> {
  const p = url.pathname;
  const m = req.method;

  if (p === '/api/me') return json({ who });
  if (p === '/api/chat' && m === 'POST') {
    if (!who) return json({ error: 'who', message: 'Nejdřív vyberte, kdo se dívá.' }, 400);
    return chat(req, env, who, url.origin);
  }
  if (p === '/api/tokens' || p.startsWith('/api/tokens/')) return tokensApi(req, env, url, who);

  if (p === '/api/comments' && m === 'GET') {
    const doc = url.searchParams.get('doc');
    const stmt = doc
      ? env.DB.prepare('SELECT * FROM comments WHERE deleted = 0 AND doc = ?1 ORDER BY id').bind(doc)
      : env.DB.prepare('SELECT * FROM comments WHERE deleted = 0 ORDER BY id DESC LIMIT 3000');
    const { results } = await stmt.all();
    return json({ comments: results });
  }

  if (p === '/api/comments' && m === 'POST') {
    if (!who) return json({ error: 'who', message: 'Nejdřív vyberte, kdo se dívá.' }, 400);
    const b = (await req.json()) as Record<string, unknown>;
    const doc = String(b.doc || '');
    const body = String(b.body || '').trim();
    if (!/^[a-z0-9-]{1,80}$/.test(doc)) return json({ error: 'doc' }, 400);
    if (!body) return json({ error: 'empty', message: 'Poznámka je prázdná.' }, 400);
    if (body.length > 4000) return json({ error: 'long', message: 'Poznámka je delší než 4000 znaků.' }, 400);
    let parent: number | null = b.parent_id ? Number(b.parent_id) : null;
    let anchor = String(b.anchor || '_doc').slice(0, 200);
    let quote = String(b.quote || '').slice(0, 400);
    if (parent) {
      const root = await env.DB.prepare('SELECT id, anchor, quote, doc FROM comments WHERE id = ?1 AND deleted = 0').bind(parent).first<{ id: number; anchor: string; quote: string; doc: string }>();
      if (!root || root.doc !== doc) return json({ error: 'parent', message: 'Vlákno už neexistuje.' }, 404);
      anchor = root.anchor;
      quote = root.quote;
      await env.DB.prepare('UPDATE comments SET resolved = 0, resolved_by = NULL WHERE id = ?1').bind(parent).run();
    }
    const row = await env.DB.prepare(
      'INSERT INTO comments (doc, anchor, quote, parent_id, author, body) VALUES (?1, ?2, ?3, ?4, ?5, ?6) RETURNING *',
    )
      .bind(doc, anchor, quote, parent, who, body)
      .first();
    return json({ comment: row }, 201);
  }

  const one = p.match(/^\/api\/comments\/(\d+)$/);
  if (one && (m === 'PATCH' || m === 'DELETE')) {
    const id = Number(one[1]);
    const c = await env.DB.prepare('SELECT * FROM comments WHERE id = ?1 AND deleted = 0').bind(id).first<{ author: string; parent_id: number | null }>();
    if (!c) return json({ error: 'missing', message: 'Poznámka už neexistuje.' }, 404);
    if (m === 'DELETE') {
      if (c.author !== who) return json({ error: 'forbidden', message: 'Smazat můžete jen svou poznámku.' }, 403);
      if (!c.parent_id) {
        const others = await env.DB.prepare('SELECT COUNT(*) AS n FROM comments WHERE parent_id = ?1 AND deleted = 0 AND author != ?2').bind(id, who).first<{ n: number }>();
        if (others && others.n > 0) return json({ error: 'replies', message: 'Na poznámku už někdo odpověděl. Označte ji raději jako vyřešenou.' }, 409);
        await env.DB.prepare('UPDATE comments SET deleted = 1 WHERE parent_id = ?1').bind(id).run();
      }
      await env.DB.prepare('UPDATE comments SET deleted = 1 WHERE id = ?1').bind(id).run();
      return json({ ok: true });
    }
    const b = (await req.json()) as Record<string, unknown>;
    if (typeof b.resolved === 'boolean') {
      if (c.parent_id) return json({ error: 'reply', message: 'Vyřešit jde jen celé vlákno.' }, 400);
      await env.DB.prepare('UPDATE comments SET resolved = ?1, resolved_by = ?2, resolved_at = datetime(\'now\') WHERE id = ?3')
        .bind(b.resolved ? 1 : 0, b.resolved ? who : null, id)
        .run();
    }
    if (typeof b.body === 'string') {
      if (c.author !== who) return json({ error: 'forbidden', message: 'Upravit můžete jen svou poznámku.' }, 403);
      const body = b.body.trim();
      if (!body || body.length > 4000) return json({ error: 'body', message: 'Poznámka musí mít 1 až 4000 znaků.' }, 400);
      await env.DB.prepare('UPDATE comments SET body = ?1, edited_at = datetime(\'now\') WHERE id = ?2').bind(body, id).run();
    }
    return json({ comment: await env.DB.prepare('SELECT * FROM comments WHERE id = ?1').bind(id).first() });
  }

  if (p === '/api/view' && m === 'POST') {
    const b = (await req.json()) as Record<string, unknown>;
    const doc = String(b.doc || '');
    if (!who || !/^[a-z0-9-]{1,80}$/.test(doc)) return json({ prev: null });
    const prev = await env.DB.prepare('SELECT last_at FROM views WHERE viewer = ?1 AND doc = ?2').bind(who, doc).first<{ last_at: string }>();
    await env.DB.prepare(
      `INSERT INTO views (viewer, doc) VALUES (?1, ?2)
       ON CONFLICT (viewer, doc) DO UPDATE SET last_at = datetime('now'), count = count + 1`,
    )
      .bind(who, doc)
      .run();
    return json({ prev: prev?.last_at || null });
  }

  if (p === '/api/summary' && m === 'GET') {
    const [open, views, latest] = await env.DB.batch([
      env.DB.prepare('SELECT doc, COUNT(*) AS n FROM comments WHERE deleted = 0 AND resolved = 0 AND parent_id IS NULL GROUP BY doc'),
      env.DB.prepare('SELECT viewer, doc, last_at FROM views ORDER BY last_at DESC'),
      env.DB.prepare('SELECT doc, MAX(created_at) AS at FROM comments WHERE deleted = 0 GROUP BY doc'),
    ]);
    return json({ open: open.results, views: views.results, latest: latest.results, who });
  }

  return json({ error: 'not_found' }, 404);
}

// ---------- helpers ----------
function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });
}

function redirect(location: string, cookies: string[] = []): Response {
  const h = new Headers({ location, 'cache-control': 'no-store' });
  for (const c of cookies) h.append('set-cookie', c);
  return new Response(null, { status: 303, headers: h });
}

function cookie(name: string, value: string, maxAge: number, httpOnly = true): string {
  return `${name}=${value}; Path=/; Max-Age=${maxAge}; Secure; SameSite=Lax${httpOnly ? '; HttpOnly' : ''}`;
}

function readCookie(req: Request, name: string): string | null {
  const all = req.headers.get('cookie') || '';
  for (const part of all.split(/;\s*/)) {
    const i = part.indexOf('=');
    if (i > 0 && part.slice(0, i) === name) return part.slice(i + 1);
  }
  return null;
}

function safeNext(n: string): string {
  return n.startsWith('/') && !n.startsWith('//') && !n.startsWith('/login') ? n : '/';
}

async function asset(env: Env, url: URL, path: string): Promise<Response> {
  const res = await env.ASSETS.fetch(new Request(new URL(path, url.origin)));
  return privateCopy(res);
}

function privateCopy(res: Response): Response {
  const out = new Response(res.body, res);
  out.headers.set('cache-control', 'private, no-cache');
  out.headers.set('x-robots-tag', 'noindex, nofollow');
  out.headers.set('x-frame-options', 'SAMEORIGIN');
  return out;
}
