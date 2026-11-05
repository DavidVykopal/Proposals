## Shrnutí
HexFort jako Hexapolis 2 rušíme, bez ověření je to příliš velké riziko. Práci vracíme do původního Hexapolisu a tam ověříme jako celek tři featury: PvP, City V2 a UGC. Všechny tři budou implementované do 11. 12. 2026 za RC flagy. PvP a City V2 dostanou hráči v lednu 2027, UGC v únoru 2027.

PvP má dva segmenty: Skill only se stejným setupem pro všechny (nejblíž Polytopii) a All-out-power, kde rozhoduje i meta síla a férovost drží 5 lig. Na start Quick game ve variantách Speed a Normal a žebříčky denní, týdenní a měsíční na SharedGameBackendu. Data rozhodnou v únoru až březnu 2027 o novém Hexapolis 2.

## Výhody
- **Nejlevnější ověření:** živá hra s komunitou a revenue cca $15k měsíčně, bez nového titulu a bez UA na start.
- **Plní nejčastější přání komunity** a bere Polytopii hlavní výhodu, kterou nás dnes přetahuje.
- **Dva segmenty, dvě motivace:** Skill only pro férový souboj, All-out-power pro hráče, kteří investovali do jednotek a talentů.
- **Smyčka s městem:** PvP dává suroviny do City V2, město dává sílu do All-out-power.
- **Bezpečné nasazení:** každá featura za vlastním RC flagem, zapínání po procentech, rollback bez buildu.

## Nevýhody
- Konec roku nese PvP, City V2, UGC i SGB vedle live ops Q4 a zimních eventů.
- Dva segmenty, dva sub-režimy a 5 lig rozdělují malou hráčskou základnu.
- O Hexapolis 2 se rozhodne nejdřív v únoru 2027, dosavadní práce na HexFortu se v současné podobě nedokončí.
- Server musí validovat tahy, ukládat replaye a řešit cheatery, což je nová provozní zátěž.
- UGC se oproti konceptu posunulo dopředu, do konce roku má být hotové místo až po lednu.

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| Malá base, Quick game potřebuje oba hráče naráz | vysoká | vysoká | onboarding proti botům, bot nebo ghost fallback při čekání, hra s přáteli, ligy sloučit, dokud nemají dost hráčů |
| Kapacita kodérů do 11. 12. nestačí, hlavně na UGC | vysoká | střední | volná kódová kapacita z konce roku, backend a logika přes agenty, rozhodnutí K4 v plánu sprintu |
| Pocit pay to win v All-out-power | střední | střední | Skill only jako férová alternativa bez koupitelné výhody, ligy podle síly |
| Cheateři v žebříčcích | střední | střední | validace akcí na serveru, replay, top 10 a achievementy jen z reálných zápasů |
| Nebalancované presety národů nebo jednotky | střední | nízká | hodnoty v remote configu odděleně od PvE, alarm nad 55 % win rate |
| Gate nemá potvrzené cílové hodnoty | střední | střední | potvrdit s Jirkou před prvním čtením na konci února |

## Co nám to přinese
- PvP (Skill only i All-out-power) a City V2 u hráčů v lednu 2027 s reaktivační kampaní "PvP a nové město".
- UGC v únoru 2027: editor map, sdílení kódem, mapa týdne, komunitní mapy v casual rotaci.
- První čtení gate na konci února 2027, cíle *(návrh)*: 25 %+ DAU zkusí PvP, 5+ zápasů týdně, D7 a D30 o 20 % relativně výš.
- Data o tom, jestli hráči platí za sílu (ARPDAU, útrata v All-out-power) a kterou motivaci mají.
- Rozhodnutí o novém Hexapolis 2 v únoru až březnu 2027 podle výsledku celku.

→ `KONCEPT_OBNOVA_HEXU.md`
