// Document + comment tools shared by the in-portal chatbot (/api/chat) and the MCP server (/mcp).
export interface Env {
  ASSETS: Fetcher;
  DB: D1Database;
  SITE_PASSWORD?: string;
  OPENROUTER_API_KEY?: string;
  CHAT_MODEL?: string;
}

export interface ToolCtx {
  who: string;
  origin: string;
}

interface ToolDef {
  name: string;
  title: string;
  description: string;
  write?: boolean;
  inputSchema: Record<string, unknown>;
}

const obj = (properties: Record<string, unknown>, required: string[] = []) => ({ type: 'object', properties, required, additionalProperties: false });

export const TOOLS: ToolDef[] = [
  {
    name: 'list_documents',
    title: 'Seznam podkladů',
    description: 'Lists all sections and documents of the NOXGAMES "Návrhy 2027" portal (delegation plan, production strategy 2027, PvP, City V2, NoxEngine, external designers, CPI tests) with ids, titles, links and open comment counts. Each section also has a "prehled-<section>" quick-overview slide deck and a "hodnoceni-<section>" text summary with pros, cons, risks and expected outcome.',
    inputSchema: obj({}),
  },
  {
    name: 'search_documents',
    title: 'Hledat v podkladech',
    description: 'Full-text search over all documents and quick-overview slides (Czech, diacritics-insensitive, prefix match). Returns matching passages with doc id, anchor, heading, snippet and a deep link. Use several short keyword queries (2-4 words) rather than one long sentence; try synonyms if nothing is found.',
    inputSchema: obj({
      query: { type: 'string', description: 'Keywords, e.g. "fake PvP boti" or "rozpočet segment"' },
      doc: { type: 'string', description: 'Optional doc id to search only inside one document' },
      limit: { type: 'integer', minimum: 1, maximum: 25, description: 'Max results, default 8' },
    }, ['query']),
  },
  {
    name: 'read_document',
    title: 'Přečíst dokument',
    description: 'Returns the full text of one document. Every block starts with its anchor in square brackets, e.g. "[p-1flvls4]", which can be used for deep links (#b=<anchor>) and for add_comment. Long documents are paged with offset.',
    inputSchema: obj({
      doc: { type: 'string', description: 'Doc id from list_documents or search_documents' },
      offset: { type: 'integer', minimum: 0, description: 'Character offset for paging, default 0' },
    }, ['doc']),
  },
  {
    name: 'list_comments',
    title: 'Poznámky',
    description: 'Lists comment threads (feedback from leadership) with thread ids, the quoted passage, author, replies and status.',
    inputSchema: obj({
      doc: { type: 'string', description: 'Optional doc id' },
      status: { type: 'string', enum: ['open', 'resolved', 'all'], description: 'Default open' },
      author: { type: 'string', description: 'Optional author name, e.g. "Jirka"' },
    }),
  },
  {
    name: 'add_comment',
    title: 'Přidat poznámku',
    write: true,
    description: 'Adds a new comment thread in the name of the token owner. Attach it to a passage with `anchor` (from read_document / search_documents), or pass `quote` with a short exact phrase from the passage and the server finds it. Without both, the comment applies to the whole document.',
    inputSchema: obj({
      doc: { type: 'string' },
      body: { type: 'string', description: 'Comment text (Czech preferred), max 4000 chars' },
      anchor: { type: 'string' },
      quote: { type: 'string', description: 'Exact phrase from the passage, used to find the anchor' },
    }, ['doc', 'body']),
  },
  {
    name: 'reply_comment',
    title: 'Odpovědět na poznámku',
    write: true,
    description: 'Replies to an existing comment thread in the name of the token owner. Reopens the thread if it was resolved.',
    inputSchema: obj({ thread_id: { type: 'integer' }, body: { type: 'string' } }, ['thread_id', 'body']),
  },
  {
    name: 'resolve_comment',
    title: 'Vyřešit vlákno',
    write: true,
    description: 'Marks a comment thread as resolved (or reopens it with resolved=false).',
    inputSchema: obj({ thread_id: { type: 'integer' }, resolved: { type: 'boolean' } }, ['thread_id']),
  },
  {
    name: 'calculate',
    title: 'Kalkulačka',
    description: 'Evaluates an arithmetic expression exactly. Supports + - * / % ^, parentheses, and round(x, digits), min(), max(), sqrt(), abs(). Use a dot as the decimal separator. Use it for any number you report that is not copied verbatim from a document.',
    inputSchema: obj({ expression: { type: 'string', description: 'e.g. "(110000 * 12) * 1.338" or "round(5/16*100, 1)"' } }, ['expression']),
  },
];

export const READ_ONLY_TOOLS = TOOLS.filter((t) => !t.write);

const link = (ctx: ToolCtx, route: string, anchor?: string) =>
  `${ctx.origin}${route}${anchor && anchor !== '_doc' ? (anchor.startsWith('s') && /^s\d+$/.test(anchor) ? `#${anchor}` : `#b=${anchor}`) : ''}`;

export async function runTool(env: Env, name: string, args: Record<string, unknown>, ctx: ToolCtx): Promise<string> {
  const a = args || {};
  switch (name) {
    case 'list_documents': {
      const [{ results: docs }, { results: open }] = await env.DB.batch([
        env.DB.prepare('SELECT id, title, section, section_title, route, kind, modified, summary FROM docs ORDER BY rowid'),
        env.DB.prepare('SELECT doc, COUNT(*) AS n FROM comments WHERE deleted = 0 AND resolved = 0 AND parent_id IS NULL GROUP BY doc'),
      ]);
      const openBy = Object.fromEntries((open as { doc: string; n: number }[]).map((r) => [r.doc, r.n]));
      const out: string[] = [];
      let sec = '';
      for (const d of docs as Record<string, string>[]) {
        if (d.section !== sec) {
          sec = d.section;
          out.push(`\n## ${d.section_title} (section: ${d.section})\n${d.summary || ''}`);
        }
        const kind = d.kind === 'slides' ? 'quick-overview slides' : d.kind === 'overview' ? 'section summary and evaluation' : d.kind === 'html' ? 'presentation/page' : 'document';
        out.push(`- ${d.title} | id: ${d.id} | ${kind} | updated ${String(d.modified).slice(0, 10)} | open comments: ${openBy[d.id] || 0} | ${link(ctx, d.route)}`);
      }
      return out.join('\n').trim();
    }

    case 'search_documents': {
      const words = String(a.query || '').toLowerCase().match(/[\p{L}\p{N}]+/gu)?.filter((w) => w.length > 1).slice(0, 12) || [];
      if (!words.length) throw new Error('Empty query.');
      const match = words.map((w) => `"${w.replace(/"/g, '')}"*`).join(' OR ');
      const limit = Math.min(Math.max(Number(a.limit) || 8, 1), 25);
      const doc = a.doc ? String(a.doc) : null;
      const sql = `SELECT chunks.doc AS doc, chunks.anchor AS anchor, chunks.heading AS heading,
          snippet(chunks, 3, '«', '»', '…', 32) AS snip, docs.title AS title, docs.route AS route
        FROM chunks JOIN docs ON docs.id = chunks.doc
        WHERE chunks MATCH ?1 ${doc ? 'AND chunks.doc = ?3' : ''}
        ORDER BY bm25(chunks, 0, 0, 2.0, 1.0) LIMIT ?2`;
      const stmt = doc ? env.DB.prepare(sql).bind(match, limit, doc) : env.DB.prepare(sql).bind(match, limit);
      const { results } = await stmt.all<Record<string, string>>();
      if (!results.length) return `No results for "${a.query}". Try other keywords or synonyms.`;
      return results
        .map((r, i) => `${i + 1}. ${r.title} (doc: ${r.doc}, anchor: ${r.anchor})${r.heading && r.heading !== r.title ? ` · ${r.heading}` : ''}\n   ${r.snip}\n   ${link(ctx, r.route, r.anchor)}`)
        .join('\n');
    }

    case 'read_document': {
      const d = await env.DB.prepare('SELECT * FROM docs WHERE id = ?1').bind(String(a.doc || '')).first<Record<string, string>>();
      if (!d) throw new Error(`Unknown doc "${a.doc}". Use list_documents.`);
      const offset = Math.max(Number(a.offset) || 0, 0);
      const PAGE = 45000;
      const part = d.text.slice(offset, offset + PAGE);
      const more = offset + PAGE < d.text.length;
      return `# ${d.title}\nSection: ${d.section_title} · id: ${d.id} · updated ${String(d.modified).slice(0, 10)} · ${link(ctx, d.route)}\n` +
        (d.kind === 'md' ? 'Block anchors in [brackets]; deep link = page URL + #b=<anchor>.\n' : '') +
        `\n${part}` +
        (more ? `\n\n[… truncated, ${d.text.length - offset - PAGE} more characters. Call read_document again with offset=${offset + PAGE}.]` : '');
    }

    case 'list_comments': {
      const status = String(a.status || 'open');
      const where = ['c.deleted = 0', 'c.parent_id IS NULL'];
      const binds: unknown[] = [];
      if (a.doc) { binds.push(String(a.doc)); where.push(`c.doc = ?${binds.length}`); }
      if (status === 'open') where.push('c.resolved = 0');
      if (status === 'resolved') where.push('c.resolved = 1');
      const { results: roots } = await env.DB.prepare(
        `SELECT c.*, d.title AS doc_title, d.route AS route FROM comments c LEFT JOIN docs d ON d.id = c.doc WHERE ${where.join(' AND ')} ORDER BY c.id DESC LIMIT 200`,
      ).bind(...binds).all<Record<string, any>>();
      const ids = roots.map((r) => r.id);
      const replies = ids.length
        ? (await env.DB.prepare(`SELECT * FROM comments WHERE deleted = 0 AND parent_id IN (${ids.map(() => '?').join(',')}) ORDER BY id`).bind(...ids).all<Record<string, any>>()).results
        : [];
      let threads = roots.map((r) => ({ r, reps: replies.filter((x) => x.parent_id === r.id) }));
      if (a.author) {
        const au = String(a.author).toLowerCase();
        threads = threads.filter((t) => t.r.author.toLowerCase() === au || t.reps.some((x) => x.author.toLowerCase() === au));
      }
      if (!threads.length) return 'No comment threads match.';
      return threads
        .map(({ r, reps }) =>
          [`Thread #${r.id} · ${r.doc_title || r.doc} (doc: ${r.doc}) · ${r.resolved ? `resolved by ${r.resolved_by}` : 'open'} · ${link(ctx, r.route || '/', r.anchor)}`,
            `  On: ${r.anchor === '_doc' ? '(whole document)' : `"${r.quote}"`}`,
            ...[r, ...reps].map((c) => `  - ${c.author} (${String(c.created_at).slice(0, 16)}): ${c.body}`)].join('\n'))
        .join('\n\n');
    }

    case 'add_comment': {
      const doc = String(a.doc || '');
      const body = String(a.body || '').trim();
      if (!body || body.length > 4000) throw new Error('Body must be 1 to 4000 characters.');
      const d = await env.DB.prepare('SELECT id, title, route, kind FROM docs WHERE id = ?1').bind(doc).first<Record<string, string>>();
      if (!d || d.kind === 'slides' || d.kind === 'overview') throw new Error(`Unknown or non-commentable doc "${doc}". Comment on the underlying document instead.`);
      let anchor = a.anchor ? String(a.anchor) : '';
      let quote = '';
      if (anchor && anchor !== '_doc') {
        const c = await env.DB.prepare('SELECT text FROM chunks WHERE doc = ?1 AND anchor = ?2 LIMIT 1').bind(doc, anchor).first<{ text: string }>();
        if (!c) throw new Error(`Anchor "${anchor}" not found in ${doc}. Use read_document to get valid anchors.`);
        quote = c.text;
      } else if (a.quote) {
        const q = String(a.quote).trim();
        const c = await env.DB.prepare("SELECT anchor, text FROM chunks WHERE doc = ?1 AND anchor != '_doc' AND instr(lower(text), lower(?2)) > 0 LIMIT 1").bind(doc, q).first<{ anchor: string; text: string }>();
        if (c) { anchor = c.anchor; quote = c.text; } else { anchor = '_doc'; quote = q; }
      } else anchor = '_doc';
      const row = await env.DB.prepare('INSERT INTO comments (doc, anchor, quote, author, body) VALUES (?1, ?2, ?3, ?4, ?5) RETURNING id')
        .bind(doc, anchor || '_doc', quote.slice(0, 400), ctx.who, body).first<{ id: number }>();
      return `Comment thread #${row!.id} added by ${ctx.who} on "${d.title}"${anchor === '_doc' ? ' (whole document)' : ` at ${anchor}`}. ${link(ctx, d.route, anchor)}`;
    }

    case 'reply_comment': {
      const id = Number(a.thread_id);
      const body = String(a.body || '').trim();
      if (!body || body.length > 4000) throw new Error('Body must be 1 to 4000 characters.');
      const root = await env.DB.prepare('SELECT * FROM comments WHERE id = ?1 AND deleted = 0 AND parent_id IS NULL').bind(id).first<Record<string, any>>();
      if (!root) throw new Error(`Thread #${id} not found.`);
      await env.DB.batch([
        env.DB.prepare('INSERT INTO comments (doc, anchor, quote, parent_id, author, body) VALUES (?1, ?2, ?3, ?4, ?5, ?6)').bind(root.doc, root.anchor, root.quote, id, ctx.who, body),
        env.DB.prepare('UPDATE comments SET resolved = 0, resolved_by = NULL WHERE id = ?1').bind(id),
      ]);
      return `Reply added by ${ctx.who} to thread #${id}.`;
    }

    case 'resolve_comment': {
      const id = Number(a.thread_id);
      const resolved = a.resolved !== false;
      const r = await env.DB.prepare("UPDATE comments SET resolved = ?1, resolved_by = ?2, resolved_at = datetime('now') WHERE id = ?3 AND parent_id IS NULL AND deleted = 0")
        .bind(resolved ? 1 : 0, resolved ? ctx.who : null, id).run();
      if (!r.meta.changes) throw new Error(`Thread #${id} not found.`);
      return `Thread #${id} ${resolved ? 'resolved' : 'reopened'} by ${ctx.who}.`;
    }

    case 'calculate': {
      const expr = String(a.expression || '');
      const v = calc(expr);
      return `${expr} = ${Number.isInteger(v) ? v : +v.toPrecision(12)}`;
    }
  }
  throw new Error(`Unknown tool ${name}`);
}

// Small safe arithmetic parser (no eval).
export function calc(src: string): number {
  const s = src.replace(/\s+/g, '').replace(/×/g, '*').replace(/÷/g, '/');
  let i = 0;
  const peek = () => s[i];
  const fail = (m: string): never => { throw new Error(`Cannot evaluate "${src}": ${m}`); };
  const FN: Record<string, (...x: number[]) => number> = {
    round: (x, d = 0) => Math.round(x * 10 ** d) / 10 ** d,
    min: Math.min, max: Math.max, sqrt: Math.sqrt, abs: Math.abs, floor: Math.floor, ceil: Math.ceil,
  };
  function expr(): number {
    let v = term();
    while (peek() === '+' || peek() === '-') v = s[i++] === '+' ? v + term() : v - term();
    return v;
  }
  function term(): number {
    let v = power();
    while (peek() === '*' || peek() === '/' || peek() === '%') {
      const op = s[i++];
      const r = power();
      v = op === '*' ? v * r : op === '/' ? v / r : v % r;
    }
    return v;
  }
  function power(): number {
    const b = unary();
    if (peek() === '^') { i++; return b ** power(); }
    return b;
  }
  function unary(): number {
    if (peek() === '-') { i++; return -unary(); }
    if (peek() === '+') { i++; return unary(); }
    return atom();
  }
  function atom(): number {
    if (peek() === '(') { i++; const v = expr(); if (s[i++] !== ')') fail('missing )'); return v; }
    const fm = s.slice(i).match(/^[a-z]+/);
    if (fm) {
      const f = FN[fm[0]] || fail(`unknown function ${fm[0]}`);
      i += fm[0].length;
      if (s[i++] !== '(') fail('expected (');
      const argv: number[] = [];
      if (peek() !== ')') { argv.push(expr()); while (peek() === ',') { i++; argv.push(expr()); } }
      if (s[i++] !== ')') fail('missing )');
      return f(...argv);
    }
    const m = s.slice(i).match(/^\d+(\.\d+)?(e[+-]?\d+)?/i);
    if (!m) fail(`unexpected "${peek() ?? 'end'}" at ${i}`);
    i += m![0].length;
    return parseFloat(m![0]);
  }
  const v = expr();
  if (i < s.length) fail(`unexpected "${s[i]}" at ${i}`);
  if (!Number.isFinite(v)) fail('result is not finite');
  return v;
}
