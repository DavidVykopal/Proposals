# Section text overview ("Shrnutí a hodnocení")

One file per section: `overview/<section-id>.md` (ids from `content.json`). Rendered by `scripts/build.mjs` on the section page under the slide deck, heading "Shrnutí a hodnocení", and indexed for the chatbot/MCP as doc `hodnoceni-<section-id>`. Section `jak-to-funguje` (portal guide) has none.

Audience: leadership and founders. They should understand the proposal, its trade-offs and what it brings in about 2 minutes of reading, without opening the source docs.

## Exact structure (headings verbatim, in this order)

```
## Shrnutí
<1 to 2 short paragraphs, together max ~120 words: what we propose, why, by when.>

## Výhody
- <3 to 5 bullets, max ~20 words each, **bold** key word allowed>

## Nevýhody
- <3 to 5 bullets: costs, trade-offs, what we give up>

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| <3 to 6 rows; Pravděpodobnost and Dopad are one of: nízká, střední, vysoká> |

## Co nám to přinese
- <3 to 5 concrete outcomes; numbers, dates and targets from the sources where they exist>

→ `SOURCE_FILE.md`
```

## Rules

- Czech. No em-dashes or en-dashes as punctuation (use a comma, colon, "až" for ranges, or a new sentence). No emojis. Plain, concrete language, no filler ("klíčový", "zásadní", "robustní").
- Never invent facts, dates, figures or names. Take them from the sources. Where the sources do not name a risk or downside explicitly, it is fine to reason it out as an evaluation, but keep it grounded in what the docs say and mark judgement calls with *(odhad)* if they are numeric.
- Last line: `→ \`FILE.md\`` with the exact basename of the main source doc (becomes a link).
- Confidential: never read or quote `*JMENOVITE*` files or `kalkulacka/vstupy.json`. No individual salaries by name.
