// Pulls all comments from production D1 into FEEDBACK.md, grouped by source file.
// Usage: npm run feedback            (open threads only)
//        npm run feedback -- --all   (include resolved)
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const all = process.argv.includes('--all');
const local = process.argv.includes('--local');

if (!fs.existsSync(path.join(ROOT, 'manifest.local.json'))) execFileSync('node', ['scripts/build.mjs'], { cwd: ROOT, stdio: 'inherit' });
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, 'manifest.local.json'), 'utf8'));
const byId = Object.fromEntries(manifest.map((d) => [d.id, d]));

const out = execFileSync(
  'npx',
  ['wrangler', 'd1', 'execute', 'noxgames-proposals', local ? '--local' : '--remote', '--json', '--command',
    'SELECT id, doc, anchor, quote, parent_id, author, body, resolved, resolved_by, created_at FROM comments WHERE deleted = 0 ORDER BY id'],
  { cwd: ROOT, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 },
);
const rows = JSON.parse(out)[0].results;

const roots = rows.filter((r) => !r.parent_id && (all || !r.resolved));
const replies = (id) => rows.filter((r) => r.parent_id === id);
const order = manifest.map((d) => d.id);
const docs = [...new Set(roots.map((r) => r.doc))].sort((a, b) => order.indexOf(a) - order.indexOf(b));

const lines = [
  '# Feedback z portálu Návrhy 2027',
  '',
  `Staženo ${new Date().toLocaleString('cs-CZ')} · ${roots.length} ${all ? 'vláken (včetně vyřešených)' : 'otevřených vláken'}.`,
  'Každé vlákno: citace místa v dokumentu, pak poznámky. Po zapracování vlákno v portálu označte jako vyřešené.',
  '',
];
for (const id of docs) {
  const d = byId[id];
  lines.push(`## ${d ? d.title : id}`, '', d ? `Zdroj: \`${d.src}\` · portál: \`${d.route}\`` : `Dokument \`${id}\` už není v content.json`, '');
  for (const r of roots.filter((x) => x.doc === id)) {
    lines.push(`### #${r.id}${r.resolved ? ` (vyřešeno, ${r.resolved_by})` : ''}`);
    lines.push(r.anchor === '_doc' ? '> K celému dokumentu' : `> ${String(r.quote || '').replace(/\n/g, ' ')}`, '');
    for (const c of [r, ...replies(r.id)]) lines.push(`- **${c.author}** (${c.created_at.slice(0, 16)}): ${c.body.replace(/\n+/g, ' / ')}`);
    lines.push('');
  }
}
fs.writeFileSync(path.join(ROOT, 'FEEDBACK.md'), lines.join('\n'));
console.log(`FEEDBACK.md: ${roots.length} threads in ${docs.length} docs`);
