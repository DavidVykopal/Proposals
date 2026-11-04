# NoxEngine + Warcamp
Proof of concept vlastního enginu a jiného workflow podle Czodeho. Warcamp ukazuje rychlou strategii s PvP a naší metou.
!! 174 | příkazů, kterými agent ovládá engine
!! 71 | commitů mezi 2. a 3. 11. 2026
!! 4 | skiny z jednoho kódu, včetně mecha
!! 0 | desynců v PvP, web proti nativu
---
## Vlastní engine jde postavit, prototyp běží
- Editor ve stylu Unity, **Warcamp** na webu, jako Android APK a v iOS simulátoru
- Online **PvP na Cloudflare**: ranked, žebříček, reconnect, ghost zápasy
- Stejný vstup dá bitově stejný zápas, test prošel na macOS i na webu
- **50 000 jednotek** při 219 fps na Apple M5
- Licence 0 USD, ale úspora licencí sama sázku **neospravedlňuje**
→ `SHRNUTI_NOXENGINE.md`
---
## Czodeho workflow: agent pracuje, člověk rozhoduje
Engine je postavený pro AI agenty jako hlavní uživatele, ne jako doplněk k editoru.
- **Jedna ovládací plocha**: agent umí v enginu vše, co člověk v editoru
- **Obsah jako data**: balanc, karty a arény v JSON, změna bez buildu
- **Simulátor**: 200 zápasů botů ověří balanc, agent ho ladí sám
- **Reskin je složka**: Pirates a Undead vznikly bez změny kódu
- **Gauntlet Loop**: kvalitu soudí čerstvý agent kritik proti referenci
→ `GAUNTLET_LOOP.md`
---
## Warcamp má PvP a metu, jakou stavíme v Mecha Fortress
- Zápas do 5 minut: zlato, **1 ze 3 karet**, jednotky bojují samy
- Trofeje, 3 arény, žebříček top 50, truhly, levely jednotek
- Obchod za gemy, skiny včetně **mecha**, testovací rewarded reklama x2
- **City V2** prototyp: zápasy dávají suroviny, město bonusy do bitvy
- Bez soupeře online hraje hráč proti **ghostu** skutečného hráče, jinak bot
→ `GDD_WARCAMP.md`
---
## Ověřené je technické jádro, ne byznysová čísla
| Ověřené | Neověřené |
|---|---|
| Ovládání agenty, smoke test 22/22 | Rychlost proti Unity |
| PvP web proti nativu bez desyncu | Výkon na reálném Androidu |
| Android APK 5,9 MB, iOS simulátor | iOS zařízení a TestFlight |
| Most na SDK se stubem | Skutečné MAX a Firebase |
→ `SHRNUTI_NOXENGINE.md`
---
## Dva kill hlasy znamenají stop, zatím nic neprošlo
| Gate | Termín | Stav k 4. 11. |
|---|---|---|
| K1 150 jednotek, 60 fps na Androidu | sprint 2 | neměřeno |
| K2 agent bez lidské úpravy kódu | sprint 2 | částečně doloženo |
| K3 nejvýš 1,5x čas Unity | sprint 2 | nezačato |
| K4 MAX a Firebase z Rustu | sprint 3 | jen mock |
| K5, K6 velikost a iPhone 12 | sprint 3 a 4 | APK 5,9 MB, simulátor |
→ `RESEARCH.md`
---
## Co je potřeba rozhodnout
- Schválit **časově omezenou sázku**: 2 inženýři a agenti, zhruba 6 sprintů
- Určit vlastníka, otázka: převezme ho **Czode**, autor workflow?
- Uvolnit **Unity vývojáře** na srovnání s Unity (K3) ve sprintu 1
- Mecha Fortress, NoxFort a Hexapolis **zůstávají v Unity**
- Po sprintu 2 (K1 až K3) rozhodnout: **Go, Pivot, nebo Stop**
→ `RESEARCH.md`
