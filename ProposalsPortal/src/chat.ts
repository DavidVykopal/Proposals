// In-portal assistant: OpenRouter chat completion with a server-side tool loop over the read-only tools.
import { READ_ONLY_TOOLS, runTool, type Env } from './tools';

const DEFAULT_MODEL = 'anthropic/claude-sonnet-5.5';
const MAX_ROUNDS = 8;

interface Msg {
  role: 'system' | 'user' | 'assistant' | 'tool';
  content: string | null;
  tool_calls?: { id: string; type: 'function'; function: { name: string; arguments: string } }[];
  tool_call_id?: string;
}

export async function chat(req: Request, env: Env, who: string, origin: string): Promise<Response> {
  if (!env.OPENROUTER_API_KEY) return json({ error: 'config', message: 'Asistent není nastavený (chybí OPENROUTER_API_KEY).' }, 503);
  const b = (await req.json()) as { messages?: { role: string; content: string }[]; doc?: string };
  const history = (b.messages || [])
    .filter((m) => (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string' && m.content.trim())
    .slice(-12)
    .map((m) => ({ role: m.role as 'user' | 'assistant', content: m.content.slice(0, 8000) }));
  if (!history.length || history[history.length - 1].role !== 'user') return json({ error: 'empty', message: 'Napište otázku.' }, 400);

  const { results: docs } = await env.DB.prepare('SELECT id, title, section_title, kind FROM docs ORDER BY rowid').all<Record<string, string>>();
  let focus = '';
  if (b.doc) {
    const d = await env.DB.prepare('SELECT id, title, section_title, route, text FROM docs WHERE id = ?1').bind(b.doc).first<Record<string, string>>();
    if (d) focus = `\n\nUživatel má právě otevřený dokument „${d.title}“ (id: ${d.id}, oddíl ${d.section_title}, odkaz ${origin}${d.route}). Otázky typu „tady“, „tento dokument“ se týkají jeho. Celý text (kotvy v hranatých závorkách):\n<document>\n${d.text.slice(0, 60000)}\n</document>`;
  }

  const today = new Date().toLocaleDateString('cs-CZ', { timeZone: 'Europe/Prague' });
  const system = `Jsi asistent interního portálu „Návrhy 2027“ vedení NOXGAMES (mobilní herní studio, Brno). Ptá se ${who}. Dnes je ${today}.

Pravidla:
- Odpovídej česky, stručně a věcně, bez úvodních frází. Odrážky jen tam, kde pomáhají.
- Fakta ber výhradně z podkladů přes nástroje (search_documents, read_document, list_comments). Hledej krátkými klíčovými slovy, zkus i synonyma. Když v podkladech něco není, řekni to rovnou a nevymýšlej.
- Každé číslo, které není doslova převzaté z podkladů, spočítej nástrojem calculate.
- Ke každému podstatnému tvrzení přidej zdroj jako markdown odkaz [název dokumentu](odkaz), kde odkaz je přesná URL z výsledků nástrojů (obsahuje #b=kotva, pokud ji má).
- Podklady se mění, novější dokument nebo zápis z porady má přednost před starším. Když se zdroje rozcházejí, upozorni na to.
- Jmenovité platy v podkladech nejsou a neodhaduj je.
- Měnit dokumenty ani psát poznámky neumíš; na to má každý ikonu poznámky u odstavce nebo vlastní MCP token v Nastavení.

Dokumenty v portálu (id | název | oddíl):
${docs.map((d) => `${d.id} | ${d.title} | ${d.section_title}${d.kind === 'slides' ? ' (rychlý přehled)' : ''}`).join('\n')}${focus}`;

  const messages: Msg[] = [{ role: 'system', content: system }, ...history];
  const tools = READ_ONLY_TOOLS.map((t) => ({ type: 'function', function: { name: t.name, description: t.description, parameters: t.inputSchema } }));
  const model = env.CHAT_MODEL || DEFAULT_MODEL;
  const used: string[] = [];
  let tokensIn = 0;
  let tokensOut = 0;

  for (let round = 0; round < MAX_ROUNDS; round++) {
    const res = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        authorization: `Bearer ${env.OPENROUTER_API_KEY}`,
        'content-type': 'application/json',
        'http-referer': origin,
        'x-title': 'NOXGAMES Navrhy 2027',
      },
      body: JSON.stringify({
        model,
        messages,
        tools,
        tool_choice: round === MAX_ROUNDS - 1 ? 'none' : 'auto',
        max_tokens: 2000,
        temperature: 0.2,
      }),
    });
    if (!res.ok) {
      console.error('openrouter', res.status, await res.text());
      return json({ error: 'llm', message: 'Asistent teď neodpovídá. Zkuste to za chvíli znovu.' }, 502);
    }
    const data = (await res.json()) as any;
    tokensIn += data.usage?.prompt_tokens || 0;
    tokensOut += data.usage?.completion_tokens || 0;
    const msg = data.choices?.[0]?.message;
    if (!msg) return json({ error: 'llm', message: 'Asistent vrátil prázdnou odpověď.' }, 502);

    if (msg.tool_calls?.length) {
      messages.push({ role: 'assistant', content: msg.content || null, tool_calls: msg.tool_calls });
      for (const call of msg.tool_calls) {
        used.push(call.function.name);
        let out: string;
        try {
          out = await runTool(env, call.function.name, JSON.parse(call.function.arguments || '{}'), { who, origin });
        } catch (e) {
          out = `Error: ${(e as Error).message}`;
        }
        messages.push({ role: 'tool', tool_call_id: call.id, content: out.slice(0, 60000) });
      }
      continue;
    }

    const answer = String(msg.content || '').trim() || 'Odpověď se nepodařilo sestavit.';
    await env.DB.prepare('INSERT INTO chat_log (who, scope, question, answer, tools, model, tokens_in, tokens_out) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8)')
      .bind(who, b.doc || 'all', history[history.length - 1].content.slice(0, 4000), answer.slice(0, 8000), used.join(','), model, tokensIn, tokensOut)
      .run()
      .catch(() => {});
    return json({ answer, tools: used });
  }
  return json({ error: 'llm', message: 'Asistent hledal příliš dlouho. Zkuste otázku zúžit.' }, 504);
}

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
}
