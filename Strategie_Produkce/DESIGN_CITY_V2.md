# City V2 meta: design dokument

> **Stav:** návrh v2, 4. 11. 2026. Přepracováno podle Davidova zadání: City V2 má být **co nejbližší klon Clash of Clans a Rise of Kingdoms**. První verze **bez výroby jednotek, globální mapy a bojů mezi hráči**, jde hlavně o vlastní stavění města, sběr surovin a upgrady; **budovy ovlivňují meta staty**. Verze v1 (1. 11.) je nahrazená. Věci označené *(návrh)* jsou návrh autora dokumentu.
> **Doplněno 5. 11. 2026:** v Hexapolisu implementované do 11. 12. 2026 za RC flagem, hráči v lednu 2027. Release freeze 14. až 18. 12. (GameJam). Čísla: `BALANC_CITY_V2.md` (ceník 60 gemů = 1 USD).
> **Rozhodnuto 6. 11. 2026 (David):** City V2 **nahradí dnešní budovy na mapě MF** (Gold Mine, Gem Mine a další), hráči dostanou **refund** investic (pravidlo je *návrh*, `BALANC_CITY_V2.md` kap. 11). Gemy kupují **startovní bundle surovin** a **City VIP** (zrychlení stavby a další výhody, čísla *návrh* v BALANC kap. 8.1 a 8.2). V Hexu v testu a připravené do 11. 12., hráči v lednu. Příjmy z Play Passu se do revenue Hexu nepočítají. Hex featury a SGB dělí Mirek, Kubík (Jakub H.) a David.
> **Názvy:** City V2 = Mapa V2 = Město V2, stejná feature. V kódu `CityV2`, v CODE BACKLOG jako **Meta Village V2, CODE-9**, rozšiřitelnost MF **CODE-65**.
> **Patří k:** `KONCEPT_OBNOVA_HEXU.md` (obnova Hexapolisu přes PvP a City V2), `STRATEGIE_PRODUKCE.md`. Sesterský dokument: `DESIGN_HEX_PVP.md`.
> **Pro AI agenty:** zdroj pravdy je tento soubor. Čísla (levely, časy, ceny, bonusy) jsou výchozí návrhy v configu per titul.

## 1. Shrnutí

- City V2 je **co nejvěrnější klon mechanik Clash of Clans a Rise of Kingdoms**: radnice, která odemyká levely ostatních budov, stavitelé, produkční budovy se sběrem, sklady, upgrady s časovači a zrychlením.
- **Verze 1 = jen vlastní město:** stavění, sběr surovin, upgrady, dekorace. **Bez výroby jednotek, globální mapy a bojů mezi hráči**, ty přijdou později.
- **Budovy zvyšují meta staty**, které platí ve hře (HP, útok, talenty, odměny). V PvP se projeví v segmentu **All-out-power**.
- Modul je sdílený: vyvíjí se v **Mecha Fortress jako staging**, do Hexapolisu se implementuje do 11. 12. 2026 za RC flagem a první hráči ho dostanou v **původním Hexapolisu** v lednu 2027.
- Klonujeme **mechaniky a strukturu**, ne art, názvy ani UI: vlastní tematika a vizuál podle titulu.
- **V MF City V2 nahradí dnešní mapu budov** (Rozhodnuto 6. 11.), žádné dvě paralelní mety. Hráči dostanou refund: *(návrh)* 100 % utracené `HardCurrency` zpět jako gemy a startovní Radnici podle nejvyšší dnešní budovy (max Radnice 5).
- **Gem sinky:** zrychlení, stavitelé, **startovní bundle surovin** (60 gemů *(návrh)*) a **City VIP** (450 gemů na 30 dní *(návrh)*: −15 % času staveb, +1 stavitelská fronta, denní zrychlení 30 min, +20 % produkce).

## 2. Proč klon CoC a RoK

- Obě hry mají **léty ověřenou city meta smyčku**, která drží hráče roky a monetizuje (stavitelé, zrychlení, balíčky surovin, VIP). Nemusíme ji vymýšlet, jen dobře přenést.
- Hráči ji **znají**: nulové učení, okamžitě pochopí radnici, stavitele a sběr.
- Hexapolis hráči dlouhodobě chtějí stavění. MF a další hry nemají žádnou hloubku mety mimo zápas.
- **Jeden modul, všechny hry:** MF reskiny, původní Hexapolis, Hexapolis 2, strategická větev. Vývoj se platí jednou.

## 3. Verze 1: co v ní je

### 3.1 Mechaniky převzaté z CoC a RoK

| Mechanika | Jak funguje | Předloha |
|---|---|---|
| **Radnice** (hlavní budova) | její level určuje max level všech ostatních budov a odemyká nové budovy | CoC Town Hall, RoK City Hall |
| **Stavitelé** | počet souběžných staveb a upgradů; start 2 stavitelé, 3. a 4. za prémiovou měnu nebo nabídku | CoC Builder's Hut, RoK druhý stavitel |
| **Produkční budovy** | průběžně vyrábí surovinu do vlastní kapacity, hráč ji **sbírá klepnutím** | CoC sběrače, RoK farmy a pily |
| **Sklady** | kapacita surovin; upgradem roste | CoC Storage, RoK sklad |
| **Upgrady s časovači** | každý level budovy stojí suroviny a čas, čas roste s levelem | obě |
| **Zrychlení** | prémiová měna nebo předměty zrychlení; krátké stavby do 5 min zdarma *(návrh)* | RoK speedupy, CoC gemy |
| **Volné umístění** na mřížce města, přesouvání budov | obě |
| **Překážky** | stromy a kameny na mapě města, odstranění dává malou odměnu | CoC |
| **Questy kapitol** | vedou hráče stavbou krok za krokem (onboarding) | RoK chapter quests |
| **Dekorace a personalizace** | neprodukční budovy, vzhled, erb, jméno města | obě |

### 3.2 Budovy ve verzi 1 *(návrh, config per titul a tematiku)*

| Budova | Typ | Co dává |
|---|---|---|
| Radnice | hlavní | gating levelů a nových budov |
| Farma, Pila, Lom, Zlatý důl | produkce | jídlo, dřevo, kámen, zlato |
| Sklad | kapacita | limit surovin |
| Chata stavitele | stavitelé | další souběžná stavba |
| **Kasárna** | meta staty | **+HP jednotek** |
| **Kovárna** | meta staty | **+útok jednotek** |
| **Akademie** | meta staty | **+talentové body / sloty** |
| **Svatyně** | meta staty | **+XP hrdinů / jednotek ze zápasu** |
| **Tržiště** | meta staty | **+odměny ze zápasů** (suroviny, měna) |
| Dekorace (2 až 3) | kosmetika | vzhled, IAP sink |

### 3.3 Budovy a meta staty

Budovy, které ovlivňují hru, vrací hostitelské hře **modifikátory**. Hra je aplikuje na start zápasu.

| Budova | Stat ve hře | Příklad hodnot *(návrh)* | Kde platí |
|---|---|---|---|
| Kasárna | HP jednotek | +1 % za level, max +20 % | PvE, PvP All-out-power |
| Kovárna | útok jednotek | +1 % za level, max +20 % | PvE, PvP All-out-power |
| Akademie | talenty | +1 talentový bod každé 3 levely | PvE, PvP All-out-power |
| Svatyně | XP z zápasu | +2 % za level | všude |
| Tržiště | odměny ze zápasu | +2 % za level | všude |

- **PvP Skill only meta staty ignoruje** (stejný setup pro všechny), viz `DESIGN_HEX_PVP.md`.
- V **All-out-power** se projeví celé, férovost drží ligy.
- Mapování statů na konkrétní hru je **config per titul** (v Hexu jednotky a talenty, v MF hradba a hrdinové).

### 3.4 Suroviny a ekonomika

- **Dva zdroje surovin:** zápasy ve hře (kampaň, PvP, odměny z žebříčků) a **pasivní produkce** v městě (klon CoC a RoK). Produkce je doplněk, hlavní příjem jde ze hraní *(návrh, ladit na datech)*.
- Gating: některé levely radnice vyžadují **progres ve hře** (např. dobyté světy, PvP úspěch), aby se hráč vracel do gameplaye.
- Sada surovin a jejich názvy podle tematiky titulu.

### 3.5 Monetizace ve verzi 1

| Sink | Předloha |
|---|---|
| Zrychlení staveb a upgradů | RoK, CoC |
| Další stavitelé | CoC, RoK |
| Balíčky surovin | obě |
| Dekorace a vzhled města | obě |
| Startovní bundle surovin za gemy (Rozhodnuto 6. 11., cena *návrh*) | obě |
| **City VIP** za gemy (Rozhodnuto 6. 11.): zrychlení stavby, stavitelská fronta navíc, denní zrychlení zdarma, bonus produkce; bez auto-sběru *(návrh, BALANC kap. 8.2)* | RoK VIP, CoC Gold Pass |

## 4. Co ve verzi 1 není (pozdější vrstvy)

| Vrstva | Obsah | Předloha | Závislost |
|---|---|---|---|
| Výroba jednotek | kasárna trénují armádu, nemocnice | CoC, RoK | design armád |
| Výzkum | strom technologií v akademii | RoK | po ověření V1 |
| Globální mapa | města ostatních hráčů, sběr na mapě | RoK | SGB profily a persistence |
| Boje mezi hráči | útoky na města, obrana, štíty, hradby | CoC, RoK | PvP vrstva SGB; nejdřív fake útoky, reálné postupně |
| Aliance a klany | společné cíle, pomoc se stavbou | RoK, CoC | SGB clans (F6) |
| Návštěvy měst | prohlédnout si město jiného hráče | CoC | NOX ID |

## 5. Modul a kontrakt s hostitelskou hrou

City V2 je **samostatný modul**. S hrou komunikuje jen přes vstupy, výstupy a požadavky.

| Směr | Co | Příklad |
|---|---|---|
| Vstupy (hra → City) | suroviny, měna, progres, události | odměna za zápas, `match_completed`, `pvp_won` |
| Výstupy (City → hra) | **meta staty**, odměny, boosty | +HP z kasáren, +odměny z tržiště |
| Požadavky | progres ve hře pro levely radnice | "dobyj svět 3" |

Technické zásady:
- Interface ve stylu meta-core DI (`ICityProvider`, `ICityModifierSource`, `ICityRewardSink`), bez závislosti na konkrétní hře.
- Obsah (budovy, ceny, časy, bonusy) **config-driven per titul**; tematika mění jen assety a texty.
- Kill switch přes Firebase RC, dark launch, rollback bez buildu.
- City nikdy neblokuje hru: bez backendu funguje lokálně a synchronizuje později.

## 6. SharedGameBackend

| Co City potřebuje | SGB | Ve V1? |
|---|---|---|
| Perzistence města (časovače, stav) | cloud save | ano (server čas proti podvádění s hodinami *(návrh)*) |
| Identita napříč tituly | NOX ID | ano, pokud bude |
| Odměny | reward bridge (B5) | ano |
| Žebříčky měst, klany, návštěvy, útoky | leaderboards, clans, PvP | ne, pozdější vrstvy |

## 7. Fáze

| Fáze | Kdy | Obsah | Kde |
|---|---|---|---|
| **V1 vývoj** | 11/2026 až 11. 12. 2026 | radnice, stavitelé, 4 produkční budovy, sklad, 5 budov s meta staty, dekorace, questy kapitol, zrychlení, kontrakt, analytika, RC flag | MF staging |
| **Import do Hexu** | do 11. 12. 2026, za RC flagem | napojení meta statů na jednotky a talenty Hexu, Hex suroviny | Hexapolis |
| **Release a ověření** | 1/2027 | hráčům původního Hexapolisu, měření podle kap. 8 | Hexapolis |
| **Náhrada mapy MF** | termín neurčený | City V2 místo `MapBuilding` budov, refund investic (BALANC kap. 11) | Mecha Fortress |
| **V2** | Q1/2027 *(návrh)* | výzkum, víc budov (Radnice 11+), VIP úrovně, výroba jednotek | podle ověření |
| **V3** | od Q2/2027 *(návrh)* | globální mapa, útoky (nejdřív fake), aliance | podle SGB |

## 8. Ověření (vstup pro gate Hexapolis 2)

| Otázka | Metrika | Laťka |
|---|---|---|
| Hrají lidé město? | % DAU v City, staveb na hráče, návraty do City za den | TBD |
| Zlepšuje retenci? | D1, D7, D30 s City proti bez (A/B přes Firebased) | D7 a D30 nahoru, D1 bez poklesu |
| Monetizuje? | konverze na zrychlení, stavitele, balíčky, ARPDAU | TBD |
| Zaplatí si VIP? | konverze na City VIP a bundle (jen iOS a Android mimo Play Pass) | TBD |
| Táhne PvP All-out-power? | útrata a aktivita hráčů s vyššími meta staty | sledovat |

Referenční čísla MF (okno 20. 5. až 13. 7. 2026): D1 26,5 %, D7 10,1 %, D30 4,2 %, podíl IAP asi 20 %.

## 9. Rizika

- **Produkční laťka CoC a RoK.** Mají roky obsahu. V1 držet malou: méně budov, víc levelů.
- **Klon mechanik, ne assetů.** Vlastní art, názvy a UI; žádné převzaté vizuály ani texty.
- **Meta staty rozbijí balanc** PvE i PvP All-out-power. Hodnoty v RC, strop bonusů, telemetrie.
- **Ekonomika ve dvou hrách naráz** (MF a Hex). Config per titul je podmínka.
- **Náhrada mapy MF:** refund a ztráta produkce Gem Mine mění přírůstek gemů hráčů MF; před releasem v MF spočítat z dat (BALANC kap. 11).
- **Import do starého Hexapolisu.** Ověřit při CODE-65.
- **Termín leden 2027** při běžícím live ops Q4.

## 10. Slabá místa a otevřené otázky

Rizika provedení jsou v kap. 9. Tady jsou námitky proti tomu, jestli je samotný návrh správně.

| Námitka | Proč může platit | Odpověď nebo co s tím |
|---|---|---|
| Tempo města je spočítané na MF, ne na Hex | `BALANC_CITY_V2.md` počítá s 6 zápasy denně a gatingem podle MF stage indexu. Zápas v Hexu trvá desítky minut (PvP Normal 15 až 25 min), takže příjem ze zápasů (17 000 až 210 000 surovin denně podle tieru) v Hexu nedorazí a město se zasekne, nebo tlačí jen do nákupu. Ekvivalent gatingu pro Hex chybí. | Před importem přepočítat model pro Hex s mediánem zápasů denně z telemetrie (BALANC otázky 6 a 7). Pro Hex nastavit vlastní tabulku časů a cen přes RC. |
| Druhá stavební meta vedle dnešní mapy MF | MF má systém budov na mapě (`MapBuilding`: Gold Mine, Wall s talenty a další) s upgrady za `HardCurrency` 240 až 1 080. City V2 platí upgrady surovinami a gemy bere jen za zrychlení. V MF (cca 39 % revenue portfolia) hrozila buď dvě paralelní mety, nebo ztráta gem sinku i investic hráčů. | **Rozhodnuto 6. 11.:** City V2 dnešní mapu nahradí, hráči dostanou refund. Pravidlo *(návrh)*: 100 % `HardCurrency` zpět jako gemy + startovní Radnice podle nejvyšší budovy (max 5). Gem sink nahrazují stavitelé, zrychlení, bundle surovin a City VIP (BALANC kap. 8 a 11). Zbývá: dorovnat produkci Gem Mine a ověřit z dat výši refundů. |
| V1 bez sociální vrstvy netestuje smyčku CoC a RoK | CoC a RoK drží hráče hlavně útoky, obranou, klany a mapou. V1 je město s časovači a bonusy, blíž idle základně. Slabý výsledek V1 nic neřekne o plné smyčce a dobrý výsledek ji nepotvrdí. | V gate hodnotit V1 jako test "chtějí hráči Hexu stavět", ne jako test celé CoC smyčky. Útoky a globální mapa (V3) potřebují vlastní ověření. |
| Monetizaci města v Hexu skoro nejde změřit | Zrychlit celou verzi 1 stojí asi 15 100 gemů (cca 250 USD). Hexapolis má cca 7 tis. aktivních hráčů a je v Play Passu, kde předplatitelé gemy nekupují. Konverze na stavitele #3 (2 až 4 %) je předpoklad. | **Rozhodnuto 6. 11.:** Play Pass se do revenue nepočítá, monetizaci měřit jen na iOS a Androidu mimo Play Pass. Vzorek bude malý, takže monetizaci (bundle, stavitelé, City VIP) ověřit hlavně v MF po náhradě mapy. |
| Bonusy z města zasahují do hotové kampaně | Na maximu verze 1 dává město ×1,44 efektivní síly a platí i v PvE. Kampaně MF i Hexu jsou vybalancované bez něj; zlehčení zkrátí obsah a sníží hodnotu dnešních nákupů síly. | Rozhodnout, jestli bonusy platí v PvE, nebo jen v PvP All-out-power. Když v PvE, nižší strop přes RC a hlídat win rate kampaně (BALANC kap. 9). |
| "Co nejbližší klon" CoC a RoK | Mechaniky chránit nejdou, ale struktura obrazovek, ikonografie a pojmenování (Chata stavitele, questy kapitol) snadno sklouznou k podobnosti, kterou si všimne store review, komunita i Supercell. Hráči Hexu chtějí civilizaci, ne CoC v jiném obalu. | Art a UI review proti CoC a RoK před releasem. Ve store a kampani slovo "klon" ani odkazy na CoC nepoužívat. Město tematicky navázat na národ v Hexu. |

**Potřebuje odpověď:**
- Kdy jde City V2 k hráčům MF jako náhrada mapy? (Nahradit s refundem: Rozhodnuto 6. 11.)
- Potvrdit pravidlo refundu a ceny bundle a City VIP (BALANC kap. 8.1, 8.2, 11).
- Kolik zápasů denně hraje medián aktivního hráče Hexu (model počítá 6)?
- Platí bonusy z města i v PvE kampani?
- Kdo udělá art budov v tématu Hexu, když je grafika vytížená?
- Stačí V1 bez sociální vrstvy na rozhodnutí o Hexapolis 2 a o City V2 v reskinech, nebo se čeká na data z V3?

## 11. Otevřené otázky

1. Kdo vlastní City V2 (design, vývoj)? Tým pro Hex featury je rozhodnutý 6. 11. (Mirek, Kubík (Jakub H.), David), zbývá rozdělit featury.
2. Release v lednu jen v Hexapolisu, nebo i v MF? (V MF City V2 nahradí mapu, termín neurčený.)
3. Jaké meta staty v Hexu přesně (jednotky, talenty, hrdinové) a jaké stropy?
4. Jsou CODE-9 a CODE-65 totéž co City V2, sloučit backlog?
5. City VIP je rozhodnuté jako gem sink (6. 11.). Zbývá: zapnout ho už ve V1 *(návrh: ano, za RC flagem)*, nebo až ve V2?
6. Laťky v kap. 8 pro gate Hexapolis 2.
