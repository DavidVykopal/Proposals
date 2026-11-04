# Slide format (quick overview decks)

One file per section: `slides/<section-id>.md` (ids from `content.json`). Rendered by `scripts/build.mjs` into the 16:9 "Rychlý přehled" deck on the section page and in the chatbot/MCP index.

## Rules

- Slides are separated by a line containing only `---`.
- 5 to 8 slides per file. A leader should grasp the whole proposal in under 3 minutes.
- Czech. No em-dashes or en-dashes as punctuation (use a comma, colon or new sentence). No emojis. Numbers and names exactly as in the sources; never invent facts, dates or figures.
- First slide: `# <Proposal title>`, one lead sentence (max 160 chars), then 2 to 4 stat lines.
- Every other slide starts with `## <Title>` (max 60 chars, a statement, not a label: "PvP spouštíme nejdřív proti botům", not "PvP").
- Body of a slide is ONE of:
  - a lead sentence (optional, max 160 chars) + 3 to 5 bullets (`- `), each max 90 chars, `**bold**` allowed for the key word;
  - 2 to 4 stat lines: `!! <value> | <label>` (value short: `5`, `40/120/440K`, `XII 2026`, `50 %`; label max 40 chars);
  - a small table (max 5 rows, max 4 columns, short cells).
- Optional last line of a slide: `→ \`SOURCE_FILE.md\`` (the exact file name of the source doc in backticks; it becomes a link to that doc in the portal).
- Last slide: `## Co je potřeba rozhodnout` (or `## Další kroky` if nothing is open) with the open questions / next steps, owners and dates where the sources give them.

## Example

```
# PvP v Hexu
Hexapolis dostane PvP a silnou sociální vrstvu, nejdřív s boty, postupně se skutečnými hráči.
!! I 2027 | první hráči v původním Hexu
!! 3–5 | prvních zápasů vždy proti botům
---
## Proč PvP: monetizace bez stropu
- Dnes jsou všechny hry **PvE**, hráč soutěží jen se hrou
- Chybí segment hráčů, kteří utrácejí, aby předehnali jiné
- PvP otevírá model Rise of Kingdoms a Clash of Clans
→ `DESIGN_HEX_PVP.md`
```
