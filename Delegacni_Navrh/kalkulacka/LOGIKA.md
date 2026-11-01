# Odměňování 2027: logika výpočtu (předloha pro kalkulačku v hubu)

Tenhle balíček popisuje, jak se počítaly návrhy narovnání odměn na 6. delegační poradu (29. 10. 2026), a jak do toho vstupuje závěr té porady. Cílem je kalkulačka v hubu vedle DJovy `/admin/bonus-system` (záložky Odměna 2026 a Pool 2027), ve které si vedení posune parametry a najde návrh, na kterém se shodne.

**Soubory:**

| Soubor | Co to je |
|---|---|
| `LOGIKA.md` | tento popis: vstupy, vzorce, ovladače, kontroly |
| `kalkulacka.py` | referenční výpočet v Pythonu bez závislostí, slouží jako test pro implementaci v hubu |
| `parametry.json` | výchozí hodnoty všech ovladačů + pojmenované scénáře |
| `vstupy.json` | **důvěrné**: lidé, dnešní příjmy, role, roky. V hubu se mají brát živě z dat, ne z tohoto souboru |
| `ukazka_vystupu.md` | výstup `--vsechny` pro kontrolu, že implementace sedí |

```bash
python3 -I kalkulacka.py --vsechny                 # všechny scénáře
python3 -I kalkulacka.py --scenar vystup-29-10     # jeden scénář
python3 -I kalkulacka.py --scenar 29-10-A --json out.json
```

**Kontrolní čísla** (musí v implementaci vyjít, roční náklad 2027 v mil. Kč pro 13 lidí bez founderů a CEO):

| Scénář | Jen fixy | Plán | Max |
|---|---|---|---|
| 29-10-A | 13,07 | 13,62 | 14,16 |
| 29-10-B | 12,29 | 12,80 | 13,30 |
| 29-10-C | 11,49 | 11,96 | 12,43 |
| Dnes | 10,40 | | |

Všechny částky jsou v tis. Kč měsíčně, roční náklady v mil. Kč.

---

## 1. Kdo je v modelu

- **Tým** (10 lidí): pásmo **J** = Jistota (řadové pozice), **L** = Lead (vedou projekt nebo tým).
- **Exekutiva** (David, DJ, Kuba): pásmo **D**.
- **Foundeři a CEO** (Mirek, Peko, Jirka): **mimo model**, jen se zobrazují pro srovnání. Jejich odměnu schvaluje rada tří, nepočítají se do nákladů ani do stropu.

**Dnes** = průměr skutečně vyplacené odměny za práci 1–10/2026 (hodiny × sazba z výplatních karet + pravidelné dofakturace). Coworking se nepočítá, je to průtokový náklad na kancelář. V hubu: `compensation_records` za období, `group_by` měsíc, průměr.

## 2. Hodnota role (H)

**Tým:**

```
základ   = Σ (základ_role[r] × podíl_r) × úroveň × benchmark_koeficient
tenure   = min(roky × tenure_krok, tenure_strop)          # 2 % za rok, strop 20 % (10 let)
základ_t = základ × (1 + tenure)
příplatky = min(Σ aktivních příplatků, priplatky_strop_podil_zakladu × základ_t)   # strop 40 %
pasivní  = min(Σ achievementů × váha, pasivni_strop)       # lead +2 (max 2×), speaker +1 (3×), event +1 (3×), mentor +0,5 (4×); strop 8
H        = základ_t + příplatky + pasivní
```

- `základ_role`: Programátor 80, UA 62, GD 60, DevOps 60, Publishing 58, Grafik MKT 56, Video, Grafik DEV a QA 52. Kotva je trh v Brně (ISPV 2025), nad průměrem netech, pod korporáty.
- `úroveň`: junior 0,8, medior 0,9, senior 1,0.
- `benchmark_koeficient` (nový ovladač, výchozí 1,0): Jirka namítl, že ISPV jsou hrubé mzdy zaměstnanců, kdežto my platíme faktury IČO. Koeficient pod 1 (např. 0,9) přepočte trh na fakturaci.
- **Roky ve firmě** z hubu: `profile_stats.joined_at`, tenure achievementy. **Achievementy** (lead, speaker, event, mentor) z odznaků v hubu.

**Exekutiva:**

```
H = exekutiva_zaklad (110)
  + min(lidí pod sebou × exekutiva_za_cloveka, exekutiva_za_cloveka_strop)    # +1 za člověka, max 6
  + opex_segmentu_pct × exekutiva_za_procento_opex                           # +0,1 za % OPEX firmy
  + role navíc (přepínač)  + pasivní (přepínač)
```

Jirka považuje příplatky za lidi a za % OPEX za pobídku k nabírání a utrácení („empire building“). Proto jsou to samostatné ovladače, které jdou nastavit na 0.

## 3. Míra narovnání a cílová odměna (T)

```
plný  = max(H, dnes)                          # nikdo pod dnešek
T     = dnes + narovnani × (plný − dnes)      # 1 = varianta A, 2/3 = B, 1/3 = C, posuvník 0–1
```

Individuální dohoda (dnes jen Milan, 85): `T = max(dohoda, dnes)`, nebo se škáluje stejně jako ostatní, když je zapnutý `dohoda_skalovat`. Bez škálování v B a C předběhne lídry.

## 4. Fix a variabilní složka

Dva režimy (`rezim_variabilni`):

**`nad_fix`**: návrh, jak šel na poradu 29. 10. Fix = T (strop 150), bonus a malus jsou procento fixu navrch:

| Pásmo | Bonus max | Malus max | Na plánu |
|---|---|---|---|
| J | 10 % | 5 % | polovina bonusu |
| L | 15 % | 7,5 % | polovina bonusu |
| D | 0 | 0 | exekutiva jen fix + podíl na zisku |

**`podil_z_celku`**: závěr porady 29. 10. T je celková cílová odměna na plánu a její část je variabilní:

| Pásmo | Variabilní podíl z T (výchozí) |
|---|---|
| J (ostatní) | 10 % |
| L (lead) | 25 % |
| D (exekutiva) | 50 % |

```
fix     = T × (1 − v)
fix     = max(fix, dnes)        jen když garance = "fix"
fix     = min(fix, strop_fixu)  # 150, platí jen na fix, ne na variabilní a podíly
var_cíl = max(T − fix, 0)       # variabilní na plánu (100 % plnění)
var_max = var_cíl × variabilni_max_nasobek[pásmo]     # výchozí 1,5×
var_min = −fix × malus_trest[pásmo]                   # J 5 %, L 7,5 %, D 10 %
```

V režimu `podil_z_celku` stojí firmu na plánu stejně obě garance, liší se jen tím, kdo nese riziko.

**Malus** (porada 29. 10.): není za nesplnění cílů. Za nesplnění člověk prostě nedostane variabilní. Malus je trest za skutečné pochybení, třeba ztrátu peněz vlastní chybou nebo vynechávání 1:1 a práce. Proto se ukazuje jen jako minimum a do plánu nevstupuje.

### 4.1 Čtyři části variabilní složky

Variabilní složka se skládá ze čtyř částí. Každá má **váhu** (výchozí 1 : 1 : 1 : 1) a **plnění** (0 až max násobek, 1,0 = na plánu):

| Klíč | Část | Odkud se bere |
|---|---|---|
| `mentor` | Osobní hodnocení mentora | hodnocení v hubu |
| `ukoly_1on1` | Splnění úkolů z 1:1 | úkoly z 1:1 v hubu |
| `kpi_firma` | Firemní KPI (profitabilita, kumulativní zisk) | Adj. EBITDA / kumulativní profit (OKR) |
| `kpi_pozice` | Osobní KPI pozice | KPI role ze stránky segmentu |

Příklad: variabilní 20 % = mentor 5 % + úkoly z 1:1 5 % + firemní KPI 5 % + KPI pozice 5 %.

```
podíl části i  = váha_i / Σ váh
plnění         = Σ (váha_i × plnění_i) / Σ váh
var_výplata    = min(var_cíl × plnění, var_max)
```

V kalkulačce by měly jít váhy nastavit globálně. Ideálně i zvlášť pro pásmo (exekutiva může mít víc firemních KPI, tým víc mentora). V referenčním skriptu jsou zatím globální.

### 4.2 Garance (přepínač `garance`)

- **`fix`**: fix nikdy neklesne pod dnešek. Komu je dnešek blízko cíli, tomu efektivní variabilní podíl klesne (ve výstupu sloupec „Podíl var.“). To je původní slib „nikdo si nepohorší“.
- **`plan`**: garantovaný je jen součet fix + variabilní na plánu ≥ dnešek. Při nulovém plnění jde člověk pod dnešek a výstup ho označí ⚠. Tohle je varianta, kde exekutiva nese stejné riziko jako firma, jak chtěl Jirka.

## 5. Dva kroky

```
Δ = fix − dnes
krok1 (1. 1.) = fix,                          když Δ ≤ krok1_min (10) nebo dohoda
              = dnes + max(krok1_min, Δ / 2), jinak
od 1. 7. plný fix
```

Zvlášť přepínač pro tým (`dva_kroky_tym`, výchozí ano) a pro exekutivu (`dva_kroky_exekutiva`). Jirka namítl „dvojí metr“, když exekutiva jde jedním skokem. Ve scénáři `vystup-29-10` jdou ve dvou krocích všichni. Variabilní složka běží celý rok.

**Brána druhého kroku** (`krok2_brana_mil`, porada 29. 10., návrh Davida jako odpověď na Jirkovu obavu „vydělá to firma vůbec“): druhý krok se neodemkne podle data, ale podle výsledku firmy. Když Adj. EBITDA nedosáhne brány, platí celý rok 1. krok. Hodnota `null` bránu vypne. V kalkulačce se brána nastavuje proti scénáři zisku. Ideálně ji brát z kumulativního profitu H1 v OKR (stejná metrika jako gate bonusů).

Ve scénáři `vystup-29-10` má brána malý efekt, protože fix drží garance na dnešku a nárůst sedí hlavně ve variabilní složce. Tam ho řídí plnění čtyř částí, z nichž jedna je firemní KPI.

## 6. Kontroly (zobrazit jako semafory)

- **Odstup** (`pravidlo_odstupu`): nikdo z týmu nad nejnižší exekutivou.
  - `fix`: max týmu (fix + plný bonus) ≤ nejnižší fix exekutivy (původní pravidlo).
  - `plan`: plán týmu ≤ nejnižší plán exekutivy. S 50 % variabilní u exekutivy dává smysl jen tohle; Jirka upozornil, že senior programátor s vyšším fixem než manažer je v oboru běžný.
- **Pod dnešek při nule**: kdo by při nulovém plnění variabilní šel pod dnešek.
- **Strop fixu 150**: komu ho fix tlačí.
- **Srovnání s foundery a CEO**: Jirka namítl, že tři manažeři by měli vyšší garantovaný fix než CEO (99,6). Zobrazit vedle exekutivy.

## 7. Náklady

```
rok 2027 = Σ (6 × krok1 + 6 × fix + 12 × var)        # var = var_min | var_plán | var_max
fixy 2028 = Σ 12 × fix
Δ plánu = plán 2027 − dnes × 12
```

Ukázat řádky: dnes, jen fixy, minimum, plán, maximum, Δ plánu, fixy 2028. Jirka upozornil, že 2028 je dražší než 2027 (druhý krok běží celý rok) a že čísla jsou bez odvodů a bez podílů. Obojí uvést přímo u tabulky.

## 8. Zisk, pool a podíl vedení

```
zisk po odměnách = Adj. EBITDA − Δ plánu
podíl vedení     = zisk po odměnách × podil_vedeni               # pod čarou
základ poolu     = zisk po odměnách (nebo po odečtení podílu vedení, přepínač)
pool             = pool_sazba × základ  (rezim "unlock": až od prahu; "above": jen nad prahem)
firmě zbyde      = zisk po odměnách − pool − podíl vedení
```

- **Pool pro tým (prasátko)**: rozhodnuto 29. 10., 5 % ze zisku pro tým, exekutiva a foundeři vyjmuti. Plní se měsíčně a je vidět, včetně milníků (např. 200k / 500k / 1M USD). Při splnění milníku do 30. 9. se může část vyplatit dřív. Výplata ve dvou částech (prosinec a červen, nebo březen a září, otevřené).
- **Rozdělení poolu**: váhou roční průměrný příjem včetně variabilní složky. DJova verze v hubu váží měsíční odměnou (`pool2027.ts`, `poolShares`), stačí změnit váhu.
- **Podíl vedení**: Jirka 29. 10. připomněl, že podle rozhodnutí z 22. 10. se nebude dělit 40 % EBITDA. Procento je potřeba stanovit, výchozí 20 % je jen pracovní.
- **Podíl z dealů** (5 % navrhovatel + 5 % executor ze zisku dealu): mimo model, počítá se po dealech. Jirka namítl double-dipping u exekutivy. V kalkulačce stačí přepínač „exekutiva má / nemá podíl z dealů“ a poznámka.
- Scénáře zisku: Adj. EBITDA 5 a 10 mil. Kč (Martin B., 22. 10.). V hubu je lepší brát projekci z cashflow modulu.

## 9. Scénáře v `parametry.json`

| Klíč | Co ukazuje |
|---|---|
| `29-10-A`, `-B`, `-C` | návrh, jak šel na poradu (plné, dvě třetiny, třetina narovnání) |
| `vystup-29-10` | závěr porady: 50 / 25 / 10 %, garance fixu, dva kroky pro všechny, brána druhého kroku 8 mil. |
| `vystup-29-10-riziko` | totéž, ale garance jen fix + plán (fix exekutivy jde pod dnešek) |
| `jirka-bez-opex` | navíc bez příplatků exekutivy za lidi a za % OPEX |

## 10. Známé chyby ve vstupech (opravit před dalším nápočtem)

- **Richi:** v datech vychází asi 120 h měsíčně, přitom má normální plný úvazek. Na poradě to vypadalo na díru v datové vrstvě (dovolená nebo nezapsané hodiny). Dnešek 79,4 = hodiny 59,4 + 20 tis. dofakturace, ověřit hodiny po měsících.
- **Peko:** Jirka na poradě zmínil, že částka 245 je nejspíš i s DPH. Ověřit a případně přepočítat bez DPH. Foundeři jsou mimo náklady modelu, ale číslo se ukazuje ve srovnání.
- **Milan:** na poradě padlo 3 600 až 3 700 EUR (dnes 3 000, původně chtěl 3 200 až 3 300). V `vstupy.json` je dohoda 85 tis. (cca 3 510 EUR). Až bude dohoda uzavřená, opravit `dohoda`.
- **Dnešek s přesčasy:** Jirka namítl, že průměr 1–10/2026 obsahuje přesčasy a hodiny bez úkolu. Přepínač pro implementaci: dnešek = skutečnost, nebo dnešek = sazba × úvazek (160 h). Podklad pro druhou variantu je ve výplatních kartách (sazba a úvazek).

## 11. Doporučení pro implementaci v hubu

- Výpočet jako čistá funkce v `src/lib/bonus/` (vzor `pool2027.ts`), testy proti kontrolním číslům výše (vzor `scenario2026.test.ts`).
- Vstupy živě: `compensation_records` (dnes), `profile_stats.joined_at` (roky), achievementy (pasivní), role a podíly ze stránek segmentů. Ruční přepis po lidech jako u Odměny 2026.
- Ovladače: posuvník narovnání 0–1, tři posuvníky variabilního podílu po pásmech, čtyři váhy a čtyři plnění částí, přepínač garance, přepínače dvou kroků, příplatky exekutivy (za člověka, za % OPEX, role navíc, pasivní), strop fixu, benchmark koeficient, zisk a pool.
- Uložené scénáře (jako `scenario-actions.ts`), aby šlo hlasovat o konkrétní pojmenované sadě parametrů. Na poradě zaznělo, že si každý udělá vlastní preset, vrátí se s ním a presety se porovnají.
- Kuba chce vidět rozsah nákladů (např. „+1 mil. ročně“) dřív, než se schvaluje rozpočet 2027. Souhrn nákladů a dopad na zisk proto patří nahoru, nad tabulku lidí.
- **Přístup**: jen vedení (exekutiva + foundeři). Obsahuje jména a příjmy všech.
