## Shrnutí
Produkci 2027 stavíme na třech větvích a sdíleném základu (City V2, SharedGameBackend). MF-branch vydá 3 reskiny s tématy z CPI testů. Hexapolis ruší HexFort a do původní hry přidá PvP, City V2 a UGC, nový Hexapolis 2 vznikne jen po gate. Strategická větev cílí na hry mezi Hexem a MF s PvP od prvního dne.

Cíl roku je aspoň 5 nových titulů v soft launchi: 3 reskiny, strategický titul #1 a titul #5. Klasicky by na to chyběla víc než trojnásobná kapacita grafiky a dvojnásobná kódu. Plán to řeší reskinovou linkou, sdíleným City V2 a SGB, AI pipeline, outsourcingem grafiky a výrobou ve dvou linkách po sobě.

## Výhody
- **PvP a sociální vrstva** otevírají monetizaci hráčů, kteří utrácejí, aby předehnali ostatní. Dnes je nemonetizujeme vůbec.
- **Nižší riziko:** všechny tituly stojí na ověřeném MF receptu, City V2 a SGB, ne na neověřeném gameplayi.
- **Obrana proti levným kopiím:** PvE hru AI snadno zkopíruje, komunitu, klany a živý svět ne.
- **City V2 a SGB se platí jednou** a používají je všechny hry včetně reskinů a strategické větve.
- **Témata vybírají data:** CPI pipeline s 1 až 2 testy měsíčně místo odhadu.

## Nevýhody
- Do 11. 12. běží souběžně City V2, PvP, UGC, SGB, CPI a live ops Q4 na stejném týmu.
- HexFort končí a Hexapolis 2 se odkládá nejméně do rozhodnutí v únoru až březnu 2027.
- Vlastníci City V2, PvP v Hexu, strategické větve a reskinové linky zatím nejsou určení.
- Titul #5 se při skluzu mění na reskin, druhý unikátní strategický titul pak v 2027 nebude.
- Plán 5 titulů potřebuje **outsourcing grafiky** zhruba 1 úvazek na rok, rozpočet zatím není.

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| Kapacita na konci roku nestačí na SGB, PvP, City V2 a UGC zároveň | vysoká | vysoká | volná kapacita kodérů z konce roku, práce přes agenty, vše za RC flagy, rozhodnutí K3 a K4 v plánu sprintu |
| Reálné PvP na malé hráčské základně zabije retenci (čekání, nevyrovnané zápasy) | střední | vysoká | fake PvP na launchi, onboarding vždy proti botům, reálné PvP postupně přes remote config |
| Gate Hexapolis 2 nemá dohodnutá čísla a rozhodnutí se protáhne | střední | střední | cílové hodnoty schválit na poradě vedení (NOVE-19) před lednovým releasem |
| CPI testy nedají jasného vítěze tématu a reskin #1 se posune | střední | střední | 4 varianty v testu A do 15. 12., další testy každý měsíc |
| Úspory z AI (40 % art, 30 % kód) se nepotvrdí a pět titulů nestihneme | střední | vysoká | kontrolní bod konec března na reskinu #1, záloha reskin #4 místo titulu #5, outsourcing navýšit |
| NoxEngine neprokáže rychlost ani funkční mobilní SDK | střední | nízká | letos jen experiment, kill gates (CE13), plán 5 titulů stojí na Unity |

## Co nám to přinese
- SGB v produkčním buildu Mecha Fortress nejpozději 11. 12. 2026, ostatní hry ho přebírají odtud.
- PvP a City V2 v původním Hexapolisu u hráčů v lednu 2027, UGC v únoru 2027.
- Témata reskinů z CPI testu A do 15. 12. 2026, start reskinu #1 v lednu, soft launch v březnu 2027.
- Rozhodnutí o Hexapolis 2 v únoru až březnu 2027 na datech z živé hry.
- Aspoň 5 nových titulů v soft launchi 2027 (III, VI, IX, X, XII): 3 reskiny a 2 strategické tituly, Hexapolis 2 jen po gate.

→ `STRATEGIE_PRODUKCE.md`
