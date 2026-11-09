## Shrnutí
HexFort jako Hexapolis 2 rušíme, bez ověření je to příliš velké riziko. Práci vracíme do původního Hexapolisu a tam ověříme jako celek tři featury: PvP, City V2 a UGC. Všechny tři budou v testu a připravené do 11. 12. 2026 za RC flagy. PvP a City V2 dostanou hráči v lednu 2027. UGC je bonus, z velké části hotové, a může k hráčům dřív než v únoru.

PvP má dva segmenty: Skill only se stejným setupem pro všechny (nejblíž Polytopii) a All-out-power, kde rozhoduje i meta síla a férovost drží 5 lig. Na start Quick game ve variantách Speed a Normal a žebříčky denní, týdenní a měsíční na SharedGameBackendu. Hexapolis má cca 7 tis. aktivních hráčů, proto Speed a Normal sdílí jednu frontu a ligy se v párování slučují (rozhodnuto 6. 11.). SGB jde živě až po svátcích, takže lednové žebříčky stojí na jeho postupném náběhu. Data rozhodnou v únoru až březnu 2027 o novém Hexapolis 2.

## Výhody
- **Nejlevnější ověření:** živá hra s komunitou (cca 7 tis. aktivních hráčů) a revenue cca $15k měsíčně bez Play Passu, bez nového titulu a bez UA na start.
- **Plní nejčastější přání komunity** a bere Polytopii hlavní výhodu, kterou nás dnes přetahuje.
- **Dva segmenty, dvě motivace:** Skill only pro férový souboj, All-out-power pro hráče, kteří investovali do jednotek a talentů.
- **Smyčka s městem:** PvP dává suroviny do City V2, město dává sílu do All-out-power.
- **Monetizace PvP:** předplatné 4,99 a 9,99 USD (ranked bez limitu, ligy, turnaje, suroviny do City) a skiny jednotek, free tier drží likviditu *(návrh 9. 11.)*.
- **Bezpečné nasazení:** každá featura za vlastním RC flagem, zapínání po procentech, rollback bez buildu.

## Nevýhody
- Konec roku nese PvP, City V2, UGC i SGB vedle live ops Q4 a zimních eventů. Hex featury a SGB dělí Mirek, Kubík a David, Milan a Čoud drží hlavní live hry.
- Při cca 7 tis. aktivních hráčů bude v lednu 20 až 50 % zápasů proti botovi, i se dvěma frontami.
- O Hexapolis 2 se rozhodne nejdřív v únoru 2027, dosavadní práce na HexFortu se v současné podobě nedokončí.
- Server musí validovat tahy, ukládat replaye a řešit cheatery, což je nová provozní zátěž.
- Lednový release žebříčků závisí na SGB, které jde živě až po svátcích, vypnuté a postupně.

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| Malá base (cca 7 tis. aktivních), Quick game potřebuje oba hráče naráz | vysoká | vysoká | jedna fronta na segment, ligy sloučené v párování (rozhodnuto 6. 11.), fallback na bota po 30 s, rychlé zapnutí pro 90 %+ hráčů, generované profily botů |
| SGB nenaběhne v lednu včas | střední | vysoká | SGB do konce roku otestované na interním buildu MF; fallback PvP nejdřív bez žebříčků *(návrh)* |
| Kapacita kodérů do 11. 12. nestačí | střední | střední | Mirek, Kubík a David na Hex featurách a SGB, UGC z velké části hotové, backend a logika přes agenty |
| Pocit pay to win v All-out-power | střední | střední | Skill only jako férová alternativa bez koupitelné výhody, ligy podle síly |
| Cheateři v žebříčcích | střední | střední | validace akcí na serveru, replay, top 10 a achievementy jen z reálných zápasů |
| Nebalancované presety národů nebo jednotky | střední | nízká | hodnoty v remote configu odděleně od PvE, alarm nad 55 % win rate |
| Předplatné odrazí neplatící a vyprázdní fronty | střední | vysoká | zdarma Quick game a 3 ranked zápasy denně, ligy Bronz a Stříbro zdarma, placené jsou jen limity a turnaje |
| Gate nemá potvrzené cílové hodnoty | střední | střední | potvrdit s Jirkou před prvním čtením na konci února |

## Co nám to přinese
- PvP (Skill only i All-out-power) a City V2 u hráčů v lednu 2027 s reaktivační kampaní "PvP a nové město".
- UGC nejpozději v únoru 2027, klidně dřív: editor map, sdílení kódem, mapa týdne, komunitní mapy v casual rotaci.
- První čtení gate na konci února 2027, cíle *(návrh)*: 25 %+ DAU v PvP (cca 1 750 hráčů), 5+ zápasů týdně, 50 %+ zápasů s reálným soupeřem v lednu a 65 %+ v únoru, D7 a D30 o 20 % relativně výš.
- Výnos PvP odhadem 0,75 až 3,3 tis. USD měsíčně (základ 1,8 tis.), s City V2 v základu cca +4,6 tis. USD měsíčně, tedy +56 % dnešního IAP Hexu *(odhad, `BALANC_HEX_PVP.md` kap. 10)*.
- Data o tom, jestli hráči platí za sílu (ARPDAU bez Play Passu, útrata v All-out-power) a kterou motivaci mají.
- Rozhodnutí o novém Hexapolis 2 v únoru až březnu 2027 podle výsledku celku.

→ `KONCEPT_OBNOVA_HEXU.md`
