# Obnova Hexapolisu: PvP + City V2

> **Stav:** koncept, 4. 11. 2026, podle Davidova zadání. Věci označené *(návrh)* jsou návrh autora dokumentu.
> **Rozhodnutí 4. 11. 2026:** HexFort jako projekt Hexapolis 2 se ruší, práce se vrací do původního Hexapolisu. Nový Hexapolis 2 vznikne až po ověření celku, jako hex gameplay nasazený na MF metu.
> **Detaily:** `DESIGN_HEX_PVP.md` (PvP), `DESIGN_CITY_V2.md` (město). **Patří k:** `STRATEGIE_PRODUKCE.md`, větev 2.
> **Pro AI agenty:** tento soubor drží celkovou myšlenku a vazby. Pravidla jednotlivých featur jsou v detailních dokumentech; když se liší, platí detailní dokument.

## 1. Shrnutí

- **HexFort (dosavadní Hexapolis 2) rušíme**, bez ověření je to příliš velké riziko. Práce se vrací do **původního Hexapolisu**.
- V Hexu ověříme tři featury jako celek: **PvP, City V2 (mapa) a UGC**. První dvě jdou k hráčům v lednu 2027, UGC hned po nich. Testujeme **jednoduše, přímo v původní hře**.
- **PvP** má dva segmenty: **Skill only** (stejný setup pro všechny, nejblíž Polytopii) a **All-out-power** (rozhoduje i meta síla, 5 lig). Na start Quick game ve variantách Speed a Normal, žebříčky denní, týdenní a měsíční s odměnami a achievementy.
- **City V2** je co nejbližší klon Clash of Clans a Rise of Kingdoms: v první verzi stavění, sběr surovin a upgrady. **Budovy zvyšují meta staty.**
- Featury do sebe zapadají: **PvP dává suroviny do města, město dává sílu do All-out-power PvP.** Skill only zůstává čistý souboj.
- Cíl: **oživit Hexapolis** (komunita, návrat hráčů, revenue) a z dat rozhodnout o **novém Hexapolis 2**: když celek funguje, udělá se **design hex gameplaye nasazeného na MF metu** a podle něj nový projekt.

## 2. Proč obnova a ne rovnou nová hra

- **Komunita chce právě tohle:** hrát proti sobě a stavět. PvP je nejčastější přání a hlavní důvod, proč nás přetahuje Polytopia.
- **Nejlevnější ověření:** živá hra s komunitou a revenue (dnes cca $15k měsíčně), žádný nový titul, žádný UA na start.
- **Data rozhodnou o Hexapolis 2:** jestli hráči hrají PvP, staví město, tvoří mapy a platí. Teprve potom vznikne nový projekt Hexapolis 2: **hex gameplay na MF metě**, "jak měl Hexapolis vždycky vypadat". HexFort se v současné podobě nedokončuje.
- **Hex zůstává civilizace.** Tahy, mapa, expanze, rozhodnutí. Nezidlovat ho, idle varianty patří do strategické větve.

## 3. Jak to do sebe zapadá

Smyčka hráče:

1. Hraje **kampaň nebo PvP** a získává suroviny, měnu a odměny z žebříčků.
2. Za suroviny **staví a upgraduje město** (City V2), klon CoC a RoK.
3. Budovy jako kasárna, kovárna a akademie **zvyšují meta staty** (HP, útok, talenty).
4. Silnější meta se projeví v **kampani a v PvP All-out-power**, kde soupeří v lize s podobně silnými hráči.
5. Umístění v žebříčcích dává **odměny, achievementy a trofeje**, které se ukazují i ve městě.

| | Skill only | All-out-power | City V2 |
|---|---|---|---|
| Rozhoduje | jen dovednost | dovednost + meta síla | čas, suroviny, rozhodnutí |
| Vazba na město | odměny dávají suroviny | odměny dávají suroviny, **město dává sílu** | zdroj meta statů |
| Monetizace | jen kosmetika a pohodlí | jednotky, talenty, zrychlení města | zrychlení, stavitelé, balíčky, VIP |
| Pro koho | hráči Polytopie, férový souboj | hráči, kteří investovali do Hexu | všichni, dlouhodobý cíl |

## 4. Co hráč dostane v lednu 2027

| Featura | Obsah |
|---|---|
| PvP Skill only | Quick game Speed a Normal, presety národů, žebříčky, achievementy |
| PvP All-out-power | Quick game Speed a Normal, vlastní jednotky a talenty, 5 lig, postup top 10 % |
| Žebříčky a odměny | denní, týdenní, měsíční v obou segmentech, přes SharedGameBackend |
| City V2 verze 1 | radnice, stavitelé, produkční budovy a sběr, sklad, budovy s meta staty, dekorace, questy |
| Onboarding | prvních několik PvP zápasů proti botovi, bot fallback při čekání |

**Hned po lednu: UGC.** Editor map ve hře na základě interního nástroje pro custom mapy, sdílení kódem, "mapa týdne", komunitní mapy v casual rotaci. Je to třetí díl ověření, ne bonus.

**Později:** Long game (online šachy), výroba jednotek a výzkum v městě, globální mapa a útoky na města (nejdřív fake), aliance.

## 5. Plán

| Období | PvP | City V2 | Komunita |
|---|---|---|---|
| listopad 2026 | design, presety národů, SGB služby (fronta, ELO, skóre, žebříčky), Quick game interně hratelné | V1 v MF staging: radnice, stavitelé, produkce, meta staty | oznámení na Discordu, sběr přání |
| prosinec 2026 | testy, validace tahů, odměny a achievementy, za RC flagem v Hexu | import do Hexu, napojení meta statů na jednotky a talenty | uzavřený test s nejaktivnějšími hráči |
| leden 2027 | k hráčům, postupně přes RC procenta | k hráčům | **reaktivační kampaň** "PvP a nové město": push, e-mail přes NOX ID, Discord, store update |
| únor 2027 | data, ladění lig a odměn | data, ladění ekonomiky | **UGC k hráčům**, feedback, hlasování o dalších módech |
| konec února 2027 | **první čtení gate** (PvP a City V2) | | |
| II až III 2027 | | | **rozhodnutí o novém Hexapolis 2** podle celku (PvP, City V2, UGC) |

Každá featura za vlastním RC flagem, zapínání po procentech, rollback bez buildu.

## 6. Gate Hexapolis 2 (první čtení konec února, rozhodnutí II až III 2027)

Rozhoduje **celek**: PvP, City V2 a UGC *(cílové hodnoty návrh, potvrdit s Jirkou)*:

| Otázka | Metrika | Cíl *(návrh)* |
|---|---|---|
| Hrají PvP? | podíl DAU v PvP, zápasy na hráče týdně | 25 %+, 5+ |
| Staví město? | % DAU v City, návraty do City za den | TBD |
| Drží je to? | D7 a D30 hráčů s PvP a City proti ostatním | +20 % relativně |
| Platí? | ARPDAU Hexu před a po, konverze na zrychlení a VIP | růst |
| Vrací se staří hráči? | reaktivace po kampani | sledovat |
| Tvoří a hrají mapy? | podíl hráčů, kteří vytvoří nebo zahrají komunitní mapu | sledovat |
| Kterou motivaci mají? | poměr Skill only a All-out-power | sledovat, určí směr Hexapolis 2 |

Když celek ukáže zájem a ochotu platit, připravit **design hex gameplaye nasazeného na MF metu** a podle něj založit nový projekt Hexapolis 2 (tematika podle CPI testů, cíl B v kapitole 07).

## 7. Co je potřeba rozhodnout

1. **Vlastníci** PvP a City V2 a kapacita na listopad a prosinec (běží live ops Q4).
2. **Rozsah lednového releasu:** obě featury naráz, nebo PvP první a City V2 o pár týdnů později *(návrh: naráz, kampaň stojí na obou)*.
3. **Prototyp PvP z května** (Codex 5.5): navázat, nebo začít znovu.
4. **Cílové hodnoty gate** potvrdit s Jirkou.
5. **OKR O5.2** (test multiplayeru do 30. 11.): posunout na leden podle tohoto plánu.
6. **NoxHub projekt Hex 2:** úkoly HexFortu uzavřít nebo přesunout do Hexapolisu (např. HEX-2-0249-72 Multiplayer patří teď k PvP v Hexu).
