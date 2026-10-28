# Fix s variabilní složkou · návrh pro celou firmu · 29. 10. 2026

> HTML render: `priprava-2026-10-29-odmenovani.html`
>
> Podklad k bloku B porady 29. 10. (úkol U-22-04, David). Na typových pozicích, bez jmen.
> Čísla: NoxHub, compensation records 1–10/2026 (skutečně vyplacená odměna za práci, bez coworkingu),
> délka ve firmě z hubu (datum nástupu, tenure achievementy), role ze stránek segmentů ve Wiki,
> trh z ISPV 2025 (MPSV) a ČSÚ. Přepočet: `model_odmenovani_2027.py`. Finanční dopad doplní Martin B. (U-22-05).

---

## 1. Čtyři věty

- **Jedna logika, pásma podle pozice:** tým má fix podle hodnoty role a k němu bonus i malus. Exekutiva má fix a podíl na zisku, bonusů podle KPI se vzdává. Podíl z dealů mají všichni. Foundeři a CEO mají návrh podle dneška, schvaluje ho jejich rada tří.
- **Nikdo si nepohorší.** Fix nikoho nebude nižší než dnešní průměrně vyplacená odměna.
- **Narovnává se, kdo nese víc, než dostává.** Víc rolí, vedení projektu nebo lidí, roky ve firmě a historie (achievementy) se propíšou do fixu.
- **Strop základu 150 tis. Kč** pro tým i exekutivu. Variabilní složka a podíly se do něj nepočítají. Strop je zároveň měrný bod pro všechny ostatní základy.

## 2. Kde stojíme proti trhu

Tržní data pro česká herní studia neexistují, srovnáváme s celým trhem ČR. Cíl: **lépe než průměrný člověk mimo tech, kolem mediánu tech trhu, vědomě pod korporáty a bankami.**

Hrubá měsíční mzda zaměstnanců v ČR, rok 2025, tis. Kč (ISPV, mzdová sféra). Pro rok 2026 přičtěte cca 7 %. P10 a P90 jsou decily, P25 a P75 kvartily.

| Srovnání | P10 | P25 | Medián | P75 | P90 | Naše hodnota role |
|---|---|---|---|---|---|---|
| Všichni zaměstnanci ČR | 25 | 33 | 43 | 59 | 85 | |
| Vývojáři softwaru (2512) | 53 | 72 | 101 | 142 | 185 | programátor 80 až 98 |
| Testeři softwaru (2519) | 46 | 59 | 83 | 117 | 167 | QA lead s vývojem a DevOps 78 |
| Specialisté marketingu (2431) | 43 | 52 | 70 | 96 | 132 | UA manager 67, publishing 63 až 78 |
| Grafici v multimédiích (2166) | 41 | 48 | 58 | 77 | 104 | grafik 42 (junior) až 65 (s ASO) |
| Technici AV záznamu (3521) | 31 | 43 | 50 | 57 | 67 | video a motion 54 |
| Ředitelé ICT (1330) | 77 | 102 | 148 | 206 | 291 | strop základu 150 |
| Ředitelé obchodu a marketingu (1221) | 47 | 68 | 103 | 163 | 239 | vlastník segmentu 117 až 133 |

- **Proti lidem mimo tech:** průměrná mzda v ČR je ve 2. čtvrtletí 2026 cca 52 tis., v Jihomoravském kraji 50,6 tis. (ČSÚ). Proto pravidlo: **žádný plný základ role pod 52 tis.** Výjimkou je jen junior (80 % základu).
- **Proti tech trhu:** senior programátor u nás 80 až 98 tis. je mezi dolním kvartilem a mediánem celé ČR. Inzertní mediány pro seniory v Brně jsou 71 až 74 tis. (Glassdoor, Indeed), takže v Brně jsme nad nimi.
- **Korporáty a banky** platí horní kvartil a víc (senior vývojář 140 tis. a výš). Tam nesoutěžíme. Nabízíme vlastní projekty, menší firmu, podíl na výsledku a stabilitu odměny.
- **Faktura proti hrubé mzdě:** naše čísla jsou fakturace, trh je hrubá mzda. Srovnání 1 : 1 je vůči nám přísné. Na paušální dani zůstane z faktury 80 tis. zhruba stejně čistého jako zaměstnanci z hrubé mzdy cca 90 tis. Kontraktor ale nemá placenou dovolenou ani nemocenskou. Firmu stojí zaměstnanec s hrubou 101 tis. včetně odvodů cca 135 tis.

## 3. Dekret: strop základu 150 tis. Kč

Návrh nového dekretu do registru Delegační dekrety:

- **Základ (fix) nikoho v týmu ani v exekutivě nepřesáhne 150 tis. Kč měsíčně.** Variabilní složka a podíly na zisku se do stropu nepočítají.
- **Foundeři a CEO** (sám je founder) pod strop nespadají, svou odměnu schvaluje rada tří.
- Pojmenování „strop základu“ drží odstup od rozhodné částky 150 tis. Kč z R-22-12, jde o jinou věc.
- **Strop je měrný bod.** Základ každé role se vede jako procento stropu (tabulka v kap. 4). Když se strop při roční evaluaci posune, víme, o kolik se mají posunout základy.
- **Nikdo pod exekutivou nemá fix ani s plným bonusem vyšší než nejnižší fix exekutivy.** V návrhu je to nejvýš 108 proti 117 tis.
- **Strop, základy rolí i fix každého se hodnotí jednou ročně** (navazuje na R-22-09). Během roku se mění jen odměny a bonusy. Výjimky: příplatek při změně odpovědnosti a druhý krok narovnání 1. 7. 2027.
- Strop odpovídá mediánu ředitelů ICT v ČR (148 tis., ISPV 2025).

## 4. Jak vznikne fix: hodnota role

| Krok | Co | Hodnoty v návrhu |
|---|---|---|
| 1 | **Základ role**, u víc rolí vážený průměr podle procent v kartě | programátor 80 · UA manager 62 · game designer 60 · DevOps a IT 60 · publishing a LiveOps 58 · grafik MKT 56 · video a motion 52 · grafik DEV 52 · QA 52 (tis. Kč) |
| 2 | **Úroveň** | senior 100 % · medior 90 % · junior 80 % |
| 3 | **Roky ve firmě**, jen na základ | +2 % za každý dokončený rok, strop +20 % (10 let). Bere se z data nástupu v hubu |
| 4 | **Aktivní příplatky** za odpovědnost navíc | project lead +12, každý další aktivní projekt +6 · Publishing a LiveOps lead +10 · odborná autorita +10 · QA lead +8 · role pro jiný segment +8 · druhá odborná role (např. správa ASO) +4 · zástup vlastníka nebo za interní nástroj (NoxHub) +5 · správa kanceláří +5 · zástup v klíčové roli +5 · mentor +2 za člověka (nejvýš 3). Dohromady nejvýš 40 % základu |
| 5 | **Pasivní složka za historii** (achievementy v hubu, trvale) | ukončené vedení projektu nebo týmu (aspoň 6 měsíců) +2, nejvýš 2× · přednáška nebo reprezentace firmy venku +1, nejvýš 3× · uspořádaný event +1, nejvýš 3× · dokončený mentoring +0,5 za člověka, nejvýš 4×. Dohromady nejvýš 8 tis. |

- **Achievementy jako jediný zdroj pravdy.** Hub už dnes počítá roky ve firmě (tenure žebříček) a má odznaky `speaker` a `company_event`. Doplníme odznaky „vedl projekt“, „vedl tým“ a „mentor“. Kdo odznak dostane, má pasivní složku, a je vidět, za co.
- **Individuální dohoda nad hodnotou role** je možná jen výjimečně, když jde o udržení klíčového člověka. Vede se jako samostatný řádek, aby byla vidět, a při roční evaluaci se k hodnotě role dorovnává.
- **Dnešek se počítá ze skutečného příjmu:** hodiny × sazba a pravidelné měsíční příplatky (dofakturace), bez coworkingu a bez proplácených nákladů.
- **Fix kryje práci, ne hodiny.** Přesčasy se schvalují předem (D05). Kdo dnes odpracuje přes 200 h, o peníze nepřijde (nikdo pod dnešek), ale fix dál neroste s hodinami.

### Základ role jako procento stropu

| Role | Základ | % stropu |
|---|---|---|
| Vlastník segmentu (společný základ) | 110 | 73 % |
| Programátor | 80 | 53 % |
| UA manager | 62 | 41 % |
| Game designer, DevOps a IT | 60 | 40 % |
| Publishing a LiveOps | 58 | 39 % |
| Grafik MKT | 56 | 37 % |
| Video a motion, grafik DEV, QA | 52 | 35 % |

## 5. Pásma a variabilní složka

| | **Jistota** | **Lead** | **Exekutiva** |
|---|---|---|---|
| Pro koho | vykonavatelské role | tým s vedením projektu, lidí nebo procesu | vlastníci segmentů |
| Fix | hodnota role, nikdy pod dnešek | hodnota role, nikdy pod dnešek | 110 + příplatky, jednorázově od 1. 1. |
| Bonus max | +10 % fixu | +15 % fixu | žádný |
| Malus max | −5 % fixu | −7,5 % fixu | žádný |
| Na plánu | fix + 5 % | fix + 7,5 % | fix |
| Hodnocení | polovina mentor, polovina splněné úkoly | polovina mentor, polovina splněné úkoly | výsledek firmy přes podíl na zisku |
| Podíl z dealů | ano | ano | ano |
| Výplata | po kvartálech | po kvartálech | fix měsíčně, podíl ze zisku pod čarou |
| Pool (prasátko) | ano | ano | ne |

### Vyhodnocení týmu (Jistota a Lead)

- **Polovina bonusu od mentora:** písemné hodnocení za kvartál ve třech stupních. Pod očekáváním 0, v očekávání polovina, nad očekáváním celá.
- **Polovina z dat:** podíl splněných úkolů z plánu sprintů v hubu za měsíce kvartálu. Pod 60 % nic, od 60 do 90 % poměrně, nad 90 % celá polovina. Podmínka: práce je v hubu u úkolu (dnes je 24 % hodin bez úkolu).
- **Plán** = v očekávání a cca 75 % splněných úkolů, tedy polovina bonusu.
- **Malus** jen když jsou obě poloviny na nule. **První kvartál 2027 bez malusu.**
- Variabilní složka je řádek rozpočtu segmentu a vyplácí se s výplatou po skončení kvartálu. Pool je zvlášť.

### Pool pro tým (prasátko)

- **Plní se měsíčně procentem ze zisku**, stejně jako si exekutiva bere podíl. Sazbu a práh dopočítá Martin B. (C1, C2).
- **Každý v hubu vidí**, kolik v prasátku je a kolik by mu z něj podle výpočtu náleželo.
- **Rozbití:** když se první stupeň stihne do pololetí (nebo dřív), prasátko se odemkne v pololetí. Jinak na konci roku. Vždycky jen z reálně vydělaných peněz (R-22-06).
- **Klíč:** podle ročního průměrného příjmu člověka včetně variabilní složky. Kdo měl lepší rok, dostane víc.
- Exekutiva a foundeři v poolu nejsou.

### Podíl z dealů (R-22-10), pro všechny včetně exekutivy

- **5 % ze zisku dealu tomu, kdo ho navrhl a přinesl, a 5 % majiteli dealu, který ho odexekuuje.** Zisk dealu = tržby po odečtení přímých nákladů na dodání.
- Když je navrhovatel i majitel jeden člověk, dostane obojí. Vyplácí se z reálně přijatých peněz za deal.
- **Úspora** se neodměňuje procentem (vede k šetření na špatných místech), ale jednorázovou částkou nebo přes variabilní složku.

### Exekutiva: fix + podíl na zisku

- **Exekutiva se vzdává bonusů podle KPI.** Má fix, podíl na zisku a jako všichni podíl z dealů. Podíl na zisku se počítá až ze zisku pod čarou, po poolu pro tým (návrh Martina B.). Bonusy týmu tak nic nesnižuje, zůstává jeden pool a nehrozí double dipping (R-22-06). Zjednoduší to i výpočet bonusů.
- **Společný základ 110 tis.** a k tomu malé příplatky, které odliší rozsah: +1 za každého člověka pod sebou (nejvýš 6), +0,1 za každé procento OPEX segmentu, role navíc (agenda celé exekutivy, finance a smlouvy celé firmy, práce pro jiný segment) a pasivní složka za historii stejně jako u týmu.
- Vychází to 117 až 133 tis. Bez pasivní složky je rozdíl mezi vlastníky do 9 tis., s ní do 16 tis.
- **Proč takový skok:** exekutiva je dnes nejvíc podhodnocená. Dva vlastníci segmentu mají dnes méně než nový fix seniorního programátora. Jde o první vyjednávání fixů vedení, proto je narovnání větší než u týmu.
- **Jednorázově a hlasováním:** fix exekutivy a foundrů se schválí do konce roku na schůzce celého vedení hlasováním a platí na celý rok 2027. Nikdo nevyjednává individuálně. Bez dvou kroků.

## 6. Rozpis po pozicích

Tis. Kč měsíčně, každý člověk ve firmě jako pozice bez jména. Minimum = fix s plným malusem, maximum = fix s plným bonusem, obojí bez poolu (prasátka). Exekutiva nemá bonus ani malus, jen fix a podíl na zisku. „Dnes“ je skutečně vyplacená průměrná odměna 1–10/2026 včetně pravidelných příplatků, bez coworkingu. Jmenovitě v důvěrném modelu.

**Z čeho je fix**

| Pozice | Základ role | Roky ve firmě | Aktivní příplatky | Pasivní (historie) | Fix 2027 |
|---|---|---|---|---|---|
| Senior programátor, 7 let, zástup, historie leadu | prog, senior: 80,0 | 7 → +11,2 | zástup B2B delivery a autority tech +5 | vedl projekt +2,0 | **98,2** |
| Senior programátor, nový, individuální dohoda | prog, senior: 80,0 | 0 → +0,0 | – | – | **85,0** (dohoda, role 80,0) |
| Game designer, lead 2 projektů, zástup vlastníka, mentor | GD 80 % + grafik DEV 20 %, senior: 58,4 | 2 → +2,3 | project lead (Sektor) +12, druhý aktivní projekt (Mecha) +6, zástup vlastníka za plán a kapacity +5, mentor 2 lidí +4 (strop 40 %: +24,3) | – | **85,0** |
| Game designer, lead 1 projektu, 7 let | GD 80 % + grafik DEV 20 %, senior: 58,4 | 7 → +8,2 | project lead (Red Command) +12 | – | **78,6** |
| Publishing a LiveOps lead, správa kanceláří | publishing, senior: 58,0 | 4 → +4,6 | Publishing a LiveOps lead +10, správa kanceláří (Operations) +5 | – | **77,6** |
| QA lead, programátor a DevOps, zástup NoxHub | QA 53 % + prog 27 % + DevOps 20 %, senior: 61,2 | 3 → +3,7 | QA lead +8, zástup za NoxHub +5 | – | **77,8** |
| Junior grafik | grafik DEV, junior: 41,6 | 0 → +0,0 | – | – | **41,6** |
| UA manager, 4 roky | UA, senior: 62,0 | 4 → +5,0 | – | – | **79,4** (garance 12,4) |
| Grafik MKT a správa ASO, 4 roky | grafik MKT, senior: 56,0 | 4 → +4,5 | správa celého ASO +4 | – | **64,5** |
| Video a motion, 2 roky | video, senior: 52,0 | 2 → +2,1 | – | – | **54,1** |
| Vlastník segmentu Produkce + agenda exekutivy | společný základ exekutivy 110 | 6 (bez vlivu) | lidé pod sebou 7 → +6,0, rozpočet 45 % OPEX → +4,5, consigliere: agenda exekutivy, plány a strategie +5 | vedl projekt +4,0, přednášky +3,0 | **132,5** |
| Vlastník segmentu Operations + finance firmy | společný základ exekutivy 110 | 9 (bez vlivu) | lidé pod sebou 1 → +1,0, rozpočet 24 % OPEX → +2,4, finance, rozpočet a smlouvy celé firmy +5 | vedl projekt +2,0 | **120,4** |
| Vlastník segmentu Marketing | společný základ exekutivy 110 | 5 (bez vlivu) | lidé pod sebou 3 → +3,0, rozpočet 20 % OPEX → +2,0, analytika pro Produkci (přechodně) +2 | – | **117,0** |
| Founder, autorita tech + programátor | návrh podle dnešní odměny, mimo strop, schvaluje rada tří | 13 | – | – | dnešek |
| Founder, autorita art + grafik | návrh podle dnešní odměny, mimo strop, schvaluje rada tří | 21 | – | – | dnešek |
| CEO, majitel | návrh podle dnešní odměny, mimo strop, schvaluje rada tří | 21 | – | – | dnešek |

**Kolik může vydělat**

| Pozice | Pásmo | Dnes | Fix 2027 | Minimum (plný malus) | Plán | Maximum (plný bonus) | Δ fixu |
|---|---|---|---|---|---|---|---|
| Senior programátor, 7 let, zástup, historie leadu | Jistota | 82,5 | **98,2** | 93,3 | 103,1 | 108,0 | +15,7 |
| Senior programátor, nový, individuální dohoda | Jistota | 71,4 | **85,0** | 80,8 | 89,3 | 93,5 | +13,6 |
| Game designer, lead 2 projektů, zástup vlastníka, mentor | Lead | 73,4 | **85,0** | 78,7 | 91,4 | 97,8 | +11,6 |
| Game designer, lead 1 projektu, 7 let | Lead | 49,1 | **78,6** | 72,7 | 84,5 | 90,4 | +29,5 |
| Publishing a LiveOps lead, správa kanceláří | Lead | 62,9 | **77,6** | 71,8 | 83,5 | 89,3 | +14,7 |
| QA lead, programátor a DevOps, zástup NoxHub | Lead | 45,3 | **77,8** | 72,0 | 83,7 | 89,5 | +32,5 |
| Junior grafik | Jistota | 36,8 | **41,6** | 39,5 | 43,7 | 45,8 | +4,8 |
| UA manager, 4 roky | Jistota | 79,4 | **79,4** | 75,4 | 83,4 | 87,3 | +0,0 |
| Grafik MKT a správa ASO, 4 roky | Jistota | 58,8 | **64,5** | 61,3 | 67,7 | 70,9 | +5,7 |
| Video a motion, 2 roky | Jistota | 42,8 | **54,1** | 51,4 | 56,8 | 59,5 | +11,3 |
| Vlastník segmentu Produkce + agenda exekutivy | fix + podíl na zisku | 105,5 | **132,5** | = fix | = fix | = fix | +27,0 |
| Vlastník segmentu Operations + finance firmy | fix + podíl na zisku | 77,7 | **120,4** | = fix | = fix | = fix | +42,7 |
| Vlastník segmentu Marketing | fix + podíl na zisku | 81,4 | **117,0** | = fix | = fix | = fix | +35,6 |
| Founder, autorita tech + programátor | rada tří | – | dnešek | – | – | – | 0 |
| Founder, autorita art + grafik | rada tří | – | dnešek | – | – | – | 0 |
| CEO, majitel | rada tří | – | dnešek | – | – | – | 0 |

## 7. Co to udělá ve firmě

- **Tým (10 lidí):** všem fix roste nebo zůstává, nikdo není pod dneškem. Největší narovnání mají dva lidé, kteří dlouho nesou roli navíc za sazbu z doby, kdy ji neměli (+30 a +33 tis., ve dvou krocích). Dalších pět dostane +11 až +16 tis., dva +5 až +6 tis. Jeden člověk má dnes víc, než je hodnota role, fix mu drží garance.
- **Malus** může v jednom kvartálu poslat odměnu pod dnešek (nejvýš −5 až −7,5 % fixu). Fix sám nikoho pod dnešek nepošle.
- **Exekutiva (3):** fix se sjednotí na společném základu 110 plus příplatky, bez bonusu a malusu.
- **Rozdíl mezi lidmi stejné role** dnes dělají sazby vyjednané v různé době. Po přechodu ho dělají jen úroveň, roky ve firmě, odpovědnosti, historie a výsledky.

## 8. Kolik to stojí: varianta A (rok 2027, mil. Kč)

Odměny za práci 13 lidí bez foundrů a CEO, bez poolu a bez podílů na zisku. Dnes 10,40 mil. Kč ročně. Finanční dopad a vazbu na scénáře doplní Martin B. (U-22-05).

| | Dnes | Bez bonusu | Plán | Vše splněno |
|---|---|---|---|---|
| Tým | 7,23 | 8,64 | 9,18 | 9,72 |
| Exekutiva | 3,18 | 4,44 | 4,44 | 4,44 |
| **Celkem** | **10,40** | **13,07** | **13,62** | **14,16** |
| Δ proti dnešku | | +2,67 | +3,21 | +3,76 |

- **Pevná část** (fixy) je v roce 2027 +2,7 mil. (tým +1,4, exekutiva +1,3), od 2028 s plným fixem po celý rok +2,9 mil.
- **Variabilní složka týmu** na plánu +0,5 mil., nejvýš +1,1 mil.
- **Proti zisku:** Martinovy scénáře Adj. EBITDA z 22. 10. jsou cca 5 až 10 mil. Kč ročně. Pevná část je tedy 27 až 53 % z nich, a to bez B2B pod provozními náklady (od července). Proto schválení vázat na U-22-05.
- Mírnější varianty B a C jsou v kap. 9. Rozpis v kap. 6 je pro variantu A.
- Narovnání týmu nad 10 tis. jde ve dvou krocích, pravidlo a důvody níže.

### Narovnání ve dvou krocích

Kdo má nový fix o víc než 10 tis. nad dneškem, dostane 1. 1. 2027 dnešek plus polovinu rozdílu (aspoň +10 tis.) a 1. 7. 2027 zbytek. Druhý krok potvrdí vlastník segmentu v červnu. Kdo roli, za kterou má příplatek, opravdu nenese, zůstává na prvním kroku a příplatek se přepočítá při roční evaluaci.

Proč:

- **Rozpočet:** v roce 2027 to ušetří cca 0,3 mil. Kč a náklad roste postupně, ne skokem v lednu.
- **Ověření role:** příplatek se platí za odpovědnost, kterou člověk nese. Půl roku ukáže, že ji opravdu nese, a druhý krok je pak zasloužený, ne slíbený.
- **Pojistka proti chybě v modelu:** role a procenta se zapisují poprvé. Když se ukáže chyba, opraví se před druhým krokem, ne zpětným snižováním.
- **Zlepšení hned:** každý, kdo se narovnává, cítí rozdíl od ledna, aspoň +10 tis. nebo polovinu.
- **Jen pro tým:** exekutiva a foundeři mají jednorázový skok od 1. 1. Fix schválí hlasováním celé vedení do konce roku a platí na celý rok, nikdo nevyjednává individuálně. Celá od 1. 1. platí i individuální dohoda.


### Kde hledat úsporu (ověří Martin B.)

- Konec placení hodin nad úvazek bez schválení a hodin bez úkolu (24 % hodin v srpnu).
- Duplicitní AI nástroje (cca 0,35 mil. Kč ročně).
- Coworking zdrojem není. Je to průtoková platba za kancelář: firma ji lidem proplácí a lidé z ní platí kancelář. Do odměny ani do fixu se nepočítá.

## 9. Tři varianty narovnání

**Preferujeme variantu A** a pokusíme se ji schválit: je nejdražší, ale splní závazek nejlepšího možného ohodnocení. B a C rozkládají rozdíl mezi dneškem a plným fixem rovnoměrně (dvě třetiny, třetina). Systém, pásma i pravidla jsou ve všech stejné, liší se jen, o kolik se fixy narovnají.

| Varianta | Jen fixy | Plán | Max | Δ plánu | Δ fixů 2027 | Δ fixů 2028 | Δ fixů / EBITDA |
|---|---|---|---|---|---|---|---|
| **A · plné narovnání (preferovaná)** | 13,07 | 13,62 | 14,16 | +3,21 | +2,67 | +2,94 | 27 až 53 % |
| B · dvě třetiny narovnání | 12,29 | 12,80 | 13,30 | +2,39 | +1,89 | +2,01 | 19 až 38 % |
| C · třetina narovnání | 11,49 | 11,96 | 12,43 | +1,56 | +1,08 | +1,09 | 11 až 22 % |
| Dnes | 10,40 | | | | | | |

Mil. Kč za rok 2027, 13 lidí bez foundrů a CEO, bez poolu a podílů na zisku. Jen fixy = nikdo nedostane bonus, max = všichni plný bonus, Δ proti dnešku. Poslední sloupec = přírůstek fixů jako podíl Adj. EBITDA ze scénářů Martina B. (5 až 10 mil. Kč).

- **Strop exekutivy** (nikdo v týmu ani s plným bonusem nad nejnižším fixem exekutivy): A (108,0 proti 117,0), B (102,3 proti 105,1), C (96,5 proti 91,9). Ve variantě C pravidlo neplatí, exekutiva by se musela narovnat víc než tým.
- **Ve všech variantách platí, že si nikdo nepohorší.** Fix každého je aspoň dnešek, liší se jen, o kolik se narovná. Individuální dohoda (85 tis.) je ve všech stejná.
- **Individuální dohoda v B a C:** pevných 85 tis. by předběhlo lídry, kteří se narovnávají jen částečně (lead dvou projektů B 81,2, C 77,3). Když se skončí u B nebo C, navrhuji dohodu snížit stejným poměrem (B 80,5, C 75,9) a zbytek nabídnout přes bonus.
- **Dvě pásma, nebo jedno:** dát lídry do Jistoty ušetří ve variantě A cca 0,10 mil. ročně. Doporučení zůstává u dvou pásem.

**Fix 2027 po lidech podle varianty** (tis. Kč měsíčně, v závorce rozdíl proti dnešku)

| Pozice | Dnes | A · plné | B · dvě třetiny | C · třetina |
|---|---|---|---|---|
| Senior programátor, 7 let, zástup, historie leadu | 82,5 | **98,2 (+15,7)** | 93,0 (+10,5) | 87,7 (+5,2) |
| Senior programátor, nový, individuální dohoda | 71,4 | **85,0 (+13,6)** | 85,0 (+13,6) | 85,0 (+13,6) |
| Game designer, lead 2 projektů, zástup vlastníka, mentor | 73,4 | **85,0 (+11,6)** | 81,2 (+7,8) | 77,3 (+3,9) |
| Game designer, lead 1 projektu, 7 let | 49,1 | **78,6 (+29,5)** | 68,8 (+19,7) | 58,9 (+9,8) |
| Publishing a LiveOps lead, správa kanceláří | 62,9 | **77,6 (+14,7)** | 72,7 (+9,8) | 67,8 (+4,9) |
| QA lead, programátor a DevOps, zástup NoxHub | 45,3 | **77,8 (+32,5)** | 67,0 (+21,7) | 56,1 (+10,8) |
| Junior grafik | 36,8 | **41,6 (+4,8)** | 40,0 (+3,2) | 38,4 (+1,6) |
| UA manager, 4 roky | 79,4 | **79,4 (+0,0)** | 79,4 (+0,0) | 79,4 (+0,0) |
| Grafik MKT a správa ASO, 4 roky | 58,8 | **64,5 (+5,7)** | 62,6 (+3,8) | 60,7 (+1,9) |
| Video a motion, 2 roky | 42,8 | **54,1 (+11,3)** | 50,3 (+7,5) | 46,6 (+3,8) |
| Vlastník segmentu Produkce + agenda exekutivy | 105,5 | **132,5 (+27,0)** | 123,5 (+18,0) | 114,5 (+9,0) |
| Vlastník segmentu Operations + finance firmy | 77,7 | **120,4 (+42,7)** | 106,2 (+28,5) | 91,9 (+14,2) |
| Vlastník segmentu Marketing | 81,4 | **117,0 (+35,6)** | 105,1 (+23,7) | 93,3 (+11,9) |

## 10. Foundeři, CEO a podíly na zisku

- **Foundeři a CEO** jsou mimo systém rolí i mimo strop základu. V rozpisu mají návrh podle toho, co dnes dostávají. Schvaluje ho rada tří a na další rok si mohou dát víc.
- **Podíl na zisku** má exekutiva, CEO a dva foundeři. Počítá se ze zisku pod čarou, po poolu pro tým. Nikdo z nich není v poolu.

## 11. Přechod

| Kdy | Co |
|---|---|
| do 15. 11. | potvrdit role a procenta každého (karty z 5. 11.), mentory, doplnit odznaky historie v hubu |
| do 30. 11. | přepočet modelu, finanční dopad Martina B. |
| do 15. 12. | hlasování celého vedení o fixech exekutivy a návrhu foundrů na rok 2027 |
| 1. až 15. 12. | individuální rozhovor s každým v týmu: hodnota role, fix, pásmo. Na all-hands princip spolu s odměnou 2026 a prasátkem |
| 1. 1. 2027 | fix místo hodinové sazby, exekutiva celý fix, tým první krok narovnání, plán sprintů a mentoři v hubu, prasátko běží |
| Q1 2027 | první kvartál bez malusu |
| 1. 7. 2027 | druhý krok narovnání týmu, případné rozbití prasátka za pololetí |
| prosinec 2027 | roční evaluace stropu, základů rolí a fixů |

## 12. K rozhodnutí

Číslování podle hlavní přípravy porady (blok B).

| # | Otázka | Návrh |
|---|---|---|
| B1 | Základ systému | hodnota role, dvě pásma pro tým, exekutiva fix + podíl. Narovnání podle varianty A (preferovaná), záloha B |
| B2 | Kdo má bezpečnou a kdo dynamickou složku | vykonavatelé Jistota, lídři Lead. Exekutiva se bonusů vzdává, riziko nese přes podíl na zisku. Foundeři mimo |
| B3 | Rozpětí a kolik to stojí | Jistota +10 / −5 %, Lead +15 / −7,5 % fixu. 2027 na plánu: A 13,62, B 12,80, C 11,96 mil. (dnes 10,40), dopad do scénářů doplní Martin B. |
| B4 | Cíle a KPI na Q1 2027 | mentoři s vlastníkem segmentu, cíle a plán sprintů v hubu do 15. 1. spolu s OKR (R-22-14). Q1 bez malusu |
| B5 | Řádek rozpočtu 2027 | A +2,7 / B +1,9 / C +1,1 mil. fixy do pevných částí segmentů (R-22-11), variabilní složka týmu +0,5 až 1,1 mil. jako řádek segmentu. Úspory: hodiny bez úkolu, AI nástroje, kancelář ne |
| B6 | Postup zavedení | David (model, rozhovory v Produkci, odznaky v hubu), Martin B. (finance, smlouvy), vlastníci (rozhovory ve svém segmentu). Exekutiva a foundeři hlasováním do 15. 12. |
| B7 | Dekret o stropu základu | základ nejvýš 150 tis. pro tým a exekutivu, bez variabilní složky a podílů, foundeři mimo, roční evaluace |
| B8 | Achievementy | pasivní složka za historii podle odznaků v hubu, nejvýš 8 tis. |
| B9 | Podíl z dealů | 5 % ze zisku dealu navrhovateli + 5 % majiteli nebo executorovi, pro všechny včetně exekutivy |

Zdroje: ISPV 2025, mzdová sféra ČR (ispv.cz, MPSV); ČSÚ, průměrná mzda v Jihomoravském kraji ve 2. čtvrtletí 2026 (csu.gov.cz); Glassdoor a Indeed, Senior software developer Brno 2026; NoxHub, compensation records a bankovní pohyby 1–10/2026.
