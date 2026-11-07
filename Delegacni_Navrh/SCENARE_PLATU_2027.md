# Platy 2027: nápočty scénářů

> **Stav:** 4. 11. 2026, podklad k bloku B porady 19. 11. Čísla spočítaná hubovou platovou kalkulačkou (stejný model `comp2027/model.ts`, karty rolí a výplatní karty 2026 k 4. 11.). Roční náklad 2027 v mil. Kč pro 13 lidí bez founderů a CEO; měsíční částky v tis. Kč. „Dnes“ = 11,11 mil. (starší verze přípravy 19. 11. uváděla 11,13, mezitím přibyly výplatní karty; příprava je už srovnaná).
> **Plnění variabilní:** sloupce 0 / 50 / 100 % plnění. „Plán“ = 50 %.
> **Pro AI agenty:** jmenovitá čísla nejsou součástí tohoto souboru. Project lead A je popsaný jen tím, co je potřeba k rozhodnutí. Navazuje na `PRIPRAVA_2026-11-19.md` a `CILE_2027.md`.
> **Aktualizace 7. 11.:** doplněno, proč systém zavádíme (kap. 0), závazek narovnání a brány (kap. 5) a testovací režim v Q1 (kap. 5.3). Návrh Davida.

## 0. Proč to děláme

Fixní platy nejsou jen způsob, jak dostat náklady pod kontrolu. Stejným krokem řešíme čtyři věci najednou:

| Co řešíme | Jak to vypadá dnes | Co s tím udělá nový systém |
|---|---|---|
| **Slábnoucí pozice na trhu práce** | Hodnota role (role, úroveň, roky, příplatky, srovnání s trhem) je nad tím, co lidé dnes berou: tým průměrně 63,6 proti 69,1 tis., leadi 63,6 proti 79,8 tis. měsíčně (kap. 2). | Fix = férová cena role, kterou umíme obhájit proti nabídce zvenku. |
| **Nerovné podmínky** | Odměna dnes závisí na sazbě, kterou si kdo vyjednal, a na počtu vykázaných hodin, ne na roli a výsledku (D05). | Stejná role, stejná pravidla, stejný výpočet pro všechny. |
| **Odliv expertů** | Lidé, kteří nesou projekty, si říkají o víc, protože systému nevěří (project lead A, kap. 4). Náhrada leada stojí víc než narovnání a trvá měsíce. | Písemný závazek s termíny a jasná cesta nahoru místo individuálního vyjednávání. |
| **Kontrola nákladů** | Hodiny se špatně budgetují a výplaty můžou nepředvídatelně vyskočit (D05). | Jistý náklad jsou jen fixy, variabilní se platí z nové hodnoty. |

**Je to investice jako každá jiná a firma si na ni musí vydělat.** Proto se plná hodnota role neuvolní najednou, ale ve třech krocích přes brány navázané na cíle 2027. **Závazek narovnání je ale pevný:** každý dostane písemně svůj cílový fix a nejzazší termín. Brány rozhodují, jak rychle se k němu dojde, ne jestli se k němu dojde (kap. 5).

## 1. Shrnutí

- **Up from here** (fix = hodnota role, variabilní navíc od nuly) investuje jistě **+1,0 mil.** do fixů a všechno nad to platí jen za novou hodnotu. Nikdo nejde pod dnešek.
- **Střídmější** je levnější, dokud lidé neplní, ale **7 lidí včetně celé exekutivy jde fixem pod dnešek**. To je přesně model, kterému lidé nevěří.
- Project lead A si řekl o **fix 110 tis.**, protože nevěří nastavení variabilní. V up from here by při plném plnění měl **113 tis.** Fix 110 tedy znamená **zaplatit plné plnění předem**, bez ohledu na výkon.
- **Lead na 110 tlačí nahoru i exekutivu.** Exekutiva musí zůstat poměrově výš; nejnižší fix v exekutivě je dnes 83 tis. Zvednout fixy exekutivy pod 110 aspoň na 110 stojí dalších **+0,58 mil. ročně**, poměrově (stejný poměr jako dnes) **+1,14 mil.** a exekutiva by přesáhla pravidlo 140 až 180 tis. Fix 110 bez podmínek tedy reálně stojí **+0,9 mil. ročně**, jako precedens pro všechny leady cca **+2,2 mil.** (6b: 14,31 proti 12,13)
- Navrhuji **cestu k 110 přes brány**: fix 85 od ledna, 97,5 od července při splnění pololetních cílů, 110 od ledna 2028 při splnění ročních cílů. Člověk dostane jistotu fixu, ale za doložený výsledek.
- Přechod pro všechny **ve třech krocích** (leden, brána v půlce roku, brána na konci roku) snižuje riziko firmy a dává lidem jasný akční plán. Cíl je mít platy **plně narovnané na konci roku 2027**, tedy od první výplaty 2028.
- **Narovnání je závazné** *(návrh 7. 11.)*: každý dostane v prosinci písemně cílový fix, kroky a podmínky bran, podepsané CEO. Plná hodnota role platí nejpozději od 1. 7. 2028, i když brány nevyjdou (kap. 5.1).
- **Q1 v testovacím režimu** *(návrh 7. 11.)*: systém běží ostře od 1. 1., ale v lednu až březnu se při tvorbě faktury spočítají oba systémy (dnešní hodiny a nový fix s variabilní) a vyplatí se ten, který vyjde pro člověka lépe (kap. 5.3).

## 2. Přehled scénářů

| # | Scénář | Jen fixy | Plnění 50 % | Plnění 100 % | Fix pod dneškem |
|---|---|---|---|---|---|
| 0 | Dnes | 11,11 | | | |
| 1 | **Up from here** (David) | 12,13 | 14,35 | 16,12 | nikdo |
| 2 | Střídmější (David) | 10,90 | 13,19 | 15,48 | 7 lidí, celá exekutiva |
| 3 | Závěr 29. 10. (fix nikdy pod dnešek) | 11,32 | 13,24 * | 14,20 * | nikdo |
| 4 | Martin B., výchozí preset | 12,24 | 14,26 | 14,26 | nikdo |
| 5 | Up from here + PL A **fix 110 a variabilní navíc** | 12,43 | 14,70 | 16,52 | nikdo |
| 5b | Up from here + PL A **fix 110 bez variabilní + exekutiva aspoň 110** | 13,01 | 15,06 | 16,66 | nikdo |
| 6 | Up from here + **všichni 4 leadi fix 110** (precedens) | 13,73 | 16,20 | 18,21 | nikdo |
| 6b | Totéž + **exekutiva aspoň 110** (odstup) | 14,31 | 16,78 | 18,79 | nikdo |
| 7 | **Up from here ve 3 krocích** (doporučení) | 11,98 ** | 14,20 | 15,97 | nikdo |

\* scénář 3 má jinou škálu plnění (60 / 100 / 130 % plánu), sloupce jsou plán a maximum.
\** fixy 2027 při splněné pololetní bráně; bez ní 11,90. Plný fix od 2028: 12,28.

Průměr na člověka, tis. Kč měsíčně:

| Pásmo | Dnes | 1 · fix | 1 · při 100 % | 2 · fix | 2 · při 100 % |
|---|---|---|---|---|---|
| Tým (6) | 63,6 | 69,1 | 76,7 | 65,4 | 72,7 |
| Lead (4) | 63,6 | 79,8 | 106,4 | 68,4 | 91,2 |
| Exekutiva (3) | 96,7 | 96,7 | 156,7 | 82,2 | 164,4 |

## 3. Scénáře jeden po druhém

### 1 · Up from here

Fix = plná hodnota role (role, úroveň, roky, příplatky, trh). Variabilní se nastaví od dnešního stavu nahoru: kdo dělá to, co dnes, plní 0 %. Tým a lead až 11 / 33 % fixu, exekutiva zůstává na dnešním fixu s variabilní až 75 % fixu (strop 60 tis.).

| Dobré | Špatné |
|---|---|
| nikdo nejde pod dnešek, žádné „srážky“ | jistý náklad +1,0 mil. do fixů hned |
| variabilní platí jen nová hodnota, financuje se sama (cíle na 100 % musí přinést aspoň 3× náklad variabilní, tedy cca 12 mil. zisku navíc) | při plném plnění +5 mil. proti dnešku, musí se to promítnout ve výsledcích |
| fix = férová cena role, jasný argument proti trhu | lidé, kteří variabilní nevěří, ji berou jako „nic“ (viz kap. 4) |
| exekutiva 143 až 178 tis. při plném plnění, v rámci pravidla 140 až 180 | |

### 2 · Střídmější

Počítá s tím, že lidé v základu splní 50 % variabilní; o tuto polovinu je fix nižší.

| Dobré | Špatné |
|---|---|
| nejlevnější, pokud lidé neplní (fixy 10,90 pod dneškem) | **7 lidí jde fixem pod dnešek**, včetně celé exekutivy (o 3 až 30 tis.) |
| riziko nese i člověk | variabilní jen vrací dnešek, nic nového nekupuje; je to fix v převleku |
| | vyrábí spory o měkčí cíle a podporuje nedůvěru, kterou už vidíme |

### 3 · Závěr porady 29. 10.

Variabilní 50 / 25 / 10 % z celku, fix nikdy pod dnešek, dva kroky, brána 8 mil.

| Dobré | Špatné |
|---|---|
| levný jistý náklad (fixy 11,32) | kdo je blízko hodnotě role, má variabilní skoro nulovou; leadi s nízkým dneškem dostanou malé narovnání |
| shoda z porady, nikdo pod dnešek | narovnání do reality se odkládá, problém s trhem zůstává |

### 4 · Martin B.

Narovnání 2/3, bonus a malus jako % fixu, brána 8 mil. na celkovou odměnu, bez příplatků za lidi a % OPEX.

| Dobré | Špatné |
|---|---|
| jednoduchý, předvídatelný strop (max = plán = 14,26) | bonus na plánu se počítá jako jistý (plnění 100 %), takže je to fakticky fix |
| bez „empire building“ příplatků exekutivy | narovnání jen na 2/3 hodnoty role |

### 5 a 6 · Fix 110 pro project leada A, a co by to znamenalo pro všechny leady

Viz kap. 4. Krátce: jednotlivě +0,30 mil. ročně jistě, s nutným zvednutím exekutivy +0,88 mil. (5b); jako precedens pro 4 leady **+1,6 mil. ročně jistě**, s exekutivou **+2,2 mil.** (6b) proti up from here.

### 7 · Up from here ve třech krocích (doporučení)

Stejné cílové fixy jako scénář 1, ale přechod v krocích s branami (kap. 5). Rok 2027 stojí na fixech 11,90 až 11,98, plný fix 12,28 až od 2028 a jen při splněné roční bráně.

| Dobré | Špatné |
|---|---|
| firma riskuje jen to, co výsledky potvrdí | lidé čekají na plnou hodnotu role až do 2028 |
| lidé mají jasný plán: co musí platit v červenci a v prosinci | tři termíny = tři komunikace a vyhodnocení |
| brány navázané na cíle 2027 (`CILE_2027.md`) | |

## 4. Project lead A: chce fix 110 tis.

**Situace:** jeden project lead (vede dva projekty, zástup vlastníka, mentor) si řekl o základ 110 tis., protože nevěří, jak budou variabilní složky nastavené. Dnes bere kolem 80 tis., hodnota jeho role v kalkulačce vychází 85 tis.

| Varianta | Měsíčně | Ročně (mil. Kč) při plnění 0 / 50 / 100 % | Poznámka |
|---|---|---|---|
| a) Up from here | fix 85, při 100 % celkem 113 | 1,02 / 1,19 / 1,36 | fix +4,5 tis. hned, zbytek za výsledek |
| b) Fix 110 bez variabilní | 110 vždy | 1,32 / 1,32 / 1,32 | proti a): +0,30 / +0,13 / −0,04; firma platí plný výkon předem |
| c) Fix 110 + variabilní | při 100 % celkem 147 | 1,32 / 1,54 / 1,76 | nad nejnižší exekutivou, porušuje pravidlo odstupu |
| Vynucené zvednutí exekutivy u b) a c) | fixy exekutivy pod 110 (nejnižší 83) → aspoň 110 | +0,58 ročně (poměrově +1,14) | exekutiva musí zůstat poměrově nad leadem |
| d) **Cesta k 110 přes brány** (návrh) | 85 → 97,5 od 1. 7. → 110 od 1. 1. 2028 | 2027: 1,10 fix + variabilní | jistota fixu za doložený výsledek |

**Co z toho plyne:**
- Fix 110 bez variabilní stojí při plném plnění skoro stejně jako up from here (113). Rozdíl je jen v tom, **kdo nese riziko**: u varianty b) celé firma.
- Jako jednotlivost je to 0,30 mil. ročně, ale **exekutiva musí zůstat poměrově výš**: když lead bere 110, fixy exekutivy pod 110 (nejnižší dnes 83 tis.) musí aspoň na 110 (+0,58 mil. ročně; samotné 83 → 110 by bylo 0,32 mil., zbytek je druhý fix exekutivy pod 110). Poměrové zvednutí (stejný poměr jako dnes, ×1,37) by stálo +1,14 mil. a exekutiva by při plném plnění přesáhla strop 180 tis. Reálná cena fixu 110 je tedy **cca +0,9 mil. ročně**.
- Jako **precedens** to otevírá stejnou žádost u dalších leadů (scénář 6: +1,6 mil. jistě).
- Žádost je **argument pro up from here**, ne proti: lidé nevěří variabilní, protože ji znají jako „dorovnání“, které se dá vzít. Up from here ji staví jako čistý upside, a tu nedůvěru je potřeba vyřešit **transparentností a rychlou první výplatou**, ne převodem všeho do fixu.

**Jak vyřešit nedůvěru k variabilní** *(návrh)*:
- KPI a cíle podepsané **před 1. 1.**, výchozí bod = skutečnost 2026, nic se během roku nemění.
- Plnění **viditelné průběžně** v hubu (stejně jako prasátko týmového poolu), každý vidí, kolik už má.
- **První výplata po prvním kvartálu**, ne až na konci roku.
- Firemní KPI jako jedna ze čtyř částí, osobní části (mentor, úkoly z 1:1, KPI pozice) jsou pod kontrolou člověka.

**Návrh cílů a ročního výsledku pro project leada A** *(návrh, potvrdí vlastník segmentu Produkce)*:

| Cíl | Výchozí stav | Cíl 2027 | Váha |
|---|---|---|---|
| Sector Defense: marketingový zisk | 2026 YTD −13,5k USD | **aspoň +50k USD** za rok | firemní / pozice |
| Reskin #1 MF / Sector: dodání a launch | | launch v II až III 2027, D30 aspoň na úrovni MF (4,2 %) | pozice |
| Mecha Fortress: marketingový zisk | 2026 YTD +355k USD | **neklesnout pod úroveň 2026** | pozice |
| Dokumentace a onboarding balíček projektů | Red Command bez dokumentace | hotové do 31. 3. 2027 | úkoly z 1:1 |
| Mentoring 2 lidí | | hodnocení mentora | mentor |

- Kontrola pravidla 3×: variabilní při 100 % = cca 0,34 mil. Kč ročně (cca 16k USD). Samotný obrat Sector Defense z −13,5k na +50k USD je cca 63k USD, tedy přes 3× náklad.
- **Brány pro variantu d):** pololetí = Sector Defense v plusu za H1 a reskin #1 v plánu → fix 97,5 od 1. 7.; rok = cíle výše splněné → fix 110 od 1. 1. 2028, variabilní se znovu nastaví od nového stavu nahoru. Ve stejném kroku (stejná roční brána) se **zvedá fix exekutivy** tak, aby zůstala nad leadem (fixy exekutivy aspoň 110, náklad od 2028 +0,58 mil.).

## 5. Přechod: závazek, brány a testovací režim

### 5.1 Závazek narovnání *(návrh 7. 11.)*

- **Písemně a předem.** Na individuálním rozhovoru 1. až 15. 12. dostane každý list podepsaný CEO: hodnota role a cílový fix, kroky s termíny, podmínky bran a nejzazší termín. List je přílohou smlouvy, ne slib z porady.
- **Cíl: plně narovnáno na konci roku 2027.** Když vyjdou obě brány, platí plná hodnota role od 1. 1. 2028.
- **Pojistka:** když roční brána nevyjde, plná hodnota role platí **nejpozději od 1. 7. 2028**, bez dalších podmínek. Brány posouvají jen tempo.
- **Nic se nevrací dolů.** Splněný krok zůstává, i když se firmě další pololetí nedaří.
- **Výsledek bran se zveřejní s čísly** (zisk podle čísel DJ proti cíli) do 15. 7. a do 31. 1., každý v hubu vidí, kde firma je.

### 5.2 Brány

| Úroveň | Kdy | Co se uvolní | Podmínka | Když nevyjde |
|---|---|---|---|---|
| **Start** | **1. 1. 2027** | malé rozdíly (do 10 tis.) hned celé, větší o třetinu (aspoň +10 tis.); variabilní up from here od ledna, pool (prasátko) se začne plnit; Q1 v testovacím režimu (5.3) | žádná, rozhodnutí 19. 11. | |
| **Brána 1: revize v půlce roku** | rozhodnutí v červnu nad čísly H1, platí **1. 7. 2027** | větší rozdíly na dvě třetiny; prasátko se může rozbít už v pololetí | zisk H1 aspoň polovina ročního cíle (scénář B: 3,75 mil. Kč, `CILE_2027.md` kap. 4.1 a 5; metrika podle čísel DJ, rozhodnuto 6. 11.) | krok 2 se přesune na roční revizi a jde spolu s krokem 3 |
| **Brána 2: revize na konci roku** | rozhodnutí v prosinci nad forecastem DJ, potvrzení v lednu, platí **1. 1. 2028** | **plná hodnota role pro všechny**; variabilní se znovu nastaví od nového stavu nahoru; project lead A fix 110 a exekutiva ve stejném kroku (kap. 4) | roční cíl zisku 2027 splněný (scénář B: 7,5 mil. Kč) | plná hodnota role nejpozději **1. 7. 2028** (pojistka 5.1) |
| **Stretch** | 1. 1. 2028 | vyšší stupeň poolu za rok 2027 | stretch cíl splněný (scénář C: 10,2 mil. Kč) | bez stretch stupně, nic dalšího se neposouvá |

- Variabilní up from here běží celý rok od ledna, nezávisle na branách. Platí se za novou hodnotu, kterou člověk vytvoří, tu brána nebrzdí.
- Soft-launch UA nových titulů jde podle návrhu z investičního rozpočtu mimo bránu (`CILE_2027.md` kap. 4.1), nové tituly tak kroky nezablokují.
- Náklad fixů 2027: 11,90 (bez pololetní brány) až 11,98 (s ní), plný fix od 2028: 12,28. Proti dvěma krokům (12,13) šetří 0,15 mil. a hlavně posouvá velké skoky leadů za doložený výsledek. Pojistka 5.1 nic nepřidává k plnému nákladu, jen určuje nejzazší termín.

### 5.3 Q1 v testovacím režimu *(návrh 7. 11.)*

Systém startuje ostře **1. 1. 2027**: fixy, KPI, mentoři a prasátko běží. První kvartál je ale **testovací**, aby nikdo neprodělal na tom, že se nový systém teprve zabíhá.

- **Při tvorbě faktury se spočítají oba systémy:** dnešní (sazba × vykázané hodiny, dnešní příplatky) a nový (fix podle kroku 1).
- **Vyplatí se ten, který vyjde pro člověka lépe.** Měsíčně se fakturuje vyšší z obou částek.
- **Po Q1 se porovná celé čtvrtletí:** dnešní systém (součet hodin) proti novému (3× fix plus variabilní za Q1). Když vyjde lépe nový, rozdíl se doplatí s dubnovou fakturou. Nic se nevrací.
- **Od 1. 4. platí jen nový systém.** Hodiny se dál vykazují k úkolům v hubu jako podklad pro plánování a pro KPI, ne pro výplatu.
- **Vyhodnocení testu do 30. 4.:** u koho a proč vyšel dnešní systém lépe (přesčasy, špatně oceněná role, chybějící příplatek). Oprava modelu jde do kroku 2, ne zpětným snižováním.
- **Co tím získáme:** lidé si nový systém vyzkouší bez rizika, máme tři měsíce reálných dat pro obě strany a nedůvěra k variabilní (kap. 4) dostane odpověď v číslech, ne slibem.
- **Náklad:** nový fix je u všech aspoň dnešek, takže dnešní systém vyjde lépe jen tam, kde někdo vykáže výrazně víc hodin. DJ ho odhadne z výplatních karet Q1 až Q3 2026 před 19. 11. *(zatím nespočítané)*.
- Podmínka: kalkulačka v hubu umí spočítat obě varianty na faktuře; jinak to DJ za Q1 počítá ručně z výkazů.

## 6. Slabá místa a otevřené otázky

| Námitka | Proč může platit | Odpověď nebo co s tím |
|---|---|---|
| **Pravidlo 3× se dá splnit jen na papíře** | Při plném plnění stojí up from here 16,12 mil. proti dnešním 11,11, tedy +45 %. Pravidlo 3× (cca 12 mil. zisku navíc) se kontroluje po lidech, takže stejný přírůstek zisku se může započítat víckrát: obrat Sector Defense (63k USD) u project leada A, v KPI Marketingu i ve firemním KPI exekutivy. | Kontrolovat 3× za firmu celkem: součet variabilní při 100 % (4,0 mil.) proti plánovanému zisku nad cílem. Každý přírůstek zisku přiřadit jednomu vlastníkovi, ostatním jen dílčí podíl. |
| **Cesta d) je fix 110 jinou cestou** | Hodnota role project leada A je 85 tis. Fix 97,5 a 110 je nad „férovou cenou role“, kterou model sám definuje. Když se od 2028 k fixu 110 znovu přidá variabilní 33 % fixu, vyjde až cca 147 tis., tedy varianta c), kterou dokument odmítá. | Buď zvýšit hodnotu role (nová odpovědnost, třeba vlastník dvou projektů), nebo cestu formulovat jako vyšší strop variabilní, ne jako fix. Rozhodnout před 1:1 s project leadem A. |
| **Odstup exekutivy zdražuje každý posun leada dvakrát** | Fix 110 u leada vynutí +0,58 mil. u exekutivy, poměrově +1,14 mil. Pravidlo „exekutiva poměrově nad leadem“ ani poměr 1,37 nejsou nikde rozhodnuté. | Rozhodnout odstup jako minimum celkové odměny při 100 % plnění (exekutiva 143 až 178 tis., leadi v up from here průměrně 106,4 tis., project lead A 113 tis.), ne jako fix. Pak posun leada exekutivu automaticky netáhne. |
| **Brány na zisk firmy dělají z fixu variabilní** | Krok 2 a 3 fixu závisí na zisku firmy, na který tým (6 lidí, průměr 63,6 tis.) nemá vliv. Narovnání týmu na hodnotu role (69,1 tis.) se tak může posunout až za rok 2028. Metrika brány je od 6. 11. sjednocená: zdrojem jsou čísla DJ (Operations), definici dodá DJ. | Malé rozdíly (do 10 tis.) jdou hned celé, to pokrývá většinu týmu. Soft-launch UA nových titulů jde podle návrhu z investičního rozpočtu mimo bránu (`CILE_2027.md` kap. 4.1), nové tituly tak kroky nezablokují. |
| **Riziko odchodu project leada A** | Vede dva projekty včetně Mecha Fortress (marketingový zisk 2026 YTD +355k USD). Odmítnutí fixu 110 může znamenat odchod. Rozdíl b) proti a) je jen +0,30 mil. ročně, náhrada leada stojí víc a trvá měsíce. | Cestu přes brány dát písemně s konkrétními podmínkami (kap. 4). Na 1:1 zjistit, jestli je 110 podmínka setrvání, a mít připravenou záložní variantu. |
| **Dnešek se mezi poradami posunul** | 29. 10. byl dnešní náklad 10,40 mil., 1. 11. 11,13, 4. 11. 11,11. Rozdíl +0,7 mil. (opravy vstupů, definice dneška, nové výplatní karty) není nikde rozepsaný. Jirka se zeptá jako první. | Doplnit jednu větu s rozpadem rozdílu 10,40 → 11,11 od DJ a Davida. |
| **Testovací Q1 platí hodiny, které 29. 10. padly** | Přesčasy se podle rozhodnutí z 29. 10. neproplácejí. V Q1 se ale dnešní systém počítá z vykázaných hodin, takže kdo vykáže hodně, vydělá si. Může to svádět k nadsazeným výkazům. | Je to přechodné a jen na tři měsíce. Hodiny musí být u úkolů v hubu a schvaluje je vlastník segmentu jako dnes. Porovnat s průměrem 2026: výkyv nad průměr vysvětlit na 1:1. |
| **Pojistka 1. 7. 2028 platí i ve ztrátě** | Závazek bez podmínky znamená, že plný fix (12,28 mil. ročně) přijde i v roce, kdy se firmě nedaří. | Proto je to závazek jen na hodnotu role, ne na variabilní ani pool, ty dál platí jen z výsledku. Plný fix je od 2028 jistý náklad, se kterým počítá rozpočet 2028. Když hrozí ztráta, škrtá se nejdřív nábor a UA (blok C porady). Rozhodnout výslovně 19. 11. |
| **Preset neumí doporučený scénář** | Kalkulačka v hubu umí jen 2 kroky, scénář 7 je počítaný mimo ni. Preset „Schváleno 19. 11.“ tak nebude odpovídat schválenému. | Doplnit třetí krok do kalkulačky před 19. 11., nebo schválit 2krokový preset a třetí krok zapsat ručně do zápisu. |

**Potřebuje odpověď:**

- Je odstup exekutivy od leadů pravidlo, a měří se ve fixu, nebo v odměně při plném plnění (Jirka).
- Je fix 110 pro project leada A podmínkou setrvání a co uděláme, když cestu přes brány odmítne (David po 1:1).
- Kdo schvaluje cíle, KPI a strop exekutivy, když autor návrhu je sám v pásmu (Jirka, foundeři).
- Proč se dnešek posunul z 10,40 na 11,11 mil. (DJ, David).
- Variabilní po Q1: záloha s doúčtováním po roce, nebo definitivní kvartální výplata (DJ).
- Kolik bude stát testovací Q1 (rozdíl, kde hodiny vyjdou lépe než fix) a zvládne ho kalkulačka na faktuře (DJ).
- Platí pojistka 1. 7. 2028 bez výjimky, i když firma za 2027 skončí ve ztrátě (Jirka, foundeři).

## 7. K rozhodnutí 19. 11.

| # | Otázka | Návrh |
|---|---|---|
| S1 | Princip variabilní | up from here (základ 0 %) |
| S2 | Přechod | 3 kroky: start 1. 1., revize v půlce roku (brána H1), revize na konci roku (roční brána); cíl plně narovnáno od 1. 1. 2028 (kap. 5.2) |
| S2b | Závazek | písemný list ke smlouvě s cílovým fixem a termíny, pojistka: plná hodnota role nejpozději 1. 7. 2028 (kap. 5.1) |
| S2c | Q1 testovací režim | leden až březen se na faktuře počítají oba systémy a platí lepší pro člověka, od 1. 4. jen nový (kap. 5.3) |
| S3 | Project lead A | varianta d): fix 85, cesta k 110 přes brány a cíle v kap. 4; ne fix 110 bez podmínek |
| S3b | Odstup exekutivy | když lead dosáhne 110, exekutiva ve stejném kroku aspoň na 110 (poměrově výš), v rámci 140 až 180 tis. při plném plnění |
| S4 | Transparentnost variabilní | KPI podepsané před 1. 1., plnění viditelné v hubu, první výplata po Q1 |
| S5 | Výstup | uložit jako preset „Schváleno 19. 11.“ (kalkulačka v hubu umí zatím 2 kroky, třetí je potřeba doplnit) |
