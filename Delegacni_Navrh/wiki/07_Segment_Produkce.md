# Segment Produkce

> Zdroj: hub wiki, kategorie Delegační dekrety (stav 15. 10. 2026, staženo 7. 11. 2026).

**Vlastník:** David Vykopal · **Účel:** hry vznikají, vycházejí, žijí a zaplatí se · **Stav:** zmapování schváleno jako podklad 8. 10. 2026, finalizace 22. 10. · **Zdroje:** podklad Produkce k 3. 9., karty lidí z 1. 10., podklad Produkce k 8. 10. (plná verze a light), porada 8. 10.

## TL;DR

- **Třináct rolí, pět oblastí, 24 činností.** Deset lidí domovsky v Produkci.
- Vlastník segmentu si nechává řízení a B2B obchod. NoxHub, evidence licencí a zařízení a AI vzdělávání patří do Operations.
- **Art lead, GD lead a tech lead napříč tituly se vědomě nezřizují.** Kvalitu drží odborné autority tech (Mirek) a art (Peko), které nevedou lidi.
- Neosazené: tester a komunitní správce (nábor v Q4). Produktovou analytiku přechodně do 31. 12. 2026 vykonává Kuba z Marketingu.
- CPI testy patří Marketingu, Produkce dodává prototypy (D06).

## Role

Názvy rolí jsou pracovní. Jeden člověk může nést víc rolí, kde roli nese víc lidí, potvrzuje se hlavní nositel.

| # | Role | Činnosti | Kdo aktuálně zastává |
| --- | --- | --- | --- |
| R1 | Vlastník segmentu | Ř1 plán a roadmapa · Ř2 kapacity a obsazení · Ř3 vedení lidí · Ř4 rozpočet a reporting · V6 R&D a greenlight. Ručí za výsledky, budget a lidi segmentu, rozhoduje priority mezi projekty. | David Vykopal; zástup za plán a kapacity Aldy |
| R2 | Project lead | V4 vedení projektu · V7 outsourcing. Denní priority, zadání pro kód a art, spory v projektu, může člověka vyřadit z projektu. | David Bém (Aldy), Karel Kunc (Karlík); každý na svých titulech, zastupují se vzájemně |
| R3 | Game designer | V1 herní design a ekonomika. Mechaniky, balanc a parametry uvnitř schváleného modelu. | Aldy, Karlík (role oddělená od R2) |
| R4 | Programátor | V2 programování · výroba B2 a B3. Způsob provedení a technické řešení uvnitř standardu. | Jan Ševčík (Čoud), Milan Vavro, Mirek, Hutis |
| R5 | Odborná autorita tech | V5 technický dluh, pipeline a engine. Standard, review a arbitráž technických sporů, nevede lidi a neručí za dodání. | Miroslav Schery (Mirek); zástup Čoud |
| R6 | Grafik DEV | V3 herní art a UI v buildu podle plánu sprintu | David Čalta, Peko; Aldy a Karlík na vlastních titulech |
| R7 | Odborná autorita art | review a standard ve V3. Vizuální standard, review a mentoring grafiků, nevede lidi. | Petr (Peko) |
| R8 | Publishing a LiveOps lead | P2 release a platformy · P3 compliance · P4 LiveOps · P5 provoz produktů. Provozní releasy a hotfixy, liveops kalendář, monetizační parametry uvnitř modelu. | Martin Vajsar (Akimo); zástup David |
| R9 | QA lead | P1 QA a release readiness. Testplán, evidence chyb, právo zastavit release. | Jakub Hutečka (Hutis); release gate drží Akimo |
| R10 | B2B lead | B1 pipeline a nabídky · B2 delivery. Scoping a cena nad prahem marže, klient, marže zakázky. | David Vykopal; zástup delivery Čoud |
| R11 | Produktový analytik | D1 datový stack a metriky · D2 herní analytika. Role Produkce, kterou přechodně vykonává Marketing. | Jakub Burian (Kuba), přechodně do 31. 12. 2026 |
| R12 | Správce backendu a nástrojů | D3 herní backend a tooling · D4 web a CPI stránky. Shared Game Backend a nástroje zrychlující vývoj; NoxHub sem nepatří. | David Vykopal, bez zástupu |
| R13 | Tester a komunitní správce | P6 komunita a support · testování v P1. Půl QA, půl komunita. | neosazeno, nábor v Q4; P6 do nástupu reaktivně Akimo |

Práce pro Operations (Akimo: kanceláře a onboarding zázemí, Hutis: DevOps a IT) a exec agenda jsou mimo činnosti segmentu a píšou se v kartě člověka jako hostující procento.

## Činnosti podle oblastí

### Ř · Řízení segmentu

| # | Činnost | Role | Kdo aktuálně zastává |
| --- | --- | --- | --- |
| Ř1 | **Plán produkce a roadmapa titulů:** sprinty, milníky, priority mezi projekty. Bez plánu si každý projekt plánuje sám a o prioritách rozhoduje ten, kdo je nejhlasitější. | R1 Vlastník segmentu | David Vykopal, zástup Aldy |
| Ř2 | **Kapacitní plánování a obsazení projektů:** kdo na čem dělá v jakém sprintu, včetně rezervace pro B2B a playables. Plánuje se na 75 % úvazku. | R1 Vlastník segmentu | David Vykopal, zástup Aldy |
| Ř3 | **Vedení lidí v segmentu:** 1:1, cíle, hodnocení, odměna, odborný onboarding. O odměně a setrvání rozhoduje vlastník segmentu, mentoři a project leadi dávají návrhy. | R1 Vlastník segmentu | David Vykopal |
| Ř4 | **Rozpočet a reporting segmentu:** návrh rozpočtu, čerpání a měsíční čísla připravená bez vyžádání. | R1 Vlastník segmentu | David Vykopal |

### V · Vývoj her

| # | Činnost | Role | Kdo aktuálně zastává |
| --- | --- | --- | --- |
| V1 | **Herní design a ekonomika titulů:** mechaniky, progres, balanc, monetizační model. Změna parametru je rozhodnutí designéra, změna monetizačního modelu jde přes vlastníka segmentu. | R3 Game designer | Aldy, Karlík |
| V2 | **Programování a technická architektura:** feature, opravy, integrace SDK, výkon. Technický spor mezi projekty rozhoduje odborná autorita tech. | R4 Programátor, arbitráž R5 | Čoud, Milan, Mirek, Hutis |
| V3 | **Herní art a UI:** postavy, prostředí, UI, animace do buildu. Zadání jde přes project leada, kvalitu drží odborná autorita art. | R6 Grafik DEV, review R7 | David Čalta, Peko; Aldy a Karlík se podílejí |
| V4 | **Vedení projektu:** denní priority, zadání pro kód a art, stav do hubu. Design leadership je součást role. | R2 Project lead | Aldy, Karlík, každý na svých titulech |
| V5 | **Technický dluh, build pipeline a engine:** verze Unity, build stroje, sdílené knihovny, standard kódu. Technická rozhodnutí se dělají per projekt. | R5 Odborná autorita tech | Mirek, zástup Čoud |
| V6 | **R&D: prototypy a podklad pro greenlight.** Nejvýš 2 sprinty na koncept, pak rozhodnutí. Greenlight plné produkce schvaluje CEO. | R1 Vlastník segmentu, tým podle konceptu | David Vykopal s Aldym nebo Karlíkem |
| V7 | **Outsourcing a externí dodávky:** zadání, převzetí a kontrola. Zadání a převzetí dělá project lead, smlouvu a budget drží vlastník segmentu. | R2 Project lead, smlouva a budget R1 | David Vykopal; návrh předat Aldymu a Karlíkovi |

### P · Publishing a LiveOps

| # | Činnost | Role | Kdo aktuálně zastává |
| --- | --- | --- | --- |
| P1 | **QA a release readiness:** testplán, evidence chyb, rozhodnutí o připravenosti buildu. QA lead může zastavit release, vydat build se známou chybou schvaluje vlastník segmentu. | R9 QA lead, testování R13 | Hutis; release gate Akimo |
| P2 | **Release management a platformy:** store konzole, review, game setup, rollout. Co je v buildu a kdy jde ven, je Produkce; store page, ASO a kampaň je Marketing. | R8 Publishing a LiveOps lead | Akimo, zástup David |
| P3 | **Produktová compliance:** privacy, rating, ATT, licence assetů ve hře. | R8 Publishing a LiveOps lead | Akimo |
| P4 | **LiveOps vydaných titulů:** eventy, kalendář, battle pass, provozní monetizace. Hlavní téma Q4. Parametry uvnitř modelu rozhoduje lead, změna modelu je eskalace. | R8 Publishing a LiveOps lead | Akimo, zástup David |
| P5 | **Provoz produktů:** servery, produktový cloud, monitoring, incidenty. | R8 Publishing a LiveOps lead | Akimo |
| P6 | **Komunita hráčů, in-game komunikace a support.** Dnes jen reaktivně. Značka a PR je Marketing, krizová komunikace CEO. | R13 Tester a komunitní správce, do nástupu R8 | neosazeno, reaktivně Akimo |

### B · B2B

| # | Činnost | Role | Kdo aktuálně zastává |
| --- | --- | --- | --- |
| B1 | **B2B pipeline a nabídky:** scoping, pricing podle interních tarifů, dojednání. V Q4 bez outreache. Zakázku pod prahem marže nebo s exkluzivitou schvaluje CEO. | R10 B2B lead | David Vykopal |
| B2 | **B2B delivery:** vedení zakázky, klient, kontrola dodávky. Klient a marže zůstávají u B2B leada, výroba jde po zakázkách na programátory. | R10 B2B lead, výroba R4 | David Vykopal, výroba podle zakázky |
| B3 | **Playable ads pro Marketing:** interní zakázka, zadání a pořadí z Marketingu (M-K4), výroba stejnou pipeline jako B2B. | R4 Programátor, zadává Marketing | k potvrzení: jméno a kapacita do 22. 10. |

### D · Data a produkční nástroje

| # | Činnost | Role | Kdo aktuálně zastává |
| --- | --- | --- | --- |
| D1 | **Datový stack, eventy v buildech a definice metrik,** aby celá firma četla jedno číslo. Vlastní Produkce, vykonává Marketing. | R11 Produktový analytik | Kuba, přechodně do 31. 12. |
| D2 | **Herní analytika:** čtení dat, doporučení k ladění, vyhodnocení A/B testů. Po 31. 12. rozhodnout: nábor, trvalé hostování, nebo automatické reporty. | R11 Produktový analytik | Kuba, David se podílí |
| D3 | **Herní backend a produkční tooling:** Shared Game Backend, extrakce playables. Každý nový nástroj má business case. | R12 Správce backendu a nástrojů | David Vykopal, bez zástupu |
| D4 | **Firemní web, produktové a CPI stránky:** technický provoz a nasazení. Obsah a marketingové části dodává Marketing. | R12 Správce backendu a nástrojů | David Vykopal |

## Rozhodovací práva rolí

| Role | Rozhoduje sama | Eskaluje |
| --- | --- | --- |
| Project lead | denní priority, zadání pro kód a art, spory v projektu, žádost o outsourcing, vyřazení člověka z projektu | vlastník segmentu: změna rozsahu nebo termínu milníku, potřeba kapacity mimo projekt |
| Game designer | mechaniky, balanc a parametry uvnitř schváleného modelu | project lead: změna rozsahu; vlastník segmentu: změna monetizačního modelu |
| Programátor | způsob provedení, technické řešení uvnitř standardu | project lead: odhad mimo sprint; autorita tech: odchylka od standardu |
| Odborná autorita tech | standard kódu, verze enginu a knihoven, výsledek technického sporu mezi projekty | vlastník segmentu: změna s dopadem na termín nebo budget |
| Grafik DEV | způsob provedení uvnitř art direction | project lead: priorita a rozsah |
| Odborná autorita art | vizuální standard, výsledek art review | vlastník segmentu: změna stylu s dopadem na rozsah |
| Publishing a LiveOps lead | provozní releasy a hotfixy, liveops kalendář, monetizační parametry uvnitř modelu, komunikace ke hráčům | vlastník segmentu: změna monetizačního modelu, stažení titulu ze storu; CEO: krizová komunikace |
| QA lead | testplán, evidence, zastavit release | vlastník segmentu: vydat build se známou chybou |
| B2B lead | scoping a cena nad prahem marže, přidělení lidí na zakázku uvnitř kapacitního plánu | CEO: zakázka pod prahem marže, závazek delší než kvartál, exkluzivita nebo zásah do IP |
| Produktový analytik | definice metrik, metodika vyhodnocení testů | vlastník segmentu: změna definice, která mění historická čísla |

**Jednosměrné dveře Produkce** (vždy přes CEO, bez ohledu na částku): greenlight nebo ukončení titulu, změna monetizačního modelu živé hry, podpis B2B zakázky s exkluzivitou nebo převodem IP, přijetí a propuštění, platformní závazek delší než rok.

## Lidé, kapacita a zástupy

Procenta jsou odhad na pětky z podkladu k 8. 10. Sloupec „Cíl" je stav po předání, které Produkce navrhuje.

| Člověk | Role | Dnes (%) | Cíl (%) | Zástup |
| --- | --- | --- | --- | --- |
| David Vykopal | R1, R10, R12 | cca 150 | cca 95 do konce Q4 | Aldy (plán, kapacity) |
| Martin Vajsar (Akimo) | R8; hostuje v Operations (R5, R6) | 70 + 25 až 30 | 70 + 10 až 15 | David |
| Jakub Hutečka (Hutis) | R9, R4; hostuje v Operations (DevOps) | 75 | 40 QA + 20 kód + 15 DevOps | Akimo (QA) |
| David Bém (Aldy) | R2, R3, R6 | 50 + nevyčísleno | 20 + 40 + 10 art = 70 | Karlík |
| Karel Kunc (Karlík) | R2, R3, R6 | 50 + nevyčísleno | 20 + 40 + 10 art = 70 | Aldy |
| Jan Ševčík (Čoud) | R4 | 75 | 75 | Milan |
| Milan Vavro | R4 | 75 | 75 | Čoud |
| Miroslav Schery (Mirek) | R5, R4 | 60 | 60 | Čoud |
| David Čalta | R6 | 75 | 75 | Peko |
| Petr (Peko) | R7, R6; výpomoc Marketingu | 60 až 70 | 60 + MKT do 10 | David Čalta |

Po předáních zůstává nad 75 % jen vlastník segmentu. Pod 75 % se dostane až po plné delegaci B2B delivery a herního backendu, tedy ne v Q4. Vlastník segmentu má dnes kolem 8,5 přímých podřízených, což je dlouhodobě neudržitelné.

## K potvrzení 22. 10.

| # | Bod | Kdo |
| --- | --- | --- |
| 1 | Pět oblastí, 24 činností a 13 rolí jako finální soupis Produkce | všichni |
| 2 | Vedení projektu vyčíslené na 20 % u obou project leadů | David |
| 3 | Hutis 40 / 20 / 15: QA lead, programování, DevOps pro Operations | David, Martin B. |
| 4 | Akimo: domovsky Produkce, pro Operations 10 až 15 % (kanceláře a onboarding zázemí), HR u Martina B. | David, Martin B. |
| 5 | Playable ads: jméno a procento v kapacitním plánu | David, Kuba |
| 6 | Domovský segment testera a komunitního správce | Kuba, David, Jirka |
| 7 | Herní analytika po 31. 12.: nábor v Q1, trvalé hostování Kuby s platbou podle P4, nebo automatické reporty (rozhodnout do 26. 11.) | David, Kuba, Jirka |
| 8 | Struktura vedení lidí v Produkci (počet přímých podřízených vlastníka) | David |
