# Koncept: strategická větev her

> **Stav:** koncept, 1. 11. 2026, doplněno 4. 11. 2026 (postupný náběh PvP). Zdroj: voice note Davida. Nadřazený dokument: `STRATEGIE_PRODUKCE.md`. NoxHub: NOVE-10.
> **Pro AI agenty:** při návrhu konceptu drž pevné body (sekce 2) a měň jen gameplay (sekce 3). Nový koncept zapiš podle šablony v sekci 6.

## 1. Proč

- Hexapolis je pro široký trh moc složitý, Mecha Fortress moc jednoduchý. Strategická větev je prostor mezi nimi.
- **Monetizační mezera:** celé portfolio jsou dnes PvE hry se slabou sociální vrstvou. Vůbec nemonetizujeme hráče, kteří chtějí předhánět jiné lidi v tom, kdo víc utratí (žebříčky, klany, globální mapa). Ve hře bez soupeřů má jejich útrata strop. PvP a silné sociálno od prvního dne tenhle segment otevírají, proto je to pevný bod větve, ne volitelná feature.
- **Snížení rizika:** offline PvE hru si díky AI levně udělá čím dál víc lidí, konkurence i samotní hráči. Hromadu hráčů, komunitu a živý svět levně zkopírovat nejde. Proto stavíme hry, jejichž hodnota roste s počtem hráčů.
- Na trhu jsou dnes i historicky silné hry tohoto typu (Clash Royale, Mechabellum, nová vlna od Voodoo).
- Tým to baví. Na Game Jamu chce řada lidí dělat Mechabellum-style hry.
- Využijeme, co už máme, takže prototyp i titul jsou levnější než nová hra od nuly.

## 2. Pevné body (stejné pro všechny tituly větve)

| Vrstva | Zdroj |
|---|---|
| Meta progrese | MF-branch meta |
| Město mezi zápasy | City V2 (`DESIGN_CITY_V2.md`) |
| Backend, Nox ID, klany, leaderboardy, promo kódy | SharedGameBackend |
| Sociální vrstva | SGB + City V2 (návštěvy měst, armády, globální mapa) |

PvP je **v designu od prvního dne**, ale na launchi je fake (boti a ghost armády), viz sekce 3, PvP.

## 3. Volný prostor: gameplay

**Charakter zápasu:**
- zápas běží na kola nebo vlny,
- v každém kole hráč udělá několik rozhodnutí (stavba, výběr jednotek, itemy, upgrady),
- pak chvíli sleduje nebo čeká na výsledek,
- celkově víc idle než Mecha Fortress (méně pozornosti mezi zápasy), ale s většími rozhodnutími.

**Reference:**

| Reference | Co si bereme |
|---|---|
| Mechabellum | kola: nákup a rozmístění jednotek, pak automatický boj; PvP i PvE |
| Clash Royale | krátké PvP zápasy, balíček, žebříček |
| Voodoo base + minion battlery | vlastní základna produkuje vojáky, ti bojují, hráč vylepšuje a opakuje |
| Goblin Gold Miners | jednoduchá ekonomika, továrny, produkce jednotek |
| Hexapolis idle spin-off | hexová strategie, ale víc idle; patří sem, ne do Hex 2 |

**PvP:** přirozeně, ne na sílu. Kola s automatickým bojem jdou snadno async (souboj proti uložené armádě/městu jiného hráče) i live.

**Postupný náběh PvP (best practices Voodoo):**
- **Launch:** fake PvP. Soupeři jsou boti nebo uložené armády jiných hráčů (ghost zápasy), prezentovaní jako hráči. Bez fronty, s řízenou obtížností a win rate.
- **Onboarding vždy fake,** i v produkční hře: prvních 3 až 5 zápasů *(návrh)* proti botům nastaveným tak, aby hráč pochopil hru a vyhrál.
- **Reálné PvP až postupně:** podle velikosti hráčské základny a postupu hráče (vyšší ligy, dokončený onboarding). Když není soupeř včas, fallback na ghost armádu nebo bota.
- Všechny prahy za remote config, ladí se A/B testy.
- Pro auto-battler formát je to přirozené: ghost zápas proti uložené armádě vypadá stejně jako live zápas.

## 4. Cíl 2027

- **Aspoň 2 unikátní tituly** (prototyp → greenlight → výroba).
- Výběr tematiky přes CPI testy, směr B (`STRATEGIE_PRODUKCE.md`, sekce CPI, NoxHub CPI-12).

## 5. Proces od nápadu po greenlight

1. **Sběr konceptů:** Game Jam, R&D, trh (AppMagic trendy). Každý koncept podle šablony níže.
2. **CPI test tematiky:** stejné základní assety převedené do více tematik.
3. **Prototyp:** nejvýš 2 sprinty na koncept (pravidlo V10), pak rozhodnutí pokračovat / stop.
   Prototypy zkoušíme i na vlastním enginu **NoxEngine 0.1** (Rust, obsah v JSON s hot reloadem, maximum práce dělají agenti). První je **Warcamp**, NoxHub CODE-217. Pracovní směr, rozhodnutí go / no-go padne v CE13.
4. **Greenlight** na poradě vedení podle metrik z prototypu a CPI.

## 6. Šablona konceptu (1 strana)

```
Název:
Reference (1 až 3 hry):
Jedna věta o zápase:
Co hráč rozhoduje v kole:
Jak vypadá PvE / PvP (fake PvP na launchi, kdy reálné):
Napojení na City V2 (co město dává do zápasu, co zápas dává městu):
Tematika (kandidáti do CPI):
Riziko č. 1:
Co ověří prototyp za 2 sprinty:
```

## 7. Otevřené otázky

1. Kdo větev vlastní (segment, lead)?
2. Kolik konceptů jde do prototypu v Q1 2027?
3. Jméno větve (pracovně "strategická větev").
