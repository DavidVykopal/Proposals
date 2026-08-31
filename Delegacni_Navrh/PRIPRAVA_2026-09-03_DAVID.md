# Moje příprava na poradu 3. 9. 2026 - David

> Osobní podklad. Společný neutrální podklad je `PRIPRAVA_2026-09-03_ROLE_A_CINNOSTI.md`,
> kompilát minulé porady `PORADA_2026-08-20_KOMPILAT.md`, stav témat `TRACKER_TEMAT.md`,
> moje předchozí příprava `PRIPRAVA_2026-08-20_DAVID.md`.
> Tenhle dokument je moje odpověď na úkol U02 za segment Produkce plus můj pohled na to,
> jaké role firma jako celek potřebuje a kolik lidí na ně reálně má.
> Stav: **v0, základ.** Metoda, soupis činností, návrh rolí a moje odpovědi na sporné body
> jsou hotové. Jména, kapacity a součty jsou označené `[DOPLNIT]` a doplním je před renderem.

---

## 0. Co si chci z porady odnést

| # | Co | Proč to nejde odložit |
|---|---|---|
| 1 | **Soupis činností Produkce jako schválený základ, ze kterého se odvozují role** | Když se role nakreslí dřív než činnosti, vzniknou podle titulů a zbytek zůstane u mě. Přesně z toho se dostáváme. |
| 2 | **Rozhodnutí o leadech uvnitř Produkce: kolik, jaké balíky, kdo** | Nesu sedm oblastí. Cílový stav z přípravy Operations jsou dvě zastřešující na vlastníka. Rozdíl je pět balíků, které musí dostat jméno, jinak se mapa jen překreslila. |
| 3 | **Součet kapacity za firmu a u každé mezery právě jedna odpověď** | Tohle je jediné číslo, které řekne, jestli tři segmenty vůbec mohou fungovat s lidmi, které máme. A jestli ne, kde přesně chybí člověk. |
| 4 | **Jmenovité rozdělení grafiků na DEV a MKT** (T11) a **termín konce přechodného stavu u analytiky** (T16) | Obě věci se z 20. 8. přenesly bez rozhodnutí. Potřetí je nechci přenášet. |

Plus jeden bod pro celou poradu: **pravidlo, jak z kapacity činností spočítat počet lidí na typ role** (kap. 2.2). Bez něj se o tom, jestli potřebujeme druhého programátora nebo druhého UA manažera, bude mluvit od oka.

## 1. Přiznaná zaujatost

- **Produkce je největší segment.** Nejvíc lidí, nejvíc činností, nejvíc leadů, které z téhle porady vzniknou. Návrh rolí uvnitř Produkce je v mém zájmu, protože mi odlehčí. Zároveň je to přesně to, co po mně porada chce, takže to nezastírám.
- **Chci předávat, ne sbírat.** Z sedmi oblastí si chci nechat dvě. Všechno ostatní má v tomhle dokumentu navrženého leada nebo odpověď ze žebříku.
- **Metodu jsem psal já.** Proto ji aplikuju nejpřísněji na sebe: tři činnosti ke zrušení jsou z mého segmentu a z mého kalendáře, ne z cizího.
- **Vlastní tooling.** Část mého času jde do interních nástrojů a AI (hub, herní backend, AMA bot, extrakce playables). Je to činnost, která v žádné kartě z 20. 8. nebyla, a nesu ji já. Dávám ji do soupisu, ať se o ní rozhodne stejně jako o ostatních.

## 2. Jak čtu zadání: role z činností, ne naopak

### 2.1 Pravidla, která přebírám ze společného podkladu

- Role je **balík činností s jedním výsledkem a jedním vlastníkem.**
- Role, kterou nese víc lidí, není role, je to tým a potřebuje leada.
- Jeden člověk může nést víc rolí, každá má vlastní výsledek a vlastní kapacitu v soupisu.
- Plánujeme na **75 % kapacity.** Kdo má v soupisu činnosti za víc než 75 % úvazku, je přetížený.

### 2.2 Co přidávám: od kapacity k počtu lidí

Otázka "potřebujeme víc programátorů" se nedá zodpovědět bez pravidla. Navrhuju tohle:

1. **Sečti kapacitu všech činností stejného typu** napříč segmenty (například všechno programování všech titulů, B2B i prototypů).
2. **Vyděl 0,75.** Výsledek je počet celých úvazků, které ten typ role potřebuje.
3. **Porovnej s počtem lidí, kteří tu roli dnes nesou.** Rozdíl je mezera nebo přebytek.
4. **Zbytek pod celé číslo se řeší podle velikosti:**

| Zbytek | Odpověď |
|---|---|
| do 0,3 úvazku | přidá se k existující roli jako druhá role s vlastním cílem |
| 0,3 až 0,7 úvazku | sdílený člověk mezi segmenty, částečný úvazek nebo externista s interním vlastníkem |
| nad 0,7 úvazku | celý člověk, tedy business case a nábor |

5. **Lead se počítá zvlášť.** Vedení lidí a rozhodování je činnost s vlastní kapacitou (u leada 3 až 5 lidí zhruba 20 až 30 % úvazku). Když se to nezapočítá, lead je na papíře na 100 % a v realitě na 130 %.

Tohle pravidlo chci odsouhlasit před blokem o mezerách, protože jinak každý najme podle pocitu.

### 2.3 Co je lead a co je vykonavatel

Dvě různé věci, které se v soupisu nesmí smíchat:

- **Lead** nese balík činností **a rozhodovací pásmo** k němu. Rozhoduje bez eskalace do napsaného limitu, řídí lidi na balíku, ručí za výsledek.
- **Vykonavatel** nese činnost, ale pásmo má jen na způsob provedení. Neručí za výsledek balíku, ručí za svůj kus.

Z toho plyne: **lead není titul za seniority.** Nejseniornější programátor nemusí být tech lead, když nechce nést lidi a rozhodnutí. A naopak.

## 3. Soupis činností Produkce (šablona A)

Segment: **Produkce** · Vlastník: **David** · Účel: hry vznikají, vycházejí, žijí a zaplatí se.

Dvacet činností, rozpad sedmi oblastí z 20. 8. plus body, které Operations navrhly jako produktové (produktový cloud, produktová compliance, licence assetů, firemní web). Vrstva: **C** core, **P** podstatné, **S** support.

| # | Činnost | Vrstva | Kdo to dnes dělá | Kapacita | Hlavní práce? | Zástup | Výsledek / číslo |
|---|---|---|---|---|---|---|---|
| 01 | **Plán produkce a roadmapa titulů**: sprinty, milníky, priority mezi projekty | C | David | `[DOPLNIT %]` | ano | `[DOPLNIT]` | milníky držené v termínu, počet přeplánování za kvartál |
| 02 | **Kapacitní plánování a obsazení projektů lidmi**, včetně půjček kapacity mezi projekty | C | David | `[DOPLNIT %]` | ano | `[DOPLNIT]` | utilizace týmu 70 až 80 %, žádný člověk nad 100 % |
| 03 | **Herní design a ekonomika titulů**: design, balanc, monetizační parametry | C | `[DOPLNIT jména per titul]` | `[DOPLNIT %]` | ano | `[DOPLNIT]` | retence D1/D7 a ARPDAU titulu proti cíli |
| 04 | **Programování a technická architektura titulů** | C | `[DOPLNIT jména]` | `[DOPLNIT %]` | ano | `[DOPLNIT]` | dodané feature za sprint, crash-free rate |
| 05 | **Herní art a UI** (DEV grafici) | C | `[DOPLNIT jména]` | `[DOPLNIT %]` | ano | `[DOPLNIT]` | art dodaný podle plánu sprintu, počet vrácení |
| 06 | **QA a release readiness buildů**: testplán, evidence chyb, právo zastavit release | C | `[DOPLNIT, Akimo?]` | `[DOPLNIT %]` | `[hlavní / navíc]` | `[DOPLNIT]` | kritické chyby v produkci po releasu: cíl 0 |
| 07 | **Technický dluh, build pipeline a engine**: upgrady, CI, technická údržba | P | `[DOPLNIT, Mirek?]` | `[DOPLNIT %]` | navíc | nevyžaduje | doba buildu, počet blokujících technických incidentů |
| 08 | **Outsourcing a externí dodávky do vývoje**: zadání, kontrola, převzetí | P | David | `[DOPLNIT %]` | navíc | nevyžaduje | dodávky převzaté na první pokus, náklad proti plánu |
| 09 | **R&D: prototypy a podklad pro greenlight**, max 2 sprinty na koncept | C | David + `[DOPLNIT]` | `[DOPLNIT %]` | navíc | `[DOPLNIT]` | počet ověřených konceptů za kvartál, rozhodnutí do 2 sprintů |
| 10 | **Release management a platformy**: store konzole, review, provozní komunikace s platformami | C | `[DOPLNIT, Akimo?]` | `[DOPLNIT %]` | `[hlavní / navíc]` | `[DOPLNIT]` | releasy v termínu, zamítnutí review: cíl 0 |
| 11 | **Produktová compliance**: privacy, rating, ATT, implementace ve hře (T57) | P | `[DOPLNIT]` | `[DOPLNIT %]` | navíc | nevyžaduje | žádný incident na storech, audit 1× za kvartál |
| 12 | **LiveOps vydaných titulů**: eventy, kalendář, provozní monetizace | C | `[DOPLNIT]` | `[DOPLNIT %]` | `[hlavní / navíc]` | `[DOPLNIT]` | výnos živých titulů proti plánu, obsazený kalendář 4 týdny dopředu |
| 13 | **Provoz produktů**: servery, produktový cloud, monitoring, incidenty | P | `[DOPLNIT]` | `[DOPLNIT %]` | navíc | `[DOPLNIT]` | dostupnost, doba řešení incidentu |
| 14 | **Komunita hráčů, in-game komunikace a support** | P | **nikdo celé** `[DOPLNIT kdo reaktivně]` | `[DOPLNIT %]` | navíc | nevyžaduje | doba odpovědi na support, hodnocení na storech |
| 15 | **Interní tooling, herní backend a AI nástroje ve vývoji**: hub, backend platforma, AMA bot, extrakce playables, AI pipeline | P | David | `[DOPLNIT %]` | navíc | **nikdo** | ušetřené hodiny za měsíc proti výchozímu stavu, každý nástroj s business casem |
| 16 | **B2B pipeline a nabídky**: scoping, pricing podle tarifů, dojednání | C | David (systematicky nikdo) | `[DOPLNIT %]` | navíc | nevyžaduje | marže nabídek, počet dealů v pipeline |
| 17 | **B2B delivery**: playables a externí vývoj, vedení zakázky, vztah s klientem | C | `[DOPLNIT jména]` | `[DOPLNIT %]` | `[hlavní / navíc]` | `[DOPLNIT]` | skutečná marže proti odhadu, dodávky v termínu |
| 18 | **Datový stack, eventy v buildech a definice metrik** | P | **nikdo formálně**, fakticky Kuba + AI | `[DOPLNIT %]` | navíc | nevyžaduje | jedna definice retence pro celou firmu, pokrytí eventy u živých titulů |
| 19 | **Herní analytika**: čtení dat, doporučení k ladění a monetizaci | P | Kuba + AI, David | `[DOPLNIT %]` | navíc | nevyžaduje | doporučení za sprint, která se promítla do buildu |
| 20 | **Vedení lidí v Produkci**: 1:1, cíle, hodnocení, návrhy odměn, odborný onboarding | P | David | `[DOPLNIT %]` | ano | nevyžaduje | 1:1 v rytmu, cíle nastavené první den měsíce |

Mimo tabulku, jako **support**, a rovnou s návrhem odpovědi:

| # | Činnost | Vrstva | Kdo dnes | Návrh |
|---|---|---|---|---|
| S1 | Firemní web a CPI/produktové stránky (T56) | S | David | vlastnictví ano, výkon zautomatizovat a předat: obsah MKT částí Marketing, technika jeden člověk z Produkce jako druhá role |
| S2 | Licence assetů, vývojové nástroje, device park | S | David, ad hoc | předat do Operations jako evidenci a nákup; odbornou potřebu určuje Produkce |

**Co z tabulky vidím ještě před doplněním čísel:**

- Řádky 01, 02, 08, 09, 15, 16, 20 a obě supportní mají v poli "kdo" **moje jméno.** To je sedm hlavních činností plus dvě supportní na jednom člověku, z toho čtyři "navíc". Součet vyjde nad 75 % ještě dřív, než napíšu čísla.
- Řádek 15 je největší **skrytá činnost** ve firmě: nikde nebyla, nikdo ji nezadal, a odhaduju, že je to jedna z mých největších položek. Musí buď dostat business case a vlastníka, nebo se zredukovat.
- Řádky 14, 16 a 18 mají v poli "kdo" **nikdo.** To jsou moje tři mezery (kap. 6).
- Zástup u core: řádky 01, 02, 10, 12 potřebují jméno. Bez něj má Produkce čtyři core činnosti visící na jednom člověku.

## 4. Součet kapacity Produkce

```
Lidé v Produkci:                 [DOPLNIT počet]  × 0,75  =  [DOPLNIT] dostupných úvazků
Součet činností 01 až 20 + S1, S2:                          [DOPLNIT] potřebných úvazků
Rozdíl:                                                      [DOPLNIT]
```

Pravidla, podle kterých to sčítám:

- Sdílení lidé (grafici před rozdělením DEV/MKT, Akimo mezi Operations a Produkcí) se počítají podle podílu času, přesnost na desítky procent.
- Moje činnosti se sčítají zvlášť, ať je vidět, o kolik jsem přes 75 % **před** předáním a o kolik **po** něm (kap. 5.4).
- Kapacita leadů na vedení (kap. 2.2, bod 5) je započítaná v řádku 20 a bude se muset rozdělit mezi nové leady.

## 5. Návrh rolí a leadů uvnitř Produkce

Odvozeno ze soupisu: každá role je balík řádků z kap. 3 s jedním výsledkem. Rozhodovací pásma jsou tu jen heslovitě, částky a limity patří na 17. 9.

### 5.1 Co si nechávám

Dvě zastřešující oblasti, v souladu s cílovým stavem z přípravy Operations:

| Oblast | Řádky | Proč právě tohle |
|---|---|---|
| **Vývoj a portfolio** | 01, 02, 09, 20 | Plán, kapacita, greenlight podklad a vedení leadů. To je práce vlastníka segmentu a nikam jinam se předat nedá. |
| **B2B** | 16 + dohled nad 17 | Pipeline a pricing jsou dnes na mně a nikdo jiný to systematicky nenosí. Delivery předám leadovi (5.2), pipeline si nechám do doby, než podílový systém ukáže, jestli dealy začnou nosit i ostatní. |

### 5.2 Role a leadi, které navrhuju

| Role | Balík řádků | Výsledek role | Rozhoduje sama (heslovitě) | Kandidát | Kapacita role |
|---|---|---|---|---|---|
| **Project lead** (jeden na živý titul nebo titul v produkci) | část 01 na úrovni projektu, denní priority 03 až 06 | titul podle plánu, problémy řešené, ne odkládané | denní priority, spory uvnitř projektu, žádost o outsourcing | `[DOPLNIT per titul]` | 20 až 30 % na titul navíc k odborné práci |
| **Tech lead** (napříč tituly) | 04 architektura, 07, 13, technická část 15 | udržitelný stack, žádný technický incident, který zastaví release | technické řešení bez dopadu na termín, pipeline, cloud v rámci rozpočtu | `[DOPLNIT]`, přirozeně Mirek jako nejseniornější programátor; rozhodnout, jestli chce nést roli a lidi, ne jen autoritu | 30 až 40 % |
| **Art lead DEV** | 05, zadání a kontrola pro DEV grafiky | art v čase a v rámci art directionu | vizuální směr v rámci art directionu, vracení práce, priorita uvnitř DEV grafiků | `[DOPLNIT]`; art direction napříč firmou drží dál Petr | 20 až 30 % |
| **Game design lead** | 03 napříč tituly, designová část 09 | hry dávají hráči smysl, retence a monetizace proti cíli | designové změny bez dopadu na monetizační model | `[DOPLNIT]` | 20 až 30 % |
| **QA lead** | 06, testovací část 10 | vždy se ví, v jakém stavu je build; kritická chyba neprojde | zastavit release | `[DOPLNIT, Akimo?]` | 20 % navíc k testování |
| **Publishing a LiveOps lead** | 10, 11, 12, 14 | vydané hry žijí a vydělávají, releasy jdou v termínu | provozní releasy a hotfixy, liveops kalendář, monetizační parametry uvnitř modelu, komunikace ke hráčům | `[DOPLNIT]` | 50 až 70 % |
| **B2B delivery lead** | 17, delivery část 08 | zakázky dodané v termínu se skutečnou marží proti odhadu | obsazení zakázky uvnitř plánu, komunikace s klientem, změny scope bez dopadu na marži | `[DOPLNIT]` | 30 až 50 % |
| **Data a analytika** (role, ne hned lead) | 18, 19 | jedna pravda o číslech pro celou firmu | technické řešení stacku, definice metrik po konzultaci s konzumenty | **nikdo, nábor** (kap. 6, mezera 1); do té doby Kuba + AI s termínem | 50 až 100 %, upřesní business case |

### 5.3 Kolik to je leadů

Sedm balíků plus jedna role k náboru. Reálně se sejdou u méně lidí, protože jeden člověk může nést dvě role, když má obě v soupisu s vlastní kapacitou. Odhad po doplnění jmen: **`[DOPLNIT]` lidí nese `[DOPLNIT]` rolí leada.**

Pojistka, kterou k tomu chci: **lead nesmí mít v součtu odbornou práci plus vedení nad 75 %.** Když vyjde víc, buď se mu sníží odborná práce, nebo balík rozdělíme. Jinak vyrobíme sedm přetížených lidí místo jednoho.

### 5.4 Co se se mnou stane po předání

```
Moje kapacita dnes (řádky 01, 02, 08, 09, 15, 16, 20, S1, S2):  [DOPLNIT %]
Po předání (01, 02, 09, 16, vedení leadů z 20):                  [DOPLNIT %]
```

Cíl je pod 75 %. Když to po předání nevyjde, není chyba v předání, ale v tom, že řádek 15 nebo 16 potřebuje vlastní odpověď ze žebříku, ne mě.

## 6. Moje tři největší mezery a odpověď ze žebříku

| # | Mezera | Řádek | Odpověď | Jméno | Termín | Co riskujeme, když se to nestane |
|---|---|---|---|---|---|---|
| 1 | **Data a analytika**: stack, eventy, definice metrik | 18, 19 | **najmout**; do té doby vědomě přechodný stav Kuba + AI **s koncem** | požadavek na headcount David, business case do 17. 9., nábor Operations | přechodný stav končí `[DOPLNIT, návrh 31. 12. 2026]` nebo nástupem, co nastane dřív | každý má vlastní definici retence a nikdo nemá pravdu; monetizace zůstává odhad |
| 2 | **Komunita a in-game komunikace** | 14 | **předat** na Publishing a LiveOps leada v **reaktivním režimu**, aktivní komunita vědomě neosazená | `[DOPLNIT]` | od 1. 10. | pomalejší odpovědi na support, žádný aktivní community management; přijatelné, dokud hodnocení na storech nespadne pod `[DOPLNIT]` |
| 3 | **B2B pipeline**: nikdo systematicky nenosí dealy | 16 | **vědomě neosadit** jako roli; nahradit podílovým systémem 5 + 5 % (delegační návrh kap. 8) a vyhodnotit po Q4 | David drží dohled | vyhodnocení 26. 11. | pipeline závisí na mém čase a na náhodě; když podíly nefungují, na 26. 11. se to mění na najmout nebo zrušit B2B jako oblast |

A jedna mezera, která není v tabulce, protože je řešená celou kap. 5: **já sám nad 75 %.** Odpověď je předat, jména jsou v 5.2.

## 7. Tři činnosti, které navrhuju zrušit

Povinný bod. Kandidáti z mého segmentu a z mého kalendáře, finální trojku vyberu po doplnění čísel:

| # | Kandidát | Co se stane, když to příští kvartál nikdo neudělá | Kdo to vrátí, když bude chybět |
|---|---|---|---|
| A | `[DOPLNIT]` Ruční sestavování provozních reportů a přehledů, které se čtou jen na poradě | nic; čísla jsou v dashboardech a v hubu | Publishing a LiveOps lead |
| B | `[DOPLNIT]` Udržování titulů bez výnosu a bez plánu (sunset místo údržby) | uvolní se kapacita 07, 10, 13; hráči dotčených titulů dostanou oznámení | David, jen s business casem |
| C | `[DOPLNIT]` Stavba vlastních nástrojů tam, kde existuje koupitelný nástroj (část řádku 15) | nástroj se koupí nebo se činnost nedělá; ušetří můj čas | Tech lead |
| D | `[DOPLNIT]` Synchro meetingy, které nahradí asynchronní denní priority (přesah do 17. 9.) | méně vyrušení, stav projektů v hubu | project leadi |

Vybrat tři, u každé napsat datum zrušení a jméno.

## 8. Moje hlasy k hraničním případům (kap. 4.5 společného podkladu)

Rozhoduje vlastník segmentu, kam činnost patří. Tohle je můj hlas, ne veto.

| Činnost | Můj hlas | Proč |
|---|---|---|
| Herní analytika | **P** | Výstup je rozhodnutí, ne produkt. Klasifikuju níž s pojmenovaným rizikem, jak doporučuje podklad. Ale musí mít vlastní kapacitu, ne zbytek po core, jinak je to trvale odložené. |
| UA a nákup médií | **C** (pro Marketing) | Je to druhá páka výnosu vedle produktu. Kdyby to dělal kdokoli jiný stejně dobře, přišli bychom o výhodu v ceně akvizice. |
| PR a brand | **S** | Efekt nepřímý a pomalý, publikační plán se dá zautomatizovat. Zbytek vědomě omezit. |
| Efektivizace a automatizace | **P** | Zvedá kapacitu ostatních, ale žádnou hru nedodá. A nedá se dělat, dokud Operations nesou 80 % operativy; nejdřív předat, pak automatizovat. |
| Komunita a in-game komunikace | **P** | Hráč to vnímá, ale v týdnech, ne ve dnech. Reaktivní režim stačí (kap. 6, mezera 2). |
| Nábor | **P** | Proces, ne výstup. Interní vlastník Operations, výkon Akimo, kapacita se musí do soupisu Operations napsat číslem. |
| Interní tooling a Wiki | **S** s výjimkou | Pravidlo kupovat, ne stavět. Výjimka: herní backend a nástroje, které přímo zrychlují vývoj titulů, jsou P a patří pod tech leada s business casem. |

## 9. Moje odpovědi na známé mezery (kap. 7 společného podkladu)

| # | Mezera | Moje odpověď |
|---|---|---|
| 01 | Data a analytika | najmout, přechodný stav s termínem (kap. 6, mezera 1) |
| 02 | Operativa Operations 80/20 | předat plus najmout: jeden operativní člověk do Operations je podle mě **první headcount, který má firma schválit**, protože bez něj nefunguje 03, 07 ani převzetí S2 a administrativního klastru z Produkce |
| 03 | Efektivizace a automatizace | vyřeší se až po 02, do té doby vědomě neosazená s rizikem |
| 04 | PR a brand | zautomatizovat publikační plán, zbytek vědomě omezit; Produkce dodává podklady v pevném rytmu (jeden update na titul za měsíc), ne na vyžádání |
| 05 | Komunita | předat v reaktivním režimu (kap. 6, mezera 2) |
| 06 | Grafická kapacita | rozhodnout jmenovitě na této poradě (kap. 10) |
| 07 | Nábor | doplnit kapacitu Akima do soupisu Operations číslem; pokud Akimo nese zároveň QA a release v Produkci, domovský segment a poměr času rozhodnout na této poradě |
| 08 | Zástupnost | jména u core řádků 01, 02, 10, 12 (kap. 3); zástup má mít přístupy a pásmo napsané, jinak je to jen jméno |

## 10. Grafici: jmenovité rozdělení DEV a MKT

Pravidlo z 20. 8. beze změny: konkrétní lidé pod konkrétní segment, uvnitř skupiny prioritizuje vlastník sám, cross práce po dohodě leadů obou stran, nikdy přes hlavu leada.

| Jméno | Segment | Poznámka |
|---|---|---|
| `[DOPLNIT]` | DEV | |
| `[DOPLNIT]` | DEV | |
| `[DOPLNIT]` | MKT | |
| `[DOPLNIT]` | MKT | |

Když počet nevychází celý (například tři grafici na dva segmenty), třetí je **jmenovitě domovský v jednom segmentu** s napsaným podílem pro druhý, ne "sdílený". Sdílený bez čísla je zpátky společný pool.

## 11. Pohled na celou firmu: typy rolí a počet lidí

Tohle je můj pokus odpovědět na otázku, kterou porada položí na konci: **kolik pozic firma potřebuje a kterých je potřeba víc.** Čísla doplní každý vlastník za svůj segment, tabulku a metodu (kap. 2.2) nabízím jako společný formát.

| Typ role | Segment | Potřeba (součet činností / 0,75) | Dnes lidí | Rozdíl | Návrh odpovědi |
|---|---|---|---|---|---|
| Programátor | Produkce (+ B2B) | `[DOPLNIT]` | `[DOPLNIT]` | | |
| Grafik DEV | Produkce | `[DOPLNIT]` | `[DOPLNIT]` | | rozdělení kap. 10 |
| Grafik MKT | Marketing | `[DOPLNIT]` | `[DOPLNIT]` | | rozdělení kap. 10 |
| Game designer | Produkce | `[DOPLNIT]` | `[DOPLNIT]` | | |
| QA | Produkce | `[DOPLNIT]` | `[DOPLNIT]` | | |
| Publishing a LiveOps | Produkce | `[DOPLNIT]` | dnes rozprostřené | | nová role, kap. 5.2 |
| Produkce a vedení (vlastník, project leadi) | Produkce | `[DOPLNIT]` | 1 + leadi | | kap. 5 |
| UA manažer | Marketing | Kuba doplní | `[DOPLNIT]` | | |
| Data a analytika | Produkce | 0,5 až 1,0 | **0** | **−0,5 až −1** | najmout |
| Operativa Operations (office, HR admin, finance admin) | Operations | DJ doplní | DJ na 80 % operativy | **−1** podle P4 | najmout, první v pořadí |
| Finance a řízení Operations | Operations | DJ doplní | DJ | | |
| Community a support | Produkce | 0,2 až 0,3 | 0 | | přidat jako druhou roli k Publishing a LiveOps |

**Co z toho čtu už teď:** firma s patnácti až šestnácti lidmi má dva prázdné typy rolí (data, operativa Operations) a jeden typ, který existuje jen jako práce navíc (publishing a liveops). To jsou tři odpovědi ze žebříku, které se dají napsat ještě před doplněním čísel: **najmout, najmout, předat.** Všechno ostatní ukáže součet.

## 12. Co potvrzuju z bodů "od Davida" (kompilát 20. 8., kap. 14)

| Bod | Odpověď |
|---|---|
| Produktový cloud, produktová compliance a licence assetů v Produkci | **Ano.** Cloud a compliance jsou řádky 11 a 13 pod Publishing a LiveOps a tech leadem. Licence assetů jako evidence a nákup do Operations (S2), odborná potřeba Produkce. |
| Odborný onboarding lidí v Produkci | **Ano**, řádek 20, po předání u leada, pod kterého člověk nastupuje. |
| Způsob předávání náborových a nákupních požadavků do Operations | Jeden kanál a jedna šablona v hubu: co, proč, rozpočet, termín, kdo rozhoduje o výběru. Bez šablony požadavek neexistuje. `[DOPLNIT: kdo šablonu postaví, návrh Operations do 17. 9.]` |
| David jako celkový vlastník firemního webu | **Ano** jako vlastník; výkon podle S1 (technika jeden člověk z Produkce jako druhá role, obsah MKT částí Marketing). |
| Které produktové oblasti vyžadují zástupnost | Řádky 01, 02 (plán a kapacita), 10 (release management a přístupy do konzolí), 12 (liveops běžících titulů), 13 (provoz a incidenty), 17 (běžící B2B zakázka). Jména v kap. 3. |

## 13. Otázky, které položím ostatním

1. **Všem:** souhlasíme s pravidlem z kap. 2.2, že počet lidí na typ role je součet kapacity dělený 0,75, a se třemi pásmy pro zbytek? Pokud ano, použijeme ho na všechny tři segmenty stejně.
2. **DJ:** je operativní člověk do Operations první headcount, který navrhneš? A vezme si S2 (licence, nástroje, device park) a administrativní klastr, který dnes nesu já? Jaký je podíl času Akima mezi náborem a Produkcí?
3. **Kuba:** sedí ti termín konce přechodného stavu u analytiky a to, že do náboru zůstáváš vykonavatelem s AI? A jmenovité rozdělení grafiků z kap. 10?
4. **Jirko:** jsi připravený na 3. 9. přijmout dva požadavky na headcount (operativa Operations, data) do business casu na 17. 9., ještě před rozpočtem 1. 10.? Bez toho nemá kvartál nanečisto co testovat.
5. **Všem:** kolik rolí leada unese jeden člověk, než je to titul a ne odpovědnost? Můj návrh: dvě, a součet odborné práce plus vedení pod 75 %.
6. **Mirek a Petr (mimo poradu, před ní):** chcete nést roli tech leada a art directora s lidmi a rozhodnutími, nebo zůstat autoritou v poradní radě? Obojí je legitimní, ale musí to být řečené, jinak jim ty role přiřadí porada bez nich.

## 14. Co si doplním před poradou

- [ ] Jména a kapacity do kap. 3 (řádky 03 až 07, 10 až 14, 17 až 19) a moje vlastní procenta.
- [ ] Součet Produkce (kap. 4) a moje kapacita před a po předání (kap. 5.4).
- [ ] Kandidáti na leady do 5.2, po rozhovoru s Mirkem a Petrem.
- [ ] Finální trojka ke zrušení (kap. 7) s daty.
- [ ] Jmenovité rozdělení grafiků (kap. 10).
- [ ] Termín konce přechodného stavu u analytiky (kap. 6, mezera 1).
- [ ] Reality check proti kalendáři za poslední dva týdny: kolik času reálně šlo do řádků 15 a 16.
- [ ] Ukázat návrh rolí aspoň jednomu leadovi mimo čtyřku před poradou (T61).
- [ ] Render `priprava-2026-09-03-david.html` po doplnění.
