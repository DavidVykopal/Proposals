# Jak portál funguje

Portál Návrhy 2027 je jedno místo pro všechny návrhy vedení NOXGAMES na konec roku 2026: delegační plán, produkční strategii 2027, design PvP a City V2, NoxEngine, výstup externích designérů a CPI testy. Každý návrh si přečtete, rychle projdete v přehledu, okomentujete konkrétní místo a zeptáte se asistenta. Totéž umí i váš vlastní AI asistent (Claude Code, Claude Desktop, Cursor) přes MCP.

Tento průvodce je psaný pro lidi i pro AI. Když si něco nastavujete s pomocí Clauda, stačí mu říct, ať si přečte tuto kapitolu.

## Přihlášení a kdo se dívá

- Vstup chrání jedno společné heslo pro celé vedení. Přihlášení vydrží 30 dní na daném zařízení.
- Po přihlášení vyberete, **kdo se dívá** (Jirka, DJ, Kuba, Mirek, Peko, David, nebo napíšete jiné jméno). Pod tímto jménem se ukládají poznámky a vidí se, kdo co četl.
- Jméno změníte kdykoli vpravo nahoře klikem na barevný štítek se jménem.
- Jméno není heslo. Portál věří, že se každý přihlásí sám za sebe.

## Jak je portál uspořádaný

- **Obsah** (úvodní stránka) ukazuje kapitoly 00 až 07. U každé vidíte počet dokumentů, počet otevřených poznámek a štítek **nové**, pokud se od vaší poslední návštěvy něco změnilo.
- Číslované záložky na pravém okraji přepínají kapitoly odkudkoli. Na telefonu jsou jako pruh pod horní lištou.
- Každá kapitola začíná shrnutím a **rychlým přehledem**: pár snímků s tím nejdůležitějším, na tři minuty. Pod ním jsou **podklady**, tedy plné dokumenty a prezentace.
- Dokumenty se navzájem odkazují. Když jeden zmiňuje druhý, zmínka je proklik.
- U každého dokumentu je datum poslední úpravy a kdo z vedení ho už četl.

## Čtení a prezentování

- **Rychlý přehled**: šipky vlevo a vpravo, tečky s čísly snímků, tlačítko **Promítat** pro celou obrazovku. Na telefonu se dá listovat tahem prstem.
- **Prezentovat** (u dokumentu, nebo klávesa P): schová poznámky a ovládání, zvětší písmo, šipky skáčou po kapitolách, Esc ukončí. Hodí se na sdílenou obrazovku na poradě.
- **Obsah dokumentu** rozbalí seznam kapitol dlouhého dokumentu.
- U prezentací (HTML) je tlačítko **Celá obrazovka** a **Otevřít samostatně**.
- Vpravo nahoře přepnete světlý a tmavý režim.

## Poznámky ke konkrétnímu místu

- Najeďte myší na odstavec, řádek tabulky nebo nadpis. Vlevo se objeví dvě ikony: **přidat poznámku** a **odkaz na toto místo**. Na telefonu na odstavec klepněte.
- Poznámka se ukáže na okraji vedle místa, ke kterému patří. Ostatní na ni mohou **odpovědět**, a kdo považuje věc za vyřízenou, dá **Vyřešit**. Vyřešená vlákna jsou skrytá, zobrazíte je zaškrtnutím „vyřešené“.
- Svou poznámku můžete **upravit** nebo **smazat**. Smazat nejde vlákno, na které už někdo odpověděl, takové se jen vyřeší.
- **Poznámka k celému dokumentu** je tlačítko nad textem, když se poznámka netýká jednoho místa.
- U prezentací zapněte **Komentovat části** a klikněte na místo v prezentaci, ke kterému chcete poznámku.
- Stránka **Poznámky** v horní liště ukazuje všechny poznámky napříč podklady, filtr podle stavu a autora. Klik na citaci vás přenese přímo na místo v textu.
- Když David text upraví, poznámky k přepsanému odstavci se přesunou do části „Text se mezitím změnil“ i s původní citací, takže se neztratí.
- Nové poznámky od ostatních se objeví samy do půl minuty, stránku není potřeba obnovovat.

## Asistent

- Tlačítko **Zeptat se** v horní liště (nebo klávesa /) otevře asistenta. Odpovídá česky a jen z podkladů v portálu, u odpovědí uvádí odkazy přímo na místo, odkud informace má.
- V dokumentu si vyberete rozsah: **Tento dokument** (otázky typu „co je tady nerozhodnuté“) nebo **Všechny podklady**.
- Umí hledat napříč dokumenty, porovnávat, shrnovat, vypsat poznámky a **počítat** (každé dopočítané číslo počítá kalkulačkou, ne odhadem).
- Neumí měnit dokumenty ani psát poznámky. Jmenovité platy v portálu nejsou, takže na ně neodpoví.
- Rozhovor si portál pamatuje, dokud nezavřete prohlížeč. **Nový dotaz** začne od čistého stolu.

## Vlastní AI asistent přes MCP

Váš vlastní Claude (nebo jiný klient s podporou MCP) se může k portálu připojit. Pak umí v podkladech hledat, číst je, vypsat poznámky a psát poznámky a odpovědi **vaším jménem**.

1. Přihlaste se a vyberte své jméno.
2. Otevřete **Nastavení** (ozubené kolečko vpravo nahoře).
3. V části Osobní tokeny pro MCP napište název (například „MacBook“) a dejte **Vytvořit token**.
4. Token se ukáže jen jednou. Zkopírujte rovnou připravený příkaz.
5. **Claude Code**: vložte příkaz do terminálu. Vypadá takto:

```
claude mcp add --transport http noxgames-navrhy https://noxgames-proposals.studio-0b0.workers.dev/mcp --header "Authorization: Bearer npt_..."
```

6. **Claude Desktop, Cursor a další**: přidejte vzdálený MCP server s adresou `https://noxgames-proposals.studio-0b0.workers.dev/mcp` a hlavičkou `Authorization: Bearer npt_...`.
7. Vyzkoušejte: „Najdi v Návrzích 2027, co je potřeba rozhodnout na příští poradě.“

Token patří jménu, pod kterým jste ho vytvořili. Kdo token má, píše poznámky vaším jménem, takže ho nesdílejte. Když ho ztratíte nebo už nepotřebujete, v Nastavení ho zrušte. V Nastavení vidíte i to, kdy byl token naposledy použit.

### Nástroje MCP serveru

| Nástroj | Co dělá |
|---|---|
| list_documents | seznam kapitol a dokumentů s id, odkazy a počtem otevřených poznámek |
| search_documents | hledání v dokumentech i rychlých přehledech, vrací úryvek, kotvu a odkaz |
| read_document | celý text dokumentu, každý blok začíná kotvou v hranatých závorkách |
| list_comments | vlákna poznámek s id, citací, autory a stavem |
| add_comment | nová poznámka vaším jménem, ke kotvě, k citaci nebo k celému dokumentu |
| reply_comment | odpověď do vlákna vaším jménem |
| resolve_comment | vyřešit nebo znovu otevřít vlákno |
| calculate | přesný výpočet výrazu |

### Pokyny pro AI agenty

- Začni nástrojem list_documents, pak hledej přes search_documents krátkými českými klíčovými slovy (diakritika je volitelná, funguje i začátek slova). Když nic nenajdeš, zkus synonyma.
- Dokument čti přes read_document. Kotva v hranatých závorkách (například `[p-1flvls4]`) identifikuje odstavec, řádek tabulky nebo nadpis. Odkaz na místo je adresa dokumentu + `#b=<kotva>`.
- Rychlý přehled kapitoly má id `prehled-<kapitola>` a kotvy `s1`, `s2`… Poznámky se k němu nepíšou, piš je k podkladovému dokumentu.
- Poznámky jsou vidět celému vedení a jsou podepsané jménem majitele tokenu. Piš je česky, věcně, bez pozdravů a úvodních frází, jedna poznámka = jedna věc. Než napíšeš novou, podívej se přes list_comments, jestli podobné vlákno už neexistuje, a raději odpověz do něj.
- Novější dokument nebo zápis z porady má přednost před starším. Když se zdroje rozcházejí, napiš to.
- Neodhaduj jmenovité platy ani čísla, která v podkladech nejsou. Dopočítaná čísla počítej nástrojem calculate.

## Jak se podklady mění

- Zdrojem pravdy jsou Davidovy dokumenty v repozitáři. Portál se z nich sestaví při každém nasazení, takže tu je vždy poslední verze.
- Poznámky z portálu si David stáhne jedním příkazem do souboru, zapracuje je do dokumentů a vlákna pak označí jako vyřešená.
- Kapitola, která ještě nemá podklady, je označená „připravuje se“.

## Časté otázky

- **Nevidím svoji poznámku u odstavce.** Text se mohl mezitím změnit, podívejte se dole na okraji do „Text se mezitím změnil“, nebo na stránku Poznámky.
- **Asistent říká, že něco v podkladech není.** Nejspíš to opravdu chybí. Napište k dokumentu poznámku, ať se to doplní.
- **Odhlásilo mě to.** Heslo se mohlo změnit, nebo vypršelo přihlášení po 30 dnech. Přihlaste se znovu, jméno zůstane.
- **Můj Claude hlásí 401.** Token je zrušený nebo špatně zkopírovaný. Vytvořte v Nastavení nový.
