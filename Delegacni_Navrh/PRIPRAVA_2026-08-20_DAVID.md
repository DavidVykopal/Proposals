# Moje příprava na poradu 20. 8. 2026 - David

> Osobní podklad. Společný neutrální podklad je `PRIPRAVA_2026-08-20_ODDELENI.md`, kompilát
> minulé porady `PORADA_2026-08-06_KOMPILAT.md`, delegační návrh `DELEGACNI_NAVRH.md` (iterace 05).
> Tenhle dokument je moje verze mapy, moje odpovědi na sporné zóny a moje podmínky.
> Stav: **v4. Rozpočet u každého oddělení (kap. 2.1), grafici rozdělení na DEV a MKT s přípustnou
> cross prací po dohodě leadů, B2B kritérium je marže 100 % místo stropu v člověkodnech, hranice
> experimentu 2 sprinty (4 týdny), metodika pro nastavení rozpočtů a interních tarifů (kap. 10).**

---

## 0. Co si chci z porady odnést

Čtyři body. Žádný z nich není přání, všechny čtyři jsou podmínky, bez kterých nemá smysl pokračovat na meet 2.

| # | Co | Proč to nejde odložit |
|---|---|---|
| 1 | **Rozhodnutí, že produkce se rozřezává** | Dokud je "produkce = vše ostatní", není co delegovat. Zbytková kategorie nemá hranici, a co nemá hranici, to se nedá předat. |
| 2 | **Rozhodovací pásmo černé na bílém** | U každé krabičky co rozhoduje vlastník sám a kde začínají jednosměrné dveře. Bez toho je mapa jen obrázek. |
| 3 | **Kapacitní pravidla** | Rozdělení grafiků na DEV a MKT a kritérium marže na B2B. Nejmenší možný test celého modelu, vyhodnotitelný za 14 dní. |
| 4 | **Přístup k číslům včetně výplat** | Rozhoduje se až na meetu 2, ale 20. 8. má zaznít jako podmínka. Krabička s rozpočtem, jejíž vlastník nevidí čísla, neprojde ani vlastním testem. |

Plus jeden bod, který porada dostane ode mě: **pravidlo, podle kterého poznáme, co je oddělení a co je jen agenda** (kap. 2). Navrhuju ho odsouhlasit jako první věc, jinak se o mapě budeme bavit každý s jinou definicí slova oddělení.

## 1. Přiznaná zaujatost

Do porady jdu jako člověk, který navrhuje pravidla pro celou firmu, a zároveň jako člověk, kterého se ta pravidla nejvíc týkají. Aby to nemusel nikdo hádat, dávám svůj zájem na stůl hned:

- **Nechci zmenšit svoji sféru.** Rozsah, který dnes nesu, je podle mě správně poskládaný. Problém není jeho velikost, ale to, že k němu nemám data, rozpočtové pásmo a napsané hranice.
- **Chci k sobě přibrat dvě věci, které dnes nikdo nedrží celé:** data a analytiku a komunitu a store. Argument je v kap. 3.5 a je věcný, ne majetnický. Když ho někdo vyvrátí lepším, ustoupím.
- **Chci celý proces náboru napříč firmou.** Nábor je kapacitní rozhodnutí a kapacitu plánuje produkce.
- **Za to shazuju čtyři věci** (kap. 7). Bez toho by to byl jen růst revíru a model by se mi rozpadl pod rukama.

Pravidla, která navrhuju, mají platit na mě stejně jako na ostatní. Když test oddělení něco z mojí sféry vyhodí, vyhodím to taky.

## 2. Test oddělení

Návrh pravidla, které chci odsouhlasit na začátku bloku o mapě. Oblast je **oddělení**, když splní všechny čtyři body. Když splní míň, je to **agenda uvnitř** jiného oddělení a nekreslíme jí vlastní krabičku.

| # | Kritérium | Kontrolní otázka |
|---|---|---|
| 1 | **Jeden vlastník** | Umíme napsat jednu roli, ne dvě? |
| 2 | **Vlastní rozpočet nebo jasná nákladová linka** | Z čeho se platí to, co se v oblasti dělá? |
| 3 | **Vlastní výsledek** | Jedno číslo nebo jeden stav, podle kterého se pozná, že oblast funguje? |
| 4 | **Vlastní rozhodovací pásmo** | Co může rozhodnout bez eskalace? Když nic, není to oddělení. |

Vedlejší efekt: rovnou vypadne, které krabičky jsou dnes prázdné (nikdo, žádný rozpočet, žádné číslo) a které jsou přeplněné. To je věcný podklad pro druhý krok, kdy se přiřazují jména.

### 2.1 Co znamená vlastní rozpočet

Bod 2 testu není nová věc, je to model z delegačního návrhu (iterace 05, kap. 5). Chci ho jen mít napsaný **u každého oddělení**, ne jenom u exec vrstvy:

- Každé oddělení má **vlastní roční rozpočet**: experimenty, vývoj a růst platů svých lidí.
- Rámec se **vyjednává ročně** s CEO a **upravuje kvartálně**, když se změní realita.
- Uvnitř rámce rozhoduje vlastník **bez eskalace**. Nad rámec, mimo plán nebo nový významný opakovaný náklad jde na CEO. Opakovaný náklad se počítá roční hodnotou závazku.
- Rozpočet je **rámec, ne povinnost ho utratit**. Nevyčerpané peníze se při reforecastu vracejí, ne propálí, ať o ně nepřijdu.
- Nový náklad **od 2 000 USD** se hlásí povinně, pod tím je vhodné ho zmínit.
- **Kdo nese rozpočet, vidí čísla pod ním** (kap. 6.4). Bez toho je rozpočtová odpovědnost formální.

U oddělení, které dnes nemá vlastní tým ani nákup (typicky Komunita a store), to může být zatím jen pojmenovaná nákladová linka místo plného rozpočtu. Ale i ta musí mít vlastníka a číslo, jinak krabička testem neprojde.

## 3. Mapa

Dvanáct oddělení ve čtyřech sférách a jedna průřezová osa. Sféra je vrstva vlastnictví a eskalace, oddělení je vrstva hranic, rozpočtu a čísla. Bez těch dvou vrstev si mapu hned rozbijeme o to, že jsme čtyři.

### 3.1 Sféry

| Sféra | Co drží pohromadě | Oddělení v ní |
|---|---|---|
| **Firma** | směr, kapitál, jednosměrné dveře | Strategie a portfolio |
| **Provoz a peníze** | firma běží, čísla sedí, firma se zrychluje | Finance · Interní provoz · Efektivizace a AI |
| **Poptávka** | hráči se o hře dozví a přijdou za rozumnou cenu | Marketing a UA |
| **Produkt** | hra vznikne, vyjde, žije, mluví a měří se | Herní produkce · Publishing a liveops · R&D a greenlight · Externí zakázky · Komunita a store · Data a analytika · Nábor |

Sféra Produkt drží sedm z dvanácti oddělení. Píšu to naplno, protože to je hlavní námitka, kterou proti téhle mapě dostanu, a je oprávněná. Odpověď na ni je v kap. 7 a v kap. 8: uvnitř sféry vznikají leady s vlastním rozhodovacím pásmem a já ze sebe současně shazuju denní koordinaci. Pokud tohle nedokážeme, mapa neplatí a sféru je potřeba rozdělit.

### 3.2 Oddělení

| # | Oddělení | Účel v jedné větě | Jedno číslo (návrh) |
|---|---|---|---|
| 1 | **Strategie a portfolio** | Rozhoduje, do čeho firma jde a co končí. | Runway a stav portfolia |
| 2 | **Finance** | Firma ví, kolik má, kolik pálí a na co. | Burn proti plánu |
| 3 | **Interní provoz** | Provoz nikoho nebrzdí. | Otevřené blokace, provozní náklad na člověka |
| 4 | **Efektivizace a AI** | Firma dělá stejnou práci za míň času. | Ušetřené člověkodny za kvartál |
| 5 | **Marketing a UA** | Hráči přijdou v ceně, která dává smysl. | CPI a ROAS proti plánu |
| 6 | **Herní produkce** | Hry se dodávají v čase a kvalitě. | Dodržení milníků, kapacita proti plánu |
| 7 | **Publishing a liveops** | Vydané hry žijí a vydělávají. | Revenue a retence vydaných titulů |
| 8 | **R&D a greenlight** | Ví se, odkud přijde další hra, a rozhodne se včas. | Počet prototypů dovedených k ano/ne za rok |
| 9 | **Externí zakázky (B2B)** | Příjem mimo vlastní tituly bez rozbití produkce. | Marže zakázek, spotřebovaná kapacita |
| 10 | **Komunita a store** | Firma má jeden hlas ke hráčům a store prodává. | Konverze store page, sentiment komunity |
| 11 | **Data a analytika** | Všichni měří to samé stejně. | Jedna definice na metriku, dostupnost dat |
| 12 | **Nábor** | Firma má lidi, které potřebuje, dřív než je potřebuje. | Doba od potřeby po nástup, úspěšnost po zkušebce |

### 3.3 Průřezová osa

| Osa | Proč to není oddělení | Kdo vlastní co |
|---|---|---|
| **Odměňování a růst lidí** | Rozhodnutí o platu a rozvoji nutně patří tomu, kdo s člověkem pracuje. Neprojde testem na bod 4. | Pravidla a rozpočtový rámec: Finance a CEO. Rozhodnutí o konkrétním člověku: sféra, ve které sedí, ve svém rozpočtu. Nový headcount: CEO, jednosměrné dveře. |

Nábor je oproti tomu oddělení, protože má proces, průběžný náklad, vlastní číslo a rozhodovací pásmo. Odměňování ne, to má jen pravidla.

### 3.4 Kde se liším od společného podkladu

| Změna | Proč |
|---|---|
| **Komunita a store jako samostatné oddělení** | V podkladu je to rozprostřené mezi marketing a publishing a je to sporná zóna č. 10. Jeden hlas navenek si zaslouží viditelnou krabičku, ne poznámku pod čarou. |
| **Data a analytika jako oddělení, ne jako spor** | V podkladu je to sporná zóna č. 4. Dokud nemá vlastníka, má každý svoji definici retence a nikdo nemá pravdu. |
| **Nábor jako oddělení, odměňování jako osa** | Podklad je slučuje do jedné oblasti Lidé. Ta má ale dvě různé povahy: nábor je proces s vlastníkem, odměňování je pravidlo s distribuovaným rozhodováním. Slepené dohromady to nikdy nedostane jasného vlastníka. |
| **R&D a greenlight místo R&D a nové produkty** | Výstupem R&D není produkt, ale rozhodnutí. Mění to, za co se oblast hodnotí: ne kolik prototypů vzniklo, ale kolik jich došlo k jasnému ano nebo ne. |
| **U každé krabičky jedno číslo** | Bez čísla nepoznáme, že delegace funguje, a na meetu 5 budeme vymýšlet KPI od nuly. |

### 3.5 Podle čeho jsem přiřazoval sporné krabičky

Nepoužívám argument "dělám to dnes". Používám dvě pravidla a jsem ochoten je nechat obrátit proti sobě:

**Pravidlo A: vlastník definice není největší konzument.**
Marketing je největší konzument dat. Kdyby definice metrik vlastnil konzument, definice se ohnou podle toho, co zrovna potřebuje vykázat. Data se navíc technicky rodí v buildu (eventy, SDK, pipeline), takže vlastnictví u produktu znamená o jedno rozhraní míň. Proto Data a analytika do sféry Produkt, marketing i finance jako konzumenti s právem si měřit cokoli, ale ne předefinovat, co ta metrika znamená.

**Pravidlo B: kampaň vlastní ten, kdo kupuje. Hlas hry vlastní ten, kdo hru dělá.**
Reklama a nákup je marketing. Ale co říká hra svým hráčům, jaká je store page a jak se odpovídá komunitě, to je součást produktu. Proto Komunita a store do sféry Produkt. Exekuce store stránek (texty, screenshoty, ASO) zůstává na marketingu jako dodavateli, protože tam sedí kreativní kapacita. Vlastním hlas a rozhodnutí, ne výrobu.

**A jedno pravidlo, které jde proti mně:** kdo přibere krabičku, musí ve stejné poradě říct, co shazuje. Můj seznam je v kap. 7.

## 4. Karty oblastí

Vyplněné podle šablony ze společného podkladu. Čtyři, které dnes fakticky držím, a tři, o které se hlásím.

### 4.1 Herní produkce

- **Účel:** Hry se dodávají v čase a kvalitě, tým ví, co dělá a proč.
- **Co řeší:** plán produkce a sprinty, vedení leadů, obsazení projektů lidmi, kapacita a její alokace, outsourcing, zadání pro týmy, kvalita dodávky.
- **Rozhoduje samo:** náplň sprintu v rámci schválené roadmapy, obsazení rolí, outsourcing v rámci vývojového budgetu, drobný vývoj a experimenty.
- **Vždy eskaluje:** změnu roadmapy, otevření produkce nového produktu, skluz s dopadem na firmu, nový headcount, ukončení spolupráce.
- **Rozhraní:** od financí reálná čísla nákladů a platů, od marketingu termíny kampaní a požadavky na kreativy, od publishingu release okno. Dodává buildy, termíny, kapacitní plán.
- **Kde to skřípe:** kapacita grafiků se prioritizuje podle toho, kdo zrovna přijde. Vývojový budget mám řídit bez přístupu k platům. Zakázky a marketingové požadavky vstupují do plánu mimo plán.

### 4.2 Publishing a liveops

- **Účel:** Vydané hry žijí a vydělávají.
- **Co řeší:** release management, liveops kalendář a eventy, provozní monetizaci, komunikaci s platformami na provozní úrovni, provozní čísla vydaných titulů.
- **Rozhoduje samo:** provozní releasy a hotfixy, liveops kalendář, monetizační kroky uvnitř schváleného modelu.
- **Vždy eskaluje:** platformní závazky, změnu monetizačního modelu (ne parametru), stažení titulu.
- **Rozhraní:** od produkce buildy a fixy, od marketingu kampaňový kalendář, od dat metriky. Dodává release termíny a provozní výsledky.
- **Kde to skřípe:** hranice s marketingem u releasu není nikde napsaná. Dnes to funguje, protože se domluvíme, ne protože je to rozhodnuté. Takové vlastnictví spadne při první neshodě.

### 4.3 R&D a greenlight

- **Účel:** Ví se, odkud přijde další hra, a rozhodnutí padne včas.
- **Co řeší:** prototypy, ověřování konceptů, market research, podklad pro greenlight.
- **Rozhoduje samo:** experimenty v rámci vývojového budgetu, zastavení prototypu.
- **Vždy eskaluje:** otevření produkce nového produktu (CEO plus zbytek exec).
- **Rozhraní:** od strategie mantinely portfolia, od marketingu pohled na trh a odhad akvizice, od financí náklad na prototyp. Dodává podklad k rozhodnutí.
- **Kde to skřípe:** není definovaná hranice mezi experimentem a otevřením produkce. Dokud není, každý povedený prototyp je potenciální spor o to, jestli jsme už něco odsouhlasili. Je to i otevřený TODO v delegačním návrhu.

### 4.4 Externí zakázky (B2B)

- **Účel:** Příjem mimo vlastní tituly, aniž by to rozbilo produkci.
- **Co řeší:** playables a externí vývoj, pipeline dealů, pricing podle interních tarifů, delivery a vztah s klientem.
- **Rozhoduje samo:** realizaci zakázky s marží alespoň 100 %, obsazení lidí uvnitř plánu, cenu nad tímto prahem.
- **Vždy eskaluje:** zakázku s marží pod 100 %, závazek sahající na kapacitu greenlightnutého titulu, strategického partnera.
- **Rozhraní:** od financí interní tarify a fakturace, od strategie mantinely (koho bereme a koho ne). Dodává marži, obsazenost, referenční práce.
- **Kde to skřípe:** iniciativu nosí všichni, což je správně a je na to podílový systém, ale rozhodnutí o alokaci lidí nese produkce sama a bez pravidla.

### 4.5 Komunita a store (hlásím se o ni)

- **Účel:** Firma má ke hráčům jeden hlas a store page prodává.
- **Co řeší:** store prezentaci a její výsledek, komunikaci s komunitou, sociální sítě směrem ke hráčům, podporu hráčů, tón hlasu hry.
- **Rozhoduje samo:** obsah a tón komunikace ke hráčům, priority na store page, reakce na komunitu.
- **Vždy eskaluje:** krizovou komunikaci, zásah do značky firmy.
- **Rozhraní:** od marketingu kreativní výrobu a ASO exekuci (jako dodavatel), od publishingu liveops kalendář a support vstupy, od dat čísla o konverzi. Dodává jednotný hlas a store výsledek.
- **Kde to dnes skřípe:** neexistuje. Rozprostřené mezi marketing a publishing, tedy dvě verze toho, co firma hráčům říká.

### 4.6 Data a analytika (hlásím se o ni)

- **Účel:** Všichni měří to samé stejně a nikdo se nehádá o čísla, jen o jejich výklad.
- **Co řeší:** datový stack, eventy v buildech, definice metrik, dostupnost přehledů, kvalitu dat.
- **Rozhoduje samo:** technické řešení stacku, definice metrik po konzultaci s konzumenty.
- **Vždy eskaluje:** citlivá data, zásah do produktu kvůli měření, větší investici do stacku.
- **Rozhraní:** dodává marketingu, financím, publishingu a produkci jedna čísla. Od nich bere požadavky na to, co se má měřit.
- **Kde to dnes skřípe:** neexistuje jako vlastnictví, existuje jako spor. Každý má svůj pohled a svoji definici.

### 4.7 Nábor (hlásím se o něj)

- **Účel:** Firma má lidi, které potřebuje, dřív než je potřebuje.
- **Co řeší:** proces od potřeby po nástup napříč firmou: definici role, standard pohovorů, inzerci a kanály, laťku, nabídku, koordinaci nástupu.
- **Rozhoduje samo:** podobu procesu a standardu, kanály a nástroje, finální ano k nabídce.
- **Vždy eskaluje:** nový headcount (CEO), plat mimo rámec rozpočtu sféry, ukončení spolupráce.
- **Kdo to odpracuje:** **pohovory a výběr do svých týmů dělají leadi**, každý podle stejného procesu a stejné laťky. Já vlastním proces, standard a finální ano, ne kalendář pohovorů. Provozní HR administrativu (smlouvy, nástupní papíry, benefity) dělá interní provoz.
- **Rozhraní:** potřebu definuje sféra, která člověka ponese, a účastní se výběru. Finance dávají rozpočtový rámec.
- **Argument, proč to patří k produkci:** nábor je kapacitní rozhodnutí a kapacitní plán firmy vzniká v produkci. Když nábor vlastní někdo, kdo nedrží kapacitní plán, začne se nabírat podle toho, kdo si nejvíc stěžuje.
- **Riziko, které přiznávám:** nábor přes leady je rychlý, ale bez společné laťky si každý tým nabere podle sebe. Proto je vlastnictví procesu a standardu podmínka, ne formalita.

## 5. Sporné zóny: můj návrh vlastníka

Ke každé zóně jdu s odpovědí, ne s otázkou. Je to k rozstřílení, ale ať se střílí do konkrétního návrhu.

| # | Sporná zóna | Návrh vlastníka | Mechanismus, který to drží |
|---|---|---|---|
| 1 | Nábor a platy | **Proces a laťka: oddělení Nábor. Výběr do týmu: lead. Plat konkrétního člověka: sféra, kde sedí. Headcount: CEO.** | Jeden proces pro celou firmu, pohovory vedou leadi, pravidla a rámec drží Finance |
| 2 | Marketingové kreativy vs. herní art | **Zdroj: produkce. Výsledek: marketing.** | Grafici se jmenovitě rozdělí na DEV a MKT; uvnitř své skupiny si každý prioritizuje sám, cross práce je přípustná po dohodě leadů obou oddělení |
| 3 | Publishing vs. marketing u releasu | **Co je v buildu a kdy jde ven: publishing. Kolik se do toho nalije a jaká je kampaň: marketing. Jak se o hře mluví: Komunita a store.** | Každý má veto jen na svoji půlku, žádné společné schvalování |
| 4 | Produktová analytika a data | **Oddělení Data a analytika** (pravidlo A, kap. 3.5) | Definice metrik jsou dekret ve Wiki, konzumenti si měří cokoli, ale nepředefinovávají významy |
| 5 | AI a automatizace vs. vývojové nástroje | **Kritérium komu to slouží: celá firma = Efektivizace a AI (provoz), vývoj her = produkce.** | Hub, wiki a procesní automatizace u provozu; pipeline, buildy a herní nástroje u produkce |
| 6 | Externí zakázky | **Pipeline: kdokoli (podílový systém). Delivery a alokace lidí: produkce. Cena: produkce nad prahem marže, pod prahem CEO.** | Práh je marže alespoň 100 %; zásah do kapacity greenlightnutého titulu je eskalace bez ohledu na marži |
| 7 | Monetizace | **Hra v produkci: game design. Hra v provozu: publishing.** | Marketing konzultovaný (LTV, ROAS) bez veta; změna modelu je eskalace, změna parametru ne |
| 8 | Provozní HR vs. Lidé | **Papír: interní provoz. Člověk: Nábor a sféry.** | Docházka, benefity a smlouvy do provozu; výběr, rozvoj a odměna k lidem, kteří s člověkem pracují |
| 9 | Smlouvy | **Registr a lhůty: Finance. Obsah závazku: sféra, která ho nese.** | Jeden registr, jeden termínovník, žádná smlouva mimo registr |
| 10 | Komunita a sociální sítě | **Oddělení Komunita a store** (pravidlo B, kap. 3.5) | Podpora hráčů a in-game komunikace je vstup, ne druhý kanál; krizová komunikace na CEO |

## 6. Čtyři podmínky, na kterých trvám

### 6.1 Rozřezání produkce

"Produkce = vše ostatní" není oddělení, je to zbytková kategorie. Za dva roky se do ní nasypal publishing, R&D, externí zakázky, nábor, platy a vývojový budget. Nikdo to nerozhodl, jen to nikam jinam nespadlo. Když z porady vyjde mapa, ve které je Herní produkce jedna krabička, nevyřešili jsme nic, jen jsme ten zbytek přejmenovali. Chci odejít s tím, že jsou to pojmenované krabičky s hranicemi, i kdyby je zítra pořád držel jeden člověk.

### 6.2 Rozhodovací pásmo černé na bílém

U každé krabičky dvě věty: co rozhoduje vlastník bez eskalace a kde začínají jednosměrné dveře. Kritérium je vratnost, ne velikost, to už jsme si odsouhlasili minule. Bez tohohle je mapa jen obrázek a na meetu 2 začneme od nuly.

Konkrétně u sebe potřebuju odsouhlasit hranici mezi experimentem a otevřením produkce nového produktu, protože dnes neexistuje a je to otevřený TODO z delegačního návrhu. **Navrhuju měřit ji časem:**

> Práce na konceptu je **experiment**, dokud nepřekročí **2 sprinty, tedy 4 týdny** práce týmu. Za tou čarou je to **otevření produkce nového produktu** a schvaluje ho CEO plus zbytek exec.

Čas je proti penězům lepší měřítko, protože ho vidí každý a nedá se schovat do jiné nákladové linky. Sprint je navíc jednotka, ve které stejně plánujeme, takže se to nemusí nikam přepočítávat. Má to jednu díru a rovnou k ní přidávám pojistku: **prodloužení experimentu o další dva sprinty není pokračování, ale nové rozhodnutí.** Jinak se produkt otevře na salám, čtyři týdny pětkrát za sebou.

### 6.3 Kapacitní pravidla

Dvě pravidla, obě dohodnutá dopředu.

**Grafická kapacita.** Dnes jsou grafici fakticky jeden pool a prioritu dostane ten, kdo přijde dřív nebo tlačí víc. Nejde přidat pravidlo nad společný pool, pool se musí rozdělit:

- Grafici se rozdělí **jmenovitě na DEV a MKT**. Ne procenta, ne půl na půl, konkrétní lidé pod konkrétní oddělení.
- Uvnitř své skupiny si vlastník prioritizuje sám a nikoho se neptá. To je celý smysl, marketing přestane žádat o čas a začne s ním hospodařit.
- **Cross práce je přípustná, když se na ní domluví leadi obou oddělení.** Není to eskalace a nepotřebuje to mě ani CEO, dohoda leadů stačí. Tohle je záměrně měkčí než tvrdý zámek: kapacita se má dát půjčit, jen ne potichu a ne přes hlavu leada.
- Co nejde: brát si lidi druhé skupiny bez té dohody, nebo si ji domluvit přímo s grafikem mimo leada.

**Kritérium na B2B zakázky.** Strop v člověkodnech nedává smysl, protože trestá i zakázky, které vydělávají. Kritérium je marže:

- Zakázka s **marží alespoň 100 %** (výnos je aspoň dvojnásobek delivery nákladů podle interních tarifů) je v pořádku a rozhoduje o ní produkce sama.
- Pod 100 % marže je to eskalace na CEO. Tam už nejde o zakázku, ale o rozhodnutí prodávat kapacitu firmy levně.
- Bez ohledu na marži: **zásah do kapacity greenlightnutého titulu je vždycky eskalace.** Ani skvěle placená zakázka nesmí potichu posunout vlastní hru.
- Předpoklad, který musí zaznít: **interní tarify musí existovat.** Dnes nejsou a je to otevřený úkol z delegačního návrhu. Bez nich se marže nedá spočítat a celé kritérium je jen věta.

Je to zároveň nejlevnější možný test celého modelu: malý rozsah, jasná hranice, vyhodnotitelné za 14 dní. Když tohle nezvládneme, nemá smysl zavádět 90denní pilot.

### 6.4 Přístup k číslům včetně výplat

Mám odpovídat za vývojový budget firmy a za návrhy platů, ale nevidím, kolik kdo bere. Bez toho neumím říct, jestli je projekt drahý, ani co znamená přidat člověka. Každé rozhodnutí o kapacitě je odhad, každý návrh platu vyjednávání naslepo.

Vím, že je to sporný bod (podklad P1 navrhuje souhrn a need-to-know) a že se o něm rozhoduje až na meetu 2. Na 20. 8. chci, aby zaznělo jako podmínka a zapsalo se to. **Kompromis, který přijmu:** vidím platy lidí, kteří spadají pod mou sféru, plus souhrny za firmu. Neprosazuju přístup ke všemu za každou cenu, prosazuju přístup k tomu, za co ručím. Platí to jako obecné pravidlo: kdo nese rozpočet, vidí čísla pod ním. Ne jen pro mě.

## 7. Co za to shazuju

Kdo přibere krabičku, musí ve stejné poradě říct, co shazuje. Můj seznam. Podmínka je u všech čtyř stejná: shazuju to i s rozhodováním. Poloviční předání znamená, že se věc vrátí zpátky ve chvíli, kdy je potřeba rozhodnout, a to je horší než ji držet.

| Co shazuju | Komu | Podmínka |
|---|---|---|
| **Denní koordinace projektů** | project leadům | Kompletně, včetně rozhodování o denních prioritách a řešení blokací uvnitř projektu. Mně zůstává sprint, roadmapa a kapacita. Tohle je největší položka a je to zároveň nutná podmínka toho, aby moje sféra unesla sedm krabiček. |
| **Provozní HR administrativa** | interní provoz | Docházka, benefity, smlouvy, nástupní papíry. Beru rozhodnutí o lidech, ne agendu kolem nich. |
| **Store operations a ASO exekuce** | marketing | Texty, screenshoty, lokalizace store stránek, ASO práce. Vlastním hlas, prioritu a výsledek store page, ne její výrobu. |
| **Vedení pohovorů a výběr do týmů** | leadům | Leadi si vybírají lidi do svých týmů podle jednoho procesu a jedné laťky. Mně zůstává proces, standard a finální ano. Krabičku Nábor beru i s tím, že ji z 80 % odpracuje někdo jiný. |

Co neshazuju a říkám to nahlas: **kapacitní plán a obsazení projektů**. To je jádro produkce. Když tohle rozhoduje někdo jiný, produkce už neručí za termíny a celý model padá.

## 8. Rizika, na která budu upozorňovat

1. **Moje sféra touhle mapou roste, ne zmenšuje se.** Sedm z dvanácti krabiček. Je to legitimní námitka a čekám ji. Moje odpověď: krabičky nejsou lidi, uvnitř sféry mají vzniknout leady s vlastním rozhodovacím pásmem a já současně shazuju denní koordinaci. Pokud tomu vedení nevěří, správné řešení není mi krabičky nedat, ale rozdělit sféru Produkt na dvě a přiřadit druhou někomu jinému. To ale znamená pátého člověka ve vedení a to je rozhodnutí, které nemám já.
2. **Dvanáct krabiček na čtyři lidi.** Když mapu nakreslíme hezky a přiřazení odložíme, na meetu 2 zjistíme, že dva z nás drží po čtyřech odděleních a někdo žádné. Proto chci u každé krabičky rovnou i větu "dnes to fakticky dělá X" jako reality check, ne jako přiřazení.
3. **Prázdné krabičky.** Efektivizace a AI, Komunita a store, Data, Nábor: dnes je nikdo nedrží celé. Krabička bez vlastníka je horší než žádná, protože se do ní začne odkazovat.
4. **Vlastnictví bez rozpočtu a bez dat.** Viz kap. 6.4. Netýká se to jen mě, týká se to každého, kdo dostane oddělení s nákladovou linkou.
5. **Ochrana delegace v prvním týdnu.** Až první rozhodnutí padne jinak, než by ho udělal CEO, ukáže se, jestli model platí. Chci dopředu dohodnuté, že se řeší přes vlastníka a nikdy kolem něj, oběma směry.
6. **Echo komora.** Čtyři lidi kreslí mapu celé firmě. Než se z toho stane dekret, měl by ho vidět aspoň někdo z leadů. Navrhuju jako úkol, ne jako diskusi na poradě.

## 9. Otázky, které položím ostatním

1. Souhlasíme, že krabička bez rozpočtu a bez čísla není oddělení? Pokud ano, je to první pravidlo mapy a použijeme ho na všechno včetně mě.
2. DJ: bereš Efektivizaci a AI jako svoji krabičku s vlastním rozpočtem, nebo je to dnes díra, kterou jen pojmenováváme?
3. Kuba: sedí ti rozdělení grafiků na DEV a MKT s cross prací po dohodě leadů, nebo v tom vidíš past? A co ti vadí na tom, aby definice metrik držel někdo jiný než jejich největší konzument?
4. Jirko: kde je pro tebe hranice mezi rozhodnutím majitele a rozhodnutím CEO u greenlightu nové hry? Předjímá to meet 2, ale ovlivní to, kam nakreslíme R&D a greenlight.
5. Všichni: pokud vám sedm krabiček u jedné sféry vadí, je odpověď rozdělit sféru Produkt, nebo mi krabičky nedat? Chci to slyšet teď, ne po poradě.
6. DJ: sestavíš baseline rozpočtů podle kap. 10.1, když ti dám rozpad lidí na oddělení? A co potřebuješ k tomu, abychom měli interní tarify do konce září?

## 10. Metodika: jak nastavit rozpočty a tarify

Dvě věci, které dnes nemáme a bez kterých zbytek modelu nefunguje. Nenesu na poradu čísla, nesu způsob, jak se k nim dostaneme. Cíl je, aby se o tom dalo rozhodnout za dvacet minut a ne za kvartál.

### 10.1 Rozpočet oddělení

**Nepočítat od nuly.** Zero-based rozpočtování je u šestnácti lidí zbytečná práce. Baseline z reality plus zdůvodněné delty.

**Krok 1: baseline, co oddělení stojí dnes** (roční run rate):

| Složka | Co do ní patří |
|---|---|
| Lidé | fixní platy lidí, kteří na oddělení dělají, plus odhad bonusové složky; u sdílených lidí odhad podle podílu času, stačí přesnost na desítky procent |
| Nástroje a subscriptions | licence, SaaS, cloud, storage, AI nástroje; roční hodnota, ne měsíční |
| Externí dodávky | outsourcing a externí spolupráce, které si oddělení objednává |
| Přímé provozní náklady | co jde jednoznačně přiřadit (UA spend, hardware, devices) |

Baseline není rozpočet, je to **podlaha**. Ukáže, co firma na tu oblast utratí, i kdyby se celý rok nic nezměnilo.

**Krok 2: obálky navrch.** Tady teprve začíná pravomoc:

| Obálka | Doporučení | K čemu je |
|---|---|---|
| Experimenty a investice | 5 až 15 % run rate podle toho, kolik změny od oblasti čekáme (Efektivizace a AI nahoře, Finance dole) | aby vlastník mohl něco zkusit bez prosby |
| Růst platů podřízených | 3 až 8 % payrollu oddělení na rok | přesně ta pravomoc, kterou dává delegační návrh |
| Rezerva | drží firma centrálně, ne oddělení | buffer v každé krabičce znamená dvanáct neviditelných rezerv |

**Pravidla, která k tomu patří:**

1. **Dvě čísla, ne jedno.** Payroll (vlastník ho vidí, ale mění se přes headcount a přes obálku na růst platů) a **diskreční část** (to, co vlastník opravdu řídí). Bez toho rozdělení to vypadá, že chief rozhoduje o milionech, a přitom nerozhoduje skoro o ničem.
2. **Kdo co dělá:** Finance sestaví baseline, mají data. Vlastník navrhne delty a zdůvodní je. CEO schvaluje rámec.
3. **Kvartální reforecast**, ne roční slib.
4. **Nevyčerpané peníze se vracejí** do centrální rezervy. Žádné utrácení v prosinci, ať o ně nepřijdu.
5. **První kvartál nanečisto.** Čísla se sledují, ale rozhoduje se pořád postaru. Ověří se, jestli přiřazení nákladů vůbec dává smysl, dřív než se z toho stane pravomoc. Sedí to k rozhodnutí zavádět postupně i k tomu, že bonusy mají první měsíc běžet nanečisto.

**Kolik to reálně stojí práce:** baseline za všechna oddělení je jedno odpoledne nad exportem z účetnictví a seznamem subscriptions. Delty jsou hodina na oddělení. Není to kvartální projekt a nechci, aby se z toho udělal.

### 10.2 Interní tarify

Tarif potřebujeme na dvě věci: spočítat **marži zakázky** (kritérium v kap. 6.3) a spočítat **zisk dealu pro podíly 5 + 5 %** (delegační návrh, kap. 8). Dokud tarify nejsou, obě pravidla jsou jen věty.

1. **Tarif na roli, ne na člověka.** Programátor, grafik, game designer, QA, produkce. Maximálně tři stupně seniority. Tarif podle jednotlivce je citlivý, nedá se sdílet a stejně se nikdy neaktualizuje.
2. **Náklad na člověkoden** = (roční náklad role včetně odvodů + přiřaditelné nástroje a hardware + přirážka na režii) / reálně odpracovatelné dny.
3. **Reálné dny, ne 250.** Po dovolené, svátcích, nemoci, interních schůzkách a školení vychází zhruba 180 až 200 dní. Počítat s utilizací 75 až 80 %. Kdo počítá se stovkou procent, zabuduje si ztrátu rovnou do tarifu.
4. **Režie se rozpouští přirážkou** na produkční role, řádově 20 až 40 %. Druhá možnost je režii nepočítat a chtít vyšší marži, ale pak číslo 100 % neznamená to, co si pod ním představujeme.
5. **Dvě sazby na roli:** cost rate (interní náklad, slouží pro marži a pro podíly) a list rate (cena pro klienta). **List = cost × 2.** Tím je kritérium marže 100 % zabudované rovnou do ceníku a nemusí se dopočítávat u každé nabídky.
6. **Revize jednou ročně** spolu s rozpočty. Tarif se nemění uprostřed běžící zakázky.
7. **Zpětná kontrola po dodání:** skutečně odpracované dny × cost rate proti odhadu. Vypadne z toho skutečná marže (podíly se počítají ze skutečně zaplaceného zisku) a lepší odhady na příště.
8. **Kdo to vlastní:** Finance počítá, produkce dodává vstupy (složení týmu, utilizace, odpracované dny), CEO schvaluje.

**Věc, kterou chci na poradě pojmenovat:** marže 100 % nad tarifem, který obsahuje režii, je něco úplně jiného než 100 % nad holými mzdami. Musíme se dohodnout, co tarif obsahuje, jinak si každý pod stejným číslem představí něco jiného. A je to zároveň další důvod, proč je přístup k mzdovým datům podmínka a ne preference: bez nich produkce cenu neobhájí a marži jen odhaduje.

## 11. Zbývá doplnit před poradou

- [ ] Reality check ke každé krabičce: kdo to dnes fakticky dělá. Dělám sám před poradou.
- [ ] Z metodik v kap. 10 udělat na poradě dva úkoly s vlastníkem a termínem: baseline rozpočtů (Finance + vlastníci oblastí) a interní tarify (Finance + produkce).
