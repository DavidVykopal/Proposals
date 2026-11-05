## Shrnutí
NoxEngine 0.2 je proof of concept vlastního enginu v Rustu postaveného tak, aby ho celý ovládali AI agenti. Nápad přinesl Czode. Běží editor ve stylu Unity, hra Warcamp na webu, jako Android APK a v iOS simulátoru, online PvP na Cloudflare. Warcamp ukazuje strategickou hru s PvP a metou, jakou stavíme v Mecha Fortress.

Navrhujeme časově omezenou sázku podle `RESEARCH.md`: 2 inženýři a agenti, zhruba 6 sprintů do první soft-launchovatelné hry, kill gates po sprintu 2, 3 a 4. Mecha Fortress, NoxFort a Hexapolis zůstávají v Unity. Žádná ze sedmi gates zatím formálně neprošla.

## Výhody
- **Agent umí vše, co člověk:** 174 příkazů přes MCP, včetně klikání v UI hry a screenshotů
- **Obsah jako data:** balanc, karty a arény v JSON s hot reloadem, změna bez buildu
- **Simulátor bitev:** 200 zápasů botů během chvíle, agent ladí balanc sám
- **Reskin je složka:** Pirates a Undead vznikly bez změny kódu, levnější CPI testy témat
- **Licence 0 USD** proti zhruba 76 tisícům USD ročně za Unity Pro při 33 místech

## Nevýhody
- Pro Rust neexistují oficiální SDK pro MAX, Firebase, IAP ani Xsolla, nutné nativní shelly v Kotlinu a Swiftu
- Váže 2 inženýry na zhruba 6 sprintů a potom zhruba 1 FTE na údržbu
- Lidská iterace v Rustu je pomalá a trh vývojářů malý
- Agent-first sám o sobě není unikát: Unity má oficiální MCP, Unreal 5.8 experimentální
- Úspora licencí podle `RESEARCH.md` sama sázku neospravedlňuje

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| Workflow není rychlejší než Unity se stejným agentem | střední | vysoká | Gate K3 ve sprintu 1 až 2: nejvýš 1,5x čas Unity 6 + Unity MCP, jinak stop |
| Výkon na reálném Androidu nestačí (měřeno jen na emulátoru) | střední | vysoká | Gate K1: p95 do 16,7 ms se 150 jednotkami na referenčním telefonu |
| Napojení MAX a Firebase z Rustu nefunguje | střední | vysoká | Gate K4 do konce sprintu 3, dnes jen stub a mock |
| Bus factor: za vším stojí jeden člověk s agenty | vysoká | vysoká | Do konce sprintu 3 buildy zvládnou aspoň 2 lidé |
| Rozsah editoru přeroste práci na hře | střední | střední | Gate K7: editor nad 35 % času před K4 je kill hlas |
| Ranked PvP jde farmit, server výsledek neověřuje | vysoká | nízká | Serverové ověření a rate limit před vydáním |

## Co nám to přinese
- Rozhodnutí Go, Pivot, nebo Stop po sprintu 2 na základě měření, ne dojmů (K1 až K3)
- Při úspěchu první soft-launchovatelná hra zhruba po 6 sprintech, Warcamp ve strategické větvi
- Ověřený agent-first workflow, který lze srovnat s Unity číslem
- Při stopu nic neztratíme na hrách: Warcamp (data a design) přejde do Godot 4.7 nebo Unity 6.3 LTS a NoxEngine zůstane interní nástroj na headless simulace a playables

→ `SHRNUTI_NOXENGINE.md`
