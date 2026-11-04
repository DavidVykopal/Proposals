# City V2 meta: design dokument (pracovní verze)

> **Stav:** návrh, založeno 1. 11. 2026 z voice note Davida (`voice/Strategie.txt`). Vše označené *návrh* je doplněné autorem dokumentu, ne Davidem. Zbytek je z voice note nebo z existujících podkladů.
> **Názvy:** City V2 = Mapa V2 = Město V2. Jde o stejnou feature, názvy jsou zaměnitelné. V kódu a v backlogu používat `CityV2` (v CODE BACKLOG se dnes vede jako **Meta Village V2, CODE-9**, kontrola rozšiřitelnosti MF **CODE-65**).
> **Navazuje na:** `STRATEGIE_PRODUKCE.md`, wiki *Hexafort (Hexapolis 2)* (sekce město, Rise of Kingdoms jako reference), wiki *Mecha Fortress × Shared Game Backend: Integration Roadmap*.

## 1. Co to je a proč

Meta vrstva mimo hlavní gameplay. Hráč z materiálů vydělaných ve hře staví a rozšiřuje vlastní město. Inspirace: **Rise of Kingdoms, Clash of Clans**. Hráč začíná v malé vesnici, staví produkční budovy, ty umožní stavět a levelovat další budovy, a ty odemykají jednotky, upgrady a vylepšení základní hry.

Proč sdílené napříč portfoliem:

- **Jeden modul, všechny hry.** MF-branch reskiny, původní Hexapolis, Hexapolis 2 i nová větev strategických her. Vývoj se platí jednou, hodnota se násobí počtem titulů.
- **Hloubka, kterou hry dnes nemají.** MF má všechny meta systémy lokální, bez sociální vrstvy (viz SGB roadmapa). Hexapolis hráči dlouhodobě chtějí stavění.
- **Kreativita a exprese.** Hráč si město staví po svém, přizpůsobuje ho, má v něm i neprodukční věci. To dává důvod k porovnávání a návštěvám.
- **Základ pro sociální vrstvu a PvP.** Armády, útoky na města, obrana, globální mapa. Všechno se dá postavit kolem města, a proto to funguje stejně v každé hře.

## 2. Modul a kontrakt s hostitelskou hrou

City V2 je **samostatný vedlejší modul**. Se základní hrou komunikuje jen přes vstupy, výstupy a požadavky. Některé požadavky jsou navázané na základní hru, aby hráč musel hrát obojí.

### 2.1 Vstupy (hra posílá do City)

| Vstup | Příklad | Poznámka |
|---|---|---|
| Suroviny / materiály | dřevo, kámen, železo z odměn za zápas | sada surovin je config per titul a tematiku *(návrh)* |
| Měkká a tvrdá měna | gold, gems | existující Currency systém z meta-core |
| Progres hráče | dosažený level / svět / počet výher | používá se pro gating budov |
| Události ze hry | `match_completed`, `stage_cleared`, `pvp_won` | přes EventBus, City z nich počítá questy a produkci *(návrh)* |

### 2.2 Výstupy (City vrací hře)

| Výstup | Příklad | Poznámka |
|---|---|---|
| Odemčené jednotky | kasárna lvl 3 odemknou lučištníka | hra se ptá `IsUnlocked(unitId)` |
| Permanentní upgrady | +5 % HP jednotek, +1 slot ve skill choice | modifikátory, které hra aplikuje na start zápasu |
| Boosty | dočasný bonus k odměnám, rychlejší výroba | časově omezené |
| Odměny | suroviny, měna, karty | přes jeden reward bridge (`IRewardGranter` / SGB reward JSON) |
| Armáda | složení armády pro útok / obranu | až ve fázi 3 |

### 2.3 Požadavky (gating)

- Budova X vyžaduje progres ve hře (např. "projdi svět 3"), nejen suroviny. Tím se hráč vrací do gameplaye.
- Produkce surovin v městě je **doplněk**, ne náhrada zápasů. Hlavní příjem surovin jde ze hry *(návrh, balanc ladit na datech)*.

### 2.4 Technické zásady *(návrh, navazuje na principy SGB roadmapy)*

- Interface ve stylu meta-core DI (`ICityProvider`, `ICityRewardSink`, `ICityRequirementSource`), bez přímé závislosti na konkrétní hře.
- Obsah (budovy, ceny, časy, odemčení) je **config-driven** per titul. Tematika (fantasy, sci-fi, zombie, římská) mění jen asety a texty, ne logiku.
- Každá část za kill switchem (Firebase RC), dark launch a rollback bez buildu.
- City nikdy neblokuje hru. Když je backend nedostupný, město funguje lokálně a synchronizuje se později.

## 3. Core loop

1. Hráč odehraje zápas a dostane suroviny.
2. V městě postaví nebo vylepší **produkční budovu** (pila, lom, důl, farma).
3. Produkce a progres ve hře odemknou stavbu a levelování dalších budov.
4. Další budovy odemykají **jednotky, upgrady a vylepšení základní hry**.
5. Silnější armáda a vylepšení jdou zpátky do zápasu.

Doplňky v základní verzi:

- **Neprodukční budovy a dekorace:** volné umístění budov (Rise of Kingdoms, ne slotová mřížka, viz Hexafort dokument), kosmetika jako IAP sink.
- **Personalizace:** vzhled města, erb, jméno.
- **Rasa / frakce podle tematiky:** v tematikách, kde to dává smysl, si hráč vybírá rasu (např. lidé / orkové u Warcraft-like tematiky). Rasa mění vzhled a sadu jednotek.

## 4. Pozdější vrstvy

| Vrstva | Obsah | Závislost |
|---|---|---|
| Globální mapa | hráč vidí města ostatních hráčů | SGB: hráčské profily, persistence |
| Návštěvy | navštívit město jiného hráče, porovnat se, "závidět" | NOX ID, veřejná data města |
| Armády a útoky | postavit armádu, zaútočit na jiné město, bránit svoje | PvP vrstva (SGB podporuje, admin UI CODE-73) |
| Sociální vrstva | klany, společné cíle, žebříčky měst | SGB clans (F6), leaderboards (F4) |

## 5. Závislost na SharedGameBackend

| Co City potřebuje | SGB služba | Stav podle roadmapy (10/2026) |
|---|---|---|
| Identita hráče napříč tituly | NOX ID | Stage D |
| Perzistence města mimo zařízení | cloud save (SGB slot-based) | dnes MF používá UGS Cloud Save, přechod je Stage G a volitelný |
| Žebříčky měst | leaderboards | Stage F4 |
| Klany, přátelé | clans, friends API | Stage F2, F6 |
| PvP útoky na města | PvP (fortress raids) | "later, only after a game-design decision" |
| Odměny | reward bridge | Stage B5 |

Důsledek: **MVP (fáze 1) musí jít bez sociální vrstvy**, jen s lokálním stavem a stávajícím cloud save. Sociální a PvP vrstvy se zapínají podle postupu SGB roadmapy.

## 6. Fáze a scope

Podle voice note: **listopad začít, prosinec doručit, leden 2027 dostat mezi hráče.** Vyvíjí se v **Mecha Fortress jako staging projektu** (stejně jako SGB), potom se importuje do **původního Hexapolisu**. Nemusí se vyvíjet přímo ve starém Hexapolisu, důležité je mít to v moderní technologii (dotáhnout lze i v současném Hexfortu).

| Fáze | Kdy | Obsah | Kde |
|---|---|---|---|
| **1. MVP** | 11 až 12/2026 | vesnice, 3 až 4 produkční budovy, 3 až 4 budovy s odemčením (jednotky, upgrady), volné umístění, 2 až 3 dekorace, kontrakt vstupů a výstupů, analytika, RC flag | MF staging |
| **1b. Import** | 12/2026 | napojení do původního Hexapolisu, Hex suroviny a jednotky | Hexapolis |
| **Release a ověření** | 1/2027 | release hráčům, měření podle sekce 7, sběr feedbacku komunity | Hexapolis (případně MF) |
| **2. Hloubka** | Q1/2027 *(návrh)* | personalizace, rasy podle tematiky, více budov, IAP sinky | podle výsledku ověření |
| **3. Sociální a PvP** | od Q2/2027 *(návrh)* | globální mapa, návštěvy, armády a útoky, klany. Útoky nejdřív fake (bot města a uložená města hráčů), reálné útoky postupně, viz `STRATEGIE_PRODUKCE.md`, PvP postupně | závisí na SGB Stage D a F |

Mimo MVP: globální mapa, útoky, klany, rasy, UGC.

## 7. Ověření (co musí platit, aby šel City do Hexapolis 2 a dalších her)

| Otázka | Metrika | Laťka |
|---|---|---|
| Hrají lidé město? | % DAU, kteří otevřou City, počet staveb na hráče, návraty do City za den | TBD |
| Zlepšuje retenci? | D1, D7, D30 hráčů s City proti bez (A/B přes Firebased) | D7 a D30 nahoru, D1 bez poklesu |
| Prodlužuje session? | playtime / DAU, počet sessions za den | TBD |
| Monetizuje? | IAP konverze na City sinky (zrychlení, dekorace, balíčky surovin), ARPDAU | TBD |
| Zaplatí si subscription? | test subscription nabídky (např. VIP s bonusem produkce) | TBD |
| Co chce komunita? | feedback z Discordu / průzkumu, reaktivace starých hráčů | kvalitativně |

Referenční čísla MF (Hexafort dokument, okno 20. 5. až 13. 7. 2026): D1 26,5 %, D7 10,1 %, D30 4,2 %, podíl IAP asi 20 %.

## 8. Rizika

- **Produkční laťka Rise of Kingdoms.** Volné umístění znamená víc artu, víc stavů a víc balancu než mřížka. MVP držet malé.
- **Sdílenost nesmí zabít hloubku.** Generický modul bez vazby na hru je nuda. Kontrakt (sekce 2) musí mít vazby, které hráče vracejí do gameplaye.
- **Ekonomika ve dvou hrách naráz.** Balanc pro MF a Hex se liší. Config per titul je podmínka, ne nice to have.
- **Import do starého Hexapolisu.** Starší codebase, riziko integrace. Ověřit odhad při CODE-65 (rozšiřitelnost).
- **Termín leden 2027.** Dva měsíce na vývoj, import a release při běžícím live ops Q4. Kapacita Unity a QA je úzké hrdlo (stejně jako u SGB).
- **Sociální vrstva čeká na SGB.** Bez NOX ID a klanů není globální mapa ani útoky. Nepřislibovat je v MVP.

## 9. Otevřené otázky pro Davida

1. Kdo vlastní City V2 (design, vývoj) a kolik kapacity má v listopadu a prosinci?
2. Release v lednu: jen v původním Hexapolisu, nebo i v MF? MF je staging, jde tam City i k hráčům?
3. Zdroj surovin: jen ze zápasů, nebo i pasivní produkce (idle)? Kolik idle je v pořádku pro Hexapolis?
4. Jsou CODE-9 (Meta Village V2) a CODE-65 totéž co City V2, nebo se má backlog přejmenovat a sloučit?
5. Subscription: testovat už v lednovém releasu, nebo až ve fázi 2?
6. Laťky v sekci 7: jaké minimum musí City splnit, aby se schválil Hexapolis 2?
7. Rasy a frakce: patří do MVP pro některou tematiku, nebo až fáze 2?
