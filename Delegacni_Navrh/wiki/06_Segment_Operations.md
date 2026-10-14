# Segment Operations

**Vlastník:** Martin B. · **Stav:** projednáno 1. 10. 2026, Martin dopracovává podle společné šablony · **Zdroje:** podklad Operations k 3. 9., zápis 21. 9., porada 1. 10.

Kódy činností na této stránce jsou sestavené ze zápisů. Po dopracování je nahradí číslování z Martinova podkladu.

## TL;DR

- **Účel:** zajistit, aby firma měla za co, jak, kdy a kde fungovat.
- **Tři oblasti:** Finance, Interní operations, Efektivizace a automatizace.
- **Tři lidé:** Martin B. (finance, smlouvy, platforma, řízení), Akimo (kanceláře a onboarding, hostuje z Produkce), externě Martin Ambroz s daňovým poradcem (účetnictví).
- **Hlavní problém:** operativa bere vlastníkovi segmentu kolem 80 % času, řízení 20 %. Má to být obráceně.
- **Směr:** finance automatizovat a nechat si plánování a cash flow, kanceláře předat jako balík s budgetem, NoxHub dát roli DevOps, bezpečnost a přístupy naplánovat na Q1 2027.

## Soupis činností

### Řízení segmentu

| Kód | Činnost a proč se dělá | Role | Dnes nese | Výsledek / číslo | Tah |
|---|---|---|---|---|---|
| 01 | **Řízení segmentu.** Priority, eskalace, rozhodování. Má být hlavní náplní vlastníka. | Vlastník segmentu | Martin B. (15 %) | plán segmentu, budget, reporting | zvednout kapacitu |

### F · Finance

| Kód | Činnost a proč se dělá | Role | Dnes nese | Výsledek / číslo | Tah |
|---|---|---|---|---|---|
| F2 | **Cash flow, runway, měsíční přehledy a budgety.** Firma musí vědět, kolik má a kolik si může dovolit. | Finanční řízení | Martin B. (10 %, v Q4 víc) | P&L z bankovních transakcí, cash flow projekce, týdenní finanční review na exekutivě | držet |
| F3 | **Podklady pro účetnictví a platby.** Faktury, výplaty, příprava plateb ke schválení. | Finanční řízení, výkon externí účetní | Martin B., Martin Ambroz | podklady chodí účetnímu z hubu bez ručního kopírování | zautomatizovat v hubu |
| F4 | **Konsolidace budgetů segmentů a baseline.** Podklad pro vlastníky segmentů a pro CEO. | Finanční řízení | Martin B. | baseline nákladů po segmentech | držet |

### O · Interní operations

| Kód | Činnost a proč se dělá | Role | Dnes nese | Výsledek / číslo | Tah |
|---|---|---|---|---|---|
| O5 | **HR administrativa.** Smlouvy lidí, evidence, první místo, kam jde člověk se sporem nebo problémem. | HR | Martin B. | smlouvy v pořádku, spory řešené | držet u vlastníka |
| O6 | **Náborový proces.** Inzerce, kanály, administrativa. Odborný výběr dělá vlastník segmentu. | HR | Martin B., výkon podle procesu může jít na Akima | proces náboru s rozpočtem | zapsat proces |
| O7 | **Kanceláře a faktický onboarding.** Provoz, vybavení, doplňování, počítač a místo pro nového člověka. | Správa kanceláří | Akimo | fungující kancelář v budgetu | předat jako balík s budgetem a KPI, možnost externisty |
| O8 | **Legal a smlouvy.** Dnes ad hoc přes externistu bez termínů. | Legal a smlouvy | Martin B., Martin Ambroz | proces a seznam potřebných smluv | zapsat proces |
| O9 | **Účty, přístupy, klíče a certifikáty.** Dnes nikdo neumí říct, kdo co používá. | Bezpečnost a přístupy | neosazeno | inventura a proces nakládání | naplánovat na Q1 2027 jako jednorázový budget |
| O10 | **Evidence vybavení a licencí.** Hardware, vývojové nástroje, device park. Odbornou potřebu určuje segment. | Správa kanceláří | k potvrzení | evidence a nákup na jednom místě | návrh Produkce, čeká na odpověď |
| O11 | **Bezpečnostní standard.** Pravidla pro firemní data a AI nástroje. | Bezpečnost a přístupy | Martin B. | jednoduchý standard, který zná každý | spolu s O9 v Q1 2027 |
| O12 | **Wiki a dekrety.** Systém a standard zápisu. | Vlastník segmentu | Martin B. | dekrety ve Wiki | držet |

### A · Efektivizace a automatizace

| Kód | Činnost a proč se dělá | Role | Dnes nese | Výsledek / číslo | Tah |
|---|---|---|---|---|---|
| A13 | **NoxHub: provoz a vývoj.** Průzkum v září: hub šetří v průměru 2 hodiny na člověka. | DevOps a IT | Martin B. (25 %), David | hub běží, roadmapa hubu navázaná na firemní plán | předat roli DevOps (kandidát Hutis) |
| A14 | **IT podpora kanceláře.** Síť, tiskárna, buildy. Dnes to padá na nejdražší lidi. | DevOps a IT | ad hoc | výpadek vyřešený bez seniorního programátora | předat roli DevOps |
| A15 | **Návrh automatizací pro segmenty.** Projít pipeline se segmentem, navrhnout řešení, předat k dodělání. | Vlastník segmentu | Martin B. | každá automatizace má problém, metriku a datum vyhodnocení | držet návrh, kódování předat |
| A16 | **AI adopce a vzdělávání.** Krátké interní workshopy, sdílení toho, co se kdo naučil. | Vlastník segmentu, přednáší kdokoli | Martin B., David | aspoň jeden interní workshop měsíčně, motivace odměnou | bez vyhrazené kapacity |
| A17 | **Nástroje, které si lidé postaví sami.** Aby nezůstaly v šuplíku. | DevOps a IT | bez vlastníka | sdílené portfolio nástrojů v hubu | proces sdílení přes hub |

## Role

| Role | Účel | Činnosti | Dnes nese | Stav |
|---|---|---|---|---|
| **Vlastník segmentu** | Operations fungují v budgetu a firma má čísla, podle kterých se rozhoduje. | 01, O12, A15, A16 | Martin B. | osazeno, přetíženo operativou |
| **Finanční řízení** | Firma ví, kolik má, kolik utrácí a co si může dovolit. | F2 až F4 | Martin B. | osazeno |
| **Externí účetní** | Účetnictví a daně v pořádku a včas. | výkon F3 | Martin Ambroz, daňový poradce | externě |
| **HR** | Proces náboru a personální administrativa, první místo pro řešení sporů. | O5, O6 | Martin B. | osazeno vlastníkem |
| **Správa kanceláří** | Kancelář funguje a nový člověk má první den všechno. | O7, O10 | Akimo, hostuje z Produkce | osazeno, balík s budgetem k zapsání |
| **Legal a smlouvy** | Firma má smlouvy, které potřebuje, a ví, kde jsou. | O8 | Martin B., externě Ambroz | proces chybí |
| **Bezpečnost a přístupy** | Je jasné, kdo má k čemu přístup a kdo za to odpovídá. | O9, O11 | neosazeno | Q1 2027 |
| **DevOps a IT** | Hub, buildy a IT kanceláře běží a mají jednoho odpovědného. | A13, A14, A17 | kandidát Hutis, hostuje z Produkce | shoda 1. 10., zapsat procento |

## Kdo rozhoduje

| Operations rozhodují sami | Rozhoduje CEO |
|---|---|
| běžní dodavatelé a nákupy uvnitř budgetu | stěhování kanceláře |
| finanční a provozní procesy | víceletý nebo obtížně vypověditelný závazek |
| standardní platby a evidence | nový významný opakovaný náklad |
| vratné experimenty efektivity | výdaj mimo schválený budget |
| přidělení přístupů podle potvrzené potřeby | podstatný dopad na runway, nový headcount |

Platby připravují Operations, schvaluje CEO. Záložní schvalovatel je k určení.

## Mezery a tahy

| Mezera | Odpověď | Kdo |
|---|---|---|
| Operativa 80 / řízení 20 | finance automatizovat, kanceláře a DevOps předat | Martin B. |
| Kanceláře bez jednoho vlastníka | balík s budgetem a KPI na Akima, výkon může jít na externistu | Martin B., Akimo |
| NoxHub stojí na dvou lidech bez zástupu | role DevOps a IT, runbook | Martin B., David |
| Účty, přístupy a bezpečnost | inventura a proces, jednorázový budget v Q1 2027 | Martin B. |
| Smlouvy ad hoc | proces a seznam potřebných smluv | Martin B. |
| Tabulky v Excelu vedle hubu | jeden zdroj finančních dat v reálném čase | Martin B., výhled |

## Otevřené

- Kolik procent dává Hutis roli DevOps a IT a co přesně je v balíku.
- Kolik procent dává Akimo Operations po přesunu HR k Martinovi B. a jaký budget dostane balík kanceláří.
- Převezme Operations evidenci licencí, nástrojů a zařízení (O10)?
