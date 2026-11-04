// Remote MCP server (Streamable HTTP, JSON responses) authenticated by personal tokens from /settings/.
import { TOOLS, runTool, type Env } from './tools';

const PROTOCOLS = ['2025-11-25', '2025-06-18', '2025-03-26', '2024-11-05'];

export async function sha256hex(s: string): Promise<string> {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return Array.from(new Uint8Array(d), (b) => b.toString(16).padStart(2, '0')).join('');
}

export async function mcp(req: Request, env: Env, url: URL): Promise<Response> {
  if (req.method !== 'POST') return new Response('Use POST (MCP Streamable HTTP).', { status: 405, headers: { allow: 'POST' } });

  const auth = req.headers.get('authorization') || '';
  const token = auth.match(/^Bearer\s+(npt_[A-Za-z0-9_-]{20,})$/)?.[1];
  const row = token
    ? await env.DB.prepare('SELECT id, owner FROM tokens WHERE token_hash = ?1 AND revoked = 0').bind(await sha256hex(token)).first<{ id: number; owner: string }>()
    : null;
  if (!row) {
    return new Response(JSON.stringify({ jsonrpc: '2.0', id: null, error: { code: -32001, message: 'Missing or invalid token. Create one at /settings/ in the portal.' } }), {
      status: 401,
      headers: { 'content-type': 'application/json', 'www-authenticate': 'Bearer realm="noxgames-navrhy"' },
    });
  }
  await env.DB.prepare("UPDATE tokens SET last_used_at = datetime('now') WHERE id = ?1").bind(row.id).run();

  let body: any;
  try {
    body = await req.json();
  } catch {
    return rpc({ jsonrpc: '2.0', id: null, error: { code: -32700, message: 'Parse error' } });
  }
  const ctx = { who: row.owner, origin: url.origin };
  const handle = async (m: any) => {
    if (!m || m.jsonrpc !== '2.0' || typeof m.method !== 'string') return { jsonrpc: '2.0', id: m?.id ?? null, error: { code: -32600, message: 'Invalid request' } };
    if (m.id === undefined || m.id === null) return null; // notification
    const ok = (result: unknown) => ({ jsonrpc: '2.0', id: m.id, result });
    switch (m.method) {
      case 'initialize': {
        const asked = m.params?.protocolVersion;
        return ok({
          protocolVersion: PROTOCOLS.includes(asked) ? asked : PROTOCOLS[1],
          capabilities: { tools: { listChanged: false } },
          serverInfo: { name: 'noxgames-navrhy', title: 'NOXGAMES Návrhy 2027', version: '1.0.0' },
          instructions:
            `Internal NOXGAMES leadership portal "Návrhy 2027" (Czech). You act as ${row.owner}. ` +
            'Start with list_documents, find passages with search_documents (short Czech keywords, diacritics optional), read with read_document (block anchors in [brackets]). ' +
            'Comments you add or reply to are signed with your name and visible to the whole leadership; write them in Czech, concise, without greetings. ' +
            'Doc "pruvodce" explains how the portal works.',
        });
      }
      case 'ping':
        return ok({});
      case 'tools/list':
        return ok({
          tools: TOOLS.map((t) => ({
            name: t.name,
            title: t.title,
            description: t.description,
            inputSchema: t.inputSchema,
            annotations: { title: t.title, readOnlyHint: !t.write, destructiveHint: false, openWorldHint: false },
          })),
        });
      case 'tools/call': {
        const name = m.params?.name;
        if (!TOOLS.some((t) => t.name === name)) return { jsonrpc: '2.0', id: m.id, error: { code: -32602, message: `Unknown tool ${name}` } };
        try {
          const text = await runTool(env, name, m.params?.arguments || {}, ctx);
          return ok({ content: [{ type: 'text', text }] });
        } catch (e) {
          return ok({ content: [{ type: 'text', text: `Error: ${(e as Error).message}` }], isError: true });
        }
      }
      default:
        return { jsonrpc: '2.0', id: m.id, error: { code: -32601, message: `Method not found: ${m.method}` } };
    }
  };

  if (Array.isArray(body)) {
    const out = (await Promise.all(body.map(handle))).filter(Boolean);
    return out.length ? rpc(out) : new Response(null, { status: 202 });
  }
  const out = await handle(body);
  return out ? rpc(out) : new Response(null, { status: 202 });
}

function rpc(data: unknown): Response {
  return new Response(JSON.stringify(data), { headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
}

export async function tokensApi(req: Request, env: Env, url: URL, who: string): Promise<Response> {
  const json = (d: unknown, s = 200) => new Response(JSON.stringify(d), { status: s, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
  if (!who) return json({ error: 'who', message: 'Nejdřív vyberte, kdo se dívá.' }, 400);
  if (req.method === 'GET') {
    const { results } = await env.DB.prepare('SELECT id, label, prefix, created_at, last_used_at FROM tokens WHERE owner = ?1 AND revoked = 0 ORDER BY id DESC').bind(who).all();
    return json({ tokens: results, who });
  }
  if (req.method === 'POST') {
    const b = (await req.json().catch(() => ({}))) as { label?: string };
    const bytes = crypto.getRandomValues(new Uint8Array(32));
    const token = 'npt_' + btoa(String.fromCharCode(...bytes)).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    const label = String(b.label || '').trim().slice(0, 60) || 'Token';
    await env.DB.prepare('INSERT INTO tokens (owner, label, prefix, token_hash) VALUES (?1, ?2, ?3, ?4)').bind(who, label, token.slice(0, 10), await sha256hex(token)).run();
    return json({ token, label }, 201);
  }
  const m = url.pathname.match(/^\/api\/tokens\/(\d+)$/);
  if (req.method === 'DELETE' && m) {
    const r = await env.DB.prepare('UPDATE tokens SET revoked = 1 WHERE id = ?1 AND owner = ?2').bind(Number(m[1]), who).run();
    return r.meta.changes ? json({ ok: true }) : json({ error: 'missing', message: 'Token nenalezen.' }, 404);
  }
  return json({ error: 'not_found' }, 404);
}
