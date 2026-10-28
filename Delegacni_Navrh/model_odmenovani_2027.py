#!/usr/bin/env python3
"""Model fixu + variabilní složky 2027 (podklad k poradě 29. 10. 2026).

Vstupy (PEOPLE):
- dnes = Ø skutečně vyplacená odměna za práci 1–10/2026 z NoxHubu (hodiny × sazba),
  bez coworkingu (ten je průtokový náklad na kancelář, ne odměna) a bez přepočtu na úvazek,
- roky = dokončené roky ve firmě k 1. 1. 2027 z hubu (profile_stats.joined_at, tenure achievementy),
- role a podíly ze stránek segmentů ve Wiki + upřesnění Davida z 28. 10.

    python3 -I model_odmenovani_2027.py

Zapíše ODMENOVANI_2027_MODEL_JMENOVITE.md (důvěrné) a vypíše souhrny pro společný podklad.
Foundeři a CEO (Mirek, Peko, Jirka) v modelu nejsou, schvaluje je jejich rada tří.
"""
import re
from pathlib import Path
from typing import Any

# ---------- Kotva a parametry (tis. Kč měsíčně) ----------
CAP = 150              # strop základu (fixu) pro tým a exekutivu (dekret); variabilní složka a podíly se nepočítají, foundeři mimo
EXEC_BASE = 110        # společný základ vlastníka segmentu
FLOOR = 52             # žádný plný základ role pod průměrnou mzdou v ČR (ČSÚ, Q2 2026)
BASE = {
    "Programátor": 80,
    "UA manager": 62,
    "Game designer": 60,
    "DevOps a IT": 60,
    "Publishing a LiveOps": 58,
    "Grafik MKT": 56,
    "Video a motion": 52,
    "Grafik DEV": 52,
    "QA": 52,
}
UROVEN = {"junior": 0.80, "medior": 0.90, "senior": 1.00}
TENURE_STEP, TENURE_CAP = 0.02, 0.20
ADD_CAP = 0.40         # aktivní příplatky nejvýš 40 % základu
PASSIVE = {            # pasivní složka za historii = achievementy v hubu, trvale
    "lead": (2.0, 2),        # ukončené vedení projektu nebo týmu (aspoň 6 měsíců): +2, nejvýš 2×
    "speaker": (1.0, 3),     # přednáška nebo reprezentace firmy venku: +1, nejvýš 3×
    "event": (1.0, 3),       # uspořádaný event: +1, nejvýš 3×
    "mentor": (0.5, 4),      # dokončený mentoring člověka: +0,5, nejvýš 4×
}
PASSIVE_CAP = 8
PASMA = {  # bonus a malus jako podíl z fixu; plan = čerpání bonusu na plánu
    "J": dict(bonus=0.10, malus=0.05, plan=0.5),
    "L": dict(bonus=0.15, malus=0.075, plan=0.5),
    "D": dict(bonus=0.0, malus=0.0, plan=0.0),   # exekutiva: jen fix + podíl na zisku pod čarou
}
PASMO_NAME = {"J": "Jistota", "L": "Lead", "D": "Fix + podíl"}
STEP1_CAP = 10
STEP2_DATE = "1. 7. 2027"
EUR = 24.2             # kurz pro dohody v eurech
# Individuální dohody nad hodnotou role: nick -> (fix v tis. Kč, popis). Platí od 1. 1. celé, bez dvou kroků.
DOHODA = {"Milan": (85.0, "dohoda 85 tis., cca 3 510 EUR; Milan chtěl 3 700 až 4 000 EUR, zápis 21. 9.")}

# ---------- Lidé ----------
# Tým: nick, segment, dnes, roky, úroveň, role {název: podíl}, příplatky [(název, tis.)], pasivní {kód: počet}, pásmo
TEAM = [
    ("Čoud", "Produkce", 82.5, 7, "senior", {"Programátor": 1}, [("zástup B2B delivery a autority tech", 5)], {"lead": 1}, "J"),
    ("Milan", "Produkce", 71.4, 0, "senior", {"Programátor": 1}, [], {}, "J"),
    ("Aldy", "Produkce", 73.4, 2, "senior", {"Game designer": .8, "Grafik DEV": .2},
     [("project lead (Sektor)", 12), ("druhý aktivní projekt (Mecha)", 6), ("zástup vlastníka za plán a kapacity", 5), ("mentor 2 lidí", 4)], {}, "L"),
    ("Karlík", "Produkce", 49.1, 7, "senior", {"Game designer": .8, "Grafik DEV": .2},
     [("project lead (Red Command)", 12)], {}, "L"),
    ("Akimo", "Produkce + Operations", 62.9, 4, "senior", {"Publishing a LiveOps": 1},
     [("Publishing a LiveOps lead", 10), ("správa kanceláří (Operations)", 5)], {}, "L"),
    ("Hutis", "Produkce + Operations", 45.3, 3, "senior", {"QA": .53, "Programátor": .27, "DevOps a IT": .20},
     [("QA lead", 8), ("zástup za NoxHub", 5)], {}, "L"),
    ("David Č.", "Produkce", 36.8, 0, "junior", {"Grafik DEV": 1}, [], {}, "J"),
    ("Richi", "Marketing", 79.4, 4, "senior", {"UA manager": 1}, [], {}, "J"),  # 59,4 hodiny + 20 tis. měsíčně dofakturace
    ("Ondra", "Marketing", 58.8, 4, "senior", {"Grafik MKT": 1}, [("správa celého ASO", 4)], {}, "J"),
    ("Ruda", "Marketing", 42.8, 2, "senior", {"Video a motion": 1}, [], {}, "J"),
]
# Exekutiva: nick, segment, dnes, roky, lidé pod sebou, podíl segmentu na OPEX %, role navíc [(název, tis.)], pasivní {kód: počet}
EXEC = [
    ("David", "Produkce", 105.5, 6, 7, 45, [("consigliere: agenda exekutivy, plány a strategie", 5)], {"lead": 2, "speaker": 3}),
    ("DJ", "Operations", 77.7, 9, 1, 24, [("finance, rozpočet a smlouvy celé firmy", 5)], {"lead": 1}),
    ("Kuba", "Marketing", 81.4, 5, 3, 20, [("analytika pro Produkci (přechodně)", 2)], {}),
]
# Foundeři a CEO: návrh = dnešek, schvaluje rada tří, na další rok si mohou navýšit
# nick, role, dnes, roky, zdroj dnešní částky
FOUNDERS = [
    ("Mirek", "founder, autorita tech + programátor", 110.6, 13, "Ø hodiny × sazba 758 Kč, 1–9/2026 (cca 146 h)"),
    ("Peko", "founder, autorita art + grafik", 245.0, 21, "Ø fakturace 1–8/2026 bez hodin, míchá práci s dalšími plněními"),
    ("Jirka", "CEO, majitel", 99.6, 21, "mzda 16,1 + měsíční platby 83,5 (TM, royalties), 1–9/2026; k tomu podíl na zisku"),
]
LABEL = {  # anonymní popis pozice pro společný podklad
    "Čoud": "Senior programátor, 7 let, zástup, historie leadu",
    "Milan": "Senior programátor, nový, individuální dohoda",
    "Aldy": "Game designer, lead 2 projektů, zástup vlastníka, mentor",
    "Karlík": "Game designer, lead 1 projektu, 7 let",
    "Akimo": "Publishing a LiveOps lead, správa kanceláří",
    "Hutis": "QA lead, programátor a DevOps, zástup NoxHub",
    "David Č.": "Junior grafik",
    "Richi": "UA manager, 4 roky",
    "Ondra": "Grafik MKT a správa ASO, 4 roky",
    "Ruda": "Video a motion, 2 roky",
    "David": "Vlastník segmentu Produkce + agenda exekutivy",
    "DJ": "Vlastník segmentu Operations + finance firmy",
    "Kuba": "Vlastník segmentu Marketing",
}
EXEC_PEOPLE = (1.0, 6)   # +1 za člověka pod sebou, nejvýš 6
EXEC_BUDGET = 0.10       # +0,1 za každé procento OPEX segmentu

TAIL = """
## 8. Foundeři, CEO a podíly na zisku

- **Mirek, Peko, Jirka (CEO):** mimo systém rolí i mimo strop základu. V rozpisu je návrh podle toho, co dnes mají. Schvaluje rada tří (Majitelé), na další rok si mohou dát víc.
- **Jirka:** dnešek 99,6 tis. měsíčně = mzda 16,1 + měsíční platby 83,5 (v bance „TM“, „Ochranné známky“, royalties; 9 plateb za 1–9/2026). Podíl na zisku navíc, mimo tento přehled.
- **Podíl na zisku** má exekutiva (David, Kuba, DJ, Jirka) a foundeři Peko a Mirek. Exekutiva se vzdává bonusů podle KPI: má fix, podíl na zisku, který se počítá až ze zisku pod čarou po poolu pro tým, a jako všichni podíl z dealů (5 % navrhovatel + 5 % majitel dealu nebo executor, ze zisku dealu). Bonusy týmu tak nic nesnižuje a nehrozí double dipping (R-22-06).

## 9. Co ještě doplnit

- **Pasivní složka:** David +7 (vedl projekty, přednášky), Čoud a DJ +2 (vedli projekt). Kuba nic. V hubu doplnit odznaky `speaker` a nové „vedl projekt“, ať to sedí se systémem.
- **Milan:** hodnota role 80 (3 300 EUR po zkušebce), dohoda 85 tis. (cca 3 510 EUR) od 1. 1., na plánu 89,3 (cca 3 690 EUR), s plným bonusem 93,5 (cca 3 860 EUR). Zápis z 21. 9.: požadavek „4 000 EUR, resp. 90 tis. Kč“. Pod Čoudem zůstává ve fixu i s plným bonusem. Dohoda 85 je zároveň revize z 10. 9. (zmrazit a revidovat za 3 měsíce).
- **Richi:** dnešek 79,4 = hodiny 59,4 + pravidelná dofakturace 20 tis. měsíčně (v záznamech „J“, „Dofakturace“). Fix drží garance nad hodnotou role 67, při roční evaluaci se dorovnává.
- **Lidé pod DJ v Operations:** potvrzeno 1. Až Operations poroste (např. happy office), příplatek se posune při roční evaluaci.
- **Odstup v exekutivě:** s pasivní složkou je David o 12 tis. nad DJ. Bez ní 125,5 / 118,4 / 117.
- **Aldy** naráží na strop příplatků 40 % základu. Buď to tak nechat, nebo zástup vlastníka přesunout do pasivní složky.
"""


def r(x):
    return round(x + 1e-9, 1)


def passive_sum(p):
    return min(sum(PASSIVE[k][0] * min(n, PASSIVE[k][1]) for k, n in p.items()), PASSIVE_CAP)


def calc_team(p, override=None) -> dict[str, Any]:
    nick, seg, today, years, lvl, roles, adds, pas, pasmo = p
    roles: dict[str, float]
    adds: list[tuple[str, float]]
    if override:
        pasmo = override.get(pasmo, pasmo)
    base = sum(BASE[k] * v for k, v in roles.items()) * UROVEN[lvl]
    tenure = min(years * TENURE_STEP, TENURE_CAP)
    base_t = base * (1 + tenure)
    add_raw = sum(a for _, a in adds)
    add = min(add_raw, ADD_CAP * base_t)
    pv = passive_sum(pas)
    H = base_t + add + pv
    fix = max(H, today)
    dohoda = DOHODA.get(nick)
    if dohoda:
        fix = max(fix, dohoda[0])
    c = finish(dict(nick=nick, seg=seg, today=today, years=years, lvl=lvl, roles=roles, adds=adds,
                    base_t=base_t, tenure=tenure, add=add, add_capped=add_raw > add, pv=pv, H=H,
                    fix=fix, garance=max(0, today - H), pasmo=pasmo, dohoda=dohoda, pas=pas))
    if dohoda:
        c["step1"] = c["fix"]
    return c


def calc_exec(e) -> dict[str, Any]:
    nick, seg, today, years, people, opex, extra, pas = e
    extra: list[tuple[str, float]]
    pp = min(people * EXEC_PEOPLE[0], EXEC_PEOPLE[1])
    bb = opex * EXEC_BUDGET
    ex = sum(a for _, a in extra)
    pv = passive_sum(pas)
    fix = min(EXEC_BASE + pp + bb + ex + pv, CAP)
    c = finish(dict(nick=nick, seg=seg, today=today, years=years, people=people, opex=opex, extra=extra,
                    pp=pp, bb=bb, ex=ex, pv=pv, pas=pas, H=fix, fix=fix, garance=0, pasmo="D"))
    c["step1"] = c["fix"]  # exekutiva: jednorázový skok od 1. 1., schválený hlasováním celého vedení
    return c


def finish(c: dict[str, Any]) -> dict[str, Any]:
    P = PASMA[c["pasmo"]]
    c["delta"] = c["fix"] - c["today"]
    c["step1"] = c["fix"] if c["delta"] <= STEP1_CAP else c["today"] + max(STEP1_CAP, c["delta"] / 2)
    c["bonus_max"] = c["fix"] * P["bonus"]
    c["malus_max"] = c["fix"] * P["malus"]
    c["plan"] = c["fix"] + c["bonus_max"] * P["plan"]
    c["low"], c["high"] = c["fix"] - c["malus_max"], c["fix"] + c["bonus_max"]
    return c


VARIANTS = [("A", "plné narovnání (preferovaná)", 1.0),
            ("B", "dvě třetiny narovnání", 2 / 3),
            ("C", "třetina narovnání", 1 / 3)]
EBITDA = (5.0, 10.0)   # Adj. EBITDA 2027 ve scénářích Martina B. z 22. 10., mil. Kč


def rows_for(s, override=None):
    """Fix = dnešek + s × (plný fix − dnešek). Individuální dohoda se nemění."""
    team = []
    for p in TEAM:
        c = calc_team(p, override)
        if not c["dohoda"]:
            c["fix"] = c["today"] + s * (c["fix"] - c["today"])
            finish(c)
        team.append(c)
    exe = []
    for e in EXEC:
        c = calc_exec(e)
        c["fix"] = c["today"] + s * (c["fix"] - c["today"])
        finish(c)
        c["step1"] = c["fix"]
        exe.append(c)
    return team, exe


def fmt(x):
    return f"{x:.2f}".replace(".", ",")


def variants_md(named):
    today = sum(c["today"] for c in rows_for(1)[0] + rows_for(1)[1]) * 12 / 1000
    out = ["| Varianta | Jen fixy | Plán | Max | Δ plánu | Δ fixů 2027 | Δ fixů 2028 | Δ fixů / EBITDA |",
           "|---|---|---|---|---|---|---|---|"]
    caps = []
    for code, name, s in VARIANTS:
        team, exe = rows_for(s)
        rows = team + exe
        lo, pl, hi = (year_cost(rows, m) for m in ("low", "plan", "high"))
        d27 = sum(6 * c["step1"] + 6 * c["fix"] - 12 * c["today"] for c in rows) / 1000
        d28 = sum(12 * (c["fix"] - c["today"]) for c in rows) / 1000
        lbl = f"**{code} · {name}**" if code == "A" else f"{code} · {name}"
        out.append(f"| {lbl} | {fmt(lo)} | {fmt(pl)} | {fmt(hi)} | +{fmt(pl - today)} | +{fmt(d27)} | +{fmt(d28)} | {round(100*d27/EBITDA[1])} až {round(100*d27/EBITDA[0])} % |")
        top = max(team, key=lambda c: c["high"])
        caps.append((code, top["high"], min(c["fix"] for c in exe)))
    out.append(f"| Dnes | {fmt(today)} | | | | | | |")
    out = table(out)
    out += ["", f"Mil. Kč za rok 2027, 13 lidí bez foundrů a CEO, bez poolu a podílů na zisku. Jen fixy = nikdo nedostane bonus, max = všichni plný bonus, Δ proti dnešku. Poslední sloupec = přírůstek fixů jako podíl Adj. EBITDA ze scénářů Martina B. ({int(EBITDA[0])} až {int(EBITDA[1])} mil. Kč).", ""]
    a, b, c3 = caps
    ok = [f"{k} ({str(round(h,1)).replace('.',',')} proti {str(round(l,1)).replace('.',',')})" for k, h, l in caps]
    out.append("- **Strop exekutivy** (nikdo v týmu ani s plným bonusem nad nejnižším fixem exekutivy): " + ", ".join(ok) + "." +
               (" Ve variantě C pravidlo neplatí, exekutiva by se musela narovnat víc než tým." if c3[1] > c3[2] else ""))
    out.append("- **Ve všech variantách platí, že si nikdo nepohorší.** Fix každého je aspoň dnešek, liší se jen, o kolik se narovná. Individuální dohoda (85 tis.) je ve všech stejná.")
    out.append("- **Individuální dohoda v B a C:** pevných 85 tis. by předběhlo lídry, kteří se narovnávají jen částečně (lead dvou projektů B 81,2, C 77,3). Když se skončí u B nebo C, navrhuji dohodu snížit stejným poměrem (B 80,5, C 75,9) a zbytek nabídnout přes bonus.")
    out.append("- **Dvě pásma, nebo jedno:** dát lídry do Jistoty ušetří ve variantě A cca " +
               fmt(year_cost(sum(rows_for(1), []), "plan") - year_cost(sum(rows_for(1, {"L": "J"}), []), "plan")) + " mil. ročně. Doporučení zůstává u dvou pásem.")
    out.append("")
    col = "Člověk" if named else "Pozice"
    who = lambda c: f"**{c['nick']}**" if named else LABEL[c["nick"]]
    out.append(f"**Fix 2027 po lidech podle varianty** (tis. Kč měsíčně, v závorce rozdíl proti dnešku)")
    out.append("")
    lines = [f"| {col} | Dnes | A · plné | B · dvě třetiny | C · třetina |", "|---|---|---|---|---|"]
    V = [rows_for(s) for _, _, s in VARIANTS]
    for i in range(len(TEAM) + len(EXEC)):
        cs = [(v[0] + v[1])[i] for v in V]
        cell = lambda c: f"{r(c['fix'])} ({c['fix'] - c['today']:+.1f})"
        lines.append(f"| {who(cs[0])} | {r(cs[0]['today'])} | **{cell(cs[0])}** | {cell(cs[1])} | {cell(cs[2])} |")
    out += table(lines)
    return out


def year_cost(rows, mode):
    """Roční náklad 2027 v mil. Kč. low = tým bez bonusu, exekutiva plný malus; plan; high."""
    tot = 0
    for c in rows:
        var = {"low": -c["malus_max"] if c["pasmo"] == "D" else 0,
               "plan": c["bonus_max"] * PASMA[c["pasmo"]]["plan"],
               "high": c["bonus_max"]}[mode]
        tot += 6 * c["step1"] + 6 * c["fix"] + 12 * var
    return tot / 1000


def table(lines):
    return [re.sub(r"(?<=\d)\.(?=\d)", ",", l) for l in lines]


def TWO_STEP(save):
    return [
        f"Kdo má nový fix o víc než {STEP1_CAP} tis. nad dneškem, dostane 1. 1. 2027 dnešek plus polovinu rozdílu (aspoň +{STEP1_CAP} tis.) a {STEP2_DATE} zbytek. Druhý krok potvrdí vlastník segmentu v červnu. Kdo roli, za kterou má příplatek, opravdu nenese, zůstává na prvním kroku a příplatek se přepočítá při roční evaluaci.",
        "",
        "Proč:",
        "",
        f"- **Rozpočet:** v roce 2027 to ušetří cca {str(round(save, 1)).replace('.', ',')} mil. Kč a náklad roste postupně, ne skokem v lednu.",
        "- **Ověření role:** příplatek se platí za odpovědnost, kterou člověk nese. Půl roku ukáže, že ji opravdu nese, a druhý krok je pak zasloužený, ne slíbený.",
        "- **Pojistka proti chybě v modelu:** role a procenta se zapisují poprvé. Když se ukáže chyba, opraví se před druhým krokem, ne zpětným snižováním.",
        "- **Zlepšení hned:** každý, kdo se narovnává, cítí rozdíl od ledna, aspoň +10 tis. nebo polovinu.",
        "- **Jen pro tým:** exekutiva a foundeři mají jednorázový skok od 1. 1. Fix schválí hlasováním celé vedení do konce roku a platí na celý rok, nikdo nevyjednává individuálně. Celá od 1. 1. platí i individuální dohoda.",
        "",
    ]


SHORT = {"Programátor": "prog", "Game designer": "GD", "Grafik DEV": "grafik DEV", "QA": "QA", "DevOps a IT": "DevOps",
         "UA manager": "UA", "Publishing a LiveOps": "publishing", "Grafik MKT": "grafik MKT", "Video a motion": "video"}
PASS_NAME = {"lead": "vedl projekt", "speaker": "přednášky", "event": "event", "mentor": "mentoring"}


def rozpis(team, exe, named=True):
    """Dvě tabulky: z čeho je fix, a kolik může kdo vydělat (minimum, plán, maximum)."""
    col = "Člověk" if named else "Pozice"
    who = lambda c: f"**{c['nick']}**" if named else LABEL[c["nick"]]
    passive = lambda c: ", ".join(f"{PASS_NAME[k]} +{r(PASSIVE[k][0]*min(n, PASSIVE[k][1]))}" for k, n in c["pas"].items()) or "–"
    a = ["**Z čeho je fix**", "",
         f"| {col} | Základ role | Roky ve firmě | Aktivní příplatky | Pasivní (historie) | Fix 2027 |",
         "|---|---|---|---|---|---|"]
    b = ["**Kolik může vydělat**", "",
         f"| {col} | Pásmo | Dnes | Fix 2027 | Minimum (plný malus) | Plán | Maximum (plný bonus) | Δ fixu |",
         "|---|---|---|---|---|---|---|---|"]
    for c in team:
        roles = " + ".join(f"{SHORT[k]} {int(v*100)} %" if v < 1 else SHORT[k] for k, v in c["roles"].items())
        base = c["base_t"] / (1 + c["tenure"])
        adds = ", ".join(f"{n} +{x}" for n, x in c["adds"]) or "–"
        if c["add_capped"]:
            adds += f" (strop 40 %: +{r(c['add'])})"
        fix = f"**{r(c['fix'])}**"
        if c["dohoda"]:
            fix += f" (dohoda, role {r(c['H'])})"
        elif c["garance"]:
            fix += f" (garance {r(c['garance'])})"
        a.append(f"| {who(c)} | {roles}, {c['lvl']}: {r(base)} | {c['years']} → +{r(c['base_t']-base)} | {adds} | {passive(c)} | {fix} |")
        b.append(f"| {who(c)} | {PASMO_NAME[c['pasmo']]} | {r(c['today'])} | **{r(c['fix'])}** | {r(c['low'])} | {r(c['plan'])} | {r(c['high'])} | {c['delta']:+.1f} |")
    for c in exe:
        ex = ", ".join(f"{n} +{x}" for n, x in c["extra"])
        adds = f"lidé pod sebou {c['people']} → +{r(c['pp'])}, rozpočet {c['opex']} % OPEX → +{r(c['bb'])}, {ex}"
        a.append(f"| {who(c)} | společný základ exekutivy {EXEC_BASE} | {c['years']} (bez vlivu) | {adds} | {passive(c)} | **{r(c['fix'])}** |")
        b.append(f"| {who(c)} | fix + podíl na zisku | {r(c['today'])} | **{r(c['fix'])}** | = fix | = fix | = fix | {c['delta']:+.1f} |")
    for nick, role, today, years, src in FOUNDERS:
        if named:
            note = f"návrh podle dneška: {src}"
            a.append(f"| **{nick}** | {note} | {years} | – | – | **{r(today)}** |")
            b.append(f"| **{nick}** | rada tří | {r(today)} | **{r(today)}** | – | – | – | 0 |")
        else:
            lab = role[0].upper() + role[1:]
            a.append(f"| {lab} | návrh podle dnešní odměny, mimo strop, schvaluje rada tří | {years} | – | – | dnešek |")
            b.append(f"| {lab} | rada tří | – | dnešek | – | – | – | 0 |")
    return table(a) + [""] + table(b)


def main():
    team = [calc_team(p) for p in TEAM]
    exe = [calc_exec(e) for e in EXEC]
    rows = team + exe
    today_year = sum(c["today"] for c in rows) * 12 / 1000
    out = []
    w = out.append
    w("# Model odměňování 2027 jmenovitě · důvěrné · k poradě 29. 10. 2026\n")
    w("> Generuje `model_odmenovani_2027.py`. Jen pro Davida a Martina B. (finanční dopad), nesdílet na hub.")
    w("> Dnes = Ø skutečně vyplacená odměna za práci 1–10/2026 z NoxHubu, bez coworkingu (průtokový náklad na kancelář).")
    w("> Roky = dokončené roky ve firmě k 1. 1. 2027 podle data nástupu v hubu (tenure achievementy).\n")
    w("## 1. Jak číst tabulky\n")
    w(f"- **H** = hodnota role: základ podle rolí a podílu × úroveň × (1 + 2 % za rok ve firmě, strop 20 % po 10 letech) + aktivní příplatky (nejvýš 40 % základu) + pasivní složka z achievementů (nejvýš {PASSIVE_CAP}).")
    w(f"- **Fix 2027** = H, nikdy pod dnešek (rozdíl drží osobní garance). U exekutivy společný základ {EXEC_BASE} + příplatky.")
    w(f"- **Strop základu** je {CAP} tis. Kč pro tým i exekutivu (CEO a foundeři mimo). Variabilní složka a podíly se do něj nepočítají. Nikdo pod exekutivou nemá ani s plným bonusem víc než nejnižší fix exekutivy.")
    w(f"- **1. 1. 2027** = první krok. V týmu jde narovnání nad {STEP1_CAP} tis. ve dvou krocích, druhý {STEP2_DATE}. Exekutiva jednorázově od 1. 1.")
    w("- **Exekutiva** nemá bonus ani malus: fix + podíl na zisku pod čarou. Minimum = maximum = fix.")
    w("- **Plán** = fix + polovina bonusu.\n")
    w("## 2. Rozpis všech ve firmě\n")
    w("Tis. Kč měsíčně. Minimum = fix s plným malusem, maximum = fix s plným bonusem. Bez poolu (prasátka), který se dělí zvlášť. Exekutiva má jen fix, k tomu podíl na zisku.\n")
    out.extend(rozpis(team, exe))
    w("")
    w("### Narovnání ve dvou krocích\n")
    steps = [c for c in team + exe if c["step1"] < c["fix"]]
    save = sum(6 * (c["fix"] - c["step1"]) for c in steps) / 1000
    out.extend(TWO_STEP(save))
    lines = ["| Člověk | Dnes | 1. 1. 2027 | " + STEP2_DATE + " | Δ celkem |", "|---|---|---|---|---|"]
    for c in steps:
        lines.append(f"| **{c['nick']}** | {r(c['today'])} | {r(c['step1'])} | {r(c['fix'])} | {c['delta']:+.1f} |")
    out += table(lines)
    w("")

    w("## 3. Tým pod exekutivou: detail\n")
    lines = ["| Člověk | Role (podíl), úroveň · příplatky | Roky | H | Dnes | Fix 2027 | Δ | 1. 1. 2027 | Pásmo | Bonus max | Malus max | Plán |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in team:
        roles = ", ".join(f"{k} {int(v*100)} %" if v < 1 else k for k, v in c["roles"].items())
        adds = "; ".join(f"+{a} {n}" for n, a in c["adds"]) or "bez příplatku"
        if c["add_capped"]:
            adds += f" (strop 40 %: {r(c['add'])})"
        if c["pv"]:
            adds += f"; pasivní +{r(c['pv'])}"
        g = f" (garance {r(c['garance'])})" if c["garance"] else ""
        if c["dohoda"]:
            g = f" ({c['dohoda'][1]})"
        lines.append(f"| **{c['nick']}** | {roles}, {c['lvl']} · {adds} | {c['years']} | {r(c['H'])} | {r(c['today'])} | "
                     f"{r(c['fix'])}{g} | {c['delta']:+.1f} | {r(c['step1'])} | {PASMO_NAME[c['pasmo']]} | "
                     f"+{r(c['bonus_max'])} | −{r(c['malus_max'])} | {r(c['plan'])} |")
    out += table(lines)

    w("\n## 4. Exekutiva: detail\n")
    lines = ["| Člověk | Základ | Lidé pod sebou | Rozpočet (% OPEX) | Role navíc | Pasivní | Fix 2027 od 1. 1. | Dnes | Δ |",
             "|---|---|---|---|---|---|---|---|---|"]
    for c in exe:
        ex = "; ".join(f"+{a} {n}" for n, a in c["extra"])
        lines.append(f"| **{c['nick']}** | {EXEC_BASE} | {c['people']} → +{r(c['pp'])} | {c['opex']} % → +{r(c['bb'])} | {ex} | +{r(c['pv'])} | "
                     f"**{r(c['fix'])}** | {r(c['today'])} | {c['delta']:+.1f} |")
    out += table(lines)
    top_team = max(c["high"] for c in team)
    low_exec = min(c["fix"] for c in exe)
    w(f"\nKontrola stropu: nejvyšší možná odměna v týmu (fix + plný bonus) je {r(top_team)}, nejnižší fix exekutivy {r(low_exec)}.".replace(".", ",", 2))

    w("\n## 5. Souhrn nákladů, varianta A (mil. Kč za rok 2027)\n")
    lines = ["| Skupina | Dnes | Špatný rok | Plán | Vše splněno |", "|---|---|---|---|---|"]
    for label, grp in (("Tým", team), ("Exekutiva", exe), ("Celkem", rows)):
        t = sum(c["today"] for c in grp) * 12 / 1000
        lines.append(f"| {label} | {t:.2f} | {year_cost(grp,'low'):.2f} | {year_cost(grp,'plan'):.2f} | {year_cost(grp,'high'):.2f} |")
    f_year = sum(f[2] for f in FOUNDERS) * 12 / 1000
    lines.append(f"| Foundeři a CEO (návrh = dnešek, mimo součet) | {f_year:.2f} | {f_year:.2f} | {f_year:.2f} | {f_year:.2f} |")
    out += table(lines)
    w("\nTým v roce 2027 s narovnáním ve dvou krocích, exekutiva celý rok plný fix. Od 2028 plný fix všem. Bez poolu (prasátka) a podílů na zisku, ty jdou ze zisku.")

    rows2 = [calc_team(p, override={"L": "J"}) for p in TEAM] + exe
    freeze = 0
    w("\n## 6. Tři varianty narovnání\n")
    w("A je preferovaná a nejdražší: splní závazek nejlepšího možného ohodnocení. B a C rozkládají rozdíl mezi dneškem a plným fixem rovnoměrně (dvě třetiny, třetina). Realisticky se může skončit u B.\n")
    out.extend(variants_md(True))
    w("\n## 7. Index ke stropu (základ role jako % ze 150)\n")
    lines = ["| Role | Základ | % stropu |", "|---|---|---|"]
    for k, v in list(BASE.items()) + [("Vlastník segmentu (společný základ)", EXEC_BASE)]:
        lines.append(f"| {k} | {v} | {round(100*v/CAP)} % |")
    out += table(lines)
    w(TAIL)
    Path(__file__).with_name("ODMENOVANI_2027_MODEL_JMENOVITE.md").write_text("\n".join(out) + "\n")
    prep = Path(__file__).with_name("PRIPRAVA_2026-10-29_ODMENOVANI.md")
    t = prep.read_text()
    i, j = t.index("## 6. "), t.index("## 7. ")
    body = ["## 6. Rozpis po pozicích", "",
            "Tis. Kč měsíčně, každý člověk ve firmě jako pozice bez jména. Minimum = fix s plným malusem, maximum = fix s plným bonusem, obojí bez poolu (prasátka). Exekutiva nemá bonus ani malus, jen fix a podíl na zisku. „Dnes“ je skutečně vyplacená průměrná odměna 1–10/2026 včetně pravidelných příplatků, bez coworkingu. Jmenovitě v důvěrném modelu.", ""]
    body += rozpis(team, exe, named=False)
    t = t[:i] + "\n".join(body) + "\n\n" + t[j:]
    k = t.index("### Narovnání ve dvou krocích") if "### Narovnání ve dvou krocích" in t else None
    two = ["### Narovnání ve dvou krocích", ""] + TWO_STEP(save) 
    if k is None:
        k = t.index("### Kde hledat úsporu")
        t = t[:k] + "\n".join(two) + "\n\n" + t[k:]
    else:
        e = t.index("### Kde hledat úsporu")
        t = t[:k] + "\n".join(two) + "\n\n" + t[e:]
    a9, b9 = t.index("## 9. "), t.index("## 10. ")
    body9 = ["## 9. Tři varianty narovnání", "",
             "**Preferujeme variantu A** a pokusíme se ji schválit: je nejdražší, ale splní závazek nejlepšího možného ohodnocení. B a C rozkládají rozdíl mezi dneškem a plným fixem rovnoměrně (dvě třetiny, třetina). Systém, pásma i pravidla jsou ve všech stejné, liší se jen, o kolik se fixy narovnají.", ""]
    body9 += variants_md(False)
    t = t[:a9] + "\n".join(body9) + "\n\n" + t[b9:]
    prep.write_text(t)

    print(f"dnes {today_year:.2f}; team {sum(c['today'] for c in team):.1f}/m exec {sum(c['today'] for c in exe):.1f}/m")
    for lbl, grp in (("team", team), ("exec", exe), ("all", rows)):
        print(lbl, "low/plan/high", f"{year_cost(grp,'low'):.2f} {year_cost(grp,'plan'):.2f} {year_cost(grp,'high'):.2f}",
              "fixΔ/yr", r(sum(6*c["step1"]+6*c["fix"]-12*c["today"] for c in grp)/1000),
              "fixΔ full", r(sum(12*(c["fix"]-c["today"]) for c in grp)/1000),
              "var plan", r(sum(12*c["bonus_max"]*PASMA[c["pasmo"]]["plan"] for c in grp)/1000))
    print("\n".join(variants_md(True)))
    for c in rows:
        print(f"{c['nick']:9} H {r(c['H']):6} today {r(c['today']):6} fix {r(c['fix']):6} d {c['delta']:+6.1f} s1 {r(c['step1']):6} plan {r(c['plan']):6} range {r(c['low'])}-{r(c['high'])}")


if __name__ == "__main__":
    main()
