# Příprava na poradu 20. 8. 2026 - Sféry vlivu a oddělení

> HTML render: `priprava-2026-08-20-oddeleni.html`
>
> Podklad k úkolu z porady 6. 8.: "Zamyslet se nad strukturou firmy (marketing, produkce,
> hiring, finance, interní operace) nezávisle na konkrétních lidech. Definovat, co má které
> oddělení řešit, jaké jsou jejich sféry působnosti a kde dochází ke konfliktům/průnikům."
> Tento dokument je startovní návrh k rozstřílení, ne hotové řešení.

---

## 1. Cíl porady

Do konce porady mít:

1. **Odsouhlasenou mapu oddělení** - seznam oblastí, ze kterých se firma skládá, nezávisle na jménech.
2. **Kartu každého oddělení** - účel, co řeší, co rozhoduje samo, co eskaluje, rozhraní na ostatní.
3. **Rozhodnuté sporné zóny** - u každého průniku určeného právě jednoho vlastníka.
4. **Potvrzený plán dalších schůzek** - recap témat z `TEMATA_DALSICH_PORAD.md`, případné doplnění.
5. **Zápis jako dekret do Wiki** - první reálný dekret nového systému.

Jména se přiřazují až v druhém kroku (jeden člověk může držet víc oddělení). Nejdřív se shodnout, JAKÉ krabičky existují a kde mají hranice.

## 2. Navrhovaná agenda (2 h)

| Čas | Blok |
|---|---|
| 10 min | Připomenutí vize firmy + kontrola úkolů z minula |
| 15 min | Každý představí svůj návrh mapy oddělení (bez diskuse, jen prezentace) |
| 20 min | Sladění mapy - shodnout se na seznamu oddělení (rozdíly v návrzích = body k diskusi) |
| 40 min | Sporné zóny - projít průniky (kap. 5), u každého určit vlastníka |
| 15 min | Karty oddělení - doplnit "rozhoduje samo / eskaluje" u shodnutých oddělení |
| 10 min | Recap plánu dalších schůzek (`TEMATA_DALSICH_PORAD.md`) - potvrdit témata, doplnit chybějící |
| 10 min | Rekapitulace, zápis dekretu, úkoly na příště |

## 3. Startovní návrh mapy oddělení

Vychází ze struktury v delegačním návrhu (iterace 05) a z oblastí zmíněných na poradě
(marketing, produkce, hiring, finance, interní operace). Devět oblastí + jedna průřezová:

### 3.1 Strategie a vedení
Účel: směr firmy, kapitál, portfolio.
Řeší: vizi a strategii, roadmapu firmy, greenlight/ukončení projektů, zásadní rizika, krize, vztahy s platformami na úrovni závazků, právní a statutární věci.
Typicky rozhoduje: všechna jednosměrná rozhodnutí firmy.

### 3.2 Finance
Účel: firma ví, kolik má, kolik pálí a na co.
Řeší: cashflow forecast, burn a runway, platby, fakturace, konsolidaci budgetů, payroll administrativu, smlouvy po finanční stránce, reporting (měsíční snapshot).
Typicky rozhoduje: standardní platby v budgetu, finanční procesy.
Eskaluje: dopad na runway, výdaje mimo budget, změny celkového rozpočtu.

### 3.3 Interní operations
Účel: provoz nikoho nebrzdí.
Řeší: kancelář, hardware a vybavení, provozní služby a dodavatele, provozní smlouvy, eventy, onboarding zázemí, provozní HR agendu (docházka, benefity).
Typicky rozhoduje: dodavatele a nákupy v operations budgetu.
Eskaluje: stěhování, dlouhé závazky, významný recurring.

### 3.4 Efektivizace a automatizace
Účel: firma se zrychluje - AI, nástroje, data.
Řeší: interní nástroje a systémy (hub, wiki), AI nástroje a automatizace procesů, interní data a přehledy, vyhodnocování experimentů efektivity.
Typicky rozhoduje: experimenty v experimentálním budgetu v rámci bezpečnostních pravidel.
Eskaluje: citlivá data, zásah do produktu, větší projekt.

### 3.5 Marketing a UA
Účel: hráči se o titulech dozví a přijdou.
Řeší: marketingovou strategii, UA kampaně a nákup, marketingové kreativy, měření výkonu kampaní, ASO/store prezentaci, sociální sítě a komunitu, brand navenek.
Typicky rozhoduje: kanály, kreativy, realokaci uvnitř schválené alokace.
Eskaluje: změnu celkové alokace, zásah do značky.

### 3.6 Herní produkce
Účel: hry se dodávají v čase a kvalitě.
Řeší: sprinty a plán produkce, vedení projektů (leadi), game design, vývoj, art, QA, obsazení projektů lidmi, outsourcing.
Typicky rozhoduje: sprint v rámci roadmapy, outsourcing, obsazení rolí.
Eskaluje: roadmapu a nové projekty, skluz s dopadem na firmu.

### 3.7 Publishing a provoz titulů
Účel: vydané hry žijí a vydělávají.
Řeší: release management, store operations, liveops a eventy ve hrách, monetizační provoz, komunikaci s platformami na provozní úrovni, produktovou analytiku vydaných titulů.
Typicky rozhoduje: provozní releasy, liveops kalendář.
Eskaluje: platformní závazky, zásadní monetizační změny.

### 3.8 R&D a nové produkty
Účel: odkud přijde další hra.
Řeší: prototypy, ověřování konceptů, market research, přípravu greenlight podkladů.
Typicky rozhoduje: experimenty v experimentálním/vývojovém budgetu.
Eskaluje: otevření produkce nového produktu (CEO + zbytek exec).

### 3.9 Externí zakázky (B2B)
Účel: příjmy mimo vlastní tituly.
Řeší: playables a externí vývoj, pipeline dealů, pricing (interní tarify), delivery a vztah s klientem.
Typicky rozhoduje: realizaci zakázek v kapacitním rámci.
Eskaluje: závazky nad rámec kapacit, strategické partnery.

### 3.10 Lidé (průřezová oblast - k diskusi, zda je to oddělení)
Účel: správní lidé, férově zaplacení, rostou.
Řeší: nábor, ukončení, platovou normalizaci, bonusový systém, rozvoj lidí, kulturu.
Poznámka: na poradě zmíněno jako "hiring" - samostatná oblast. Dnes to v návrhu drží produkce (nábor/platy) + každý exec (růst platů podřízených) + finance (payroll administrativa). Rozhodnout, zda je to samostatné oddělení, nebo rozprostřená odpovědnost s jasnými pravidly.

## 4. Karta oddělení - šablona na vyplnění

Každý si před poradou zkusí vyplnit kartu minimálně pro oblasti, které dnes fakticky drží, a přinést vlastní verzi celkové mapy (klidně jinou než kap. 3):

```
Oddělení: ...
Účel (1 věta, proč existuje): ...
Co řeší (5-10 položek): ...
Rozhoduje samo (bez eskalace): ...
Vždy eskaluje (jednosměrné dveře oblasti): ...
Rozhraní na ostatní oddělení (od koho co potřebuje, komu co dodává): ...
Kde to dnes skřípe (konflikty, nejasné vlastnictví): ...
```

## 5. Sporné zóny - průniky k rozhodnutí

Místa, kde si dnes vlastnictví může nárokovat víc oblastí. Cíl: u každé určit právě jednoho vlastníka (ostatní jsou konzultovaní, bez veta).

1. **Nábor a platy** - produkce (obsazení projektů, návrhy platů) × finance (payroll, budget) × každý exec (růst platů podřízených) × CEO (finální slovo). Kdo vlastní proces náboru od potřeby po nástup?
2. **Marketingové kreativy vs. herní art** - marketing (výkon kreativ) × produkce/art (kapacita grafiků, kvalita, art direction napříč firmou). Kdo prioritizuje čas grafiků, když se tlačí kampaň i hra?
3. **Publishing** - produkce (dodání buildů, feature development) × marketing (store prezentace, ASO, launch komunikace). Kde přesně vede hranice u releasu?
4. **Produktová analytika a data** - marketing (kampaně, atribuce) × publishing/produkce (metriky her) × efektivizace (interní data a nástroje). Kdo vlastní datový stack a definice metrik?
5. **AI a automatizace vs. vývojové nástroje** - efektivizace (interní systémy, AI) × produkce (nástroje ve vývoji her, vývojový budget). Kde končí interní efektivita a začíná vývoj?
6. **Externí zakázky** - kdo vlastní pipeline a pricing, když sales tým neexistuje a iniciativy nosí všichni (podíly z dealů)? Kdo rozhoduje o alokaci lidí z produkce na zakázku vs. vlastní titul?
7. **Monetizace** - game design (ekonomika hry) × publishing (provozní monetizace) × marketing (LTV/ROAS pohled). Kdo má finální slovo u monetizační změny?
8. **Provozní HR vs. Lidé** - interní operations (administrativa, benefity) × oblast Lidé (nábor, rozvoj, odměňování). Hranice?
9. **Smlouvy** - finance (finanční stránka) × interní operations (provozní dodavatelé) × strategie (platformy, IP). Kdo drží registr smluv a hlídá závazky?
10. **Komunita a sociální sítě** - marketing (brand, akvizice) × publishing (podpora hráčů, liveops komunikace). Jeden hlas navenek?

## 6. Pravidla diskuse (z minulé porady a podkladů)

- Bavíme se o krabičkách, ne o lidech - jména až v kroku 2.
- Každý průnik končí právě jedním vlastníkem; ostatní jsou konzultovaní bez veta.
- Neshoda = disagree & commit po rozhodnutí; nesouhlas zazní teď, ne po poradě.
- Kritérium pro eskalace: vratnost rozhodnutí, ne jeho velikost.
- Výstup se zapíše jako dekret do Wiki.

## 7. Co si každý přinese

1. Vlastní verzi mapy oddělení (klidně odlišnou od kap. 3) - stačí seznam s jednou větou u každého.
2. Vyplněné karty (kap. 4) pro oblasti, které dnes fakticky drží.
3. Svoje 3 nejpalčivější sporné zóny - kde ho dnes nejvíc brzdí nejasné vlastnictví.
