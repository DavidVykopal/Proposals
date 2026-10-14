# Segment Produkce: činnosti a role · 8. 10. 2026

> HTML render: `priprava-produkce-2026-10-08.html`
>
> Podklad segmentu Produkce na delegační poradu 8. 10. 2026. Stejný formát, jaký jsme 1. 10.
> odsouhlasili nad podkladem Operations (Martin B.): činnosti rozdělené do oblastí s kódem,
> u každé popis a důvod, **role**, která ji nese, a zvlášť sloupec, **kdo tu roli nese dnes**.
> Role jsou pak rozepsané samostatně, aby systém stál i bez konkrétních jmen.
>
> Navazuje na `PRIPRAVA_2026-09-03_DAVID.md` (soupis 20 činností), na karty lidí z
> `../Q4Plan/PORADA_2026-10-01_DELEGACE_4.md`, na rozhodnutí z 21. 9. (budget, personální
> pravomoci a reporting nese vlastník segmentu) a na Q4 OKR (`../Q4Plan/Q4_OKR_2026.md`).
> Procenta jsou z úvazku daného člověka, odhad na pětky. Částky a limity sem nepatří, ty jsou
> téma rozpočtové porady 22. 10.

---

## 1. TL;DR

**Situace**

- Produkce je největší segment: 10 lidí, pět oblastí, 24 činností. Účel: hry vznikají, vycházejí, žijí a zaplatí se.
- Součet činností vychází na **cca 7,85 úvazku**, plánovatelná kapacita segmentu (75 % na člověka, po odečtení práce pro Operations) je **cca 7,2**. Schodek kolem půl úvazku sedí celý u vlastníka segmentu.
- Vlastník segmentu je na cca 150 %. Na řízení (plán, kapacity, lidé, budget) z toho jde 45 bodů, zbytek je exekuce: B2B, backend a tooling, R&D. Stejný problém jako u Operations, jen v jiném poměru.

**Hlavní problém**

- Exekuce se sbíhá u vlastníka a řízení dostává zbytek. Od 21. 9. k tomu přibyla odpovědnost za budget a reporting segmentu, která kapacitu zatím nemá.
- Tři činnosti nemají roli osazenou: data a analytika (přechodně Kuba s AI do 31. 12.), aktivní komunita, výroba playable ads pro Marketing.
- Dva lidé nesou roli pro jiný segment bez čísla v kartě: Akimo (kanceláře) a nově Hutis (DevOps a IT).

**Co navrhuju**

- **11 rolí**, z toho 9 osazených, 1 přechodně osazená a 1 nově k náboru. Žádná nová vedoucí role, žádný art lead ani GD lead.
- Vlastník segmentu si nechává řízení a B2B obchod. Odchází hub (do Operations pod DevOps roli), outsourcing (na project leady), licence (evidence do Operations) a postupně B2B delivery.
- Project leadi dostávají vedení projektu vyčíslené: 20 % úvazku každý. Dosud to v kartách nebylo.
- Hutis: QA lead 40, programování 20, DevOps a IT pro Operations 15. Bez snížení programování by byl na 90.

**K potvrzení na poradě:** kapitola 10, devět bodů.

## 2. Co je nové proti podkladu z 3. 9.

| Změna | Odkud | Dopad na Produkci |
|---|---|---|
| Formát: činnost má roli a zvlášť jméno, role jsou popsané samostatně | porada 1. 10., review podkladu Operations | kap. 4 a 5 jsou přepsané do tohoto tvaru |
| Budget, personální pravomoci a reporting nese vlastník segmentu | rozhodnutí 21. 9. | nová činnost R4, v soupisu z 3. 9. nebyla |
| HR a nábor zastřešuje Martin B., Akimovi zůstává faktický onboarding v kanceláři a balík kanceláří s vlastním budgetem | záznam 1. 10., k potvrzení | Akimo dává Operations méně než 25 až 30 %, odhadem 10 až 15 % |
| NoxHub dostává DevOps roli, kandidát Hutis | záznam 1. 10., shoda u stolu | hub odchází z mých 25 % toolingu, Hutis potřebuje číslo v kartě |
| AI vzdělávání není vyhrazená kapacita, dělá se, když zbyde čas | záznam 1. 10. | mých 10 % pro Operations padá na 0 až 5 |
| V Q4 se nehledá samostatný herní analytik, hledá se tester a komunitní správce (půl QA, půl Discord) | Q4 OKR, O6.1 a "co neděláme" | přechodný stav analytiky nemá po 31. 12. pokračování, viz kap. 9 |
| Sector Defense je venku, Q4 je o live-ops a ladění, žádný nový titul | Q4 OKR, O2 a O3 | těžiště kapacity se přesouvá z vývoje do oblasti P |

## 3. Mapa segmentu: pět oblastí

| Kód | Oblast | Co pokrývá | Činnosti | Kapacita (% úvazku) |
|---|---|---|---|---|
| R | **Řízení segmentu** | plán a roadmapa, kapacity, lidé, budget a reporting | R1 až R4 | 45 |
| V | **Vývoj her** | design, kód, art, vedení projektu, technický základ, R&D | V5 až V11 | 540 |
| P | **Publishing a LiveOps** | QA, release, compliance, live-ops, provoz, komunita | P12 až P17 | 110 |
| B | **B2B** | pipeline a nabídky, delivery, playable ads | B18 až B20 | 35 + playables |
| D | **Data a produkční tooling** | datový stack, herní analytika, herní backend, web | D21 až D24 | 55 |

Celkem cca **785 %**, tedy 7,85 úvazku. Z toho 20 bodů dnes vykonává Kuba (D21, D22).

Vrstvy: **C** core (bez toho se hra nevydá nebo nevydělá), **P** podstatné (bez toho to jde týdny, ne měsíce), **S** support.

## 4. Soupis činností

Sloupec "Tah" říká, co se s činností stane: **držet**, **předat**, **zautomatizovat**, **najmout**, **zúžit** nebo **zrušit**.

### 4.1 R · Řízení segmentu

| Kód | Činnost a proč se dělá | Vrstva | Role | Dnes nese (%) | Zástup | Výsledek / číslo | Tah |
|---|---|---|---|---|---|---|---|
| R1 | **Plán produkce a roadmapa titulů.** Sprinty, milníky a priority mezi projekty. Bez toho si každý projekt plánuje sám a o prioritách rozhoduje ten, kdo je nejhlasitější. | C | Vlastník segmentu | David 20 | Aldy | milníky v termínu, počet přeplánování za kvartál | držet |
| R2 | **Kapacitní plánování a obsazení projektů.** Kdo na čem dělá v jakém sprintu, včetně rezervace pro B2B a playables. Chrání tým před přetížením a projekty před tichým odsáváním lidí. | C | Vlastník segmentu | David 10 | Aldy | utilizace 70 až 80 %, nikdo nad 100 % | držet |
| R3 | **Vedení lidí v segmentu.** 1:1, cíle, hodnocení, odměna, odborný onboarding. Od 21. 9. sem patří i rozhodnutí o odměně a setrvání lidí v mém budgetu. | P | Vlastník segmentu | David 10 | nevyžaduje | 1:1 v rytmu, cíle první den měsíce | držet, zvednout na 15 až 20 |
| R4 | **Budget a reporting segmentu.** Návrh rozpočtu, čerpání, měsíční čísla segmentu připravená bez vyžádání. Nové od 21. 9.: CEO reporty jen sbírá, nevyhledává. | P | Vlastník segmentu | David 5 | nevyžaduje | budget vs. skutečnost do 5. dne měsíce, čísla v hubu | držet, čísla tahat z hubu |

### 4.2 V · Vývoj her

| Kód | Činnost a proč se dělá | Vrstva | Role | Dnes nese (%) | Zástup | Výsledek / číslo | Tah |
|---|---|---|---|---|---|---|---|
| V5 | **Herní design a ekonomika titulů.** Mechaniky, progres, balanc, monetizační model hry v produkci. Určuje retenci a výnos na hráče dřív, než se napíše řádek kódu. | C | Game designer | Aldy 40, Karlík 40 | vzájemně | retence D1 a D7, ARPDAU proti cíli | držet |
| V6 | **Programování a technická architektura.** Feature, opravy, integrace SDK, výkon. | C | Programátor | Čoud 75, Milan 75, Mirek 50, Hutis 35 | vzájemně | dodané feature za sprint, crash-free rate | držet, Hutis na 20 |
| V7 | **Herní art a UI.** Postavy, prostředí, UI, animace do buildu. | C | Grafik DEV | David Č. 75, Peko 60, Aldy 10, Karlík 10 | vzájemně | art podle plánu sprintu, počet vrácení | držet |
| V8 | **Vedení projektu.** Denní priority, zadání pro kód a art, řešení sporů v projektu, stav do hubu. Dosud nevyčíslené, proto to project leadům v kartách chybělo. | C | Project lead | Aldy 20, Karlík 20 | vzájemně | sprint dodaný podle plánu, stav projektu v hubu bez dotazu | držet, zapsat číslo |
| V9 | **Technický dluh, build pipeline a engine.** Verze Unity, build stroje, sdílené knihovny, standard kódu a review. Bez toho roste doba buildu a každý projekt řeší totéž znovu. | P | Odborná autorita tech | Mirek 10 | Čoud | doba buildu, blokující technické incidenty | držet |
| V10 | **R&D: prototypy a podklad pro greenlight.** Nejvýš 2 sprinty na koncept, pak rozhodnutí. V Q4 bez nového titulu jen Hexapolis 2 a testy. | C | Vlastník segmentu + tým podle konceptu | David 15 | Aldy, Karlík | rozhodnutí do 2 sprintů, ověřené koncepty za kvartál | zúžit na 10 |
| V11 | **Outsourcing a externí dodávky do vývoje.** Zadání, převzetí a kontrola externích dodávek (art, překlady, externí designér). | P | Project lead (zadání a převzetí), Vlastník segmentu (smlouva a budget) | David 5 | nevyžaduje | dodávky převzaté na první pokus | předat project leadům |

### 4.3 P · Publishing a LiveOps

| Kód | Činnost a proč se dělá | Vrstva | Role | Dnes nese (%) | Zástup | Výsledek / číslo | Tah |
|---|---|---|---|---|---|---|---|
| P12 | **QA a release readiness.** Testplán, evidence chyb, rozhodnutí, jestli je build připravený ven. | C | QA lead | Hutis 40, Akimo 10 (release gate) | Akimo | kritické chyby v produkci po releasu: 0 | držet, posílit testerem |
| P13 | **Release management a platformy.** Store konzole, review, game setup, rollout po procentech. | C | Publishing a LiveOps lead | Akimo 20 | David | releasy v termínu, zamítnutí review: 0 | držet |
| P14 | **Produktová compliance.** Privacy, rating, ATT, licence použitých assetů ve hře. V září se u licencí ukázalo, že nebylo jasné, kdo je řeší. | P | Publishing a LiveOps lead | Akimo 5 | David | žádný incident na storech, audit 1× za kvartál | držet, zapsat vlastníka do Wiki |
| P15 | **LiveOps vydaných titulů.** Eventy, kalendář, battle pass, provozní monetizace uvnitř modelu. Hlavní téma Q4 (O3.4: 25 % revenue živého titulu z LiveOps). | C | Publishing a LiveOps lead | Akimo 20 | David, výhledově Hutis | podíl LiveOps na revenue, kalendář 4 týdny dopředu | držet, v Q4 priorita |
| P16 | **Provoz produktů.** Servery, produktový cloud, monitoring, incidenty. | P | Publishing a LiveOps lead | Akimo 10 | David | dostupnost, doba řešení incidentu | držet |
| P17 | **Komunita hráčů, in-game komunikace a support.** Odpovědi na recenze a tickety, oznámení ve hře. Dnes jen reaktivně. | P | Komunitní správce (neosazeno), do nástupu Publishing a LiveOps lead | Akimo 5 | nevyžaduje | doba odpovědi, hodnocení na storech | najmout (O6.1), viz kap. 9 |

### 4.4 B · B2B

| Kód | Činnost a proč se dělá | Vrstva | Role | Dnes nese (%) | Zástup | Výsledek / číslo | Tah |
|---|---|---|---|---|---|---|---|
| B18 | **B2B pipeline a nabídky.** Scoping, pricing podle interních tarifů, dojednání. V Q4 bez outreache, jen RON_India a příchozí příležitosti. | C | B2B lead | David 10 | nevyžaduje | marže nabídek, podpis další fáze RON_India | držet |
| B19 | **B2B delivery.** Vedení zakázky, klient, kontrola dodávky (playables a externí vývoj). | C | B2B lead (klient a marže), Programátor (výroba) | David 25 | Čoud | skutečná marže proti odhadu, dodávky v termínu | předat výrobu po zakázkách, cíl 15 do konce Q4 |
| B20 | **Playable ads pro Marketing.** Interní zakázka: zadání a priorita z Marketingu, výroba v Produkci stejnou pipeline jako B2B. Dnes bez rezervované kapacity. | P | Programátor (výroba), zadává Marketing přes vlastníky | nevyčísleno | nevyžaduje | playable dodaný do termínu kampaně, počet za kvartál | zapsat procento a jméno, viz kap. 9 |

### 4.5 D · Data a produkční tooling

| Kód | Činnost a proč se dělá | Vrstva | Role | Dnes nese (%) | Zástup | Výsledek / číslo | Tah |
|---|---|---|---|---|---|---|---|
| D21 | **Datový stack, eventy v buildech a definice metrik.** Co se loguje, jak se počítá retence a ROAS, aby celá firma četla jedno číslo. | P | Datový analytik | Kuba + AI 10 (hostuje z Marketingu) | nevyžaduje | jedna definice retence, pokrytí eventy | přechodně do 31. 12., pak rozhodnout |
| D22 | **Herní analytika.** Čtení dat, doporučení k ladění a monetizaci, vyhodnocení A/B testů. | P | Datový analytik | Kuba + AI 10, David 5 | nevyžaduje | doporučení za sprint promítnutá do buildu | přechodně do 31. 12., pak rozhodnout |
| D23 | **Herní backend a produkční tooling.** Shared Game Backend, extrakce playables, nástroje zrychlující vývoj. Hub a AMA sem od teď nepatří, jdou pod Operations. | P | Vlastník segmentu, výhledově Programátor | David 25 včetně hubu | nikdo | SGB v prvním titulu (O5.4), každý nástroj s business casem | zúžit na 10, hub předat |
| D24 | **Firemní web a produktové a CPI stránky.** Technický provoz a nasazení. Obsah a marketingové části jsou Marketing. | S | Vlastník segmentu | David 5 | nevyžaduje | stránky dostupné, nová stránka do 2 dnů od zadání | zautomatizovat šablonou |

### 4.6 Co ze soupisu odchází mimo segment

| Činnost | Dnes | Kam | Stav |
|---|---|---|---|
| NoxHub a AMA: vývoj a provoz | David, část z D23 | Operations, role DevOps | shoda 1. 10., zapsat |
| Licence assetů, vývojové nástroje, device park: evidence a nákup | David 5 | Operations (evidence a nákup), odbornou potřebu určuje Produkce | návrh z 3. 9., bez odpovědi |
| AI vzdělávání firmy | David 10 | Operations, bez vyhrazené kapacity | záznam 1. 10. |
| Kanceláře a faktický onboarding | Akimo | Operations, s vlastním budgetem | záznam 1. 10. |

## 5. Role segmentu

Jedenáct rolí. Role je balík činností s jedním výsledkem. Jeden člověk může nést víc rolí, každá má pak v jeho kartě vlastní číslo.

| Role | Účel jednou větou | Činnosti | Dnes nese | Zástup | Stav |
|---|---|---|---|---|---|
| **Vlastník segmentu** | Segment dodává hry podle plánu, v budgetu a s lidmi, kteří vědí, co mají dělat. | R1 až R4, V10, D23, D24 | David | Aldy (plán a kapacity) | osazeno, přetíženo |
| **Project lead** | Titul jde podle plánu sprintu a tým ví, co je dnes priorita. | V8, V11 | Aldy, Karlík, každý na svých titulech | vzájemně | osazeno, formalizovat |
| **Game designer** | Hra drží hráče a vydělává podle cíle. | V5 | Aldy, Karlík | vzájemně | osazeno |
| **Programátor** | Funkční a stabilní build podle zadání sprintu. | V6, výroba B19 a B20 | Čoud, Milan, Mirek, Hutis | vzájemně | osazeno, Milan do 31. 10. (O6.3) |
| **Odborná autorita tech** | Jeden technický standard napříč tituly a rozhodnutý spor, když se projekty neshodnou. | V9, review a arbitráž ve V6 | Mirek | Čoud | osazeno, roli napsat |
| **Grafik DEV** | Art a UI v buildu podle plánu sprintu. | V7 | David Č., Peko | vzájemně | osazeno |
| **Odborná autorita art** | Jeden vizuální standard, review a mentoring grafiků. | review ve V7 | Peko | nevyžaduje | osazeno, roli napsat |
| **Publishing a LiveOps lead** | Co je hotové, vyjde včas, žije a vydělává i po vydání. | P13 až P16, release gate v P12 | Akimo | David | osazeno, na hraně kapacity |
| **QA lead** | Ven nejde build s kritickou chybou. | P12 | Hutis | Akimo | osazeno, potvrdit |
| **B2B lead** | Zakázky s marží nad prahem, dodané v termínu. | B18, B19 | David | Čoud (delivery) | osazeno vlastníkem segmentu, bez vlastního člověka |
| **Datový analytik** | Jedna pravda v číslech a doporučení, podle kterých se ladí hry. | D21, D22 | přechodně Kuba + AI | nevyžaduje | přechodně do 31. 12. |

**Neosazená role k náboru:** tester a komunitní správce (O6.1, půl QA, půl Discord). V QA půlce spadá pod QA leada (P12), v komunitní půlce nese P17.

**Role, které se vědomě nezřizují:**

- **Art lead DEV.** Zadání pro grafiky jde přes project leady, kvalitu drží odborná autorita art.
- **GD lead napříč tituly.** Design leadership je součást role project leada, spory arbitruje vlastník segmentu.
- **Tech lead napříč tituly.** Zatím ne. Technická rozhodnutí per projekt, arbitrem je odborná autorita tech. Vrátit se k tomu po rozhodnutí o Milanovi (31. 10.).

## 6. Rozhodovací pásma rolí

Bez částek a bez čísel úrovní, ty čekají na rozhodnutí o stupnici (T17) a na schvalovací matici.

| Role | Rozhoduje sama | Eskaluje, komu | Hodnotí se podle |
|---|---|---|---|
| **Vlastník segmentu** | priority mezi projekty, obsazení lidí, čerpání uvnitř schváleného budgetu, odměna a setrvání lidí segmentu, provozní release | CEO: greenlight a ukončení titulu, nový headcount, překročení budgetu, víceletý závazek, zásah do IP a značky | profit segmentu proti plánu, milníky v termínu, utilizace 70 až 80 % |
| **Project lead** | denní priority, zadání pro kód a art, spory v projektu, žádost o outsourcing, vyřazení člověka z projektu | vlastník segmentu: změna rozsahu nebo termínu milníku, potřeba kapacity mimo projekt | sprinty dodané podle plánu, metriky titulu |
| **Game designer** | mechaniky, balanc a parametry uvnitř schváleného modelu | project lead: změna rozsahu. Vlastník segmentu: změna monetizačního modelu | retence a ARPDAU proti cíli |
| **Programátor** | způsob provedení, technické řešení uvnitř standardu | project lead: odhad mimo sprint. Autorita tech: odchylka od standardu | dodané feature, crash-free rate |
| **Odborná autorita tech** | standard kódu, verze enginu a knihoven, výsledek technického sporu mezi projekty | vlastník segmentu: změna s dopadem na termín nebo budget | doba buildu, blokující incidenty |
| **Grafik DEV** | způsob provedení uvnitř art direction | project lead: priorita a rozsah | art podle plánu, počet vrácení |
| **Odborná autorita art** | vizuální standard, výsledek art review | vlastník segmentu: změna stylu s dopadem na rozsah | konzistence, počet vrácení |
| **Publishing a LiveOps lead** | provozní releasy a hotfixy, liveops kalendář, monetizační parametry uvnitř modelu, komunikace ke hráčům | vlastník segmentu: změna monetizačního modelu, stažení titulu ze storu. CEO: krizová komunikace | releasy v termínu, podíl LiveOps na revenue, incidenty |
| **QA lead** | testplán, evidence, **zastavit release** | vlastník segmentu: vydat build se známou chybou | kritické chyby v produkci: 0 |
| **B2B lead** | scoping a cena nad prahem marže, přidělení lidí na zakázku uvnitř kapacitního plánu | CEO: zakázka pod prahem marže, závazek delší než kvartál, exkluzivita nebo zásah do IP | marže proti odhadu, dodávky v termínu |
| **Datový analytik** | definice metrik, metodika vyhodnocení testů | vlastník segmentu: změna definice, která mění historická čísla | doporučení promítnutá do buildu |

**Jednosměrné dveře Produkce** (vždy přes CEO, bez ohledu na částku): greenlight nebo ukončení titulu, změna monetizačního modelu živé hry, podpis B2B zakázky s exkluzivitou nebo převodem IP, přijetí a propuštění, platformní závazek delší než rok.

## 7. Lidé a role dnes

| Člověk | Role | Dnes (%) | Po tazích (%) | Co se mění |
|---|---|---|---|---|
| **David** | Vlastník segmentu, B2B lead | cca 150 | cca 95 do konce Q4 | hub do Operations, V11 na project leady, licence do Operations, AI vzdělávání bez vyhrazené kapacity, výroba B19 po zakázkách na programátory |
| **Akimo** | Publishing a LiveOps lead; hostuje v Operations (kanceláře, faktický onboarding) | 70 + 25 až 30 | 70 + 10 až 15 | HR a nábor u Martina B., kanceláře s budgetem a možností externisty, P17 odejde s nástupem komunitního správce |
| **Hutis** | QA lead, Programátor; hostuje v Operations (DevOps a IT) | 75 | 40 + 20 + 15 = 75 | programování z 35 na 20, jinak by byl na 90 |
| **Aldy** | Project lead, Game designer | 50 + nevyčísleno | 20 + 40 + 10 art = 70 | vedení projektu má číslo, přibývá V11 na vlastních titulech, zástup vlastníka za plán a kapacity |
| **Karlík** | Project lead, Game designer | 50 + nevyčísleno | 20 + 40 + 10 art = 70 | stejně jako Aldy |
| **Čoud** | Programátor | 75 | 75 | výroba B2B zakázek uvnitř 75, zástup B19 |
| **Milan** | Programátor | 75 | 75 | trvalý kontrakt, nebo ukončení do 31. 10. (O6.3) |
| **Mirek** | Odborná autorita tech, Programátor | 60 | 60 | role autority napsaná do Wiki, Hex 2 dostane projekt v hubu |
| **David Č.** | Grafik DEV | 75 | 75 | beze změny |
| **Peko** | Odborná autorita art, Grafik DEV | 60 až 70 | 60 + MKT do 10 | role autority napsaná, strop pro Marketing 10 % |

Po tazích zůstává nad 75 % jen vlastník segmentu. Pod 75 se dostane až po plné delegaci B2B delivery a herního backendu, tedy ne v Q4.

## 8. Mezery a tahy

U každé mezery právě jedna odpověď, jméno a termín.

| # | Mezera | Činnosti | Odpověď | Kdo a do kdy | Riziko, když se to nestane |
|---|---|---|---|---|---|
| 1 | Vlastník segmentu na 150 % | R1 až R4, V10, B18, B19, D23 | **předat**: hub, V11, licence, výroba B19 | David, vyhodnocení 26. 11. | trpí plán, kapacity a lidé, tedy jádro role |
| 2 | Data a analytika bez vlastního člověka | D21, D22 | **přechodně** Kuba + AI do 31. 12., pak rozhodnutí | David a Kuba, rozhodnout do 26. 11. | od 1. 1. činnost nemá nikdo, monetizace zůstane odhad |
| 3 | Aktivní komunita | P17 | **najmout** testera a komunitního správce | podle O6.1 do 30. 11., domovský segment rozhodnout dnes | Discord pro RC a SD bez správce, Akimo to vedle LiveOps neunese |
| 4 | Playable ads pro Marketing bez kapacity | B20 | **zapsat** procento a jméno do kapacitního plánu | David a Kuba, do 22. 10. | kampaně čekají na výrobu, která se dělá po večerech |
| 5 | Herní backend a tooling bez zástupu | D23 | **zúžit a předat**: SGB po prvním nasazení na programátora | David, po O5.4 | výpadek stojí na jednom člověku |
| 6 | QA kapacita tenká | P12 | **najmout** (QA půlka nového člověka), do té doby Hutis 40 + Akimo gate | podle O6.1 | chyby projdou do produkce při souběhu dvou releasů |
| 7 | Hutis ve třech rolích | V6, P12, DevOps | **zapsat** 40 / 20 / 15 a zadávat přes vlastníky | David a Martin B., dnes | DevOps a QA si budou kapacitu brát potichu z programování |

## 9. Hranice s Marketingem, Operations a EXEC

### 9.1 S Marketingem

| Téma | Návrh Produkce | Otázka na Kubu |
|---|---|---|
| **Herní analytika po 31. 12.** | Role Datový analytik patří Produkci. Q4 OKR říká, že se analytik do konce roku nehledá. Do 26. 11. rozhodnout jednu ze tří cest: nábor v Q1, trvalé hostování Kuby s procentem a platbou podle P4, nebo zúžení na automatické reporty v hubu. | Kterou z těch tří cest unese Marketing? Kolik z dnešních 30 % je po automatizaci reálně potřeba? |
| **Playable ads** | Výroba v Produkci (B20), zadání a pořadí z Marketingu, kapacita rezervovaná v plánu sprintu. | Kolik playables za kvartál Marketing potřebuje a s jakým předstihem přijde zadání? |
| **Tester a komunitní správce** | Domovsky Produkce: QA půlku vede QA lead, komunitu hráčů má podle T05 Produkce. Značkovou komunikaci a PR zadává Marketing přes vlastníky. | Nábor podle OKR vede Kuba. Souhlasí s domovským segmentem Produkce, nebo chce komunitní půlku pod sebou? |
| **Peko pro Marketing** | Strop 10 %, zadání přes vlastníky. | Stačí 10 % i pro další tranše Sector Defense? |
| **Ruda na Sector Defense** | Jednorázová výpomoc s launchem. Pokud má být trvalá, napsat procento do karty. | Jednorázově, nebo trvale? |
| **Release** | Co je v buildu a kdy jde ven: Produkce. Store page, ASO a kampaň: Marketing (T02). | potvrdit zápisem |

### 9.2 S Operations

| Téma | Návrh Produkce | Otázka na Martina B. |
|---|---|---|
| **Hutis jako DevOps a IT** | Domovsky Produkce, 15 % pro Operations, zadání přes vlastníky. Architektonická rozhodnutí (síť, infrastruktura) posvěcuje odborná autorita tech. | Stačí 15 %? Co přesně je v balíku: hub, buildy, IT v kanceláři? |
| **Akimo** | Domovsky Produkce, pro Operations 10 až 15 %: balík kanceláří a faktický onboarding. HR a nábor u Martina B. | Platí rozdělení z 1. 10.? Jaký budget a jaká KPI dostane balík kanceláří? |
| **NoxHub** | Vlastní Operations. Produkce je uživatel a zadavatel přes roadmapu hubu. Herní backend (SGB) zůstává Produkci. | Kde je hranice mezi hubem a herním backendem u sdílených částí (účty, API)? |
| **Licence, nástroje, device park** | Evidence a nákup Operations, odbornou potřebu určuje Produkce. | Přebírá to Operations? Odkdy? |
| **Odborný onboarding** | Dělá lead, pod kterého člověk nastupuje, s přizvaným odborníkem na roli. Faktický onboarding Operations. | potvrdit zápisem |

### 9.3 S EXEC a CEO

- **Greenlight a ukončení titulu** rozhoduje CEO na podklad Produkce. Experiment do 2 sprintů rozhoduje vlastník segmentu (T01).
- **Legacy review** (O3.6) vlastní Jirka. Produkce dodá dopad na kapacitu v P13 a P16.
- **Zadání do segmentu jde přes vlastníka** i od CEO (T06). Týká se hlavně přímých zadání project leadům a grafikům.

## 10. K potvrzení na poradě

| # | Co potvrdit | Kdo rozhoduje |
|---|---|---|
| 1 | Pět oblastí a 24 činností jako soupis Produkce | všichni |
| 2 | Jedenáct rolí z kap. 5 a tři role, které se vědomě nezřizují | všichni |
| 3 | Vedení projektu vyčíslené na 20 % u obou project leadů | David |
| 4 | Hutis 40 / 20 / 15: QA lead, programování, DevOps a IT pro Operations | David, Martin B. |
| 5 | Akimo: domovsky Produkce, pro Operations 10 až 15 % (kanceláře a faktický onboarding), HR u Martina B. | David, Martin B. |
| 6 | Hub, licence a AI vzdělávání odchází z Produkce do Operations | Martin B. |
| 7 | Playable ads pro Marketing: výroba v Produkci s rezervovaným procentem, jméno a číslo do 22. 10. | David, Kuba |
| 8 | Domovský segment testera a komunitního správce | Kuba, David, Jirka |
| 9 | Termín rozhodnutí o analytice po 31. 12.: do 26. 11. | David, Kuba, Jirka |

## 11. Vstup pro rozpočtovou poradu 22. 10.

Z tohoto podkladu vychází struktura budgetu Produkce. Čísla doplním po baseline od Martina B.

| Řádek budgetu | Z čeho se počítá |
|---|---|
| Payroll domovských lidí | 10 lidí podle kap. 7 |
| Hostující kapacita přijatá | Kuba (D21, D22), Ruda a Ondra podle rozhodnutí z kap. 9.1 |
| Hostující kapacita poskytnutá | Akimo 10 až 15 % a Hutis 15 % pro Operations, Peko do 10 % pro Marketing |
| Nábor | tester a komunitní správce podle domovského segmentu |
| Externí dodávky | outsourcing artu, překlady, externí designér (V11) |
| Produktový cloud a nástroje | servery, SDK, licence enginu a assetů (P16, V9) |
| R&D obálka | prototypy do 2 sprintů (V10) |
| B2B | vlastní řádek s výnosem i nákladem, aby šla vidět marže zakázky (B18, B19) |

## 12. Po poradě

- [ ] Zapracovat opravy z porady do tohoto podkladu a vystavit ho ve Wiki vedle Operations a EXEC.
- [ ] Projít kartu s každým člověkem segmentu, opravit procenta podle reality.
- [ ] Napsat role odborné autority tech a art (Mirek, Peko) a roli project leada do Wiki.
- [ ] Dohodnout s Martinem B. balík DevOps a IT pro Hutise a zadávání přes vlastníky.
- [ ] S Kubou vyčíslit playable ads na kvartál a zapsat jméno do kapacitního plánu.
- [ ] Připravit návrh budgetu segmentu podle kap. 11 na 22. 10.
- [ ] Aktualizovat `TRACKER_TEMAT.md`.
