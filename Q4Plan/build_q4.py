#!/usr/bin/env python3
"""Build the Q4 output from one data source.

Usage: python3 build_q4.py
Writes Q4_OKR_2026.md (OKR list for the hub) and q4-vystup.html (výstup z porady: akční kroky,
OKR, rozpad prezentace, body k ověření). The deck itself is hand-written in q4-kickoff-prezentace.html.
Items with proposed=True were not said at the meeting and need confirming at Delegace 4 (1. 10.).
"""
import html
from pathlib import Path

HERE = Path(__file__).parent
PEOPLE = ["David", "Martin", "Jirka", "Kuba"]

# (text, owner, start, deadline, dod, blockers, proposed)
OKRS = [
    {
        "id": "O1", "title": "Finance: H2 profit k druhému tieru", "owner": "Jirka", "proposed_owner": True,
        "why": "H2 cíl zůstává $200k / $500k / $1M. $1M je strop, reálně míříme k $500k. Dnes $107k, ve vzduchu $300k až $350k.",
        "krs": [
            ("Kumulativní profit H2 ≥ $200k (bronz), stretch $500k (stříbro)", "Jirka", "1. 10.", "31. 12.",
             "Číslo v hubu (Cashflow API) včetně plateb z RON_India k 31. 12.", "Výsledky SD, RC a podpis RON_India", True),
            ("Rozhodnout daily profit tiery: stávající $1k / $2,5k / $5k, nebo $2,5k / $5k / $7,5k", "Martin", "1. 10.", "1. 10.",
             "Tiery zapsané v hubu (Cíle)", "Žádné", True),
            ("ROI firmy ≥ 50 % do konce roku", "Martin", "1. 10.", "31. 12.",
             "ROI v hubu ≥ 50 % za H2, definice ROI zapsaná", "Definice ROI, platby z RON_India", False),
            ("Nové portfolio (RC, MF, Hexapolis, SD) tvoří 85 / 90 / 95 % revenue", "Jirka", "1. 10.", "31. 12.",
             "Podíl v hubu za Q4 ≥ 85 % (bronz)", "Q3 skončilo na 85 % bez RON_India (79 % s ní), sjednotit definici", False),
            ("Týdenní finanční review na EXEC běží každý týden", "Martin", "1. 10.", "od 2. týdne Q4",
             "Review proběhlo ≥ 10 z 13 týdnů Q4, podklad z hubu", "Dashboard z účtů a cash flow", True),
        ],
    },
    {
        "id": "O2", "title": "Sector Defense: vydat a dostat na čísla Red Command", "owner": "David", "proposed_owner": False,
        "why": "Hlavní produktový cíl Q4. Když čísla po 2 až 4 týdnech výrazně zaostanou za pásmem mezi MF a RC, projekt končí.",
        "krs": [
            ("Release na Android", "David, Kuba", "hned", "st 30. 9.",
             "Hra live na Google Play, tranše 1 UA spuštěná", "Poslední interní playtest, ladění 29. 9. (28. 9. svátek)", False),
            ("Gate 1 (7. den od spuštění UA): D1 ROAS ≥ 28 %, D1 retence ≥ 24 %, D3 retence ≥ 14 %", "Kuba", "start UA", "7. den UA",
             "Zápis u každé metriky: splněno / nesplněno, rozhodnutí o další tranši", "Kampaně běží bez technických chyb, spolehlivé měření revenue", False),
            ("Gate 2 (14. den): D7 ROAS dozrálých kohort ≥ 65 %, predikovaný D30 ROAS ≥ 90 %", "Kuba", "po Gate 1", "14. den UA",
             "Zápis u každé metriky: splněno / nesplněno, rozhodnutí o další tranši", "Gate 1, dozrálé D7 kohorty", False),
            ("Gate 3 (21. den): D7 ROAS ≥ 65 % ve dvou vyhodnocovacích oknech, predikovaný D30 ROAS ≥ 100 %, růst CPI při navyšování spendu max. o 20 %", "Kuba", "po Gate 2", "21. den UA",
             "Zápis u každé metriky: splněno / nesplněno, verdikt scale / hold / stop", "Gate 2, dvě vyhodnocovací okna", False),
            ("Stop pravidla škálování: nespolehlivé měření revenue = zastavit value kampaně; D1 ROAS pod 15 % = zastavit škálování a prověřit produktovou ekonomiku; D7 ROAS pod 45 % = neuvolňovat další rozpočtovou tranši", "Kuba", "start UA", "průběžně",
             "Každé pondělí report na poradě, porušení pravidla zapsané s přijatým krokem", "Data z měřicí platformy", False),
            ("Rozhodnutí pokračovat, nebo scrap", "David", "30. 9.", "28. 10.",
             "Zapsané rozhodnutí s CPI, retencí a ROAS proti pásmu MF až RC", "Výsledky Gate 1 až 3", True),
            ("Naškálovat na úroveň Red Command (cca $50k měsíčně)", "David, Kuba", "po rozhodnutí", "31. 12.",
             "Měsíční profit SD v hubu na úrovni RC", "Rozhodnutí pokračovat, rozpočet UA", False),
            ("iOS verze jen když Android na D21 drží D7 ROAS nad 65 %", "Kuba", "21. 10.", "listopad",
             "Rozhodnutí o iOS zapsané, případně iOS live", "Gate 3", True),
        ],
    },
    {
        "id": "O3", "title": "Live-ops a retence: víc z titulů, které už máme", "owner": "David", "proposed_owner": False,
        "why": "Klíčové téma kvartálu. Nový produkt nevyvíjíme, ze stávajících titulů chceme přes live-ops a tweaky vytáhnout maximum.",
        "krs": [
            ("Plán sprintů na zbytek Q4 (první 2 až 3 sprinty ladění RC a MF)", "David", "25. 9.", "2. 10.",
             "Sprinty naplánované v hubu, zapracované externí review RC a MF", "Výstup externího designéra a review MF", True),
            ("Red Command: review monetizace a hooku, 1 až 2 A/B iterace", "David", "1. 10.", "30. 11.",
             "Vyhodnocené A/B testy, rozhodnutí o rolloutu", "Externí designér, kapacita po launchi SD", True),
            ("Red Command iOS: letos na 1 500 (upřesnit metriku)", "David", "1. 10.", "31. 12.",
             "Metrika v hubu dosáhla 1 500", "Upřesnit, co 1 500 znamená", False),
            ("LiveOps: 25 % revenue živého titulu z LiveOps, začít na RC", "David", "1. 10.", "31. 12.",
             "Podíl LiveOps na revenue RC ≥ 25 % v prosinci", "Plán sprintů, obsah eventů a battle passu", True),
            ("Retence D1 +2 až 3 p. b. na RC a SD", "David", "1. 10.", "31. 12.",
             "D1 proti baseline z září, ověřeno 50% A/B testem nebo rolloutem", "Baseline SD existuje až po launchi", True),
            ("Legacy review: tituly pod cca $100 profitu denně", "Jirka", "1. 10.", "30. 11.",
             "Seznam legacy titulů s rozhodnutím: držet, nebo pustit", "Data z hubu (profit po titulech)", True),
        ],
    },
    {
        "id": "O4", "title": "B2B a RON_India: dotáhnout rozjetý deal", "owner": "David", "proposed_owner": False,
        "why": "B2B bez aktivního outreache. Dotahujeme RON_India, příležitosti bereme, když přijdou.",
        "krs": [
            ("Podpis další fáze RON_India ($60k)", "David", "hned", "15. 10.",
             "Podepsaná fáze a přijatá platba", "Rozhodnutí klienta (14 dní)", True),
            ("Kapacitní plán pro plnou hru ($800k), pokud klient kývne", "David", "po podpisu", "31. 10.",
             "Plán: externí kontrakty (překlady), AI assety, +1 grafik, designéři na review", "Podpis další fáze", True),
            ("LEGO a Heroes hra z TinySoftu: reaktivně, bez outreache", "David", "průběžně", "31. 12.",
             "Každá příchozí příležitost má zapsané rozhodnutí", "Iniciativa partnera", True),
        ],
    },
    {
        "id": "O5", "title": "Portfolio a R&D: rozhodnutí místo otevřených projektů", "owner": "Jirka", "proposed_owner": True,
        "why": "Žádný nový titul v Q4. Hexapolis 2 a Puppet Sports rozhodnout v prvním měsíci, R&D staví základ pro další hry.",
        "krs": [
            ("Hexapolis 2: design dokument a sekundární turn-based koncept, rozhodnutí", "Jirka", "1. 10.", "31. 10.",
             "Design dokument, testy tématik, zapsané rozhodnutí pokračovat / zmrazit / stop", "Kapacita designérů", True),
            ("Test multiplayeru Hexapolisu na původním Hexapolisu", "Jirka", "po rozhodnutí o Hex 2", "30. 11.",
             "Test proběhl, vyhodnocený", "Rozhodnutí o Hexapolis 2", True),
            ("Puppet Sports: vyhodnotit první vlny outreache, pokračovat, nebo stop", "David", "1. 10.", "31. 10.",
             "Partner na financování, nebo zapsaný stop", "Odezva partnerů", True),
            ("Shared Game Backend: první nasazení (Hexapolis nebo MF) a základ membership systému (Nox ID)", "David", "1. 10.", "31. 12.",
             "SGB live v jednom titulu, návrh membershipu", "Výběr titulu, programátorská kapacita", True),
            ("Reskin nástroj otestovat bez cíle něco vydat", "Martin", "1. 10.", "30. 11.",
             "Jeden testovací reskin, zapsaný learning", "Žádné", True),
        ],
    },
    {
        "id": "O6", "title": "Tým a řízení: lidi, delegace, data", "owner": "Martin", "proposed_owner": True,
        "why": "Dotáhnout delegaci včetně budgetů a odměňování, doplnit tým o testera a komunitu, mít čas přiřazený k práci.",
        "krs": [
            ("Nábor: tester + komunitní správce (půl QA, půl Discord)", "Kuba", "1. 10.", "30. 11.",
             "Člověk nastoupil nebo má podepsanou smlouvu", "Rozpočet segmentu (Delegace 4)", True),
            ("Discord (a další) komunity pro naše hry založené a spravované", "Kuba", "1. 10.", "31. 10.",
             "Komunita pro RC a SD běží, správce určený", "Nábor community správce", True),
            ("Milan: trvalý kontrakt, nebo postupné ukončení", "David", "1. 10.", "31. 10.",
             "Rozhodnutí zapsané, případně podepsaná smlouva", "Dohoda o platu", True),
            ("Zjistit stav a plány Katky (mateřská)", "Kuba", "1. 10.", "16. 10.",
             "Známe termín návratu a úvazek, nebo že se nevrací", "Odpověď Katky", True),
            ("Delegace dotažená: role, segmenty, činnosti, budgety, model odměňování (fix + bonus)", "Martin", "1. 10.", "31. 12.",
             "Role a činnosti schválené (Delegace 4), budgety segmentů a model odměňování rozhodnuté", "Delegace 4, rozpočtová porada", True),
            ("Time tracking: u většiny lidí přes 95 % času přiřazeno k práci", "Martin", "1. 10.", "31. 12.",
             "Měsíční kontrola v hubu: ≥ 95 % hodin s taskem u většiny lidí", "Pravidlo P8 z Delegace 4", True),
            ("Status OKR na každé druhé firemní poradě", "Martin", "1. 10.", "31. 12.",
             "Status proběhl na každé druhé poradě", "Žádné", False),
        ],
    },
]

ACTIONS = [
    ("Před Delegací 4", [
        ("Rozeslat výstup z porady a návrh OKR vedení k připomínkám", "David", "út 29. 9.", True),
        ("Release Sector Defense", "David, Kuba", "st 30. 9.", False),
        ("Projít návrh OKR: potvrdit vlastníky a termíny označené jako návrh", "všichni", "čt 1. 10.", True),
        ("Rozhodnout daily profit tiery a definici ROI firmy", "Martin", "čt 1. 10.", True),
        ("Vyjasnit body k ověření (iOS 1 500, fixní náklady 2 vs. 3 měsíce, H2 tiery, „tělo FOP“)", "David", "čt 1. 10.", True),
        ("Delegace 4: role a činnosti mezi segmenty, budgety", "všichni", "čt 1. 10.", False),
    ]),
    ("Příprava Q4 kickoffu", [
        ("Plán sprintů na zbytek Q4 (ladění RC a MF)", "David", "pá 2. 10.", True),
        ("Aktualizovat datové slidy k 30. 9.: celé Q3, RC za celé září, H2 profit", "Martin", "út 6. 10.", True),
        ("Portfolio slide: Hexapolis 2, Puppet Sports, legacy", "Jirka", "út 6. 10.", True),
        ("SD slide: první data z gate D7", "Kuba", "st 7. 10.", True),
        ("Zkontrolovat deck pro celou firmu: žádné údaje o mzdách jednotlivců ani osobní HR", "Martin", "st 7. 10.", True),
        ("Generálka 30 min se všemi řečníky", "David", "st 7. 10.", True),
        ("Q4 kickoff s celou firmou", "všichni", "čt 8. 10.", True),
    ]),
    ("Po kickoffu", [
        ("Zapsat Q4 OKR do hubu (Cíle): vlastník, DoD, start, termín", "Martin", "pá 9. 10.", True),
        ("Dekret do Wiki: portfolio, gaty SD, žádný nový titul, legacy pod $100 denně", "David", "pá 9. 10.", True),
        ("Inzerát tester + komunitní správce venku", "Kuba", "pá 9. 10.", True),
        ("Zjistit stav Katky", "Kuba", "pá 16. 10.", True),
        ("Rozhodnutí SD: pokračovat, nebo scrap", "David", "st 28. 10.", True),
        ("Aktualizovat tracker témat (Delegacni_Navrh)", "David", "pá 9. 10.", True),
    ]),
]

SLIDES = [
    # (#, part, title, presenter, minutes, message, source)
    (1, "", "Q3 → Q4 2026", "Jirka", 1, "Otevření: Q3 zavřený, Q4 je o škálování toho, co máme.", ""),
    (2, "", "Program a kdo mluví", "Jirka", 1, "Šest částí, čtyři řečníci, otázky na konci.", ""),
    (3, "A · Review Q3", "Kancelář a konference", "Jirka", 1, "Fotky z kanceláře a konferencí.", "fotky z akcí"),
    (4, "A · Review Q3", "Motokáry, minigolf a gril", "Jirka", 1, "Fotky z teambuildingů.", "fotky z akcí"),
    (5, "A · Review Q3", "Motokáry: video", "Jirka", 1, "Video z motokár, YouTube odkaz se doplní.", ""),
    (6, "A · Review Q3", "Q3 v událostech", "Jirka", 3, "Co se stalo po měsících, jen události, bez peněz z Red Command.", "Q4 plan kap. 4, OKR checklist"),
    (7, "B · Data", "Revenue Q3 a nové portfolio", "Martin", 3, "$486k revenue her, 85 % z nového portfolia (koláč). S RON_India $526k.", "data od Kuby za Q3"),
    (8, "B · Data", "Red Command se zaplatil 1,4×", "Martin", 3, "Náš 50% podíl $144k proti vývoji cca $100k, splaceno v září, září je rekord.", "RC revenue k 30. 9."),
    (9, "B · Data", "Kolik stál Sector Defense", "Martin", 2, "$93k stejným nápočtem jako RC ($100k). Rychleji, za stejné peníze.", "cost-roi-overview"),
    (10, "B · Data", "Kanceláře a hub v číslech", "Martin", 2, "Stěhování 690 tis. Kč, break-even v listopadu. Dotazník k hubu: úspora cca 2 h na člověka.", "rozvaha kanceláří, dotazník k hubu"),
    (11, "B · Data", "RON_India: ROI 2 700 %", "David", 2, "$40k za MVP s náklady cca $1,4k. Při podpisu plné hry $100k ještě letos.", "cost-roi-overview"),
    (12, "B · Data", "Kam šel čas", "David", 2, "Třetina hodin bez tasku. Bez toho nejde spočítat náklad projektu.", "time tracking v hubu"),
    (13, "C · Cíle Q3", "Skóre Q3: 35 z 52", "David", 3, "Činnosti z velké části splněné, finanční výsledky pod cílem.", "hub, Firemní cíle 24. 9."),
    (14, "C · Cíle Q3", "Co nevyšlo a proč", "David", 3, "Finanční KPI, reporting, LiveOps bez fokusu. Chyběl vlastník nebo termín.", "OKR checklist"),
    (15, "D · Rozhodnutí", "Sector Defense: launch a gaty", "Kuba", 4, "Release 30. 9., gaty 7. / 14. / 21. den od kampaní, cíl $50k měsíčně, kdy neškálujeme.", "gaty marketingu 2. 10."),
    (16, "D · Rozhodnutí", "Portfolio: kdo dostane kapacitu", "David", 3, "Nejdřív RC (nový content), SD škálovat, MF externí designéři, Hex 2 a Puppet do října, legacy podle profitu.", "záznam porady"),
    (17, "D · Rozhodnutí", "B2B, RON_India a R&D", "David", 3, "Bez outreache, dotáhnout Indii. SGB jako základ membershipu a social features.", "záznam porady"),
    (18, "D · Rozhodnutí", "Tým a organizace", "David", 3, "Hledáme testera + komunitního správce. Komunity, postmortem SD 8. 10., time tracking.", "záznam porady"),
    (19, "E · Cíle Q4", "H2 profit: kde jsme", "Jirka", 2, "$175k z $200k / $500k / $1M (EBITDA $315k minus $140k z H1). Ve vzduchu $300k až $350k.", "adjusted EBITDA k 30. 9."),
    (20, "E · Cíle Q4", "Q4 OKR", "Jirka", 4, "Šest cílů, každý s vlastníkem, DoD a termínem. Status každou druhou poradu.", "Q4_OKR_2026.md"),
    (21, "F · Priority", "Dvě priority Q4", "Jirka", 2, "SD launch a škálování, live-ops a retence. Co neděláme.", ""),
    (22, "", "Otázky", "všichni", 5, "Otevřená diskuse.", ""),
]

VERIFY = [
    "Fixní náklady SD $57,609 odpovídají 3 měsícům (celé Q3), v nahrávce zaznělo „dva měsíce“. Pro 2 měsíce vychází $38,406.",
    "H2 tiery: v nahrávce „100, 200, 500“, v hubu $200k / $500k / $1M.",
    "Součet k $500k: $107k + $300k až $350k dává cca $407k až $457k, tedy blízko, ale pod druhým tierem.",
    "Daily profit tiery: necháváme, nebo $2,5k / $5k / $7,5k? (KR v O1)",
    "Red Command iOS „letos na 1 500, share 150 na stranu“: v jaké metrice?",
    "„Dotáhnout hlavní tělo FOP“: co přesně?",
    "Smlouva na Red Command: přepis nesrozumitelný, zapsáno „stávající ujednání stačí“.",
    "Milan: „do měsíce“, nebo konkrétní měsíc?",
    "LEGO / Heroes hra z TinySoftu: jména z přepisu.",
    "Q4 kickoff 8. 10. a všechny termíny označené jako návrh.",
]


def esc(s):
    return html.escape(s, quote=False)


def owner_keys(owner):
    o = owner.lower()
    keys = [p.lower() for p in PEOPLE if p.lower() in o]
    if "všichni" in o:
        keys = [p.lower() for p in PEOPLE]
    return " ".join(keys) or "other"


def chips(owner):
    parts = [p.strip() for p in owner.split(",")]
    return "".join(f'<span class="who who-{html.escape(p.lower())}">{esc(p)}</span>' for p in parts)


def tag(proposed):
    return '<span class="tag">návrh</span>' if proposed else ""


def build_md():
    out = ["# Q4 2026 · OKR", "",
           "> Návrh z EXEC porady 24. 9. 2026. Hlavních cílů je málo, podkroků kolik je potřeba. Každý podkrok má co, "
           "DoD (definition of done), kdo, od kdy, termín a blokery. Položky označené *(návrh)* na poradě nezazněly "
           "a potvrzují se na Delegaci 4 (čt 1. 10.). Status OKR na každé druhé firemní poradě.", ""]
    for o in OKRS:
        out += [f"## {o['id']} · {o['title']}", "",
                f"**Odpovídá:** {o['owner']}{' *(návrh)*' if o['proposed_owner'] else ''}  ", o["why"], "",
                "| # | Co | DoD | Kdo | Od | Termín | Blokery / závislosti |", "|---|---|---|---|---|---|---|"]
        for i, (t, who, start, end, dod, blk, prop) in enumerate(o["krs"], 1):
            out.append(f"| {o['id']}.{i} | {t}{' *(návrh)*' if prop else ''} | {dod} | {who} | {start} | {end} | {blk} |")
        out.append("")
    out += ["## Co v Q4 vědomě neděláme", "",
            "- Žádný nový titul, rozhodně ne velký. Reskin nástroj se jen testuje.",
            "- Žádný B2B outreach. Příležitosti bereme, když přijdou.",
            "- Žádný cíl na udržení Mecha Fortress (údržba).",
            "- Nehledáme samostatného game analytika (do konce roku).", ""]
    (HERE / "Q4_OKR_2026.md").write_text("\n".join(out))


CSS = """
:root {
  --navy: #001a33; --navy-2: #003366; --blue: #004d99; --accent: #007bff; --cyan: #00d2ff;
  --bg: #f3f8fd; --surface: #ffffff; --ink: #0b2239; --muted: #4c6680; --line: #d5e3f0; --soft: #e8f1fb;
  --ok: #1f9d68; --warn: #c7702a; --focus: #007bff;
  --c-david: #007bff; --c-martin: #0e9f8f; --c-jirka: #7a5af5; --c-kuba: #d9642b; --c-other: #5b7188;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #001426; --surface: #03213d; --ink: #e6f1fc; --muted: #9db6cf; --line: #173a5c; --soft: #062a4b;
    --accent: #3d9bff; --c-david: #4aa3ff; --c-martin: #2fc4b2; --c-jirka: #a08bff; --c-kuba: #ff9157; color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #001426; --surface: #03213d; --ink: #e6f1fc; --muted: #9db6cf; --line: #173a5c; --soft: #062a4b;
  --accent: #3d9bff; --c-david: #4aa3ff; --c-martin: #2fc4b2; --c-jirka: #a08bff; --c-kuba: #ff9157; color-scheme: dark;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 16px/1.55 Inter, system-ui, sans-serif; -webkit-font-smoothing: antialiased; }
::selection { background: var(--cyan); color: var(--navy); }
a { color: var(--accent); text-underline-offset: 3px; }
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; border-radius: 4px; }
.wrap { max-width: 1160px; margin: 0 auto; padding: 0 16px; }
header.band { background: radial-gradient(120% 140% at 85% -20%, #0a4d8f 0%, var(--navy-2) 38%, var(--navy) 75%); color: #fff; padding: 28px 0 40px; }
.band .top { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.band .top img { height: 44px; width: auto; }
.band .top span { font-size: 0.85rem; color: #a9cbee; }
.band h1 { font: 900 clamp(2.1rem, 5.4vw, 3.6rem)/1.02 Montserrat, sans-serif; letter-spacing: -0.02em; margin: 34px 0 12px; max-width: 18ch; text-wrap: balance; }
.band p.lead { color: #cfe3f7; max-width: 62ch; margin: 0; font-size: 1.06rem; }
.band .links { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }
.band .links a { color: #fff; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.18); padding: 9px 14px; border-radius: 999px; text-decoration: none; font-size: 0.92rem; min-height: 44px; display: inline-flex; align-items: center; }
.band .links a.primary { background: var(--cyan); color: var(--navy); border-color: var(--cyan); font-weight: 600; }
.band .links a:hover { background: rgba(255,255,255,0.16); }
.band .links a.primary:hover { background: #5ee3ff; }
nav.toc { position: sticky; top: 0; z-index: 5; background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }
nav.toc .wrap { display: flex; gap: 4px; overflow-x: auto; scrollbar-width: none; }
nav.toc a { white-space: nowrap; padding: 12px 12px; color: var(--muted); text-decoration: none; font-size: 0.92rem; font-weight: 500; }
nav.toc a:hover { color: var(--ink); }
section { padding: 48px 0 8px; scroll-margin-top: 48px; }
h2 { font: 800 clamp(1.5rem, 3vw, 2.1rem)/1.15 Montserrat, sans-serif; letter-spacing: -0.01em; margin: 0 0 8px; }
h3 { font: 700 1.12rem/1.3 Montserrat, sans-serif; margin: 0; }
.intro { color: var(--muted); max-width: 70ch; margin: 0 0 22px; }
.decisions { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2px; background: var(--line); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
.decisions div { background: var(--surface); padding: 18px 20px; }
.decisions b { display: block; font-family: Montserrat, sans-serif; font-weight: 700; margin-bottom: 4px; }
.decisions p { margin: 0; color: var(--muted); font-size: 0.95rem; }
.filter { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: 0 0 18px; }
.filter span { color: var(--muted); font-size: 0.9rem; margin-right: 4px; }
.filter button { font: inherit; font-size: 0.92rem; border: 1px solid var(--line); background: var(--surface); color: var(--ink); padding: 8px 14px; border-radius: 999px; cursor: pointer; min-height: 44px; }
.filter button[aria-pressed="true"] { background: var(--ink); color: var(--bg); border-color: var(--ink); }
.who { display: inline-block; font-size: 0.78rem; font-weight: 600; padding: 2px 9px; border-radius: 999px; margin: 1px 4px 1px 0; color: #fff; background: var(--c-other); white-space: nowrap; }
.who-david { background: var(--c-david); } .who-martin { background: var(--c-martin); } .who-jirka { background: var(--c-jirka); } .who-kuba { background: var(--c-kuba); }
.who-všichni { background: var(--navy-2); }
.tag { display: inline-block; font-size: 0.72rem; font-weight: 600; color: var(--warn); border: 1px solid currentColor; border-radius: 4px; padding: 0 5px; margin-left: 6px; vertical-align: 1px; letter-spacing: 0.02em; }
.phase { margin: 0 0 26px; }
.phase h3 { margin-bottom: 10px; }
ul.actions { list-style: none; margin: 0; padding: 0; background: var(--surface); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; }
ul.actions li { display: grid; grid-template-columns: 28px 1fr auto; gap: 12px; align-items: start; padding: 12px 16px; border-top: 1px solid var(--line); }
ul.actions li:first-child { border-top: 0; }
ul.actions input { width: 20px; height: 20px; margin: 3px 0 0; accent-color: var(--accent); cursor: pointer; }
ul.actions label { cursor: pointer; }
ul.actions li.done label { color: var(--muted); text-decoration: line-through; text-decoration-color: var(--muted); }
ul.actions .meta { text-align: right; font-size: 0.88rem; color: var(--muted); font-variant-numeric: tabular-nums; }
.okr { background: var(--surface); border: 1px solid var(--line); border-radius: 16px; margin: 0 0 18px; overflow: hidden; }
.okr > header { display: grid; grid-template-columns: auto 1fr auto; gap: 14px; align-items: start; padding: 18px 20px; background: linear-gradient(180deg, var(--soft), transparent); }
.okr .oid { font: 900 1.5rem/1 Montserrat, sans-serif; color: var(--accent); }
.okr .why { color: var(--muted); margin: 4px 0 0; font-size: 0.95rem; max-width: 72ch; }
.okr .own { text-align: right; font-size: 0.8rem; color: var(--muted); }
.okr table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.okr th { text-align: left; font-weight: 600; color: var(--muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; padding: 8px 10px; border-top: 1px solid var(--line); background: var(--surface); }
.okr td { padding: 10px; border-top: 1px solid var(--line); vertical-align: top; }
.okr td.n { color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; }
.okr td.d { white-space: nowrap; font-variant-numeric: tabular-nums; }
.okr td.b { color: var(--muted); }
.okr td.t b { font-weight: 600; }
.tscroll { overflow-x: auto; }
.nots { display: flex; flex-wrap: wrap; gap: 8px; margin: 6px 0 0; padding: 0; list-style: none; }
.nots li { background: var(--surface); border: 1px dashed var(--line); padding: 8px 12px; border-radius: 10px; font-size: 0.92rem; color: var(--muted); }
.run { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; margin: 0 0 22px; }
.run div { background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 14px 16px; }
.run strong { font: 800 1.4rem Montserrat, sans-serif; font-variant-numeric: tabular-nums; }
.run p { margin: 2px 0 0; color: var(--muted); font-size: 0.9rem; }
table.slides { width: 100%; border-collapse: collapse; background: var(--surface); border: 1px solid var(--line); border-radius: 14px; overflow: hidden; font-size: 0.92rem; }
table.slides th { text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--muted); padding: 10px 12px; border-bottom: 1px solid var(--line); }
table.slides td { padding: 10px 12px; border-top: 1px solid var(--line); vertical-align: top; }
table.slides tr.part td { background: var(--soft); font-weight: 700; font-family: Montserrat, sans-serif; font-size: 0.86rem; }
table.slides td.n, table.slides td.m { color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; }
ol.verify { padding-left: 1.3em; max-width: 80ch; }
ol.verify li { margin: 6px 0; }
footer { margin: 56px 0 0; padding: 22px 0 40px; border-top: 1px solid var(--line); color: var(--muted); font-size: 0.86rem; }
.hidden { display: none !important; }
@media (max-width: 720px) {
  ul.actions li { grid-template-columns: 28px 1fr; }
  ul.actions .meta { grid-column: 2; text-align: left; }
  .okr > header { grid-template-columns: auto 1fr; }
  .okr .own { grid-column: 2; text-align: left; }
  .okr table, .okr thead, .okr tbody, .okr tr, .okr td { display: block; }
  .okr thead { display: none; }
  .okr tr { border-top: 1px solid var(--line); padding: 10px 14px; }
  .okr td { border: 0; padding: 2px 0; }
  .okr td[data-l]::before { content: attr(data-l) ": "; color: var(--muted); font-size: 0.82rem; }
  .okr td.d { white-space: normal; }
  table.slides td.src, table.slides th.src { display: none; }
}
@media print {
  nav.toc, .filter, .band .links { display: none; }
  body { background: #fff; font-size: 10pt; }
  header.band { padding: 14px 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  section { padding-top: 18px; }
  .okr, ul.actions li, table.slides tr { break-inside: avoid; }
  .who { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
"""

JS = """
(function () {
  var KEY = 'q4-vystup-done';
  var done = {};
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) {}
  document.querySelectorAll('ul.actions input').forEach(function (cb) {
    var li = cb.closest('li');
    if (done[cb.id]) { cb.checked = true; li.classList.add('done'); }
    cb.addEventListener('change', function () {
      li.classList.toggle('done', cb.checked);
      done[cb.id] = cb.checked;
      try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {}
    });
  });
  var buttons = document.querySelectorAll('.filter button');
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var who = b.dataset.who;
      buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      document.querySelectorAll('[data-owner]').forEach(function (el) {
        el.classList.toggle('hidden', who !== 'all' && el.dataset.owner.split(' ').indexOf(who) < 0);
      });
      document.querySelectorAll('.okr, .phase').forEach(function (box) {
        var rows = box.querySelectorAll('[data-owner]');
        var visible = Array.prototype.some.call(rows, function (r) { return !r.classList.contains('hidden'); });
        box.classList.toggle('hidden', rows.length > 0 && !visible);
      });
    });
  });
})();
"""


def filter_bar():
    btns = '<button type="button" data-who="all" aria-pressed="true">Všichni</button>' + "".join(
        f'<button type="button" data-who="{p.lower()}" aria-pressed="false">{p}</button>' for p in PEOPLE)
    return f'<div class="filter" role="group" aria-label="Filtr podle člověka"><span>Zobrazit úkoly pro</span>{btns}</div>'


def build_html():
    decisions = [
        ("Sector Defense jde ven 30. 9.", "Po 2 až 4 týdnech dat pokračujeme, nebo projekt končí. Cíl Q4: čísla Red Command."),
        ("Q4 je kvartál live-ops a retence", "Žádný nový titul. První 2 až 3 sprinty ladí RC a MF."),
        ("H2 profit: míříme k $500k", "Dnes $107k, ve vzduchu $300k až $350k. $1M je strop. Platby z Indie se počítají."),
        ("RON_India je priorita B2B", "MVP za $40k s ROI cca 2 700 %. Podpis další fáze, jinak B2B bez outreache."),
        ("Hexapolis 2 a Puppet Sports do října", "Hex 2 jako sekundární turn-based koncept. Puppet podle odezvy partnerů."),
        ("Legacy pod cca $100 denně končí", "Review nákladů na QA a údržbu legacy titulů."),
        ("Nábor: tester + komunitní správce", "Urgentně na začátku Q4. Obnovíme komunity her."),
        ("Delegace a time tracking jako OKR", "Role, budgety a odměňování do konce roku. Přes 95 % času přiřazeno k práci."),
    ]
    dec = "".join(f"<div><b>{esc(t)}</b><p>{esc(d)}</p></div>" for t, d in decisions)

    phases = ""
    n = 0
    for name, items in ACTIONS:
        lis = ""
        for text, who, when, prop in items:
            n += 1
            lis += (f'<li data-owner="{owner_keys(who)}"><input type="checkbox" id="a{n}">'
                    f'<label for="a{n}">{esc(text)}</label>'
                    f'<div class="meta">{chips(who)}<br>{esc(when)}{tag(prop)}</div></li>')
        phases += f'<div class="phase"><h3>{esc(name)}</h3><ul class="actions">{lis}</ul></div>'

    okrs = ""
    for o in OKRS:
        rows = ""
        for i, (t, who, start, end, dod, blk, prop) in enumerate(o["krs"], 1):
            rows += (f'<tr data-owner="{owner_keys(who)}"><td class="n">{o["id"]}.{i}</td>'
                     f'<td class="t" data-l="Co"><b>{esc(t)}</b>{tag(prop)}</td>'
                     f'<td data-l="DoD">{esc(dod)}</td><td data-l="Kdo">{chips(who)}</td>'
                     f'<td class="d" data-l="Od">{esc(start)}</td><td class="d" data-l="Termín">{esc(end)}</td>'
                     f'<td class="b" data-l="Blokery">{esc(blk)}</td></tr>')
        okrs += (f'<article class="okr"><header><span class="oid">{o["id"]}</span>'
                 f'<div><h3>{esc(o["title"])}</h3><p class="why">{esc(o["why"])}</p></div>'
                 f'<div class="own">odpovídá<br>{chips(o["owner"])}{tag(o["proposed_owner"])}</div></header>'
                 f'<div class="tscroll"><table><thead><tr><th>#</th><th>Co</th><th>DoD</th><th>Kdo</th><th>Od</th><th>Termín</th>'
                 f'<th>Blokery a závislosti</th></tr></thead><tbody>{rows}</tbody></table></div></article>')

    total = sum(s[4] for s in SLIDES)
    per = {}
    for s in SLIDES:
        for p in [x.strip() for x in s[3].split(",")]:
            per[p] = per.get(p, 0) + s[4] / len(s[3].split(","))
    run = f'<div><strong>{total} min</strong><p>{len(SLIDES)} slidů, z toho 5 min otázky</p></div>' + "".join(
        f'<div><strong>{round(per.get(p, 0))} min</strong><p>{chips(p)} {", ".join(str(s[0]) for s in SLIDES if p in s[3])}</p></div>'
        for p in PEOPLE)
    srows, last = "", None
    for num, part, title, who, mins, msg, src in SLIDES:
        if part and part != last:
            srows += f'<tr class="part"><td colspan="6">{esc(part)}</td></tr>'
        last = part or last
        srows += (f'<tr data-owner="{owner_keys(who)}"><td class="n">{num}</td><td><b>{esc(title)}</b></td>'
                  f'<td>{chips(who)}</td><td class="m">{mins} min</td><td>{esc(msg)}</td><td class="src">{esc(src)}</td></tr>')

    ver = "".join(f"<li>{esc(v)}</li>" for v in VERIFY)

    doc = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Q4 2026: výstup z porady</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="band"><div class="wrap">
  <div class="top"><img src="assets/noxgames-logo.png" alt="NOXGAMES"><span>EXEC porada 24. 9. 2026 · interní, vedení</span></div>
  <h1>Q4 2026: co jsme rozhodli a kdo co udělá</h1>
  <p class="lead">Výstup z porady vedení: hlavní rozhodnutí, akční kroky s vlastníky, rozepsané Q4 OKR a rozpad Q4 kickoff prezentace pro celou firmu. Položky se štítkem „návrh“ na poradě nezazněly a potvrzují se na Delegaci 4 (čt 1. 10.).</p>
  <div class="links"><a class="primary" href="q4-kickoff-prezentace.html">Otevřít prezentaci</a><a href="zaznam-2026-09-24-exec-porada.html">Záznam porady a přepisy</a><a href="Q4_OKR_2026.md">OKR jako Markdown</a></div>
</div></header>
<nav class="toc" aria-label="Obsah"><div class="wrap">
  <a href="#rozhodnuti">Rozhodnutí</a><a href="#kroky">Akční kroky</a><a href="#okr">Q4 OKR</a><a href="#prezentace">Rozpad prezentace</a><a href="#overit">K ověření</a>
</div></nav>
<main class="wrap">
<section id="rozhodnuti"><h2>Hlavní rozhodnutí</h2><p class="intro">Osm věcí, na kterých jsme se 24. 9. shodli. Podrobnosti a čísla jsou v záznamu porady.</p>
<div class="decisions">{dec}</div></section>
<section id="kroky"><h2>Akční kroky</h2><p class="intro">Seřazené podle toho, kdy musí být hotové. Odškrtnutí se pamatuje jen v tomto prohlížeči.</p>
{filter_bar()}{phases}</section>
<section id="okr"><h2>Q4 OKR</h2><p class="intro">Šest hlavních cílů, pod každým podkroky s DoD (kdy je hotovo), vlastníkem, startem, termínem a blokery. Vlastník odpovídá za výsledek, nemusí vše dělat sám. Status na každé druhé firemní poradě, nesplněné Q3 cíle jsou převedené do podkroků.</p>
{filter_bar()}{okrs}
<h3 style="margin-top:26px">Co v Q4 vědomě neděláme</h3>
<ul class="nots"><li>Žádný nový titul (reskin nástroj jen test)</li><li>Žádný B2B outreach</li><li>Žádný cíl na udržení Mecha Fortress</li><li>Samostatného game analytika do konce roku nehledáme</li></ul></section>
<section id="prezentace"><h2>Rozpad prezentace</h2><p class="intro">Q4 kickoff pro celou firmu, návrh na čt 8. 10. (první data z gate D7 už budou). Struktura: review událostí Q3, data, splněné cíle, kontext rozhodnutí, nové cíle, priority. Deck je pro celou firmu, takže neobsahuje mzdy jednotlivců ani osobní HR věci (Milan, Katka).</p>
<div class="run">{run}</div>
<div class="tscroll"><table class="slides"><thead><tr><th>#</th><th>Slide</th><th>Mluví</th><th>Čas</th><th>Hlavní sdělení</th><th class="src">Zdroj dat</th></tr></thead><tbody>{srows}</tbody></table></div></section>
<section id="overit"><h2>K ověření před kickoffem</h2><ol class="verify">{ver}</ol></section>
</main>
<footer class="wrap">Interní podklad pro vedení NOXGAMES · generováno z build_q4.py · navazuje na záznam porady 24. 9. 2026</footer>
<script>{JS}</script>
</body>
</html>
"""
    (HERE / "q4-vystup.html").write_text(doc)


if __name__ == "__main__":
    build_md()
    build_html()
    print("built")
