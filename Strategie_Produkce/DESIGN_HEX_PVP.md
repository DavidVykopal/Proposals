# Design dokument: PvP v Hexapolisu (+ UGC)

> **Stav:** návrh v1, 1. 11. 2026. Vychází z Davidova voice note ke strategii (`voice/Strategie.txt`) a z existujících podkladů v hubu. Věci označené *(návrh)* jsou můj návrh, ne rozhodnutí.
> **Patří k:** `STRATEGIE_PRODUKCE.md`, větev 2 (Hexapolis). Sesterský dokument: design City V2 (město / mapa V2).
> **Pro AI agenty:** zdroj pravdy je tento soubor. Číselné hodnoty (časy tahů, ELO, limity) jsou výchozí návrhy, ladí se přes remote config. Tasky žijí v NoxHubu, projekt *Nové projekty* (NOVE-7 "Hexapolis 1, but with PvP", NOVE-9 UGC) a *Hex 2* (HEX-2-0249-72 "Multiplayer").

## 1. Proč PvP

- **Hráči chtějí hrát proti sobě.** Je to nejčastější přání komunity Hexapolisu a hlavní věc, kterou nás dnes přetahuje Polytopia. Tenhle náskok jde smazat rychle.
- **Cíl:** nabídnout nejlepší civilization-like hru na mobilu. Hex zůstává civilizace: tahy, mapa, expanze, rozhodnutí. **Nezidlovat ho, nedělat z něj pasivní hru.** Idle varianty patří do nové strategické větve, ne do Hexu.
- PvP je jedna ze tří featur, které ověřujeme na současném Hexapolisu (PvP, City V2, UGC). Teprve když ověření projde, schvaluje se Hexapolis 2 (Hexafort).

### Co už existuje

| Co | Kde | Stav |
|---|---|---|
| Funkční prototyp Hexapolis PvP (postavený agentem, Codex 5.5) | Davidova poznámka, porada 11. 5. 2026 | prototyp, neověřený na hráčích |
| Task "Multiplayer" | Hex 2, HEX-2-0249-72 | Open, termín 21. 8. prošel |
| OKR O5.2: test multiplayeru na původním Hexapolisu | Q4 OKR | termín 30. 11. 2026 |
| Hexafort GDD (Hexapolis 2): PvP v základní podobě je součást proof of conceptu | wiki, "Hexafort (Hexapolis 2)" | návrh, rozhodovací bod TBD |
| SGB: PvP podporuje, admin UI je CODE-73; leaderboardy na SGB s anti-cheat limity CODE-71 | wiki, SGB roadmap, Stage F | backlog |
| Custom mapy a bug report nástroj, který přenese stav hry do editoru | Hexapolis, interní testování | existuje, základ pro replay i UGC |

Rizika zapsaná na poradě 24. 9.: **PvP, cheateři, OP jednotky, PowerProgress.** Tento dokument je řeší v kapitolách 4 a 5.

## 2. Herní módy

Princip: začít jedním módem, který jde postavit rychle a funguje na mobilu i s malou hráčskou základnou. Rozšiřovat až podle dat.

| Mód | Popis | Pro | Proti | Kdy |
|---|---|---|---|---|
| **A. Async 1v1** *(doporučeno jako první)* | Tahová hra, každý hraje svůj tah, kdy chce. Limit na tah (výchozí 24 h, rychlá varianta 1 h). Víc her souběžně. | Funguje s malou base, žádné čekání ve frontě, přirozené pro tahovou hru, nízké nároky na síť | Hra trvá dny, horší pocit "souboje" | MVP, leden 2027 |
| **B. Live 1v1 (blitz)** | Oba online, limit 30 až 60 s na tah, malá mapa, zápas do 15 min | Silný zážitek, krátké, dobré pro žebříček | Potřebuje matchmaking s dost hráči, odpojení | po ověření A |
| **C. FFA 3 až 4 hráči (async)** | Klasická civ partie víc hráčů | Nejvíc "Civilization" | Dlouhé, kingmaking, odpadávání hráčů | později |
| **D. Hra s přáteli** | Pozvánka přes NOX ID kód / odkaz, vlastní nastavení mapy | Virální, bez nároku na matchmaking | Závisí na friends API (SGB F2/F3) | s A nebo hned po |

**Pravidla pro PvP mapy:** malé mapy (1v1 cca 11x11 až 14x14 hexů *(návrh)*), symetrické nebo zrcadlené starty, omezený počet tahů (výchozí 30 *(návrh)*), vítězství dobytím hlavního města nebo body po limitu tahů. Mlha války zapnutá.

**Fallback na boty:** když není soupeř do X sekund (live) nebo pro úplně nové hráče, nabídnout zápas proti AI označené jako bot. Nikdy nevydávat bota za člověka *(návrh)*.

## 3. Matchmaking a žebříček

- **Rating:** ELO nebo Glicko-2 (lepší pro málo odehraných her) *(návrh: Glicko-2)*. Skryté MMR pro párování, viditelné ligy pro hráče.
- **Ligy:** Bronz, Stříbro, Zlato, Platina, Diamant, Mistr *(návrh)*. Sezóna 4 týdny, soft reset na konci, odměny podle ligy.
- **Párování:** podle MMR, rozšiřování okna podle času čekání. U async módu stačí párovat z fronty bez nutnosti být online.
- **Backend:** Shared Game Backend. Fronta, stav zápasu, tahy, MMR a sezónní leaderboard jako SGB služby, identita přes NOX ID. Leaderboard přes SGB (CODE-71) s anti-cheat limity.
- **Placement:** prvních 5 zápasů s rychlejším posunem ratingu.

## 4. Fairness: meta progrese vs. PvP

Největší designové riziko. Hexapolis má progresi jednotek (rarity, hvězdy, levely), PowerProgress a nově City V2 boosty. V PvP nesmí vyhrávat peněženka ani délka hraní.

**Doporučený model *(návrh)*: normalizovaný rated PvP + nenormalizovaný casual.**

| Prvek | Rated PvP | Casual / přátelé |
|---|---|---|
| Statistiky jednotek | normalizované na jednotný level (např. všechny jednotky na "PvP levelu") | plné, podle hráče |
| Odemčené jednotky / hrdinové | jen ty, které hráč má, ale se stropem rarity *(otevřená otázka)* | vše, co hráč má |
| City V2 boosty | vypnuté, nebo jen kosmetické a pohodlnostní (ne bojové) | zapnuté |
| Jednorázové prémiové předměty (lektvary, kostky) | zakázané | povolené |
| PowerProgress | nepoužívá se pro výpočet síly v zápase, jen pro párování v casual | párování podle PowerProgress |

Princip: **progrese odemyká volby (víc jednotek, víc strategií), ne čistou sílu.** Rozmanitost místo převahy.

**OP jednotky:** v playtestech už se ukázalo, že Warrior, Archer, Knight a Solmyr po vylevelování rozbíjí obtížnost. Pro PvP:
- všechny bojové hodnoty PvP verze jednotek přes remote config, oddělené od PvE hodnot,
- telemetrie win rate podle jednotky a hrdiny, alarm nad 55 % *(návrh)*,
- balance patch přes RC bez buildu, jednou za sezónu nebo hotfix.

## 5. Anti-cheat, odpojení, AFK

**Autorita serveru.** Tahová hra je pro to ideální: klient posílá jen akce (pohyb, útok, stavba, výzkum), ne výsledný stav.

| Varianta | Jak | Náklad | Doporučení |
|---|---|---|---|
| **Deterministická simulace + validace** | Sdílená herní logika (C#) běží i na serveru nebo se tahy na serveru přehrají a ověří. Server drží seed RNG. | střední: logiku zápasu je nutné oddělit od Unity | **ano, cíl** |
| Validace jen klíčových pravidel | Server kontroluje legálnost akcí (dosah, cena, akční body), ne celou simulaci | nízký | MVP, pokud plná simulace nestihne leden |
| Důvěra klientovi | Klient posílá stav | žádný | ne |

- **Replay:** každý zápas uložený jako seed + seznam akcí. Slouží pro reporty, kontrolu podezřelých výsledků i sdílení (navazuje na existující bug report nástroj).
- **Podezřelé chování:** nemožné výsledky, extrémní win streaky, statistiky mimo rozsah. Flag a ruční kontrola, ban přes SGB (vynucení banů je v SGB A3).
- **Odpojení (live):** 60 s na návrat, pak tah propadá. Dva propadlé tahy = prohra *(návrh)*.
- **AFK (async):** po vypršení limitu tahu se tah přeskočí, po 2 přeskočených tazích prohra. Hráč, který hru opustí, dostane penalizaci MMR a krátký zákaz rated fronty.
- **Vzdání:** povolené kdykoli, počítá se jako prohra.

## 6. Odměny a napojení na City V2

- PvP zápasy dávají **suroviny a materiál do města (City V2)**, ne sílu do PvP. Tím se PvP stává druhým zdrojem pro stavbu města vedle kampaně.
- Sezónní odměny podle ligy: kosmetika města (budovy, dekorace, vlajky), rámečky profilu, tituly. Ukazují se na globální mapě a při návštěvě města.
- Denní PvP truhla za první výhru dne *(návrh)*.
- Navazující krok (pozdější): útoky na města ostatních hráčů a armády patří do City V2 designu, ne do tohoto dokumentu.

## 7. Monetizace (hypotézy k ověření)

| Hypotéza | Co testujeme | Pozn. |
|---|---|---|
| **Subscription** (např. "Hex Pass Plus"): víc souběžných async her, statistiky zápasů, replay, PvP kosmetika, bez reklam | Zaplatí si hráči za PvP komfort a obsah? | David zmínil subscription přímo jako ověřovací signál |
| **PvP battle pass / sezóna** | Placená vrstva sezónních odměn | Hexapolis už battle pass má, rozšířit o PvP úkoly |
| Kosmetika | Skiny jednotek a města, jen vizuální | Bez vlivu na rated PvP |
| Reklamy | Rewarded jen mimo zápas (extra truhla, rychlejší refill) | V zápase nikdy |

Pravidlo: **v rated PvP se nedá koupit výhoda.** Jinak to rozbije důvěru komunity a ověřování ztratí smysl.

## 8. Postup vývoje a technika

Z voice note: PvP, mapu (City V2) a UGC není nutné vyvíjet ve starém Hexapolisu. Vyvíjet v moderní technologii a potom importovat do původního Hexu, feature po feature.

| Vrstva | Kde vzniká | Proč |
|---|---|---|
| Backend PvP (fronta, stav zápasu, MMR, sezóny, replay, bany) | **Shared Game Backend**, staging přes Mecha Fortress | MF je náš staging projekt pro SGB; služby pak sdílí všechny hry |
| Herní logika zápasu (hex pravidla, validace tahů) | **Hexfort codebase** (= budoucí Hexapolis 2), jako oddělený modul bez závislosti na Unity scéně | Moderní kód, stejná logika poslouží serveru i oběma hrám |
| UI a flow PvP | Hexfort, potom port do Hexapolisu 1 | |
| Nasazení k hráčům | **Hexapolis 1** (původní hra, živá komunita) | Ověření na reálných hráčích bez čekání na Hex 2 |

**Časová osa (z voice note):**

| Období | Co |
|---|---|
| listopad 2026 | Start: design dotáhnout, oddělit herní logiku, SGB služby pro zápasy a frontu, async 1v1 interně hratelné |
| prosinec 2026 | Doručit: interní testy, anti-cheat validace, import do Hexapolisu 1 za RC flagem |
| leden 2027 | Mezi hráče: postupné zapínání (RC procenta), komunitní test, reaktivace bývalých hráčů |

Každá featura za vlastním RC flagem (`hex_pvp_enabled`, `hex_pvp_ranked_enabled` *(návrh)*), stejně jako v SGB roadmapě.

## 9. Komunita a reaktivace

- **Uzavřený test s komunitou** (Discord) v prosinci: pozvat nejaktivnější hráče, sbírat feedback, co by upravili.
- **Reaktivační kampaň** na bývalé hráče Hexapolisu: "PvP je tady". Push, e-mail přes NOX ID (s marketingovým souhlasem), Discord, store update text.
- **Feedback smyčka:** hlasování o dalších PvP módech a mapách v Community Hubu (SGB F1), až bude.

## 10. Metriky, které rozhodují o Hexapolis 2

PvP je jeden ze tří testů (PvP, City V2, UGC). Pro greenlight Hexapolis 2 sledujeme *(cílové hodnoty návrh, potvrdit s Davidem a Jirkou)*:

| Metrika | Co říká | Cíl *(návrh)* |
|---|---|---|
| Podíl DAU, který zkusí PvP | zájem | 25 %+ |
| PvP zápasů na PvP hráče týdně | opakované hraní | 5+ |
| D7 / D30 retence PvP hráčů vs. ostatní | přidaná hodnota | +20 % relativně |
| Návrat bývalých hráčů po kampani | síla značky + featury | sledovat, baseline neexistuje |
| Konverze na subscription / PvP pass | ochota platit | 1 až 2 % PvP hráčů |
| ARPDAU Hexapolisu 1 před a po | dopad na revenue (dnes cca $15k / měsíc) | růst |
| Win rate top jednotek | balance | pod 55 % |
| Reporty podvádění na 1 000 zápasů | integrita | nízké, trend klesá |

Rozhodnutí: když PvP i City V2 ukážou zájem a ochotu platit, připravit design Hexapolis 2 postavený pro PvP od základu (Hexafort GDD, fáze A).

## 11. UGC (třešnička na dortu)

Až po PvP a City V2. Ne podmínka pro greenlight, ale silný nástroj pro live ops.

- **Mapy od hráčů:** editor map ve hře, postavený na existujícím interním nástroji pro custom mapy (Hexapolis už ho má pro testování).
- **Sdílení:** kód mapy / odkaz, procházení oblíbených a nových, hodnocení. Úložiště a katalog přes SGB (Hexapolis UGC je v backlogu jako CODE-8).
- **Live ops nad UGC:** "mapa týdne", výzvy na komunitní mapě, soutěže o nejlepší mapu (napojit na Community Hub a hlasování).
- **PvP vazba:** vybrané komunitní mapy do casual PvP rotace, ne do rated.
- **Moderace:** názvy a popisy přes profanity filtr, report tlačítko, schvalování před zařazením do "doporučených", validace mapy (hratelnost, symetrie pro PvP).

## 12. Drobnost: suroviny na Hex mapě

Z voice note: **přidat suroviny do Hex mapy.** Napojení na City V2: suroviny vytěžené na mapě v zápase se přenáší do města. Detail patří do design dokumentu City V2, tady jen jako závislost (PvP odměny v surovinách, kap. 6).

## 13. Rizika

| Riziko | Dopad | Zmírnění |
|---|---|---|
| Malá hráčská base, dlouhé čekání na soupeře | špatný první dojem | async jako první mód, boti jako fallback, hra s přáteli |
| Pay to win pocit | odchod komunity, recenze | normalizace v rated PvP, kap. 4 a 7 |
| Cheateři | ztráta důvěry v žebříček | server validace, replay, bany přes SGB |
| OP jednotky | jeden dominantní build | oddělené PvP hodnoty v RC, telemetrie win rate |
| Oddělení herní logiky od Unity je pracnější, než vypadá | posun termínu | MVP s validací klíčových pravidel, plná simulace později |
| Port z Hexfortu do starého Hexapolisu (rozdílný kód) | dvojí práce | logika jako samostatný modul se stejným rozhraním v obou hrách |
| Kapacita (Q4 je kvartál live ops, žádný nový titul) | PvP soupeří o lidi s Sector Defense a RC | agenti na backend a logiku, lidský čas dávkovat jako v SGB roadmapě |

## 14. Otevřené otázky pro Davida

1. **Kde přesně vzniká herní logika PvP:** v Hexfortu (Hex 2 codebase), nebo v Mecha Fortressu? Voice note zmiňuje obojí. Návrh: backend přes MF/SGB staging, hex logika v Hexfortu.
2. **První mód:** souhlas s async 1v1 jako MVP pro leden, live blitz až potom?
3. **Fairness:** plná normalizace statů v rated PvP, nebo jen strop (např. max rarita / level)? A smí rated PvP používat hrdiny?
4. **City V2 boosty v PvP:** úplně vypnout, nebo povolit pohodlnostní (ne bojové)?
5. **Navazuje prototyp z května** (Codex 5.5)? Kde leží a kdo ho převezme?
6. **Vlastník** PvP featury (design, dev) a vztah k HEX-2-0249-72 a OKR O5.2 (termín 30. 11.): posunout na leden?
7. **Monetizace:** testovat subscription hned při launchi PvP, nebo až po měsíci dat?
8. **Cílové hodnoty metrik** v kap. 10: potvrdit, případně doplnit s Jirkou.
