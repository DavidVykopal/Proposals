# Design dokument: PvP v Hexapolisu

> **Stav:** návrh v2, 4. 11. 2026. Přepracováno podle Davidova zadání z 4. 11. večer: dva segmenty (Skill only a All-out-power), Quick game se sub-režimy Speed a Normal, žebříčky denní, týdenní a měsíční, achievementy, skóre a ELO, 5 lig. Verze v1 (1. 11.) navrhovala async 1v1 jako MVP; to je nahrazené. Věci označené *(návrh)* jsou návrh autora dokumentu, ne Davidovo rozhodnutí.
> **Patří k:** `KONCEPT_OBNOVA_HEXU.md` (obnova původního Hexapolisu přes PvP a City V2), `STRATEGIE_PRODUKCE.md` větev 2. Sesterský dokument: `DESIGN_CITY_V2.md`.
> **Pro AI agenty:** zdroj pravdy je tento soubor. Číselné hodnoty (časy tahů, počty tahů, skóre, prahy lig) jsou výchozí návrhy a ladí se přes remote config. Tasky žijí v NoxHubu, projekt *Nové projekty* (NOVE-7 "Hexapolis 1, but with PvP") a *Hex 2* (HEX-2-0249-72 "Multiplayer").

## 1. Shrnutí

- PvP **testujeme jednoduše, přímo v původním Hexapolisu**. Žádná nová hra, žádné čekání na Hexapolis 2.
- Dva oddělené segmenty: **Skill only** (všichni stejný setup, rozhoduje jen to, jak kdo hraje, nejblíž Polytopii) a **All-out-power** (rozhoduje i síla jednotek a talentů z mety).
- Na začátku v obou segmentech jen **Quick game**: oba hráči jsou ve hře a čekají na své tahy. Sub-režimy **Speed** (méně času na tah a méně tahů) a **Normal**. Později **Long game** ve stylu online šachů.
- **Žebříčky denní, týdenní a měsíční** v obou segmentech, postavené na SharedGameBackendu. Odměny podle pořadí, **achievementy** za top 10, top 3, 2. místo a výhru, **série** za opakované umístění.
- Každý zápas dává **skóre** (výhra, prohra a celkový výkon), které se počítá do aktuálního denního, týdenního a měsíčního žebříčku. Vedle toho má každý hráč **ELO**.
- All-out-power má **5 lig** (nováčci, mid game, late game). Hráč se umisťuje jen ve své lize, **do další ligy postupuje top 10 % ligy**.

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
| OKR O5.2: test multiplayeru na původním Hexapolisu | Q4 OKR | termín 30. 11. 2026 |
| SGB: leaderboardy s anti-cheat limity (CODE-71), PvP admin UI (CODE-73) | wiki, SGB roadmap, Stage F | backlog |
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

**Postupný náběh (rozhodnutí 4. 11. 2026, best practices Voodoo).** Quick game potřebuje oba hráče naráz, takže při malé base hrozí čekání. Proto:
- **Onboarding:** prvních 3 až 5 zápasů *(návrh)* proti botovi s hráčským profilem, nastaveným tak, aby hráč pochopil pravidla.
- **Fallback:** když se do 20 s *(návrh)* nenajde soupeř se stejným ELO a ligou, nastoupí AI soupeř s hráčským profilem nebo ghost zápas podle uložených tahů reálného hráče.
- **Hra s přáteli je vždy reálná.**
- Zápasy proti botům se počítají do skóre a odměn, ale **pozice v top 10 a achievementy jen z reálných zápasů** *(návrh)*, aby žebříček zůstal důvěryhodný.
- Telemetrie odlišuje soupeře (`pvp_match_completed` s `opponent_type`: `bot`, `ghost`, `human`).

## 5. Skóre a ELO

Dvě oddělená čísla s různým účelem:

| | **Skóre** | **ELO** |
|---|---|---|
| Účel | pořadí v denním, týdenním a měsíčním žebříčku | síla hráče, párování |
| Jak vzniká | z výsledku a celkového výkonu v zápase | klasický ELO výpočet z výhry a prohry proti síle soupeře |
| Reset | s koncem dne, týdne a měsíce | nikdy, jen soft reset při změně ligy *(otevřená otázka)* |
| Kde je vidět | v žebříčcích | v profilu hráče |

**Výpočet skóre za zápas** *(návrh)*:

| Složka | Body |
|---|---|
| Výhra | +100 |
| Prohra | +20 (odměna za odehrání) |
| Celkový výkon | +0 až 50: dobytá města, území, zničené jednotky, rychlost výhry |
| Síla soupeře | výhra nad soupeřem s vyšším ELO x1,2 až 1,5 |
| Vzdání nebo AFK | 0 |

Jedno skóre zápasu se připíše **zároveň do denního, týdenního i měsíčního žebříčku** segmentu (u All-out-power ligy).

## 6. Ligy v All-out-power

- **5 lig** *(názvy návrh)*: Bronz, Stříbro, Zlato, Diamant, Mistr. Oddělují **nováčky, mid game a late game** hráče.
- Nový hráč začíná v **Bronzu**, případně ho podle meta síly (PowerProgress) zařadíme výš *(návrh, aby vylevelovaný hráč nedrtil nováčky)*.
- Hráč se **umisťuje jen ve své lize**: žebříčky a odměny jsou per liga.
- **Postup: top 10 % ligy** v měsíčním žebříčku postupuje do vyšší ligy *(návrh: vyhodnocení na konci měsíce)*.
- **Sestup** *(návrh)*: spodních 10 % aktivních hráčů ligy sestupuje, neaktivní hráči sestupují po 2 měsících bez zápasu. Mistr bez sestupu pod top 50 %.
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
- **Quick game, odpojení:** 30 s na návrat *(návrh)*, pak tah propadá, dva propadlé tahy = prohra.
- **Vzdání** kdykoli, počítá se jako prohra se skóre 0. Opakované opouštění zápasů = krátký zákaz rankovaných zápasů.

## 10. Monetizace (hypotézy k ověření)

| Hypotéza | Segment | Pozn. |
|---|---|---|
| Jednotky, talenty, City V2 zrychlení | All-out-power | meta síla se v této lize projeví, ligy drží férovost mezi podobně silnými |
| PvP battle pass se sezónními úkoly | oba | Hexapolis už battle pass má |
| Subscription (víc statistik, replay, PvP kosmetika, bez reklam) | oba | David zmínil subscription jako ověřovací signál |
| Kosmetika (skiny jednotek, rámečky, tituly) | oba | bez vlivu na výsledek |
| Rewarded reklamy jen mimo zápas | oba | v zápase nikdy |

Pravidlo: **ve Skill only se výhoda koupit nedá.**

## 11. Postup a technika

**Testovat jednoduše v původní hře.** PvP se staví přímo pro původní Hexapolis tak, aby šlo co nejdřív k hráčům. Backend (fronta, stav zápasu, ELO, skóre, žebříčky, odměny, replay) jde na **SharedGameBackend**, staging přes Mecha Fortress.

| Období | Co |
|---|---|
| listopad 2026 | design dotáhnout, presety národů, SGB služby (fronta, zápas, ELO, skóre, žebříčky), Quick game Speed a Normal interně hratelné |
| prosinec 2026 | interní testy, validace tahů na serveru, žebříčky a odměny, achievementy, za RC flagem v Hexapolisu |
| leden 2027 | k hráčům: Skill only a All-out-power v Quick game, postupné zapínání (RC procenta), komunitní test, reaktivační kampaň |
| únor 2027 | UGC mapy (třetí díl ověření), hra s přáteli |
| později | Long game, ligový postup a sestup na datech |

RC flagy *(návrh)*: `hex_pvp_enabled`, `hex_pvp_skill_enabled`, `hex_pvp_power_enabled`, `hex_pvp_speed_enabled`.

## 12. Metriky (vstup pro gate Hexapolis 2)

| Metrika | Co říká | Cíl *(návrh)* |
|---|---|---|
| Podíl DAU, který zkusí PvP | zájem | 25 %+ |
| Poměr hráčů Skill only a All-out-power | kterou motivaci hráči mají | sledovat |
| Zápasů na PvP hráče týdně | opakované hraní | 5+ |
| D7 / D30 retence PvP hráčů vs. ostatní | přidaná hodnota | +20 % relativně |
| Návrat bývalých hráčů po kampani | síla značky + featury | sledovat |
| Útrata v All-out-power vs. ostatní | ochota platit za sílu | růst |
| ARPDAU Hexapolisu před a po | dopad na revenue (dnes cca $15k / měsíc) | růst |
| Win rate presetů a jednotek | balanc | pod 55 % |
| Čekání na soupeře, podíl bot zápasů | zdraví matchmakingu | klesá v čase |

## 13. UGC (třetí díl ověření, únor 2027)

Hned po PvP a City V2, součást ověření celku: editor map postavený na interním nástroji, sdílení kódem, "mapa týdne", komunitní mapy jen do casual rotace, ne do žebříčků. Úložiště přes SGB (CODE-8).

## 14. Rizika

| Riziko | Zmírnění |
|---|---|
| Malá base, Quick game potřebuje oba hráče naráz | bot fallback a onboarding (kap. 4), dva sub-režimy místo mnoha módů, hra s přáteli |
| Pay to win pocit | Skill only jako férová alternativa, ligy v All-out-power |
| Rozdrobení base mezi 2 segmenty, 2 sub-režimy a 5 lig | v launchi párovat napříč sub-režimy, pokud fronta čeká *(návrh)*; ligy sloučit, dokud nemají dost hráčů |
| Cheateři v žebříčcích | server validace, replay, top 10 a achievementy jen z reálných zápasů |
| Kapacita v Q4 (live ops) | backend a logika přes agenty, lidský čas dávkovat |

## 15. Otevřené otázky

1. **Presety národů ve Skill only:** kolik a jaké národy na start?
2. **ELO:** jedno ELO per segment, nebo i per sub-režim (Speed a Normal zvlášť)?
3. **Ligy:** vyhodnocení postupu na konci měsíce, nebo průběžně? Zařazovat nové hráče podle PowerProgress?
4. **Odměny:** konkrétní obsah truhel a kosmetiky podle ekonomiky Hexapolisu.
5. **Prototyp z května** (Codex 5.5): navazujeme na něj? Kde leží a kdo ho převezme?
6. **Vlastník** PvP featury a vztah k HEX-2-0249-72 a OKR O5.2 (termín 30. 11.).
7. **Cílové hodnoty metrik** v kap. 12 potvrdit s Jirkou.
