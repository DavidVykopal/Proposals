# Moje příprava na poradu 3. 9. 2026 - David

> Osobní podklad. Společný neutrální podklad je `PRIPRAVA_2026-09-03_ROLE_A_CINNOSTI.md`,
> kompilát minulé porady `PORADA_2026-08-20_KOMPILAT.md`, stav témat `TRACKER_TEMAT.md`,
> moje předchozí příprava `PRIPRAVA_2026-08-20_DAVID.md`.
> Tenhle dokument je moje odpověď na úkol U02 za segment Produkce plus můj pohled na to,
> jaké role firma jako celek potřebuje a kolik lidí na ně reálně má.
> Stav: **v1.** Doplněná jména, kapacity a součty; zapracovaný výstup Operations (DJ),
> se kterým v zásadě souhlasím a píšu k němu svoje potvrzení a jednu výhradu (kap. 12).
> Kapacity jsou odhady na desítky procent, přesnost na 5 % doladíme na poradě.

---

## 0. Moje teze do porady

**Musíme zúžit firmu na hlavní činnosti.** Všechno ostatní se od toho odvíjí, v tomhle pořadí:

1. **Zúžit.** Vyjmenovat hlavní činnosti a mít odvahu říct, co mezi ně nepatří.
2. **Pokrýt.** Každá hlavní činnost má jméno, kapacitu a u core zástup. Ne "řeší se".
3. **Nepředimenzovat.** Žádná činnost nedostane víc kapacity ani víc rolí, než potřebuje.
   Role, pro kterou nemáme člověka ani obsah, se nezřizuje.
4. **Nevyhovující kapacitu řešit třemi tahy: přeřadit, zautomatizovat, najmout.**
5. **Když nejde ani jedno z toho, není to důležitá činnost.** Škrtnout a zapsat, kdo ji
   vrátí, kdyby chyběla.

Je to totéž, co žebřík pěti odpovědí ze společného podkladu, jen řečené jako filtr: zrušení
není pátá možnost na konci, je to závěr, ke kterému se dojde vždycky, když činnost neobstojí
v bodech 2 až 4.

**A cíl, ke kterému to celé míří: přesunout pozornost z množství práce a odsezených hodin
na kvalitu odvedené práce a přidanou hodnotu.** Soupis činností není nástroj na měření
vytížení, je to nástroj na to, aby každý mohl dělat míň věcí pořádně. Navazuje na man-days
místo man-hours a kognitivní limit 4 až 6 hodin z porady 6. 8.

**A jedno pravidlo výšky letu:** porada řeší **core a management role**, ne grassroot
odpovědnosti. Že grafik a developer společně drží čistý git tree a ukládají assety, kam
patří, je věc popisu jednotlivých rolí a doladí se mezi poradami. Porada rozhoduje o patro
výš: kdo odpovídá za to, že git a pipeline vůbec jedou (tech autorita projektu), kdo za to,
že build jde ven (publishing), kdo za kvalitu (QA lead).

## 1. Co si chci z porady odnést

| # | Co | Proč to nejde odložit |
|---|---|---|
| 1 | **Soupis činností Produkce jako schválený základ, ze kterého se odvozují role** | Když se role nakreslí dřív než činnosti, vzniknou podle titulů a zbytek zůstane u mě. Přesně z toho se dostáváme. |
| 2 | **Rozhodnutí o rolích uvnitř Produkce** (kap. 5): co se formalizuje, co se vědomě nezřizuje, kdo co nese | Nesu sedm oblastí a jsem na cca 150 %. Návrh nepřidává management, zužuje ho: dvě role se vědomě nezřizují. |
| 3 | **Součet kapacity za firmu a u každé mezery právě jedna odpověď** | Číslo vychází: schodek zhruba 1 až 2 úvazky, dnes schovaný v přetížení dvou lidí (já a Akimo) a v neosazených činnostech. |
| 4 | **Tři personální tahy jako balík**: datový analytik/tester, OPS & AI programátor, part-time externista na kanceláře | Všechny tři vzešly nezávisle z mojí přípravy i z přípravy Operations. Jednotlivě jsou to prosby, dohromady je to plán, jak schodek zaplatit. |
| 5 | **Jmenovité rozdělení grafiků DEV a MKT** (T11) a **termín konce přechodného stavu u analytiky** (T16) | Obě věci se z 20. 8. přenesly bez rozhodnutí. Potřetí je nechci přenášet. |

## 2. Přiznaná zaujatost

- **Produkce je největší segment** a většina rolí z téhle porady vznikne v ní. Návrh mi uleví. Zároveň je to přesně to, co po mně porada chce, takže to nezastírám.
- **Chci předávat, ne sbírat.** Ze sedmi oblastí si nechávám dvě. Všechno ostatní má v tomhle dokumentu jméno nebo odpověď.
- **Metodu jsem psal já,** proto ji aplikuju nejpřísněji na sebe: největší škrt (kap. 7) je z mého vlastního času a jsem jediný, kdo v soupisu přiznává 150 %.
- **Vlastní tooling.** Odhadem čtvrtina mého času jde do interních nástrojů a AI (hub, herní backend, AMA bot, extrakce playables). Je to činnost, která v žádné kartě z 20. 8. nebyla. Dávám ji do soupisu a rovnou na ni aplikuju vlastní filtr: část škrtám, zbytek má převzít OPS & AI programátor z návrhu Operations.

## 3. Jak čtu zadání: role z činností, ne naopak

### 3.1 Pravidla ze společného podkladu, která přebírám

- Role je **balík činností s jedním výsledkem a jedním vlastníkem.**
- Role, kterou nese víc lidí, není role, je to tým a potřebuje leada.
- Jeden člověk může nést víc rolí, každá má vlastní výsledek a vlastní kapacitu v soupisu.
- Plánujeme na **75 % kapacity.** Kdo má v soupisu činnosti za víc než 75 % úvazku, je přetížený.

### 3.2 Co přidávám: od kapacity k počtu lidí

Otázka "potřebujeme víc programátorů" se nedá zodpovědět bez pravidla. Navrhuju tohle:

1. **Sečti kapacitu všech činností stejného typu** napříč segmenty.
2. **Vyděl 0,75.** Výsledek je počet celých úvazků, které ten typ role potřebuje.
3. **Porovnej s počtem lidí, kteří tu roli dnes nesou.** Rozdíl je mezera nebo přebytek.
4. **Zbytek pod celé číslo:**

| Zbytek | Odpověď |
|---|---|
| do 0,3 úvazku | přidá se k existující roli jako druhá role s vlastním cílem |
| 0,3 až 0,7 úvazku | sdílený člověk mezi segmenty, částečný úvazek nebo externista s interním vlastníkem |
| nad 0,7 úvazku | celý člověk, tedy business case a nábor |

5. **Vedení se počítá zvlášť.** U leada 3 až 5 lidí zhruba 20 až 30 % úvazku. Když se to nezapočítá, lead je na papíře na 100 % a v realitě na 130 %.

### 3.3 Lead, vykonavatel a odborná autorita

Tři různé věci, které se v soupisu nesmí smíchat:

- **Lead** nese balík činností **a rozhodovací pásmo**. Rozhoduje bez eskalace do napsaného limitu, vede lidi, ručí za výsledek balíku.
- **Vykonavatel** nese činnost, pásmo má jen na způsob provedení.
- **Odborná autorita** drží standard, review a mentoring v oboru, ale nevede lidi a neručí za dodání. Tohle je role pro Mirka (tech) a Peka (art): jsou to mistři oboru, ne manažeři, a je poctivější to napsat, než jim rozdat lead role, které nebudou dělat. Autorita je legitimní a placená role, jen jiná.

Z toho plyne: **lead není titul za seniority** a seniorita nikoho k vedení lidí nezavazuje.

## 4. Soupis činností Produkce (šablona A)

Segment: **Produkce** · Vlastník: **David** · Účel: hry vznikají, vycházejí, žijí a zaplatí se.

Lidé v segmentu (10, z toho Akimo cca 70 % času): David, Akimo (Martin V.), Hutis (Jakub H.), Aldy (David B.), Karlík (Karel K.), Čoud (Jan Š.), Milan, David C., Mirek, Peko. Kapacity jsou odhad v % úvazku, "H" hlavní práce, "N" navíc. Vrstva: **C** core, **P** podstatné, **S** support.

| # | Činnost | Vrstva | Kdo | Kap. | H/N | Zástup | Výsledek / číslo |
|---|---|---|---|---|---|---|---|
| 01 | **Plán produkce a roadmapa titulů**: sprinty, milníky, priority mezi projekty | C | David | 20 | H | Aldy (návrh) | milníky v termínu, počet přeplánování za kvartál |
| 02 | **Kapacitní plánování a obsazení projektů** | C | David | 10 | H | Aldy (návrh) | utilizace 70 až 80 %, nikdo nad 100 % |
| 03 | **Herní design a ekonomika titulů** | C | Aldy 40, Karlík 40 | 80 | H | vzájemně | retence D1/D7 a ARPDAU proti cíli |
| 04 | **Programování a technická architektura** | C | Mirek 50, Čoud 75, Milan 75, Hutis 35 | 235 | H | vzájemně | dodané feature za sprint, crash-free rate |
| 05 | **Herní art a UI** (DEV grafici) | C | David C. 75, Peko 60, Aldy 10, Karlík 10 | 155 | H | vzájemně | art podle plánu sprintu, počet vrácení |
| 06 | **QA a release readiness buildů** | C | Hutis 40, Akimo 10 | 50 | H | David | kritické chyby v produkci po releasu: cíl 0 |
| 07 | **Technický dluh, build pipeline a engine** | P | Mirek | 10 | N | Čoud | doba buildu, blokující technické incidenty |
| 08 | **Outsourcing a externí dodávky do vývoje** | P | David | 5 | N | nevyžaduje | dodávky převzaté na první pokus |
| 09 | **R&D: prototypy a podklad pro greenlight**, max 2 sprinty | C | David + tým dle konceptu | 15 | N | Aldy/Karlík | rozhodnutí do 2 sprintů, ověřené koncepty za kvartál |
| 10 | **Release management a platformy**: store konzole, review, game setup | C | Akimo | 20 | H | David | releasy v termínu, zamítnutí review: cíl 0 |
| 11 | **Produktová compliance**: privacy, rating, ATT (T57) | P | Akimo | 5 | N | David | žádný incident na storech, audit 1× za kvartál |
| 12 | **LiveOps vydaných titulů**: eventy, kalendář, provozní monetizace | C | Akimo | 20 | H | David (návrh: přejde na Hutise) | výnos živých titulů proti plánu, kalendář 4 týdny dopředu |
| 13 | **Provoz produktů**: servery, produktový cloud, monitoring, incidenty | P | Akimo | 10 | N | David | dostupnost, doba řešení incidentu |
| 14 | **Komunita hráčů, in-game komunikace a support** | P | Akimo (reaktivně) | 5 | N | nevyžaduje | doba odpovědi, hodnocení na storech |
| 15 | **Interní tooling, herní backend a AI nástroje**: hub, backend platforma, AMA bot, extrakce playables | P | David | 25 | N | **nikdo** (návrh: Hutis + runbook) | ušetřené hodiny za měsíc, každý nástroj s business casem |
| 16 | **B2B pipeline a nabídky**: scoping, pricing podle tarifů, dojednání | C | David | 10 | N | nevyžaduje | marže nabídek, počet dealů v pipeline |
| 17 | **B2B delivery**: playables a externí vývoj, vedení zakázky, klient | C | David | 25 | N | Čoud (návrh) | skutečná marže proti odhadu, dodávky v termínu |
| 18 | **Datový stack, eventy v buildech a definice metrik** | P | **nikdo formálně**, fakticky Kuba + AI | 10 | N | nevyžaduje | jedna definice retence pro firmu, pokrytí eventy |
| 19 | **Herní analytika**: čtení dat, doporučení k ladění a monetizaci | P | Kuba + AI, David 5 | 15 | N | nevyžaduje | doporučení za sprint promítnutá do buildu |
| 20 | **Vedení lidí v Produkci**: 1:1, cíle, hodnocení, onboarding | P | David | 10 | H | nevyžaduje | 1:1 v rytmu, cíle první den měsíce |

Mimo tabulku **support** a mimo segment:

| # | Činnost | Vrstva | Kdo | Kap. | Návrh |
|---|---|---|---|---|---|
| S1 | Firemní web a CPI/produktové stránky (T56) | S | David | 5 | vlastnictví ano, výkon: technika jako druhá role v Produkci, obsah MKT částí Marketing |
| S2 | Licence assetů, vývojové nástroje, device park | S | David | 5 | předat do Operations jako evidenci a nákup, odbornou potřebu určuje Produkce |
| S3 | AI vzdělávání firmy (s Operations, výstup DJ) | P | Břenek + David | 10 | potvrzuju svých 10 % jako vědomou položku svého úvazku |

**Co z tabulky vyplývá:**

- **Já: součet cca 145 až 150 %.** Rovnoměrně rozprostřené, na management, plánování a people management (01, 02, 20) zbývá dohromady 40 bodů ze 150, tedy nejmíň. Přesně obráceně, než co má vlastník segmentu dělat. Stejný problém, jaký Operations popisují u DJ (80/20), jen v jiném poměru.
- **Akimo: součet cca 100 %** (70 Produkce + 30 Operations). Druhý přetížený člověk segmentu, a to mu příprava Operations přidává lead HR a zástup kanceláří.
- **Tři činnosti mají v poli kdo "nikdo" nebo provizorium:** 14 (jen reaktivně), 15 (bez zástupu), 18 (Kuba + AI bez formy). To jsou mezery v kap. 6.
- Zástupy u core jsou návrhy a z velké části vedou na mě. To je slabé místo: zástup, který je sám na 150 %, není zástup. Řeší se to až tahy z kap. 6.

## 5. Návrh rolí uvnitř Produkce: formalizovat málo, škrtnout zbytek

Odvozeno ze soupisu. Proti verzi v0 jsem návrh **zúžil**: dvě role se vědomě nezřizují, dvě se jen formalizují tam, kde už fakticky existují. Rozhodovací pásma heslovitě, částky patří na 17. 9.

### 5.1 Co si nechávám

| Oblast | Řádky | Proč |
|---|---|---|
| **Vývoj a portfolio** | 01, 02, 09, 20 | Plán, kapacita, greenlight podklad a vedení. Práce vlastníka segmentu, nepředává se. Cíl: zvednout podíl 20 z 10 na 20 %. |
| **B2B** | 16, 17 | B2B by měla být vlastní pozice, ale není komu ji dát, takže ji držím já. Delivery budu postupně delegovat po zakázkách (první kandidát: vývojová část na Čouda/Milana), pipeline a pricing si nechávám. |

### 5.2 Role, které se formalizují (už fakticky existují)

| Role | Kdo | Balík | Rozhoduje sama | Poznámka |
|---|---|---|---|---|
| **Project lead** | Aldy a Karlík, každý na svých titulech | denní priority, 03 na projektu, koordinace 04 a 05 | denní priority, spory v projektu, žádost o outsourcing | dnes to už dělají, dostanou napsané pásmo; design leadership je součást role, samostatný GD lead se nezřizuje |
| **Publishing a LiveOps lead** | Akimo | 10, 11, 12, 13, 14 | provozní releasy a hotfixy, liveops kalendář, monetizační parametry uvnitř modelu, komunikace ke hráčům | fakticky jeho dnešní hlavní práce (publishing manager); podmínky v kap. 5.5 |
| **QA lead** | Hutis | 06 | testplán, evidence, **zastavit release** | přebírá ownership QA od Akima (odlehčení), Akimo si nechává release gate na 10 |

### 5.3 Role, které se vědomě nezřizují

| Role | Proč ne | Jak se to pokryje |
|---|---|---|
| **Art lead DEV** | Peko je mistr oboru, ne manažer; jiného kandidáta nemáme a roli bez člověka nezřizujeme | zadání pro DEV grafiky jde přes project leady (Aldy a Karlík umí art), Peko drží kvalitu jako **odborná autorita** (standard, review, mentoring) |
| **GD lead napříč** | design leadership už je v roli project leada, samostatná role by byla titul | Aldy a Karlík na svých titulech, spory arbitruje David |

### 5.4 Role k rozhodnutí na poradě

| Role | Varianty | Můj návrh |
|---|---|---|
| **Tech lead napříč tituly** (07, technická část 15, arbitr 04) | a) Čoud jako tech lead (senior, ale remote a je třeba se ho zeptat) · b) vědomě neosadit: technická rozhodnutí per projekt, Mirek jako odborná autorita a arbitr | začít variantou b), po zapracování Milana se vrátit k a); Mirek dostane napsanou roli autority, ne leada |
| **Data a analytika** (18, 19) | nábor | **najmout datového analytika/testera**, shodná priorita s Operations; profil s testerskou kapacitou pomůže i QA; do nástupu Kuba + AI s koncem 31. 12. 2026 |

### 5.5 Akimo: domovský segment a podmínky

Potvrzuju **scénář A**: domovský segment **Produkce** (publishing manager), do Operations cca **25 až 30 %** jako lead HR administrativy. K tomu dvě podmínky, jinak ho rozpůlíme:

1. **Kanceláře jdou na part-time externistu.** Akimo může být lead a zástup jen do jeho nástupu, ne trvalý vykonavatel.
2. **QA ownership přechází na Hutise** (5.2). Akimo si nechává release gate.

Po obou tazích je Akimo na cca 85 až 90 a s dalším zúžením komunit a reportů (kap. 7) se dostane k 75.

### 5.6 Co se stane se mnou

```
Dnes:                                   cca 150 %
Po tazích z porady:
  odchází: 15 tooling na OPS & AI programátora (zbytek po škrtu z kap. 7),
           17 delivery postupně (první zakázky cca -10), S1 a S2, 08 na project leady
  roste:   20 vedení z 10 na 20, 02 zůstává
Cíl do konce Q4:                        cca 85 až 95 %, po plné delegaci delivery pod 75 %
```

Říkám to natvrdo: **pod 75 % se nedostanu okamžitě ani rozhodnutím porady.** Dostanu se tam kombinací nájmu OPS & AI programátora, delegace B2B delivery a škrtů. Do té doby jsem vědomě přetížený s pojmenovaným rizikem: trpí řádky 01, 02 a 20, tedy přesně to, co má vlastník dělat.

## 6. Mezery a přetížení: u každého právě jedna odpověď

| # | Mezera | Řádky | Odpověď | Jméno a termín | Riziko, když se to nestane |
|---|---|---|---|---|---|
| 1 | **Data a analytika** | 18, 19 | **najmout** datového analytika/testera (priorita shodná s Operations); do té doby vědomě přechodný stav Kuba + AI | business case David do 17. 9., nábor Operations; přechodný stav končí 31. 12. 2026 nebo nástupem | každý má vlastní definici retence; monetizace zůstává odhad |
| 2 | **Moje přetížení 150 %** | 01 až 20 | **přeřadit + najmout**: kap. 5 + OPS & AI programátor přebírá tooling | tahy z 5.6, vyhodnocení 26. 11. | trpí plán, kapacita a vedení lidí, tedy jádro segmentu |
| 3 | **Akimo 100 %** | 06, 10 až 14 + Operations | **přeřadit**: QA na Hutise, kanceláře na externistu | 5.5, do 1. 10. | publishing a liveops, dvě core činnosti, spadnou první |
| 4 | **Komunita a in-game komunikace** | 14 | **vědomě jen reaktivně** (Akimo), aktivní komunita neosazená | potvrdit na poradě, revize při poklesu hodnocení na storech | žádný aktivní community management; přijatelné a pojmenované |
| 5 | **B2B pipeline** | 16 | **držím já** jako vlastní pozici; podílový systém 5 + 5 % jako druhý zdroj dealů | vyhodnocení 26. 11.: pokud pipeline stojí jen na mně, na 2027 zvážit nábor | pipeline závisí na mém čase; když podíly nezaberou, je to nejdražší mezera na najmutí |
| 6 | **NoxHub bez zástupu** | 15 | **jmenovat zástup + runbook** (výstup Operations) | navrhuju **Hutise** (já jsem už teď single point na moc věcech), runbook do 1. 10. | výpadek hubu zastaví schvalování plateb a feedback pipeline |

**Pravidlo, které chci k přetížení odsouhlasit:** jakmile soupisy ukážou, kdo dělá co a kdo
je kde přetížený, u každého přetíženého se **konkrétně stanoví, co s tím** (přeřadit,
zautomatizovat, najmout, škrtnout), se jménem a termínem. A tam, kde se udělat nedá nic,
se přetížení **kompenzuje penězi nebo jiným bonusem**, vědomě a napsaně, ne mlčky.
Navazuje na zásadu delegačního návrhu, že kdo se ukáže jako výrazně přetížený, má být
odměněn víc. Konkrétní částky patří na 15. 10., pravidlo chci odsouhlasit teď.

## 7. Co ruším (povinné tři)

Všechny tři z mého segmentu a z mého času, s datem a se jménem, kdo to vrátí:

| # | Ruším | Od kdy | Co se stane | Kdo to vrátí |
|---|---|---|---|---|
| 1 | **Stavbu nástrojů bez rozvahy build vs. buy.** Před každým novým interním toolem se zváží, jestli na trhu neexistuje hotové řešení, a rozhodne se podle toho, co vyjde jednodušeji, sedí nám líp nebo je výhodnější; vlastní integrované řešení je legitimní výsledek té rozvahy. K rozhodnutí patří business case (výchozí stav, metrika, náklad, vyhodnocení). Škrtám stavění bez rozvahy a bez business casu; řádek 15 se tím zmenší ještě před předáním. | ihned | část mého času z 25 se vrací do 01 a 20 | OPS & AI programátor, který rozvahu dělá u každého požadavku |
| 2 | **Ruční reporty a přehledy, které umí vygenerovat hub.** Provozní čísla se čtou v hubu, ne v dokumentech skládaných před poradou. | 1. 10. | uvolní Akima i mě | Akimo, jen pokud konkrétní číslo v hubu chybí |
| 3 | **Synchro meetingy nahraditelné asynchronními prioritami v hubu.** Stav projektů se hlásí async, meeting zůstává jen tam, kde se rozhoduje. | 1. 10. | méně vyrušení pro celý tým; navazuje na redesign schůzek 17. 9. | project leadi |

A čtvrtý námět, který nepatří mně, ale poradě: **sunset titulů bez výnosu a bez plánu.** Uvolnil by kapacitu v 07, 10 a 13, ale je to portfolio rozhodnutí (CEO). Navrhuju otevřít 17. 9.

## 8. Moje hlasy k hraničním případům (kap. 4.5 společného podkladu)

Rozhoduje vlastník segmentu, kam činnost patří. Tohle je můj hlas, ne veto.

| Činnost | Můj hlas | Proč |
|---|---|---|
| Herní analytika | **P** | Výstup je rozhodnutí, ne produkt. Klasifikuju níž s pojmenovaným rizikem. Ale musí mít vlastní kapacitu, ne zbytek po core. |
| UA a nákup médií | **C** (pro Marketing) | Druhá páka výnosu vedle produktu. |
| PR a brand | **S** | Efekt nepřímý a pomalý, publikační plán zautomatizovat, zbytek vědomě omezit. |
| Efektivizace a automatizace | **P** | Zvedá kapacitu ostatních, ale žádnou hru nedodá. Souhlasím s Operations, že roadmapa automatizací je záměr, ne rozhodnutí: každá jednotlivě s business casem, žádný program. |
| Komunita a in-game komunikace | **P** | Hráč to vnímá v týdnech, ne ve dnech. Reaktivní režim stačí (kap. 6, mezera 4). |
| Nábor | **P** | Proces, ne výstup. Vlastník Operations, výkon Akimo, kapacita napsaná číslem v soupisu Operations. |
| Interní tooling a Wiki | **S** s výjimkou | Pravidlo build vs. buy (kap. 7, škrt 1): před stavbou zvážit trh a rozhodnout podle jednoduchosti, fitu a výhodnosti, ne dogma jedním ani druhým směrem. Výjimka: herní backend a nástroje přímo zrychlující vývoj jsou P, s business casem. |

## 9. Moje odpovědi na známé mezery (kap. 7 společného podkladu)

| # | Mezera | Moje odpověď |
|---|---|---|
| 01 | Data a analytika | najmout, kap. 6 mezera 1 |
| 02 | Operativa Operations 80/20 | souhlasím s tahy DJ: HR na Akima (s podmínkami 5.5), kanceláře na externistu, smlouvy na Ambroze; OPS & AI programátor je pak investice, ne záplata |
| 03 | Efektivizace a automatizace | po vyřešení 02; jednotlivé automatizace s business casem, ne roadmapa |
| 04 | PR a brand | zautomatizovat publikační plán; Produkce dodává podklady v pevném rytmu (jeden update na titul za měsíc), ne na vyžádání |
| 05 | Komunita | vědomě reaktivně, kap. 6 mezera 4 |
| 06 | Grafická kapacita | jmenovitě rozhodnout dnes, kap. 10 |
| 07 | Nábor | kapacita Akima na nábor napsaná v soupisu Operations; domovský segment potvrzuju: Produkce (5.5) |
| 08 | Zástupnost | jména v soupisu (kap. 4); přebírám standard Operations: **zástup činnost 1× za kvartál reálně vykoná**, jinak je to jen jméno v tabulce |

## 10. Grafici: jmenovité rozdělení DEV a MKT

Pravidlo z 20. 8. beze změny: konkrétní lidé pod konkrétní segment, uvnitř skupiny prioritizuje vlastník, cross práce po dohodě leadů obou stran, nikdy přes hlavu leada.

| Jméno | Segment | Poznámka |
|---|---|---|
| David C. | **DEV** | junior 2D artist, plně herní art |
| Peko | **DEV** | domovsky DEV art + odborná autorita art directionu; výpomoc MKT po dohodě leadů, orientačně do 10 % |
| Aldy, Karlík | **DEV** | art kapacita uvnitř vlastních projektů (cca 10 % každý), nejde o poolové grafiky |
| Ondra | **MKT** | marketing artist a ASO |
| Ruda | **MKT** | videomaker a motion graphic |

Lichý člověk je Peko: domovský segment DEV s napsaným podílem pro MKT, ne "sdílený". Sdílený bez čísla je zpátky společný pool.

## 11. Pohled na celou firmu: typy rolí a počet lidí

Odpověď na otázku, **kterých pozic je potřeba víc.** Dostupná kapacita firmy: 16 lidí × 0,75 = **12,0 plánovatelných úvazků**. Součet činností podle mého soupisu, výstupu Operations a odhadu za Marketing vychází orientačně **12,5 až 13** a neobsahuje neosazené činnosti (data, aktivní komunita, efektivizace). **Reálný schodek je 1,5 až 2 úvazky** a dnes je schovaný v přetížení dvou lidí a v mlčení o neosazeném.

| Typ role | Segment | Dnes lidí (úvazků) | Stav | Odpověď |
|---|---|---|---|---|
| Programátor | Produkce | Mirek, Čoud, Milan, část Hutise (cca 3,3) | drží, Milan v onboardingu | po zapracování Milana OK; B2B delivery si z ní ukusuje, hlídat v kapacitním plánu |
| Grafik DEV | Produkce | David C., Peko (cca 1,8) | drží | rozdělení kap. 10 |
| Grafik MKT | Marketing | Ondra, Ruda (2,0) | Kuba doplní potřebu | |
| Game designer + project lead | Produkce | Aldy, Karlík (2,0) | na limitu (design + lead + art) | nepřidávat jim nic dalšího |
| QA | Produkce | Hutis 0,4 + Akimo gate | tenké | QA lead Hutis; testerská kapacita přijde s datovým analytikem/testerem |
| Publishing a LiveOps | Produkce | Akimo 0,7 | přetížený vč. Operations | přeřadit (5.5) |
| Vlastník Produkce | Produkce | David 1,5 | přetížený | kap. 5.6 |
| UA | Marketing | Richi + Kuba | Kuba doplní | |
| Data a analytika | Produkce | **0** | prázdné | **najmout: datový analytik/tester** (priorita 1, shodně s Operations) |
| OPS & AI programátor | Operations | **0** (dnes David 0,25 + DJ) | skryté v přetížení | **najmout jako investici** (priorita 2); přebírá hub a tooling |
| Operativa Operations | Operations | DJ 0,73, díry | 80/20 naopak | **externista part-time kanceláře** (priorita 3) + HR na Akima |
| Community a support | Produkce | Akimo reaktivně 0,05 | vědomě minimální | nepřidávat, revize při poklesu hodnocení |

**Balík na schválení: dva nábory a jeden externista.** Datový analytik/tester, OPS & AI programátor, part-time externista na kanceláře. Všechno ostatní se řeší přeřazením a škrty, žádná další pozice se nezřizuje. To je celá moje odpověď na otázku "je nějakých pozic potřeba více": ano, těchhle tří, a žádné jiné.

## 12. Co potvrzuji z výstupu Operations (a jedna výhrada)

| Bod DJ | Moje odpověď |
|---|---|
| Domovský segment Akima, scénář A/B | **Scénář A, domovský segment Produkce**, 25 až 30 % do Operations, lead HR ano. Podmínky v 5.5: kanceláře jen do nástupu externisty, QA přechází na Hutise. |
| Lead role Akima pro HR a kanceláře | HR ano. **Kanceláře výhrada:** lead a zástup jen dočasně; Akimo je na 100 % a tohle je přesně činnost "navíc", která spadne první. |
| 10 % mého úvazku na AI vzdělávání | **Potvrzuji** a mám to v soupisu jako S3, tedy vědomě, ne navíc potají. |
| NoxHub zástup David nebo Hutis | **Hutis** + runbook. Já jsem už teď single point na příliš mnoha místech, zástup přes dalšího přetíženého nic neřeší. |
| Odpovědnost segmentů za vlastní data, hranice efektivizace, organické tooly bez režie Operations | Ano, s pravidlem: organický tool žije bez režie Operations, dokud ho používá jen segment, který ho postavil. Jakmile ho používají dva segmenty, dostane vlastníka, business case a zástup. |
| Standard zástupů: zástup činnost 1× za kvartál reálně vykoná | **Přebírám** pro všechny zástupy v kap. 4. |
| Priorita náboru datový analytik/tester | **Shoda**, u mě priorita 1 (kap. 11). |
| Smlouvy na Ambroze, platby self-service v hubu | Souhlas, bez připomínek. |

## 13. Co potvrzuji z bodů "od Davida" (kompilát 20. 8., kap. 14)

| Bod | Odpověď |
|---|---|
| Produktový cloud, compliance a licence assetů v Produkci | **Ano.** Cloud a compliance řádky 11 a 13 (Akimo), licence jako evidence a nákup do Operations (S2), odborná potřeba Produkce. |
| Odborný onboarding lidí v Produkci | **Ano**, řádek 20, u leada, pod kterého člověk nastupuje. |
| Předávání náborových a nákupních požadavků do Operations | Jeden kanál a jedna šablona v hubu: co, proč, rozpočet, termín, kdo vybírá. Bez šablony požadavek neexistuje. Postaví Operations do 17. 9. |
| David celkový vlastník firemního webu | **Ano** jako vlastník; výkon podle S1. |
| Které produktové oblasti vyžadují zástupnost | Řádky 01, 02, 06, 10, 12, 13, 15 a běžící B2B zakázka. Jména v soupisu, standard 1× za kvartál. |

## 14. Otázky, které položím ostatním

1. **Všem:** souhlasíme s pravidlem z kap. 3.2 (počet lidí = kapacita / 0,75 a tři pásma pro zbytek)? Pokud ano, platí pro všechny segmenty stejně.
2. **Jirko:** bereš balík z kap. 11 (datový analytik/tester, OPS & AI programátor, externista kanceláře) jako tři business casy do 17. 9.? Bez nich nemá kvartál nanečisto co testovat, protože schodek zůstane schovaný ve mně a v Akimovi.
3. **Kubo:** sedí ti termín konce přechodného stavu u analytiky 31. 12. 2026 a role vykonavatele s AI do té doby? A jmenovité rozdělení grafiků z kap. 10 včetně Pekova limitu 10 %?
4. **DJ:** sedí ti moje podmínky ke scénáři A (5.5)? A převezme Operations S2 (licence, nástroje, devices) jako evidenci a nákup?
5. **Všem:** souhlasíme, že role odborné autority (Mirek tech, Peko art) je legitimní placená role bez vedení lidí, a nebudeme jim lead role nutit? Chci to mít zapsané, jinak to za půl roku někdo otevře jako "proč Mirek nikoho nevede".
6. **Všem:** kolik rolí leada unese jeden člověk? Můj návrh: dvě, a součet odborné práce plus vedení pod 75 %.

## 15. Zbývá před poradou

- [ ] Projít soupis (kap. 4) s Aldym nebo Karlíkem jako validace mimo čtyřku (T61).
- [ ] Reality check mých procent proti kalendáři za poslední dva týdny, hlavně řádky 15 a 17.
- [ ] Render `priprava-2026-09-03-david.html`.
