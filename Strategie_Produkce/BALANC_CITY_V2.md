# City V2: první nahození čísel (verze 1)

> **Stav:** první nahození, 5. 11. 2026. Všechna čísla jsou k ladění na stagingu Mecha Fortress (MF), pak se přenesou do Hexapolisu. Design a rozsah: `DESIGN_CITY_V2.md`.
> **Pro AI agenty:** tento soubor je číselný doprovod k `DESIGN_CITY_V2.md`. Pravidla a rozsah určuje design dokument; když se liší, platí design. Čísla tady jsou vygenerovaná ze vzorců v kapitole 10, při změně parametrů se přepočítají všechny tabulky (žádné ruční úpravy jednotlivých buněk). Věci označené *(předpoklad)* nejsou ověřené na datech.

## 1. Shrnutí

- **Radnice 1 až 10** ve verzi 1. Ostatní budovy mají max level podle Radnice: produkce, Sklad, Tržiště a Svatyně = level Radnice (max 10), Kasárna, Kovárna a Akademie = 2× level Radnice (max 20).
- **Tempo aktivního hráče** (6 zápasů denně, 2 stavitelé, 3 a více návštěv města denně): Radnice 4 první den, Radnice 6 do konce prvního týdne, Radnice 8 kolem 21. dne, **Radnice 10 kolem 50. dne**, **vše na maximu verze 1 kolem 68. dne**. To kryje leden a únor 2027, než přijde V2 (Radnice 11 a víc).
- **Rytmus session:** sběr produkce 2 až 3× denně (kapacita budovy 10 h produkce), stavitelé se od Radnice 6 přenastavují 1 až 2× denně, první den časovače do 45 min.
- **Ekonomika:** pasivní produkce kryje **asi 1/3** útraty (31 až 38 % od Radnice 4), zbytek jde ze zápasů, odměn a questů. Odpovídá zásadě z designu: hlavní příjem je ze hraní.
- **Síla z města:** na maximu verze 1 dává město +20 % HP a +20 % útok, tedy **×1,44 efektivní síly** (HP × útok), plus 6 talentových bodů, 2 sloty, +20 % XP a +20 % odměn. Cíl: město tvoří **15 až 25 % celkové síly** hráče na D30 *(předpoklad, ověřit telemetrií)*.
- **Monetizace:** zrychlení za gemy (prvních 5 min zdarma), stavitel #3 za 300 gemů, #4 za 600 gemů, balíčky surovin. Zrychlit celou verzi 1 stojí asi **15 100 gemů** (cca 250 USD při našem ceníku 60 gemů za 1 USD).
- **Celkový objem verze 1:** 2 461 hodin práce stavitelů a asi 12,1 milionu surovin.

## 2. Pilíře ekonomiky

| Pilíř | Pravidlo | Proč |
|---|---|---|
| Rychlý první den | Radnice 2 a 3 v prvních 30 min, časovače do 5 min zdarma, kapitoly questů kryjí náklady prvního dne | klon CoC a RoK: hráč musí hned vidět, že město roste |
| Křivka časovačů | jedna časová jednotka na tier Radnice, roste z 1 min (tier 1) na 34 h (tier 10), viz kapitola 10 | delší časovače = důvod se vracet a prostor pro zrychlení |
| Radnice je nejdelší stavba tieru | Radnice má váhu 3,0 (ostatní 0,8 až 1,4) | jasný cíl každého tieru, jako CoC Town Hall |
| 2 stavitelé zdarma, 3. a 4. prémiově | základní tempo je spočítané na 2 stavitele a 75 % vytížení | stavitel #3 je nejčistší nákup (CoC, RoK) |
| Produkce je doplněk | pasivní produkce kryje asi 1/3 útraty, zbytek zápasy | město tlačí hráče zpět do hry, ne naopak |
| Sklad gatuje skoky | kapacita Skladu na levelu L stačí na nejdražší jednotlivou stavbu tieru L s rezervou asi 25 % | hráč musí upgradovat Sklad, než může zvednout Radnici |
| Progres ve hře gatuje Radnici | Radnice 4 a výš vyžaduje postup ve hře (MF stage index) | hráč se vrací do gameplaye, design kap. 3.4 |
| Meta bonusy lineární a se stropem | +1 % nebo +2 % za level, stropy 20 % | čitelné, snadno se ladí přes RC, nerozbije balanc |

**Cílové tempo podle období** (aktivní hráč, 2 stavitelé):

| Období | Kde hráč je | Meta bonus Kasárna a Kovárna | Efektivní síla z města |
|---|---|---|---|
| Den 1 | Radnice 4, první produkční budovy na L3 až L4 | asi +7 % | ×1,15 |
| Den 7 | Radnice 6 | asi +11 % | ×1,23 |
| Den 14 | Radnice 7 | asi +13 % | ×1,28 |
| Den 30 | Radnice 8, blízko 9 | asi +15 % | ×1,32 |
| Den 50 | Radnice 10 | asi +18 % | ×1,39 |
| Den 68 | vše na maximu verze 1 | +20 % | ×1,44 |

Vliv počtu stavitelů (jen čas, při 75 % vytížení): 2 stavitelé 68 dní, **3 stavitelé 46 dní, 4 stavitelé 34 dní**. Příjem surovin je ale spočítaný na 2 stavitele a 6 zápasů denně, takže 3. a 4. stavitel zrychlí jen hráče, kteří hrají víc nebo kupují suroviny. To je záměr: stavitel se vyplatí aktivním a platícím hráčům.

## 3. Suroviny

| Surovina | Zdroj | Sink | Strop |
|---|---|---|---|
| **Jídlo** | Farma (od Radnice 1), zápasy, questy | Pila, Lom, Zlatý důl, Radnice, Kasárna, Tržiště, Svatyně | Radnice 1 000 + Sklad |
| **Dřevo** | Pila (od Radnice 1), zápasy, questy, odstranění stromů | Farma, Lom, Zlatý důl, Sklad, Radnice, Kasárna, Kovárna, Akademie, Tržiště | Radnice 1 000 + Sklad |
| **Kámen** | Lom (od Radnice 2), zápasy, questy, odstranění kamenů | Farma, Pila, Zlatý důl, Sklad, Radnice, Kovárna, Akademie, Svatyně | Radnice 1 000 + Sklad |
| **Zlato** | Zlatý důl (od Radnice 3), zápasy, odměny z žebříčků | Radnice, meta budovy (Kasárna, Kovárna, Akademie, Tržiště, Svatyně), dekorace | Radnice 1 000 + Sklad |
| **Gemy** (prémiová měna; v MF `HardCurrency`) | IAP, questy kapitol, překážky, achievementy | zrychlení, stavitelé #3 a #4, suroviny, prémiové dekorace | bez stropu |
| **Předměty zrychlení** 5 min, 1 h, 8 h (v MF existuje `SkipItsCurrency`) | questy, zápasy, nabídky | zrychlení staveb | bez stropu |

Pravidla stropů:
- Každá surovina má vlastní strop = **1 000 (Radnice) + kapacita Skladu** na daném levelu. Nad strop se nic nepřičte, produkce v budově čeká.
- Produkční budova drží **10 hodin produkce**, pak se zastaví, dokud hráč nesebere (klon CoC sběračů).
- Odměny ze zápasů nad strop: přebytek propadá *(návrh: ukázat hráči "sklad plný" jako výzvu k upgradu Skladu)*.
- Jedna budova Sklad pro všechny 4 suroviny (jednodušší než CoC, kde má každá surovina vlastní sklad).
- Recepty cen: každá budova platí 2 až 3 surovinami podle receptu v kapitole 10. Surovina, která ještě není odemčená (kámen před Radnicí 2, zlato před Radnicí 3), se do ceny nepočítá a její podíl se rozdělí na ostatní.

## 4. Radnice

| Level | Cena | Čas | Zrychlení (gemy) | Požadavek ve hře | Odemyká | Max level ostatních budov |
|---|---|---|---|---|---|---|
| 1 | start |  | 0 | nic | Farma, Pila, Sklad, Kasárna | produkce, Sklad, Tržiště, Svatyně 1; Kasárna, Kovárna, Akademie 2 |
| 2 | 75 jídla, 75 dřeva | 3 min | 0 | nic | Lom, Kovárna | produkce, Sklad, Tržiště, Svatyně 2; Kasárna, Kovárna, Akademie 4 |
| 3 | 180 jídla, 180 dřeva, 100 kamene | 15 min | 5 | nic | Zlatý důl, Tržiště | produkce, Sklad, Tržiště, Svatyně 3; Kasárna, Kovárna, Akademie 6 |
| 4 | 630 jídla, 630 dřeva, 360 kamene, 180 zlata | 2 h | 21 | MF stage 5 | Akademie, +1 kus Farmy, Pily, Lomu a Dolu | produkce, Sklad, Tržiště, Svatyně 4; Kasárna, Kovárna, Akademie 8 |
| 5 | 2 600 jídla, 2 600 dřeva, 1 500 kamene, 750 zlata | 9 h | 66 | MF stage 8 | Svatyně | produkce, Sklad, Tržiště, Svatyně 5; Kasárna, Kovárna, Akademie 10 |
| 6 | 7 300 jídla, 7 300 dřeva, 4 200 kamene, 2 100 zlata | 18 h | 112 | MF stage 13 | - | produkce, Sklad, Tržiště, Svatyně 6; Kasárna, Kovárna, Akademie 12 |
| 7 | 17 000 jídla, 17 000 dřeva, 9 600 kamene, 4 800 zlata | 1 d 6 h | 165 | MF stage 17 | +1 kus Farmy, Pily, Lomu a Dolu | produkce, Sklad, Tržiště, Svatyně 7; Kasárna, Kovárna, Akademie 14 |
| 8 | 50 000 jídla, 50 000 dřeva, 29 000 kamene, 14 000 zlata | 1 d 18 h | 214 | MF stage 21 | - | produkce, Sklad, Tržiště, Svatyně 8; Kasárna, Kovárna, Akademie 16 |
| 9 | 94 000 jídla, 94 000 dřeva, 54 000 kamene, 27 000 zlata | 2 d 12 h | 281 | MF stage 24 | - | produkce, Sklad, Tržiště, Svatyně 9; Kasárna, Kovárna, Akademie 18 |
| 10 | 190 000 jídla, 190 000 dřeva, 110 000 kamene, 54 000 zlata | 3 d 6 h | 344 | MF stage 27 | - | produkce, Sklad, Tržiště, Svatyně 10; Kasárna, Kovárna, Akademie 20 |

- Požadavky ve hře vychází z dnešních odemykacích stage indexů mapy MF (Zlatý důl v `MapBuilding` se odemyká na stage 8, upgrady na 13, 17, 21, 24, 27). Pro Hexapolis se při importu nahradí ekvivalentem (dobyté světy, PvP výhry), viz otevřené otázky.
- Sloupec "Zrychlení" je cena okamžitého dokončení celé stavby podle vzorce v kapitole 8.

## 5. Budovy verze 1

Sloupec "Radnice" = minimální level Radnice pro daný level budovy. Budova odemčená později (např. Akademie na Radnici 4) dožene nižší levely levně, protože cena a čas se řídí nominálním tierem levelu, ne tierem odemčení.

### 5.1 Produkce

Počet kusů od každé produkční budovy: **1 na Radnici 1 až 3, 2 od Radnice 4, 3 od Radnice 7** (Lom od Radnice 2, Zlatý důl od Radnice 3). Každý kus se staví a upgraduje zvlášť, cena a čas jsou stejné pro všechny kusy. Produkce je za hodinu na jeden kus.

#### Farma (jídlo)

| Level | Radnice | Cena | Čas | Produkce / h | Kapacita budovy |
|---|---|---|---|---|---|
| 1 | 1 | 30 dřeva | 50 s | 20 | 200 |
| 2 | 2 | 65 dřeva, 25 kamene | 3 min | 30 | 300 |
| 3 | 3 | 250 dřeva, 110 kamene | 30 min | 40 | 400 |
| 4 | 4 | 1 000 dřeva, 450 kamene | 2 h 30 min | 55 | 550 |
| 5 | 5 | 2 900 dřeva, 1 300 kamene | 5 h | 75 | 750 |
| 6 | 6 | 6 700 dřeva, 2 900 kamene | 8 h | 110 | 1 100 |
| 7 | 7 | 20 000 dřeva, 8 600 kamene | 11 h | 150 | 1 500 |
| 8 | 8 | 38 000 dřeva, 16 000 kamene | 16 h | 210 | 2 100 |
| 9 | 9 | 76 000 dřeva, 32 000 kamene | 21 h | 300 | 3 000 |
| 10 | 10 | 150 000 dřeva, 65 000 kamene | 1 d 4 h | 410 | 4 100 |
| **Celkem 1 kus** | | 294 945 dřeva, 126 385 kamene | 3 d 20 h 3 min | | |

#### Pila (dřevo)

| Level | Radnice | Cena | Čas | Produkce / h | Kapacita budovy |
|---|---|---|---|---|---|
| 1 | 1 | 30 jídla | 50 s | 20 | 200 |
| 2 | 2 | 65 jídla, 25 kamene | 3 min | 30 | 300 |
| 3 | 3 | 250 jídla, 110 kamene | 30 min | 40 | 400 |
| 4 | 4 | 1 000 jídla, 450 kamene | 2 h 30 min | 55 | 550 |
| 5 | 5 | 2 900 jídla, 1 300 kamene | 5 h | 75 | 750 |
| 6 | 6 | 6 700 jídla, 2 900 kamene | 8 h | 110 | 1 100 |
| 7 | 7 | 20 000 jídla, 8 600 kamene | 11 h | 150 | 1 500 |
| 8 | 8 | 38 000 jídla, 16 000 kamene | 16 h | 210 | 2 100 |
| 9 | 9 | 76 000 jídla, 32 000 kamene | 21 h | 300 | 3 000 |
| 10 | 10 | 150 000 jídla, 65 000 kamene | 1 d 4 h | 410 | 4 100 |
| **Celkem 1 kus** | | 294 945 jídla, 126 385 kamene | 3 d 20 h 3 min | | |

#### Lom (kámen)

| Level | Radnice | Cena | Čas | Produkce / h | Kapacita budovy |
|---|---|---|---|---|---|
| 1 | 2 | 15 jídla, 15 dřeva | 50 s | 20 | 200 |
| 2 | 2 | 45 jídla, 45 dřeva | 3 min | 30 | 300 |
| 3 | 3 | 180 jídla, 180 dřeva | 30 min | 40 | 400 |
| 4 | 4 | 750 jídla, 750 dřeva | 2 h 30 min | 55 | 550 |
| 5 | 5 | 2 100 jídla, 2 100 dřeva | 5 h | 75 | 750 |
| 6 | 6 | 4 800 jídla, 4 800 dřeva | 8 h | 110 | 1 100 |
| 7 | 7 | 14 000 jídla, 14 000 dřeva | 11 h | 150 | 1 500 |
| 8 | 8 | 27 000 jídla, 27 000 dřeva | 16 h | 210 | 2 100 |
| 9 | 9 | 54 000 jídla, 54 000 dřeva | 21 h | 300 | 3 000 |
| 10 | 10 | 110 000 jídla, 110 000 dřeva | 1 d 4 h | 410 | 4 100 |
| **Celkem 1 kus** | | 212 890 jídla, 212 890 dřeva | 3 d 20 h 3 min | | |

#### Zlatý důl (zlato)

| Level | Radnice | Cena | Čas | Produkce / h | Kapacita budovy |
|---|---|---|---|---|---|
| 1 | 3 | 10 jídla, 10 dřeva, 10 kamene | 50 s | 20 | 200 |
| 2 | 3 | 25 jídla, 35 dřeva, 25 kamene | 3 min | 30 | 300 |
| 3 | 3 | 110 jídla, 140 dřeva, 110 kamene | 30 min | 40 | 400 |
| 4 | 4 | 450 jídla, 600 dřeva, 450 kamene | 2 h 30 min | 55 | 550 |
| 5 | 5 | 1 300 jídla, 1 700 dřeva, 1 300 kamene | 5 h | 75 | 750 |
| 6 | 6 | 2 900 jídla, 3 800 dřeva, 2 900 kamene | 8 h | 110 | 1 100 |
| 7 | 7 | 8 600 jídla, 12 000 dřeva, 8 600 kamene | 11 h | 150 | 1 500 |
| 8 | 8 | 16 000 jídla, 22 000 dřeva, 16 000 kamene | 16 h | 210 | 2 100 |
| 9 | 9 | 32 000 jídla, 43 000 dřeva, 32 000 kamene | 21 h | 300 | 3 000 |
| 10 | 10 | 65 000 jídla, 86 000 dřeva, 65 000 kamene | 1 d 4 h | 410 | 4 100 |
| **Celkem 1 kus** | | 126 395 jídla, 169 285 dřeva, 126 395 kamene | 3 d 20 h 3 min | | |

### 5.2 Sklad

| Level | Radnice | Cena | Čas | Kapacita za každou surovinu (Sklad) | Celkem s Radnicí |
|---|---|---|---|---|---|
| 1 | 1 | 50 dřeva | 1 min | 500 | 1 500 |
| 2 | 2 | 75 dřeva, 75 kamene | 5 min | 650 | 1 650 |
| 3 | 3 | 300 dřeva, 300 kamene | 45 min | 840 | 1 840 |
| 4 | 4 | 1 200 dřeva, 1 200 kamene | 3 h | 2 200 | 3 200 |
| 5 | 5 | 3 500 dřeva, 3 500 kamene | 6 h | 8 100 | 9 100 |
| 6 | 6 | 8 000 dřeva, 8 000 kamene | 10 h | 20 000 | 21 000 |
| 7 | 7 | 24 000 dřeva, 24 000 kamene | 14 h | 61 000 | 62 000 |
| 8 | 8 | 45 000 dřeva, 45 000 kamene | 20 h | 120 000 | 121 000 |
| 9 | 9 | 90 000 dřeva, 90 000 kamene | 1 d 2 h | 240 000 | 241 000 |
| 10 | 10 | 180 000 dřeva, 180 000 kamene | 1 d 10 h | 310 000 | 311 000 |
| **Celkem 1 kus** | | 352 125 dřeva, 352 075 kamene | 4 d 17 h 51 min | | |

### 5.3 Chata stavitele

Chaty se neupgradují, každá chata = jeden stavitel = jedna souběžná stavba (klon CoC Builder's Hut).

| Stavitel | Jak ho hráč získá | Cena |
|---|---|---|
| #1 | start | zdarma |
| #2 | start (dokončení prvního kroku tutoriálu) | zdarma |
| #3 | gemy, nebo startovní nabídka | 300 gemů, nebo nabídka 4,99 USD (stavitel + 180 gemů + suroviny na 1 den) |
| #4 | gemy, nebo nabídka | 600 gemů, nebo nabídka 9,99 USD |

Stavby do 5 minut se dokončují zdarma (tlačítko "dokončit"), takže první hodiny neblokují stavitele.

### 5.4 Meta budovy

Bonusy se posílají hostitelské hře jako modifikátory na start zápasu (`ICityModifierSource`, design kap. 5). Hodnoty jsou kumulativní pro daný level, ne přírůstek. Stropy: HP +20 %, útok +20 %, XP +20 %, odměny +20 %, 6 talentových bodů a 2 sloty. **PvP Skill only bonusy ignoruje**, All-out-power je aplikuje celé.

#### Kasárna (+HP jednotek; v MF hradba a hrdinové)

| Level | Radnice | Cena | Čas | Bonus (kumulativně) |
|---|---|---|---|---|
| 1 | 1 | 25 jídla, 15 dřeva | 1 min | +1 % HP |
| 2 | 1 | 30 jídla, 20 dřeva | 1 min | +2 % HP |
| 3 | 2 | 70 jídla, 50 dřeva | 5 min | +3 % HP |
| 4 | 2 | 85 jídla, 65 dřeva | 5 min | +4 % HP |
| 5 | 3 | 190 jídla, 140 dřeva, 140 zlata | 45 min | +5 % HP |
| 6 | 3 | 240 jídla, 180 dřeva, 180 zlata | 45 min | +6 % HP |
| 7 | 4 | 800 jídla, 600 dřeva, 600 zlata | 3 h | +7 % HP |
| 8 | 4 | 1 000 jídla, 750 dřeva, 750 zlata | 3 h 30 min | +8 % HP |
| 9 | 5 | 2 200 jídla, 1 700 dřeva, 1 700 zlata | 6 h | +9 % HP |
| 10 | 5 | 2 800 jídla, 2 100 dřeva, 2 100 zlata | 7 h | +10 % HP |
| 11 | 6 | 5 100 jídla, 3 800 dřeva, 3 800 zlata | 10 h | +11 % HP |
| 12 | 6 | 6 400 jídla, 4 800 dřeva, 4 800 zlata | 12 h | +12 % HP |
| 13 | 7 | 15 000 jídla, 12 000 dřeva, 12 000 zlata | 13 h | +13 % HP |
| 14 | 7 | 19 000 jídla, 14 000 dřeva, 14 000 zlata | 17 h | +14 % HP |
| 15 | 8 | 29 000 jídla, 22 000 dřeva, 22 000 zlata | 19 h | +15 % HP |
| 16 | 8 | 36 000 jídla, 27 000 dřeva, 27 000 zlata | 1 d | +16 % HP |
| 17 | 9 | 58 000 jídla, 43 000 dřeva, 43 000 zlata | 1 d | +17 % HP |
| 18 | 9 | 72 000 jídla, 54 000 dřeva, 54 000 zlata | 1 d 8 h | +18 % HP |
| 19 | 10 | 120 000 jídla, 86 000 dřeva, 86 000 zlata | 1 d 8 h | +19 % HP |
| 20 | 10 | 140 000 jídla, 110 000 dřeva, 110 000 zlata | 1 d 16 h | +20 % HP |
| **Celkem 1 kus** | | 507 940 jídla, 382 220 dřeva, 382 070 zlata | 10 d 4 h 12 min | |

#### Kovárna (+útok jednotek)

| Level | Radnice | Cena | Čas | Bonus (kumulativně) |
|---|---|---|---|---|
| 1 | 2 | 15 dřeva, 25 kamene | 1 min | +1 % útok |
| 2 | 2 | 20 dřeva, 30 kamene | 1 min | +2 % útok |
| 3 | 2 | 50 dřeva, 70 kamene | 5 min | +3 % útok |
| 4 | 2 | 65 dřeva, 85 kamene | 5 min | +4 % útok |
| 5 | 3 | 140 dřeva, 190 kamene, 140 zlata | 45 min | +5 % útok |
| 6 | 3 | 180 dřeva, 240 kamene, 180 zlata | 45 min | +6 % útok |
| 7 | 4 | 600 dřeva, 800 kamene, 600 zlata | 3 h | +7 % útok |
| 8 | 4 | 750 dřeva, 1 000 kamene, 750 zlata | 3 h 30 min | +8 % útok |
| 9 | 5 | 1 700 dřeva, 2 200 kamene, 1 700 zlata | 6 h | +9 % útok |
| 10 | 5 | 2 100 dřeva, 2 800 kamene, 2 100 zlata | 7 h | +10 % útok |
| 11 | 6 | 3 800 dřeva, 5 100 kamene, 3 800 zlata | 10 h | +11 % útok |
| 12 | 6 | 4 800 dřeva, 6 400 kamene, 4 800 zlata | 12 h | +12 % útok |
| 13 | 7 | 12 000 dřeva, 15 000 kamene, 12 000 zlata | 13 h | +13 % útok |
| 14 | 7 | 14 000 dřeva, 19 000 kamene, 14 000 zlata | 17 h | +14 % útok |
| 15 | 8 | 22 000 dřeva, 29 000 kamene, 22 000 zlata | 19 h | +15 % útok |
| 16 | 8 | 27 000 dřeva, 36 000 kamene, 27 000 zlata | 1 d | +16 % útok |
| 17 | 9 | 43 000 dřeva, 58 000 kamene, 43 000 zlata | 1 d | +17 % útok |
| 18 | 9 | 54 000 dřeva, 72 000 kamene, 54 000 zlata | 1 d 8 h | +18 % útok |
| 19 | 10 | 86 000 dřeva, 120 000 kamene, 86 000 zlata | 1 d 8 h | +19 % útok |
| 20 | 10 | 110 000 dřeva, 140 000 kamene, 110 000 zlata | 1 d 16 h | +20 % útok |
| **Celkem 1 kus** | | 382 220 dřeva, 507 940 kamene, 382 070 zlata | 10 d 4 h 12 min | |

#### Akademie (+talentové body a sloty)

+1 talentový bod každé 3 levely, +1 talentový slot na L10 a L20.

| Level | Radnice | Cena | Čas | Bonus (kumulativně) |
|---|---|---|---|---|
| 1 | 4 | 15 dřeva, 15 kamene, 20 zlata | 1 min | 0 |
| 2 | 4 | 20 dřeva, 20 kamene, 25 zlata | 1 min | 0 |
| 3 | 4 | 45 dřeva, 45 kamene, 60 zlata | 5 min | +1 talentový bod |
| 4 | 4 | 55 dřeva, 55 kamene, 70 zlata | 5 min | +1 talentový bod |
| 5 | 4 | 170 dřeva, 170 kamene, 230 zlata | 45 min | +1 talentový bod |
| 6 | 4 | 220 dřeva, 220 kamene, 290 zlata | 1 h | +2 talentové body |
| 7 | 4 | 720 dřeva, 720 kamene, 960 zlata | 3 h 30 min | +2 talentové body |
| 8 | 4 | 900 dřeva, 900 kamene, 1 200 zlata | 4 h | +2 talentové body |
| 9 | 5 | 2 000 dřeva, 2 000 kamene, 2 700 zlata | 7 h | +3 talentové body |
| 10 | 5 | 2 500 dřeva, 2 500 kamene, 3 400 zlata | 8 h | +3 talentové body, +1 slot |
| 11 | 6 | 4 600 dřeva, 4 600 kamene, 6 100 zlata | 11 h | +3 talentové body, +1 slot |
| 12 | 6 | 5 800 dřeva, 5 800 kamene, 7 700 zlata | 14 h | +4 talentové body, +1 slot |
| 13 | 7 | 14 000 dřeva, 14 000 kamene, 18 000 zlata | 16 h | +4 talentové body, +1 slot |
| 14 | 7 | 17 000 dřeva, 17 000 kamene, 23 000 zlata | 20 h | +4 talentové body, +1 slot |
| 15 | 8 | 26 000 dřeva, 26 000 kamene, 35 000 zlata | 22 h | +5 talentových bodů, +1 slot |
| 16 | 8 | 32 000 dřeva, 32 000 kamene, 43 000 zlata | 1 d 4 h | +5 talentových bodů, +1 slot |
| 17 | 9 | 52 000 dřeva, 52 000 kamene, 69 000 zlata | 1 d 6 h | +5 talentových bodů, +1 slot |
| 18 | 9 | 65 000 dřeva, 65 000 kamene, 86 000 zlata | 1 d 12 h | +6 talentových bodů, +1 slot |
| 19 | 10 | 100 000 dřeva, 100 000 kamene, 140 000 zlata | 1 d 14 h | +6 talentových bodů, +1 slot |
| 20 | 10 | 130 000 dřeva, 130 000 kamene, 170 000 zlata | 2 d | +6 talentových bodů, +2 sloty |
| **Celkem 1 kus** | | 453 045 dřeva, 453 045 kamene, 606 755 zlata | 11 d 23 h 27 min | |

#### Tržiště (+odměny ze zápasů)

Platí na suroviny a soft měnu ze zápasů, ne na gemy a ne na odměny z žebříčků *(návrh)*. Pozor na smyčku: Tržiště zvyšuje i příjem surovin pro město, model v kapitole 7 s tímto bonusem nepočítá (je to rezerva asi 10 až 20 % pro aktivní hráče).

| Level | Radnice | Cena | Čas | Bonus (kumulativně) |
|---|---|---|---|---|
| 1 | 3 | 15 jídla, 15 dřeva, 20 zlata | 1 min | +2 % odměn ze zápasu |
| 2 | 3 | 40 jídla, 40 dřeva, 55 zlata | 5 min | +4 % odměn ze zápasu |
| 3 | 3 | 160 jídla, 160 dřeva, 220 zlata | 45 min | +6 % odměn ze zápasu |
| 4 | 4 | 680 jídla, 680 dřeva, 900 zlata | 3 h | +8 % odměn ze zápasu |
| 5 | 5 | 1 900 jídla, 1 900 dřeva, 2 500 zlata | 6 h | +10 % odměn ze zápasu |
| 6 | 6 | 4 300 jídla, 4 300 dřeva, 5 800 zlata | 10 h | +12 % odměn ze zápasu |
| 7 | 7 | 13 000 jídla, 13 000 dřeva, 17 000 zlata | 14 h | +14 % odměn ze zápasu |
| 8 | 8 | 24 000 jídla, 24 000 dřeva, 32 000 zlata | 20 h | +16 % odměn ze zápasu |
| 9 | 9 | 49 000 jídla, 49 000 dřeva, 65 000 zlata | 1 d 2 h | +18 % odměn ze zápasu |
| 10 | 10 | 97 000 jídla, 97 000 dřeva, 130 000 zlata | 1 d 10 h | +20 % odměn ze zápasu |
| **Celkem 1 kus** | | 190 095 jídla, 190 095 dřeva, 253 495 zlata | 4 d 17 h 51 min | |

#### Svatyně (+XP ze zápasů)

| Level | Radnice | Cena | Čas | Bonus (kumulativně) |
|---|---|---|---|---|
| 1 | 5 | 15 jídla, 15 kamene, 20 zlata | 1 min | +2 % XP ze zápasu |
| 2 | 5 | 40 jídla, 40 kamene, 55 zlata | 5 min | +4 % XP ze zápasu |
| 3 | 5 | 160 jídla, 160 kamene, 220 zlata | 45 min | +6 % XP ze zápasu |
| 4 | 5 | 680 jídla, 680 kamene, 900 zlata | 3 h | +8 % XP ze zápasu |
| 5 | 5 | 1 900 jídla, 1 900 kamene, 2 500 zlata | 6 h | +10 % XP ze zápasu |
| 6 | 6 | 4 300 jídla, 4 300 kamene, 5 800 zlata | 10 h | +12 % XP ze zápasu |
| 7 | 7 | 13 000 jídla, 13 000 kamene, 17 000 zlata | 14 h | +14 % XP ze zápasu |
| 8 | 8 | 24 000 jídla, 24 000 kamene, 32 000 zlata | 20 h | +16 % XP ze zápasu |
| 9 | 9 | 49 000 jídla, 49 000 kamene, 65 000 zlata | 1 d 2 h | +18 % XP ze zápasu |
| 10 | 10 | 97 000 jídla, 97 000 kamene, 130 000 zlata | 1 d 10 h | +20 % XP ze zápasu |
| **Celkem 1 kus** | | 190 095 jídla, 190 095 kamene, 253 495 zlata | 4 d 17 h 51 min | |

### 5.5 Dekorace

Bez stavitele, stavba okamžitá, bez meta bonusu (kosmetika a sink, design kap. 3.2).

| Dekorace | Odemyká Radnice | Cena | Poznámka |
|---|---|---|---|
| Prapor | 2 | 2 000 dřeva | max 4 kusy, barva podle erbu města |
| Fontána | 4 | 15 000 zlata | max 2 kusy |
| Socha hrdiny | 6 | 150 gemů | max 1 kus, prémiový sink; varianta v nabídkách a battle passu |

### 5.6 Překážky

| Parametr | Hodnota *(návrh)* |
|---|---|
| Počet na startu | 30 (stromy a kameny) |
| Odstranění | 10 s, potřebuje volného stavitele, zdarma |
| Odměna | strom: dřevo, kámen: kámen, množství = 1 h produkce jedné produkční budovy na aktuální Radnici; plus 0 až 2 gemy (průměr 0,9) |
| Obnova | 1 nová překážka za 8 h, max 30 na mapě |

Překážky dají na startu asi 27 gemů a pak asi 2,7 gemu denně.

### 5.7 Questy kapitol (onboarding)

Kapitola končí zvednutím Radnice o level, odměny se vyplácí průběžně za jednotlivé úkoly. Odměny kryjí náklady prvního dne (chybějících asi 115 zlata dodají první zápasy), pak postupně klesají.

| Kapitola | Úkoly | Odměna | Pokrytí nákladů tieru |
|---|---|---|---|
| Start | | 500 jídla, 500 dřeva | |
| 1 | Farma, Pila, Sklad, Kasárna L2, Radnice 2 | 500 jídla, 500 dřeva, 500 kamene, 12 gemů | tier 1 a 2: 100 % i se startem |
| 2 | Lom, Kovárna, Radnice 3 | 600 jídla, 600 dřeva, 500 kamene, 18 gemů, 3× zrychlení 15 min | |
| 3 | Zlatý důl, Tržiště, Radnice 4 | 2 000 jídla, 2 000 dřeva, 1 500 kamene, 1 000 zlata, 30 gemů, 2× zrychlení 1 h | tier 1 až 3 dohromady asi 100 % (náklady 8 710 surovin) |
| 4 | Akademie, druhé kusy produkce, Radnice 5 | 5 000 jídla, 5 000 dřeva, 4 000 kamene, 3 000 zlata, 30 gemů, 1× zrychlení 8 h | tier 4: asi 40 % |
| 5 | Svatyně, Radnice 6 | 10 000 jídla, 10 000 dřeva, 8 000 kamene, 6 000 zlata, 60 gemů | tier 5: asi 29 % |

Gemy zdarma za první týden: kapitoly 150 + překážky asi 45 = **asi 195 gemů**, tedy stavitel #3 je pro neplatícího hráče dosažitelný za asi 2 týdny (CoC podobně).

## 6. Souhrnné tabulky

### 6.1 Po tierech Radnice

Tier = období, kdy má hráč daný level Radnice; obsahuje všechny upgrady dostupné na tom levelu včetně zvednutí Radnice na další level. "Kumulativně den" = kdy aktivní hráč dokončí celý tier (2 stavitelé, 75 % vytížení; tier 1 až 2 při 100 %). Hráč, který Radnici "rushuje", je v dalším tieru dřív.

| Tier (Radnice) | Práce stavitelů | Dní se 2 staviteli | Kumulativně den | Cena tieru celkem | Pasivní produkce / den | Podíl produkce | Gemy na zrychlení celého tieru |
|---|---|---|---|---|---|---|---|
| 1 | 0,1 h | 0 | 0 | 160 jídla, 190 dřeva | 770 | 1 % | 0 |
| 2 | 0,9 h | 0 | 0 | 460 jídla, 645 dřeva, 435 kamene | 1 600 | 2 % | 5 |
| 3 | 8,7 h | 0,2 | 0,3 | 1 850 jídla, 2 400 dřeva, 1 455 kamene, 1 115 zlata | 3 000 | 11 % | 113 |
| 4 | 59,7 h | 1,7 | 1,9 | 10 210 jídla, 14 795 dřeva, 9 760 kamene, 7 205 zlata | 8 400 | 33 % | 563 |
| 5 | 120,8 h | 3,4 | 5,3 | 29 595 jídla, 38 200 dřeva, 27 795 kamene, 21 995 zlata | 12 000 | 34 % | 948 |
| 6 | 193 h | 5,4 | 10,6 | 65 900 jídla, 87 500 dřeva, 61 200 kamene, 47 400 zlata | 17 000 | 34 % | 1 333 |
| 7 | 376,3 h | 10,5 | 21,1 | 261 430 jídla, 333 120 dřeva, 222 765 kamene, 141 000 zlata | 35 000 | 38 % | 2 565 |
| 8 | 448 h | 12,4 | 33,5 | 450 000 jídla, 580 000 dřeva, 390 000 kamene, 267 000 zlata | 49 000 | 36 % | 2 665 |
| 9 | 586 h | 16,3 | 49,8 | 904 000 jídla, 1 159 000 dřeva, 784 000 kamene, 533 000 zlata | 68 000 | 33 % | 3 281 |
| 10 | 668 h | 18,6 | 68,4 | 1 429 000 jídla, 1 937 000 dřeva, 1 352 000 kamene, 962 000 zlata | 95 000 | 31 % | 3 625 |
| **Celkem** | 2 461 h | | 68,4 | 3 152 605 jídla, 4 152 850 dřeva, 2 849 410 kamene, 1 980 715 zlata (Σ 12 135 580) | | | 15 098 |

### 6.2 Celkem na maximum podle budovy

| Budova | Kusů | Čas na max (1 kus) | Cena na max (všechny kusy) |
|---|---|---|---|
| Radnice | 1 | 9 d 23 h 18 min | 361 785 jídla, 361 785 dřeva, 208 760 kamene, 102 830 zlata |
| Farma | 3 | 3 d 20 h 3 min | 884 835 dřeva, 379 155 kamene |
| Pila | 3 | 3 d 20 h 3 min | 884 835 jídla, 379 155 kamene |
| Lom | 3 | 3 d 20 h 3 min | 638 670 jídla, 638 670 dřeva |
| Zlatý důl | 3 | 3 d 20 h 3 min | 379 185 jídla, 507 855 dřeva, 379 185 kamene |
| Sklad | 1 | 4 d 17 h 51 min | 352 125 dřeva, 352 075 kamene |
| Kasárna | 1 | 10 d 4 h 12 min | 507 940 jídla, 382 220 dřeva, 382 070 zlata |
| Kovárna | 1 | 10 d 4 h 12 min | 382 220 dřeva, 507 940 kamene, 382 070 zlata |
| Akademie | 1 | 11 d 23 h 27 min | 453 045 dřeva, 453 045 kamene, 606 755 zlata |
| Tržiště | 1 | 4 d 17 h 51 min | 190 095 jídla, 190 095 dřeva, 253 495 zlata |
| Svatyně | 1 | 4 d 17 h 51 min | 190 095 jídla, 190 095 kamene, 253 495 zlata |

## 7. Příjem surovin, který musí dodat hostitelská hra

Aby tempo z kapitoly 6 sedělo, musí zápasy, odměny a questy dodávat zbytek po pasivní produkci. Toto je **zadání pro reward config hostitelské hry** (MF, Hex). Bonus Tržiště ani nákupy tu nejsou započítané.

| Tier | Útrata / den (cíl) | Pasivní produkce / den | Ze zápasů a odměn / den | Na zápas při 6 zápasech denně |
|---|---|---|---|---|
| 3 | 28 000 | 3 000 | 25 000 | 4 200 |
| 4 | 25 000 | 8 400 | 17 000 | 2 800 |
| 5 | 35 000 | 12 000 | 23 000 | 3 900 |
| 6 | 49 000 | 17 000 | 32 000 | 5 400 |
| 7 | 92 000 | 35 000 | 57 000 | 9 500 |
| 8 | 140 000 | 49 000 | 87 000 | 14 000 |
| 9 | 210 000 | 68 000 | 140 000 | 23 000 |
| 10 | 310 000 | 95 000 | 210 000 | 35 000 |

- Tier 3 je první den a kryjí ho kapitoly questů, ne zápasy.
- Odměny ze zápasů se mají škálovat podle levelu Radnice hráče (jinak hráč na Radnici 9 dostane stejně jako na Radnici 3), *(návrh)*: reward = základ tieru z tabulky / 6 × výkon v zápase.
- PvP odměny (design PvP kap. 8) jsou součást tohoto příjmu, ne navíc.

## 8. Monetizace

| Touchpoint | Cena | Poznámka |
|---|---|---|
| Zrychlení stavby | `gemy = ceil(12 × hodiny^0,77)`, do 5 min zdarma | v dolarech blízko CoC (1 h = 12, 1 d = 139, 7 d = 621) |
| Dokoupení chybějících surovin | `gemy = ceil(0,6 × (množství / 100)^0,695)` za každou surovinu zvlášť | 1 000 = 3, 100 000 = 73; levnější než čas, jako v CoC |
| Stavitel #3 | 300 gemů nebo nabídka 4,99 USD | hlavní konverzní nákup prvního týdne |
| Stavitel #4 | 600 gemů nebo nabídka 9,99 USD | |
| Balíček surovin podle tieru | 1 den příjmu ze zápasů (kapitola 7): 1,99 USD (Radnice 4 až 6), 4,99 USD (7 až 8), 9,99 USD (9 až 10) | nabídka při "chybí suroviny" a při plném stavitelském slotu |
| Předměty zrychlení | v nabídkách a battle passu | MF už má `SkipItsCurrency` |
| Prémiové dekorace | 150 gemů a víc | čistá kosmetika |
| VIP / subscription | až podle otázky 5 v designu | návrh: +20 % produkce, auto-sběr, stavitel navíc po dobu předplatného |

Ceny zrychlení:

| Čas | Gemy |
|---|---|
| 5 min | 0 |
| 10 min | 4 |
| 30 min | 8 |
| 1 h | 12 |
| 3 h | 28 |
| 8 h | 60 |
| 1 d | 139 |
| 3 d | 324 |
| 7 d | 621 |

| Suroviny | Gemy |
|---|---|
| 1 000 | 3 |
| 10 000 | 15 |
| 50 000 | 46 |
| 100 000 | 73 |
| 190 000 | 114 |

Přepočet gemů na peníze: **60 gemů = 1 USD** (náš ceník, potvrzeno 5. 11.). Gemové ceny jsou proti CoC (asi 100 gemů za 1 USD) vynásobené 0,6, takže v dolarech stojí totéž. Zrychlení Radnice 10 stojí 344 gemů, zrychlení celé verze 1 asi 15 100 gemů (asi 250 USD). Koeficient 12 ve vzorci odpovídá právě 60 gemům za 1 USD.

## 9. KPI pro ladění na stagingu MF

| KPI | Cíl | Když je pod cílem | Když je nad cílem |
|---|---|---|---|
| Den dosažení Radnice 4 / 6 / 8 / 10 (medián hráčů, kteří město hrají) | 1 / 5 až 7 / 21 až 25 / 50 | zkrátit časovou tabulku τ tieru, přidat odměny kapitol | prodloužit τ vyšších tierů, zpomalit gating stage indexem |
| Vytížení stavitelů (podíl času, kdy staví) | 70 až 80 % | časovače jsou moc krátké vůči rytmu návštěv: prodloužit τ, nebo přidat notifikace "stavitel volný" | v pořádku, hlídat churn |
| Stavitel čeká na suroviny (podíl času) | pod 25 % | | snížit tabulku cen C, nebo zvýšit odměny ze zápasů |
| Návraty do města za den | 3 a víc | zkrátit kapacitu budovy (10 h → 8 h), push "sklad plný" | v pořádku |
| Podíl pasivní produkce na příjmu | 30 až 40 % | zvýšit produkci (r1) | snížit produkci, hráči přestávají hrát zápasy |
| Hráči s plným Skladem (denně) | pod 20 % | | posílit kapacitu Skladu, nebo upozornit na upgrade |
| Konverze na stavitele #3 do D7 | 2 až 4 % hráčů města *(předpoklad)* | silnější startovní nabídka, víc gemů zdarma na ochutnání | zvážit cenu 450 gemů |
| Podíl síly z města na celkové síle (D30) | 15 až 25 % | zvýšit procenta za level | snížit procenta nebo strop přes RC |
| Win rate PvE a All-out-power podle levelu Radnice | rozdíl mezi Radnicí 5 a 10 do 10 p. b. ve stejné lize | | snížit stropy bonusů, ligy podle síly |
| D1 / D7 / D30 s městem proti bez (A/B) | D7 a D30 nahoru, D1 bez poklesu | zjednodušit první den, víc kapitol | |

Ladí se jen parametry z kapitoly 10 (tabulky τ a C, váhy, r1, kapacita) přes Remote Config, pak se tabulky přepočítají.

## 10. Vzorce a parametry (pro přepočet)

Úkol = jeden level jedné budovy (u produkce pro každý kus zvlášť).

- **Nominální tier** levelu L: produkce, Sklad, Tržiště, Svatyně: `n = L`; Kasárna, Kovárna, Akademie: `n = ceil(L / 2)`; Radnice: `n = L - 1` (staví se v předchozím tieru).
- **Gating** (kdy jde postavit): `max(n, Radnice odemčení budovy nebo kusu)`, u Radnice tier `L - 1`.
- **Čas:** `čas = w × f × τ(n)`, **cena celkem:** `cena = k × f × C(n)`, rozdělená podle receptu. `f = 0,8` pro lichý level u budov se 2 levely na tier, jinak 1,0.
- **Produkce:** `r(L) = 20 × 1,4^(L - 1)` za hodinu, kapacita budovy = 10 × r(L). Do příjmu se počítá s účinností sběru 80 %.
- **Sklad:** kapacita(L) = max(1,25 × nejdražší jednotlivá surovina v tieru L - 1 000; 1,3 × kapacita(L - 1); 500).
- **Zaokrouhlení:** ceny pod 100 na 5, jinak na 2 platné číslice; časy pod 1 h na 1, 2, 3, 5, 10, 15, 20, 30, 45 min, do 6 h na půl hodiny, do 24 h na hodiny, nad 24 h na 2 hodiny.
- **Dny tieru:** `Σ časů tieru / (stavitelé × vytížení) / 24`, vytížení 0,75 (tier 1 až 2: 1,0).
- **Podíl produkce:** `pasivní za den × dny tieru / cena tieru`, pasivní za den = r(tier) × 24 × 0,8 × kusů × počet odemčených surovin.

Tabulky tierů:

| Tier | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| τ (časová jednotka) | 1 min | 5 min | 45 min | 3 h | 6 h | 10 h | 14 h | 20 h | 26 h | 34 h |
| C (cenová jednotka) | 50 | 150 | 600 | 2 500 | 7 000 | 16 000 | 48 000 | 90 000 | 180 000 | 360 000 |

Váhy a recepty:

| Budova | w (čas) | k (cena) | Recept ceny | Odemčení | Max level |
|---|---|---|---|---|---|
| Radnice | 3,0 | 3,0 | jídlo 35 %, dřevo 35 %, kámen 20 %, zlato 10 % | start | 10 |
| Farma | 0,8 | 0,6 | dřevo 70 %, kámen 30 % | Radnice 1 | Radnice |
| Pila | 0,8 | 0,6 | jídlo 70 %, kámen 30 % | Radnice 1 | Radnice |
| Lom | 0,8 | 0,6 | jídlo 50 %, dřevo 50 % | Radnice 2 | Radnice |
| Zlatý důl | 0,8 | 0,6 | jídlo 30 %, dřevo 40 %, kámen 30 % | Radnice 3 | Radnice |
| Sklad | 1,0 | 1,0 | dřevo 50 %, kámen 50 % | Radnice 1 | Radnice |
| Kasárna | 1,2 | 1,0 | jídlo 40 %, dřevo 30 %, zlato 30 % | Radnice 1 | 2× Radnice |
| Kovárna | 1,2 | 1,0 | dřevo 30 %, kámen 40 %, zlato 30 % | Radnice 2 | 2× Radnice |
| Akademie | 1,4 | 1,2 | dřevo 30 %, kámen 30 %, zlato 40 % | Radnice 4 | 2× Radnice |
| Tržiště | 1,0 | 0,9 | jídlo 30 %, dřevo 30 %, zlato 40 % | Radnice 3 | Radnice |
| Svatyně | 1,0 | 0,9 | jídlo 30 %, kámen 30 %, zlato 40 % | Radnice 5 | Radnice |

Kalibrace: τ je nastavené tak, aby aktivní hráč došel na Radnici 10 kolem 50. dne; C tak, aby pasivní produkce kryla asi 35 % útraty tieru (tier 7 má C zvýšené kvůli třetím kusům produkce, které jinak podíl produkce vychýlí nahoru).

## 11. Vazba na dnešní mapu MF

V MF už existuje systém budov na mapě (`NoxFort/Assets/_Project/Entities/MapBuilding`): Gold Mine, Gem Mine, Stone Mine, Energy Generator, Jeweler, Wall (s talenty), Bestiary, Challenges. Moduly `ConstructionModule`, `UpgradingModule`, `CurrencyGeneratorModule`, `TalentModule` a `Modifiers` jsou dobrý základ pro City V2. Dnešní Gold Mine má 10 levelů, upgrady stojí 240 až 1 080 `HardCurrency` a trvají 2 h až 2 d 8 h, odemyká se podle stage indexu. City V2 platí upgrady surovinami (klon CoC a RoK), gemy jen za zrychlení a stavitele; jak to sladit s dnešní mapou, je otevřená otázka.

## 12. Později (mimo verzi 1, podle designu kap. 4)

- Radnice 11 a výš, víc kusů budov, nové budovy (V2).
- Výroba jednotek a nemocnice, výzkum v Akademii.
- HP budov, obrana, hradby a štíty (až s útoky na města; ve verzi 1 nejsou, proto tu HP chybí).
- VIP, pokud se nerozhodne pro verzi 1.
- Síla města jako číslo pro žebříčky, aliance a pomoc se stavbou, návštěvy měst.

## 13. Otevřené otázky

1. **Ceník gemů:** vyřešeno, 60 gemů = 1 USD (5. 11.). Zbývá ověřit, že `HardCurrency` v MF a gemy v Hexu mají stejný ceník.
2. **Mapování surovin:** MF má soft měnu, `HardCurrency`, kameny a další měny; Hex má vlastní. Které z nich jsou jídlo, dřevo, kámen a zlato, nebo zavádíme 4 nové suroviny jen pro město?
3. **Dnešní mapa MF:** nahradí City V2 současné `MapBuilding` budovy, nebo je rozšíří (Gold Mine a Stone Mine jako produkce, Wall jako Kasárna)?
4. **Meta staty v MF a Hexu:** HP a útok čeho přesně (hradba, hrdinové, jednotky Hexu)? Co znamená talentový bod a slot v MF a v Hexu? Na čem se počítá XP ze Svatyně?
5. **Stropy 20 %:** sedí vůči ostatním zdrojům síly? Potřebujeme křivku síly hráče MF a Hexu na D1, D7, D30 (telemetrie), pak doladit procenta za level.
6. **Odměny ze zápasů:** dodá hostitelská hra příjem z kapitoly 7 (škálovaný podle Radnice), a kolik zápasů denně hraje medián aktivního hráče (model počítá 6)?
7. **Gating Radnice v Hexu:** jaké milníky (světy, PvP výhry) odpovídají MF stage 5 až 27?
8. **Stavitel #3 a #4:** cena 300 a 600 gemů, nebo jen přes nabídky, a jestli VIP dává stavitele.
