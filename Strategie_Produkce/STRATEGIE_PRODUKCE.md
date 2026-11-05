# Produkční strategie NOXGAMES 2027

> **Stav:** pracovní verze 6, 6. 11. 2026: nová kapitola Jak vydat aspoň 5 titulů v 2027 (definice titulu, slate 3 reskiny + 2 nové tituly, kapacita po rolích, pořadí škrtů, KPI), rozdělení lidí z 6. 11. Verze 5 ze 4. 11. 2026 večer, doplněno 5. 11. (SGB nejdřív v Mecha Fortress s releasem do 11. 12.; PvP, City V2 i UGC v původním Hexu implementované do 11. 12. za RC flagy; release freeze 14. až 18. 12. kvůli GameJamu; ceník 60 gemů = 1 USD). Verze 5: HexFort zrušen a obnova původního Hexu, PvP v2 se segmenty Skill only a All-out-power, City V2 jako klon CoC a RoK, CPI pipeline, NoxEngine 0.2). Verze 4: monetizační důvod, snížení rizika, postupný náběh PvP podle Voodoo. Zdroj: voice note Davida (`voice/Strategie.txt`, surový přepis Whisper) + Q4 OKR + exec porada 24. 9.
> **Zdroj pravdy:** tento MD. Z něj vychází: tasky v NoxHubu, wiki (kategorie Strategie), prezentace pro vedení.
> **Detailní dokumenty:** `KONCEPT_OBNOVA_HEXU.md`, `DESIGN_HEX_PVP.md`, `BALANC_HEX_PVP.md`, `DESIGN_CITY_V2.md`, `BALANC_CITY_V2.md`, `KONCEPT_STRATEGICKA_VETEV.md`, `CPI_PIPELINE.md`, `SHRNUTI_NOXENGINE.md`.

## Shrnutí v pěti větách

1. MF-branch (Mecha Fortress, Command, Sector) má **ověřený recept na rychle splatnou hru**. Gameplay už neiterujeme, v 2027 vydáme **3 reskiny** se silnými tématy vybranými přes CPI testy.
2. Sdílená práce, která podpoří současné i budoucí hry: **City V2 meta** a **SharedGameBackend**.
3. **Hexapolis zůstává civilization-like. HexFort rušíme** a práci vracíme do původního Hexu: přidáme PvP, City V2 a UGC a ověříme, že to hráči chtějí a zaplatí. Když funguje celek, navrhneme **nový Hexapolis 2: hex gameplay na MF metě**.
4. Otevíráme **strategickou větev**: hry mezi složitým Hexem a jednoduchým Mecha Fortressem, víc idle s většími rozhodnutími, PvP tam, kde přirozeně sedí. Cíl 2027: **aspoň 2 unikátní tituly**.
5. Cíl 2027 je **aspoň 5 nových titulů v soft launchi**: 3 reskiny, strategický titul #1 a titul #5 (strategický #2 nebo koncept z GameJamu). Hexapolis 2 jen když projde gate, a pak místo titulu #5 nebo nad plán. Jak to 16 lidí zvládne, je v kapitole Jak vydat aspoň 5 titulů v 2027. Všechny stojí na tom, co už máme nebo dotáhneme letos, takže jde o posun produkce bez velkého neověřeného rizika. Nové tituly mají nahradit slábnoucí hry z roku 2026.

## Produkty 2027 na jedné stránce

| Produkt | Větev | Myšlenka | Kdy | Stav 4. 11. | Detail |
|---|---|---|---|---|---|
| **Reskin #1** (Mecha Fortress / Sector Defense) | MF-branch | ověřený MF recept, nové silné téma, stejná kvalita | téma z CPI do 15. 12., výroba I až II 2027, soft launch III, global V | CPI test cíle A se připravuje | `CPI_PIPELINE.md` |
| **Reskin #2 a #3** | MF-branch | dtto, téma z dalších CPI testů, reskinová linka | #2 soft launch VI, #3 soft launch X 2027 | plán počítá se 3 reskiny, v NoxHubu zatím 2 | `CPI_PIPELINE.md` |
| **Obnova Hexapolisu** (PvP, City V2, UGC) | Hexapolis | ověřit v živé hře, co hráči chtějí: hrát proti sobě, stavět, tvořit mapy | implementace všech tří do 11. 12. za RC flagy, hráči PvP a City V2 I 2027, UGC II 2027 | design hotový | `KONCEPT_OBNOVA_HEXU.md` |
| **Hexapolis 2** | Hexapolis | nový projekt: hex gameplay na MF metě (HexFort zrušen) | gate III 2027; když projde, bere slot titulu #5 nebo jde nad plán s externí kapacitou, soft launch nejdřív XII | čeká na data z obnovy | `KONCEPT_OBNOVA_HEXU.md` |
| **Strategický titul #1** | strategická větev | mezi Hexem a MF: víc idle, větší rozhodnutí, PvP od prvního dne | Q1 prototypy, greenlight III, výroba IV až VIII, soft launch IX, global XI | prototyp Warcamp na NoxEngine | `KONCEPT_STRATEGICKA_VETEV.md` |
| **Titul #5** (strategický #2 nebo z GameJamu) | strategická větev | druhý nejlepší prototyp z Q1, stojí na kódu titulu #1 | výroba IX až XI, soft launch XII 2027 | koncepty, Game Jam | `KONCEPT_STRATEGICKA_VETEV.md` |
| City V2 | sdílené | klon Clash of Clans a Rise of Kingdoms, budovy zvyšují meta staty | V1 do 11. 12. (staging MF, import do Hexu za RC flagem), hráči Hexu I 2027, reskiny od II | design hotový | `DESIGN_CITY_V2.md` |
| SharedGameBackend | sdílené | Nox ID, žebříčky, klany, PvP backend pro všechny hry | nejdřív Mecha Fortress (rozhodnuto 5. 11.), release do 11. 12., pak další hry | integrace do MF běží | |
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

**Rozhodnuto 6. 11.:** NoxEngine je letos čistě experiment (David a Čoud), rozšiřovat ho jde během GameJamu. Plán 5 titulů s ním nepočítá.

**Vztah ke strategii:** jde hlavně o strategickou větev, kde se dělají nové tituly od nuly. MF reskiny a Hexapolis zůstávají v Unity, dokud experiment neprokáže, že je to rychlejší a mobilní SDK fungují.

## Větev 1: MF-branch reskiny

- Gameplay MF-branch neiterujeme, máme potvrzený recept.
- **3 reskiny v 2027** (NoxHub: NOVE-11, NOVE-12, třetí založit) se silnými tématy, ve stejné kvalitě jako dosud, ideálně s něčím navíc. Soft launch III, VI a X; při skluzu titulu #5 i čtvrtý (kapitola Jak vydat aspoň 5 titulů v 2027).
- **Reskinová linka:** jedna kódová základna MF-branch, téma jako sada assetů a konfigurace, stejný checklist a publishing. Grafika přes AI pipeline a outsourcing.
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

**Časování:** listopad a začátek prosince vývoj → **do 11. 12. 2026 PvP, City V2 i UGC implementované za RC flagy** → 14. až 18. 12. release freeze (GameJam) → leden 2027 PvP a City V2 hráčům, test s komunitou, pokus o re-engagement hráčů, kteří odešli → únor 2027 UGC hráčům.

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
- **Cíl 2027:** aspoň 2 unikátní tituly: titul #1 se soft launchem IX a titul #5 se soft launchem XII. Oba vzejdou z Q1 prototypů (Warcamp a koncepty z GameJamu). Když titul #5 nestihne, nahradí ho reskin a cíl 2 unikátních titulů se nesplní.

## CPI testy

Stálá pipeline: **aspoň 1 test měsíčně, podle potřeby 2**, jeden test běží asi 14 dní. Každý test kombinuje **strukturu / gameplay, vizuální styl a téma** a odpovídá na konkrétní cíl. Výsledky se skládají do vlastní knihovny nápadů. Detail: `CPI_PIPELINE.md`.

| Cíl | Otázka | Varianty prvního testu | Termín | NoxHub |
|---|---|---|---|---|
| **A: MF reskiny** | které téma a styl dají nejnižší CPI pro stejný MF gameplay | Warcraft fantasy, zombie bunkr, dračí doupě, plastoví vojáčci | do 15. 12. 2026 | CPI-11, CPI-14 |
| **B: Hexapolis 2 a strategická větev** | které téma a styl nahradí vizuál Hexapolisu | římská říše, Warcraft fantasy, vikingové, kolonie na cizí planetě | do 15. 1. 2027 | CPI-12, CPI-16 |

## Roadmapa

| Období | MF-branch | Hexapolis | Strategická větev | Sdílené a podpora |
|---|---|---|---|---|
| **XI 2026** | brief a kreativy CPI testu cíle A | vývoj PvP přímo v Hexu, City V2 V1 ve stagingu MF | Warcamp na NoxEngine 0.2, koncepty | SGB integrace do MF (PvP backend, žebříčky) |
| **XII 2026** | CPI test cíle A, výběr témat (do 15. 12.) | do 11. 12. PvP, City V2 a UGC v Hexu za RC flagy, pak interní a komunitní test | Game Jam 14. až 18. 12., sada assetů pro CPI cíl B | SGB v MF release a City V2 V1 hotové do 11. 12., release freeze 14. až 18. 12. |
| **I 2027** | výroba reskinu #1 | **PvP a City V2 k hráčům**, reaktivační kampaň | Q1 prototypy (Warcamp + koncepty z GameJamu, max 2 sprinty na koncept), CPI test cíle B (do 15. 1.) | NoxEngine kill gates, outsourcing grafiky vybraný do 31. 1. |
| **II až III 2027** | **reskin #1 soft launch III**, pre-produkce reskinu #2 | **UGC k hráčům**, data, **rozhodnutí o novém Hexapolis 2** | greenlight titulu #1, kandidát na titul #5 | City V2 do reskinů, CPI 1 až 2 testy měsíčně, kontrolní bod kapacity |
| **IV až VI 2027** | reskin #2 výroba, **soft launch VI**; reskin #1 global V | Hexapolis 2 design, jen pokud gate projde | titul #1 výroba | City V2 V2 (jednotky) |
| **VII až IX 2027** | reskin #3 výroba; reskin #2 global VIII | Hexapolis 2 jen místo titulu #5 nebo s externí kapacitou | **titul #1 soft launch IX**, titul #5 pre-produkce a výroba | City V2 V3 (mapa, útoky) |
| **X až XII 2027** | **reskin #3 soft launch X**, global XII; záloha reskin #4 | | titul #1 global XI, **titul #5 soft launch XII** | |

Roadmapa od února dál je orientační, upřesní se po CPI testech a datech z obnovy Hexu. Termíny titulů drží kapitola Jak vydat aspoň 5 titulů v 2027.

## Jak vydat aspoň 5 titulů v 2027

**Zadání (David):** "ideálně přijít na to, jak zvládnou minimálně 5 titulů". Tato kapitola je plán, jak to 16 lidí zvládne, a co musí platit, aby to vyšlo. Čísla kapacity jsou odhady, ne měření, a jsou označená *(předpoklad)*. Ověří se na reskinu #1 do konce března.

### Co je titul

**Titul = nový store listing (nové bundle ID), který je v roce 2027 venku u hráčů aspoň v soft launchi.** Global launch v 2027 je bonus, ne podmínka. Update existující hry, i velký, titul není.

| Kandidát | Počítá se? | Poznámka |
|---|---|---|
| Reskin #1, #2, #3 (MF-branch) | ano | jádro plánu, nejlevnější titul |
| Strategický titul #1 | ano | nový titul na sdílené metě |
| Titul #5: strategický titul #2 nebo koncept z GameJamu | ano | slot pro nejlepší prototyp z Q1, který neskončí jako titul #1 |
| Hexapolis 2 | ano, jen po gate | kapacitu na něj plán nemá; když gate projde, bere slot titulu #5, nebo jde nad plán jen s externí kapacitou |
| Reskin #4 nebo skin strategického titulu #1 | ano, záloha | náhrada titulu #5, když nestihne |
| Obnova Hexu (PvP, City V2, UGC) | ne | update existující hry |
| Rise of a Nation (B2B, `Hexapolis_India/`) | ne, pokud vedení nerozhodne jinak | hra pro klienta. **K rozhodnutí:** jestli se počítá. Když se podepíše, bere kapacitu stejných lidí a plán se musí přepočítat |
| Red Command, eventy, playables | ne | live ops a B2B |

### Slate: 3 reskiny a 2 nové tituly

Dvě linky vedle sebe. **Linka A (reskiny)** jede jako továrna: jeden reskin ve výrobě, další v pre-produkci. **Linka B (nové tituly)** dělá strategický titul #1 a po jeho soft launchi titul #5. Lidé z 6. 11.: live hry vedou Milan a Čoud, nový vývoj nesou Mirek, Kubík a David V.

| Titul | Typ | Na čem stojí | Tým | Start výroby | Soft launch | Global | Riziko |
|---|---|---|---|---|---|---|---|
| **Reskin #1** | reskin | kód a meta MF-branch, téma z CPI testu A | kód Kubík (Milan konzultuje kód MF), design Karel, art David C. + outsourcing, art direction Peko, QA a publishing Martin V., UA Richard, kreativy Ondra a Ruda | I 2027 | III 2027 | V 2027 | střední: první běh linky, AI pipeline a outsourcing se teprve zabíhají |
| **Reskin #2** | reskin | dtto, téma z dalšího CPI testu (do III) | linka A | IV 2027 | VI 2027 | VIII 2027 | nízké |
| **Strategický titul #1** | nový na sdílené metě | MF meta, City V2, SGB; vítěz Q1 prototypů (Warcamp nebo koncept z GameJamu), téma z CPI testu B | kód Mirek (lead) + David V., Čoud technicky (engine, PvP), design Aldy + Karel, art Peko + outsourcing, QA Kubík + Martin V., UA Richard | IV 2027 (greenlight III) | IX 2027 | XI 2027 | vysoké: nový gameplay, PvP, rozhodnutí o enginu (CE13) |
| **Reskin #3** | reskin | dtto, téma z CPI (do VI) | linka A | VII 2027 | X 2027 | XII 2027 | nízké, léto a dovolené prodlužují výrobu na 3 měsíce |
| **Titul #5** (strategický #2 nebo z GameJamu) | nový na sdílené metě, menší rozsah | kód a nástroje strategického titulu #1, druhý nejlepší prototyp z Q1, téma z CPI (do VIII) | tým linky B po soft launchi titulu #1 (Mirek, David V., Aldy nebo Karel, art David C. + outsourcing) | IX 2027 | XII 2027 | 2028 | vysoké: nejkratší okno, první na řadě při skluzu (záloha reskin #4) |
| *Hexapolis 2* | *nový, hex gameplay na MF metě* | *obnova Hexu, MF meta, City V2* | *jen místo titulu #5, nebo s externí kapacitou* | *nejdřív V 2027 (gate III)* | *nejdřív XII 2027* | *2028* | *vysoké: velký rozsah, gate, kapacita* |

**Rozložení v čase:**

| Měsíc | Linka A: reskiny | Linka B: nové tituly |
|---|---|---|
| XII 2026 | pre-produkce reskinu #1 (téma z CPI do 15. 12.) | GameJam 14. až 18. 12.: koncepty a prototypy |
| I až II | reskin #1 výroba | Q1 prototypy: Warcamp + 2 až 3 koncepty z GameJamu, každý nejvýš 2 sprinty; CPI test B; CE13 |
| III | **reskin #1 soft launch**, reskin #2 pre-produkce | greenlight titulu #1, gate Hexapolis 2, výběr kandidáta na titul #5 |
| IV až V | reskin #2 výroba, reskin #1 global (V) | titul #1 výroba |
| VI | **reskin #2 soft launch**, reskin #3 pre-produkce | titul #1 výroba |
| VII až VIII | reskin #3 výroba, reskin #2 global (VIII) | titul #1 výroba, titul #5 pre-produkce a CPI |
| IX | reskin #3 výroba | **titul #1 soft launch**, titul #5 výroba |
| X | **reskin #3 soft launch** | titul #5 výroba |
| XI | pre-produkce reskinu #4 jako záloha | titul #1 global, titul #5 výroba |
| XII | reskin #3 global | **titul #5 soft launch** |

Soft launche se schválně nepřekrývají ve stejném měsíci, protože QA, publishing a UA mají na launch jednoho až dva lidi.

### Kapacita: lidé, měsíce a úzké místo

**Předpoklady:**
- *(předpoklad)* Jeden člověk dá za rok 10 efektivních člověkoměsíců (ČM) práce: dovolená, svátky, nemoci, GameJam a porady jsou odečtené.
- *(předpoklad)* Live hry (Mecha Fortress, Red Command, Sector Defense, Hexapolis a další) a sdílené moduly (City V2 V2 a V3, SGB) dostanou přednost. Na nové tituly jde jen podíl úvazku v tabulce níže.
- *(předpoklad)* Potřeba na titul je odhad podle typu, ne z historických dat. Skutečná čísla reskinu #1 ji do konce března nahradí.

**Potřeba na jeden titul v ČM** *(předpoklad)*:

| Typ titulu | Kód | Design | DEV art | MKT art (store, kreativy) | QA a publishing | UA a CPI |
|---|---|---|---|---|---|---|
| Reskin, klasicky | 3 | 1,5 | 6 | 1,5 | 1,5 | 1,5 |
| Reskin, s pákami | 1,5 | 0,5 | 3,5 | 1,5 | 1 | 1,5 |
| Nový na sdílené metě (titul #1), klasicky | 9 | 4 | 8 | 2 | 2 | 2 |
| Nový na sdílené metě, s pákami | 6 | 3 | 5 | 1,5 | 1,5 | 2 |
| Titul #5 (na základu titulu #1), klasicky | 5 | 2,5 | 6 | 1,5 | 1,5 | 1,5 |
| Titul #5, s pákami | 3,5 | 2 | 3,5 | 1,5 | 1 | 1,5 |
| Q1 prototypy (3 až 4 koncepty × 2 sprinty), klasicky / s pákami | 3 / 2 | 1,5 / 1,5 | 1,5 / 1 | 0 | 0 | 0,5 / 0,5 |

**K dispozici proti potřebě za rok 2027 (3 reskiny + titul #1 + titul #5 + Q1 prototypy):**

| Role | Kdo a jaký podíl na nových titulech *(předpoklad)* | K dispozici | Potřeba klasicky | Potřeba s pákami | Rozdíl s pákami | Jak dorovnat |
|---|---|---|---|---|---|---|
| Kód | Mirek 0,5, Kubík 0,4, David V. 0,2, Čoud 0,2, Milan 0,1 | 14 | 26 (1,9×) | 16 | −2 | od IV, po stabilizaci obnovy Hexu, Milan a Čoud +0,1 každý; jinak menší rozsah titulu #5 |
| Design | Aldy 0,3, Karel 0,4, David V. 0,1 | 8 | 12,5 (1,6×) | 8 | 0 | design dokumenty a balanc s agenty (simulace bitev jako u Warcampu) |
| DEV art | Peko 0,4, David C. 0,6 | 10 | 33,5 (3,4×) | 20 | **−10** | outsourcing zhruba 1 úvazek na celý rok; Peko jako art director, ne výroba |
| MKT art | Ondra 0,4, Ruda 0,3 | 7 | 8 | 7,5 | −0,5 | šablony kreativ a AI video (Higgsfield) |
| QA a publishing | Martin V. 0,4, Kubík 0,2 | 6 | 8 | 5,5 | +0,5 | sdílený checklist publishingu a smoke testy pro linku A |
| UA a CPI | Richard 0,4, Kuba B. 0,3 | 7 | 8,5 | 8,5 | −1,5 | soft launche nepřekrývat, kampaně ze šablony; Richard od VI 0,5 |

**Závěr:** klasickým způsobem 16 lidí 5 titulů neudělá. Grafika chybí víc než trojnásobně, kód zhruba dvojnásobně, a to je důvod, proč dosavadní roadmapa vycházela na 3 až 4 tituly. **S pákami níže je kód, design, QA a UA zhruba v rovnováze a zbývá díra v grafice kolem 10 ČM, kterou kryje outsourcing.** Hexapolis 2 se do této kapacity nevejde: buď vezme slot titulu #5, nebo potřebuje externí tým.

**Páky, které z 3 až 4 titulů dělají 5:**

1. **Reskinová linka.** Jedna kódová základna MF-branch, téma je jen sada assetů a konfigurace, gameplay se nemění. Stejný checklist, stejný regresní test, stejný publishing. Kód na reskin z 3 na 1,5 ČM *(předpoklad)*.
2. **Sdílené moduly.** MF meta, City V2 a SGB se nepíšou znovu. Nové tituly je přebírají, titul #5 navíc přebírá kód a nástroje titulu #1.
3. **AI pipeline pro grafiku.** Higgsfield na koncepty, 2D assety a 3D modely, grafik dělá art direction a čištění. Úspora DEV artu zhruba 40 % *(předpoklad)*. Trénink na AI workshopu v GameJamu 14. 12.
4. **AI pipeline pro kód.** Claude Code a agentní workflow (zkušenost z Warcampu a NoxEngine). Úspora kódu zhruba 30 % *(předpoklad)*. NoxEngine zůstává experiment, plán stojí na Unity, dokud CE13 neřekne jinak.
5. **Outsourcing grafiky.** Externí výroba jednotek, budov a store assetů podle art direction Peka, zhruba 1 úvazek na rok *(předpoklad)*. Rozpočet není součástí tohoto dokumentu, schvaluje Jirka.
6. **Rozložená výroba.** V každé lince jeden titul ve výrobě a další v pre-produkci. Grafika a UA nikdy nedělají dva launche naráz.
7. **Pravidlo 2 sprintů.** Každý prototyp má nejvýš 2 sprinty, pak go nebo stop. Q1 prototypy dají titul #1 i kandidáta na titul #5 najednou.
8. **CPI před výrobou.** Žádný titul nejde do výroby bez CPI testu tématu (pipeline Kuby B., 1 až 2 testy měsíčně). Výroba se tak neplýtvá na téma, které neprodá.

### Co musí platit a do kdy

| Do kdy | Co | Kdo |
|---|---|---|
| 1. 12. 2026 | exekutiva schválí cíl "aspoň 5 titulů v soft launchi" a definici titulu, rozhodne, jestli se počítá Rise of a Nation | Jirka, David V. |
| 15. 12. 2026 | téma reskinu #1 z CPI testu A | Kuba B., Richard |
| 15. 1. 2027 | vlastník reskinové linky určený; kód MF-branch připravený jako šablona pro výměnu tématu | David V., Milan |
| 31. 1. 2027 | partner pro outsourcing grafiky vybraný a rozpočet schválený; AI art pipeline nasazená na reskinu #1 | Jirka, Peko |
| konec I 2027 | verdikt CPI testu B (téma pro strategickou větev a Hexapolis 2) | Kuba B. |
| konec II 2027 | Q1 prototypy rozhodnuté podle pravidla 2 sprintů; CE13 go / no-go pro NoxEngine | David V., Čoud |
| konec III 2027 | greenlight titulu #1, kandidát na titul #5, gate Hexapolis 2 a rozhodnutí, čí slot bere; **kontrolní bod kapacity:** skutečné ČM reskinu #1 proti předpokladu | vedení, David V. |
| III, VI, VIII 2027 | CPI testy témat pro reskin #2, reskin #3 a titul #5 | Kuba B. |

**Kontrolní bod konec března:** když reskin #1 spotřebuje o víc než 50 % ČM víc, než předpokládá tabulka, titul #5 se hned mění na reskin #4 nebo skin titulu #1 a outsourcing se navyšuje.

### Co vypadne první při skluzu

Pořadí, od prvního škrtu:

1. **Hexapolis 2** se posune do 2028 (už teď je nad plán).
2. **City V2 V2 a V3 v nových titulech** (jednotky, globální mapa, útoky) se přesune do pozdějšího updatu. Tituly vyjdou s MF metou a City V2 V1.
3. **NoxEngine** nad rámec experimentu: žádná další kapacita.
4. **Titul #5 jako unikátní hra** se nahradí reskinem #4 nebo skinem titulu #1. Počet 5 zůstane, cíl strategické větve "2 unikátní tituly" se nesplní.
5. **Global launch** pozdějších titulů (reskin #3, titul #1) se posune do 2028, soft launch zůstává v 2027.

**Neškrtá se nikdy:** live ops hlavních her (nesou revenue), CPI test před výrobou, pravidlo 2 sprintů.

### KPI plánu 5 titulů

| KPI | Cíl | Kdy se měří | Vlastník |
|---|---|---|---|
| Soft launche kumulativně proti plánu | III: 1, VI: 2, IX: 3, X: 4, XII: 5 | měsíčně na poradě vedení | David V. |
| Doba reskinu od startu výroby po soft launch | do 10 týdnů *(předpoklad)* | po každém reskinu | vlastník reskinové linky |
| ČM na reskin (interní + externí) | DEV art do 3,5 ČM, kód do 1,5 ČM *(předpoklad)* | po reskinu #1 (konec III), pak po každém | David V., Peko |
| Disciplína procesu | 100 % prototypů rozhodnutých po 2 sprintech, 100 % titulů s CPI testem před výrobou | při každém greenlightu | David V., Kuba B. |
| Soft launch proti benchmarku MF (CPI, D1, D7) | rozhodnutí o global launchi do 6 týdnů od soft launche *(předpoklad)* | u každého titulu | Richard, Martin V. |

## Slabá místa a otevřené otázky

| Námitka | Proč může platit | Odpověď nebo co s tím |
|---|---|---|
| 16 lidí neutáhne paralelní větve | Od dubna 2027 běží souběžně dva reskiny, strategický titul #1, příprava titulu #5, City V2 V2 a V3, CPI 1 až 2 testy měsíčně, live ops stávajících her a případně Hexapolis 2. Kód má na konci roku volněji, grafika je vytížená, a reskiny i nové tituly jsou hlavně grafická práce. | Kapacita po rolích, rozložená výroba ve dvou linkách a pořadí škrtů jsou v kapitole Jak vydat aspoň 5 titulů v 2027. Zbývá riziko: čísla jsou odhady *(předpoklad)* a úzkým místem zůstává grafika (zhruba 10 ČM navíc přes outsourcing). Kontrolní bod je konec března na skutečných číslech reskinu #1. |
| "Aspoň 5 nových titulů v 2027" je na hraně kapacity | Původní roadmapa realisticky dávala 3 až 4 tituly: strategický titul #2 byl jen prototyp, Hexapolis 2 závisí na gate. | Vyřešeno v kapitole Jak vydat aspoň 5 titulů v 2027: titul = soft launch v 2027, slate 3 reskiny + titul #1 + titul #5, Hexapolis 2 jen místo titulu #5 nebo nad plán, záloha reskin #4. **Co zůstává rizikové:** titul #5 má nejkratší okno (výroba IX až XI), úspory z AI (40 % art, 30 % kód) jsou neověřené, outsourcing grafiky ještě nemá partnera ani rozpočet a Rise of a Nation by při podpisu bral stejné lidi. Cíl pořád chce doplnit o revenue, které mají nové tituly nahradit. |
| Monetizační teze PvP nemá vlastní data | Celé portfolio je PvE. Útrata "bez stropu" je model RoK a CoC s obří základnou a klanovými válkami. Náš první test běží v Hexu s cca $15k měsíčně, který je navíc v Google Play Passu, kde předplatitelé gemy nekupují. | Gate musí měřit útratu zvlášť pro iOS, Android mimo Play Pass a Play Pass (`BALANC_HEX_PVP.md`, kap. 10). Výsledek z malé hry brát jako signál směru, ne jako potvrzení modelu RoK. |
| Obrana "lidé ve hře" v 2027 ještě neexistuje | Na launchi je PvP fake (boti a ghosti), City V2 V1 nemá sociální vrstvu, klany, globální mapa a útoky přijdou až ve V3 od Q2 2027. Síťový efekt potřebuje velkou živou základnu, kterou žádný titul zatím nemá. | Otevřeně říct, že 2027 staví infrastrukturu (SGB, Nox ID, klany). Jako předstihový ukazatel sledovat počet hráčů s Nox ID ve více titulech a podíl reálných PvP zápasů. |
| SGB je jediný bod selhání | Na SGB stojí PvP Hexu (fronta, ELO, součtové žebříčky, propadání tahů; chybějící kusy v `BALANC_HEX_PVP.md`, kap. 12), perzistence a odměny City V2 i release v MF do 11. 12. Integrace SGB klienta do Hexapolisu není v plánu nikde rozepsaná. | Určit vlastníka SGB, práci z kap. 12 BALANC dát do sprintu s termínem a mít záložní rozsah (lednový release PvP bez součtového žebříčku nebo s menším počtem front). |
| Gate Hexapolis 2 není měřitelný | City má cíl "TBD", platby "růst", UGC "sledovat". Lednová reaktivační kampaň, store update a sezónnost rozmažou srovnání před a po. UGC jde k hráčům v únoru, do prvního čtení na konci února má jen pár týdnů dat. | Holdout skupina přes RC procenta (část hráčů bez featur) místo srovnání před a po. Čísla a kill kritérium schválit na NOVE-19 ještě před lednem. |
| Staging City V2 v MF ohrožuje hlavní hru | MF nese cca 39 % revenue portfolia. Dnešní mapa MF (`MapBuilding`) prodává upgrady za `HardCurrency`, City V2 je platí surovinami a gemy bere jen za zrychlení a stavitele. Souběh může kanibalizovat dnešní gem sink. | Staging City V2 držet v MF jen interně nebo za RC flagem s revenue guardrailem v A/B. Rozhodnout otázku 3 v `BALANC_CITY_V2.md` (nahradit, nebo rozšířit dnešní mapu). |
| Strategická větev stojí na neověřeném enginu | Warcamp běží na NoxEngine 0.2 s mock SDK. Když CE13 skončí no-go, prototyp se přepisuje a greenlight II až III se posune. | Rozhodnutí CE13 dát před greenlight titulu #1 a hodnotit koncept nezávisle na enginu. |

**Potřebuje odpověď:**
- Schválit plán 5 titulů: definici titulu (soft launch v 2027), pořadí škrtů a rozpočet na outsourcing grafiky (kapitola Jak vydat aspoň 5 titulů v 2027).
- Počítá se Rise of a Nation (B2B) do 5 titulů, a když se podepíše, odkud vezme kapacitu?
- Kolik měsíčního revenue mají nové tituly nahradit?
- Jaký podíl revenue Hexapolisu jde přes Play Pass a jak se k předplatitelům Play Passu bude chovat monetizace City V2 a All-out-power?
- Smí City V2 do produkčního buildu MF už v prosinci a lednu, nebo jen interní staging, dokud se neověří v Hexu?
- Kdo vlastní SGB a jaký je plán B pro lednový release PvP v Hexu, když SGB v MF sklouzne za 11. 12.?
- Kill kritérium: při jakých číslech obnovu Hexu i Hexapolis 2 zastavíme?

## Otevřené otázky (neblokují start)

1. **Vlastníci:** kdo vede City V2, PvP v Hexu, strategickou větev a CPI program? Voice note jména neuvádí.
2. **Reskiny:** plán 5 titulů počítá se 3 (soft launch III, VI, X). V NoxHubu jsou zatím 2 (NOVE-11, NOVE-12), třetí založit. Kdo vlastní reskinovou linku (do 15. 1.)?
3. **Kapacita:** do 11. 12. rozhodnuto 6. 11.: live hry vedou Milan a Čoud, SGB, PvP, City V2 a UGC si dělí Mirek, Kubík a David. Kapacita na 2027 je v kapitole Jak vydat aspoň 5 titulů v 2027.
4. **Gate pro Hex 2:** jaká čísla (podíl hráčů v PvP, D30, ARPDAU, konverze na subscription) stačí na schválení?
5. **Rise of a Nation** (`Hexapolis_India/`): sdílí kód nebo City V2 s Hexapolisem?

## Výstupy

- [x] Surový přepis: `voice/Strategie.txt`
- [x] Strategický dokument (tento)
- [x] Design dokumenty City V2 (v2), PvP v Hexu (v2), koncept strategické větve, koncept obnovy Hexu, CPI pipeline, shrnutí NoxEngine
- [x] Tasky v NoxHubu: NOVE-13 až NOVE-38, CPI-13 až CPI-26 (subtasky pod NOVE-1, 5, 7, 9, 10, 11, 12 a CPI-11, 12, 13)
- [x] Wiki: Strategie / Produkční strategie 2027 (5 stránek)
- [x] Prezentace pro vedení: `strategie-2027-prezentace.html` (draft, 22 slidů)
- [x] Plán 5 titulů: kapitola Jak vydat aspoň 5 titulů v 2027 (6. 11.)
- [ ] Porada vedení: rozhodnout vlastníky, schválit plán 5 titulů a outsourcing grafiky, čísla pro gate Hex 2 (NOVE-19)

## Wiki stránky
- [Produkční strategie 2027 (přehled)](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=e6497b8c-3f2c-406c-a8d2-8a023e66e3bd)
- [City V2 meta: design dokument](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=40baabfd-d09b-4007-8a25-3a58f49ee1b7)
- [Obnova Hexapolisu: koncept](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=4a9efa9b-9fa0-491a-8293-ddf409a3c176)
- [PvP v Hexapolisu: design dokument](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=1289bcaf-4811-484e-a5cb-d59c9d870d20)
- [Strategická větev: koncept](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=19838dbd-8e92-401b-b4d2-28b79b4f7b11)
