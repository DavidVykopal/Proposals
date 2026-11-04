# Produkční strategie NOXGAMES 2027

> **Stav:** pracovní verze 5, 4. 11. 2026 večer (HexFort zrušen a obnova původního Hexu, PvP v2 se segmenty Skill only a All-out-power, City V2 jako klon CoC a RoK, CPI pipeline, NoxEngine 0.2). Verze 4: monetizační důvod, snížení rizika, postupný náběh PvP podle Voodoo. Zdroj: voice note Davida (`voice/Strategie.txt`, surový přepis Whisper) + Q4 OKR + exec porada 24. 9.
> **Zdroj pravdy:** tento MD. Z něj vychází: tasky v NoxHubu, wiki (kategorie Strategie), prezentace pro vedení.
> **Detailní dokumenty:** `KONCEPT_OBNOVA_HEXU.md`, `DESIGN_HEX_PVP.md`, `DESIGN_CITY_V2.md`, `KONCEPT_STRATEGICKA_VETEV.md`, `CPI_PIPELINE.md`, `SHRNUTI_NOXENGINE.md`.

## Shrnutí v pěti větách

1. MF-branch (Mecha Fortress, Command, Sector) má **ověřený recept na rychle splatnou hru**. Gameplay už neiterujeme, v 2027 vydáme **2 až 3 reskiny** se silnými tématy vybranými přes CPI testy.
2. Sdílená práce, která podpoří současné i budoucí hry: **City V2 meta** a **SharedGameBackend**.
3. **Hexapolis zůstává civilization-like. HexFort rušíme** a práci vracíme do původního Hexu: přidáme PvP, City V2 a UGC a ověříme, že to hráči chtějí a zaplatí. Když funguje celek, navrhneme **nový Hexapolis 2: hex gameplay na MF metě**.
4. Otevíráme **strategickou větev**: hry mezi složitým Hexem a jednoduchým Mecha Fortressem, víc idle s většími rozhodnutími, PvP tam, kde přirozeně sedí. Cíl 2027: **aspoň 2 unikátní tituly**.
5. Cíl 2027 je **až 5 nových titulů** (2 reskiny + 2 strategické tituly + Hexapolis 2, ten jen když projde gate). Všechny stojí na tom, co už máme nebo dotáhneme letos, takže jde o posun produkce bez velkého neověřeného rizika. Nové tituly mají nahradit slábnoucí hry z roku 2026.

## Produkty 2027 na jedné stránce

| Produkt | Větev | Myšlenka | Kdy | Stav 4. 11. | Detail |
|---|---|---|---|---|---|
| **Reskin #1** (Mecha Fortress / Sector Defense) | MF-branch | ověřený MF recept, nové silné téma, stejná kvalita | téma z CPI do 15. 12., výroba od I 2027, launch II až III | CPI test cíle A se připravuje | `CPI_PIPELINE.md` |
| **Reskin #2 (a #3)** | MF-branch | dtto, téma z dalších CPI testů | Q2 až Q4 2027 | 2, nebo 3 reskiny je otevřené | `CPI_PIPELINE.md` |
| **Obnova Hexapolisu** (PvP, City V2, UGC) | Hexapolis | ověřit v živé hře, co hráči chtějí: hrát proti sobě, stavět, tvořit mapy | vývoj XI až XII, hráči I 2027, UGC II 2027 | design hotový | `KONCEPT_OBNOVA_HEXU.md` |
| **Hexapolis 2** | Hexapolis | nový projekt: hex gameplay na MF metě (HexFort zrušen) | rozhodnutí II až III 2027, vývoj Q2 až Q4 jen po gate | čeká na data z obnovy | `KONCEPT_OBNOVA_HEXU.md` |
| **Strategický titul #1** | strategická větev | mezi Hexem a MF: víc idle, větší rozhodnutí, PvP od prvního dne | greenlight II až III, výroba Q2 až Q4 | prototyp Warcamp na NoxEngine | `KONCEPT_STRATEGICKA_VETEV.md` |
| **Strategický titul #2** | strategická větev | druhý unikátní titul větve | prototyp Q2 až Q4 2027 | koncepty, Game Jam | `KONCEPT_STRATEGICKA_VETEV.md` |
| City V2 | sdílené | klon Clash of Clans a Rise of Kingdoms, budovy zvyšují meta staty | V1 XI až XII, Hex I 2027, reskiny od II | design hotový | `DESIGN_CITY_V2.md` |
| SharedGameBackend | sdílené | Nox ID, žebříčky, klany, PvP backend pro všechny hry | průběžně, staging v MF | integrace do MF běží | |
| NoxEngine + Warcamp | experiment | vlastní engine a agent-first workflow (Czode) | časově omezená sázka s kill gates | 0.2 proof of concept | `SHRNUTI_NOXENGINE.md` |
| CPI pipeline | podpora | 1 až 2 testy měsíčně, vlastní knihovna nápadů | test A do 15. 12., test B do 15. 1. | úkoly CPI-17 až CPI-26 | `CPI_PIPELINE.md` |

## Proč PvP a silná sociální vrstva: monetizace a snížení rizika

**Dnes:** celé portfolio jsou PvE hry se slabou sociální vrstvou. Hráč soutěží jen se hrou nebo sám se sebou.

**Co nám chybí:** segment hráčů, kteří utrácejí, aby předehnali jiné lidi. Jde o pozici v žebříčku, sílu klanu, místo na globální mapě a o to, kdo do hry dá víc. V PvE hře nemají proti komu utrácet, takže jejich útrata má strop. Tenhle typ hráče dnes nemonetizujeme vůbec.

**Co to změní:** PvP a silné sociálno (klany, armády, globální svět, leaderboardy) otevírají monetizaci, kterou dnes nemáme. Soupeření mezi hráči posouvá útratu bez pevného stropu, to je model Rise of Kingdoms a Clash of Clans. Je to hlavní obchodní důvod, proč:
- strategická větev má PvP v designu od prvního dne,
- City V2 nese sociální vrstvu (globální mapa, armády, útoky) a je ve všech hrách,
- SharedGameBackend dodává klany, leaderboardy a Nox ID napříč tituly,
- gate pro Hexapolis 2 měří, jestli hráči PvP hrají a platí za něj.

**Druhá výhoda, snížení rizika:** vyrobit offline PvE hru je díky AI čím dál levnější a jednodušší, pro konkurenci i pro samotné hráče. Čistě PvE titul se tak bude čím dál snáz kopírovat a nahrazovat. Co se levně zkopírovat nedá, je **velká základna hráčů, komunita, klany a živý globální svět**. Soupeř je pro hráče hodnota jen tam, kde jsou ostatní hráči. Tahle hodnota roste s každým titulem napojeným na SharedGameBackend (Nox ID, klany napříč hrami). PvP a sociálno jsou tedy kromě monetizace i naše obrana: přidanou hodnotou nebude jen hra, ale lidé v ní.

**Kde soutěžní útrata žije:** PvP v Hexu má dva segmenty (`DESIGN_HEX_PVP.md`): **Skill only** je férový souboj se stejným setupem, výhoda se tam koupit nedá; **All-out-power** pouští do hry sílu jednotek, talentů a města, férovost drží 5 lig. Další prostor pro soupeření v útratě je v City V2 (síla města a armády, globální mapa, klanové války, žebříčky moci) a ve strategické větvi, kde to navrhujeme od začátku. Kde je hranice mezi "pay to compete" a férovým PvP, se rozhoduje titul po titulu.

**PvP postupně, podle best practices Voodoo:** s PvP počítáme ve všech nových hrách, ale reálné PvP nezapínáme hned. Platí pro strategickou větev, PvP v Hexu i útoky na města v City V2:
1. **Launch a soft launch: fake PvP.** Hráč hraje proti botům nebo uloženým armádám a městům jiných hráčů (async "ghost" zápasy), prezentovaným jako soupeři. Nepotřebujeme velkou hráčskou základnu, nikdo nečeká ve frontě a obtížnost i win rate máme pod kontrolou.
2. **I v produkční hře je onboarding fake.** Prvních několik zápasů (výchozí 3 až 5, ladí se přes remote config) jsou vždy boti nastavení tak, aby hráč pochopil hru a vyhrál. Do reálného soupeře se nedostane nový hráč, který ještě neumí hrát.
3. **Reálné PvP až postupně.** Zapíná se podle velikosti hráčské základny a postupu hráče, typicky od vyšších lig nebo po dokončení onboardingu. Když na daném MMR není soupeř včas, párujeme dál s ghost armádami nebo boty.

Důvod: reálné PvP na malé základně znamená čekání, nevyrovnané zápasy a prohry hned na začátku, což zabíjí retenci. Fake PvP dává pocit soupeření od prvního dne a reálné PvP přidáváme, až má z čeho párovat. Nastavení (počet fake zápasů, kdy se zapíná reálné PvP, podíl botů) je za remote config a ladí se A/B testy.

## Sdílený základ všech her

| Prvek | Co to je | Pro koho |
|---|---|---|
| **City V2 meta** (= Mapa V2, Město V2, stejná feature) | Samostatný modul budování města mezi zápasy, inspirace Rise of Kingdoms a Clash of Clans. Se základní hrou komunikuje přes vstupy, výstupy a požadavky. Detail: `DESIGN_CITY_V2.md` | MF reskiny, původní Hexapolis, Hexapolis 2, strategická větev |
| **SharedGameBackend** | Jeden backend pro všechny tituly: Nox ID (tracking hráčů napříč tituly), invite friends, klany, leaderboardy, promo kódy. Pod jednou střechou, ovládaný agenty, na míru našim hrám, cesta k automatizaci live-ops | Všechny hry |
| **MF meta** | Vyvinutá meta MF-branch | MF reskiny, strategická větev |

**Mecha Fortress je staging projekt** pro City V2 a SharedGameBackend (včetně backendu PvP). Feature se vyvine tam, pak se importuje do dalších her. PvP samotné se staví přímo v původním Hexu.

## Vývojový přístup: maximum schopností agentů (experiment NoxEngine)

Cíl: co nejvíc zrychlit vývoj nových titulů tím, že agenti zvládnou co největší část práce sami. Proto od 2. 11. 2026 běží rychlý YOLO experiment: **vlastní engine NoxEngine a na něm první prototyp strategické hry (Warcamp)**, s workflow podle Czodeho, kde engine ovládají agenti. NoxHub: CODE-217 (CE0) v epicu Custom Engine. Shrnutí pro vedení: `SHRNUTI_NOXENGINE.md`.

- **Rust:** agenti v něm píšou dobře. Kompilátor zachytí většinu chyb ještě před spuštěním hry, agent dostane přesnou chybu a opraví ji ve smyčce napiš, sestav, oprav. Jeden kód pro iOS, Android i web, bez GC záseků na mobilu.
- **Obsah jako data:** jednotky, budovy, karty, schopnosti, balanc i skiny jsou v JSON s hot reloadem. Agent nebo designér změní data a hned to vidí. **Reskin = jiná složka skinů se stejnou logikou**, což přímo zrychluje prototypy i reskiny.
- **Knihovny místo psaní:** rendering (wgpu), UI a editor (egui), matematika a modely jsou hotové open-source knihovny. Píšeme jen to, co dělá engine naším: obrazovky a okna, data, MCP, editor a agenty.
- **SDK třetích stran** (MAX, Singular, Firebase, IAP) přes tenký nativní most pro každou platformu. SharedGameBackend je čisté HTTP, funguje všude.

**Stav a riziko (4. 11.):** verze 0.2 běží na webu, jako Android APK a v iOS simulátoru, s online PvP na Cloudflare. Reklamní a attribution SDK jsou zatím jen mocky a výkon na reálném telefonu ani rychlost vývoje proti Unity nejsou změřené; největší neznámá je napojení reálných SDK na iOS a Androidu (CE6, CE12). Srovnání s alternativami je v `RESEARCH.md`; NoxEngine je pracovní směr s kill gates, ne rozhodnutí. Go / no-go: CE13.

**Vztah ke strategii:** jde hlavně o strategickou větev, kde se dělají nové tituly od nuly. MF reskiny a Hexapolis zůstávají v Unity, dokud experiment neprokáže, že je to rychlejší a mobilní SDK fungují.

## Větev 1: MF-branch reskiny

- Gameplay MF-branch neiterujeme, máme potvrzený recept.
- **2 až 3 reskiny v 2027** (NoxHub: NOVE-11, NOVE-12) se silnými tématy, ve stejné kvalitě jako dosud, ideálně s něčím navíc.
- City V2 a SharedGameBackend se do reskinů integrují postupně, až budou hotové.
- **Postup:** CPI testy tématik spustit ještě do konce 2026 → leden příprava → výroba.
- Kandidátní témata v CPI testu cíle A: Warcraft fantasy (CPI-9), zombie bunkr (CPI-10), dračí doupě (CPI-21), plastoví vojáčci (CPI-22). Detail: `CPI_PIPELINE.md`.

## Větev 2: Hexapolis a Hexapolis 2

**Pozice:** nabídnout nejlepší civilization-like gameplay na mobilu. Hex neměníme na pasivní/idle hru.

**HexFort jako projekt Hexapolis 2 rušíme** (rozhodnutí Davida, 4. 11. 2026). Bez ověření je to příliš velké riziko. Práce se vrací do **původního Hexapolisu**: tam si vyzkoušíme UGC, PvP a mapu (City V2). Teprve když to bude fungovat jako celek, udělá se **design hex gameplaye nasazeného na MF metu** a podle něj nový projekt Hexapolis 2. Celý plán obnovy: `KONCEPT_OBNOVA_HEXU.md`.

**Co nechceme:** vzít metu z Mecha Fortressu a bez ověření ji naroubovat na současný Hex.

**Co hráči chtějí a co přidáváme do původního Hexu (feature po feature):**

| Feature | Proč | Kde se vyvíjí | Detail |
|---|---|---|---|
| **City V2** (stavění města mezi zápasy) | hráči to vždycky chtěli, dlouhodobá motivace | Mecha Fortress (staging) → import do Hexu | `DESIGN_CITY_V2.md` |
| **PvP** | Polytopia nás dnes poráží hlavně tím, náskok lze rychle smazat | přímo v Hexapolisu, backend na SharedGameBackendu (staging MF) | `DESIGN_HEX_PVP.md` |
| **UGC** (vlastní mapy, sdílení, live-ops nad nimi) | součást ověření celku, nasazuje se po PvP a City V2 | přímo v Hexapolisu (interní editor map) | `DESIGN_HEX_PVP.md`, sekce UGC |
| Suroviny na hex mapě | drobnost z poznámek | Hex | task |

**Časování:** listopad 2026 vývoj → prosinec dodání a interní test → leden 2027 vydání hráčům, test s komunitou, pokus o re-engagement hráčů, kteří odešli.

**Co ověřujeme (gate pro Hexapolis 2):**
- hráči interagují se stavěním města,
- hráči hrají PvP,
- hráči tvoří a hrají vlastní mapy (UGC),
- hráči za to platí (IAP, případně subscription).

Rozhoduje to, jestli funguje **celek**, ne jedna featura.

**Hexapolis 2 po ověření:** nový projekt (ne HexFort), **hex gameplay nasazený na MF metu**. Pořád plnohodnotný civilization-like, upravená a zjednodušená meta, pravděpodobně jiná tématika, design od začátku pro PvP a dlouhodobé hraní přes město. "To, čím měl Hexapolis vždycky být."

**Idle spin-off Hexu** (hexová strategie, ale víc idle) nepatří sem, ale do strategické větve.

## Větev 3: Strategická větev

Detail: `KONCEPT_STRATEGICKA_VETEV.md` (NoxHub: NOVE-10).

- **Esence:** Hexapolis je moc složitý, Mecha Fortress moc jednoduchý. Mezi nimi je prostor.
- Stojí na MF metě, City V2, SharedGameBackend a sociálních features.
- Gameplay: víc idle než MF, ale s většími rozhodnutími. Zápasy na kola nebo vlny: hráč udělá několik rozhodnutí, použije itemy, pak sleduje výsledek.
- **Obchodní důvod:** dnes máme jen PvE a slabé sociálno, takže nemonetizujeme hráče, kteří soutěží v tom, kdo víc utratí. PvP a sociální vrstva tuhle mezeru zavírají (viz sekce Proč PvP a silná sociální vrstva).
- PvP tam, kde přirozeně sedí, ne na sílu. Na launchi fake PvP (boti a ghost armády), reálné PvP až postupně (viz sekce Proč PvP, PvP postupně). Reference: Mechabellum, Clash Royale, Voodoo base + minion battlery, Goblin Gold Miners.
- Jde snadno PvE i PvP, hodně prostoru pro experimenty a tweaky.
- Tým to baví, na Game Jamu chce řada lidí dělat Mechabellum-style hry.
- **První prototyp běží:** Warcamp na vlastním enginu NoxEngine 0.2: PvP lane battler s metou jako MF (trofeje, truhly, levely jednotek, City V2, 4 skiny). Detail: `SHRNUTI_NOXENGINE.md`.
- **Cíl 2027:** aspoň 2 unikátní tituly.

## CPI testy

Stálá pipeline: **aspoň 1 test měsíčně, podle potřeby 2**, jeden test běží asi 14 dní. Každý test kombinuje **strukturu / gameplay, vizuální styl a téma** a odpovídá na konkrétní cíl. Výsledky se skládají do vlastní knihovny nápadů. Detail: `CPI_PIPELINE.md`.

| Cíl | Otázka | Varianty prvního testu | Termín | NoxHub |
|---|---|---|---|---|
| **A: MF reskiny** | které téma a styl dají nejnižší CPI pro stejný MF gameplay | Warcraft fantasy, zombie bunkr, dračí doupě, plastoví vojáčci | do 15. 12. 2026 | CPI-11, CPI-14 |
| **B: Hexapolis 2 a strategická větev** | které téma a styl nahradí vizuál Hexapolisu | římská říše, Warcraft fantasy, vikingové, kolonie na cizí planetě | do 15. 1. 2027 | CPI-12, CPI-16 |

## Roadmapa

| Období | MF-branch | Hexapolis | Strategická větev | Sdílené a podpora |
|---|---|---|---|---|
| **XI 2026** | brief a kreativy CPI testu cíle A | vývoj PvP přímo v Hexu, City V2 V1 ve stagingu MF | Warcamp na NoxEngine 0.2, koncepty, Game Jam | SGB integrace do MF (PvP backend, žebříčky) |
| **XII 2026** | CPI test cíle A, výběr témat (do 15. 12.) | import City V2 do Hexu, interní a komunitní test | sada assetů pro CPI cíl B | City V2 V1 hotové |
| **I 2027** | start reskinu #1 | **PvP a City V2 k hráčům**, reaktivační kampaň | prototypy (max 2 sprinty na koncept), CPI test cíle B (do 15. 1.) | NoxEngine kill gates |
| **II až III 2027** | reskin #1 výroba a launch | **UGC k hráčům**, data, **rozhodnutí o novém Hexapolis 2** | greenlight titulu #1 | City V2 do reskinů, CPI 1 až 2 testy měsíčně |
| **Q2 až Q4 2027** | reskin #2 (a #3) | Hexapolis 2 vývoj (hex gameplay na MF metě), jen pokud gate projde | titul #1 výroba, titul #2 prototyp | City V2 V2 a V3 (jednotky, mapa, útoky) |

Roadmapa od února dál je orientační, upřesní se po CPI testech a datech z obnovy Hexu.

## Otevřené otázky (neblokují start)

1. **Vlastníci:** kdo vede City V2, PvP v Hexu, strategickou větev a CPI program? Voice note jména neuvádí.
2. **Reskiny:** 2, nebo 3? V NoxHubu jsou zatím 2 (NOVE-11, NOVE-12).
3. **Kapacita:** listopad až prosinec souběžně City V2, PvP, SGB a CPI. Kdo na čem?
4. **Gate pro Hex 2:** jaká čísla (podíl hráčů v PvP, D30, ARPDAU, konverze na subscription) stačí na schválení?
5. **Rise of a Nation** (`Hexapolis_India/`): sdílí kód nebo City V2 s Hexapolisem?

## Výstupy

- [x] Surový přepis: `voice/Strategie.txt`
- [x] Strategický dokument (tento)
- [x] Design dokumenty City V2 (v2), PvP v Hexu (v2), koncept strategické větve, koncept obnovy Hexu, CPI pipeline, shrnutí NoxEngine
- [x] Tasky v NoxHubu: NOVE-13 až NOVE-38, CPI-13 až CPI-26 (subtasky pod NOVE-1, 5, 7, 9, 10, 11, 12 a CPI-11, 12, 13)
- [x] Wiki: Strategie / Produkční strategie 2027 (5 stránek)
- [x] Prezentace pro vedení: `strategie-2027-prezentace.html` (draft, 22 slidů)
- [ ] Porada vedení: rozhodnout vlastníky, kapacitu, 2 nebo 3 reskiny, čísla pro gate Hex 2 (NOVE-19)

## Wiki stránky
- [Produkční strategie 2027 (přehled)](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=e6497b8c-3f2c-406c-a8d2-8a023e66e3bd)
- [City V2 meta: design dokument](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=40baabfd-d09b-4007-8a25-3a58f49ee1b7)
- [Obnova Hexapolisu: koncept](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=4a9efa9b-9fa0-491a-8293-ddf409a3c176)
- [PvP v Hexapolisu: design dokument](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=1289bcaf-4811-484e-a5cb-d59c9d870d20)
- [Strategická větev: koncept](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=19838dbd-8e92-401b-b4d2-28b79b4f7b11)
