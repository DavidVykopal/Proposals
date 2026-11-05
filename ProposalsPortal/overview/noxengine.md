## Shrnutí
NoxEngine 0.2 je proof of concept vlastního enginu v Rustu postaveného tak, aby ho celý ovládali AI agenti. Nápad přinesl Czode. Běží editor ve stylu Unity, hra Warcamp na webu, jako Android APK a v iOS simulátoru, online PvP na Cloudflare. Warcamp ukazuje strategickou hru s PvP a metou, jakou stavíme v Mecha Fortress.

Rozhodnuto 6. 11.: letos je NoxEngine čistě experiment, dělají na něm David a Čoud a z plánu kvůli němu nic nevypadává. Rozšiřovat a testovat ho jde i během GameJamu 14. až 18. 12. O případné větší investici (podle `RESEARCH.md` 2 inženýři a agenti na zhruba 6 sprintů) se rozhodne později, kill gates jsou kritéria pro to rozhodnutí. Mecha Fortress, NoxFort a Hexapolis zůstávají v Unity. Žádná ze sedmi gates zatím formálně neprošla.

## Výhody
- **Agent umí vše, co člověk:** 174 příkazů přes MCP, včetně klikání v UI hry a screenshotů
- **Obsah jako data:** balanc, karty a arény v JSON s hot reloadem, změna bez buildu
- **Simulátor bitev:** 200 zápasů botů během chvíle, agent ladí balanc sám
- **Reskin je složka:** Pirates a Undead vznikly bez změny kódu, levnější CPI testy témat
- **Licence 0 USD** proti Unity Pro, při 16 lidech nejvýš zhruba 37 tisíc USD ročně (`RESEARCH.md` počítá 76 tisíc při 33 místech)

## Nevýhody
- Pro Rust neexistují oficiální SDK pro MAX, Firebase, IAP ani Xsolla, nutné nativní shelly v Kotlinu a Swiftu
- Případná větší investice by vázala 2 inženýry na zhruba 6 sprintů a potom zhruba 1 FTE na údržbu (letos jen experiment)
- Lidská iterace v Rustu je pomalá a trh vývojářů malý
- Agent-first sám o sobě není unikát: Unity má oficiální MCP, Unreal 5.8 experimentální
- Úspora licencí podle `RESEARCH.md` sama sázku neospravedlňuje

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| Workflow není rychlejší než Unity se stejným agentem | střední | vysoká | Gate K3 před rozhodnutím o větší investici: nejvýš 1,5x čas Unity 6 + Unity MCP, jinak stop |
| Výkon na reálném Androidu nestačí (měřeno jen na emulátoru) | střední | vysoká | Gate K1: p95 do 16,7 ms se 150 jednotkami na referenčním telefonu |
| Napojení MAX a Firebase z Rustu nefunguje | střední | vysoká | Gate K4 do konce sprintu 3, dnes jen stub a mock |
| Bus factor: za vším stojí jeden člověk s agenty | vysoká | vysoká | Na experimentu jsou od 6. 11. David a Čoud, buildy mají zvládnout aspoň 2 lidé před rozhodnutím o větší investici |
| Rozsah editoru přeroste práci na hře | střední | střední | Gate K7: editor nad 35 % času před K4 znamená zmrazit práci na editoru |
| Ranked PvP jde farmit, server výsledek neověřuje | vysoká | nízká | Serverové ověření a rate limit před vydáním |

## Co nám to přinese
- Experiment bez dopadu na plán, rozšířený a otestovaný i během GameJamu
- Pozdější rozhodnutí o větší investici (Go, Pivot, nebo Stop) na základě měření, ne dojmů (K1 až K3)
- Při úspěchu a větší investici první soft-launchovatelná hra zhruba po 6 sprintech, Warcamp ve strategické větvi
- Ověřený agent-first workflow, který lze srovnat s Unity číslem
- Při stopu nic neztratíme na hrách: Warcamp (data a design) přejde do Godot 4.7 nebo Unity 6.3 LTS a NoxEngine zůstane interní nástroj na headless simulace a playables

→ `SHRNUTI_NOXENGINE.md`
