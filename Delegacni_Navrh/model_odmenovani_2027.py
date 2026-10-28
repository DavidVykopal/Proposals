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
CAP = 150              # strop základu ve firmě (dekret), nad něj jen podíl na zisku
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
TENURE_STEP, TENURE_CAP = 0.02, 0.10
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
    "D": dict(bonus=0.40, malus=0.10, plan=0.5),
}
PASMO_NAME = {"J": "Jistota", "L": "Lead", "D": "Dynamika"}
STEP1_CAP = 10
STEP2_DATE = "1. 7. 2027"
EUR = 24.2             # kurz pro dohody v eurech
# Individuální dohody nad hodnotou role: nick -> (fix v tis. Kč, popis). Platí od 1. 1. celé, bez dvou kroků.
DOHODA = {"Milan": (3600 * EUR / 1000, "dohoda 3 600 EUR (Milan chtěl 3 700 až 4 000, zápis 21. 9.)")}

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
     [("QA lead", 8)], {}, "L"),
    ("David Č.", "Produkce", 36.8, 0, "junior", {"Grafik DEV": 1}, [], {}, "J"),
    ("Richi", "Marketing", 59.4, 4, "senior", {"UA manager": 1}, [], {}, "J"),
    ("Ondra", "Marketing", 58.8, 4, "senior", {"Grafik MKT": 1}, [], {}, "J"),
    ("Ruda", "Marketing", 42.8, 2, "senior", {"Video a motion": 1}, [], {}, "J"),
]
# Exekutiva: nick, segment, dnes, roky, lidé pod sebou, podíl segmentu na OPEX %, role navíc [(název, tis.)], pasivní {kód: počet}
EXEC = [
    ("David", "Produkce", 105.5, 6, 7, 45, [("consigliere: agenda exekutivy, plány a strategie", 5)], {"lead": 2, "speaker": 3}),
    ("DJ", "Operations", 77.7, 9, 1, 24, [("finance, rozpočet a smlouvy celé firmy", 5)], {}),
    ("Kuba", "Marketing", 81.4, 5, 3, 20, [("analytika pro Produkci (přechodně)", 2)], {}),
]
EXEC_PEOPLE = (1.0, 6)   # +1 za člověka pod sebou, nejvýš 6
EXEC_BUDGET = 0.10       # +0,1 za každé procento OPEX segmentu

TAIL = """
## 7. Foundeři, CEO a podíly na zisku

- **Mirek, Peko, Jirka (CEO):** úplně mimo model. Jejich odměnu schvaluje rada tří (Majitelé).
- **Podíl na zisku** má exekutiva (David, Kuba, DJ, Jirka) a foundeři Peko a Mirek. Nikdo z nich není v poolu pro tým. Exekutiva si bonus vyplácí průběžně podle KPI, pololetní a roční pool je jen pro lidi pod exekutivou.

## 8. Co ještě doplnit

- **Pasivní složka:** podle Davida 28. 10. má historii leadů a přednášky David (+7), vedení projektu Čoud (+2). Přednášky má jinak jen Jirka (mimo model). Chybí DJ a Kuba. V hubu doplnit odznaky `speaker` a nové „vedl projekt“, ať to sedí se systémem.
- **Milan:** hodnota role 80 (3 300 EUR po zkušebce), dohoda 3 600 EUR = cca 87 tis. od 1. 1. Zápis z 21. 9. uvádí požadavek „4 000 EUR, resp. 90 tis. Kč“ (90 tis. je cca 3 700 EUR). Nad 3 600 si může vydělat bonusem (Jistota až +10 %). Pod Čoudem zůstává ve fixu i na plánu. 10. 9. padlo rozhodnutí plat zmrazit a revidovat za 3 měsíce, dohoda 3 600 je tedy zároveň ta revize.
- **Lidé pod DJ v Operations:** potvrzeno 1. Až Operations poroste (např. happy office), příplatek se posune při roční evaluaci.
- **Odstup v exekutivě:** s pasivní složkou je David o 14 tis. nad DJ. Pokud má rozdíl zůstat malý, dá se pasivní složka exekutivy vynechat (David by měl 125,5).
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
                    fix=fix, garance=max(0, today - H), pasmo=pasmo, dohoda=dohoda))
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
    return finish(dict(nick=nick, seg=seg, today=today, years=years, people=people, opex=opex, extra=extra,
                       pp=pp, bb=bb, ex=ex, pv=pv, H=fix, fix=fix, garance=0, pasmo="D"))


def finish(c: dict[str, Any]) -> dict[str, Any]:
    P = PASMA[c["pasmo"]]
    c["delta"] = c["fix"] - c["today"]
    c["step1"] = c["fix"] if c["delta"] <= STEP1_CAP else c["today"] + max(STEP1_CAP, c["delta"] / 2)
    c["bonus_max"] = c["fix"] * P["bonus"]
    c["malus_max"] = c["fix"] * P["malus"]
    c["plan"] = c["fix"] + c["bonus_max"] * P["plan"]
    c["low"], c["high"] = c["fix"] - c["malus_max"], c["fix"] + c["bonus_max"]
    return c


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
    w(f"- **H** = hodnota role: základ podle rolí a podílu × úroveň × (1 + 2 % za rok ve firmě, strop 10 %) + aktivní příplatky (nejvýš 40 % základu) + pasivní složka z achievementů (nejvýš {PASSIVE_CAP}).")
    w(f"- **Fix 2027** = H, nikdy pod dnešek (rozdíl drží osobní garance). U exekutivy společný základ {EXEC_BASE} + příplatky.")
    w(f"- **Strop** základu ve firmě je {CAP} tis. Kč. Nikdo pod exekutivou nemá fix ani s plným bonusem vyšší než nejnižší fix exekutivy.")
    w(f"- **1. 1. 2027** = první krok. Narovnání nad {STEP1_CAP} tis. jde ve dvou krocích, druhý {STEP2_DATE}.")
    w("- **Plán** = fix + polovina bonusu.\n")

    w("## 2. Tým pod exekutivou\n")
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

    w("\n## 3. Exekutiva\n")
    lines = ["| Člověk | Základ | Lidé pod sebou | Rozpočet (% OPEX) | Role navíc | Pasivní | Fix 2027 | Dnes | Δ | 1. 1. 2027 | Bonus max | Malus max | Plán |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in exe:
        ex = "; ".join(f"+{a} {n}" for n, a in c["extra"])
        lines.append(f"| **{c['nick']}** | {EXEC_BASE} | {c['people']} → +{r(c['pp'])} | {c['opex']} % → +{r(c['bb'])} | {ex} | +{r(c['pv'])} | "
                     f"{r(c['fix'])} | {r(c['today'])} | {c['delta']:+.1f} | {r(c['step1'])} | +{r(c['bonus_max'])} | −{r(c['malus_max'])} | {r(c['plan'])} |")
    out += table(lines)
    top_team = max(c["high"] for c in team)
    low_exec = min(c["fix"] for c in exe)
    w(f"\nKontrola stropu: nejvyšší možná odměna v týmu (fix + plný bonus) je {r(top_team)}, nejnižší fix exekutivy {r(low_exec)}.".replace(".", ",", 2))

    w("\n## 4. Souhrn nákladů (mil. Kč za rok 2027)\n")
    lines = ["| Skupina | Dnes | Špatný rok | Plán | Vše splněno |", "|---|---|---|---|---|"]
    for label, grp in (("Tým", team), ("Exekutiva", exe), ("Celkem", rows)):
        t = sum(c["today"] for c in grp) * 12 / 1000
        lines.append(f"| {label} | {t:.2f} | {year_cost(grp,'low'):.2f} | {year_cost(grp,'plan'):.2f} | {year_cost(grp,'high'):.2f} |")
    out += table(lines)
    w("\nFix v roce 2027 počítá narovnání ve dvou krocích. Od 2028 plný fix po celý rok.")

    rows2 = [calc_team(p, override={"L": "J"}) for p in TEAM] + exe
    freeze = sum(12 * (c["today"] + c["today"] * PASMA[c["pasmo"]]["bonus"] * PASMA[c["pasmo"]]["plan"]) for c in rows) / 1000
    w("\n## 5. Varianty (mil. Kč za 2027, plán)\n")
    lines = ["| Varianta | Plán | Δ proti dnešku |", "|---|---|---|"]
    for label, val in (("1 · Tři pásma Jistota / Lead / Dynamika (doporučeno)", year_cost(rows, "plan")),
                       ("2 · Dvě pásma (lídři v Jistotě)", year_cost(rows2, "plan")),
                       ("3 · Zmrazit dnešní odměnu jako fix, jen přidat variabilní složku", freeze)):
        lines.append(f"| {label} | {val:.2f} | {val - today_year:+.2f} |")
    out += table(lines)

    w("\n## 6. Index ke stropu (základ role jako % ze 150)\n")
    lines = ["| Role | Základ | % stropu |", "|---|---|---|"]
    for k, v in list(BASE.items()) + [("Vlastník segmentu (společný základ)", EXEC_BASE)]:
        lines.append(f"| {k} | {v} | {round(100*v/CAP)} % |")
    out += table(lines)
    w(TAIL)
    Path(__file__).with_name("ODMENOVANI_2027_MODEL_JMENOVITE.md").write_text("\n".join(out) + "\n")

    print(f"dnes {today_year:.2f}; team {sum(c['today'] for c in team):.1f}/m exec {sum(c['today'] for c in exe):.1f}/m")
    for lbl, grp in (("team", team), ("exec", exe), ("all", rows)):
        print(lbl, "low/plan/high", f"{year_cost(grp,'low'):.2f} {year_cost(grp,'plan'):.2f} {year_cost(grp,'high'):.2f}",
              "fixΔ/yr", r(sum(6*c["step1"]+6*c["fix"]-12*c["today"] for c in grp)/1000),
              "fixΔ full", r(sum(12*(c["fix"]-c["today"]) for c in grp)/1000),
              "var plan", r(sum(12*c["bonus_max"]*PASMA[c["pasmo"]]["plan"] for c in grp)/1000))
    print("v2", f"{year_cost(rows2,'plan'):.2f}", "v3", f"{freeze:.2f}", "top team", r(top_team), "low exec", r(low_exec))
    for c in rows:
        print(f"{c['nick']:9} H {r(c['H']):6} today {r(c['today']):6} fix {r(c['fix']):6} d {c['delta']:+6.1f} s1 {r(c['step1']):6} plan {r(c['plan']):6} range {r(c['low'])}-{r(c['high'])}")


if __name__ == "__main__":
    main()
