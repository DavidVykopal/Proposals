# City V2: první nahození čísel (verze 1)

> **Stav:** první nahození, 5. 11. 2026. Všechna čísla jsou k ladění na stagingu Mecha Fortress (MF), pak se přenesou do Hexapolisu. Design a rozsah: `DESIGN_CITY_V2.md`.
> **Pro AI agenty:** tento soubor je číselný doprovod k `DESIGN_CITY_V2.md`. Pravidla a rozsah určuje design dokument; když se liší, platí design. Čísla tady jsou vygenerovaná ze vzorců v kapitole 10, při změně parametrů se přepočítají všechny tabulky (žádné ruční úpravy jednotlivých buněk). Věci označené *(předpoklad)* nejsou ověřené na datech.
> **Rozhodnuto 6. 11. 2026 (David):** City V2 **nahradí dnešní budovy na mapě MF** (Gold Mine, Gem Mine a další) a hráči dostanou **refund** toho, co do nich investovali (pravidlo v kap. 11, *návrh*). Za gemy si hráč koupí **startovní bundle surovin** a **City VIP** (zrychlení stavby a další výhody), čísla v kap. 8.1 a 8.2 (*návrh*). Příjmy z Play Passu se do revenue Hexu nepočítají. Kap. 10 (vzorce) se nemění; tabulka dopadu VIP na tempo je spočítaná skriptem z tabulky 6.1 (vzorec u tabulky).

## 1. Shrnutí

- **Radnice 1 až 10** ve verzi 1. Ostatní budovy mají max level podle Radnice: produkce, Sklad, Tržiště a Svatyně = level Radnice (max 10), Kasárna, Kovárna a Akademie = 2× level Radnice (max 20).
- **Tempo aktivního hráče** (6 zápasů denně, 2 stavitelé, 3 a více návštěv města denně): Radnice 4 první den, Radnice 6 do konce prvního týdne, Radnice 8 kolem 21. dne, **Radnice 10 kolem 50. dne**, **vše na maximu verze 1 kolem 68. dne**. To kryje leden a únor 2027, než přijde V2 (Radnice 11 a víc).
- **Rytmus session:** sběr produkce 2 až 3× denně (kapacita budovy 10 h produkce), stavitelé se od Radnice 6 přenastavují 1 až 2× denně, první den časovače do 45 min.
- **Ekonomika:** pasivní produkce kryje **asi 1/3** útraty (31 až 38 % od Radnice 4), zbytek jde ze zápasů, odměn a questů. Odpovídá zásadě z designu: hlavní příjem je ze hraní.
- **Síla z města:** na maximu verze 1 dává město +20 % HP a +20 % útok, tedy **×1,44 efektivní síly** (HP × útok), plus 6 talentových bodů, 2 sloty, +20 % XP a +20 % odměn. Cíl: město tvoří **15 až 25 % celkové síly** hráče na D30 *(předpoklad, ověřit telemetrií)*.
- **Monetizace:** zrychlení za gemy (prvních 5 min zdarma), stavitel #3 za 300 gemů, #4 za 600 gemů, balíčky surovin, **startovní bundle surovin za 60 gemů** a **City VIP za 450 gemů na 30 dní** *(návrh, kap. 8.1 a 8.2)*. Zrychlit celou verzi 1 stojí asi **15 100 gemů** (cca 250 USD při našem ceníku 60 gemů za 1 USD).
- **Hloubka monetizace (9. 11., kap. 8.3):** cíl je, aby plné město stálo za gemy **10 až 100 tis. USD** a průměrný platící hráč nechal **aspoň desítky USD**. Verze 1 má hloubku jen cca **440 USD** (zrychlení 250 + dokoupení surovin 185). Hloubku dají až další verze: Radnice 15 cca 5 tis., Radnice 20 cca 20 tis., **Radnice 25 cca 58 tis. USD** s novými vrstvami (výzkum, obranné věže, hradby, nemocnice). Vzorce cen se nemění, roste obsah. Odhad výnosu v Hexu: **1,3 až 9,5 tis. USD měsíčně, základ 2,8 tis.**
- **City VIP nerozbije tempo:** průměrnému hráči (6 zápasů denně) zkrátí cestu na Radnici 10 jen z 50 na 47 dní, protože brzdí suroviny. Strop je hráč se stavitelem #3, VIP a dokupováním surovin: Radnice 10 kolem 21. dne, vše na maximu kolem 29. dne (kap. 8.2).
- **Náhrada mapy MF (Rozhodnuto 6. 11.):** City V2 nahradí `MapBuilding` budovy v MF. Refund *(návrh)*: 100 % utracené `HardCurrency` zpět jako gemy a startovní Radnice podle nejvyšší dnešní budovy (max Radnice 5), kap. 11.
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
| Startovní bundle surovin | 60 gemů, jednorázově | kap. 8.1 *(návrh)* |
| City VIP | 120 gemů / 7 dní, 450 gemů / 30 dní | kap. 8.2 *(návrh)*: −15 % času staveb, +1 stavitelská fronta, denní zrychlení 30 min zdarma, +20 % produkce |

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

### 8.1 Startovní bundle surovin *(návrh)*

Rozhodnuto 6. 11.: gemy kupují bundle surovin do začátku. Čísla jsou návrh.

| Parametr | Hodnota |
|---|---|
| Obsah | 10 000 jídla, 15 000 dřeva, 10 000 kamene, 7 000 zlata, 3× zrychlení 1 h |
| Cena | **60 gemů** (1 USD), jednorázově na účet |
| Kdy se nabízí | od Radnice 3 do dokončení Radnice 5 |
| Hodnota podle ceníku | suroviny 62 gemů (vzorec dokoupení surovin), zrychlení 36 gemů, celkem cca 98 gemů, tedy sleva cca 40 % |

- Obsah odpovídá ceně celého tieru 4 (41 970 surovin), tedy asi 2,5 dne příjmu ze zápasů na tieru 4 (kap. 7).
- **Tempo:** tier 4 je se 2 staviteli časově omezený (1,7 dne), takže bundle zkrátí cestu jen o čekání na suroviny, odhadem pod 1 den. Hlavní účel je první nákup za gemy, ne zrychlení.
- Hráči MF s refundem (kap. 11) mají gemy hned, bundle je pro ně přirozený první nákup.

### 8.2 City VIP *(návrh)*

Rozhodnuto 6. 11.: City VIP je gem sink se zrychlením stavby. Konkrétní hodnoty jsou návrh, ladí se přes RC.

| Parametr | Hodnota |
|---|---|
| Cena | **120 gemů na 7 dní** (2 USD), **450 gemů na 30 dní** (7,50 USD) |
| Čas staveb a upgradů | −15 % |
| Stavitelská fronta | +1 po dobu VIP (sčítá se se staviteli #3 a #4) |
| Denní zrychlení zdarma | 1× 30 min (hodnota 8 gemů denně, 240 gemů za 30 dní) |
| Pasivní produkce | +20 % |
| Auto-sběr | ne: sběr drží návraty do města (KPI 3+ návraty denně) |
| Platnost | vyprší bez obnovy; rozestavěné stavby ve frontě VIP doběhnou, novou už do ní hráč nezadá |

- Proč 450, ne 300 gemů: stavitel #3 stojí trvale 300 gemů, takže VIP za 300 na měsíc by ho kanibalizovalo. Pořadí nákupů: bundle (60), stavitel #3 (300), pak VIP jako opakovaný nákup.
- VIP se hodí i jako prémiová odměna (PvP žebříčky, battle pass) v 7denní variantě.

**Dopad na tempo** (dny do dosažení, model z kap. 6.1: čas tieru = práce stavitelů × 0,85 / (fronty × 0,75 × 24 h + 0,5 h zdarma denně); dny podle surovin = dny základu / (1 + 0,2 × podíl produkce tieru); platí delší z obou):

| Hráč | Radnice 6 | Radnice 8 | Radnice 10 | Vše na max V1 |
|---|---|---|---|---|
| Základ: 2 stavitelé, 6 zápasů denně, bez VIP | 5,3 | 21,1 | 49,8 | 68,4 |
| VIP, 6 zápasů denně (brzdí suroviny) | 5,0 | 19,7 | 46,6 | 64,0 |
| Stavitel #3 bez VIP, o 30 % víc příjmu (cca 8 zápasů denně) | 4,1 | 16,2 | 38,3 | 52,6 |
| VIP, o 30 % víc příjmu | 3,9 | 15,4 | 36,4 | 50,0 |
| VIP, suroviny nebrzdí (dokupuje) | 3,0 | 11,8 | 28,0 | 38,4 |
| Stavitel #3 + VIP, suroviny nebrzdí | 2,2 | 8,9 | 21,0 | 28,9 |

Čtení:
- **Průměrný hráč s VIP je rychlejší jen o 6 %**, protože příjem surovin je spočítaný na 2 stavitele (kap. 2). VIP tempo nerozbije a nepřeskočí gating stage indexem.
- **Aktivní a platící hráč** se zkrátí výrazně, to je záměr (stejná logika jako stavitel #3).
- **Strop:** stavitel #3 + VIP + dokupování surovin = vše na max V1 kolem 29. dne. Při lednovém releasu je to polovina února, před V2 (Radnice 11+, Q1 2027). Když V2 nebude do března, hlídat podíl hráčů na maximu a případně snížit −15 % na −10 % přes RC.

### 8.3 Hloubka monetizace a kolik to přinese *(návrh 9. 11.)*

**Cíl (David, 9. 11.):** plné město v řádu **10 až 100 tis. USD** za gemy, aby velryby měly kam růst, a průměrný platící hráč nechá **aspoň desítky USD**.

**Kde jsme dnes:** verze 1 (Radnice 1 až 10) se dá celá koupit za cca **26 100 gemů, tedy cca 440 USD**: zrychlení všech staveb 15 100 gemů (250 USD) a dokoupení všech surovin 11 100 gemů (185 USD), plus stavitelé #3 a #4 (900 gemů, 15 USD). Na cíl to nestačí ani o dva řády. Vzorce cen (kap. 8 a 10) jsou konkávní, zdražují pomaleji než roste objem, takže hloubku musí dát **obsah**, ne vyšší ceny.

**Jak hloubku postavit:** roadmapa Radnice 11 až 25 a nové vrstvy z kap. 12 a designu kap. 4. Vzorce z kap. 10 platí beze změny, tabulky τ a C se prodlouží:

| Tier | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| τ (h) | 42 | 50 | 60 | 70 | 80 | 92 | 104 | 116 | 130 | 144 | 160 | 176 | 192 | 210 | 228 |
| C (mil.) | 0,6 | 0,9 | 1,3 | 1,8 | 2,5 | 3,4 | 4,5 | 6 | 8 | 10,5 | 13,5 | 17 | 21 | 26 | 32 |

| Nová vrstva | Od Radnice | Kusů (Radnice 11 / 16 / 21) | Váhy w / k | Proč je to sink |
|---|---|---|---|---|
| Výzkum (linie v Akademii, vlastní fronta laboratoře) | 6 | 8 od Radnice 6, pak 14 / 20 | 1,2 / 1,0 | dlouhé časovače mimo stavitele, RoK |
| Obranné věže (s útoky na města, V3) | 11 | 6 / 10 / 14 | 1,0 / 0,8 | hodně kusů na každý level, CoC |
| Hradby (segmenty, bez časovače) | 11 | 100 / 175 / 250 | 0 / 0,06 | čistý surovinový sink, v CoC největší útrata velryb |
| Nemocnice | 11 | 1 | 1,2 / 1,0 | |
| Produkce: 4. a 5. kus | 11 a 16 | | jako dnes | |

**Hloubka podle verzí** (gemy na zrychlení všeho a dokoupení všech surovin, 60 gemů = 1 USD; skript nad vzorci kap. 10):

| Obsah | Kdy *(návrh)* | Plné město za gemy | z toho zrychlení / suroviny | F2P hráč se 4 staviteli |
|---|---|---|---|---|
| Verze 1: Radnice 10 | leden 2027 | **cca 440 USD** | 250 / 185 | 34 dní (68 se 2 staviteli) |
| Radnice 15 + výzkum, věže, hradby | Q2 2027 | **cca 5 000 USD** | 1 700 / 3 300 | cca 190 dní |
| Radnice 20 | Q4 2027 | **cca 20 500 USD** | 4 700 / 15 800 | cca 550 dní |
| Radnice 25 | 2028 | **cca 58 000 USD** | 8 800 / 49 100 | cca 1 200 dní |

- Největší sinky na Radnici 25: hradby cca 17,9 tis. USD, výzkum 14,4 tis., věže 7,9 tis., produkce celkem 9,5 tis. Hradby a výzkum jsou pro velryby, běžný hráč je dělá postupně.
- **Cíl 10 až 100 tis. USD splní Radnice 20 a víc.** V roce 2027 tedy realisticky 5 až 20 tis. USD podle toho, kolik verzí stihneme. To stačí: velryba tolik neutratí za měsíc, hloubka je hlavně důvod pokračovat.
- Výzkum má vlastní frontu laboratoře, aby neblokoval stavitele. Při jedné laboratoři by výzkum na Radnici 25 trval přes 7 let, proto 2 laboratoře (druhá jako prémiový nákup, stejně jako stavitel #3).
- **VIP úrovně** *(návrh)*: City VIP z kap. 8.2 doplnit o úrovně 1 až 10 podle celkové útraty gemů, s trvalými bonusy (RoK VIP). Hloubku v gemech nemění, ale dává velrybám viditelný cíl a status.

**Průměrný platící hráč** (žebříček nákupů, prvních 90 dní, ceny z kap. 8):

| Nákup | Cena |
|---|---|
| Startovní bundle surovin | 1 USD |
| Stavitel #3 (nabídka) | 4,99 USD |
| City VIP 30 dní, 2× | 15 USD |
| 2 balíčky surovin na Radnici 7 až 8 | 10 USD |
| Zrychlení (cca 300 gemů) | 5 USD |
| **Celkem za 90 dní** | **cca 36 USD** |

- Za rok s 6 měsíci VIP a stavitelem #4 je to cca **90 až 110 USD**. Cíl „desítky USD“ tedy platí pro **průměrného platícího hráče** města.
- **Na všechny hráče města to neplatí:** platí jen 1 až 3 % z nich měsíčně *(předpoklad)*, takže průměr na všechny hráče města je 0,1 až 0,9 USD měsíčně, v základu cca 0,3 USD. Desítky USD na každého hráče žádná F2P hra nemá, proto je potřeba cíl formulovat přes platící hráče a ARPDAU.

**Kolik to přinese** *(odhad, ověřit A/B testem)*:

Předpoklady: Hexapolis cca 7 tis. DAU, MAU 2,5× DAU, město hraje 60 % (cca 10 500 hráčů měsíčně). Dnešní IAP Hexu cca **8,2 tis. USD měsíčně**, MF cca **11,8 tis. USD měsíčně** (cashflow srpen až říjen 2026).

| Scénář | Platí měsíčně | ARPPU měsíčně | Hex: City za měsíc | Hex: rok 2027 (11 měsíců) | MF: čistý přírůstek za měsíc |
|---|---|---|---|---|---|
| Nízký | 1 % | 12 USD | 1,3 tis. USD | 14 tis. USD | 0,9 tis. USD |
| **Základ** | **1,5 %** | **18 USD** | **2,8 tis. USD** | **31 tis. USD** | **2 tis. USD** |
| Vysoký | 3 % | 30 USD | 9,5 tis. USD | 104 tis. USD | 6,8 tis. USD |

- MF: přepočet podle poměru IAP MF a Hexu (1,44×) a polovina odečtená za kanibalizaci dnešní mapy, která už gemy prodává (kap. 11).
- **Vysoký scénář táhnou velryby:** jeden hráč, který dojde zrychlením na Radnici 15, udělá 5 tis. USD. Proto musí obsah (Radnice 11 až 15) přijít dřív, než první velryby dojdou na strop verze 1 (při stavitelích, VIP a dokupování cca 29. den, kap. 8.2).
- Základ znamená cca +34 % IAP Hexu. Měřit jako ARPDAU před a po jen na iOS a Androidu mimo Play Pass (KONCEPT_OBNOVA_HEXU kap. 6).

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

## 11. Vazba na dnešní mapu MF: náhrada a refund

V MF už existuje systém budov na mapě (`NoxFort/Assets/_Project/Entities/MapBuilding`): Gold Mine, Gem Mine, Stone Mine, Energy Generator, Jeweler, Wall (s talenty), Bestiary, Challenges. Moduly `ConstructionModule`, `UpgradingModule`, `CurrencyGeneratorModule`, `TalentModule` a `Modifiers` jsou dobrý základ pro City V2. Dnešní Gold Mine má 10 levelů, upgrady stojí 240 až 1 080 `HardCurrency` a trvají 2 h až 2 d 8 h, odemyká se podle stage indexu.

**Rozhodnuto 6. 11.:** City V2 **nahradí** dnešní budovy na mapě MF a hráči dostanou refund investic. Dvě paralelní stavební mety nebudou.

**Pravidlo refundu *(návrh, jednoduché)*:**

| Co | Jak |
|---|---|
| Gemy | **100 % `HardCurrency` utracené za stavbu, upgrady a zrychlení nahrazených budov** se vrátí jako gemy (v MF `HardCurrency` = gemy) |
| Startovní Radnice | podle nejvyšší úrovně dnešní budovy na mapě: Radnice = nejvyšší level / 2, zaokrouhleno nahoru, **min. 1, max. 5** (Gold Mine 10 = Radnice 5, Gold Mine 5 = Radnice 3) |
| Budovy na startu | produkční budovy, Sklad a Kasárna na maximu pro startovní Radnici, ostatní od nuly; questy kapitol do startovní Radnice se označí jako splněné bez odměn |
| Komunikace | jedno okno "Mapa se mění na město" se souhrnem refundu, žádná volba hráče |

- Hráč na Radnici 5 přeskočí asi 5 dní tempa (kumulativní den 5,3 v kap. 6.1), zbytek je stejný jako u nového hráče. Gemy z refundu může dát do bundle, stavitelů, VIP nebo zrychlení.
- **Riziko pro tempo:** maxovaný hráč může mít refund v tisících gemů (u Gold Mine 240 až 1 080 za level). Celá verze 1 se dá zrychlit za cca 15 100 gemů. Je to vrácení vlastní investice, ale před releasem vytáhnout z dat rozložení utracené `HardCurrency` na mapě a podle něj potvrdit 100 %.
- **Ztráta produkce měn:** Gold Mine a Gem Mine dnes vyrábí měny. City V2 gemy nevyrábí (jen překážky, questy, achievementy), takže se změní přírůstek gemů hráčům MF. Spočítat z dat, kolik gemů Gem Mine denně dává, a dorovnat přes questy nebo denní odměnu *(návrh)*.
- **Gem sink:** upgrady mapy za `HardCurrency` zmizí; nahrazují je stavitelé, zrychlení, bundle a City VIP (kap. 8).
- Otevřené: co s talenty z Wall (návrh: převést na talentové body Akademie) a jestli Bestiary a Challenges zůstanou ve městě jako vstupy do featur bez upgradů.

## 12. Později (mimo verzi 1, podle designu kap. 4)

- Radnice 11 a výš, víc kusů budov, nové budovy (V2); parametry a hloubka monetizace v kap. 8.3.
- Výroba jednotek a nemocnice, výzkum v Akademii.
- HP budov, obrana, hradby a štíty (až s útoky na města; ve verzi 1 nejsou, proto tu HP chybí).
- VIP úrovně a další výhody (City VIP ve verzi 1 je jedna nabídka, kap. 8.2).
- Síla města jako číslo pro žebříčky, aliance a pomoc se stavbou, návštěvy měst.

## 13. Otevřené otázky

1. **Ceník gemů:** vyřešeno, 60 gemů = 1 USD (5. 11.). Zbývá ověřit, že `HardCurrency` v MF a gemy v Hexu mají stejný ceník.
2. **Mapování surovin:** MF má soft měnu, `HardCurrency`, kameny a další měny; Hex má vlastní. Které z nich jsou jídlo, dřevo, kámen a zlato, nebo zavádíme 4 nové suroviny jen pro město?
3. **Dnešní mapa MF: Rozhodnuto 6. 11., City V2 ji nahradí s refundem.** Zbývá potvrdit pravidlo refundu z kap. 11 (100 % gemů, startovní Radnice max 5), dorovnání produkce Gem Mine a talenty z Wall.
4. **Meta staty v MF a Hexu:** HP a útok čeho přesně (hradba, hrdinové, jednotky Hexu)? Co znamená talentový bod a slot v MF a v Hexu? Na čem se počítá XP ze Svatyně?
5. **Stropy 20 %:** sedí vůči ostatním zdrojům síly? Potřebujeme křivku síly hráče MF a Hexu na D1, D7, D30 (telemetrie), pak doladit procenta za level.
6. **Odměny ze zápasů:** dodá hostitelská hra příjem z kapitoly 7 (škálovaný podle Radnice), a kolik zápasů denně hraje medián aktivního hráče (model počítá 6)?
7. **Gating Radnice v Hexu:** jaké milníky (světy, PvP výhry) odpovídají MF stage 5 až 27?
8. **Stavitel #3 a #4:** cena 300 a 600 gemů, nebo jen přes nabídky. VIP dává stavitelskou frontu navíc jen po dobu VIP *(návrh, kap. 8.2)*.
9. **City VIP a bundle** *(návrh, kap. 8.1 a 8.2)*: potvrdit ceny 60 / 120 / 450 gemů a efekty, a jestli VIP zapnout už ve verzi 1 (návrh: ano, za RC flagem, nahrazuje gem sink mapy MF).
10. **Hloubka monetizace** (kap. 8.3): potvrdit roadmapu Radnice 11 až 25 a nové vrstvy (výzkum, věže, hradby). Kdy přijde Radnice 11 až 15, aby velryby nenarazily na strop verze 1?
