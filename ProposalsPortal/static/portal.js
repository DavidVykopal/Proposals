(() => {
  'use strict';
  const D = JSON.parse(document.getElementById('p-data')?.textContent || '{}');
  const roster = D.roster || [];
  const docsById = Object.fromEntries((D.docs || []).map((d) => [d.id, d]));
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const me = (() => {
    const m = document.cookie.match(/(?:^|;\s*)np_who=([^;]*)/);
    try { return m ? decodeURIComponent(decodeURIComponent(m[1])) : ''; } catch { return ''; }
  })();
  const colorOf = (name) => roster.find((v) => v.name === name)?.color || 'var(--faint)';
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const plural = (n, one, few, many) => `${n} ${n === 1 ? one : n > 1 && n < 5 ? few : many}`;
  const ICONS = {
    comment: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/><path d="M12 8v5M9.5 10.5h5"/></svg>',
    link: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  };

  // ---------- basics ----------
  document.addEventListener('click', (e) => {
    if (!e.target.closest('[data-act="theme"]')) return;
    const root = document.documentElement;
    const next = root.dataset.theme === 'light' ? 'dark' : 'light';
    root.dataset.theme = next;
    try { localStorage.setItem('np-theme', next); } catch {}
  });

  const chip = $('[data-viewer]');
  if (chip && me) {
    chip.querySelector('span').textContent = me;
    chip.style.setProperty('--c', colorOf(me));
    chip.href = `/who/?next=${encodeURIComponent(location.pathname)}`;
  }

  async function api(path, opts = {}) {
    const r = await fetch(path, {
      method: opts.method || 'GET',
      headers: opts.body ? { 'content-type': 'application/json' } : undefined,
      body: opts.body ? JSON.stringify(opts.body) : undefined,
      credentials: 'same-origin',
    });
    if (r.status === 401) {
      location.href = `/login/?next=${encodeURIComponent(location.pathname)}`;
      throw new Error('auth');
    }
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.message || 'Nepodařilo se uložit. Zkontrolujte připojení a zkuste to znovu.');
    return j;
  }

  let toastTimer;
  function toast(msg) {
    let t = $('.toast');
    if (!t) {
      t = document.createElement('div');
      t.className = 'toast';
      t.setAttribute('role', 'status');
      document.body.append(t);
    }
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove('show'), 2400);
  }

  const parseTs = (s) => (s ? new Date(s.includes('T') ? s : s.replace(' ', 'T') + 'Z') : null);
  const rtf = new Intl.RelativeTimeFormat('cs', { numeric: 'auto' });
  function ago(s) {
    const d = parseTs(s);
    if (!d) return '';
    const sec = (d - Date.now()) / 1000;
    const abs = Math.abs(sec);
    if (abs < 60) return 'právě teď';
    if (abs < 3600) return rtf.format(Math.round(sec / 60), 'minute');
    if (abs < 86400) return rtf.format(Math.round(sec / 3600), 'hour');
    if (abs < 7 * 86400) return rtf.format(Math.round(sec / 86400), 'day');
    return `${d.getDate()}. ${d.getMonth() + 1}.`;
  }
  const fullDate = (s) => parseTs(s)?.toLocaleString('cs-CZ', { dateStyle: 'medium', timeStyle: 'short' }) || '';

  // ---------- summary: home, section, badge, doc meta ----------
  async function loadSummary() {
    let s;
    try { s = await api('/api/summary'); } catch { return; }
    const open = Object.fromEntries(s.open.map((r) => [r.doc, r.n]));
    const latest = Object.fromEntries(s.latest.map((r) => [r.doc, r.at]));
    const myView = {};
    const readers = {};
    for (const v of s.views) {
      (readers[v.doc] ||= []).push(v);
      if (v.viewer === me) myView[v.doc] = v.last_at;
    }
    const isNew = (docId) => {
      const seen = parseTs(myView[docId]);
      const d = docsById[docId];
      if (!seen) return true;
      return new Date(d.modified) > seen || (latest[docId] && parseTs(latest[docId]) > seen);
    };
    const total = Object.values(open).reduce((a, b) => a + b, 0);
    const badge = $('[data-open-total]');
    if (badge && total) { badge.textContent = total; badge.hidden = false; badge.setAttribute('aria-label', plural(total, 'otevřená poznámka', 'otevřené poznámky', 'otevřených poznámek')); }

    for (const row of $$('[data-section-row]')) {
      const ids = D.docs.filter((d) => d.section === row.dataset.sectionRow).map((d) => d.id);
      const n = ids.reduce((a, id) => a + (open[id] || 0), 0);
      $('[data-count]', row).textContent = n ? plural(n, 'otevřená poznámka', 'otevřené poznámky', 'otevřených poznámek') : '';
      $('[data-new]', row).hidden = !ids.some(isNew);
    }
    for (const row of $$('[data-doc-row]')) {
      const id = row.dataset.docRow;
      $('[data-count]', row).textContent = open[id] ? plural(open[id], 'poznámka', 'poznámky', 'poznámek') : '';
      $('[data-new]', row).hidden = !isNew(id);
    }
    const hello = $('[data-hello]');
    if (hello) {
      hello.innerHTML = `Díváte se jako <b style="color:${colorOf(me)}">${esc(me)}</b>. ${total ? `${plural(total, 'otevřená poznámka', 'otevřené poznámky', 'otevřených poznámek')} ${total > 1 && total < 5 ? 'čekají' : 'čeká'} na vyřešení. <a href="/feedback/">Projít poznámky</a>` : 'Zatím žádné otevřené poznámky.'}`;
    }
    if (D.doc) {
      const r = (readers[D.doc] || []).filter((v) => v.viewer !== me);
      const el = $('[data-readers]');
      if (el && r.length) {
        el.className = 'who-dots';
        el.innerHTML = 'Četli: ' + r.map((v) => `<span title="${esc(fullDate(v.last_at))}"><i style="--c:${colorOf(v.viewer)}"></i>${esc(v.viewer)}</span>`).join(', ');
      }
    }
  }
  loadSummary();

  // ---------- block anchors (shared by markdown and showcases) ----------
  const fnv = (str) => {
    let h = 0x811c9dc5;
    for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 0x01000193); }
    return (h >>> 0).toString(36);
  };
  function ownText(el) {
    const c = el.cloneNode(true);
    c.querySelectorAll('.cnt, .np-ui').forEach((n) => n.remove());
    if (el.tagName === 'LI') c.querySelectorAll('ul, ol').forEach((n) => n.remove());
    let t = c.textContent.replace(/\s+/g, ' ').trim();
    if (!t) {
      const img = el.querySelector('img');
      t = img ? `img:${img.getAttribute('src')}` : '';
    }
    return t.slice(0, 2000);
  }
  function anchorFor(el, root) {
    const tag = el.tagName.toLowerCase();
    const h = fnv(ownText(el));
    let idx = 0;
    for (const o of root.querySelectorAll(tag)) {
      if (o === el) break;
      if (fnv(ownText(o)) === h) idx++;
    }
    return `${tag}-${h}${idx ? `-${idx}` : ''}`;
  }
  function findAnchor(anchor, root) {
    const m = anchor.match(/^([a-z0-9]+)-([a-z0-9]+)(?:-(\d+))?$/);
    if (!m) return null;
    let idx = Number(m[3] || 0);
    for (const o of root.querySelectorAll(m[1])) {
      if (fnv(ownText(o)) === m[2] && idx-- === 0) return o;
    }
    return null;
  }

  // ---------- comment rendering ----------
  function threadsFrom(comments) {
    const roots = new Map();
    for (const c of comments) if (!c.parent_id) roots.set(c.id, { root: c, replies: [] });
    for (const c of comments) if (c.parent_id && roots.has(c.parent_id)) roots.get(c.parent_id).replies.push(c);
    return Array.from(roots.values());
  }
  const linkify = (s) => esc(s).replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');

  function commentHtml(c, isRoot, prevSeen) {
    const fresh = prevSeen && c.author !== me && parseTs(c.created_at) > parseTs(prevSeen);
    const own = c.author === me;
    const acts = [];
    if (isRoot) acts.push(`<button type="button" data-c="reply">Odpovědět</button>`, `<button type="button" data-c="resolve">${c.resolved ? 'Znovu otevřít' : 'Vyřešit'}</button>`);
    if (own) acts.push(`<button type="button" data-c="edit" data-id="${c.id}">Upravit</button>`, `<button type="button" data-c="delete" data-id="${c.id}">Smazat</button>`);
    return `<div class="c" data-id="${c.id}">
      <div class="chead"><i style="--c:${colorOf(c.author)}"></i><b>${esc(c.author)}</b><time datetime="${esc(c.created_at)}" title="${esc(fullDate(c.created_at))}">${ago(c.created_at)}${c.edited_at ? ' · upraveno' : ''}</time>${fresh ? '<span class="new">nové</span>' : ''}</div>
      <div class="cbody">${linkify(c.body)}</div>
      ${acts.length ? `<div class="cacts${isRoot ? '' : ' minor'}">${acts.join('')}</div>` : ''}
    </div>`;
  }

  function threadEl(t, opts) {
    const el = document.createElement('div');
    el.className = `thread${t.root.resolved ? ' resolved' : ''}`;
    el.dataset.root = t.root.id;
    el.dataset.anchor = t.root.anchor;
    const showAll = opts.expanded?.has(t.root.id) || t.replies.length <= 2;
    const replies = showAll ? t.replies : t.replies.slice(-1);
    const quote = opts.quote
      ? opts.link
        ? `<a class="quote" href="${opts.link}">${t.root.anchor === '_doc' ? 'K celému dokumentu' : esc(t.root.quote || 'Část dokumentu')}</a>`
        : `<button type="button" class="quote" data-c="goto">${t.root.anchor === '_doc' ? 'K celému dokumentu' : esc(t.root.quote || 'Část dokumentu')}</button>`
      : '';
    el.innerHTML = `${quote}${commentHtml(t.root, true, opts.prevSeen)}${!showAll ? `<button type="button" class="more" data-c="expand">${plural(t.replies.length - 1, 'další odpověď', 'další odpovědi', 'dalších odpovědí')}</button>` : ''}${replies.map((r) => commentHtml(r, false, opts.prevSeen)).join('')}${t.root.resolved && t.root.resolved_by ? `<p class="resolved-by">Vyřešil(a) ${esc(t.root.resolved_by)} ${ago(t.root.resolved_at)}</p>` : ''}`;
    return el;
  }

  function composerEl({ placeholder = 'Napište poznámku…', value = '', submitLabel = 'Uložit' } = {}) {
    const f = document.createElement('form');
    f.className = 'composer np-ui';
    f.innerHTML = `<textarea aria-label="Text poznámky" placeholder="${esc(placeholder)}" maxlength="4000"></textarea>
      <div class="row"><small>Ctrl + Enter uloží</small><span><button type="button" class="btn" data-c="cancel">Zrušit</button><button type="submit" class="btn primary">${submitLabel}</button></span></div>
      <p class="err" hidden></p>`;
    const ta = f.querySelector('textarea');
    ta.value = value;
    ta.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); f.requestSubmit(); }
      if (e.key === 'Escape') { e.preventDefault(); f.querySelector('[data-c="cancel"]').click(); }
    });
    return f;
  }

  // Shared thread controller used by doc pages and the feedback page.
  function wireThreads(container, ctx) {
    container.addEventListener('click', async (e) => {
      const b = e.target.closest('[data-c]');
      if (!b) return;
      const th = b.closest('.thread');
      const rootId = th ? Number(th.dataset.root) : null;
      const docId = th?.dataset.doc || ctx.doc;
      const act = b.dataset.c;
      if (act === 'goto') return ctx.goto?.(th.dataset.anchor, rootId);
      if (act === 'expand') { ctx.expanded.add(rootId); return ctx.render(); }
      if (act === 'reply') {
        if (th.querySelector('.composer')) return th.querySelector('textarea').focus();
        ctx.activate?.(rootId);
        const f = composerEl({ placeholder: 'Odpovědět…', submitLabel: 'Odpovědět' });
        th.append(f);
        f.querySelector('textarea').focus();
        f.addEventListener('submit', (ev) => submit(ev, f, { doc: docId, parent_id: rootId }));
        f.querySelector('[data-c="cancel"]').onclick = () => { f.remove(); ctx.relayout?.(); };
        ctx.relayout?.();
        return;
      }
      if (act === 'resolve') {
        const c = ctx.comments.find((x) => x.id === rootId);
        b.disabled = true;
        try {
          const r = await api(`/api/comments/${rootId}`, { method: 'PATCH', body: { resolved: !c.resolved } });
          Object.assign(c, r.comment);
          toast(c.resolved ? 'Vlákno je vyřešené' : 'Vlákno je znovu otevřené');
          ctx.render();
          loadSummary();
        } catch (err) { toast(err.message); b.disabled = false; }
        return;
      }
      if (act === 'edit') {
        const id = Number(b.dataset.id);
        const c = ctx.comments.find((x) => x.id === id);
        const node = b.closest('.c');
        const f = composerEl({ value: c.body, submitLabel: 'Uložit změnu' });
        node.querySelector('.cbody').replaceWith(f);
        node.querySelector('.cacts')?.remove();
        f.querySelector('textarea').focus();
        f.querySelector('[data-c="cancel"]').onclick = () => ctx.render();
        f.addEventListener('submit', async (ev) => {
          ev.preventDefault();
          try {
            const r = await api(`/api/comments/${id}`, { method: 'PATCH', body: { body: f.querySelector('textarea').value } });
            Object.assign(c, r.comment);
            ctx.render();
          } catch (err) { showErr(f, err.message); }
        });
        ctx.relayout?.();
        return;
      }
      if (act === 'delete') {
        if (!b.dataset.armed) {
          b.dataset.armed = '1';
          b.textContent = 'Opravdu smazat?';
          setTimeout(() => { if (b.isConnected) { delete b.dataset.armed; b.textContent = 'Smazat'; } }, 4000);
          return;
        }
        const id = Number(b.dataset.id);
        try {
          await api(`/api/comments/${id}`, { method: 'DELETE' });
          ctx.comments = ctx.comments.filter((x) => x.id !== id && x.parent_id !== id);
          ctx.setComments?.(ctx.comments);
          toast('Poznámka je smazaná');
          ctx.render();
          loadSummary();
        } catch (err) { toast(err.message); }
      }
    });

    async function submit(ev, f, payload) {
      ev.preventDefault();
      const ta = f.querySelector('textarea');
      const body = ta.value.trim();
      if (!body) return showErr(f, 'Poznámka je prázdná.');
      const btn = f.querySelector('[type=submit]');
      btn.disabled = true;
      try {
        const r = await api('/api/comments', { method: 'POST', body: { ...payload, body } });
        ctx.comments.push(r.comment);
        if (payload.parent_id) {
          const root = ctx.comments.find((x) => x.id === payload.parent_id);
          if (root) root.resolved = 0;
        }
        ctx.setComments?.(ctx.comments);
        ctx.activeId = r.comment.parent_id || r.comment.id;
        ctx.render();
        loadSummary();
      } catch (err) {
        showErr(f, err.message);
        btn.disabled = false;
      }
    }
    ctx.submit = submit;
  }
  function showErr(f, msg) {
    const p = f.querySelector('.err');
    p.textContent = msg;
    p.hidden = false;
  }

  // ---------- document pages ----------
  if (D.doc) initDoc();

  function initDoc() {
    const kind = document.body.classList.contains('kind-md') ? 'md' : 'html';
    const margin = $('#margin');
    const pagebody = $('.pagebody');
    const narrowMq = matchMedia('(max-width: 1180px)');
    const ctx = { doc: D.doc, comments: [], expanded: new Set(), activeId: null, showResolved: false, prevSeen: null };
    let root = kind === 'md' ? $('#doc') : null;
    let idoc = null;
    let blocks = [];
    let byAnchor = new Map();
    let pending = null; // open new-thread composer {anchor, quote}
    let gut, hoverBlock, picking = false, sheetBtn, rT, hint;

    api('/api/view', { method: 'POST', body: { doc: D.doc } }).then((r) => { ctx.prevSeen = r.prev; render(); }).catch(() => {});

    // --- markdown blocks
    if (kind === 'md') {
      // Anchors are assigned at build time (scripts/build.mjs) so the server, chatbot and MCP share them.
      for (const el of root.querySelectorAll('[data-anchor]')) {
        el.classList.add('cb');
        blocks.push(el);
        byAnchor.set(el.dataset.anchor, el);
      }
      setupGutter();
    }

    // --- showcase iframe
    const frame = $('#frame');
    if (frame) {
      const onLoad = () => {
        try { idoc = frame.contentDocument; } catch { idoc = null; }
        if (!idoc) return;
        const st = idoc.createElement('style');
        st.textContent = '.np-hover{outline:3px solid #00d2ff !important;outline-offset:3px;cursor:copy !important}.np-flash{outline:3px solid #00d2ff !important;outline-offset:4px;transition:outline-color 1.4s}';
        idoc.head.append(st);
        idoc.addEventListener('click', onFrameClick, true);
        idoc.addEventListener('mouseover', onFrameHover, true);
        idoc.addEventListener('keydown', (e) => { if (e.key === 'Escape' && picking) setPicking(false); });
        render();
      };
      frame.addEventListener('load', onLoad);
      if (frame.contentDocument?.readyState === 'complete') onLoad();
    }
    const pickBtn = $('[data-act="pick"]');
    function setPicking(on) {
      picking = on;
      pickBtn?.setAttribute('aria-pressed', String(on));
      $('.frame')?.classList.toggle('picking', on);
      if (!on) idoc?.querySelectorAll('.np-hover').forEach((n) => n.classList.remove('np-hover'));
      if (on) toast('Klikněte na část prezentace, ke které chcete poznámku. Esc ruší.');
    }
    pickBtn?.addEventListener('click', () => setPicking(!picking));
    function pickTarget(t) {
      const sem = t.closest('h1,h2,h3,h4,h5,h6,p,li,tr,blockquote,figcaption,dt,dd,img,svg');
      let el = sem || t;
      while (el && el !== idoc.body && (!el.textContent.trim() && !el.querySelector('img')) ) el = el.parentElement;
      return el && el !== idoc.body && el !== idoc.documentElement ? el : null;
    }
    function onFrameHover(e) {
      if (!picking) return;
      idoc.querySelectorAll('.np-hover').forEach((n) => n.classList.remove('np-hover'));
      pickTarget(e.target)?.classList.add('np-hover');
    }
    function onFrameClick(e) {
      if (picking) {
        e.preventDefault();
        e.stopPropagation();
        const el = pickTarget(e.target);
        setPicking(false);
        if (el) openNew(anchorFor(el, idoc.body), ownText(el).slice(0, 280));
        return;
      }
      const a = e.target.closest('a[href]');
      if (!a) return;
      const u = new URL(a.getAttribute('href'), idoc.baseURI);
      if (u.origin !== location.origin) { a.target = '_blank'; a.rel = 'noopener'; return; }
      const clean = (x) => x.replace(/\.html?$/, '').replace(/\/index$/, '/');
      const target = (D.docs || []).find((d) => d.raw && clean(d.raw) === clean(u.pathname));
      if (target) { e.preventDefault(); location.href = target.route + u.hash; }
    }
    $('[data-act="fullscreen"]')?.addEventListener('click', () => $('.frame')?.requestFullscreen?.());

    // --- gutter (markdown)
    function setupGutter() {
      gut = document.createElement('div');
      gut.className = 'gut np-ui';
      gut.innerHTML = `<button type="button" data-g="comment" aria-label="Přidat poznámku k této části" title="Přidat poznámku">${ICONS.comment}</button><button type="button" data-g="link" aria-label="Zkopírovat odkaz na tuto část" title="Odkaz na tuto část">${ICONS.link}</button>`;
      pagebody.append(gut);
      let hideT;
      const show = (el) => {
        clearTimeout(hideT);
        if (hoverBlock && hoverBlock !== el) hoverBlock.classList.remove('hover');
        hoverBlock = el;
        el.classList.add('hover');
        const top = el.getBoundingClientRect().top - pagebody.getBoundingClientRect().top;
        gut.style.top = `${Math.max(0, top - (narrowMq.matches ? 0 : 2))}px`;
        gut.classList.add('show');
      };
      const hide = () => {
        hideT = setTimeout(() => {
          gut.classList.remove('show');
          hoverBlock?.classList.remove('hover');
        }, 350);
      };
      root.addEventListener('mouseover', (e) => {
        const el = e.target.closest('.cb');
        if (el && !document.body.classList.contains('present')) show(el);
      });
      root.addEventListener('mouseleave', hide);
      gut.addEventListener('mouseenter', () => clearTimeout(hideT));
      gut.addEventListener('mouseleave', hide);
      root.addEventListener('click', (e) => {
        if (e.target.closest('a, .cnt, button')) return;
        if (String(getSelection()).length) return;
        const el = e.target.closest('.cb');
        if (el && (e.pointerType === 'touch' || narrowMq.matches)) show(el);
      });
      gut.addEventListener('click', (e) => {
        const b = e.target.closest('[data-g]');
        if (!b || !hoverBlock) return;
        const el = hoverBlock;
        if (b.dataset.g === 'link') {
          const url = `${location.origin}${location.pathname}#b=${el.dataset.anchor}`;
          navigator.clipboard?.writeText(url).then(() => toast('Odkaz na tuto část je ve schránce'), () => toast(url));
          history.replaceState(null, '', `#b=${el.dataset.anchor}`);
          return;
        }
        const t = threadsFrom(ctx.comments).find((x) => x.root.anchor === el.dataset.anchor && !x.root.resolved);
        if (t) {
          ctx.activeId = t.root.id;
          render();
          openSheet();
          margin.querySelector(`.thread[data-root="${t.root.id}"] [data-c="reply"]`)?.click();
        } else openNew(el.dataset.anchor, ownText(el).slice(0, 280));
        gut.classList.remove('show');
      });
    }

    $('[data-act="doc-comment"]')?.addEventListener('click', () => openNew('_doc', ''));

    function openNew(anchor, quote) {
      pending = { anchor, quote };
      ctx.activeId = null;
      render();
      openSheet();
      const ta = margin.querySelector('.thread.pending textarea');
      ta?.focus({ preventScroll: !narrowMq.matches });
    }

    // --- sheet (narrow screens)
    function openSheet() { if (narrowMq.matches) margin.classList.add('open'); }
    function closeSheet() { margin.classList.remove('open'); }

    // --- rendering
    ctx.render = render;
    ctx.relayout = () => layout();
    ctx.activate = (id) => { ctx.activeId = id; markActive(); };
    ctx.goto = (anchor, id) => {
      ctx.activeId = id;
      markActive();
      if (anchor === '_doc') return;
      if (kind === 'md') {
        const el = byAnchor.get(anchor);
        if (el) { closeSheet(); el.scrollIntoView({ behavior: 'smooth', block: 'center' }); flash(el); }
      } else if (idoc) {
        const el = findAnchor(anchor, idoc.body);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          el.classList.add('np-flash');
          setTimeout(() => el.classList.remove('np-flash'), 1600);
        } else toast('Tuhle část v prezentaci teď nevidím. Možná je na jiném slajdu.');
      }
    };
    wireThreads(margin, ctx);

    function flash(el) {
      el.classList.remove('flash');
      void el.offsetWidth;
      el.classList.add('flash');
    }

    function render() {
      const aligned = kind === 'md' && !narrowMq.matches;
      margin.classList.toggle('list', !aligned && kind === 'md');
      const all = threadsFrom(ctx.comments);
      const visible = all.filter((t) => ctx.showResolved || !t.root.resolved || t.root.id === ctx.activeId);
      const resolvedN = all.filter((t) => t.root.resolved).length;
      const openN = all.length - resolvedN;

      // block markers
      for (const el of blocks) {
        el.classList.remove('has');
        el.querySelector(':scope > .cnt, :scope > td:last-child > .cnt')?.remove();
      }
      const perBlock = new Map();
      for (const t of all) if (!t.root.resolved) perBlock.set(t.root.anchor, (perBlock.get(t.root.anchor) || 0) + 1 + t.replies.length);
      for (const [a, n] of perBlock) {
        const el = byAnchor.get(a);
        if (!el) continue;
        el.classList.add('has');
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'cnt np-ui';
        b.textContent = n;
        b.setAttribute('aria-label', `Zobrazit poznámky (${n})`);
        b.onclick = (e) => {
          e.stopPropagation();
          const t = all.find((x) => x.root.anchor === a && !x.root.resolved);
          ctx.activeId = t?.root.id ?? null;
          render();
          openSheet();
          margin.querySelector('.thread.active')?.scrollIntoView({ block: 'nearest' });
        };
        (el.tagName === 'TR' ? el.lastElementChild : el).append(b);
      }

      // order: doc-level, blocks in document order, orphans
      const pos = (t) => (t.root.anchor === '_doc' ? -1 : byAnchor.has(t.root.anchor) ? blocks.indexOf(byAnchor.get(t.root.anchor)) : Infinity);
      const resolvedOrphan = (t) => kind === 'md' && t.root.anchor !== '_doc' && !byAnchor.has(t.root.anchor);
      visible.sort((a, b) => pos(a) - pos(b) || a.root.id - b.root.id);

      margin.innerHTML = '';
      const head = document.createElement('div');
      head.className = narrowMq.matches ? 'sheetbar' : 'panelhead';
      head.innerHTML = `${narrowMq.matches ? `<b>Poznámky (${openN})</b>` : `<h2>Poznámky (${openN})</h2>`}
        <span style="display:flex;gap:8px;align-items:center">${resolvedN ? `<label><input type="checkbox" data-showres ${ctx.showResolved ? 'checked' : ''}> vyřešené (${resolvedN})</label>` : ''}${narrowMq.matches ? `<button type="button" class="iconbtn" data-close aria-label="Zavřít poznámky">${ICONS.close}</button>` : ''}</span>`;
      if (!aligned || resolvedN || narrowMq.matches) margin.append(head);
      head.querySelector('[data-showres]')?.addEventListener('change', (e) => { ctx.showResolved = e.target.checked; render(); });
      head.querySelector('[data-close]')?.addEventListener('click', closeSheet);

      const listOpts = { expanded: ctx.expanded, prevSeen: ctx.prevSeen, quote: !aligned };
      const orphans = [];
      for (const t of visible) {
        if (resolvedOrphan(t)) { orphans.push(t); continue; }
        const el = threadEl(t, { ...listOpts, quote: !aligned || t.root.anchor === '_doc' });
        margin.append(el);
      }
      if (orphans.length) {
        const box = document.createElement('div');
        box.className = 'orphans';
        box.innerHTML = '<h3>Text se mezitím změnil</h3>';
        for (const t of orphans) box.append(threadEl(t, { ...listOpts, quote: true }));
        margin.append(box);
      }
      if (pending) {
        const p = document.createElement('div');
        p.className = 'thread active pending';
        p.dataset.anchor = pending.anchor;
        if (!aligned || pending.anchor === '_doc') p.innerHTML = `<p class="quote">${pending.anchor === '_doc' ? 'K celému dokumentu' : esc(pending.quote)}</p>`;
        const f = composerEl();
        p.append(f);
        const pAnchor = pending.anchor;
        f.addEventListener('submit', (ev) => { ctx.submit(ev, f, { doc: D.doc, anchor: pAnchor, quote: pending?.quote || '' }).then(() => { if (!f.querySelector('.err:not([hidden])')) pending = null; }); });
        f.querySelector('[data-c="cancel"]').onclick = () => { pending = null; render(); if (narrowMq.matches && !ctx.comments.length) closeSheet(); };
        const firstAfter = Array.from(margin.querySelectorAll('.thread')).find((el) => pos({ root: { anchor: el.dataset.anchor } }) > pos({ root: { anchor: pAnchor } }));
        if (pAnchor === '_doc' || !aligned) head.isConnected ? head.after(p) : margin.prepend(p);
        else firstAfter ? firstAfter.before(p) : margin.append(p);
      }
      if (!visible.length && !pending) {
        const e = document.createElement('p');
        e.className = 'empty';
        e.innerHTML = kind === 'md'
          ? '<b>Zatím bez poznámek.</b> Najeďte myší na odstavec a klikněte na ikonu poznámky vlevo. Na telefonu klepněte na odstavec.'
          : '<b>Zatím bez poznámek.</b> Zapněte „Komentovat části“ a klikněte na místo v prezentaci, nebo napište poznámku k celému dokumentu.';
        margin.append(e);
      }
      const count = $('[data-doc-count]');
      if (count) count.textContent = openN ? plural(openN, 'otevřená poznámka', 'otevřené poznámky', 'otevřených poznámek') : '';
      updateSheetButton(openN);
      markActive();
      layout();
    }

    function markActive() {
      margin.querySelectorAll('.thread').forEach((el) => el.classList.toggle('active', el.classList.contains('pending') || Number(el.dataset.root) === ctx.activeId));
      blocks.forEach((b) => b.classList.remove('active'));
      const act = margin.querySelector('.thread.active');
      const el = act && byAnchor.get(act.dataset.anchor);
      el?.classList.add('active');
    }

    function layout() {
      if (kind !== 'md' || narrowMq.matches) { margin.style.minHeight = ''; margin.querySelectorAll('.thread').forEach((t) => (t.style.top = '')); return; }
      const mTop = margin.getBoundingClientRect().top;
      let cursor = 0;
      const head = margin.querySelector('.panelhead');
      if (head) cursor = head.offsetHeight + 8;
      const placed = Array.from(margin.querySelectorAll(':scope > .thread'));
      for (const t of placed) {
        const el = byAnchor.get(t.dataset.anchor);
        const want = el ? el.getBoundingClientRect().top - mTop - 10 : cursor;
        const top = Math.max(want, cursor);
        t.style.top = `${top}px`;
        cursor = top + t.offsetHeight + 10;
      }
      const orph = margin.querySelector('.orphans');
      if (orph) {
        orph.style.position = 'absolute';
        orph.style.left = '0';
        orph.style.right = '0';
        orph.style.top = `${cursor + 12}px`;
        cursor += orph.offsetHeight + 24;
      }
      margin.style.minHeight = `${cursor}px`;
    }

    function updateSheetButton(n) {
      if (!narrowMq.matches) { sheetBtn?.remove(); sheetBtn = null; return; }
      if (!sheetBtn) {
        sheetBtn = document.createElement('button');
        sheetBtn.type = 'button';
        sheetBtn.className = 'btn';
        sheetBtn.onclick = () => margin.classList.add('open');
        $('.tools')?.prepend(sheetBtn);
      }
      sheetBtn.textContent = `Poznámky (${n})`;
    }

    narrowMq.addEventListener('change', () => { closeSheet(); render(); });
    addEventListener('resize', () => { clearTimeout(rT); rT = setTimeout(layout, 120); });
    document.fonts?.ready.then(layout);
    $$('.toc a').forEach((a) => a.addEventListener('click', () => { a.closest('details').open = false; }));

    async function load(first) {
      try {
        const r = await api(`/api/comments?doc=${encodeURIComponent(D.doc)}`);
        const typing = margin.querySelector('.composer textarea');
        if (!first && typing && typing.value.trim()) return;
        if (!first && JSON.stringify(r.comments) === JSON.stringify(ctx.comments)) return;
        ctx.comments = r.comments;
        render();
        if (first) handleHash();
      } catch (err) {
        if (first) { margin.innerHTML = `<p class="empty">${esc(err.message)}</p>`; }
      }
    }
    function handleHash() {
      const h = location.hash;
      let anchor = null;
      if (h.startsWith('#b=')) anchor = decodeURIComponent(h.slice(3));
      if (h.startsWith('#c=')) {
        const id = Number(h.slice(3));
        const c = ctx.comments.find((x) => x.id === id);
        if (c) {
          ctx.activeId = c.parent_id || c.id;
          if (c.resolved) ctx.showResolved = true;
          anchor = c.anchor;
          render();
          openSheet();
        }
      }
      if (!anchor || anchor === '_doc') return;
      if (kind === 'md') {
        const el = byAnchor.get(anchor);
        if (el) { setTimeout(() => { el.scrollIntoView({ block: 'center' }); flash(el); }, 60); }
      } else ctx.goto(anchor, ctx.activeId);
    }
    load(true);
    setInterval(() => { if (document.visibilityState === 'visible') load(false); }, 25000);
    addEventListener('hashchange', handleHash);

    // --- present mode
    const presentBtn = $('[data-act="present"]');
    function setPresent(on) {
      document.body.classList.toggle('present', on);
      if (on) {
        hint = document.createElement('div');
        hint.className = 'presenthint np-ui';
        hint.innerHTML = '<span><kbd>←</kbd> <kbd>→</kbd> kapitoly</span><span><kbd>Esc</kbd> konec</span><button type="button" class="btn">Ukončit</button>';
        hint.querySelector('button').onclick = () => setPresent(false);
        document.body.append(hint);
        $('.dochead').scrollIntoView();
      } else {
        hint?.remove();
        layout();
      }
    }
    presentBtn?.addEventListener('click', () => setPresent(true));
    document.addEventListener('keydown', (e) => {
      if (e.target.closest('input, textarea, select, [contenteditable]')) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      if (kind === 'md' && (e.key === 'p' || e.key === 'P')) { e.preventDefault(); setPresent(!document.body.classList.contains('present')); return; }
      if (e.key === 'Escape') {
        if (document.body.classList.contains('present')) setPresent(false);
        else if (picking) setPicking(false);
        else if (margin.classList.contains('open')) closeSheet();
        return;
      }
      if (!document.body.classList.contains('present')) return;
      const heads = [$('.dochead h1'), ...$$('#doc h2')].filter(Boolean);
      const y = 8;
      if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(e.key)) {
        const next = heads.find((h) => h.getBoundingClientRect().top > y + 4);
        if (next) { e.preventDefault(); next.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
      } else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) {
        const prev = heads.filter((h) => h.getBoundingClientRect().top < y - 4).pop();
        if (prev) { e.preventDefault(); prev.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
      }
    });
  }

  // ---------- feedback overview ----------
  const fbList = $('#feedback-list');
  if (fbList) initFeedback();

  function initFeedback() {
    const state = $('[data-filter="state"]');
    const author = $('[data-filter="author"]');
    const ctx = { comments: [], expanded: new Set(), render };
    wireThreads(fbList, ctx);
    async function load() {
      try {
        ctx.comments = (await api('/api/comments')).comments.reverse();
        render();
      } catch (err) { fbList.innerHTML = `<p class="empty">${esc(err.message)}</p>`; }
    }
    function render() {
      const want = state.value;
      const who = author.value;
      const threads = threadsFrom(ctx.comments).filter((t) => {
        if (want === 'open' && t.root.resolved) return false;
        if (want === 'resolved' && !t.root.resolved) return false;
        if (who && t.root.author !== who && !t.replies.some((r) => r.author === who)) return false;
        return true;
      });
      fbList.innerHTML = '';
      if (!threads.length) {
        fbList.innerHTML = `<p class="empty">${ctx.comments.length ? 'Tomuto filtru nic neodpovídá.' : '<b>Zatím tu nejsou žádné poznámky.</b> Otevřete libovolný podklad a přidejte první poznámku k odstavci.'}</p>`;
        return;
      }
      const order = (D.docs || []).map((d) => d.id);
      const byDoc = new Map();
      for (const t of threads) (byDoc.get(t.root.doc) || byDoc.set(t.root.doc, []).get(t.root.doc)).push(t);
      const docIds = Array.from(byDoc.keys()).sort((a, b) => order.indexOf(a) - order.indexOf(b));
      for (const id of docIds) {
        const d = docsById[id] || { title: id, route: '/', section: '' };
        const sec = (D.sections || []).find((s) => s.id === d.section);
        const box = document.createElement('section');
        box.className = 'fbdoc';
        const list = byDoc.get(id);
        box.innerHTML = `<h2>${sec ? `<span class="num">${sec.num}</span>` : ''}<a href="${d.route}">${esc(d.title)}</a><small>${plural(list.length, 'vlákno', 'vlákna', 'vláken')}</small></h2>`;
        const m = document.createElement('div');
        m.className = 'margin list';
        for (const t of list) {
          const el = threadEl(t, { expanded: ctx.expanded, quote: true, link: `${d.route}#c=${t.root.id}` });
          el.dataset.doc = id;
          m.append(el);
        }
        box.append(m);
        fbList.append(box);
      }
    }
    state.addEventListener('change', render);
    author.addEventListener('change', render);
    load();
  }
  // ---------- quick-overview slides ----------
  for (const q of $$('.quick')) {
    const slides = $$('.dslide', q);
    const view = $('.deckview', q);
    const count = $('.qcount', q);
    const dots = $$('.qdots button', q);
    let at = 0;
    const show = (i) => {
      at = Math.max(0, Math.min(slides.length - 1, i));
      slides.forEach((sl, k) => { sl.hidden = k !== at; sl.classList.toggle('on', k === at); });
      dots.forEach((d, k) => (k === at ? d.setAttribute('aria-current', 'true') : d.removeAttribute('aria-current')));
      count.textContent = `${at + 1} / ${slides.length}`;
    };
    q.addEventListener('click', (e) => {
      const b = e.target.closest('[data-q]');
      if (!b) return;
      const v = b.dataset.q;
      if (v === 'prev') show(at - 1);
      else if (v === 'next') show(at + 1);
      else if (v === 'full') (view.requestFullscreen ? view.requestFullscreen() : null)?.then?.(() => view.focus());
      else show(Number(v));
      if (v !== 'full') history.replaceState(null, '', `#s${at + 1}`);
    });
    view.addEventListener('keydown', (e) => {
      if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(at + 1); }
      if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(at - 1); }
      if (e.key === 'Home') show(0);
      if (e.key === 'End') show(slides.length - 1);
    });
    view.addEventListener('click', (e) => {
      if (e.target.closest('a')) return;
      if (document.fullscreenElement === view) show(at + 1);
    });
    let x0 = null;
    view.addEventListener('pointerdown', (e) => { x0 = e.clientX; });
    view.addEventListener('pointerup', (e) => {
      if (x0 === null) return;
      const dx = e.clientX - x0;
      x0 = null;
      if (Math.abs(dx) > 50) show(at + (dx < 0 ? 1 : -1));
    });
    const m = location.hash.match(/^#s(\d+)$/);
    if (m) { show(Number(m[1]) - 1); q.scrollIntoView(); }
  }

  // ---------- assistant ----------
  function md(src) {
    const inline = (t) =>
      esc(t)
        .replace(/`([^`]+)`/g, '<code>$1</code>')
        .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
        .replace(/\[([^\]]+)\]\(((?:https?:\/\/|\/)[^)\s]+)\)/g, (m, txt, url) => {
          const same = url.startsWith('/') || url.startsWith(location.origin);
          return `<a href="${url}"${same ? '' : ' target="_blank" rel="noopener"'}>${txt}</a>`;
        });
    const lines = String(src).replace(/\r/g, '').split('\n');
    let out = '';
    let list = null;
    let table = [];
    const flushList = () => { if (list) { out += `</${list}>`; list = null; } };
    const flushTable = () => {
      if (!table.length) return;
      const rows = table.filter((r) => !/^\|?\s*:?-{2,}/.test(r)).map((r) => r.replace(/^\||\|$/g, '').split('|').map((c) => inline(c.trim())));
      out += `<div class="tablewrap"><table><thead><tr>${rows[0].map((c) => `<th>${c}</th>`).join('')}</tr></thead><tbody>${rows.slice(1).map((r) => `<tr>${r.map((c) => `<td>${c}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
      table = [];
    };
    for (const raw of lines) {
      const l = raw.trimEnd();
      if (/^\s*\|.*\|\s*$/.test(l)) { flushList(); table.push(l.trim()); continue; }
      flushTable();
      let m;
      if ((m = l.match(/^\s*[-*]\s+(.*)/))) { if (list !== 'ul') { flushList(); out += '<ul>'; list = 'ul'; } out += `<li>${inline(m[1])}</li>`; continue; }
      if ((m = l.match(/^\s*\d+[.)]\s+(.*)/))) { if (list !== 'ol') { flushList(); out += '<ol>'; list = 'ol'; } out += `<li>${inline(m[1])}</li>`; continue; }
      flushList();
      if ((m = l.match(/^#{1,4}\s+(.*)/))) { out += `<p class="h">${inline(m[1])}</p>`; continue; }
      if (l.trim()) out += `<p>${inline(l)}</p>`;
    }
    flushList();
    flushTable();
    return out;
  }

  const chatState = {
    scope: D.doc ? (sessionStorage.getItem('np-chat-scope') || 'doc') : 'all',
    busy: false,
  };
  const chatKey = () => `np-chat-${chatState.scope === 'doc' ? D.doc : 'all'}`;
  const loadHist = () => { try { return JSON.parse(sessionStorage.getItem(chatKey()) || '[]'); } catch { return []; } };
  const saveHist = (h) => sessionStorage.setItem(chatKey(), JSON.stringify(h.slice(-30)));
  let chatEl;

  function buildChat() {
    chatEl = document.createElement('aside');
    chatEl.className = 'chat';
    chatEl.setAttribute('aria-label', 'Asistent');
    const docTitle = D.doc ? (docsById[D.doc]?.title || 'Tento dokument') : '';
    chatEl.innerHTML = `
      <div class="chathead">
        <h2>Asistent</h2>
        ${D.doc ? `<div class="scope" role="group" aria-label="Rozsah"><button type="button" data-scope="doc" title="${esc(docTitle)}">Tento dokument</button><button type="button" data-scope="all">Všechny podklady</button></div>` : '<span class="scope-note">Všechny podklady</span>'}
        <span class="chatacts"><button type="button" class="textbtn" data-chat="clear">Nový dotaz</button><button type="button" class="iconbtn" data-chat="close" aria-label="Zavřít asistenta">${ICONS.close}</button></span>
      </div>
      <div class="chatlog" aria-live="polite"></div>
      <form class="chatform">
        <textarea rows="2" aria-label="Otázka pro asistenta" placeholder="Zeptejte se na cokoli z podkladů, nebo ať něco spočítá…" maxlength="4000"></textarea>
        <button class="btn primary" type="submit">Zeptat se</button>
      </form>`;
    document.body.append(chatEl);
    const ta = $('textarea', chatEl);
    ta.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); $('form', chatEl).requestSubmit(); }
      if (e.key === 'Escape') toggleChat(false);
    });
    $('form', chatEl).addEventListener('submit', (e) => { e.preventDefault(); ask(ta.value); });
    chatEl.addEventListener('click', (e) => {
      const b = e.target.closest('[data-chat],[data-scope],[data-suggest]');
      if (!b) return;
      if (b.dataset.chat === 'close') toggleChat(false);
      if (b.dataset.chat === 'clear') { saveHist([]); renderChat(); ta.focus(); }
      if (b.dataset.scope) { chatState.scope = b.dataset.scope; sessionStorage.setItem('np-chat-scope', chatState.scope); renderChat(); ta.focus(); }
      if (b.dataset.suggest) ask(b.dataset.suggest);
    });
  }

  function renderChat() {
    const log = $('.chatlog', chatEl);
    $$('[data-scope]', chatEl).forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.scope === chatState.scope)));
    const hist = loadHist();
    if (!hist.length && !chatState.busy) {
      const sugg = chatState.scope === 'doc'
        ? ['Shrň mi tento dokument v pěti bodech', 'Co je tady otevřené nebo nerozhodnuté?', 'Jaké poznámky k tomu už padly?']
        : ['Co je potřeba rozhodnout na příští poradě?', 'Kolik nových titulů plánujeme v roce 2027 a které?', 'Jak funguje PvP na startu a proč?', 'Jak si připojím vlastního Clauda?'];
      log.innerHTML = `<div class="chatempty"><p>Odpovídám z podkladů v portálu a u každé odpovědi uvedu zdroj. Umím i počítat.</p><div class="sugg">${sugg.map((t) => `<button type="button" data-suggest="${esc(t)}">${esc(t)}</button>`).join('')}</div></div>`;
      return;
    }
    log.innerHTML = hist
      .map((m) => (m.role === 'user'
        ? `<div class="msg user"><span class="who" style="--c:${colorOf(me)}">${esc(me || 'Vy')}</span><p>${esc(m.content)}</p></div>`
        : `<div class="msg bot${m.error ? ' error' : ''}">${m.error ? `<p>${esc(m.content)}</p>` : md(m.content)}</div>`))
      .join('') + (chatState.busy ? '<div class="msg bot busy"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span> Hledám v podkladech…</div>' : '');
    log.scrollTop = log.scrollHeight;
  }

  async function ask(q) {
    q = String(q || '').trim();
    if (!q || chatState.busy) return;
    const ta = $('textarea', chatEl);
    ta.value = '';
    const hist = loadHist();
    hist.push({ role: 'user', content: q });
    saveHist(hist);
    chatState.busy = true;
    renderChat();
    try {
      const r = await api('/api/chat', { method: 'POST', body: { messages: hist.filter((m) => !m.error).map(({ role, content }) => ({ role, content })), doc: chatState.scope === 'doc' ? D.doc : undefined } });
      hist.push({ role: 'assistant', content: r.answer });
    } catch (err) {
      hist.push({ role: 'assistant', content: err.message, error: true });
    }
    saveHist(hist);
    chatState.busy = false;
    renderChat();
    ta.focus();
  }

  function toggleChat(open) {
    if (!chatEl) buildChat();
    const on = open ?? !document.body.classList.contains('chat-open');
    document.body.classList.toggle('chat-open', on);
    sessionStorage.setItem('np-chat-open', on ? '1' : '');
    if (on) { renderChat(); setTimeout(() => $('textarea', chatEl).focus(), 50); }
  }
  document.addEventListener('click', (e) => { if (e.target.closest('[data-act="chat"]')) toggleChat(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && !e.target.closest('input, textarea, select, [contenteditable]') && !e.metaKey && !e.ctrlKey) { e.preventDefault(); toggleChat(true); }
  });
  if (sessionStorage.getItem('np-chat-open') && $('[data-act="chat"]')) toggleChat(true);

  // ---------- settings: MCP tokens ----------
  if (document.body.classList.contains('settingspage')) {
    $$('[data-me]').forEach((el) => { el.textContent = me || 'nikdo'; el.style.color = colorOf(me); });
    $$('pre.cmd, [data-origin]').forEach((el) => { el.textContent = el.textContent.replace('ORIGIN', location.origin); });
    const list = $('[data-toklist]');
    const fresh = $('[data-newtoken]');
    const loadTokens = async () => {
      try {
        const { tokens } = await api('/api/tokens');
        list.innerHTML = tokens.length
          ? `<ul class="toklist">${tokens.map((t) => `<li><span><b>${esc(t.label)}</b><small>${esc(t.prefix)}… · vytvořen ${ago(t.created_at)} · ${t.last_used_at ? `naposledy použit ${ago(t.last_used_at)}` : 'zatím nepoužit'}</small></span><button type="button" class="btn" data-revoke="${t.id}">Zrušit</button></li>`).join('')}</ul>`
          : '<p class="muted">Zatím nemáte žádný token.</p>';
      } catch (err) { list.innerHTML = `<p class="muted">${esc(err.message)}</p>`; }
    };
    list.addEventListener('click', async (e) => {
      const b = e.target.closest('[data-revoke]');
      if (!b) return;
      if (!b.dataset.armed) { b.dataset.armed = '1'; b.textContent = 'Opravdu zrušit?'; setTimeout(() => { if (b.isConnected) { delete b.dataset.armed; b.textContent = 'Zrušit'; } }, 4000); return; }
      try { await api(`/api/tokens/${b.dataset.revoke}`, { method: 'DELETE' }); toast('Token je zrušený'); loadTokens(); } catch (err) { toast(err.message); }
    });
    $('[data-tokform]').addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = $('[type=submit]', e.target);
      btn.disabled = true;
      try {
        const r = await api('/api/tokens', { method: 'POST', body: { label: e.target.label.value } });
        const cmd = `claude mcp add --transport http noxgames-navrhy ${location.origin}/mcp --header "Authorization: Bearer ${r.token}"`;
        fresh.hidden = false;
        fresh.innerHTML = `<div class="newtok"><p><b>Nový token „${esc(r.label)}“.</b> Zkopírujte si ho teď, znovu se nezobrazí.</p><pre class="cmd">${esc(r.token)}</pre><button type="button" class="btn" data-copy="${esc(r.token)}">Zkopírovat token</button><p>Příkaz pro Claude Code s vloženým tokenem:</p><pre class="cmd">${esc(cmd)}</pre><button type="button" class="btn primary" data-copy="${esc(cmd)}">Zkopírovat příkaz</button></div>`;
        e.target.reset();
        loadTokens();
      } catch (err) { toast(err.message); }
      btn.disabled = false;
    });
    document.addEventListener('click', (e) => {
      const b = e.target.closest('[data-copy]');
      if (b) navigator.clipboard?.writeText(b.dataset.copy).then(() => toast('Zkopírováno'), () => toast('Kopírování selhalo, označte text ručně'));
    });
    loadTokens();
  }
})();
