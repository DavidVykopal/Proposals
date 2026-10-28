# Fix s variabilní složkou · návrh pro celou firmu · 29. 10. 2026

> HTML render: `priprava-2026-10-29-odmenovani.html`
>
> Podklad k bloku B porady 29. 10. (úkol U-22-04, David). Na typových pozicích, bez jmen.
> Čísla: NoxHub, compensation records 1–10/2026 (skutečně vyplacená odměna za práci, bez coworkingu),
> délka ve firmě z hubu (datum nástupu, tenure achievementy), role ze stránek segmentů ve Wiki,
> trh z ISPV 2025 (MPSV) a ČSÚ. Přepočet: `model_odmenovani_2027.py`. Finanční dopad doplní Martin B. (U-22-05).

---

## 1. Čtyři věty

- **Jeden systém pro všechny:** fix podle hodnoty role, k tomu bonus i malus. Tým má jistotu, exekutiva víc rizika a víc možného zisku. Foundeři a CEO jsou mimo, schvaluje je jejich rada tří.
- **Nikdo si nepohorší.** Fix nikoho nebude nižší než dnešní průměrně vyplacená odměna.
- **Narovnává se, kdo nese víc, než dostává.** Víc rolí, vedení projektu nebo lidí, roky ve firmě a historie (achievementy) se propíšou do fixu.
- **Strop 150 tis. Kč na základ** pro kohokoli ve firmě. Co je nad, jen z podílu na zisku. Strop je zároveň měrný bod pro všechny ostatní základy.

## 2. Kde stojíme proti trhu

Tržní data pro česká herní studia neexistují, srovnáváme s celým trhem ČR. Cíl: **lépe než průměrný člověk mimo tech, kolem mediánu tech trhu, vědomě pod korporáty a bankami.**

Hrubá měsíční mzda zaměstnanců v ČR, rok 2025, tis. Kč (ISPV, mzdová sféra). Pro rok 2026 přičtěte cca 7 %. P10 a P90 jsou decily, P25 a P75 kvartily.

| Srovnání | P10 | P25 | Medián | P75 | P90 | Naše hodnota role |
|---|---|---|---|---|---|---|
| Všichni zaměstnanci ČR | 25 | 33 | 43 | 59 | 85 | |
| Vývojáři softwaru (2512) | 53 | 72 | 101 | 142 | 185 | programátor 80 až 95 |
| Testeři softwaru (2519) | 46 | 59 | 83 | 117 | 167 | QA s vývojem a DevOps 73 |
| Specialisté marketingu (2431) | 43 | 52 | 70 | 96 | 132 | UA manager 67, publishing 63 až 78 |
| Grafici v multimédiích (2166) | 41 | 48 | 58 | 77 | 104 | grafik 42 (junior) až 61 |
| Technici AV záznamu (3521) | 31 | 43 | 50 | 57 | 67 | video a motion 54 |
| Ředitelé ICT (1330) | 77 | 102 | 148 | 206 | 291 | strop základu 150 |
| Ředitelé obchodu a marketingu (1221) | 47 | 68 | 103 | 163 | 239 | vlastník segmentu 117 až 133 |

- **Proti lidem mimo tech:** průměrná mzda v ČR je ve 2. čtvrtletí 2026 cca 52 tis., v Jihomoravském kraji 50,6 tis. (ČSÚ). Proto pravidlo: **žádný plný základ role pod 52 tis.** Výjimkou je jen junior (80 % základu).
- **Proti tech trhu:** senior programátor u nás 80 až 95 tis. je mezi dolním kvartilem a mediánem celé ČR. Inzertní mediány pro seniory v Brně jsou 71 až 74 tis. (Glassdoor, Indeed), takže v Brně jsme nad nimi.
- **Korporáty a banky** platí horní kvartil a víc (senior vývojář 140 tis. a výš). Tam nesoutěžíme. Nabízíme vlastní projekty, menší firmu, podíl na výsledku a stabilitu odměny.
- **Faktura proti hrubé mzdě:** naše čísla jsou fakturace, trh je hrubá mzda. Srovnání 1 : 1 je vůči nám přísné. Na paušální dani zůstane z faktury 80 tis. zhruba stejně čistého jako zaměstnanci z hrubé mzdy cca 90 tis. Kontraktor ale nemá placenou dovolenou ani nemocenskou. Firmu stojí zaměstnanec s hrubou 101 tis. včetně odvodů cca 135 tis.

## 3. Dekret: strop základu 150 tis. Kč

Návrh nového dekretu do registru Delegační dekrety:

- **Základ (fix) nikoho ve firmě nepřesáhne 150 tis. Kč měsíčně.** Cokoli nad to jde jen z podílu na zisku.
- **Strop je měrný bod.** Základ každé role se vede jako procento stropu (tabulka v kap. 4). Když se strop při roční evaluaci posune, víme, o kolik se mají posunout základy.
- **Nikdo pod exekutivou nemá fix ani s plným bonusem vyšší než nejnižší fix exekutivy.** Dnes je to 105 proti 117 tis.
- **Strop, základy rolí i fix každého se hodnotí jednou ročně** (navazuje na R-22-09). Během roku se mění jen odměny a bonusy, a příplatky při změně odpovědnosti.
- Strop odpovídá mediánu ředitelů ICT v ČR (148 tis., ISPV 2025).

## 4. Jak vznikne fix: hodnota role

| Krok | Co | Hodnoty v návrhu |
|---|---|---|
| 1 | **Základ role**, u víc rolí vážený průměr podle procent v kartě | programátor 80 · UA manager 62 · game designer 60 · DevOps a IT 60 · publishing a LiveOps 58 · grafik MKT 56 · video a motion 52 · grafik DEV 52 · QA 52 (tis. Kč) |
| 2 | **Úroveň** | senior 100 % · medior 90 % · junior 80 % |
| 3 | **Roky ve firmě**, jen na základ | +2 % za každý dokončený rok, strop +10 % (5 let). Bere se z data nástupu v hubu |
| 4 | **Aktivní příplatky** za odpovědnost navíc | project lead +12, každý další aktivní projekt +6 · Publishing a LiveOps lead +10 · odborná autorita +10 · QA lead +8 · role pro jiný segment +8 · zástup vlastníka +5 · správa kanceláří +5 · zástup v klíčové roli +5 · mentor +2 za člověka (nejvýš 3). Dohromady nejvýš 40 % základu |
| 5 | **Pasivní složka za historii** (achievementy v hubu, trvale) | ukončené vedení projektu nebo týmu (aspoň 6 měsíců) +2, nejvýš 2× · přednáška nebo reprezentace firmy venku +1, nejvýš 3× · uspořádaný event +1, nejvýš 3× · dokončený mentoring +0,5 za člověka, nejvýš 4×. Dohromady nejvýš 8 tis. |

- **Achievementy jako jediný zdroj pravdy.** Hub už dnes počítá roky ve firmě (tenure žebříček) a má odznaky `speaker` a `company_event`. Doplníme odznaky „vedl projekt“, „vedl tým“ a „mentor“. Kdo odznak dostane, má pasivní složku, a je vidět, za co.
- **Individuální dohoda nad hodnotou role** je možná jen výjimečně, když jde o udržení klíčového člověka. Vede se jako samostatný řádek, aby byla vidět, a při roční evaluaci se k hodnotě role dorovnává.
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

## 5. Tři pásma variabilní složky

| | **Jistota** | **Lead** | **Dynamika** |
|---|---|---|---|
| Pro koho | vykonavatelské role | tým s vedením projektu, lidí nebo procesu | exekutiva |
| Fix | hodnota role, nikdy pod dnešek | hodnota role, nikdy pod dnešek | 110 + příplatky |
| Bonus max | +10 % fixu | +15 % fixu | +40 % fixu |
| Malus max | −5 % fixu | −7,5 % fixu | −10 % fixu |
| Na plánu | fix + 5 % | fix + 7,5 % | fix + 20 % |
| Hodnocení | polovina mentor, polovina splněné úkoly | polovina mentor, polovina splněné úkoly | KPI segmentu a firmy |
| Výplata | z poolu, pololetně | z poolu, pololetně | průběžně, kvartálně |

### Vyhodnocení týmu (Jistota a Lead)

- **Polovina bonusu od mentora:** písemné hodnocení za kvartál ve třech stupních. Pod očekáváním 0, v očekávání polovina, nad očekáváním celá.
- **Polovina z dat:** podíl splněných úkolů z plánu sprintů v hubu za měsíce kvartálu. Pod 60 % nic, od 60 do 90 % poměrně, nad 90 % celá polovina. Podmínka: práce je v hubu u úkolu (dnes je 24 % hodin bez úkolu).
- **Plán** = v očekávání a cca 75 % splněných úkolů, tedy polovina bonusu.
- **Malus** jen když jsou obě poloviny na nule. **První kvartál 2027 bez malusu.**
- Bonus jde z poolu (R-22-06). Když zisk na plný pool nestačí, krátí se všem stejným poměrem.

### Vyhodnocení exekutivy (Dynamika)

- KPI ve čtyřech oblastech po čtvrtině (finance segmentu proti plánu, výsledek segmentu, delivery, business a lidé). Bonus se vyplácí průběžně po kvartálech, exekutiva není v poolu.
- **Firemní pojistka:** když firma v kvartálu nedosáhne 80 % plánovaného Adj. EBITDA, bonus exekutivy se krátí na polovinu. Ve ztrátě se nevyplácí a malus platí.
- Podíl na zisku dealu: 5 % ze zisku po nákladech, 60 : 40 mezi tím, kdo přinesl, a kdo dodal (R-22-10).

### Fix exekutivy

- **Společný základ 110 tis.** a k tomu malé příplatky, které odliší rozsah: +1 za každého člověka pod sebou (nejvýš 6), +0,1 za každé procento OPEX segmentu, role navíc (vedení agendy celé exekutivy, finance a smlouvy celé firmy, práce pro jiný segment) a pasivní složka za historii stejně jako u týmu.
- Vychází to 117 až 133 tis. Bez pasivní složky je rozdíl mezi vlastníky do 9 tis., s ní do 16 tis. Odůvodnění: role navíc, počet lidí, rozpočet a historie. Příplatek za lidi se posune, až segment poroste.
- Exekutiva si fix navrhuje sama. Schvaluje ho rada tří foundrů spolu s exekutivou na daný rok.

## 6. Typové pozice

Tis. Kč měsíčně. „Dnes“ je skutečná průměrná vyplacená odměna na podobné pozici ve firmě.

| Typová pozice | Skladba | Dnes | Fix 2027 | Rozpětí | Plán |
|---|---|---|---|---|---|
| Junior grafik, první rok | 52 × 0,8 | 37 | 42 | 40 až 46 | 44 |
| Specialista, 2 roky | 52 × 1,04 | 43 | 54 | 51 až 60 | 57 |
| Specialista, 4 roky | 56 × 1,08 | 59 | 61 | 58 až 67 | 64 |
| Senior programátor, nový ve firmě | 80 | 71 | 80 | 76 až 88 | 84 |
| Senior programátor, 7 let, se zástupem a historií leadu | 80 × 1,10 + 5 + 2 | 83 | 95 | 90 až 105 | 100 |
| Game designer, lead jednoho projektu, 7 let | (GD 80 % + art 20 %) × 1,10 + 12 | 49 | 76 (ve 2 krocích) | 71 až 88 | 82 |
| Game designer, lead dvou projektů, zástup, mentor, 2 roky | 61 + příplatky na stropu 40 % | 73 | 85 (ve 2 krocích) | 79 až 98 | 91 |
| Víc rolí: QA lead, programátor, DevOps, 3 roky | (QA 53 % + prog 27 % + DevOps 20 %) × 1,06 + 8 | 45 | 73 (ve 2 krocích) | 67 až 84 | 78 |
| Vlastník segmentu | 110 + příplatky | 78 až 106 | 117 až 133 | 105 až 186 | 140 až 159 |

## 7. Co to udělá ve firmě

- **Tým (10 lidí):** všem fix roste, nikdo není pod dneškem. Největší narovnání mají dva lidé, kteří dlouho nesou roli navíc za sazbu z doby, kdy ji neměli (+27 tis., ve dvou krocích). Dalších pět dostane +11 až +16 tis.
- **Exekutiva (3):** fix se sjednotí na společném základu 110 plus příplatky. Dva vlastníci jdou nahoru výrazně, protože jsou dnes pod novým fixem seniorního programátora.
- **Rozdíl mezi lidmi stejné role** dnes dělají sazby vyjednané v různé době. Po přechodu ho dělají jen úroveň, roky ve firmě, odpovědnosti, historie a výsledky.

## 8. Kolik to stojí (rok 2027, mil. Kč)

Odměny za práci 13 lidí bez foundrů a CEO. Dnes 10,16 mil. Kč ročně.

| | Dnes | Špatný rok | Plán | Vše splněno |
|---|---|---|---|---|
| Tým | 6,99 | 8,38 | 8,90 | 9,43 |
| Exekutiva | 3,18 | 3,66 | 4,99 | 5,87 |
| **Celkem** | **10,16** | **12,04** | **13,89** | **15,30** |
| Δ proti dnešku | | +1,88 | +3,73 | +5,14 |

- **Pevná část** (fixy) je v roce 2027 +2,3 mil. (tým +1,4, exekutiva +0,9), od 2028 s plným fixem po celý rok +2,9 mil.
- **Variabilní část na plánu** +1,4 mil. se vyplatí jen ze zisku: tým z poolu, exekutiva jen v kvartálech, kdy firma plní plán (pojistka).
- Narovnání nad 10 tis. jde ve dvou krocích (1. 1. a 1. 7. 2027).
- Pro srovnání: zářijový výhled provozního zisku 2027 byl 6,6 mil. Kč, poslední výhled Martina B. je nižší. Pevná část je tedy zhruba třetina výhledu zisku. To je hlavní otázka pro U-22-05.

### Kde hledat úsporu (ověří Martin B.)

- Konec placení hodin nad úvazek bez schválení a hodin bez úkolu (24 % hodin v srpnu).
- Duplicitní AI nástroje (cca 0,35 mil. Kč ročně).
- Coworking zdrojem není. Je to průtoková platba za kancelář: firma ji lidem proplácí a lidé z ní platí kancelář. Do odměny ani do fixu se nepočítá.

## 9. Tři varianty k výběru

| Varianta | Co | 2027 na plánu | Plus | Minus |
|---|---|---|---|---|
| **1 · Tři pásma (doporučeno)** | Jistota / Lead / Dynamika | 13,89 (+3,73) | lídři mají silnější motivaci, systém odlišuje odpovědnost | o jedno pásmo víc k vysvětlení |
| 2 · Dvě pásma | lídři v Jistotě | 13,80 (+3,64) | nejjednodušší komunikace | lídr a vykonavatel mají stejné riziko i odměnu |
| 3 · Zmrazit dnešek | dnešní odměna jako fix, jen přidat variabilní složku | 11,22 (+1,06) | nejlevnější | nefér rozdíly zůstanou zabetonované ve fixu |

## 10. Foundeři, CEO a podíly na zisku

- **Foundeři a CEO** jsou mimo tento model. Jejich odměnu schvaluje rada tří.
- **Podíl na zisku** má exekutiva, CEO a dva foundeři. Nikdo z nich není v poolu pro tým.

## 11. Přechod

| Kdy | Co |
|---|---|
| do 15. 11. | potvrdit role a procenta každého (karty z 5. 11.), mentory, doplnit odznaky historie v hubu |
| do 30. 11. | přepočet modelu, finanční dopad Martina B., schválení exekutivou a radou tří |
| 1. až 15. 12. | individuální rozhovor s každým: hodnota role, fix, pásmo. Na all-hands princip spolu s odměnou 2026 a poolem |
| 1. 1. 2027 | fix místo hodinové sazby, první krok narovnání, plán sprintů a mentoři v hubu |
| Q1 2027 | první kvartál bez malusu |
| 1. 7. 2027 | druhý krok narovnání |
| prosinec 2027 | roční evaluace stropu, základů rolí a fixů |

## 12. K rozhodnutí

| # | Otázka | Návrh |
|---|---|---|
| B1 | Základ systému | varianta 1, tři pásma |
| B2 | Dekret o stropu | základ nejvýš 150 tis., nad to jen podíl na zisku, strop jako měrný bod, roční evaluace |
| B3 | Fix exekutivy | společný základ 110 + příplatky za lidi, rozpočet a role navíc, bonus +40 / −10 % s pojistkou |
| B3a | Rozpětí týmu | Jistota +10 / −5 %, Lead +15 / −7,5 % fixu |
| B3b | Hodnocení týmu | polovina mentor, polovina splněné úkoly v hubu, výplata z poolu pololetně |
| B4 | Achievementy | pasivní složka za historii podle odznaků v hubu, nejvýš 8 tis. |
| B5 | Řádek rozpočtu 2027 | +2,3 mil. fixy, variabilní složka +1,4 mil. jako řádek v Řízení krytý ziskem |
| B6 | Kdo zavede | David (model, rozhovory v Produkci, odznaky v hubu), Martin B. (finance, smlouvy), vlastníci (rozhovory ve svém segmentu) |

Zdroje: ISPV 2025, mzdová sféra ČR (ispv.cz, MPSV); ČSÚ, průměrná mzda v Jihomoravském kraji ve 2. čtvrtletí 2026 (csu.gov.cz); Glassdoor a Indeed, Senior software developer Brno 2026; Ravio, Executive bonus plans; Hyring, Variable pay.
