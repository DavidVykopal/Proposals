# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Cloudflare Worker (TypeScript) serving prebuilt static pages through the Workers assets binding, D1 for comments and view tracking. Markdown is rendered to HTML at build time by `scripts/build.mjs` from the source docs that live elsewhere in `_PROPOSALS/` (and `Experiments/NoxEngine/docs`). No frontend framework.

## Users

NOXGAMES leadership and founders: Jirka (CEO), DJ (Martin B., Operations), Kuba (Marketing), Mirek and Peko (co-founders), and David (Produkce, author of the proposals). Occasional guests are possible through a free-text name.

Two situations, equally important:
- **Live meeting:** David presents on a shared screen, one document or deck at a time, people react in the room.
- **Async review:** each person reads on their own (laptop, sometimes phone) before or after a meeting and leaves feedback on specific passages.

## Product Purpose

One place for all end-of-year proposals (delegation plan, production strategy 2027, PvP and City V2 design docs, NoxEngine + Warcamp, external designers review, themes and CPI tests). Success: every leader has read what concerns them, feedback lands on the exact passage it is about, and David can pull all feedback back into the source Markdown for the next revision.

## Positioning

Not a wiki and not a slide tool. The source of truth stays in Markdown in the repo; the portal is the readable, commentable face of it, rebuilt on every deploy. Feedback is anchored to blocks of text and exportable for revision.

## Operating Context

- Source docs are Czech Markdown (tables, lists, headings) and standalone HTML decks (1920x1080 stage decks, review pages).
- Leadership meets biweekly on Thursdays; proposals get revised between meetings.
- Feedback loop: comments in D1 → `npm run feedback` → `FEEDBACK.md` → David revises MD → `npm run cf:deploy`.

## Capabilities and Constraints

- One shared password (Worker secret `SITE_PASSWORD`), then a "Kdo se dívá" picker (fixed roster + free text). The name is not authentication, only attribution.
- Documents link to each other; any block has a shareable link.
- Comments attach to blocks (paragraph, list item, heading, table, slide element), support replies, resolve, delete own.
- Sections may exist before their content does ("připravuje se").
- Confidential per-name pay data (`ODMENOVANI_2027_MODEL_JMENOVITE.md`, `kalkulacka/vstupy.json`) must never be included.
- UI language Czech, code English.

## Brand Commitments

NOXGAMES, one word, all caps. Logo `Strategie_Produkce/assets/noxgames-logo.png`. The Q4 kickoff visual system (navy ground, cyan accent, Montserrat display, Inter text, person colours David blue / DJ teal / Jirka violet / Kuba orange) is the incumbent leadership-presentation identity.

## Evidence on Hand

All content is real and in the repo; nothing to fabricate. Sections without docs yet are shown as planned, not filled with placeholder prose.

## Product Principles

1. The document is the hero; chrome stays out of the way.
2. Feedback must point at something specific.
3. MD in the repo stays the source of truth; the portal never becomes a second copy to maintain by hand.
4. Works in the meeting room and on a phone in a hallway.

## Accessibility & Inclusion

Keyboard reachable comment flow, AA contrast, 16px minimum body text on mobile, 44px touch targets.
