# Obnova Hexapolisu: PvP + City V2

> **Stav:** koncept, 4. 11. 2026, podle Davidova zadání. Věci označené *(návrh)* jsou návrh autora dokumentu.
> **Rozhodnutí 4. 11. 2026:** HexFort jako projekt Hexapolis 2 se ruší, práce se vrací do původního Hexapolisu. Nový Hexapolis 2 vznikne až po ověření celku, jako hex gameplay nasazený na MF metu.
> **Doplněno 5. 11. 2026:** PvP, City V2 i UGC budou implementované do 11. 12. 2026 za RC flagy; hráči dostanou PvP a City V2 v lednu 2027, UGC v únoru 2027. SharedGameBackend jde nejdřív do Mecha Fortress (6. 11. upřesněno: do konce roku jen interní build MF, živě po svátcích). Release freeze 14. až 18. 12. (GameJam). Čísla: `BALANC_HEX_PVP.md`, `BALANC_CITY_V2.md`.
> **Rozhodnuto 6. 11. 2026 (David):** Hexapolis má **cca 7 tis. aktivních hráčů**, příjmy z Play Passu se do revenue a gate nepočítají. PvP, City V2 i UGC v testu a připravené do 11. 12.; PvP a City V2 k hráčům v lednu, UGC (bonus, z velké části hotové) může k hráčům dřív než v únoru. SGB se do konce roku vyvine a otestuje na interním buildu MF, živě jde až po svátcích, vypnuté a s postupným zapínáním; žebříčky PvP na něm stojí. City V2 nahradí dnešní budovy na mapě MF s refundem investic (`DESIGN_CITY_V2.md`). Hex featury, SGB a nové věci dělí Mirek, Kubík (Jakub H.) a David; Milan a Čoud drží hlavní live hry.
> **Detaily:** `DESIGN_HEX_PVP.md` (PvP), `DESIGN_CITY_V2.md` (město). **Patří k:** `STRATEGIE_PRODUKCE.md`, větev 2.
> **Pro AI agenty:** tento soubor drží celkovou myšlenku a vazby. Pravidla jednotlivých featur jsou v detailních dokumentech; když se liší, platí detailní dokument.

## 1. Shrnutí

- **HexFort (dosavadní Hexapolis 2) rušíme**, bez ověření je to příliš velké riziko. Práce se vrací do **původního Hexapolisu**.
- V Hexu ověříme tři featury jako celek: **PvP, City V2 (mapa) a UGC**. Všechny tři budou v testu a připravené do 11. 12. 2026 za RC flagy. PvP a City V2 jdou k hráčům v lednu 2027, UGC může dřív než v únoru 2027. Testujeme **jednoduše, přímo v původní hře**, na base cca 7 tis. aktivních hráčů.
- **PvP** má dva segmenty: **Skill only** (stejný setup pro všechny, nejblíž Polytopii) a **All-out-power** (rozhoduje i meta síla, 5 lig). Na start Quick game ve variantách Speed a Normal, žebříčky denní, týdenní a měsíční s odměnami a achievementy.
- **City V2** je co nejbližší klon Clash of Clans a Rise of Kingdoms: v první verzi stavění, sběr surovin a upgrady. **Budovy zvyšují meta staty.**
- **Kolik to přinese (odhad 9. 11.):** City V2 v Hexu 1,3 až 9,5 tis. USD měsíčně (základ 2,8 tis.), plné město za gemy 10 až 100 tis. USD od Radnice 20. PvP předplatné a skiny 0,75 až 3,3 tis. USD měsíčně (základ 1,8 tis.). Základ obou je cca **+4,6 tis. USD měsíčně, +56 % dnešního IAP Hexu** (8,2 tis.), rok 2027 cca 50 tis. USD (`BALANC_CITY_V2.md` kap. 8.3, `BALANC_HEX_PVP.md` kap. 10).
- Featury do sebe zapadají: **PvP dává suroviny do města, město dává sílu do All-out-power PvP.** Skill only zůstává čistý souboj.
- Cíl: **oživit Hexapolis** (komunita, návrat hráčů, revenue) a z dat rozhodnout o **novém Hexapolis 2**: když celek funguje, udělá se **design hex gameplaye nasazeného na MF metu** a podle něj nový projekt.

## 2. Proč obnova a ne rovnou nová hra

- **Komunita chce právě tohle:** hrát proti sobě a stavět. PvP je nejčastější přání a hlavní důvod, proč nás přetahuje Polytopia.
- **Nejlevnější ověření:** živá hra s komunitou (cca 7 tis. aktivních hráčů) a revenue (dnes cca $15k měsíčně, bez Play Passu), žádný nový titul, žádný UA na start.
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
| Žebříčky a odměny | denní, týdenní, měsíční v obou segmentech, přes SharedGameBackend (předpoklad: SGB v lednu postupně naběhne, jinak PvP nejdřív bez žebříčků *(návrh)*) |
| City V2 verze 1 | radnice, stavitelé, produkční budovy a sběr, sklad, budovy s meta staty, dekorace, questy |
| Onboarding | prvních několik PvP zápasů proti botovi, bot fallback při čekání, generované profily botů (Rozhodnuto 6. 11.) |
| Fronty | jedna fronta na segment, Speed a Normal i ligy sloučené v párování (Rozhodnuto 6. 11.) |

**UGC, únor 2027 nebo dřív** (v testu a připravené za RC flagem už do 11. 12.). Editor map ve hře na základě interního nástroje pro custom mapy, sdílení kódem, "mapa týdne", komunitní mapy v casual rotaci. Je to bonus a třetí díl ověření; je z velké části hotové, takže **může k hráčům dřív než v únoru** (Rozhodnuto 6. 11.).

**Později:** Long game (online šachy), výroba jednotek a výzkum v městě, globální mapa a útoky na města (nejdřív fake), aliance.

## 5. Plán

| Období | PvP | City V2 | UGC | Komunita |
|---|---|---|---|---|
| listopad 2026 | design, presety národů, SGB služby (fronta, ELO, skóre, žebříčky), Quick game interně hratelné | V1 v MF staging: radnice, stavitelé, produkce, meta staty | editor map na interním nástroji, úložiště přes SGB (CODE-8) | oznámení na Discordu, sběr přání |
| prosinec 2026 | do 11. 12.: v testu a připravené, validace tahů, odměny a achievementy, za RC flagem v Hexu; SGB do konce roku na interním buildu MF | do 11. 12.: import do Hexu, napojení meta statů na jednotky a talenty | do 11. 12. v testu a připravené za RC flagem | release freeze 14. až 18. 12. (GameJam), pak uzavřený test s nejaktivnějšími hráči |
| leden 2027 | SGB živě po svátcích, postupně; PvP k hráčům přes RC procenta, rychle na 90 %+ *(návrh, kvůli likviditě)* | k hráčům | může k hráčům dřív než v únoru | **reaktivační kampaň** "PvP a nové město": push, e-mail přes NOX ID, Discord, store update |
| únor 2027 | data, ladění lig a odměn | data, ladění ekonomiky | k hráčům nejpozději teď | feedback, hlasování o dalších módech |
| konec února 2027 | **první čtení gate** (PvP a City V2) | | | |
| II až III 2027 | | | | **rozhodnutí o novém Hexapolis 2** podle celku (PvP, City V2, UGC) |

Každá featura za vlastním RC flagem, zapínání po procentech, rollback bez buildu. Kapacita: Hex featury a SGB dělí Mirek, Kubík (Jakub H.) a David, Milan a Čoud drží hlavní live hry (6. 11.).

## 6. Gate Hexapolis 2 (první čtení konec února, rozhodnutí II až III 2027)

Rozhoduje **celek**: PvP, City V2 a UGC *(cílové hodnoty návrh, potvrdit s Jirkou)*. Base cca 7 tis. aktivních hráčů, revenue a placení bez Play Passu (Rozhodnuto 6. 11.):

| Otázka | Metrika | Cíl *(návrh)* |
|---|---|---|
| Hrají PvP? | podíl DAU v PvP, zápasy na hráče týdně | 25 %+ (cca 1 750 PvP DAU), 5+ |
| Funguje párování? | podíl zápasů s reálným soupeřem | 50 %+ v lednu, 65 %+ v únoru *(návrh, sníženo 6. 11. z 60 % / 80 %)* |
| Staví město? | % DAU v City, návraty do City za den | TBD |
| Drží je to? | D7 a D30 hráčů s PvP a City proti ostatním | +20 % relativně |
| Platí? | ARPDAU Hexu před a po (iOS a Android mimo Play Pass), konverze na zrychlení, City VIP a PvP předplatné | IAP +4,6 tis. USD měsíčně (+56 %) v základu, minimum +2 tis. *(návrh 9. 11.)* |
| Vrací se staří hráči? | reaktivace po kampani | sledovat |
| Tvoří a hrají mapy? | podíl hráčů, kteří vytvoří nebo zahrají komunitní mapu | sledovat |
| Kterou motivaci mají? | poměr Skill only a All-out-power | sledovat, určí směr Hexapolis 2 |

Když celek ukáže zájem a ochotu platit, připravit **design hex gameplaye nasazeného na MF metu** a podle něj založit nový projekt Hexapolis 2 (tematika podle CPI testů, cíl B v kapitole 07).

## 7. Slabá místa a otevřené otázky

| Námitka | Proč může platit | Odpověď nebo co s tím |
|---|---|---|
| Hex nemá dost hráčů na živé PvP | **Base je cca 7 tis. aktivních hráčů (6. 11.).** Při 25 % DAU v PvP je to cca 1 750 PvP DAU: 12 front dá jen 21 % reálných zápasů, 2 fronty 68 % (fallback 20 s) nebo 80 % (fallback 30 s). Původní cíl 60 % do konce ledna potřebuje aspoň cca 1 350 PvP DAU (19 % DAU) a 80 % cca 2 650 (38 %). Během postupného zapínání v lednu je podíl nižší (při RC 50 % cca 47 až 59 %). Simulace lig počítala s 10 000 hráči All-out-power, reálně čekáme 1 000 až 2 000 týdně aktivních. | **Rozhodnuto 6. 11.:** 2 fronty (segmenty), Speed a Normal v jedné frontě, ligy sloučené v párování. *(Návrh)*: fallback 30 s, rychlý RC náběh na 90 %+, holdout max 10 %, cíl 50 %+ reálných v lednu a 65 %+ v únoru, žebříčky Diamant a Mistr při launchi se Zlatem (`BALANC_HEX_PVP.md`, kap. 5, 6 a 13). Když podíl reálných zápasů zůstane pod 50 %, přednost dostane async Long game. |
| Synchronní zápas nesedí na mobilní civilizaci | Normal trvá 15 až 25 min a oba hráči musí být u telefonu. Verze v1 designu (1. 11.) navrhovala jako MVP async 1v1, ten formát likviditu nepotřebuje. | Speed nechat jako hlavní režim, sledovat podíl vzdání a AFK (cíl pod 10 %). Pokud Normal nebude hraný, nahradit ho dřív Long game. |
| Play Pass zkresluje monetizační test | Hexapolis je v Google Play Passu: předplatitelé gemy nekupují a passy i nabídky mají zdarma. ARPDAU "před a po" míchá platící a Play Pass hráče, takže "platí za sílu" nejde z celé base vyčíst. | **Rozhodnuto 6. 11.:** příjmy z Play Passu se do revenue, baselines ani gate nepočítají. Gate o placení hodnotit jen na iOS a Androidu mimo Play Pass; Play Pass hráči se počítají jen do likvidity PvP a do zapojení. Ověřit, že baseline cca $15k měsíčně je bez Play Passu. |
| Gate se nedá vyhodnotit čistě | Lednová reaktivační kampaň a store update zvednou čísla bez ohledu na featury. UGC jde k hráčům nejpozději v únoru, do prvního čtení na konci února má málo dat. Cíle pro City a platby jsou "TBD" a "růst". | Holdout skupina přes RC procenta (část hráčů bez featur) po celé období, u PvP max 10 % kvůli likviditě. Čísla a kill kritérium schválit před lednem. UGC pustit dřív než v únoru, jakmile je připravené (Rozhodnuto 6. 11.), a hodnotit až při rozhodnutí II až III. |
| Původní Hex nepredikuje Hexapolis 2 | Testujeme starou base s reaktivací, ne nové hráče z UA. Hexapolis 2 má být hex gameplay na MF metě, kterou v Hexu netestujeme (testujeme City V2). | V gate oddělit, co se přenese (zájem o PvP a město, poměr segmentů) od toho, co ne (CPI, retence nových hráčů). Druhý vstup do rozhodnutí je CPI test cíle B. |
| Bonusy z města rozbijí kampaň a stávající hráče | City V2 dává na maximu verze 1 ×1,44 efektivní síly (`BALANC_CITY_V2.md`, kap. 1) a platí i v PvE. Kampaň Hexu zlehčí a dnešní nákupy síly ztratí hodnotu. | Rozhodnout, jestli bonusy platí v PvE kampani Hexu, nebo jen v All-out-power. Když ano, nižší strop v PvE přes RC a sledovat win rate kampaně. |
| Do 11. 12. je to moc práce naráz | Tři featury plus SGB za pět týdnů, s release freeze hned potom. City V2 potřebuje art budov v tématu Hexu a grafika je vytížená. Lednový release PvP navíc stojí na SGB, které jde živě až po svátcích. | **Rozhodnuto 6. 11.:** SGB do konce roku jen na interním buildu MF, živě po svátcích s postupným zapínáním; Hex featury a SGB dělí Mirek, Kubík a David, Milan a Čoud drží live hry. UGC je z velké části hotové. Pořadí priorit PvP, City V2, UGC. City V2 v Hexu s reuse nebo placeholder artem. Co nestihne 11. 12., jde za vypnutý flag. Fallback, když SGB v lednu nenaběhne: PvP bez žebříčků *(návrh)*. |

**Potřebuje odpověď:**
- Jaký nejnižší podíl reálných PvP zápasů v lednu ještě přijmeme, než přepneme důraz na async Long game? *(Návrh: 50 %.)* (DAU cca 7 tis. a Play Pass mimo revenue: Rozhodnuto 6. 11.)
- Pokud SGB v lednu nenaběhne včas: PvP bez žebříčků, nebo posunout?
- Platí bonusy z City V2 i v PvE kampani Hexu?
- Kill kritérium: při jakých číslech obnovu ukončíme a Hexapolis 2 nezaložíme?
- Pokud se do 11. 12. nestihnou všechny tři featury, co má přednost?

## 8. Co je potřeba rozhodnout

1. ~~**Vlastníci** PvP a City V2~~ **Rozhodnuto 6. 11.:** PvP Mirek, City V2 Kubík (Jakub H.), UGC David; základ SGB David, integrace SGB do her všichni. Milan a Čoud drží live hry.
2. **Rozsah lednového releasu** je rozhodnutý (PvP a City V2 v lednu, UGC může dřív než v únoru). Zbývá: zapnout PvP a City V2 ve stejný den, nebo s odstupem pár dní *(návrh: naráz, kampaň stojí na obou)*.
3. **Prototyp PvP z května** (Codex 5.5): navázat, nebo začít znovu.
4. **Cílové hodnoty gate** potvrdit s Jirkou.
5. **OKR O5.2** (test multiplayeru do 30. 11.): posunout podle tohoto plánu (implementace do 11. 12. za RC flagem, hráči v lednu).
6. **NoxHub projekt Hex 2:** úkoly HexFortu uzavřít nebo přesunout do Hexapolisu (např. HEX-2-0249-72 Multiplayer patří teď k PvP v Hexu).
