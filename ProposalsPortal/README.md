# Návrhy 2027 · proposals portal

Password-protected Cloudflare Worker that shows all end-of-year proposals (delegation, strategy 2027, PvP, City V2, NoxEngine, external designers, CPI) with cross-links and block-level comments.

- Live: https://noxgames-proposals.studio-0b0.workers.dev
- Worker `noxgames-proposals`, D1 `noxgames-proposals` (account studio@noxgames.com)
- Source of truth stays in the Markdown/HTML files elsewhere in `_PROPOSALS/` (and `Experiments/NoxEngine/docs`). The portal is rebuilt from them on every deploy.

## Commands (run in this folder)

| Command | What it does |
|---|---|
| `npm run cf:deploy` | Build `dist/` from `content.json`, deploy to production, reload the search index (`cf:index`) |
| `npm run cf:index` | Reload only the chatbot/MCP search index from `build/index.sql` into D1 |
| `npm run feedback` | Pull open comment threads from production into `FEEDBACK.md` (`-- --all` includes resolved) |
| `npm run cf:preview` | Build + local `wrangler dev` (needs `.dev.vars` with `SITE_PASSWORD=...`) |
| `npm run cf:migrate` | Apply D1 migrations in `migrations/` to production |
| `npx wrangler secret put SITE_PASSWORD` | Set or change the shared password (changing it logs everyone out) |
| `npx wrangler secret put OPENROUTER_API_KEY` | OpenRouter key for the chatbot; model is `vars.CHAT_MODEL` in `wrangler.jsonc` |

## Adding or changing content

Edit `content.json`: sections are the numbered dividers (01, 02, ...), `docs` are the pages inside a section.

```json
{ "src": "../Strategie_Produkce/DESIGN_HEX_PVP.md", "title": "Design dokument PvP", "group": "Design" }
{ "src": "../CPI_Tests/foo.html", "title": "...", "assets": ["assets", "prototype.html"] }
```

- `src` is relative to this folder. `.md` is rendered; `.html` is shown as a showcase in an iframe.
- `assets` lists files/folders next to an HTML showcase that it needs. Only listed files are copied; folders are never copied wholesale.
- `title` is optional for Markdown (first `# H1` is used). `group` groups docs in the section sub-nav.
- A section with `"docs": []` shows as "připravuje se".
- Then `npm run cf:deploy`.

## Chapter 00, quick-overview slides

- `docs/PRUVODCE.md` is chapter 00 "Jak portál funguje": the user + AI-agent guide to the portal (login, comments, assistant, MCP setup, agent rules). Update it whenever a feature changes; the chatbot and MCP answer "how do I…" questions from it.
- Each section page shows a summary, then a 16:9 "Rychlý přehled" deck from `slides/<section-id>.md` (format and rules in `slides/FORMAT.md`), then the docs. Slides deep-link as `/<section>/#s3`.

## Chatbot and MCP (RAG)

- Build writes `build/index.sql`: table `docs` (full text with `[anchor]` per block) and FTS5 table `chunks` (one row per block, `unicode61 remove_diacritics 2`). Slides are indexed as doc `prehled-<section>`.
- Anchors are assigned at build time in `scripts/build.mjs` (`data-anchor` on every block) and shared by the page, comments, chatbot and MCP.
- `/api/chat` (`src/chat.ts`): OpenRouter tool loop over the read-only tools in `src/tools.ts` (search, read, list comments, calculate). Scope = current doc or everything. Every Q/A is logged to `chat_log`.
- `/mcp` (`src/mcp.ts`): remote MCP server, Streamable HTTP with JSON responses, bearer token from `/settings/` (stored as SHA-256 in `tokens`, bound to the viewer name). Tools: the read-only set + `add_comment`, `reply_comment`, `resolve_comment`, signed with the token owner's name.
- Connect: `claude mcp add --transport http noxgames-navrhy https://noxgames-proposals.studio-0b0.workers.dev/mcp --header "Authorization: Bearer npt_..."`

## Linking between pages

- Markdown links to another doc in `content.json` (`[text](../Strategie_Produkce/DESIGN_CITY_V2.md#heading)`) become portal links.
- An inline code mention of a doc file name (`` `DESIGN_HEX_PVP.md` ``) is auto-linked with the doc title.
- `[[DESIGN_HEX_PVP]]` or `[[DESIGN_HEX_PVP|custom text]]` wiki links work too.
- Links between HTML showcases (e.g. `prototype.html`) are rewritten to the portal route when the target is in `content.json`.
- Every block has a link button (hover the paragraph): `/<section>/<doc>/#b=<anchor>`. Comment links use `#c=<id>`.

## How comments work

- Login = one shared password (HMAC-signed cookie, 30 days). Then "Kdo se dívá" sets a name cookie (`np_who`); the roster lives in `content.json` → `viewers`. The name is attribution, not security.
- A comment is anchored to a block by `tag + FNV hash of its text + occurrence index` (computed client-side in `static/portal.js`, same algorithm for Markdown and showcases). If the text of a block changes, its comments move to "Text se mezitím změnil" with the original quote. That is expected after a revision.
- Markdown docs: comments align in the right margin next to their block (desktop), bottom sheet on mobile. Showcases: "Komentovat části" toggles pick mode, then click an element in the deck.
- Present mode on Markdown docs: `P` or the button, arrow keys jump between H2 chapters, `Esc` exits.
- D1 tables: `comments` (soft delete, `resolved`, replies via `parent_id`) and `views` (who read which doc, used for "Četli" and "nové" badges).

## Gotchas

- Confidential files are hard-blocked in `scripts/build.mjs` (`BLOCKLIST`: the per-name pay model and `kalkulacka/vstupy.json`). Build fails if `content.json` references them.
- Workers assets serves `x.html` as `/x` (auto trailing slash). Do not hardcode `.html` URLs for raw showcases in code that compares paths.
- Everything except `/_p/*` (CSS, JS, fonts, logo, login/who pages) is behind the session check, including raw decks.
- `dist/`, `build/` and `manifest.local.json` are build output (gitignored).
- `wrangler dev` does not pick up a rebuilt `dist/`; restart it after `npm run build`.
- After editing source docs, deploy with `npm run cf:deploy` (not plain `wrangler deploy`), otherwise the chatbot/MCP index stays stale.
