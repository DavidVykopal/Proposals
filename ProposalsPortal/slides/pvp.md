# Obnova Hexu a PvP
HexFort rušíme a práci vracíme do původního Hexapolisu. Tam ověříme PvP, City V2 a UGC jako celek.
!! I 2027 | PvP a City V2 k hráčům
!! 2 | PvP segmenty: Skill only a All-out-power
!! 5 | lig v All-out-power
!! II až III | rozhodnutí o novém Hexapolis 2
---
## Nejdřív ověřit v Hexu, pak nový Hexapolis 2
- **HexFort jako Hexapolis 2 rušíme**, bez ověření je to moc velké riziko
- V původním Hexu zkusíme **PvP, mapu (City V2) a UGC**
- Rozhoduje, jestli funguje **celek**, ne jedna featura
- Když ano: design **hex gameplaye na MF metě** a nový projekt Hexapolis 2
→ `KONCEPT_OBNOVA_HEXU.md`
---
## PvP má dva segmenty pro dva typy hráčů
| | Skill only | All-out-power |
|---|---|---|
| Rozhoduje | jen jak kdo hraje | i síla jednotek a talentů |
| Setup | stejný pro všechny, volba presetu národa | vlastní jednotky, talenty, meta staty |
| Ligy | jeden žebříček | 5 lig, postup top 10 % |
→ `DESIGN_HEX_PVP.md`
---
## Na start Quick game, později Long game
- Oba hráči jsou ve hře a čekají na své tahy
- **Speed:** méně času na tah a méně tahů
- **Normal:** standardní limit a počet tahů
- **Long game** ve stylu online šachů přijde později
- Prvních pár zápasů a fallback při čekání proti botovi
→ `DESIGN_HEX_PVP.md`
---
## Žebříčky denně, týdně, měsíčně, s odměnami a sériemi
- Skóre z výhry, prohry a celkového výkonu, vedle toho **ELO**
- Žebříčky v obou segmentech na **SharedGameBackendu**
- Odměny podle pořadí, achievementy za **top 10, top 3, 2. místo, výhru**
- **Série:** top 10 dva týdny po sobě a dál
- Top 10 a achievementy jen z reálných zápasů
→ `DESIGN_HEX_PVP.md`
---
## PvP a město se navzájem krmí
- PvP a žebříčky dávají **suroviny do města**
- Budovy ve městě zvyšují **meta staty** pro All-out-power
- Skill only meta ignoruje, zůstává čistý souboj
- UGC mapy přijdou v únoru jako třetí díl ověření
→ `KONCEPT_OBNOVA_HEXU.md`
---
## Co je potřeba rozhodnout
- **Vlastníci** PvP, City V2 a UGC a kapacita na XI a XII
- Presety národů pro Skill only, ELO per segment nebo i per režim
- Navázat na **prototyp PvP z května**, nebo začít znovu
- Cílové hodnoty gate potvrdit s Jirkou
- Úkoly v NoxHub projektu **Hex 2** uzavřít nebo přesunout do Hexu
→ `KONCEPT_OBNOVA_HEXU.md`
