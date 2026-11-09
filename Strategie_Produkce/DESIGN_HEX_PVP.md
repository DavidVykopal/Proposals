# Design dokument: PvP v Hexapolisu

> **Stav:** návrh v2, 4. 11. 2026. Přepracováno podle Davidova zadání z 4. 11. večer: dva segmenty (Skill only a All-out-power), Quick game se sub-režimy Speed a Normal, žebříčky denní, týdenní a měsíční, achievementy, skóre a ELO, 5 lig. Verze v1 (1. 11.) navrhovala async 1v1 jako MVP; to je nahrazené. Věci označené *(návrh)* jsou návrh autora dokumentu, ne Davidovo rozhodnutí.
> **Doplněno 5. 11. 2026:** PvP, City V2 i UGC implementované do 11. 12. 2026 za RC flagy, hráči PvP a City V2 v lednu 2027, UGC v únoru 2027. Release freeze 14. až 18. 12. (GameJam). Čísla a RC parametry: `BALANC_HEX_PVP.md`.
> **Rozhodnuto 6. 11. 2026 (David):** Hexapolis má cca 7 tis. aktivních hráčů, Play Pass se do revenue nepočítá. Přijaté návrhy z BALANC: ELO podmínka postupu, sestup rostoucí s ligou, jedna fronta pro Speed a Normal do PvP DAU cca 5 000 (při 7 tis. aktivních tedy jedna fronta na segment při launchi), generované profily botů. PvP, City V2 i UGC v testu a připravené do 11. 12.; PvP a City V2 k hráčům v lednu, UGC (bonus, z velké části hotové) může k hráčům dřív než v únoru. Žebříčky stojí na SGB, které jde živě až po svátcích (kap. 11). Hex featury a SGB dělí Mirek, Kubík (Jakub H.) a David, Milan a Čoud drží hlavní live hry.
> **Patří k:** `KONCEPT_OBNOVA_HEXU.md` (obnova původního Hexapolisu přes PvP a City V2), `STRATEGIE_PRODUKCE.md` větev 2. Sesterský dokument: `DESIGN_CITY_V2.md`.
> **Pro AI agenty:** zdroj pravdy je tento soubor. Číselné hodnoty (časy tahů, počty tahů, skóre, prahy lig) jsou výchozí návrhy a ladí se přes remote config. Tasky žijí v NoxHubu, projekt *Nové projekty* (NOVE-7 "Hexapolis 1, but with PvP") a *Hex 2* (HEX-2-0249-72 "Multiplayer").

## 1. Shrnutí

- PvP **testujeme jednoduše, přímo v původním Hexapolisu**. Žádná nová hra, žádné čekání na Hexapolis 2.
- Dva oddělené segmenty: **Skill only** (všichni stejný setup, rozhoduje jen to, jak kdo hraje, nejblíž Polytopii) a **All-out-power** (rozhoduje i síla jednotek a talentů z mety).
- Na začátku v obou segmentech jen **Quick game**: oba hráči jsou ve hře a čekají na své tahy. Sub-režimy **Speed** (méně času na tah a méně tahů) a **Normal**. Později **Long game** ve stylu online šachů.
- **Žebříčky denní, týdenní a měsíční** v obou segmentech, postavené na SharedGameBackendu. Odměny podle pořadí, **achievementy** za top 10, top 3, 2. místo a výhru, **série** za opakované umístění.
- Každý zápas dává **skóre** (výhra, prohra a celkový výkon), které se počítá do aktuálního denního, týdenního a měsíčního žebříčku. Vedle toho má každý hráč **ELO**.
- All-out-power má **5 lig** (nováčci, mid game, late game). Hráč se umisťuje jen ve své lize, **do další ligy postupuje top 10 % ligy** s ELO aspoň na mediánu ligy (Rozhodnuto 6. 11.).
- **Monetizace (návrh 9. 11.):** **PvP předplatné** 4,99 USD měsíčně (ranked bez limitu, všechny ligy, turnaje, Normal ranked, bonus surovin do City), Premium 9,99 USD, a **skiny jednotek** 120 až 600 gemů. Free tier zůstává (3 ranked zápasy denně), jinak by párování zůstalo bez soupeřů. Odhad 0,75 až 3,3 tis. USD měsíčně v Hexu, základ 1,8 tis. (`BALANC_HEX_PVP.md` kap. 10).
- Base je **cca 7 tis. aktivních hráčů**: Speed a Normal sdílí jednu frontu a ligy se v párování slučují, takže při launchi běží **2 fronty (jedna na segment)**. Při 25 % DAU v PvP to dává cca 68 až 80 % zápasů s reálným soupeřem (`BALANC_HEX_PVP.md`, kap. 6).

## 2. Proč PvP

- **Hráči chtějí hrát proti sobě.** Je to nejčastější přání komunity Hexapolisu a hlavní věc, kterou nás dnes přetahuje Polytopia. Ten náskok jde smazat rychle.
- **Cíl:** nejlepší civilization-like hra na mobilu. Hex zůstává civilizace: tahy, mapa, expanze, rozhodnutí. Nezidlovat ho.
- **Dva typy hráčů, dvě motivace.** Skill only obslouží hráče, kteří chtějí férový souboj jako v Polytopii. All-out-power obslouží hráče, kteří investovali do jednotek a talentů a chtějí tu sílu použít, a otevírá monetizaci, kterou dnes nemáme.
- PvP je spolu s City V2 a UGC jádro obnovy Hexu (`KONCEPT_OBNOVA_HEXU.md`). HexFort se ruší; nový Hexapolis 2 (hex gameplay na MF metě) vznikne až po ověření celku.

### Co už existuje

| Co | Kde | Stav |
|---|---|---|
| Funkční prototyp Hexapolis PvP (postavený agentem, Codex 5.5) | Davidova poznámka, porada 11. 5. 2026 | prototyp, neověřený na hráčích |
| Task "Multiplayer" | Hex 2, HEX-2-0249-72 | Open, termín 21. 8. prošel; HexFort se ruší, task patří k PvP v Hexu |
| OKR O5.2: test multiplayeru na původním Hexapolisu | Q4 OKR | termín 30. 11. 2026; podle plánu obnovy posunout (v testu a připravené do 11. 12. za RC flagem, hráči v lednu) |
| SGB: leaderboardy s anti-cheat limity (CODE-71), PvP admin UI (CODE-73) | wiki, SGB roadmap, Stage F | backlog; SGB do konce roku na interním buildu MF, živě po svátcích (6. 11.) |
| Custom mapy a nástroj, který přenese stav hry do editoru | Hexapolis, interní testování | existuje, základ pro replay |

## 3. Dva segmenty

| | **Skill only** | **All-out-power** |
|---|---|---|
| O čem to je | čistě o tom, kdo jak hraje | síla jednotek a talentů z mety + jak kdo hraje |
| Setup | všichni hrají **stejný setup**: stejné jednotky, staty a startovní podmínky | hráč bere svoje jednotky, levely, talenty a meta staty (včetně bonusů z City V2) |
| Volba hráče | jediná volba: **preset národa** (národ určuje sadu jednotek, které se v zápase objeví) | národ podle svých odemčených jednotek a talentů |
| Inspirace | nejblíž Polytopii | Clash Royale / Rise of Kingdoms: investice se projeví |
| Ligy | žádné, jeden žebříček pro všechny | **5 lig**, žebříček jen v rámci ligy (kap. 6) |
| Monetizace | nikdy výhoda za peníze, jen kosmetika a pohodlí | meta progrese má vliv, monetizace přes jednotky, talenty a City V2 |
| Párování | podle ELO segmentu | podle ligy, uvnitř ligy podle ELO segmentu |

- Segmenty mají **oddělené ELO, skóre i žebříčky**. Výsledek v jednom segmentu neovlivní druhý.
- **Presety národů pro Skill only** *(návrh)*: 3 až 4 národy na start, každý s pevnou sadou jednotek a stejnou celkovou silou. Balanc presetů přes remote config, sledovat win rate presetu (alarm nad 55 % *(návrh)*).
- **OP jednotky v All-out-power:** ligy oddělují hráče podle síly, takže vylevelovaný Warrior, Archer, Knight nebo Solmyr narazí na podobně silné soupeře. Bojové hodnoty PvP verze jednotek stejně držet v remote configu odděleně od PvE.

## 4. Herní módy

| Mód | Jak se hraje | Kdy |
|---|---|---|
| **Quick game: Speed** | oba hráči ve hře, **kratší limit na tah a méně tahů** | start (leden 2027) |
| **Quick game: Normal** | oba hráči ve hře, standardní limit na tah a počet tahů | start (leden 2027) |
| **Long game** | online šachy: tah kdykoli během delšího limitu, víc her souběžně | později, podle dat |
| Hra s přáteli | pozvánka přes NOX ID kód nebo odkaz, mimo žebříčky | s Quick game nebo hned po |

**Výchozí hodnoty** *(návrh, remote config)*:

| | Speed | Normal |
|---|---|---|
| Limit na tah | 30 s | 60 s |
| Max počet tahů | 15 | 30 |
| Délka zápasu | do 8 min | do 30 min |
| Mapa (1v1) | malá, 11x11 hexů | střední, 14x14 hexů |

**Pravidla PvP map:** symetrické nebo zrcadlené starty, mlha války zapnutá, vítězství dobytím hlavního města, jinak **body po limitu tahů** (města, území, jednotky).

**Postupný náběh (rozhodnutí 4. 11. 2026, best practices Voodoo).** Quick game potřebuje oba hráče naráz a Hex má cca 7 tis. aktivních hráčů, takže hrozí čekání. Proto:
- **Jedna fronta pro Speed a Normal** (Rozhodnuto 6. 11.): nejdřív se hledá soupeř ve stejném sub-režimu, po 10 s i v druhém. Rozdělení až od PvP DAU cca 5 000.
- **Onboarding:** prvních 3 až 5 zápasů *(návrh)* proti botovi s hráčským profilem, nastaveným tak, aby hráč pochopil pravidla.
- **Fallback:** když se do 20 s nenajde soupeř se stejným ELO a ligou, nastoupí AI soupeř s hráčským profilem nebo ghost zápas podle uložených tahů reálného hráče. Při launchi 30 s *(návrh, BALANC kap. 6)*. **Profily botů jsou generované** (Rozhodnuto 6. 11.), ne reálných neaktivních hráčů.
- **Hra s přáteli je vždy reálná.**
- Zápasy proti botům se počítají do skóre a odměn, ale **pozice v top 10 a achievementy jen z reálných zápasů** *(návrh)*, aby žebříček zůstal důvěryhodný.
- Telemetrie odlišuje soupeře (`pvp_match_completed` s `opponent_type`: `bot`, `ghost`, `human`).

## 5. Skóre a ELO

Dvě oddělená čísla s různým účelem:

| | **Skóre** | **ELO** |
|---|---|---|
| Účel | pořadí v denním, týdenním a měsíčním žebříčku | síla hráče, párování |
| Jak vzniká | z výsledku a celkového výkonu v zápase | klasický ELO výpočet z výhry a prohry proti síle soupeře |
| Reset | s koncem dne, týdne a měsíce | nikdy, jen soft reset při změně ligy *(návrh v BALANC kap. 3)* |
| Kde je vidět | v žebříčcích | v profilu hráče |

**Výpočet skóre za zápas** *(návrh)*:

| Složka | Body |
|---|---|
| Výhra | +100 |
| Prohra | +20 (odměna za odehrání) |
| Celkový výkon | +0 až 50 ve výhře, +0 až 25 v prohře: dobytá města, území, zničené jednotky, rychlost výhry |
| Síla soupeře | výhra nad soupeřem s vyšším ELO x1,2 až 1,5 |
| Vzdání nebo AFK | 0 |

Jedno skóre zápasu se připíše **zároveň do denního, týdenního i měsíčního žebříčku** segmentu (u All-out-power ligy).

Další násobiče (Normal x2, bot a ghost x0,5, série výher, denní strop zápasů) a strop skóre za zápas: `BALANC_HEX_PVP.md`, kap. 2.3.

## 6. Ligy v All-out-power

- **5 lig** *(názvy návrh)*: Bronz, Stříbro, Zlato, Diamant, Mistr. Oddělují **nováčky, mid game a late game** hráče.
- Nový hráč začíná v **Bronzu**, případně ho podle meta síly (PowerProgress) zařadíme výš *(návrh, aby vylevelovaný hráč nedrtil nováčky)*.
- Hráč se **umisťuje jen ve své lize**: žebříčky a odměny jsou per liga.
- **Postup: top 10 % ligy** v měsíčním žebříčku postupuje do vyšší ligy, vyhodnocení na konci měsíce. Podmínka (**Rozhodnuto 6. 11.**): ELO aspoň medián ligy a aspoň 15 reálných zápasů za měsíc. Bez ní by ligy řadily podle aktivity, ne podle síly (simulace v `BALANC_HEX_PVP.md`, kap. 1).
- **Sestup (Rozhodnuto 6. 11.):** roste s ligou, spodních 10 / 12 / 15 / 20 % aktivních hráčů ve Stříbru, Zlatu, Diamantu a Mistru; Bronz bez sestupu. Neaktivní hráči sestupují po 2 měsících bez zápasu. Mistr pak drží 2 až 3 % hráčů a horní polovina Mistra nesestupuje.
- **Launch *(návrh)*:** při cca 7 tis. aktivních bude mít Diamant kolem 100 a Mistr kolem 10 týdně aktivních hráčů, proto se jejich žebříčky a odměny při launchi zobrazí společně se Zlatem a oddělí se, až každá liga má 200+ týdně aktivních (`BALANC_HEX_PVP.md`, kap. 5). Párování jde přes všechny ligy s oknem síly.
- Skill only ligy nemá, všichni hrají na stejných podmínkách.

## 7. Žebříčky, odměny a achievementy

**Žebříčky:** v každém segmentu (a u All-out-power v každé lize) **denní, týdenní a měsíční**, řazené podle skóre. Postavené na **SharedGameBackendu** (leaderboards, Stage F4, anti-cheat limity CODE-71), identita přes NOX ID.

**Odměny podle pořadí** *(návrh)*, vyplácené na konci období do hry:

| Pořadí | Denní | Týdenní | Měsíční |
|---|---|---|---|
| Vítěz | truhla + měna | velká truhla + kosmetika | prémiová truhla + exkluzivní kosmetika + titul |
| 2. až 3. místo | truhla | velká truhla | prémiová truhla + titul |
| top 10 | menší truhla | truhla | velká truhla |
| top 10 % | suroviny do City V2 | truhla | truhla |
| všichni s aspoň 1 zápasem | malá odměna | suroviny | suroviny |

**Achievementy** za umístění (počítají se jen reálné zápasy):

| Achievement | Podmínka |
|---|---|
| Top 10 | umístění v top 10 denního, týdenního nebo měsíčního žebříčku |
| Top 3 | umístění v top 3 |
| Stříbro | 2. místo |
| Vítěz | 1. místo |
| **Série** | top 10 týdenního žebříčku **2 týdny po sobě**, pak 3, 4, 8 týdnů *(návrh)*; obdobně denní série 3, 7, 14 dní a měsíční 2, 3, 6 měsíců |

Achievementy mají stupně podle období (denní, týdenní, měsíční) a segmentu, ukazují se v profilu a ve městě (City V2) jako trofeje *(návrh)*.

## 8. Napojení na City V2

- PvP zápasy a odměny z žebříčků dávají **suroviny a materiál do města**. PvP je druhý zdroj pro stavbu města vedle kampaně.
- **Budovy v City V2 zvyšují meta staty**, které platí v **All-out-power**. Skill only je ignoruje. Tím vzniká smyčka: hraju PvP → stavím město → jsem silnější v All-out-power.
- Trofeje a tituly z achievementů se ukazují ve městě *(návrh)*.

## 9. Anti-cheat, odpojení, AFK

**Autorita serveru.** Klient posílá jen akce (pohyb, útok, stavba, výzkum), ne výsledný stav.

| Varianta | Jak | Doporučení |
|---|---|---|
| Validace klíčových pravidel | server kontroluje legálnost akcí (dosah, cena, akční body) | MVP pro leden |
| Deterministická simulace + přehrání tahů na serveru, server drží seed RNG | sdílená herní logika i na serveru | cíl po MVP |

- **Replay:** každý zápas uložený jako seed + seznam akcí (kontrola podezřelých výsledků, sdílení).
- **Podezřelé chování:** nemožné výsledky, extrémní série, statistiky mimo rozsah. Flag, ruční kontrola, ban přes SGB.
- **Quick game, odpojení:** 30 s na návrat *(návrh)*, pak tah propadá; 2 propadlé tahy po sobě nebo 3 celkem = prohra (`BALANC_HEX_PVP.md`, kap. 9).
- **Vzdání** kdykoli, počítá se jako prohra se skóre 0. Opakované opouštění zápasů = krátký zákaz rankovaných zápasů.

## 10. Monetizace *(návrh 9. 11., čísla v `BALANC_HEX_PVP.md` kap. 10)*

| Zdroj | Segment | Pozn. |
|---|---|---|
| **PvP předplatné** 4,99 USD / měsíc: ranked bez limitu, všechny ligy, měsíční turnaj, Normal ranked, statistiky, replay, bez reklam, skin měsíce, +25 % surovin do City | oba | směr Davida 9. 11.: PvP placené jako předplatné |
| **Premium** 9,99 USD / měsíc: navíc epický skin měsíce, rámeček, +50 % surovin | oba | |
| **Zdarma**: Quick game, 3 ranked zápasy denně, ligy Bronz a Stříbro | oba | neplatící jsou soupeři předplatitelů; celé PvP za paywallem by při 1 750 PvP DAU nechalo placenou frontu na 35 až 105 lidech denně |
| **Skiny jednotek** 120 / 300 / 600 gemů, sezónní limitované, skiny hlavního města, rámečky a emoty | oba | bez vlivu na staty; kompletní sbírka cca 510 USD, sběratel s Premium cca 1 tis. USD za rok |
| Jednotky, talenty, City V2 | All-out-power | hlavní hloubka je ve městě (`BALANC_CITY_V2.md` kap. 8.3) |
| PvP úkoly ve stávajícím battle passu | oba | zůstávají |
| Rewarded reklamy jen mimo zápas | oba | v zápase nikdy |

Odhad v Hexu: **0,75 / 1,8 / 3,3 tis. USD měsíčně** (nízký / základ / vysoký), rok 2027 v základu cca 20 tis. USD. PvP samo vydělá málo, hlavní efekt je retence a útrata v City a All-out-power.

Pravidlo: **ve Skill only se výhoda koupit nedá.**

## 11. Postup a technika

**Testovat jednoduše v původní hře.** PvP se staví přímo pro původní Hexapolis tak, aby šlo co nejdřív k hráčům. Backend (fronta, stav zápasu, ELO, skóre, žebříčky, odměny, replay) jde na **SharedGameBackend**, staging přes Mecha Fortress.

| Období | Co |
|---|---|
| listopad 2026 | design dotáhnout, presety národů, SGB služby (fronta, zápas, ELO, skóre, žebříčky), Quick game Speed a Normal interně hratelné |
| prosinec 2026 | do 11. 12.: PvP, City V2 i UGC v testu a připravené, validace tahů na serveru, žebříčky a odměny, achievementy, vše za RC flagem v Hexapolisu; 14. až 18. 12. release freeze; SGB do konce roku vyvinuté a otestované na interním buildu MF |
| leden 2027 | SGB živě po svátcích, vypnuté a postupně zapínané; k hráčům: Skill only a All-out-power v Quick game, postupné zapínání (RC procenta, do 2 týdnů na 90 %+ *(návrh)*), komunitní test, reaktivační kampaň |
| únor 2027 nebo dřív | UGC mapy k hráčům (bonus, z velké části hotové, může dřív než v únoru), hra s přáteli |
| později | Long game, ligový postup a sestup na datech |

RC flagy *(návrh)*: `hex_pvp_enabled`, `hex_pvp_skill_enabled`, `hex_pvp_power_enabled`, `hex_pvp_speed_enabled`.

**Závislost na SGB (6. 11.):** žebříčky, a podle této kapitoly i fronta, ELO a skóre, stojí na SharedGameBackendu. SGB jde živě až po svátcích, vypnuté a s postupným zapínáním, takže **lednový release PvP předpokládá, že SGB v lednu postupně naběhne**. Fallback *(návrh)*: PvP pustit nejdřív bez žebříčků a lig (Quick game, ELO, odměny za zápasy) a žebříčky zapnout RC flagem po náběhu SGB.

**Kapacita (6. 11.):** Hex featury, SGB a nové věci dělí Mirek, Kubík (Jakub H.) a David. Milan a Čoud drží hlavní live hry.

## 12. Metriky (vstup pro gate Hexapolis 2)

| Metrika | Co říká | Cíl *(návrh)* |
|---|---|---|
| Podíl DAU, který zkusí PvP | zájem | 25 %+ (cca 1 750 z 7 tis. aktivních) |
| Podíl zápasů s reálným soupeřem | likvidita | 50 %+ během lednového náběhu, 65 %+ v únoru *(návrh, sníženo 6. 11. z 60 % / 80 %)* |
| Poměr hráčů Skill only a All-out-power | kterou motivaci hráči mají | sledovat |
| Zápasů na PvP hráče týdně | opakované hraní | 5+ |
| D7 / D30 retence PvP hráčů vs. ostatní | přidaná hodnota | +20 % relativně |
| Návrat bývalých hráčů po kampani | síla značky + featury | sledovat |
| Útrata v All-out-power vs. ostatní | ochota platit za sílu | růst |
| ARPDAU Hexapolisu před a po | dopad na revenue (cca $15k / měsíc, **bez Play Passu**, Rozhodnuto 6. 11.; měřit iOS a Android mimo Play Pass) | růst |
| Win rate presetů a jednotek | balanc | pod 55 % |
| Čekání na soupeře, podíl bot zápasů | zdraví matchmakingu | klesá v čase |

## 13. UGC (třetí díl ověření, únor 2027 nebo dřív)

V testu a připravené do 11. 12. 2026 za RC flagem. UGC je bonus, ale z velké části hotové, takže **může k hráčům dřív než v únoru 2027** (Rozhodnuto 6. 11.). Je součást ověření celku: editor map postavený na interním nástroji, sdílení kódem, "mapa týdne", komunitní mapy jen do casual rotace, ne do žebříčků. Úložiště přes SGB (CODE-8).

## 14. Rizika

| Riziko | Zmírnění |
|---|---|
| Malá base (cca 7 tis. aktivních), Quick game potřebuje oba hráče naráz | jedna fronta na segment (Rozhodnuto 6. 11.), fallback 30 s při launchi, rychlý RC náběh, malý holdout, bot onboarding (kap. 4), hra s přáteli |
| Pay to win pocit | Skill only jako férová alternativa, ligy v All-out-power |
| Rozdrobení base mezi 2 segmenty, 2 sub-režimy a 5 lig | Speed a Normal v jedné frontě a ligy sloučené v párování (Rozhodnuto 6. 11.); žebříčky Diamant a Mistr při launchi se Zlatem *(návrh)* |
| SGB jde živě až po svátcích | lednový release žebříčků stojí na postupném náběhu SGB; fallback PvP bez žebříčků *(návrh)*, kap. 11 |
| Cheateři v žebříčcích | server validace, replay, top 10 a achievementy jen z reálných zápasů |
| Kapacita v Q4 (live ops) | Milan a Čoud drží live hry, Hex featury a SGB dělí Mirek, Kubík a David (6. 11.); backend a logika přes agenty |

## 15. Slabá místa a otevřené otázky

Rizika provedení jsou v kap. 14. Tady jsou námitky proti tomu, jestli je samotný návrh správně.

| Námitka | Proč může platit | Odpověď nebo co s tím |
|---|---|---|
| Návrh má víc front, než Hex unese | 2 segmenty × 2 sub-režimy × 5 lig = 12 front. Při cca 7 tis. aktivních a 25 % DAU v PvP (1 750 PvP DAU) dává 12 front jen 21 % reálných zápasů, 2 fronty 68 % (`BALANC_HEX_PVP.md`, kap. 6). Práh PvP DAU 5 000 pro rozdělení front je 70 % DAU, takže se v roce 2027 nejspíš nedosáhne. | **Rozhodnuto 6. 11.:** launch se 2 frontami (segmenty), Speed a Normal v jedné frontě, ligy sloučené v párování. Ligy slouží jako žebříčky a odměny. Hráči to otevřeně říct: Speed a Normal jsou volba preference, ne oddělené fronty. |
| Ligy a párování vyrovnávají sílu, takže útrata nekupuje výhry | All-out-power řadí hráče podle síly (ligy, zařazení podle PowerProgress, okno síly v párování). Platící hráč hraje proti stejně silným a win rate se mu srovná k 50 %. Teze "útrata bez stropu" ze strategie tak v tomto segmentu neplatí. | Říct otevřeně, co platící hráč kupuje: rychlejší postup do vyšší ligy, prestiž a ligové odměny (Mistr x2,5), ne výhry. Měřit, jestli to na útratu stačí (metrika "útrata v All-out-power" v kap. 12). |
| Kumulativní skóre odměňuje grind, ne dovednost | Simulace v BALANC: korelace ligy s dovedností 0,07, s aktivitou 0,79. Top 10 denních a týdenních žebříčků obsadí nejaktivnější hráči, ne nejlepší, což jde proti slibu férového souboje. | **Rozhodnuto 6. 11.:** ELO podmínka postupu a sestup rostoucí s ligou (korelace ligy s dovedností 0,34). Denní a týdenní top 10 zůstávají podle skóre; sledovat, jestli je neobsadí jen grindeři. |
| Fake PvP podkope důvěru právě té komunity, která PvP chce | Boti vystupují s hráčským profilem. Hráči Polytopie, kvůli kterým Skill only děláme, chtějí skutečné soupeře; odhalení na Discordu poškodí obnovu. Při 7 tis. aktivních bude bot zápasů v lednu 20 až 50 %. | **Rozhodnuto 6. 11.:** jen generované profily, ne reálné. Zbývá: po onboardingu bota ve Skill only přiznat (např. "trénink, než se najde soupeř")? |
| Suroviny z PvP jsou o řády menší, než město potřebuje | BALANC PvP (kap. 8) dává aktivnímu hráči 1 500 až 2 500 surovin měsíčně a chce krýt 30 až 40 % příjmu. `BALANC_CITY_V2.md` (kap. 7) čeká ze zápasů 17 000 až 210 000 surovin denně. Smyčka "PvP krmí město" tak v číslech nefunguje. | Přeškálovat suroviny v PvP odměnách podle tieru Radnice (vzorec z BALANC City kap. 7) a teprve pak ladit podíl PvP. |
| Skill only není izolovaný | Odměny ze Skill only dávají suroviny do City V2, které posílí hráče v All-out-power (BALANC otázka 7). Výhoda není koupená, ale segmenty se míchají. | Buď Skill only odměňovat jen kosmetikou a měnou mimo město, nebo míchání přijmout jako záměr a napsat to do designu. |
| Metrika "25 % DAU zkusí PvP" měří zvědavost | Onboarding proti botům, reaktivační kampaň a store update dostanou do PvP hodně hráčů na jeden zápas. O hodnotě featury to neříká nic. | Do gate dát podíl DAU s 5+ **reálnými** zápasy týdně a retenci PvP hráčů proti holdoutu bez PvP. Holdout max 10 % hráčů, větší sníží likviditu front (BALANC kap. 6). |
| Lednový release stojí na SGB | Žebříčky (a fronta a ELO) běží na SGB, které jde živě až po svátcích, vypnuté a postupně. Zpoždění SGB posune PvP. | Fallback *(návrh)*: PvP bez žebříčků a lig, žebříčky dozapnout RC flagem (kap. 11). |

**Potřebuje odpověď:**
- Pouštíme v lednu oba segmenty, nebo jen jeden (a který)?
- Přiznáme bota ve Skill only po onboardingu?
- Pokud SGB v lednu nenaběhne včas: PvP bez žebříčků, nebo posunout?
- Co přesně má platící hráč v All-out-power kupovat, když párování srovnává sílu?
- Smí Skill only dávat suroviny do City V2?

## 16. Otevřené otázky

1. **Presety národů ve Skill only:** kolik a jaké národy na start?
2. **ELO:** jedno ELO per segment, nebo i per sub-režim? Návrh v BALANC: jedno ELO per segment, sedí na jednu frontu pro Speed a Normal (Rozhodnuto 6. 11.).
3. **Ligy:** zařazovat nové hráče podle PowerProgress? (Postup a sestup na konci měsíce s ELO podmínkou: Rozhodnuto 6. 11.)
4. **Odměny:** konkrétní obsah truhel a kosmetiky podle ekonomiky Hexapolisu.
5. **Prototyp z května** (Codex 5.5): navazujeme na něj? Kde leží a kdo ho převezme?
6. **Vlastník** PvP featury: **rozhodnuto 6. 11., Mirek** (City V2 Kubík, UGC David). Zbývá vztah k HEX-2-0249-72 a OKR O5.2 (termín 30. 11., posunout podle plánu obnovy).
7. **Cílové hodnoty metrik** v kap. 12 potvrdit s Jirkou (likvidita a podíl DAU přepočítané na 7 tis. aktivních).
