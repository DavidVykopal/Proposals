# CPI testy: pipeline, cíle a knihovna nápadů

**Stav:** návrh 4. 11. 2026, vlastník rozhodnut 6. 11. 2026. Zdroje: `STRATEGIE_PRODUKCE.md` (kapitola CPI testy), květnový CPI návrh Mecha Fortress (podklad této kapitoly), NoxHub projekt CPI tests (CPI-9 až CPI-16). **Pro AI agenty:** zdrojem pravdy je tento soubor. Věci označené *(návrh)* jsou Davidův návrh, ne rozhodnutí. Úkoly žijí v NoxHubu, projekt CPI tests.

## Shrnutí

- CPI testy běží **jako stálá pipeline: minimálně 1 test měsíčně, podle potřeby 2**. Běh jednoho testu trvá zhruba **14 dní**, celý cyklus od briefu po zápis do knihovny zhruba měsíc.
- Každý test je **kombinace tří věcí: struktura / gameplay, vizuální styl a téma**, a vždy má **cíl, na který odpovídá**.
- Výsledky skládáme do **vlastní knihovny nápadů**: co jsme testovali, za kolik, s jakým výsledkem. Časem z ní vybíráme témata bez nových testů.
- Teď běží **dva cíle**: (A) témata a styly pro **2 až 3 reskiny Mecha Fortress / Sector Defense**, (B) téma a styl, které **nahradí vizuál Hexapolisu** pro Hexapolis 2 nebo další strategické idle hry.
- Pro každý cíl je připravená **sada variant** do prvního testu (cíl A 4, cíl B 5): co už máme v NoxHubu a v květnovém návrhu, doplněné o nejlepší odhady.
- **Program vlastní marketing, tedy Kuba B.** (rozhodnuto 6. 11.). Produkce zadává, co se chce dozvědět, a dává podněty.

## Z čeho se skládá každý test

| Složka | Co to je | Příklad |
|---|---|---|
| **Struktura / gameplay** | jaký herní loop kreativa ukazuje | MF obrana hradby s vlnami; hexová 4X mapa s městem |
| **Vizuální styl** | jak to vypadá | stylizovaný cartoon, malovaný premium, low-poly diorama |
| **Téma** | o čem to je | fantasy království, zombie, Řím, vikingové |
| **Cíl** | jakou otázku test zodpoví | který z reskinů má nejnižší CPI proti MF baseline |

Pravidlo: v jednom testu se mezi variantami **mění jen to, co testujeme**. Když testujeme téma a styl, struktura (gameplay ve videu, kompozice, délka, CTA) zůstává stejná. Proto se pro každý cíl dělá **jedna sada základních assetů převedená do variant** (NoxHub CPI-15).

## Pipeline: jeden test zhruba za měsíc

| Krok | Co se děje | Délka |
|---|---|---|
| 1. Brief | cíl, 4 až 5 variant (struktura + styl + téma), baseline, geo, rozpočet | 1 až 2 dny |
| 2. Kreativy | statiky, video, případně landing page nebo playable pro každou variantu | asi 1 týden |
| 3. Běh testu | kampaně v geo US, DE, KR, SE, JP; po 72 h kontrola a vypnutí jasných propadáků | asi 14 dní |
| 4. Vyhodnocení | CPI, CTR, IPM po variantách a geo, verdikt k cíli | 1 až 2 dny |
| 5. Knihovna | zápis do knihovny níže a do úkolu v NoxHubu, návrh dalšího testu | 1 den |

- **Kadence:** 1 test měsíčně je minimum. Druhý test v měsíci, když se kreativy dalšího testu stihnou připravit během běhu předchozího *(návrh: kroky 1 a 2 dalšího testu dělat během kroku 3 předchozího)*.
- **Kreativy:** pro každé téma tři typy, jak navrhl květnový podklad: landing page only (čistý appeal tématu), playable only (přenáší gameplay install intent?), kombinace (kandidát na scaling).
- **Baseline:** cíl A měří proti aktuálnímu Mecha Fortress, cíl B proti aktuálnímu Hexapolisu.
- **Vítěz** *(návrh)*: varianta s nejnižším CPI, která je zároveň levnější než baseline a drží CTR. Konkrétní práh nastaví UA podle MF benchmarku.
- **Vlastník programu:** marketing, tedy **Kuba B.** (rozhodnuto 6. 11., CPI-20). Produkce zadává, co se chce dozvědět, a dává podněty k variantám.
- **Úkoly pipeline v NoxHubu** (pod CPI-13): šablona briefu CPI-17, kadence CPI-18, knihovna CPI-19, vlastník a rozpočet CPI-20.

## Cíl A: témata pro 2 až 3 reskiny Mecha Fortress / Sector Defense

**Otázka:** které téma a styl dají nejnižší CPI pro **stejný MF gameplay**? Gameplay MF-branch neiterujeme, recept je ověřený, mění se jen obal. NoxHub: CPI-11 (test CPI-14, do 15. 12. 2026).

Struktura je u všech čtyř stejná: **MF obrana pevnosti proti vlnám, hrdinové/jednotky na hradbách, vylepšování mezi vlnami**.

| # | Téma | Vizuální styl | Proč to testujeme | Odkud |
|---|---|---|---|---|
| A1 | **Warcraft fantasy: lidé proti orkům** | Warcraft styl: robustní proporce, přehnaná zbroj a zbraně, ručně malované textury, sytě barvy | silná známá estetika, frakce a hrdinové, široké mužské publikum; jasný Jirkův input | CPI-9 |
| A2 | **Zombie bunkr** (The Bunker) | semi-realistický, gritty, vojenský | nejmenší změna proti MF, jasný 3sekundový read, muži 28 až 45 | CPI-10, květnový návrh |
| A3 | **Dračí doupě** (Wyrm's Lair) | malovaný premium fantasy realismus | nejvyšší appeal a potenciál sběru draků, ale dražší art | květnový návrh, CPI-21 |
| A4 | **Plastoví vojáčci** (Army Men styl) | hračková dioráma, plast, stůl nebo dětský pokoj | nostalgie napříč věkem, levný art, vtipné destrukce; test, jestli levný styl udrží CPI | nejlepší odhad (z nostalgických nápadů v květnovém návrhu), CPI-22 |

Warcraft styl je v obou cílech schválně stejný (A1 a B2): jedna sada assetů ve Warcraft stylu poslouží oběma testům a ukáže, jestli táhne v obranné i hexové struktuře.

**Rozhodne:** dvě až tři nejlevnější varianty proti MF baseline jdou do výroby reskinů 2027 (NOVE-11, NOVE-12). A3 testujeme, i když je dražší, abychom věděli, jestli se prémiový art vyplatí.

## Cíl B: téma a styl místo současného vizuálu Hexapolisu

**Otázka:** které téma a styl přitáhnou nejlevněji hráče **civilization-like hexové strategie**, pro Hexapolis 2 a strategické idle hry? NoxHub: CPI-12 (assety CPI-15, test CPI-16).

Struktura je u všech pěti stejná: **hexová mapa, růst města, expanze a souboj o území**. Test běží ve dvou settingách (MF a Hex), jak říká strategie, aby šlo téma použít i ve strategické větvi.

| # | Téma | Vizuální styl | Proč to testujeme | Odkud |
|---|---|---|---|---|
| B1 | **Římská říše** (legie, provincie, silnice) | stylizovaná low-poly dioráma, teplé barvy | historická 4X klasika, srozumitelná expanze, silné pro PvP dobývání | CPI-23 |
| B2 | **Warcraft fantasy: lidé, orkové, elfové** | Warcraft styl: robustní proporce, přehnaná zbroj, ručně malované textury, sytě barvy | sdílí estetiku a assety s A1, frakce přirozeně nesou PvP | CPI-24 |
| B3 | **Vikingové** (fjordy, nájezdy, klany) | malovaný stylizovaný sever, chladné barvy a oheň | klany a nájezdy sedí na PvP a sociální vrstvu, silný mužský segment | nejlepší odhad, CPI-25 |
| B4 | **Kolonie na cizí planetě** (sci-fi osídlování hexů) | čistý sci-fi, světlé biomy | odliší nás od historických 4X; navazuje na projekt Space Hex | nejlepší odhad, CPI-26 |
| B5 | **Mýtická antika: bohové a kouzla** (inspirace Age of Mythology: Řecko, Egypt, sever; božské síly jako blesk a meteor, mýtické jednotky jako minotaur a kyklop) | malovaný stylizovaný antický svět, mramor a zlato, výrazné efekty božských sil | božská síla je efektní 3sekundový moment do kreativy; bohové a kouzla nesou meta a monetizaci (síly, talenty, mýtické jednotky), panteony nesou PvP frakce | Davidův input 5. 11., CPI-27 |

B1 a B5 jsou schválně pár: stejná antika, test ukáže, jestli táhne víc **historická, nebo mýtická** verze. Část assetů (architektura, krajina, jednotky) se dá sdílet.

**Rozhodne:** téma a styl pro nový Hexapolis 2 (hex gameplay na MF metě, vznikne jen po gate, rozhodnutí II až III 2027) a zásobník témat pro strategickou větev.

## Knihovna nápadů a výsledků

Každý test sem přidá řádky. Výsledky doplní UA po vyhodnocení.

| Test | Cíl | Varianta (struktura / styl / téma) | Geo | CPI | CTR | IPM | Verdikt |
|---|---|---|---|---|---|---|---|
| Star Marines v1 až v3 (CPI-1 až CPI-3) | starší test | sci-fi mariňáci | doplnit | doplnit | doplnit | doplnit | doplnit |
| CPI-14 | A | A1 až A4 | US, DE, KR, SE, JP | | | | čeká |
| CPI-16 | B | B1 až B5 | US, DE, KR, SE, JP | | | | čeká |

### Zásobník dalších nápadů (pro další kola)

- **Cartoon fantasy (Realm's Keep):** měkčí casual styl Kingdom Rush / Rush Royale, hero summon, z květnového návrhu.
- **Monster trainer defense:** sběr a evoluce elementálních stvoření (nostalgie Pokémon bez IP).
- **Empire ages defense:** vesnice roste v pevnost, velké tlačítko age-up (Age of Empires).
- **Dungeon commander:** obrácená obrana, bráníme temné jádro před hrdiny (Dungeon Keeper).
- **Loot fortress:** vlny padají s vybavením a legendárními díly věží (Diablo).
- **Low-CPI stickman:** pár jednotek, velká čísla, minimum detailu (We Are Warriors, Stickman).
- **Warhammer grim fantasy:** masivní zbroj, frakce, temné bojiště.
- **Feudální Japonsko** pro cíl B: klany, hrady, sezóny (silné pro asijské geo).

## Termíny

| Kdy | Test |
|---|---|
| XI 2026 | brief a kreativy cíle A (A1 až A4) |
| do 15. 12. 2026 | běh a vyhodnocení testu cíle A (CPI-14) |
| XII 2026 | sada assetů pro cíl B (CPI-15, do 15. 12.) |
| do 15. 1. 2027 | test cíle B v MF a Hex settingu (CPI-16) |
| od I 2027 | 1 až 2 testy měsíčně ze zásobníku podle potřeb větví |

## Slabá místa a otevřené otázky

| Námitka | Proč může platit | Odpověď nebo co s tím |
|---|---|---|
| **Bez rozpočtu nevíme, jestli test vůbec něco řekne** | Cíl A má 4 varianty × 3 typy kreativ × 5 geo = 60 buněk, cíl B 5 variant × 2 settingy × 3 typy × 5 geo = 150 buněk. Rozpočet rozdělený takhle jemně dá na buňku málo instalací a rozdíly v CPI budou šum. | UA předem určí minimální počet instalací na variantu a rozpočet dopočítá z něj, ne naopak. Pro verdikt zúžit buňky: méně geo a tři typy kreativ jen u finalistů. |
| **Kvalita kreativy přebije téma** | A3 a B5 mají dražší art, Warcraft styl má silnou referenci, plastoví vojáčci jsou schválně levní. Vyhrát může nejlepší video, ne nejlepší téma. Jedna sada základních assetů (CPI-15) je naplánovaná jen pro cíl B. | Pro cíl A stejné pravidlo: jeden storyboard, stejný hook, délka a CTA, kreativy od stejného autora. Před spuštěním slepé porovnání kvality, nevyrovnanou variantu dorovnat nebo vyřadit. |
| **Baseline není férová** | MF a Hexapolis mají kreativy vyladěné dlouhým během, nové varianty jsou první verze. Porovnání s historickým CPI hry zvýhodní baseline. | Baseline točit ve stejném testu: vizuál MF a Hexapolisu převedený stejnou šablonou, stejný rozpočet a stejné období. |
| **Síť rozdělí rozpočet sama** | Když varianty běží v jedné kampani, algoritmus pošle peníze variantě, která vede první dny, a ostatní nedostanou šanci. | Každá varianta vlastní kampaň nebo ad set s pevným rozpočtem. Vypínání po 72 h jen podle předem daného prahu, ne od oka. |
| **Termíny kolidují s koncem roku** | Verdikt testu A do 15. 12. padá do týdne GameJamu. Test B by běžel přes Vánoce a Nový rok, kdy jsou aukce dražší a tým má volno. Assety B má dělat DEV grafika souběžně s vánočním board game a zimními eventy. | Test B spustit až v lednu a verdikt posunout na konec ledna; rozhodnutí o Hexapolis 2 je až II až III 2027, nic se tím nezdrží. |
| **Průměr přes geo schová, kde téma funguje** | US, DE a SE se chovají jinak než KR a JP; římská nebo vikinská témata můžou vyhrát na Západě a propadnout v Asii. | Verdikt psát po regionech (Západ, Asie) a předem určit, který region je pro rozhodnutí rozhodující. |
| **Bez vlastníka pipeline nepoběží** | Pět kroků přes UA, marketing a DEV grafiku, nikdo za celek neodpovídá (CPI-20). Měsíční kadence bez vlastníka spadne po prvním testu. | **Rozhodnuto 6. 11.:** program vlastní marketing, tedy Kuba B. Produkce zadává, co se chce dozvědět, a dává podněty. |

**Potřebuje odpověď:**

- Kolik je rozpočet na jeden test a na jednu variantu, a kdo ho schvaluje?
- ~~Kdo je vlastník programu?~~ **Rozhodnuto 6. 11.:** marketing, Kuba B. Zbývá: kdo napíše brief testu A ještě v listopadu?
- Měří se baseline MF a Hexapolisu ve stejném testu, nebo z historických dat?
- Spustit test B přes svátky, nebo až v lednu?
- Které geo je pro verdikt rozhodující, a zůstávají KR a JP v prvních testech?
- Kdo dělá kreativy cíle A v listopadu, když DEV grafika dělá vánoční board game a zimní eventy?

## Co je potřeba rozhodnout

- ~~**Vlastník CPI programu**~~ **Rozhodnuto 6. 11.:** marketing, tedy Kuba B. (brief, kreativy, vyhodnocení, knihovna). Produkce zadává, co se chce dozvědět, a dává podněty.
- **Rozpočet na test** a práh vítěze proti baseline (UA podle MF benchmarku).
- **Potvrdit sady A1 až A4 a B1 až B5**, případně prohodit variantu ze zásobníku.
- Kdo dělá **kreativy**: marketing (Ondra, Ruda), nebo i DEV grafika pro sadu assetů cíle B.
