# Produkční strategie NOXGAMES 2027

> **Stav:** pracovní verze 2, 1. 11. 2026. Zdroj: voice note Davida (`voice/Strategie.txt`, surový přepis Whisper) + Q4 OKR + exec porada 24. 9.
> **Zdroj pravdy:** tento MD. Z něj vychází: tasky v NoxHubu, wiki (kategorie Strategie), prezentace pro vedení.
> **Detailní dokumenty:** `DESIGN_CITY_V2.md`, `DESIGN_HEX_PVP.md`, `KONCEPT_STRATEGICKA_VETEV.md`.

## Shrnutí v pěti větách

1. MF-branch (Mecha Fortress, Command, Sector) má **ověřený recept na rychle splatnou hru**. Gameplay už neiterujeme, v 2027 vydáme **2 až 3 reskiny** se silnými tématy vybranými přes CPI testy.
2. Sdílená práce, která podpoří současné i budoucí hry: **City V2 meta** a **SharedGameBackend**.
3. **Hexapolis zůstává civilization-like.** Do původního Hexu postupně přidáme City V2, PvP a UGC, ověříme, že to hráči chtějí a zaplatí, a teprve pak navrhneme **Hexapolis 2**.
4. Otevíráme **strategickou větev**: hry mezi složitým Hexem a jednoduchým Mecha Fortressem, víc idle s většími rozhodnutími, PvP tam, kde přirozeně sedí. Cíl 2027: **aspoň 2 unikátní tituly**.
5. Cíl 2027 je **až 5 nových titulů** (2 reskiny + 2 strategické tituly + Hexapolis 2). Všechny stojí na tom, co už máme nebo dotáhneme letos, takže jde o posun produkce bez velkého neověřeného rizika. Nové tituly mají nahradit slábnoucí hry z roku 2026.

## Sdílený základ všech her

| Prvek | Co to je | Pro koho |
|---|---|---|
| **City V2 meta** (= Mapa V2, Město V2, stejná feature) | Samostatný modul budování města mezi zápasy, inspirace Rise of Kingdoms a Clash of Clans. Se základní hrou komunikuje přes vstupy, výstupy a požadavky. Detail: `DESIGN_CITY_V2.md` | MF reskiny, původní Hexapolis, Hexapolis 2, strategická větev |
| **SharedGameBackend** | Jeden backend pro všechny tituly: Nox ID (tracking hráčů napříč tituly), invite friends, klany, leaderboardy, promo kódy. Pod jednou střechou, ovládaný agenty, na míru našim hrám, cesta k automatizaci live-ops | Všechny hry |
| **MF meta** | Vyvinutá meta MF-branch | MF reskiny, strategická větev |

**Mecha Fortress je staging projekt** pro City V2, PvP a SharedGameBackend. Feature se vyvine tam, pak se importuje do dalších her.

## Větev 1: MF-branch reskiny

- Gameplay MF-branch neiterujeme, máme potvrzený recept.
- **2 až 3 reskiny v 2027** (NoxHub: NOVE-11, NOVE-12) se silnými tématy, ve stejné kvalitě jako dosud, ideálně s něčím navíc.
- City V2 a SharedGameBackend se do reskinů integrují postupně, až budou hotové.
- **Postup:** CPI testy tématik spustit ještě do konce 2026 → leden příprava → výroba.
- Kandidátní témata v CPI: Warcraft-like fantasy (CPI-9), zombie (CPI-10), další.

## Větev 2: Hexapolis a Hexapolis 2

**Pozice:** nabídnout nejlepší civilization-like gameplay na mobilu. Hex neměníme na pasivní/idle hru.

**Co je špatně:** jen vzít metu z Mecha Fortressu a nasadit ji na gameplay Hexu.

**Co hráči chtějí a co přidáváme do původního Hexu (feature po feature):**

| Feature | Proč | Kde se vyvíjí | Detail |
|---|---|---|---|
| **City V2** (stavění města mezi zápasy) | hráči to vždycky chtěli, dlouhodobá motivace | Mecha Fortress (staging) → import do Hexu | `DESIGN_CITY_V2.md` |
| **PvP** | Polytopia nás dnes poráží hlavně tím, náskok lze rychle smazat | Mecha Fortress (staging) / moderní technologie (Hexfort) → import do Hexu | `DESIGN_HEX_PVP.md` |
| **UGC** (vlastní mapy, sdílení, live-ops nad nimi) | třešnička na dortu, až po City a PvP | moderní technologie (Hexfort) | `DESIGN_HEX_PVP.md`, sekce UGC |
| Suroviny na hex mapě | drobnost z poznámek | Hex | task |

**Časování:** listopad 2026 vývoj → prosinec dodání a interní test → leden 2027 vydání hráčům, test s komunitou, pokus o re-engagement hráčů, kteří odešli.

**Co ověřujeme (gate pro Hexapolis 2):**
- hráči interagují se stavěním města,
- hráči hrají PvP,
- hráči za to platí (IAP, případně subscription).

**Hexapolis 2 po ověření:** pořád plnohodnotný civilization-like, upravená a zjednodušená meta, pravděpodobně jiná tématika, design od začátku pro PvP a dlouhodobé hraní přes město. "To, čím měl Hexapolis vždycky být."

**Idle spin-off Hexu** (hexová strategie, ale víc idle) nepatří sem, ale do strategické větve.

## Větev 3: Strategická větev

Detail: `KONCEPT_STRATEGICKA_VETEV.md` (NoxHub: NOVE-10).

- **Esence:** Hexapolis je moc složitý, Mecha Fortress moc jednoduchý. Mezi nimi je prostor.
- Stojí na MF metě, City V2, SharedGameBackend a sociálních features.
- Gameplay: víc idle než MF, ale s většími rozhodnutími. Zápasy na kola nebo vlny: hráč udělá několik rozhodnutí, použije itemy, pak sleduje výsledek.
- PvP tam, kde přirozeně sedí, ne na sílu. Reference: Mechabellum, Clash Royale, Voodoo base + minion battlery, Goblin Gold Miners.
- Jde snadno PvE i PvP, hodně prostoru pro experimenty a tweaky.
- Tým to baví, na Game Jamu chce řada lidí dělat Mechabellum-style hry.
- **Cíl 2027:** aspoň 2 unikátní tituly.

## CPI testy

Kadence: minimálně 1x měsíčně, začít ještě v listopadu až prosinci 2026.

| Směr | Co testujeme | Jak | NoxHub |
|---|---|---|---|
| **A: MF reskiny** | témata pro 2 až 3 reskiny (fantasy/Warcraft, zombie, další) | klasický MF setting | CPI-11 (+ CPI-9, CPI-10) |
| **B: Hex 2 a strategická větev** | tematika (římská, Warcraft-like a další) | stejná struktura testu, jedny základní assety převedené do různých tematik; setting MF i Hex | CPI-12 |

## Roadmapa

| Období | MF-branch | Hexapolis | Strategická větev | Sdílené |
|---|---|---|---|---|
| **XI 2026** | CPI testy témat reskinů | vývoj City V2 + PvP (staging v MF), design dokumenty | sběr konceptů, Game Jam | SGB integrace do MF |
| **XII 2026** | vyhodnocení CPI, výběr témat | dodání City V2 + PvP, interní test | CPI testy tematik (směr B) | City V2 MVP |
| **I 2027** | start reskinu #1 | release do původního Hexu, komunitní test | prototypy (max 2 sprinty na koncept) | |
| **II až III 2027** | reskin #1 výroba / launch | vyhodnocení, UGC; rozhodnutí o Hex 2 | greenlight titulu #1 | City V2 do reskinů |
| **Q2 až Q4 2027** | reskin #2 (a #3) | Hexapolis 2 vývoj (pokud gate projde) | titul #1 výroba, titul #2 prototyp | |

Roadmapa od února dál je orientační, upřesní se po vyhodnocení CPI a lednového releasu v Hexu.

## Otevřené otázky (neblokují start)

1. **Vlastníci:** kdo vede City V2, PvP v Hexu, strategickou větev a CPI program? Voice note jména neuvádí.
2. **Reskiny:** 2, nebo 3? V NoxHubu jsou zatím 2 (NOVE-11, NOVE-12).
3. **Kapacita:** listopad až prosinec souběžně City V2, PvP, SGB a CPI. Kdo na čem?
4. **Gate pro Hex 2:** jaká čísla (podíl hráčů v PvP, D30, ARPDAU, konverze na subscription) stačí na schválení?
5. **Rise of a Nation** (`Hexapolis_India/`): sdílí kód nebo City V2 s Hexapolisem?

## Výstupy

- [x] Surový přepis: `voice/Strategie.txt`
- [x] Strategický dokument (tento)
- [x] Design dokumenty City V2, PvP v Hexu, koncept strategické větve
- [x] Tasky v NoxHubu: NOVE-13 až NOVE-38, CPI-13 až CPI-16 (subtasky pod NOVE-1, 5, 7, 9, 10, 11, 12 a CPI-11, 12)
- [x] Wiki: Strategie / Produkční strategie 2027 (4 stránky)
- [x] Prezentace pro vedení: `strategie-2027-prezentace.html` (draft, 18 slidů)
- [ ] Porada vedení: rozhodnout vlastníky, kapacitu, 2 nebo 3 reskiny, čísla pro gate Hex 2 (NOVE-19)

## Wiki stránky
- [Produkční strategie 2027 (přehled)](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=e6497b8c-3f2c-406c-a8d2-8a023e66e3bd)
- [City V2 meta: design dokument](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=40baabfd-d09b-4007-8a25-3a58f49ee1b7)
- [PvP v Hexapolisu: design dokument](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=1289bcaf-4811-484e-a5cb-d59c9d870d20)
- [Strategická větev: koncept](https://hub.noxgames.com/wiki?category=26ffba05-b690-4250-8b91-3cbed02563b6&doc=19838dbd-8e92-401b-b4d2-28b79b4f7b11)
