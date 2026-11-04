# NoxEngine + Warcamp: shrnutí pro vedení

**Stav:** 4. 11. 2026. Zdroje: repo `Experiments/NoxEngine` (README 0.2, git log 2. až 3. 11., build reporty `docs/reports/*.md`, průvodci 0.2), `STATUS_2026-11-02.md`, `RESEARCH.md`, `GDD_WARCAMP.md`, `ROADMAP.md`. Živý web s buildy, dokumentací a videi: [noxengine.studio-0b0.workers.dev](https://noxengine.studio-0b0.workers.dev). Kde se zdroje liší, platí novější důkaz (git log, reporty 0.2) a u každého čísla rozlišujeme, co je ověřené a co je jen tvrzení.

## Shrnutí

- **Je to proof of concept vlastního enginu.** NoxEngine 0.2 (Rust) běží: editor ve stylu Unity, hra Warcamp na webu, Android APK a iOS v simulátoru, online PvP na Cloudflare. Ověřené testy a záznamy, ne slidy.
- **Hlavní hodnota je jiné workflow, s nápadem přišel Czode (Jan Š., senior Unity developer).** Engine je postavený tak, aby ho celý ovládali AI agenti: 174 příkazů, které agent volá stejně jako člověk tlačítka v editoru. Obsah je v datech, kvalitu hlídá oddělený kritik.
- **Warcamp ukazuje, jak rychle jde udělat strategickou hru s PvP a naší metou.** Trofeje, truhly, levely jednotek, obchod, City V2, žebříček a 4 skiny včetně mecha. Celé repo má 71 commitů mezi 2. a 3. 11. 2026.
- **Neověřené zůstává to podstatné pro byznys:** výkon na reálném telefonu, skutečné SDK (AppLovin MAX, Firebase), iOS na zařízení a hlavně srovnání rychlosti s Unity. Žádná ze sedmi kill gates zatím formálně neprošla.
- **Návrh:** schválit časově omezenou sázku podle `RESEARCH.md` (2 inženýři + agenti, gates po sprintu 2, 3 a 4), Mecha Fortress a Unity týmy nechat beze změny.

## 1. Proof of concept enginu: vlastní engine je proveditelný

Co v repu existuje a je ověřené (zdroj: README 0.2, reporty v `docs/reports/`):

| Oblast | Stav | Důkaz |
|---|---|---|
| Engine a editor | Play/Stop, hierarchie, inspektor, gizmy, undo/redo, prefaby, profiler, skriptování (Rhai), rozšíření editoru | reporty editor a scripting, smoke test 22/22 |
| Ovládání agenty | 174 příkazů přes MCP, agent vidí přesně to, co hráč (screenshoty i bez okna) | web, smoke test |
| Platformy | web (WebGPU i WebGL2) živě, Android APK 5,9 MB na emulátoru, iOS v simulátoru 60 fps | report platform |
| Online PvP | relay na Cloudflare, reconnect, ranked, žebříček, rematch, ghost zápasy | 20/20 testů relay, prohlížeč proti nativnímu klientovi 502 tahů bez desyncu |
| Determinismus | stejný vstup dá na všech platformách bitově stejný zápas | golden test prošel na macOS a wasm32, Linux a Windows jen v CI (zatím nespuštěno) |
| Masové scény | 50 000 jednotek při 219 fps na Apple M5, v Chrome stabilních 60 fps | report massive, měřeno na vytíženém stroji |

Engine nestaví vše od nuly: rendering, UI a audio jsou hotové open-source knihovny (wgpu, egui, kira). Vlastní je to, co z něj dělá náš engine: příkazy pro agenty, obrazovky a okna z NoxE, data, skiny, PvP a editor. Licence vychází na 0 USD, pro srovnání Unity Pro by při 33 místech stálo zhruba 76 tisíc USD ročně. Samotná úspora licencí ale podle `RESEARCH.md` sázku neospravedlňuje.

Detail: `STATUS_2026-11-02.md` (stav 0.1), `ARCHITECTURE.md`, `NOXENGINE_GUIDE.md`.

## 2. Jiné workflow: agent dělá práci, člověk rozhoduje a kontroluje

Myšlenka, se kterou přišel Czode: místo toho, aby AI pomáhala programátorovi v Unity zvenku, postavit nástroj, ve kterém je agent hlavní uživatel. Rozdíl proti dnešnímu Unity workflow:

| Dnes v Unity | V NoxEngine |
|---|---|
| Agent vidí Unity úzkým oknem (MCP pluginu), řadu věcí musí udělat člověk v editoru | **Jedna ovládací plocha:** každá akce v enginu je příkaz, agent může všechno co člověk, včetně klikání v UI hry a screenshotů |
| Balanc a obsah často v prefabech a kódu, změna znamená zásah vývojáře | **Obsah jako data:** jednotky, karty, ekonomika, arény a efekty jsou JSON s hot reloadem; designér nebo agent změní číslo a hned to vidí |
| Balanc se ladí hraním | **Simulátor bitev:** 200 zápasů botů proběhne během chvíle (poslední běh 102/98, průměr 4:11), agent ladí balanc sám |
| Reskin je projekt | **Reskin je složka:** modely, barvy, fonty, názvy a zvuky ze složky skinu, bez změny kódu; Pirates a Undead vznikly takto |
| Kvalitu posuzuje ten, kdo věc udělal | **Gauntlet Loop:** výsledek porovná s reálnou referencí čerstvý agent kritik, který neviděl, jak vznikl, a odpoví jen OURS nebo BAR plus jednu největší mezeru |

Verzi 0.2 podle průvodce stavělo jedenáct paralelních agentů, každý na vlastní větvi s písemným reportem, pak se vše sloučilo a znovu ověřilo. Proč by to mohlo být rychlejší: Rust kompilátor chytí většinu chyb agenta před spuštěním, determinismus dovoluje agentovi přehrát a ověřit každý zápas bez člověka a data se mění bez buildu. Jak rychlé to skutečně je proti Unity se stejným agentem, zatím **nikdo neměřil** (gate K3).

Detail: `GAUNTLET_LOOP.md`, `ARCHITECTURE.md`.

## 3. Warcamp: strategická hra s PvP a naší metou

Portrait PvP lane battler: horníci těží zlato, za 100 zlata hráč vybírá 1 ze 3 karet (budovy, ekonomika, vylepšení), jednotky bojují samy, hráč řídí bitvu třemi schopnostmi hrdiny. Zápas trvá nejvýš 5 minut. Patří do strategické větve (`KONCEPT_STRATEGICKA_VETEV.md`): větší rozhodnutí než Mecha Fortress, PvP od prvního dne.

Meta odpovídá tomu, co stavíme v Mecha Fortress jako staging (`STRATEGIE_PRODUKCE.md`):

- **Trofeje a arény:** +30 / −15, tři arény odemykané trofejemi (0, 150, 350), žebříček top 50.
- **Truhly a levely:** truhla za výhru, mince na levely jednotek (+10 % statů za level), 7 jednotek, 5 schopností.
- **Obchod a skiny:** truhly za gemy (20 a 60), skiny za gemy, testovací rewarded reklama x2 na výsledku. Bez reálných plateb.
- **City V2 prototyp:** zápasy přinášejí dřevo a kámen, budovy města dávají bonusy do dalšího zápasu (`DESIGN_CITY_V2.md`), zatím jen 2D.
- **4 skiny z jednoho kódu:** Tribal, **Mecha** (MECHCAMP, blízko stylu Mecha Fortress), Pirates a Undead jako CPI testovací témata.
- **PvP:** online lockstep, a když nikdo není online, ghost zápas proti nahrávce skutečného hráče, jinak bot. Sedí na náběh PvP s boty, který plánujeme pro Hex.

Detail: `GDD_WARCAMP.md` (stav 0.1), `WARCAMP_GUIDE.md` (stav 0.2), hrát lze na [webu](https://noxengine.studio-0b0.workers.dev/play/).

## 4. Co je ověřené a co ne

| Ověřené (testy, záznamy, screenshoty v repu) | Jen tvrzení nebo neověřené |
|---|---|
| Hra se ovládá agenty přes MCP, smoke test 22/22 | Rychlost proti Unity: srovnání se nedělalo |
| PvP mezi webem a nativním klientem bez desyncu, 20/20 testů relay | Výkon na reálném Android telefonu: běželo jen na emulátoru, ten ukazuje zastaralé snímky |
| Determinismus na macOS a ve wasm32 | Linux, Windows, Android a iOS determinismus jen předpoklad nebo CI, které zatím neběželo |
| Android APK 5,9 MB, iOS simulátor 60 fps | iOS na zařízení a TestFlight: potřebuje Apple tým NOXGAMES |
| Most na SDK (JSON kanál) funguje na emulátoru a simulátoru se stubem | Skutečné AppLovin MAX a Firebase: zatím jen mock a testovací reklama |
| SharedGameBackend klient proti lokálnímu SGB | Na webu a Androidu SGB nefunguje, chybí transport |
| Reskin bez kódu (Pirates, Undead), kritik: pirates a mecha OURS, undead BAR | Zvuky nikdo neslyšel uchem, hra nebyla hraná na telefonu |

Ranked PvP zatím věří dvěma shodným klientům, server výsledek neověřuje a chybí rate limit, takže trofeje jdou farmit.

## 5. Rizika a kill gates

Hlavní rizika podle `RESEARCH.md`:

- **Mobilní napojení, ne grafika.** Pro Rust neexistují oficiální SDK pro MAX, Firebase, IAP ani Xsolla. Řešení jsou tenké nativní aplikace v Kotlinu a Swiftu, které SDK obslouží.
- **Agent-first už není unikát sám o sobě.** Unity má oficiální MCP, Unreal 5.8 experimentální. Náskok musí dát 100% pokrytí agenty, data a determinismus.
- **Lidská iterace v Rustu je pomalá** (kompilace, malý trh vývojářů). Proto musí hratelnost zůstat v datech.
- **Bus factor:** dnes je za vším git historie jednoho člověka s agenty. Do konce sprintu 3 mají buildy zvládnout aspoň 2 lidé.
- **Rozsah editoru:** verze 0.2 přidala hodně editoru dřív, než prošla gate K4, což K7 hlídá.

Kill gates (sprint = 2 týdny, **dva kill hlasy = stop**):

| Gate | Termín | Podmínka | Stav k 4. 11. |
|---|---|---|---|
| K1 Výkon | konec sprintu 2 | p95 do 16,7 ms se 150 jednotkami na referenčním Androidu, start do 3 s | neměřeno, jen emulátor |
| K2 Agent | konec sprintu 2 | agent zvládne úkoly (a) až (d) bez lidské úpravy kódu, každý pod 1 h | částečně doloženo (nové jednotky, balanc, reskin udělali agenti), ale neměřeno podle šablony |
| K3 Srovnání s Unity | konec sprintu 2 | NoxEngine nejvýš 1,5x čas Unity 6 + Unity MCP | nezačato |
| K4 SDK | konec sprintu 3 | MAX interstitial a rewarded, Firebase událost a RemoteConfig z Rustu na Androidu | jen stub a mock |
| K5 Velikost | konec sprintu 3 | prázdné AAB do 15 MB, hra do 25 MB | APK 5,9 MB bez SDK, AAB neměřeno |
| K6 iOS | konec sprintu 4 | hra na iPhone 12 přes TestFlight s MAX testovací reklamou | jen simulátor |
| K7 Rozsah | kdykoli | editor nad 35 % času před průchodem K4 | neměřeno, riziko |

Stav gates je naše čtení důkazů v repu, formální měření zatím neproběhlo. Při stopu se Warcamp (data a design) přesune do Godot 4.7 nebo Unity 6.3 LTS a NoxEngine zůstane jen interní nástroj (headless simulace, generátor playables).

## 6. Co rozhodnout

1. **Pokračovat jako časově omezená sázka, ne migrace?** `RESEARCH.md` navrhuje 2 inženýry a agenty na zhruba 6 sprintů do první soft-launchovatelné hry, potom zhruba 1 FTE na údržbu.
2. **Kdo ji vlastní?** Podle `RESEARCH.md` 1 senior na jádro enginu a FFI, 1 inženýr na mobilní shelly, CI a SDK. Otázka pro vedení: má roli vlastníka převzít Czode, od kterého workflow pochází?
3. **Uvolnit Unity vývojáře na kontrolní srovnání (K3) ve sprintu 1.** Bez něj nejde říct, jestli je workflow rychlejší.
4. **Potvrdit hranice:** lidi z Mecha Fortress nepřesouvat, NoxFort, MF reskiny a Hexapolis zůstávají v Unity.
5. **Další gate:** konec sprintu 2 (K1 až K3) na reálném Android zařízení a s Unity srovnáním, pak rozhodnutí Go, Pivot, nebo Stop. Nejbližší praktické kroky z reportů: reálný telefon, Apple tým pro TestFlight, skutečné MAX a Firebase přes Gradle.

Detail plánu: `ROADMAP.md` a `RESEARCH.md` (kapitoly 5 a 11).
