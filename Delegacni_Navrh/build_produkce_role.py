#!/usr/bin/env python3
"""Build priprava-produkce-2026-10-08-role-a-cinnosti-light.html.

Light card layout matching the Operations podklad (Martin B.): role table first, then
activities by area with a detail line, role and current holder. Run: python3 build_produkce_role.py
"""
import html
from pathlib import Path

ROLES = {
    "R1": "Vlastník segmentu",
    "R2": "Project lead",
    "R3": "Game designer",
    "R4": "Programátor",
    "R5": "Odborná autorita tech",
    "R6": "Grafik DEV",
    "R7": "Odborná autorita art",
    "R8": "Publishing a LiveOps lead",
    "R9": "QA lead",
    "R10": "B2B lead",
    "R11": "Produktový analytik",
    "R12": "Správce backendu a nástrojů",
    "R13": "Tester a komunitní správce",
}

# (kód, role, činnosti, poznámka k roli, kdo, poznámka ke kdo)
ROLE_ROWS = [
    ("R1", "Ř1 plán a roadmapa · Ř2 kapacity a obsazení · Ř3 vedení lidí · Ř4 rozpočet a reporting · V6 R&D a greenlight",
     "ručí za výsledky, budget a lidi segmentu; rozhoduje priority mezi projekty", "David Vykopal", "zástup za plán a kapacity: Aldy"),
    ("R2", "V4 vedení projektu · V7 outsourcing",
     "denní priority, zadání pro kód a art, spory v projektu; může člověka vyřadit z projektu", "David Bém (Aldy), Karel Kunc (Karlík)", "každý na svých titulech, zastupují se vzájemně"),
    ("R3", "V1 herní design a ekonomika",
     "mechaniky, balanc a parametry uvnitř schváleného modelu", "Aldy, Karlík", "stejní lidé jako R2, role je oddělená"),
    ("R4", "V2 programování · výroba B2 a B3",
     "způsob provedení a technické řešení uvnitř standardu", "Jan Ševčík (Čoud), Milan Vavro, Mirek, Hutis", ""),
    ("R5", "V5 technický dluh, pipeline a engine",
     "standard, review a arbitráž technických sporů; nevede lidi a neručí za dodání", "Miroslav Schery (Mirek)", "zástup: Čoud"),
    ("R6", "V3 herní art a UI",
     "art a UI v buildu podle plánu sprintu", "David Čalta, Peko", "Aldy a Karlík se podílejí na vlastních titulech"),
    ("R7", "review a standard ve V3",
     "vizuální standard, review a mentoring grafiků; nevede lidi", "Petr (Peko)", ""),
    ("R8", "P2 release a platformy · P3 compliance · P4 LiveOps · P5 provoz produktů",
     "provozní releasy a hotfixy, liveops kalendář, monetizační parametry uvnitř modelu", "Martin Vajsar (Akimo)", "zástup: David"),
    ("R9", "P1 QA a release readiness",
     "testplán, evidence chyb, právo zastavit release", "Jakub Hutečka (Hutis)", "release gate drží Akimo"),
    ("R10", "B1 pipeline a nabídky · B2 delivery",
     "scoping a cena nad prahem marže, klient, marže zakázky", "David Vykopal", "bez vlastního člověka; zástup delivery: Čoud"),
    ("R11", "D1 datový stack a metriky · D2 herní analytika",
     "role Produkce, kterou přechodně vykonává Marketing", "Jakub Burian (Kuba)", "přechodně do 31. 12. 2026"),
    ("R12", "D3 herní backend a tooling · D4 web a CPI stránky",
     "Shared Game Backend a nástroje zrychlující vývoj; NoxHub sem nepatří", "David Vykopal", "bez zástupu"),
    ("R13", "P6 komunita a support · testování v P1",
     "půl QA, půl komunita; nábor v Q4", "neosazeno", "P6 do nástupu reaktivně Akimo"),
]

# oblast: (písmeno, název, [(kód, činnost, detail, role, poznámka k roli, kdo, poznámka ke kdo)])
AREAS = [
    ("Ř", "Řízení segmentu", [
        ("Ř1", "Plán produkce a roadmapa titulů: sprinty, milníky, priority mezi projekty",
         "bez plánu si každý projekt plánuje sám a o prioritách rozhoduje ten, kdo je nejhlasitější", "R1", "", "David Vykopal", "zástup Aldy"),
        ("Ř2", "Kapacitní plánování a obsazení projektů",
         "kdo na čem dělá v jakém sprintu, včetně rezervace pro B2B a playables; plánuje se na 75 % úvazku", "R1", "", "David Vykopal", "zástup Aldy"),
        ("Ř3", "Vedení lidí v segmentu: 1:1, cíle, hodnocení, odměna, odborný onboarding",
         "o odměně a setrvání rozhoduje vlastník segmentu, mentoři a project leadi dávají návrhy", "R1", "", "David Vykopal", ""),
        ("Ř4", "Rozpočet a reporting segmentu",
         "návrh rozpočtu, čerpání a měsíční čísla připravená bez vyžádání; CEO reporty jen sbírá", "R1", "", "David Vykopal", ""),
    ]),
    ("V", "Vývoj her", [
        ("V1", "Herní design a ekonomika titulů: mechaniky, progres, balanc, monetizační model",
         "změna parametru je rozhodnutí designéra, změna monetizačního modelu jde přes vlastníka segmentu", "R3", "", "Aldy, Karlík", ""),
        ("V2", "Programování a technická architektura: feature, opravy, integrace SDK, výkon",
         "technický spor mezi projekty rozhoduje odborná autorita tech", "R4", "arbitráž R5", "Čoud, Milan, Mirek, Hutis", ""),
        ("V3", "Herní art a UI: postavy, prostředí, UI, animace do buildu",
         "zadání jde přes project leada, kvalitu drží odborná autorita art; art lead se nezřizuje", "R6", "review R7", "David Čalta, Peko", "Aldy a Karlík se podílejí"),
        ("V4", "Vedení projektu: denní priority, zadání pro kód a art, stav do hubu",
         "dosud nevyčíslené; design leadership je součást role, samostatný GD lead se nezřizuje", "R2", "", "Aldy, Karlík", "každý na svých titulech"),
        ("V5", "Technický dluh, build pipeline a engine: verze Unity, build stroje, sdílené knihovny, standard kódu",
         "tech lead napříč tituly se zatím nezřizuje, technická rozhodnutí se dělají per projekt", "R5", "", "Mirek", "zástup Čoud"),
        ("V6", "R&D: prototypy a podklad pro greenlight",
         "nejvýš 2 sprinty na koncept, pak rozhodnutí; greenlight plné produkce schvaluje CEO", "R1", "tým podle konceptu", "David Vykopal", "s Aldym nebo Karlíkem"),
        ("V7", "Outsourcing a externí dodávky: zadání, převzetí a kontrola",
         "zadání a převzetí dělá project lead, smlouvu a budget drží vlastník segmentu", "R2", "smlouva a budget R1", "David Vykopal", "návrh: předat Aldymu a Karlíkovi"),
    ]),
    ("P", "Publishing a LiveOps", [
        ("P1", "QA a release readiness: testplán, evidence chyb, rozhodnutí o připravenosti buildu",
         "QA lead může zastavit release; vydat build se známou chybou schvaluje vlastník segmentu", "R9", "testování R13", "Hutis", "release gate Akimo"),
        ("P2", "Release management a platformy: store konzole, review, game setup, rollout",
         "co je v buildu a kdy jde ven, je Produkce; store page, ASO a kampaň je Marketing", "R8", "", "Akimo", "zástup David"),
        ("P3", "Produktová compliance: privacy, rating, ATT, licence assetů ve hře",
         "reklamní a atribuční compliance je Marketing, firemní právní a smluvní Operations", "R8", "", "Akimo", ""),
        ("P4", "LiveOps vydaných titulů: eventy, kalendář, battle pass, provozní monetizace",
         "hlavní téma Q4; parametry uvnitř modelu rozhoduje lead, změna modelu je eskalace", "R8", "", "Akimo", "zástup David"),
        ("P5", "Provoz produktů: servery, produktový cloud, monitoring, incidenty",
         "", "R8", "", "Akimo", ""),
        ("P6", "Komunita hráčů, in-game komunikace a support",
         "dnes jen reaktivně; značka a PR je Marketing, krizová komunikace CEO", "R13", "do nástupu R8", "neosazeno", "reaktivně Akimo"),
    ]),
    ("B", "B2B", [
        ("B1", "B2B pipeline a nabídky: scoping, pricing podle interních tarifů, dojednání",
         "v Q4 bez outreache; zakázku pod prahem marže nebo s exkluzivitou schvaluje CEO", "R10", "", "David Vykopal", ""),
        ("B2", "B2B delivery: vedení zakázky, klient, kontrola dodávky",
         "klient a marže zůstávají u B2B leada, výroba jde po zakázkách na programátory", "R10", "výroba R4", "David Vykopal", "výroba podle zakázky"),
        ("B3", "Playable ads pro Marketing",
         "interní zakázka: zadání a pořadí z Marketingu (jejich K4), výroba stejnou pipeline jako B2B", "R4", "zadává Marketing", "k potvrzení", "jméno a kapacita do 22. 10."),
    ]),
    ("D", "Data a produkční nástroje", [
        ("D1", "Datový stack, eventy v buildech a definice metrik",
         "aby celá firma četla jedno číslo; vlastní Produkce, vykonává Marketing", "R11", "", "Kuba", "přechodně do 31. 12."),
        ("D2", "Herní analytika: čtení dat, doporučení k ladění, vyhodnocení A/B testů",
         "po 31. 12. je potřeba rozhodnout: nábor, trvalé hostování, nebo automatické reporty", "R11", "", "Kuba", "David se podílí"),
        ("D3", "Herní backend a produkční tooling: Shared Game Backend, extrakce playables",
         "NoxHub a AMA patří do Operations; každý nový nástroj má business case", "R12", "", "David Vykopal", "bez zástupu"),
        ("D4", "Firemní web a produktové a CPI stránky: technický provoz a nasazení",
         "obsah a marketingové části dodává Marketing", "R12", "", "David Vykopal", ""),
    ]),
]

CSS = """
:root{--bg:#f4f6f9;--card:#fff;--head:#f5f7fa;--ink:#1c2430;--muted:#5f6b7a;--faint:#8a94a3;--line:#e3e8ee;--line-strong:#d5dce5;--teal:#2f7d74;--shadow:0 1px 2px rgba(16,24,40,.04),0 12px 32px -12px rgba(16,24,40,.12)}
:root[data-theme="dark"]{--bg:#11151b;--card:#181e26;--head:#1e252f;--ink:#e8edf3;--muted:#a3adba;--faint:#7f8a98;--line:#2a323d;--line-strong:#36404d;--teal:#5fc4b6;--shadow:0 1px 2px rgba(0,0,0,.3),0 12px 32px -12px rgba(0,0,0,.5)}
.theme{position:absolute;top:0;right:0;min-height:44px;padding:0 16px;border:1px solid var(--line-strong);border-radius:999px;background:var(--card);color:var(--muted);font:inherit;font-size:.875rem;cursor:pointer}
.theme:hover{color:var(--ink)}
.theme:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
header{position:relative;padding-right:150px}
*{box-sizing:border-box;margin:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font:16px/1.5 Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-variant-numeric:tabular-nums;padding:48px 16px 80px}
::selection{background:var(--teal);color:var(--card)}
main{max-width:1180px;margin:0 auto}
header{margin-bottom:40px}
h1{font-size:clamp(1.6rem,3.4vw,2.1rem);font-weight:700;letter-spacing:-.02em;line-height:1.2;text-wrap:balance}
.lede{color:var(--muted);margin-top:10px;max-width:70ch}
.meta{color:var(--faint);font-size:.875rem;margin-top:14px}
h2{font-size:1.25rem;font-weight:700;letter-spacing:-.01em;margin:44px 0 6px}
h2+p{color:var(--muted);max-width:75ch;margin-bottom:8px}
h3{display:flex;align-items:baseline;gap:10px;font-size:1.125rem;font-weight:700;margin:32px 0 12px}
h3 .k{color:var(--teal);font-size:.75rem;font-weight:700;width:1em}
h3 .n{color:var(--faint);font-size:.8125rem;font-weight:400}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);overflow:hidden}
table{width:100%;border-collapse:collapse}
th{background:var(--head);color:var(--muted);font-size:.6875rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;text-align:left;padding:14px 16px;border-bottom:2px solid var(--line-strong)}
td{padding:14px 16px;vertical-align:top;border-top:1px solid var(--line)}
tbody tr:first-child td{border-top:0}
th:first-child,td:first-child{padding-left:20px}
th:last-child,td:last-child{padding-right:20px}
.code{color:var(--teal);font-weight:700;white-space:nowrap;width:1%}
.sub{display:block;color:var(--muted);font-size:.875rem;margin-top:4px}
.rc{color:var(--teal);font-weight:700}
.w-role{width:24%}.w-who{width:23%}.w-rolename{width:21%}
.note{color:var(--muted);font-size:.9375rem;max-width:75ch;margin-top:16px}
@media (max-width:760px){
 body{padding:28px 16px 56px}
 thead{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
 table,tbody,tr,td{display:block;width:auto}
 tr{padding:14px 16px;border-top:1px solid var(--line)}
 tbody tr:first-child{border-top:0}
 td,td:first-child,td:last-child{padding:0;border:0}
 td+td{margin-top:8px}
 td[data-l]::before{content:attr(data-l);display:block;color:var(--faint);font-size:.6875rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:2px}
 .code,.w-role,.w-who,.w-rolename{width:auto}
 .w-rolename{font-weight:600}
 header{padding-right:0}.theme{position:static;margin-bottom:16px}
}
@media print{.theme{display:none}body{background:#fff;padding:0}.card{box-shadow:none}tr{break-inside:avoid}}
"""

e = html.escape


def sub(text):
    return f'<span class="sub">{e(text)}</span>' if text else ""


def role_cell(code, note):
    return f'<span class="rc">{code}</span> {e(ROLES[code])}{sub(note)}'


def build():
    out = []
    out.append('<h2>Role v produkci</h2><p>Názvy rolí jsou pracovní. Jeden člověk může nést víc rolí; kde roli nese víc lidí, potvrzuje se hlavní nositel.</p>')
    out.append('<div class="card"><table><thead><tr><th>#</th><th>Role</th><th>Činnosti</th><th>Kdo aktuálně zastává</th></tr></thead><tbody>')
    for code, acts, rnote, who, wnote in ROLE_ROWS:
        out.append(
            f'<tr><td class="code">{code}</td><td class="w-rolename">{e(ROLES[code])}</td>'
            f'<td data-l="Činnosti">{e(acts)}{sub(rnote)}</td><td class="w-who" data-l="Kdo aktuálně zastává">{e(who)}{sub(wnote)}</td></tr>'
        )
    out.append('</tbody></table></div>')
    out.append('<p class="note">Art lead, GD lead a tech lead napříč tituly se vědomě nezřizují. NoxHub, evidence licencí a zařízení a AI vzdělávání patří do Operations. Práce pro Operations (Akimo: kanceláře a onboarding zázemí, Hutis: DevOps a IT) je mimo činnosti segmentu, stejně jako exec agenda.</p>')

    out.append('<h2>Činnosti podle oblastí</h2><p>Kódy jsou pracovní označení této verze. Samostatný řádek neznamená automaticky další kapacitu.</p>')
    for i, (letter, name, rows) in enumerate(AREAS, 1):
        out.append(f'<h3><span class="k">{letter}</span>{e(name)}<span class="n">(2.{i})</span></h3>')
        out.append('<div class="card"><table><thead><tr><th>#</th><th>Činnost</th><th>Role</th><th>Kdo aktuálně zastává</th></tr></thead><tbody>')
        for code, act, detail, role, rnote, who, wnote in rows:
            out.append(
                f'<tr><td class="code">{code}</td><td>{e(act)}{sub(detail)}</td>'
                f'<td class="w-role" data-l="Role">{role_cell(role, rnote)}</td>'
                f'<td class="w-who" data-l="Kdo aktuálně zastává">{e(who)}{sub(wnote)}</td></tr>'
            )
        out.append('</tbody></table></div>')

    doc = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Produkce: role a činnosti · NOXGAMES</title>
<style>{CSS}</style>
</head>
<body>
<main>
<header>
<button class="theme" type="button" id="theme">Tmavý režim</button>
<h1>Produkce: role a činnosti</h1>
<p class="lede">Účel segmentu: hry vznikají, vycházejí, žijí a zaplatí se. Třináct rolí, pět oblastí, 24 činností. U každé činnosti je role, která ji nese, a kdo ji zastává dnes.</p>
<p class="meta">Podklad k delegační poradě 8. 10. 2026 · vlastník segmentu David Vykopal · NOXGAMES, interní</p>
</header>
{''.join(out)}
</main>
<script>
(function(){{var r=document.documentElement,b=document.getElementById('theme'),k='produkce-role-theme';
function set(t){{if(t==='dark'){{r.setAttribute('data-theme','dark');b.textContent='Světlý režim'}}else{{r.removeAttribute('data-theme');b.textContent='Tmavý režim'}}}}
var saved=null;try{{saved=localStorage.getItem(k)}}catch(e){{}}set(saved);
b.addEventListener('click',function(){{var t=r.getAttribute('data-theme')==='dark'?'light':'dark';set(t);try{{localStorage.setItem(k,t)}}catch(e){{}}}});}})();
</script>
</body>
</html>
"""
    target = Path(__file__).parent / "priprava-produkce-2026-10-08-role-a-cinnosti-light.html"
    target.write_text(doc, encoding="utf-8")
    print(target.name, len(doc))


if __name__ == "__main__":
    build()
