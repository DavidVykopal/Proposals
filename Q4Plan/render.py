#!/usr/bin/env python3
"""Render the Q4Plan meeting markdown into the Delegacni_Navrh visual style.

Usage: python3 render.py   (renders every PORADA_*.md in this folder)
The CSS is taken from ../Delegacni_Navrh/priprava-2026-09-03-role-a-cinnosti.html so both
folders keep one look. Supports the markdown subset these docs use: headings, paragraphs,
blockquote, tables, bullet / numbered / checkbox lists (one nesting level), bold, code.
"""
import html
import re
from pathlib import Path

HERE = Path(__file__).parent
SOURCE_CSS = HERE.parent / "Delegacni_Navrh" / "priprava-2026-09-03-role-a-cinnosti.html"

EXTRA_CSS = """
  .hero { min-height: auto; padding-bottom: 20px; }
  .hero-body { padding-block: 90px 56px; }
  .hero-copy { max-width: 760px; }
  .hero-copy h1 { font-size: clamp(2.3rem, 5.6vw, 4.1rem); }
  .origin code, p code, li code, td code { font-family: ui-monospace, 'SF Mono', Menlo, monospace; font-size: 0.86em; color: var(--gold-dim); }
  .origin { max-width: 46em; line-height: 1.6; }
  .origin p { color: var(--faint); font-size: 0.88rem; max-width: none; }
  .origin p + p { margin-top: 8px; }
  table.wordy td:first-child { color: var(--ink); }
  ul.points li ol { margin: 10px 0 0 0; padding-left: 20px; display: grid; gap: 8px; }
  ul.points li ol li { padding-left: 4px; }
  ul.points li ol li::before { display: none; }
  ul.checks { list-style: none; margin-top: 10px; display: grid; gap: 12px; max-width: 52em; }
  ul.checks li { position: relative; padding-left: 32px; color: var(--muted); font-size: 0.97rem; }
  ul.checks li::before { content: ''; position: absolute; left: 2px; top: 0.3em; width: 14px; height: 14px; border: 1px solid var(--gold-dim); border-radius: 3px; }
  p.label { margin-top: 26px; }
  :root { color-scheme: dark; --muted-2: #8f826e; }
"""


def inline(text: str) -> str:
    parts = re.split(r"(`[^`]+`)", text)
    out = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append(f"<code>{html.escape(p[1:-1])}</code>")
        else:
            e = html.escape(p, quote=False)
            e = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", e)
            out.append(e)
    return "".join(out)


def slug(text: str) -> str:
    m = re.match(r"(\d+)\.", text)
    return f"s{m.group(1)}" if m else re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def render_table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head, body = cells[0], cells[2:]
    wordy = not all(re.fullmatch(r"[A-Z]?\d+|[A-Z]\d*|\d+ min|\d+", r[0] or "x") for r in body)
    cls = ' class="wordy"' if wordy else ""
    h = "".join(f"<th>{inline(c)}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
    return f'<div class="tscroll"><table{cls}><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def render_list(items):
    """items: list of (kind, text, children[]) where kind is 'ul' or 'check'."""
    kind = items[0][0]
    cls = "checks" if kind == "check" else "points"
    out = [f'<ul class="{cls}">']
    for _, text, children in items:
        sub = ""
        if children:
            sub = "<ol>" + "".join(f"<li>{inline(c)}</li>" for c in children) + "</ol>"
        out.append(f"<li>{inline(text)}{sub}</li>")
    out.append("</ul>")
    return "".join(out)


def md_to_body(md: str):
    lines = md.splitlines()
    title = ""
    origin = []
    sections = []  # (h2 text, html)
    cur_h2 = None
    buf = []
    i = 0

    def flush_section():
        if cur_h2 is not None:
            sections.append((cur_h2, "".join(buf)))

    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            title = line[2:].strip()
            i += 1
            continue
        if line.startswith("> ") or line == ">":
            block = []
            while i < len(lines) and (lines[i].startswith(">")):
                block.append(lines[i][1:].strip())
                i += 1
            paras, p = [], []
            for b in block:
                if b:
                    p.append(b)
                elif p:
                    paras.append(" ".join(p))
                    p = []
            if p:
                paras.append(" ".join(p))
            if cur_h2 is None:
                origin.extend(paras)
            else:
                buf.append("".join(f'<div class="pull">{inline(x)}</div>' for x in paras))
            continue
        if line.startswith("## "):
            flush_section()
            cur_h2 = line[3:].strip()
            buf = []
            i += 1
            continue
        if line.startswith("### "):
            buf.append(f"<h3>{inline(line[4:].strip())}</h3>")
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            buf.append(render_table(rows))
            continue
        if re.match(r"- ", line):
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or (lines[i].startswith("  ") and items)):
                l = lines[i]
                if l.startswith("- "):
                    t = l[2:]
                    kind = "ul"
                    if t.startswith("[ ] "):
                        kind, t = "check", t[4:]
                    items.append([kind, t, []])
                else:
                    s = l.strip()
                    if re.match(r"\d+\. ", s):
                        items[-1][2].append(re.sub(r"^\d+\. ", "", s))
                    elif items[-1][2]:
                        items[-1][2][-1] += " " + s
                    else:
                        items[-1][1] += " " + s
                i += 1
            buf.append(render_list(items))
            continue
        if line.strip() in ("", "---"):
            i += 1
            continue
        if line.startswith("```"):
            i += 1
            code = []
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            buf.append(f'<pre class="sheet">{html.escape(chr(10).join(code))}</pre>')
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"(#|\||- |> |```)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        text = " ".join(para)
        cls = ' class="label"' if text.startswith("**") and text.endswith(":**") else ""
        buf.append(f"<p{cls}>{inline(text)}</p>")
    flush_section()
    return title, origin, sections


def build(md_path: Path, out_path: Path, meta: str, related):
    src = SOURCE_CSS.read_text()
    css = src[src.index("<style>") + 7 : src.index("</style>")] + EXTRA_CSS
    title, origin, sections = md_to_body(md_path.read_text())
    main_title, _, date = title.partition(" · ")
    toc = "".join(
        f'<a href="#{slug(h)}"><span>{h.split(".")[0].zfill(2)}</span>{inline(h.split(". ", 1)[-1])}</a>'
        for h, _ in sections
    )
    rows = (len(sections) + 1) // 2
    secs = "".join(
        f'<section id="{slug(h)}"><h2><span class="no">{h.split(".")[0].zfill(2)}</span>{inline(h.split(". ", 1)[-1])}</h2>{body}</section>'
        for h, body in sections
    )
    origin_html = "".join(f"<p>{inline(o)}</p>" for o in origin if not o.startswith("HTML render"))
    rel = "".join(f'<a href="{href}">{html.escape(label)}</a>' for href, label in related)
    doc = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(main_title)} · NOXGAMES</title>
<style>{css}</style>
</head>
<body>
<header class="hero">
  <div class="shell topbar"><span class="wordmark">NOXGAMES</span><span class="meta">{html.escape(meta)}</span></div>
  <div class="shell hero-body">
    <div class="hero-copy">
      <h1>{inline(main_title)}</h1>
      <p class="sub">{inline(date or "")}</p>
      <div class="origin">{origin_html}</div>
    </div>
  </div>
  <nav class="shell toc" style="grid-template-rows: repeat({rows}, auto)">{toc}</nav>
</header>
<main class="shell">{secs}</main>
<footer class="shell">
  <div class="related">{rel}</div>
  <div class="colophon">NOXGAMES · interní podklad pro vedení · render z {html.escape(md_path.name)}</div>
</footer>
</body>
</html>
"""
    out_path.write_text(doc)


PRINT_CSS = """
  :root { --ink: #1d1c1a; --ink-2: #5d5a55; --rule: #c9c4ba; --bg: #fff; --accent: #b4532a; }
  @media screen and (prefers-color-scheme: dark) {
    :root { --ink: #ece8df; --ink-2: #b3ada2; --rule: #3a3833; --bg: #1a1916; --accent: #e59770; color-scheme: dark; }
  }
  @page { size: A4; margin: 13mm 15mm 13mm 16mm; }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--ink); font: 9.6pt/1.4 Georgia, "Times New Roman", serif; }
  .page { max-width: 780px; margin: 0 auto; padding: 32px 16px; }
  header { border-bottom: 1.5pt solid var(--ink); padding-bottom: 8px; margin-bottom: 10px; }
  h1 { font-size: 19pt; font-weight: normal; margin: 0; line-height: 1.15; }
  .meta, .origin { font: 8.8pt/1.45 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; color: var(--ink-2); }
  .origin p { margin: 4px 0 0; }
  h2 { font-size: 12.5pt; margin: 14px 0 4px; break-after: avoid; }
  h2 .no { display: inline-block; min-width: 1.8em; color: var(--ink-2); font-weight: normal; }
  h3 { font-size: 10.3pt; font-style: italic; font-weight: normal; margin: 8px 0 2px; break-after: avoid; }
  p { margin: 3px 0; }
  ul { margin: 2px 0 4px; padding-left: 1.3em; }
  li { margin: 2px 0; break-inside: avoid; }
  li ol { margin: 2px 0; padding-left: 1.4em; }
  strong { font-weight: bold; }
  code { font: 8.5pt ui-monospace, Menlo, monospace; color: var(--ink-2); }
  .tscroll { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; margin: 4px 0 6px; font: 8.6pt/1.35 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
  th { text-align: left; font-weight: 600; border-bottom: 1pt solid var(--ink); padding: 3px 6px 3px 0; }
  td { border-bottom: 0.5pt solid var(--rule); padding: 3px 6px 3px 0; vertical-align: top; }
  tr { break-inside: avoid; }
  .pull { border-left: 2pt solid var(--accent); padding-left: 8px; margin: 4px 0; }
  footer { margin-top: 16px; padding-top: 6px; border-top: 0.75pt solid var(--rule); font: 8pt -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; color: var(--ink-2); }
  @media print { .page { padding: 0; max-width: none; } }
"""


def build_print(md_path: Path, out_path: Path, skip=()):
    title, origin, sections = md_to_body(md_path.read_text())
    main_title, _, date = title.partition(" · ")
    sections = [(h, b) for h, b in sections if not any(k in h for k in skip)]
    b = lambda body: body.replace('class="points"', "").replace('class="checks"', "")
    secs = "".join(
        f'<section><h2><span class="no">{h.split(".")[0]}</span>{inline(h.split(". ", 1)[-1])}</h2>{b(body)}</section>'
        for h, body in sections
    )
    origin_html = "".join(f"<p>{inline(o)}</p>" for o in origin)
    doc = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(main_title)} · tisk</title>
<style>{PRINT_CSS}</style>
</head>
<body><div class="page">
<header><h1>{inline(main_title)}</h1><div class="meta">{inline(date)} · NOXGAMES · interní, vedení</div><div class="origin">{origin_html}</div></header>
{secs}
<footer>Interní podklad pro vedení NOXGAMES · Obsahuje údaje odvozené z odměn, nešířit mimo vedení · Kompletní přepisy: zaznam-2026-09-24-exec-porada.html</footer>
</div></body>
</html>
"""
    out_path.write_text(doc)


if __name__ == "__main__":
    related = [
        ("porada-2026-09-24-q4-plan.html", "Q4 plánování 24. 9."),
        ("porada-2026-10-01-delegace-4.html", "Delegace 4 · 1. 10."),
        ("sector-defense-q3-naklady.html", "Sector Defense: náklady Q3"),
        ("zaznam-2026-09-24-exec-porada.html", "Záznam z porady 24. 9."),
        ("../Delegacni_Navrh/tracker-temat.html", "Tracker témat"),
    ]
    build(HERE / "PORADA_2026-09-24_Q4_PLAN.md", HERE / "porada-2026-09-24-q4-plan.html",
          "Porada vedení · Q4 2026", related)
    build(HERE / "PORADA_2026-10-01_DELEGACE_4.md", HERE / "porada-2026-10-01-delegace-4.html",
          "Delegační porada 4 · segmenty a role", related)
    build(HERE / "ZAZNAM_2026-09-24_EXEC_PORADA.md", HERE / "zaznam-2026-09-24-exec-porada.html",
          "Záznam z porady vedení · Q4 2026", related)
    build_print(HERE / "ZAZNAM_2026-09-24_EXEC_PORADA.md", HERE / "zaznam-2026-09-24-exec-porada-tisk.html",
                skip=("Přepisy",))
    print("rendered")
