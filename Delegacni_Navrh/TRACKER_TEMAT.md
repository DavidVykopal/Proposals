# Tracker transformace - stav témat, rozhodnutí a úkolů

> HTML render: `tracker-temat.html`
>
> Jeden živý dokument, ve kterém je vidět, co je hotové, co běží, co je otevřené a co nám
> po cestě přibylo. Aktualizuje se po každé poradě, vždy při psaní kompilátu.
>
> Plán schůzek: `TEMATA_DALSICH_PORAD.md` · Kompiláty: `PORADA_2026-08-06_KOMPILAT.md`,
> `PORADA_2026-08-20_KOMPILAT.md` · Delegační návrh: `DELEGACNI_NAVRH.md`
>
> **Poslední aktualizace: 22. 8. 2026, po poradě 20. 8.**

---

## 0. Jak se s tím pracuje

- **Téma** je věc, o které se musí rozhodnout. Má číslo (T01, T02, …), stav, vlastníka
  a termín ve formě porady, na kterou patří.
- **Rozhodnutí** (R01, R02, …) je uzavřené téma. Jde do dekretu do Wiki a už se neotevírá,
  pokud se nezmění vstupy.
- **Úkol** (U01, U02, …) je práce mezi poradami. Má jednoho řešitele a datum.
- Nová témata přibývají zdola, viz kap. 5. Nic se z trackeru nemaže, jen se mění stav.

### Stavy

| Stav | Význam |
|---|---|
| **rozhodnuto** | Padlo rozhodnutí, je zapsané, jde do dekretu |
| **shoda, nezapsáno** | Nezávisle se na tom shodly aspoň dvě přípravy a nikdo to nerozporuje, ale zápis to nemá mezi rozhodnutími. Stačí potvrdit jedním hlasováním |
| **otevřeno** | Ví se, že se to musí rozhodnout, návrh existuje nebo ne |
| **rozpor** | Existují dva konkrétní protichůdné návrhy, je nutné vybrat |
| **průběžné** | Není to jednorázové rozhodnutí, dělá se dál |

---

## 1. Přehled: kde jsme

| Metrika | Stav k 22. 8. 2026 |
|---|---|
| Porady odjeté | 2 z 9 plánovaných (6. 8., 20. 8.) |
| Rozhodnutí zapsaná | 9 (R01 až R09) |
| Témat celkem v trackeru | 61 (T01 až T61) |
| Z toho shoda bez zápisu, k rychlému potvrzení | 10, z toho 6 na jedno hlasování 3. 9. |
| Z toho otevřených | 45 |
| Z toho rozporů k rozseknutí | 2 (stupnice delegace, práh marže na B2B) |
| Úkolů otevřených | 4 |
| Deadline celé transformace | do konce roku, Q4 nanečisto, ostrý start 1. 1. 2027 |

**Šest klíčových oblastí plus budžetování** (definice ze zápisu 20. 8.), které musí být
do konce roku hotové:

| # | Oblast | Stav | Kdy |
|---|---|---|---|
| 1 | **Segmenty** | rozhodnuto na high-level úrovni, rozpad na oblasti chybí | 20. 8. hotovo, doladění 3. 9. |
| 2 | **Role** | otevřeno | 3. 9. |
| 3 | **Optimalizace činností** | otevřeno | 3. 9. |
| 4 | **Budžetování** | otevřeno, přibylo 20. 8. | 1. 10. |
| 5 | **Odměňování** | otevřeno | 15. 10. |
| 6 | **Cíle a mentoring** | otevřeno | 29. 10. |
| 7 | **1-on-1 a vedení lidí** | otevřeno | 12. 11. |

---

## 2. Rozhodnuto

### Z porady 6. 8. 2026

| # | Rozhodnutí |
|---|---|
| **R01** | **Rytmus transformačních porad**: 1× za 14 dní ve čtvrtek, v týdnu ceremonií, cca 2 hodiny |
| **R02** | **Dokumentace**: schválené výstupy a rozhodnutí jako dekrety do interní Wiki, transparentně pro všechny |
| **R03** | **Postupná implementace**: začít jednou oblastí, otestovat, pak přidávat |
| **R04** | **Formát odměňování**: fixní mzda plus variabilní složka vázaná na KPI, ne tabulkové platy; pro vedení a postupně celou firmu |

### Z porady 20. 8. 2026

| # | Rozhodnutí |
|---|---|
| **R05** | **Terminologie**: používá se "segment" (případně "úsek"), ne "oddělení" |
| **R06** | **Třípilířová struktura**: Operations, Marketing, Produkce; nad nimi Řízení (CEO plus exec) a úroveň Majitelů (Jirka, Petr, Mirek) |
| **R07** | **Vlastnictví**: každý segment má jednoho vlastníka z exec týmu, vlastní rozpočet, definovaný účel a jasné výstupy. Operations DJ, Marketing Kuba, Produkce David |
| **R08** | **Nábor**: proces zastřešuje Operations (prakticky Akimo, s vyčleněným rozpočtem), požadavek na headcount a finální výběr kandidáta má vlastník segmentu, nový headcount schvaluje CEO |
| **R09** | **Přístup k datům**: vlastníci segmentů mají absolutní přístup ke všem datům svého segmentu a ke klíčovým datům celé firmy |

**Ke zpracování:** R05 až R09 zapsat jako dekret do Wiki (úkol U05).

---

## 3. Shoda v podkladech, čeká na zápis

Věci, na kterých se nezávisle shodly minimálně dvě přípravy, nikdo je nerozporoval, ale
nemají zapsané rozhodnutí. **Návrh: potvrdit jedním hlasováním na začátku porady 3. 9.**,
ať se o nich nemusí diskutovat znovu.

| # | Téma | Návrh k potvrzení | Zdroj |
|---|---|---|---|
| **T01** | Hranice experiment vs. otevření produkce | Práce na konceptu je experiment do **2 sprintů**, tedy 4 týdnů. Za tou čarou je to otevření produkce a schvaluje CEO plus exec. Prodloužení není pokračování, ale nové rozhodnutí | David, Jirka |
| **T02** | Publishing vs. marketing u releasu | Co je v buildu a kdy jde ven: Produkce. Store page, ASO a kampaň: Marketing. Komunikace ke hráčům o hře: Produkce | David, Kuba |
| **T03** | Rozdělení analytiky | Produktová a herní analytika: Produkce. UA a marketingová analytika: Marketing. Vlastnictví a výkon jsou dvě různé věci a napíšou se odděleně | David, Kuba |
| **T04** | Monetizace | Hra v produkci: game design. Hra v provozu: publishing. Marketing konzultovaný bez veta. Změna modelu je eskalace, změna parametru ne | David |
| **T05** | Komunita a sociální sítě | Značka a PR: Marketing. Komunita hráčů a in-game komunikace: Produkce. Krizová komunikace: CEO | David, Kuba |
| **T06** | Zadávání přes vlastníky a zákaz obcházení | Práce do segmentu jde přes jeho vlastníka, ne přímo za lidmi. Platí oběma směry a vztahuje se i na CEO. Cross-segmentové zadání přes leady, kapacitu dohodnou oba leadi | Kuba, DJ, David |

---

## 4. Otevřená témata

### Na poradu 3. 9. - role, činnosti a osazení

| # | Téma | Stav | Vlastník |
|---|---|---|---|
| **T07** | Rozpad segmentů na konkrétní činnosti, klasifikace core / podstatné / support | otevřeno | všichni za svůj segment |
| **T08** | Osazení činností konkrétními lidmi a kapacitními úvazky | otevřeno | všichni |
| **T09** | Strategie u neosazených činností: zrušit, zautomatizovat, předat, najmout, vědomě neosadit | otevřeno | všichni |
| **T10** | Role a leadi uvnitř segmentů, jejich rozhodovací pásma | otevřeno | vlastníci segmentů |
| **T11** | Rozdělení grafické kapacity jmenovitě na DEV a MKT, pravidla cross práce | otevřeno, návrh David existuje | David, Kuba |
| **T12** | Vlastník a realizace PR a brandu, případná automatizace publikačního plánu | otevřeno | Kuba |
| **T13** | Zástupnost kritických oblastí, konkrétní jména a rozsah oprávnění | otevřeno | všichni |
| **T14** | Poměr operativa / řízení v Operations: z 80/20 na 20/80, čím se to zaplatí | otevřeno | DJ |
| **T15** | Prázdné oblasti: data a analytika, efektivizace procesů, komunita | otevřeno | vlastníci segmentů |
| **T16** | Přechodný stav u analytiky (Kuba plus AI): dát mu termín konce | otevřeno | David, Kuba |

### Na poradu 17. 9. - rozhodovací pásma, limity a pravidla delegace

| # | Téma | Stav | Poznámka |
|---|---|---|---|
| **T17** | Jedna firemní stupnice delegace | **rozpor** | Jirka pracuje se 4 stupni, DJ se 7 úrovněmi. Návrh: 7 úrovní jako referenční, 4stupňová zkratka pro běžnou komunikaci. Otevřené od 6. 8. |
| **T18** | Tichý souhlas (silence = consent) | otevřeno, návrh existuje | Jirka navrhuje 48 hodin. Otevřené od 6. 8., poprvé s konkrétním číslem |
| **T19** | Schvalovací matice s konkrétními částkami a limity | otevřeno | Limity lead / vlastník segmentu / CEO, opakovaný náklad o úroveň výš, pravidlo nedostupného schvalovatele |
| **T20** | Mechanismus rozhodování při neshodě uvnitř Řízení a rozhodovací práva CEO vůči majitelům | otevřeno | **Přibylo 20. 8.** |
| **T21** | Rozsah přístupu EXEC k finančním datům podle rolí a bezpečnostní režim | otevřeno | Zbytek po R09: patří tam payroll mimo vlastní segment? Bez toho se nedopočítá interní tarif |
| **T22** | Formát rozhraní delegace: dohodový list vs. mandátové karty vs. popisy pozic | otevřeno | Vybrat jeden formát. Otevřené od 6. 8. |
| **T23** | Názvosloví rolí napříč firmou | otevřeno | Segment vyřešen (R05), pojmenování rolí a leadů ne |
| **T24** | Same-page meeting CEO a vlastník segmentu plus decision log | otevřeno | Formát a frekvence |
| **T25** | Připomenutí a potvrzení vize firmy jako referenčního bodu | otevřeno | Otevřené od 6. 8. |
| **T26** | Formát dekretu a proces zápisu do Wiki | otevřeno | Operations vlastní systém a standard zápisu |

### Na poradu 1. 10. - budžetování

| # | Téma | Stav | Poznámka |
|---|---|---|---|
| **T27** | Proces budžetování odspodu: segmenty dodají požadavky, Operations baseline a limity, CEO schvaluje rámec | shoda, nezapsáno | Věcně rozhodnuto 20. 8., chybí zapsat jako dekret |
| **T28** | Baseline nákladů za segment, roční run rate | otevřeno | Podmínka: finanční revize od DJ (U04) |
| **T29** | Struktura rozpočtu segmentu: payroll a fixní baseline vs. diskreční část, výše obálek na experimenty a růst platů | otevřeno | Metodika v přípravě Davida, čísla chybí |
| **T30** | Interní tarify: metodika, obsah cost rate, list rate | otevřeno | Operations počítá, Produkce dodává vstupy, CEO schvaluje |
| **T31** | Práh marže na B2B zakázky | **rozpor** | David navrhuje minimálně 100 %, DJ 50 %. Rozdíl je i v tom, co tarif obsahuje |
| **T32** | Metodika sdílených nákladů: cloud, zařízení, AI licence, web, právní služby, sdílení lidé | otevřeno | **Přibylo 20. 8.** Princip: viditelné a přiřaditelné, ne skryté v Operations |
| **T33** | Platby a záložní schvalovatel | otevřeno | Operations připravují, CEO schvaluje; záložní schvalovatel Peko nebo Martin, k určení |
| **T34** | Práce s úsporami | shoda, nezapsáno | Nevyčerpané zpět do centrální rezervy; prokazatelná úspora je podklad pro manažerský bonus, ne automatický vzorec |

### Na poradu 15. 10. - odměňování

| # | Téma | Stav |
|---|---|---|
| **T35** | Přechod na fixní platy a normalizace ze současné reality | otevřeno |
| **T36** | Flexibilní složka 0 až 15 %, dělení 50/50 tým a osobní, měsíční cyklus, první měsíc nanečisto | otevřeno |
| **T37** | Profit share 2× ročně, přesná pravidla | otevřeno |
| **T38** | Odměny z dealů a iniciativ, model 5 plus 5 % | otevřeno, závisí na T30 |
| **T39** | Diferencované odměňování uvnitř týmů, pravomoc leadů rozlišovat | otevřeno |
| **T40** | Man-days místo man-hours jako jednotka sledování práce | otevřeno |
| **T41** | Komunikační plán pro zbytek firmy proti echo komoře | otevřeno |

### Na poradu 29. 10. - cíle, hodnocení a růst

| # | Téma | Stav |
|---|---|---|
| **T42** | Proces nastavování cílů, KPI a OKR na oblasti a role | otevřeno |
| **T43** | Firemní scorecard, max 10 čísel, jeden vlastník na číslo | otevřeno |
| **T44** | Jak se cíle vyhodnocují a co se děje při odchylce | otevřeno |
| **T45** | Gradient důsledků, pozitivních i negativních | shoda, nezapsáno (rámec od Jirky) |
| **T46** | Osobní růst, rozvojové plány, investice do vzdělávání | otevřeno |
| **T47** | Kritéria připravenosti člověka na vyšší odpovědnost | otevřeno |

### Na poradu 12. 11. - vedení lidí a 1:1

| # | Téma | Stav |
|---|---|---|
| **T48** | Formát 1:1 oddělený od synchro meetingů, obsah a frekvence | otevřeno |
| **T49** | Kultura zpětné vazby, oprava chyb bez hledání viníka | otevřeno |
| **T50** | Důvěra jako pracovní dohoda, disagree and commit, žádné end runs | otevřeno, částečně kryto T06 |
| **T51** | Práce s přetíženými lidmi, kognitivní limit, prevence vyhoření | otevřeno, závisí na T08 |
| **T52** | Mentoring a jeho vazba na odměňování | otevřeno |

### Na poradu 26. 11. - vyhodnocení a ostrý start

| # | Téma | Stav |
|---|---|---|
| **T53** | Vyhodnocení testovacího provozu Q4: co drží, co ne | otevřeno |
| **T54** | Retrospektiva delegace: co se eskaluje moc často, tam posunout limity | průběžné |
| **T55** | Připravenost na ostrý start 1. 1. 2027 | otevřeno |

---

## 5. Co nám přibylo po cestě

Témata, která nebyla v původním plánu z 11. 8. a vznikla během porad. Tahle kapitola je
hlavní důvod, proč tracker existuje.

| Kdy přibylo | Téma | Odkud | Kam zařazeno |
|---|---|---|---|
| 20. 8. | **Budžetování jako samostatné téma** a proces sestavování rozpočtů | zápis 20. 8., jako sedmá klíčová oblast do konce roku | nová porada 1. 10. (T27 až T34) |
| 20. 8. | **Metodika sdílených nákladů** | zápis 20. 8., riziko | T32 |
| 20. 8. | **Mechanismus rozhodování při neshodě uvnitř Řízení a práva CEO vůči majitelům** | zápis 20. 8., riziko | T20 |
| 20. 8. | **Vlastnictví a realizace PR, riziko deprioritizace, automatizace publikačního plánu** | zápis 20. 8., riziko | T12 |
| 20. 8. | **Zástupnost kritických oblastí** jako páté kritérium samostatné oblasti | příprava DJ | T13 |
| 20. 8. | **Práh marže na B2B** jako číselný rozpor | přípravy David a DJ | T31 |
| 20. 8. | **Jmenovité rozdělení grafické kapacity DEV / MKT** | příprava David, podmínka bez zápisu | T11 |
| 20. 8. | **Celkový vlastník firemního webu** | příprava DJ, návrh David | T56 |
| 20. 8. | **Produktová compliance**: privacy, rating, ATT, implementace ve hře vs. reklamní a atribuční část | příprava DJ | T57 |
| 20. 8. | **Holdingová struktura jako výhled** a co z toho plyne už teď (vlastní P&L segmentu, interní tarify) | příprava David | T58 |
| 20. 8. | **Kapacitní pravidlo**: nová odpovědnost vyžaduje současně kapacitu, data, budget a mandát | příprava DJ | zapracováno do metody porady 3. 9. |
| 20. 8. | **Pravidlo kompenzace priorit**: co se ruší, když přibude práce mimo plán | příprava Kuba, převzato CEO | T06, k potvrzení |

### Drobná témata bez vlastní porady

| # | Téma | Stav | Kdo |
|---|---|---|---|
| **T56** | Celkový vlastník firemního webu a rozhraní Marketingu k němu | otevřeno, návrh David | David, Kuba |
| **T57** | Rozdělení compliance: produktová (privacy, rating, ATT) Produkce, reklamní a atribuční Marketing, firemní právní a smluvní Operations | shoda, nezapsáno | DJ |
| **T58** | Holdingová struktura jako cílový tvar: potvrdit nebo odmítnout jako referenční bod | otevřeno | Jirka |
| **T59** | Evidence ad účtů a přístupů: Operations eviduje, Marketing určuje odbornou potřebu | shoda, nezapsáno | Kuba, DJ |
| **T60** | Kombinovaný model marketingového rozpočtu: schválený rámec a škálování podle návratnosti | otevřeno | Kuba, Jirka |
| **T61** | Validace návrhu s leady před vydáním dekretu, prevence echo komory | průběžné | David |

---

## 6. Úkoly

### Otevřené

| # | Úkol | Řešitel | Termín | Stav |
|---|---|---|---|---|
| **U02** | Detailně rozpracovat svůj segment: konkrétní činnosti, role, současné obsazení konkrétními lidmi a výše kapacitních úvazků | David, DJ, Kuba, Jirka | 3. 9. | šablona v `PRIPRAVA_2026-09-03_ROLE_A_CINNOSTI.md` |
| **U03** | Rekonstruovat a doplnit ztracenou část písemné přípravy k segmentům | Kuba | 3. 9. | |
| **U04** | Kompletní finanční revize hospodaření firmy za poslední rok jako podklad pro rozpočty segmentů | DJ | podzim, před 1. 10. | podmínka porady o budžetování |
| **U05** | Zapsat rozhodnutí R05 až R09 jako dekret do Wiki a odkomunikovat firmě | David / Operations | 3. 9. | |

### Hotové

| # | Úkol | Řešitel | Uzavřeno |
|---|---|---|---|
| **U01** | Oficiální zápis a kompilát z porady 20. 8. plus podklady na další schůzku | David | 22. 8. |
| **U00a** | Sjednocení podkladů z porady 6. 8. do jednoho kompilátu | David | 11. 8. |
| **U00b** | Příprava na téma sféry vlivu a oddělení | všichni | 20. 8. |

### Průběžné

| Činnost | Kdo | Poznámka |
|---|---|---|
| Logování denních aktivit a rozhodnutí | dobrovolné, Kuba testuje | Vstup do porady 3. 9., reality check k soupisu činností |
| Projít popisy pozic s každým člověkem a doladit podle reality | vlastníci segmentů | Exekuce mezi poradami, ne bod porady |
| Decision log a počet overridů jako metrika zdraví delegace | CEO plus vlastníci | Cíl max 1 override měsíčně a klesající trend |
| Volat zpět Máďovi | Jirka | Z porady 6. 8., stav neznámý |

---

## 7. Rizika, která se dál sledují

| # | Riziko | Odkud | Stav |
|---|---|---|---|
| 1 | Pokles operativní produktivity během nastavování struktur | 6. 8. | trvá |
| 2 | Kontraproduktivní šetření: úspora na úkor kvality | 6. 8. | částečně ošetřeno (úspora nesmí snížit kvalitu ani vytvořit provozní dluh) |
| 3 | Echo komora: čtyři lidé kreslí mapu celé firmě | 6. 8., 20. 8. | trvá, ošetření navrženo v T61 |
| 4 | Závislost na finanční transparentnosti | 6. 8. | částečně ošetřeno R09, zbytek T21 |
| 5 | Závislost na správném nastavení KPI | 6. 8. | trvá, řeší se 29. 10. |
| 6 | Deprioritizace PR bez dedikované osoby | 20. 8. | trvá, T12 |
| 7 | Nedostatečná kapacita Operations: převzetí procesů bez snížení 80 % operativy | 20. 8. | trvá, T14 |
| 8 | Přímé zadávání mimo vlastníky, včetně shora | 20. 8. | ošetření navrženo v T06 |
| 9 | Převzetí nevymezených agend do Operations bez kapacity, budgetu a pravomoci | 20. 8. | trvá |
| 10 | Automatizace bez měřitelného přínosu | 20. 8. | ošetření v metodě porady 3. 9. |
| 11 | Prázdné oblasti, do kterých se začne odkazovat | 20. 8. | trvá, T15 |
| 12 | Přechodné stavy bez termínu konce | 20. 8. | trvá, T16 |
| 13 | Vlastník segmentu se sedmi oblastmi bez leadů jako úzké hrdlo | 20. 8. | trvá, T10 |

---

## 8. Harmonogram

| Kdy | Co |
|---|---|
| **do konce roku 2026** | Zpracovat a schválit všech šest klíčových oblastí plus proces budžetování |
| **Q4 2026** | Testovací provoz nové struktury a rozpočtů, kvartál nanečisto: čísla se sledují, rozhoduje se ještě postaru |
| **1. 1. 2027** | Ostrý start, nová struktura a roční rozpočty platí naplno |

Plán jednotlivých porad je v `TEMATA_DALSICH_PORAD.md`.
