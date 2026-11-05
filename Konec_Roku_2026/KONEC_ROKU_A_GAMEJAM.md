# Konec roku 2026 a GameJam

> **Stav:** 5. 11. 2026, návrh Davida. Podklady: roadmapa a zpráva Aldyho z 3. 11. 2026, `STRATEGIE_PRODUKCE.md`, `KONCEPT_OBNOVA_HEXU.md`. Věci označené *(návrh)* je potřeba potvrdit.
> **Pro AI agenty:** zdrojem pravdy je tento soubor. Termíny Hexu navazují na `KONCEPT_OBNOVA_HEXU.md`, témata jamu na `CPI_PIPELINE.md` a `SHRNUTI_NOXENGINE.md`.

## 1. Shrnutí

- **Do konce roku chceme dvě věci hotové:** SharedGameBackend (SGB) integrovaný **aspoň v jedné hře** a v Hexu **hotové a implementované featury PvP, City V2 a UGC** (za RC flagy, k hráčům od ledna).
- **Exekutiva** má nejpozději **1. 12.** první schůzku k vyhodnocení roku 2026 a ke strategii 2027.
- **Poslední pracovní týden 14. až 18. 12. se nic nevydává.** Je to uvolněný týden ve znamení **GameJamu** s tématy pro projekty 2027 a společným **AI workshopem** na celý vývojový cyklus.
- **18. 12.** si hry projdeme a vyhodnotíme, večer **firemní párty**. Od 21. 12. volno.
- Podle Aldyho roadmapy to sedí: Red Command nejpozději 11. 11., pak sprinty Sector Defense a MF, 7. až 11. 12. úklid a opravy, 14. až 18. 12. XMAS JAM.

## 2. Kalendář do konce roku

| Týden | Produkce (Aldy) | Firma a vedení |
|---|---|---|
| 2. až 6. 11. | sprint Red Command, A/B test obtížnosti Sector Defense | |
| 9. až 13. 11. | **Red Command hotový nejpozději 11. 11.** (grafika offerů, balanc); jednotýdenní buffer, plán zbytku roku | |
| 16. až 27. 11. | sprint Sector Defense (do 4. 12.) a sprint MF (do 27. 11.) | **19. 11. porada vedení** |
| 30. 11. až 4. 12. | konec sprintu Sector Defense | **do 1. 12. schůzka exekutivy:** vyhodnocení roku a strategie 2027 |
| 7. až 11. 12. | **úklid a opravy, poslední release roku:** zimní eventy Sector Defense a MF | |
| 14. až 18. 12. | **bez releasů: GameJam + AI workshop** | **18. 12. vyhodnocení her a párty** |
| 21. 12. až 1. 1. | volno, zimní eventy běží | pohotovost na live ops *(návrh)* |

Davidův návrh pro Aldyho platí: po Red Command jeden týdenní sprint na dohodu, co stihneme buď v jednom čtyřtýdenním, nebo ve dvou dvoutýdenních sprintech, tak aby poslední týden zůstal volný na jam.

## 3. Produkce do konce roku (Aldy, 3. 11.)

![Roadmapa Aldyho, říjen až prosinec 2026](roadmap-aldy-2026-11.png)

**Red Command:** za nás hotový **nejpozději 11. 11.** Dolaďuje se grafika offerů a balanc (hlavně Karel). Na roadmapě je sprint RC od 12. 10. s gacha hrdiny, novými věžemi, stěnami, talenty a novými jednotkami, pak test, polish a release.

**Mecha Fortress:**
- balíček **Welcome back**;
- **reskin board game eventu na Vánoce** (práce pro grafiky, Peko nebo další);
- zimní event od 7. 12.

**Sector Defense:**
- nový **A/B test obtížnosti**;
- v dalším sprintu úpravy tutorialu a drobnosti, které šly do Red Command (reklamy v metě);
- grafika backgroundů, board game a jeho odměny, grafika gacha claim, změny v ad monetizaci, release;
- Aldy s Karlem zvažují přidat aspoň **leaderboard**;
- board game na svátky a zimní event od 7. 12.

**Kapacita:** podle Aldyho jsou to menší věci a plán sedí. **Kódově bude konec roku volnější**, práce je víc na grafice. Kodéři si proto vytáhnou úkoly z backlogu a připraví začátek roku 2027. Tuto volnou kapacitu dáváme do SGB a featur v Hexu (kapitola 4).

## 4. Co chce David mít hotové do konce roku

| Cíl | Co znamená hotovo | Termín |
|---|---|---|
| **SGB aspoň v jedné hře** | hra posílá data do SGB a používá aspoň jednu službu (Nox ID, žebříčky, PvP backend) v produkčním buildu | release nejpozději 11. 12. |
| **PvP v Hexu** | Skill only a All-out-power, Quick game Speed a Normal, žebříčky přes SGB, za RC flagem | implementováno do 11. 12., hráči v lednu |
| **City V2 v Hexu** | verze 1 (stavění, suroviny, upgrady, budovy s meta staty) importovaná z MF stagingu, za RC flagem | implementováno do 11. 12., hráči v lednu |
| **UGC v Hexu** | editor map ve hře, sdílení kódem, komunitní mapy v rotaci, za RC flagem | implementováno do 11. 12., hráči v únoru |

- **Kterou hrou začít se SGB** *(návrh)*: přirozeně **Hexapolis**, protože PvP žebříčky na SGB stejně stojí. Menší a rychlejší varianta je **leaderboard v Sector Defense**, o kterém mluví Aldy s Karlem: mohl by jít ven ještě před freeze a ověřit SGB na živé hře.
- **UGC se tím posouvá dopředu:** v konceptu obnovy Hexu šlo UGC až po lednu. Teď má být implementované do konce roku a k hráčům jde v únoru.
- Všechno za vlastními RC flagy, takže implementace v prosinci neznamená release v týdnu jamu.

## 5. Schůzka exekutivy do 1. 12.

Navazuje na poradu 19. 11. Program *(návrh)*:

1. **Vyhodnocení roku 2026:** čísla (zisk, tržby po hrách, viz `CILE_2027.md`), co se povedlo a co ne, projekty, lidé.
2. **Strategie 2027:** schválení větví a produktů (`STRATEGIE_PRODUKCE.md`), obnova Hexu a gate Hexapolis 2.
3. **Cíle 2027 a platy:** scénář cíle, brány a preset platů, pokud se nerozhodly 19. 11.
4. **Delegace od 1. 1.:** vlastníci segmentů a projektů.
5. **Konec roku:** potvrdit release freeze, GameJam, budget a pohotovost přes svátky.

## 6. Poslední týden: bez releasů

- **Poslední release roku je 11. 12.** Zimní eventy, board game, Welcome back a všechno ostatní musí být venku do té doby.
- **14. až 18. 12. se nic nevydává.** Výjimka jen hotfix na pád hry nebo chybu, která zásadně bere revenue, se souhlasem Davida *(návrh)*.
- Live ops běží na tom, co je venku. Přes svátky jeden člověk drží pohotovost na pády a eventy *(návrh: rotace)*.
- Letos to chceme **konečně dodržet**. Proto je freeze napsaný v plánu sprintů už teď, ne až v prosinci.

## 7. GameJam 14. až 18. 12.

### Proč

- Uvolněný týden, který zároveň vyrobí **základ pro projekty 2027**.
- Každý si vyzkouší **celý vývojový cyklus s AI** sám nebo v malém týmu. Je to i trénink na workflow, které ukázal NoxEngine a Warcamp.

### Témata

| Téma | Příklad směru | Vazba na 2027 |
|---|---|---|
| **Tweaky formule Hexapolisu** | jiná mapa, kratší partie, PvP twist, nová frakce | obnova Hexu, nový Hexapolis 2 |
| **Strategické idle hry** | hry mezi Hexem a MF, rychlá strategie s PvP přesahem | strategická větev, titul #1 |
| **Twisty MF-branch** | nový žánrový háček na metě MF, jiné téma | reskiny MF a Sector Defense |
| volné | cokoliv, co obhájí přínos pro 2027 | |

Nejlepší nápady můžou jít do **CPI pipeline** v lednu *(návrh)*, viz `CPI_PIPELINE.md`.

### Program

| Den | Co |
|---|---|
| po 14. 12. dopoledne | **AI workshop: celý vývojový cyklus.** Nápad, krátký design, prototyp v Claude Code, assety přes Higgsfield (obrázky, 3D modely), build, hratelná verze. Vedou David a Czode *(návrh)* |
| po 14. 12. odpoledne | výběr tématu, týmy po 1 až 3 lidech |
| út až čt | vývoj, průběžná pomoc s AI nástroji |
| **pá 18. 12.** | **prezentace a vyhodnocení her**, večer párty |

**Výstup každého týmu:** hratelný build a jedna stránka: co to je, pro koho, proč by to mělo smysl v 2027.

**Vyhodnocení 18. 12.** *(návrh)*: každý tým 5 minut ukázka. Hodnotí se zábava, napojení na strategii 2027, proveditelnost a potenciál pro CPI test. Hlasuje celá firma, exekutiva vybere, co pokračuje.

### Budget

| Položka | Kolik |
|---|---|
| Extra účty Claude | 1 až 2 účty na dobu jamu |
| Kredity Higgsfield | generování obrázků a 3D modelů |
| Asset pack | **50 USD na člověka**, jen když o něj někdo požádá |

Částku za Claude a Higgsfield doplnit podle tarifu. Asset packy maximálně 50 USD × počet lidí, kteří o ně požádají (při 16 lidech nejvýš 800 USD).

## 8. K rozhodnutí

| # | Otázka | Kdo | Do kdy |
|---|---|---|---|
| K1 | Termín schůzky exekutivy (nejpozději 1. 12.) | Jirka, David | 19. 11. |
| K2 | Release freeze od 14. 12., poslední release 11. 12. | exekutiva | 19. 11. |
| K3 | Ve které hře je SGB první: Hexapolis, nebo leaderboard v Sector Defense | David, Aldy, Karel | plán sprintu po 11. 11. |
| K4 | UGC implementované do konce roku: kapacita kodérů | David, Mirek | plán sprintu po 11. 11. |
| K5 | Budget jamu: Claude účty, Higgsfield, asset packy | Jirka, DJ | 1. 12. |
| K6 | Pohotovost na live ops přes svátky | Martin V., Aldy | 11. 12. |
