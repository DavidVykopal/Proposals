// Builds dist/ from content.json: renders Markdown docs, copies listed HTML showcases + their assets.
// Only files named in content.json are copied, never whole folders.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { Marked, Renderer } from 'marked';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(ROOT, 'dist');
const cfg = JSON.parse(fs.readFileSync(path.join(ROOT, 'content.json'), 'utf8'));
const BLOCKLIST = [/JMENOVITE/i, /kalkulacka\/vstupy\.json/i];

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
const slugify = (s) =>
  s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'x';
const pad = (n) => String(n).padStart(2, '0');
const fmtDate = (d) => `${d.getDate()}. ${d.getMonth() + 1}. ${d.getFullYear()}`;
// Block anchors: tag + FNV-1a(base36) of the block's plain text + occurrence index. Computed here, read by the client and the MCP.
const fnv = (str) => {
  let h = 0x811c9dc5;
  for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 0x01000193); }
  return (h >>> 0).toString(36);
};
const ENT = { amp: '&', lt: '<', gt: '>', quot: '"', '#39': "'", nbsp: ' ', apos: "'" };
const htmlToText = (html) =>
  String(html)
    .replace(/<(script|style)[\s\S]*?<\/\1>/gi, ' ')
    .replace(/<br\s*\/?>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&(#\d+|#x[0-9a-f]+|\w+);/gi, (m, e) => (ENT[e] ?? (e[0] === '#' ? String.fromCodePoint(e[1] === 'x' ? parseInt(e.slice(2), 16) : +e.slice(1)) : m)))
    .replace(/\s+/g, ' ')
    .trim();

function modified(file) {
  const dir = path.dirname(file);
  try {
    const dirty = execFileSync('git', ['-C', dir, 'status', '--porcelain', '--', file], { encoding: 'utf8' }).trim();
    if (!dirty) {
      const iso = execFileSync('git', ['-C', dir, 'log', '-1', '--format=%cI', '--', file], { encoding: 'utf8' }).trim();
      if (iso) return new Date(iso);
    }
  } catch {}
  return fs.statSync(file).mtime;
}

function copyInto(src, dest) {
  const st = fs.statSync(src);
  if (st.isDirectory()) {
    fs.mkdirSync(dest, { recursive: true });
    for (const f of fs.readdirSync(src)) {
      if (f === '.DS_Store') continue;
      copyInto(path.join(src, f), path.join(dest, f));
    }
  } else {
    if (BLOCKLIST.some((re) => re.test(src))) throw new Error(`Refusing to copy confidential file ${src}`);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(src, dest);
  }
}

// ---------- collect docs ----------
let nextNum = 1;
const sections = cfg.sections.map((s) => ({ ...s, num: s.num || pad(nextNum++), route: `/${s.id}/` }));
const docs = [];
const bySrc = new Map();
const seenIds = new Set();
for (const s of sections) {
  s.docList = [];
  for (const d of s.docs) {
    const abs = path.resolve(ROOT, d.src);
    if (BLOCKLIST.some((re) => re.test(abs))) throw new Error(`Confidential doc in content.json: ${d.src}`);
    if (!fs.existsSync(abs)) throw new Error(`Missing source: ${d.src}`);
    const ext = path.extname(abs).toLowerCase();
    let id = slugify(path.basename(abs, ext));
    if (id === 'index') id = slugify(d.title || s.id);
    while (seenIds.has(id)) id += '-2';
    seenIds.add(id);
    const doc = {
      ...d, abs, id, section: s, kind: ext === '.md' ? 'md' : 'html',
      route: `/${s.id}/${id}/`, modified: modified(abs),
    };
    docs.push(doc);
    s.docList.push(doc);
    bySrc.set(abs, doc);
  }
}

// ---------- markdown ----------
function resolveLink(href, fromFile) {
  if (!href || /^(https?:|mailto:|#|\/)/i.test(href)) return null;
  const [p, hash] = href.split('#');
  if (!/\.(md|html?)$/i.test(p)) return null;
  const target = bySrc.get(path.resolve(path.dirname(fromFile), decodeURI(p)));
  return target ? target.route + (hash ? `#${hash}` : '') : 'missing';
}

function wikiLinks(md) {
  return md.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (m, name, label) => {
    const key = name.trim().toLowerCase();
    const t = docs.find((d) => path.basename(d.abs, path.extname(d.abs)).toLowerCase() === key || (d.title || '').toLowerCase() === key || d.id === slugify(name));
    return t ? `[${label || t.title || name}](${t.route})` : label || name;
  });
}

function renderMd(doc) {
  let src = fs.readFileSync(doc.abs, 'utf8').replace(/^---\n[\s\S]*?\n---\n/, '');
  const h1 = src.match(/^#\s+(.+)$/m);
  if (!doc.title) doc.title = h1 ? h1[1].trim() : doc.id;
  if (h1 && src.trimStart().startsWith(h1[0])) src = src.replace(h1[0], '');
  src = wikiLinks(src);
  const ids = new Map();
  const toc = [];
  const counts = new Map();
  const blocks = [];
  let liDepth = 0;
  let heading = doc.title;
  const addBlock = (tag, html) => {
    const text = htmlToText(html);
    if (!text) return '';
    const k = `${tag}-${fnv(text.slice(0, 2000))}`;
    const n = counts.get(k) || 0;
    counts.set(k, n + 1);
    const anchor = n ? `${k}-${n}` : k;
    blocks.push({ anchor, tag, heading, text });
    return ` data-anchor="${anchor}"`;
  };
  const marked = new Marked({ gfm: true });
  marked.use({
    walkTokens(t) {
      if (t.type === 'image' && t.href && !/^(https?:|data:|\/)/i.test(t.href)) {
        const srcImg = path.resolve(path.dirname(doc.abs), decodeURI(t.href));
        if (fs.existsSync(srcImg)) {
          const rel = `/raw/${doc.section.id}/${doc.id}/${path.relative(path.dirname(doc.abs), srcImg).split(path.sep).join('/')}`;
          copyInto(srcImg, path.join(DIST, rel));
          t.href = rel;
        }
      }
      if (t.type === 'link') {
        const r = resolveLink(t.href, doc.abs);
        if (r === 'missing') t.missing = true;
        else if (r) t.href = r;
      }
    },
    renderer: {
      heading({ tokens, depth, text }) {
        const plain = text.replace(/<[^>]+>/g, '').replace(/[*_`]/g, '');
        let id = slugify(plain);
        const n = ids.get(id) || 0;
        ids.set(id, n + 1);
        if (n) id += `-${n}`;
        if (depth === 2) toc.push({ id, text: plain });
        const inner = this.parser.parseInline(tokens);
        if (depth <= 3) heading = htmlToText(inner);
        return `<h${depth} id="${id}"${addBlock(`h${depth}`, inner)}>${inner}</h${depth}>\n`;
      },
      paragraph({ tokens }) {
        const inner = this.parser.parseInline(tokens);
        return `<p${liDepth ? '' : addBlock('p', inner)}>${inner}</p>\n`;
      },
      listitem(item) {
        liDepth++;
        const own = this.parser.parse(item.tokens.filter((t) => t.type !== 'list'), !!item.loose);
        liDepth--;
        const attr = addBlock('li', own);
        liDepth++;
        const body = this.parser.parse(item.tokens, !!item.loose);
        liDepth--;
        return `<li${attr}>${body}</li>\n`;
      },
      tablerow({ text }) {
        return `<tr${addBlock('tr', text.replace(/<\/t[hd]>/g, ' | '))}>\n${text}</tr>\n`;
      },
      code({ text }) {
        return `<pre${addBlock('pre', esc(text))}><code>${esc(text)}</code></pre>\n`;
      },
      link({ href, title, tokens, missing }) {
        const inner = this.parser.parseInline(tokens);
        if (missing) return `<span class="deadlink" title="Dokument není v portálu">${inner}</span>`;
        const ext = /^https?:/i.test(href);
        return `<a href="${esc(href)}"${title ? ` title="${esc(title)}"` : ''}${ext ? ' target="_blank" rel="noopener"' : ''}>${inner}</a>`;
      },
      codespan({ text }) {
        const name = text.replace(/&amp;/g, '&').split('#')[0];
        const t = /\.(md|html?)$/i.test(name) && docs.find((d) => path.basename(d.abs) === path.basename(name));
        return t ? `<a class="doclink" href="${t.route}">${esc(t.title)}</a>` : `<code>${text}</code>`;
      },
      table(token) {
        const out = Renderer.prototype.table.call(this, token);
        return `<div class="tablewrap">${out}</div>`;
      },
    },
  });
  const html = marked.parse(src);
  return { html, toc, blocks };
}


// ---------- quick-overview slides (slides/<section>.md, see slides/FORMAT.md) ----------
function renderSlides(section) {
  const file = path.join(ROOT, 'slides', `${section.id}.md`);
  if (!fs.existsSync(file)) return null;
  const sm = new Marked({ gfm: true });
  sm.use({
    renderer: {
      codespan({ text }) {
        const t = /\.(md|html?)$/i.test(text) && docs.find((d) => path.basename(d.abs) === path.basename(text));
        return t ? `<a href="${t.route}">${esc(t.title)}</a>` : `<code>${text}</code>`;
      },
      table(token) {
        return `<div class="tablewrap">${Renderer.prototype.table.call(this, token)}</div>`;
      },
    },
  });
  const raw = fs.readFileSync(file, 'utf8').split(/^---\s*$/m).map((x) => x.trim()).filter(Boolean);
  return raw.map((md, i) => {
    const stats = [];
    const body = md
      .split('\n')
      .filter((line) => {
        const m = line.match(/^!!\s*(.+?)\s*\|\s*(.+)$/);
        if (m) stats.push(m);
        return !m;
      })
      .join('\n')
      .replace(/\n(→)/g, '\n\n$1');
    let html = sm.parse(body);
    html = html.replace(/<p>→\s*/g, '<p class="src"><span aria-hidden="true">→</span> ');
    if (stats.length) {
      const st = `<div class="stats">${stats.map((m) => `<div class="stat"><b>${esc(m[1])}</b><span>${esc(m[2])}</span></div>`).join('')}</div>`;
      html = html.includes('<p class="src">') ? html.replace('<p class="src">', `${st}<p class="src">`) : html + st;
    }
    const title = (md.match(/^#{1,2}\s+(.+)$/m) || [, ''])[1];
    return { i: i + 1, title, html, text: htmlToText(html).replace(/^→\s*/, '') };
  });
}

function deckHtml(slides) {
  return `<section class="quick" aria-label="Rychlý přehled">
  <div class="quickhead"><h2>Rychlý přehled</h2><span class="qcount" aria-live="polite">1 / ${slides.length}</span>
  <span class="qnav"><button type="button" class="iconbtn" data-q="prev" aria-label="Předchozí snímek"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button><button type="button" class="iconbtn" data-q="next" aria-label="Další snímek"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button><button type="button" class="btn" data-q="full">Promítat</button></span></div>
  <div class="deckview" tabindex="0" aria-roledescription="prezentace">${slides
    .map((sl, i) => `<div class="dslide${i === 0 ? ' first on' : ''}" data-anchor="s${sl.i}" aria-roledescription="snímek" aria-label="${sl.i} z ${slides.length}"${i ? ' hidden' : ''}><div class="dinner">${sl.html}</div><span class="dnum">${sl.i} / ${slides.length}</span></div>`)
    .join('')}</div>
  <ol class="qdots">${slides.map((sl, i) => `<li><button type="button" data-q="${i}"${i === 0 ? ' aria-current="true"' : ''} title="${esc(sl.title)}"><span>${sl.i}</span></button></li>`).join('')}</ol>
</section>`;
}

// ---------- page chrome ----------
const roster = cfg.viewers;
const clientData = (extra) =>
  `<script type="application/json" id="p-data">${JSON.stringify({
    roster,
    docs: docs.map((d) => ({ id: d.id, title: d.title, route: d.route, section: d.section.id, kind: d.kind, raw: d.raw || null, modified: d.modified.toISOString() })),
    sections: sections.map((s) => ({ id: s.id, num: s.num, title: s.title, route: s.route })),
    ...extra,
  }).replace(/</g, '\\u003c')}</script>`;

const ICON = {
  logo: `<img class="logo" src="/_p/logo.png" alt="NOXGAMES" width="32" height="28">`,
  sun: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  feedback: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
};

function bar(active) {
  return `<header class="bar">
  <a class="brand" href="/">${ICON.logo}<span>${esc(cfg.title)}</span></a>
  <nav class="barnav" aria-label="Hlavní">
    <a href="/"${active === 'home' ? ' aria-current="page"' : ''}>Obsah</a>
    <a href="/feedback/"${active === 'feedback' ? ' aria-current="page"' : ''}>Poznámky<span class="badge" data-open-total hidden></span></a>
  </nav>
  <div class="barright">
    <button class="askbtn" type="button" data-act="chat" aria-label="Zeptat se asistenta" title="Zeptat se (klávesa /)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg><span>Zeptat se</span></button>
    <a class="viewer" href="/who/" data-viewer title="Změnit, kdo se dívá"><i></i><span>Kdo se dívá?</span></a>
    <a class="iconbtn" href="/settings/" aria-label="Nastavení a přístup pro AI" title="Nastavení"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg></a>
    <button class="iconbtn" type="button" data-act="theme" aria-label="Přepnout světlý / tmavý režim">${ICON.sun}</button>
    <a class="textbtn" href="/logout/">Odhlásit</a>
  </div>
</header>`;
}

function tabs(activeId) {
  return `<nav class="tabs" aria-label="Oddíly">${sections
    .map(
      (s) =>
        `<a class="tab${s.id === activeId ? ' on' : ''}${s.docList.length ? '' : ' planned'}" href="${s.route}"${s.id === activeId ? ' aria-current="true"' : ''}><b>${s.num}</b><span>${esc(s.title)}</span></a>`,
    )
    .join('')}</nav>`;
}

function page({ title, body, bodyClass = '', active, section, data = {} }) {
  return `<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>${esc(title)} · ${esc(cfg.title)}</title>
<link rel="icon" href="/_p/favicon.png">
<link rel="stylesheet" href="/_p/portal.css?v=${BUILD}">
<script>try{var t=localStorage.getItem('np-theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script>
</head>
<body class="${bodyClass}">
${bar(active)}
${tabs(section)}
${body}
${clientData(data)}
<script src="/_p/portal.js?v=${BUILD}" defer></script>
</body>
</html>`;
}

function siblings(s, current) {
  if (s.docList.length < 2) return '';
  const groups = [];
  for (const d of s.docList) {
    const g = d.group || '';
    let grp = groups.find((x) => x.name === g);
    if (!grp) groups.push((grp = { name: g, docs: [] }));
    grp.docs.push(d);
  }
  return `<nav class="siblings" aria-label="Dokumenty oddílu">${groups
    .map(
      (g) =>
        `<div class="sibgroup">${g.name ? `<span class="sibname">${esc(g.name)}</span>` : ''}${g.docs
          .map((d) => `<a href="${d.route}"${d === current ? ' aria-current="page"' : ''}>${esc(d.title)}</a>`)
          .join('')}</div>`,
    )
    .join('')}</nav>`;
}

// ---------- build ----------
const BUILD = Date.now().toString(36);
fs.rmSync(DIST, { recursive: true, force: true });
fs.mkdirSync(path.join(DIST, '_p', 'fonts'), { recursive: true });

// static
for (const f of fs.readdirSync(path.join(ROOT, 'static'))) copyInto(path.join(ROOT, 'static', f), path.join(DIST, '_p', f));
const fontSrc = (pkg) => path.join(ROOT, 'node_modules', '@fontsource-variable', pkg, 'files');
for (const [pkg, files] of [
  ['inter', ['inter-latin-wght-normal.woff2', 'inter-latin-ext-wght-normal.woff2']],
  ['montserrat', ['montserrat-latin-wght-normal.woff2', 'montserrat-latin-ext-wght-normal.woff2']],
])
  for (const f of files) fs.copyFileSync(path.join(fontSrc(pkg), f), path.join(DIST, '_p', 'fonts', f));
fs.copyFileSync(path.join(ROOT, '..', 'Strategie_Produkce', 'assets', 'noxgames-logo.png'), path.join(DIST, '_p', 'logo.png'));

// render md first so titles exist for nav
const rendered = new Map();
for (const d of docs) {
  if (d.kind === 'md') rendered.set(d, renderMd(d));
  else {
    if (!d.title) d.title = path.basename(d.abs);
    const rawDir = `/raw/${d.section.id}/${d.id}/`;
    d.raw = rawDir + path.basename(d.abs);
    copyInto(d.abs, path.join(DIST, d.raw));
    for (const a of d.assets || []) copyInto(path.join(path.dirname(d.abs), a), path.join(DIST, rawDir, a));
  }
}

const write = (route, html) => {
  const file = path.join(DIST, route, 'index.html');
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, html);
};

for (const d of docs) {
  const s = d.section;
  const head = `<div class="dochead">
  <p class="crumb"><a href="/">Obsah</a><span aria-hidden="true">/</span><a href="${s.route}">${s.num} ${esc(s.title)}</a></p>
  <h1>${esc(d.title)}</h1>
  <p class="meta"><span>Upraveno ${fmtDate(d.modified)}</span><span data-readers></span><span data-doc-count></span></p>
  ${siblings(s, d)}
</div>`;
  let main;
  if (d.kind === 'md') {
    const { html, toc } = rendered.get(d);
    const tocHtml = toc.length > 2
      ? `<details class="toc"><summary>Obsah dokumentu <small>${toc.length} kapitol</small></summary><ol>${toc.map((t) => `<li><a href="#${t.id}">${esc(t.text)}</a></li>`).join('')}</ol></details>`
      : '';
    main = `<main class="sheet" id="main">${head}
<div class="tools">${tocHtml}<button type="button" class="btn" data-act="doc-comment">Poznámka k celému dokumentu</button><button type="button" class="btn" data-act="present" title="Klávesa P">Prezentovat</button></div>
<div class="pagebody"><article class="prose" id="doc">${html}</article><aside class="margin" id="margin" aria-label="Poznámky"></aside></div>
</main>`;
  } else {
    main = `<main class="sheet wide" id="main">${head}
<div class="tools"><button type="button" class="btn" data-act="pick" aria-pressed="false">Komentovat části</button><button type="button" class="btn" data-act="doc-comment">Poznámka k celému dokumentu</button><button type="button" class="btn" data-act="fullscreen">Celá obrazovka</button><a class="btn" href="${d.raw}" target="_blank" rel="noopener">Otevřít samostatně</a></div>
<div class="pagebody showcase"><div class="frame${d.frame === 'deck' || /prezentace/.test(d.abs) ? ' deck' : ''}"><iframe id="frame" src="${d.raw}" title="${esc(d.title)}"></iframe></div><aside class="margin panel" id="margin" aria-label="Poznámky"></aside></div>
</main>`;
  }
  write(d.route, page({ title: d.title, body: main, bodyClass: `doc kind-${d.kind}`, section: s.id, data: { doc: d.id } }));
}

// section divider pages
for (const s of sections) {
  const groups = [];
  for (const d of s.docList) {
    const g = d.group || '';
    let grp = groups.find((x) => x.name === g);
    if (!grp) groups.push((grp = { name: g, docs: [] }));
    grp.docs.push(d);
  }
  const list = s.docList.length
    ? groups
        .map(
          (g) => `${g.name ? `<h2 class="grouph">${esc(g.name)}</h2>` : ''}<ul class="doclist">${g.docs
            .map(
              (d) => `<li data-doc-row="${d.id}"><a href="${d.route}"><span class="dt">${esc(d.title)}</span><span class="dm"><span>${d.kind === 'md' ? 'Dokument' : 'Prezentace'}</span><span>upraveno ${fmtDate(d.modified)}</span><span data-count></span><span data-new hidden>nové</span></span></a></li>`,
            )
            .join('')}</ul>`,
        )
        .join('')
    : `<p class="planned-note">Připravuje se. Podklady sem přibudou před poradou.</p>`;
  const slides = renderSlides(s);
  s.slides = slides;
  const docsHead = slides ? '<h2 class="grouph docsh">Podklady</h2>' : '';
  const body = `<main class="sheet divider" id="main"><div class="divhead"><span class="bignum" aria-hidden="true">${s.num}</span><div><h1>${esc(s.title)}</h1><p class="lede">${esc(s.summary)}</p></div></div>${slides ? deckHtml(slides) : ''}${docsHead}${list}</main>`;
  write(s.route, page({ title: s.title, body, bodyClass: 'section', section: s.id, data: { sectionId: s.id } }));
}

// home
const home = `<main class="sheet home" id="main">
<div class="cover"><h1>${esc(cfg.title)}</h1><p class="lede">${esc(cfg.subtitle)}</p><p class="hello" data-hello></p></div>
<ol class="contents">${sections
  .map(
    (s) => `<li class="${s.docList.length ? '' : 'planned'}" data-section-row="${s.id}"><a href="${s.route}">
  <span class="num" aria-hidden="true">${s.num}</span>
  <span class="ct"><span class="title">${esc(s.title)}</span><span class="sum">${esc(s.summary)}</span></span>
  <span class="cm"><span>${s.docList.length ? `${s.docList.length} ${s.docList.length === 1 ? 'dokument' : s.docList.length < 5 ? 'dokumenty' : 'dokumentů'}` : 'připravuje se'}</span><span data-count></span><span data-new hidden>nové</span></span>
</a></li>`,
  )
  .join('')}</ol>
</main>`;
write('/', page({ title: 'Obsah', body: home, bodyClass: 'home', active: 'home' }));

// feedback overview
const fb = `<main class="sheet feedback" id="main">
<div class="cover small"><h1>Poznámky</h1><p class="lede">Všechny poznámky napříč podklady. Klikem skočíte přímo na místo v textu.</p></div>
<div class="filters" role="group" aria-label="Filtr">
  <label>Stav <select data-filter="state"><option value="open">Otevřené</option><option value="resolved">Vyřešené</option><option value="all">Vše</option></select></label>
  <label>Autor <select data-filter="author"><option value="">Všichni</option>${roster.map((v) => `<option>${esc(v.name)}</option>`).join('')}</select></label>
</div>
<div id="feedback-list" aria-live="polite"><p class="muted">Načítám…</p></div>
</main>`;
write('/feedback/', page({ title: 'Poznámky', body: fb, bodyClass: 'feedbackpage', active: 'feedback' }));

// login + who (served publicly by the worker)
const gate = (title, inner) => `<!DOCTYPE html>
<html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>${esc(title)} · ${esc(cfg.title)}</title><link rel="icon" href="/_p/favicon.png"><link rel="stylesheet" href="/_p/portal.css?v=${BUILD}">
<script>try{var t=localStorage.getItem('np-theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script></head>
<body class="gate"><main class="gatebox">${ICON.logo}<h1>${esc(cfg.title)}</h1><p class="lede">${esc(cfg.subtitle)}</p>${inner}</main></body></html>`;

fs.writeFileSync(
  path.join(DIST, '_p', 'login.html'),
  gate('Přihlášení', `<form method="post" action="/login/" class="gateform">
<label for="pw">Společné heslo</label>
<input id="pw" name="password" type="password" autocomplete="current-password" required autofocus>
<p class="err" data-err hidden>Heslo nesedí. Zkuste to znovu.</p>
<p class="err" data-nopw hidden>Heslo zatím není nastavené. David ho nastaví příkazem wrangler secret put SITE_PASSWORD.</p>
<input type="hidden" name="next" value="">
<button class="btn primary" type="submit">Vstoupit</button>
</form>
<script>var q=new URLSearchParams(location.search);if(q.get('e')==='1')document.querySelector('[data-err]').hidden=false;if(q.get('e')==='nopw')document.querySelector('[data-nopw]').hidden=false;document.querySelector('[name=next]').value=q.get('next')||'/';</script>`),
);
fs.writeFileSync(
  path.join(DIST, '_p', 'who.html'),
  gate('Kdo se dívá', `<form method="post" action="/who/" class="gateform">
<fieldset><legend>Kdo se dívá?</legend><p class="hint">Vaše jméno se ukáže u poznámek. Změnit ho jde kdykoli vpravo nahoře.</p>
<div class="whogrid">${roster.map((v) => `<button type="submit" name="who" value="${esc(v.id)}" style="--c:${v.color}"><i></i><span>${esc(v.name)}</span><small>${esc(v.role)}</small></button>`).join('')}</div>
</fieldset>
<label for="other">Někdo jiný</label>
<div class="row"><input id="other" name="other" maxlength="40" placeholder="Vaše jméno"><button class="btn" type="submit" name="who" value="_other">Pokračovat</button></div>
<input type="hidden" name="next" value="">
</form>
<script>var q=new URLSearchParams(location.search);document.querySelector('[name=next]').value=q.get('next')||'/';</script>`),
);

// settings: personal MCP tokens
const settings = `<main class="sheet settings" id="main">
<div class="cover small"><h1>Nastavení</h1><p class="lede">Přístup pro vlastního AI asistenta (Claude Code, Claude Desktop, Cursor). Asistent pak umí hledat v podkladech, číst je a psát poznámky vaším jménem.</p></div>
<section class="setblock"><h2>Kdo se dívá</h2><p>Jste přihlášeni jako <b data-me>…</b>. <a href="/who/?next=/settings/">Změnit</a></p></section>
<section class="setblock"><h2>Vzhled</h2><p><button type="button" class="btn" data-act="theme">Přepnout světlý / tmavý režim</button></p></section>
<section class="setblock"><h2>Osobní tokeny pro MCP</h2>
<p class="muted">Token patří vám: poznámky napsané přes něj ponesou vaše jméno. Zobrazí se jen jednou, uložte si ho. Kdykoli ho tu můžete zrušit.</p>
<form class="tokform" data-tokform><label for="toklabel">Název tokenu</label><div class="row"><input id="toklabel" name="label" maxlength="60" placeholder="např. MacBook, Claude Code"><button class="btn primary" type="submit">Vytvořit token</button></div></form>
<div data-newtoken hidden></div>
<div data-toklist aria-live="polite"><p class="muted">Načítám…</p></div>
</section>
<section class="setblock"><h2>Jak připojit</h2>
<p>Claude Code (terminál), token vložte místo <code>VÁŠ_TOKEN</code>:</p>
<pre class="cmd" data-cmd="cc">claude mcp add --transport http noxgames-navrhy ORIGIN/mcp --header "Authorization: Bearer VÁŠ_TOKEN"</pre>
<p>Claude Desktop, Cursor a další klienti: přidejte vzdálený MCP server s adresou <code data-origin>ORIGIN/mcp</code> a hlavičkou <code>Authorization: Bearer VÁŠ_TOKEN</code>.</p>
<p class="muted">Nástroje: hledání v podkladech, čtení dokumentu i rychlého přehledu, seznam poznámek, nová poznámka, odpověď, vyřešení vlákna, kalkulačka.</p>
</section>
</main>`;
write('/settings/', page({ title: 'Nastavení', body: settings, bodyClass: 'settingspage', active: 'settings' }));

// search index for chatbot + MCP (loaded into D1 by `npm run cf:index`)
const sq = (v) => (v == null ? 'NULL' : `'${String(v).replace(/'/g, "''")}'`);
const sql = ['DELETE FROM chunks;', 'DELETE FROM docs;'];
const htmlBlocks = (abs) => {
  const raw = fs.readFileSync(abs, 'utf8')
    .replace(/<(script|style|svg|head)[\s\S]*?<\/\1>/gi, ' ')
    .replace(/<\/(p|li|h[1-6]|div|section|tr|td|th|br|article)>/gi, '\n');
  const paras = htmlToText(raw.replace(/\n/g, '\u0001')).split('\u0001').map((x) => x.trim()).filter((x) => x.length > 2);
  const out = [];
  let cur = '';
  for (const p of paras) {
    if ((cur + ' ' + p).length > 900 && cur) { out.push(cur); cur = ''; }
    cur = cur ? `${cur} ${p}` : p;
  }
  if (cur) out.push(cur);
  return out;
};
for (const d of docs) {
  let blocks;
  if (d.kind === 'md') blocks = rendered.get(d).blocks;
  else blocks = htmlBlocks(d.abs).map((text, i) => ({ anchor: '_doc', tag: 'p', heading: d.title, text, part: i }));
  const text = blocks.map((b) => (d.kind === 'md' ? `[${b.anchor}] ${/^h\d/.test(b.tag) ? '#'.repeat(+b.tag[1]) + ' ' : b.tag === 'li' ? '- ' : ''}${b.text}` : b.text)).join('\n');
  sql.push(`INSERT INTO docs (id, title, section, section_title, route, kind, modified, summary, text) VALUES (${[d.id, d.title, d.section.id, d.section.title, d.route, d.kind, d.modified.toISOString(), d.section.summary, text].map(sq).join(', ')});`);
  for (const b of blocks) sql.push(`INSERT INTO chunks (doc, anchor, heading, text) VALUES (${[d.id, b.anchor, b.heading, b.text].map(sq).join(', ')});`);
}
for (const s of sections) {
  if (!s.slides) continue;
  const id = `prehled-${s.id}`;
  const text = s.slides.map((sl) => `[s${sl.i}] ${sl.text}`).join('\n');
  sql.push(`INSERT INTO docs (id, title, section, section_title, route, kind, modified, summary, text) VALUES (${[id, `Rychlý přehled: ${s.title}`, s.id, s.title, s.route, 'slides', new Date().toISOString(), s.summary, text].map(sq).join(', ')});`);
  for (const sl of s.slides) sql.push(`INSERT INTO chunks (doc, anchor, heading, text) VALUES (${[id, `s${sl.i}`, sl.title, sl.text].map(sq).join(', ')});`);
}
fs.mkdirSync(path.join(ROOT, 'build'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'build', 'index.sql'), sql.join('\n') + '\n');

fs.writeFileSync(path.join(DIST, '_p', 'roster.json'), JSON.stringify(roster));
fs.writeFileSync(
  path.join(ROOT, 'manifest.local.json'),
  JSON.stringify(docs.map((d) => ({ id: d.id, title: d.title, route: d.route, src: path.relative(ROOT, d.abs) })), null, 2),
);

console.log(`Built ${docs.length} docs in ${sections.length} sections -> dist/`);
