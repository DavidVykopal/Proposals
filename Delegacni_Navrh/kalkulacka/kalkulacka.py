#!/usr/bin/env python3
"""Referenční výpočet odměňování 2027 (NOXGAMES). Předloha pro kalkulačku v hubu.

    python3 -I kalkulacka.py                      # výchozí parametry
    python3 -I kalkulacka.py --scenar vystup-29-10
    python3 -I kalkulacka.py --vsechny            # všechny scénáře vedle sebe
    python3 -I kalkulacka.py --scenar 29-10-A --json vysledek.json

Bez závislostí (jen standardní knihovna). Vstupy: vstupy.json (lidé), parametry.json (ovladače).
Logika je popsaná v LOGIKA.md, čísla kapitol v komentářích na ni odkazují.
Částky v tis. Kč měsíčně, roční náklady v mil. Kč.
"""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).parent


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def params_for(base, scenar):
    p = {k: v for k, v in base.items() if k != "scenare"}
    if scenar:
        over = base["scenare"][scenar]
        for k, v in over.items():
            if not k.startswith("_"):
                p[k] = v
    return p


# ---------- 2. Hodnota role ----------
def pasivni(p, pas):
    s = sum(p["pasivni"][k][0] * min(n, p["pasivni"][k][1]) for k, n in pas.items())
    return min(s, p["pasivni_strop"])


def hodnota_tym(p, x):
    zaklad = sum(p["zaklady_roli"][r] * w for r, w in x["role"].items())
    zaklad *= p["uroven"][x["uroven"]] * p["benchmark_koeficient"]
    tenure = min(x["roky"] * p["tenure_krok"], p["tenure_strop"])
    zaklad_t = zaklad * (1 + tenure)
    prip_raw = sum(a for _, a in x["priplatky"])
    prip = min(prip_raw, p["priplatky_strop_podil_zakladu"] * zaklad_t)
    pv = pasivni(p, x["pasivni"])
    return dict(zaklad=zaklad, tenure=tenure, zaklad_t=zaklad_t, prip=prip,
                prip_oriznuto=prip_raw > prip, pasivni=pv, H=zaklad_t + prip + pv)


def hodnota_exekutiva(p, x):
    lidi = min(x["lidi_pod_sebou"] * p["exekutiva_za_cloveka"], p["exekutiva_za_cloveka_strop"])
    opex = x["opex_segmentu_pct"] * p["exekutiva_za_procento_opex"]
    navic = sum(a for _, a in x["role_navic"]) if p["exekutiva_role_navic"] else 0
    pv = pasivni(p, x["pasivni"]) if p["exekutiva_pasivni"] else 0
    return dict(zaklad=p["exekutiva_zaklad"], lidi=lidi, opex=opex, navic=navic, pasivni=pv,
                H=p["exekutiva_zaklad"] + lidi + opex + navic + pv)


# ---------- 4. Variabilní složka: 4 části s vahami ----------
def plneni_variabilni(p):
    """Vážené plnění 0..max ze čtyř částí. 1,0 = vše na plánu."""
    sl = {k: v for k, v in p["variabilni_slozky"].items() if not k.startswith("_")}
    w = sum(s["vaha"] for s in sl.values())
    return sum(s["vaha"] * s["plneni"] for s in sl.values()) / w if w else 0.0


def rozpad_slozek(p, var_cil):
    sl = {k: v for k, v in p["variabilni_slozky"].items() if not k.startswith("_")}
    w = sum(s["vaha"] for s in sl.values()) or 1
    return {s["nazev"]: var_cil * s["vaha"] / w for s in sl.values()}


# ---------- 3.–5. Celkový cíl, rozdělení fix / variabilní, garance ----------
def osoba(p, x, skupina):
    h = hodnota_tym(p, x) if skupina == "tym" else hodnota_exekutiva(p, x)
    dnes = x["dnes"]
    pasmo = x.get("pasmo", "D") if skupina == "tym" else "D"
    plny = max(h["H"], dnes)                         # plné narovnání: nikdy pod dnešek
    T = dnes + p["narovnani"] * (plny - dnes)        # 3. míra narovnání (A = 1, B = 2/3, C = 1/3)
    dohoda = x.get("dohoda")
    if dohoda:
        T = dnes + p["narovnani"] * (dohoda - dnes) if p["dohoda_skalovat"] else max(dohoda, dnes)

    if p["rezim_variabilni"] == "nad_fix":
        # Původní návrh 29. 10.: fix = T, bonus / malus jako % fixu navrch
        P = p["pasma_nad_fix"][pasmo]
        fix = min(T, p["strop_fixu"])
        var_cil = fix * P["bonus"] * P["plan"]
        var_max = fix * P["bonus"]
        var_min = -fix * P["malus"]
        podil_var = 0.0
    else:
        # Závěr 29. 10.: T je celková cílová odměna, z ní podíl v je variabilní
        v = p["variabilni_podil"][pasmo]
        fix = T * (1 - v)
        if p["garance"] == "fix":                    # 5. fix nikdy pod dnešek, variabilní je jen zbytek nad ním
            fix = max(fix, dnes)
        fix = min(fix, p["strop_fixu"])              # strop 150 jen na fix
        var_cil = max(T - fix, 0)
        var_max = var_cil * p["variabilni_max_nasobek"][pasmo]
        var_min = -fix * p["malus_trest"][pasmo]     # trest za pochybení, ne za nesplnění
        podil_var = var_cil / T if T else 0

    plneni = plneni_variabilni(p)
    if p["rezim_variabilni"] == "nad_fix":
        var_plan = var_cil
    else:
        var_plan = min(var_cil * plneni, var_max)

    # 6. dva kroky: Δ fixu nad krok1_min se dělí na 1. 1. a 1. 7.
    dva = p["dva_kroky_tym"] if skupina == "tym" else p["dva_kroky_exekutiva"]
    d = fix - dnes
    krok1 = fix if (not dva or d <= p["krok1_min"] or dohoda) else dnes + max(p["krok1_min"], d / 2)

    return dict(nick=x["nick"], skupina=skupina, pasmo=pasmo, dnes=dnes, H=h["H"], detail=h, T=T,
                fix=fix, krok1=krok1, var_cil=var_cil, var_plan=var_plan, var_max=var_max, var_min=var_min,
                podil_var=podil_var, slozky=rozpad_slozek(p, var_cil),
                minimum=fix + var_min, plan=fix + var_plan, maximum=fix + var_max,
                pod_dneskem_pri_nule=fix < dnes - 1e-9)


# ---------- 7. Náklady a kontroly ----------
def rok(rows, co, krok2=True):
    """Roční náklad 2027 v mil. Kč (krok1 leden–červen, fix červenec–prosinec).
    krok2=False: firma nesplnila bránu, druhý krok se neodemkne a celý rok platí krok1."""
    t = 0
    for r in rows:
        var = {"minimum": r["var_min"], "plan": r["var_plan"], "maximum": r["var_max"]}[co]
        t += 6 * r["krok1"] + 6 * (r["fix"] if krok2 else r["krok1"]) + 12 * var
    return t / 1000


def pool(p, ebitda_mil, delta_plan_mil):
    """8. Pool pro tým (prasátko) a podíl vedení ze zisku po zvýšení odměn. mil. Kč."""
    zisk = ebitda_mil - delta_plan_mil
    zisk = max(zisk, 0)
    vedeni = zisk * p["podil_vedeni"]
    zaklad = zisk - vedeni if p["pool_az_po_podilu_vedeni"] else zisk
    if p["pool_rezim"] == "above":
        pl = p["pool_sazba"] * max(0, zaklad - p["pool_prah_mil"])
    else:
        pl = p["pool_sazba"] * zaklad if zaklad >= p["pool_prah_mil"] else 0
    return dict(ebitda=ebitda_mil, po_odmenach=ebitda_mil - delta_plan_mil, pool=pl, vedeni=vedeni,
                firme_zbyde=ebitda_mil - delta_plan_mil - pl - vedeni)


def delta_pro(p, rows, dnes, naklady, ebitda_mil):
    """Δ plánu pro daný scénář zisku: pod bránou se druhý krok neodemkne."""
    brana = p.get("krok2_brana_mil")
    if brana is not None and ebitda_mil < brana:
        return rok(rows, "plan", krok2=False) - dnes
    return naklady["plan"] - dnes


def spocti(vstupy, p):
    rows = [osoba(p, x, "tym") for x in vstupy["tym"]] + [osoba(p, x, "exekutiva") for x in vstupy["exekutiva"]]
    tym = [r for r in rows if r["skupina"] == "tym"]
    exe = [r for r in rows if r["skupina"] == "exekutiva"]
    dnes = sum(r["dnes"] for r in rows) * 12 / 1000
    naklady = {co: rok(rows, co) for co in ("minimum", "plan", "maximum")}
    fixy = sum(6 * r["krok1"] + 6 * r["fix"] for r in rows) / 1000
    fixy_2028 = sum(12 * r["fix"] for r in rows) / 1000
    delta_plan = naklady["plan"] - dnes
    # Pravidlo odstupu: nikdo z týmu (max nebo plán) nad nejnižší exekutivou (fix nebo plán)
    k = "fix" if p["pravidlo_odstupu"] == "fix" else "plan"
    top = max(tym, key=lambda r: r["maximum"] if k == "fix" else r["plan"])
    low = min(exe, key=lambda r: r[k])
    odstup_ok = (top["maximum"] if k == "fix" else top["plan"]) <= low[k] + 1e-9
    return dict(rows=rows, dnes=dnes, naklady=naklady, fixy=fixy, fixy_2028=fixy_2028, delta_plan=delta_plan,
                plneni=plneni_variabilni(p),
                odstup=dict(pravidlo=k, tym=top["nick"], tym_hodnota=top["maximum"] if k == "fix" else top["plan"],
                            exekutiva=low["nick"], exekutiva_hodnota=low[k], ok=odstup_ok),
                pod_dneskem=[r["nick"] for r in rows if r["pod_dneskem_pri_nule"]],
                nad_stropem=[r["nick"] for r in rows if r["T"] - r["var_cil"] > p["strop_fixu"] + 1e-9],
                zisk=[pool(p, e, delta_pro(p, rows, dnes, naklady, e)) for e in p["zisk_adj_ebitda_mil"]],
                foundeři=vstupy["foundeři"])


# ---------- výstup ----------
def c(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")


def markdown(name, popis, p, res):
    out = [f"## Scénář: {name or 'výchozí'}", ""]
    if popis:
        out += [popis, ""]
    out += [f"Režim variabilní: `{p['rezim_variabilni']}` · garance: `{p['garance']}` · narovnání: {c(p['narovnani'], 2)} · "
            f"vážené plnění variabilní: {c(res['plneni'], 2)}", ""]
    out += ["| Kdo | Pásmo | Dnes | Hodnota role | Cíl celkem | Fix | 1. 1. | Variabilní cíl | Podíl var. | Min | Plán | Max |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in res["rows"]:
        flag = " ⚠" if r["pod_dneskem_pri_nule"] else ""
        out.append(f"| {r['nick']}{flag} | {r['pasmo']} | {c(r['dnes'])} | {c(r['H'])} | {c(r['T'])} | {c(r['fix'])} | {c(r['krok1'])} | "
                   f"{c(r['var_cil'])} | {c(100 * r['podil_var'], 0)} % | {c(r['minimum'])} | {c(r['plan'])} | {c(r['maximum'])} |")
    out += ["", "⚠ = fix je pod dneškem, dnešek drží jen variabilní složka na plánu. Min = fix minus malus jako trest (nebo plný malus v režimu nad_fix).", ""]
    n = res["naklady"]
    out += ["| Roční náklad 2027 (13 lidí, mil. Kč) | Hodnota |", "|---|---|",
            f"| Dnes | {c(res['dnes'], 2)} |", f"| Jen fixy | {c(res['fixy'], 2)} |",
            f"| Minimum (variabilní 0 nebo plný malus) | {c(n['minimum'], 2)} |", f"| Plán | {c(n['plan'], 2)} |",
            f"| Maximum | {c(n['maximum'], 2)} |", f"| Δ plánu proti dnešku | +{c(res['delta_plan'], 2)} |",
            f"| Fixy 2028 (plný náběh) | {c(res['fixy_2028'], 2)} |", ""]
    o = res["odstup"]
    out.append(f"- Odstup ({o['pravidlo']}): nejvýš v týmu {o['tym']} {c(o['tym_hodnota'])}, nejníž v exekutivě {o['exekutiva']} "
               f"{c(o['exekutiva_hodnota'])} → {'drží' if o['ok'] else 'NEDRŽÍ'}.")
    if res["pod_dneskem"]:
        out.append(f"- Pod dnešek při nulové variabilní: {', '.join(res['pod_dneskem'])}.")
    brana = p.get("krok2_brana_mil")
    if brana is not None:
        out.append(f"- Druhý krok fixu (1. 7.) se odemkne jen při Adj. EBITDA aspoň {c(brana)} mil. Kč; pod bránou platí celý rok 1. krok.")
    for z in res["zisk"]:
        out.append(f"- Adj. EBITDA {c(z['ebitda'])} mil.: po zvýšení odměn {c(z['po_odmenach'], 2)}, pool týmu {c(z['pool'], 2)}, "
                   f"podíl vedení {c(z['vedeni'], 2)}, firmě zbyde {c(z['firme_zbyde'], 2)} mil.")
    out.append("")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vstupy", default=HERE / "vstupy.json")
    ap.add_argument("--parametry", default=HERE / "parametry.json")
    ap.add_argument("--scenar")
    ap.add_argument("--vsechny", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()
    vstupy, base = load(a.vstupy), load(a.parametry)
    names = list(base["scenare"]) if a.vsechny else [a.scenar]
    md, dump = [], {}
    for n in names:
        p = params_for(base, n)
        res = spocti(vstupy, p)
        md += markdown(n, base["scenare"].get(n, {}).get("_popis") if n else None, p, res)
        dump[n or "vychozi"] = res
    print("\n".join(md))
    if a.json:
        Path(a.json).write_text(json.dumps(dump, ensure_ascii=False, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
