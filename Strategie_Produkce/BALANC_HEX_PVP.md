# PvP v Hexu: první nahození čísel

> **Stav:** první nahození, 5. 11. 2026. Všechno se ladí v Remote Config, nic tu není finální. Design a pravidla: `DESIGN_HEX_PVP.md`. Navazuje na `KONCEPT_OBNOVA_HEXU.md` a `DESIGN_CITY_V2.md`.
> **Pro AI agenty:** tohle je číselný doprovod k `DESIGN_HEX_PVP.md`. Když se liší pravidla, platí design dokument; tady jsou jen hodnoty. **Každá hodnota je RC parametr** (prefix `hex_pvp_`), výchozí hodnota je ta v tabulce. Měny a obsah truhel jsou předpoklady, ověřit proti ekonomice Hexapolisu. Simulace v kap. 11 je orientační model, ne predikce.

## 1. Shrnutí: klíčová čísla

| Co | Hodnota |
|---|---|
| Speed | 30 s na tah, 15 tahů na hráče, banka času 4 min na hráče, zápas do cca 8 min |
| Normal | 60 s na tah, 30 tahů na hráče, banka času 15 min na hráče, zápas do cca 30 min |
| Skóre za zápas | výhra 100 + výkon 0 až 50, prohra 20 + výkon 0 až 25, vzdání nebo AFK 0 |
| Násobiče skóre | síla soupeře x1,2 až 1,5, série výher x1,1 až 1,2, Normal x2, bot a ghost x0,5 |
| Max skóre za zápas | Speed 270, Normal 540 (strop pro SGB anti-cheat) |
| ELO | start 1 200, podlaha 800, K 48 (zařazování) / 32 / 24 / 16 (od 1 800) |
| Onboarding | 3 zápasy proti botovi (až 5, když hráč prohrává), bez vlivu na ELO |
| Fallback na bota | po 20 s ve frontě, okno ELO roste ze ±100 na ±300 |
| Ligy (All-out-power) | 5 lig, sezóna = kalendářní měsíc, postup top 10 % (min. 15 reálných zápasů a ELO nad mediánem ligy), sestup 10 / 12 / 15 / 20 % |
| Rozložení lig po 6 měsících (simulace) | Bronz 40 %, Stříbro 32 %, Zlato 18 %, Diamant 7 %, Mistr 2 % |
| Odpojení | 30 s na návrat, pak tah propadá; 2 propadlé tahy po sobě nebo 3 celkem = prohra |
| Monetizace (hypotézy) | PvP úkoly do stávajícího battle passu, předplatné 4,99 USD / měsíc, kosmetika 0,99 až 4,99 USD |

**Dvě zjištění ze simulace, která mění design:**
1. **Kumulativní skóre řadí podle aktivity, ne podle síly.** Párování podle ELO srovná win rate všech hráčů k 50 %, takže měsíční skóre je hlavně počet zápasů (korelace liga a aktivita 0,79, liga a skill 0,07). Proto návrh: do postupu jen hráči s **ELO nad mediánem své ligy** a aspoň 15 reálnými zápasy. Korelace se skillem pak vyskočí na 0,33, se silou na 0,49.
2. **Postup top 10 % a stejný sestup 10 % ve všech ligách dělá ligy stejně velké.** Mistr by dlouhodobě rostl k 20 %. Proto sestup roste s ligou (10 / 12 / 15 / 20 %), Mistr pak drží 2 až 3 %.

## 2. Skóre v zápase

V zápase existují dvě různá čísla:
- **Vítězné body (VB):** rozhodují zápas po limitu tahů. Hráč je vidí během hry.
- **Skóre:** jde do denního, týdenního a měsíčního žebříčku (`DESIGN_HEX_PVP.md`, kap. 5). Počítá se z výsledku a výkonu.

### 2.1 Čas a délka zápasu

Design chce zároveň 30 s na tah, 15 tahů a zápas do 8 minut. Při střídání tahů by to bylo až 15 min (15 x 2 x 30 s). Řešení: **limit na tah plus banka času na celý zápas** jako v šachových hodinách.

| RC parametr | Speed | Normal |
|---|---|---|
| `turn_limit_sec` (max na jeden tah) | 30 | 60 |
| `max_turns` (tahů na hráče) | 15 | 30 |
| `time_bank_sec` (banka na hráče na celý zápas) | 240 | 900 |
| `turn_limit_after_bank_sec` (když banka dojde) | 10 | 15 |
| Průměr na tah, aby banka vyšla | 16 s | 30 s |
| Typická délka zápasu | 5 až 8 min | 15 až 25 min |
| Tvrdý strop délky | cca 10 min | cca 35 min |
| Mapa | 11x11 hexů | 14x14 hexů |

- Čas se odečítá z banky, ale jeden tah nesmí přesáhnout `turn_limit_sec`. Prvních 5 s každého tahu (`turn_free_sec`) se z banky neodečítá, aby rychlé tahy na začátku hry nebyly trestané.
- Když tah vyprší, **tah propadá** (jednotky stojí, hra pokračuje). Propadlý tah bez jediné akce se počítá do AFK pravidla (kap. 9).

### 2.2 Jak se vyhrává

| Podmínka | Výsledek |
|---|---|
| Dobytí hlavního města soupeře | okamžitá výhra |
| Soupeř se vzdá | výhra |
| Soupeř AFK nebo odpojený (2 propadlé tahy po sobě nebo 3 celkem) | výhra |
| Po `max_turns` | výhra hráče s víc VB |
| Shoda VB | rozhoduje: víc měst, víc území, víc zničených jednotek, nakonec vyhrává hráč, který táhl **druhý** |

Remízy nejsou. Sedí to i na SGB, které remízu v PvP nemá.

**Vítězné body po limitu tahů** (`vp_*`):

| Zdroj | VB |
|---|---|
| Vlastní město | 10 |
| Hlavní město (vlastní nebo dobyté) | +5 navíc |
| Úroveň města nad 1 | +2 za úroveň |
| Hex území | 1 |
| Vlastní jednotka na mapě | 1 (veterán 2) |
| Zničená jednotka soupeře | 1 |

Kontrola balancu: na mapě 11x11 má hráč po 15 tazích typicky 3 až 5 měst a 25 až 40 hexů, tedy kolem 80 až 120 VB. Zničené jednotky dávají do 15 % VB, aby se vyplatilo bojovat, ale vyhrávala hlavně expanze.

### 2.3 Skóre do žebříčku

| Složka | Body | RC |
|---|---|---|
| Výhra | +100 | `score_win` |
| Prohra (odměna za odehrání) | +20 | `score_loss` |
| Výkon ve výhře | 0 až 50 | `score_perf_win_max` |
| Výkon v prohře | 0 až 25 | `score_perf_loss_max` |
| Vzdání, AFK, odpojení | 0 | |

**Výkon** se skládá z (součet, strop podle výsledku):

| Složka | Body | Strop |
|---|---|---|
| Dobyté město | 5 za město | 20 |
| Území na konci | 1 za každá 4 % hexů mapy | 10 |
| Zničené jednotky soupeře | 1 za jednotku | 10 |
| Rychlost výhry (jen výhra dobytím) | 10 x zbývající tahy / `max_turns` | 10 |

**Násobiče** (násobí se celé skóre zápasu):

| Násobič | Hodnota | Kdy |
|---|---|---|
| Síla soupeře | x1,2 při ELO soupeře o 50 až 149 vyšším, x1,35 při 150 až 249, x1,5 při 250+ | jen výhra |
| Série výher | x1,1 od 3. výhry v řadě, x1,2 od 5. | jen výhra, série počítá i boty |
| Sub-režim | Speed x1, Normal x2 | vždy |
| Soupeř bot nebo ghost | x0,5 | vždy |
| Denní strop | prvních 20 zápasů za den plně, 21. až 30. x0,5, dál 0 | vždy |

Proč Normal x2: Normal trvá zhruba 2,5x déle než Speed. S x2 dává Speed pořád o něco víc bodů za minutu (cca 16 vs. 12), takže Speed je "grind" režim a Normal "kvalitní" režim, ale Normal není ztráta času.

**Příklady:**

| Situace | Výpočet | Skóre |
|---|---|---|
| Speed, výhra dobytím nad stejně silným, 2 města, 30 % mapy, 4 jednotky, zbývá 5 tahů | 100 + (10 + 7 + 4 + 3) = 124 | 124 |
| Totéž proti soupeři o 180 ELO silnějšímu | 124 x 1,35 | 167 |
| Normal, výhra po limitu tahů, 3. výhra v řadě | (100 + 30) x 1,1 x 2 | 286 |
| Speed, prohra s výkonem 12 | 20 + 12 | 32 |
| Speed, výhra nad botem | 124 x 0,5 | 62 |
| Teoretické maximum | (100 + 50) x 1,5 x 1,2 x 2 | 540 |

Průměrný aktivní hráč (50 % výher, 60 % Speed) udělá kolem **110 až 130 bodů za zápas**. Medián měsíčního skóre aktivního hráče v simulaci: cca 3 000, top 10 % nad 8 000, top 1 % kolem 14 500.

## 3. Rating: ELO

| RC parametr | Hodnota | Pozn. |
|---|---|---|
| `elo_start` | 1 200 | sedí na `DEFAULT_ELO` v SGB |
| `elo_floor` | 800 | pod podlahu nikdo nespadne |
| `elo_scope` | 1 ELO na segment | Speed a Normal sdílí ELO (malá base); interně logovat i stínové ELO per sub-režim |
| `onboarding_bot_matches` | 3, až 5 | 4. a 5. zápas s botem jen když hráč 2 z prvních 3 prohraje |
| `placement_matches` | 10 | prvních 10 reálných zápasů, v profilu "Zařazování 4/10", ELO se ukáže až potom |
| K: zařazování (zápas 1 až 10) | 48 | rychle najít správnou úroveň |
| K: zápas 11 až 30 | 32 | |
| K: zápas 31+ | 24 | |
| K: ELO 1 800+ | 16 | stabilní top žebříčku |
| K: návrat po 30+ dnech | 40 na 5 zápasů | rekalibrace místo decay |
| Decay | žádný | ELO slouží párování, žebříčky dělá skóre, decay nepotřebujeme |
| Bot, ghost, onboarding | ELO se nemění | žádné farmení ELO na botech, žebříček zůstává důvěryhodný |
| Hra s přáteli | ELO se nemění | mimo žebříčky (design kap. 4) |
| Stejný soupeř | max 3 rankované zápasy za 24 h, další bez ELO a skóre | proti win tradingu |
| Změna ligy (All-out-power) | `ELO = 1 200 + 0,5 x (ELO − 1 200)` | návrh na otevřenou otázku z designu; postoupivší hráč je v nové lize slabší, než říká staré ELO |

Vzorec: očekávání `E = 1 / (1 + 10^((ELO_soupeře − ELO_hráče) / 400))`, změna `K x (výsledek − E)`, zaokrouhleno.

**Příklady (změna ELO za výhru / prohru):**

| Soupeř | K 48 | K 32 | K 24 | K 16 |
|---|---|---|---|---|
| stejně silný | +24 / −24 | +16 / −16 | +12 / −12 | +8 / −8 |
| o 200 silnější (E = 24 %) | +36 / −12 | +24 / −8 | +18 / −6 | +12 / −4 |
| o 200 slabší | +12 / −36 | +8 / −24 | +6 / −18 | +4 / −12 |
| o 400 silnější | +44 / −4 | +29 / −3 | +22 / −2 | +15 / −1 |

Čtení: hráč po zařazování (K 24), který vyhraje 6 z 10 zápasů proti stejně silným, jde o +24 ELO. Rozptyl ELO po 3 měsících (simulace, hráči s 10+ zápasy): p10 cca 1 000, medián 1 200, p90 cca 1 400, top 1 % nad 1 550. Hranice K 16 na 1 800 se tak týká jen úplné špičky, to je záměr.

## 4. Trofeje a ligové body

**Žádná třetí měna navíc.** Design už má dvě čísla: skóre (žebříčky) a ELO (párování, viditelné v profilu). Roli "trofejí" z Clash Royale hraje **měsíční skóre**, podle kterého se postupuje v lize. Třetí číslo by hráče jen mátlo.

| Výsledek | Skóre | ELO |
|---|---|---|
| Výhra | 100 + výkon, s násobiči | +K x (1 − E) |
| Prohra | 20 + výkon (max 25) | −K x E |
| Remíza | neexistuje (tiebreak) | |
| Vzdání | 0 | plná prohra |
| Odpojení, AFK | 0 | plná prohra |
| Výhra díky vzdání nebo AFK soupeře | 100 + výkon v okamžiku konce, výkon minimálně 25 | plná výhra |
| Série výher | x1,1 od 3 výher, x1,2 od 5 | bez vlivu |

## 5. Ligy v All-out-power

| Liga | Pro koho | Start (zařazení podle PowerProgress) | Postup | Sestup |
|---|---|---|---|---|
| Bronz | nováčci | spodních 50 % síly | top 10 % | není |
| Stříbro | early mid game | 50 až 80 % | top 10 % | spodních 10 % |
| Zlato | mid game | 80 až 95 % | top 10 % | spodních 12 % |
| Diamant | late game | horních 5 % | top 10 % | spodních 15 % |
| Mistr | špička | jen postupem | | spodních 20 % |

- **Sezóna = kalendářní měsíc** (UTC), stejně jako měsíční perioda v SGB (`YYYY-MM`). Když launch přijde po 15. lednu, první vyhodnocení až na konci února.
- **Zařazení nových hráčů** podle percentilu PowerProgress mezi aktivními hráči All-out-power (při launchi snapshot všech aktivních hráčů Hexapolisu). Bez zařazení by v simulaci zůstalo 59 % hráčů v Bronzu i po roce a nováčci by naráželi na vylevelované hráče.
- **Postup:** top 10 % aktivních hráčů ligy (aspoň 1 reálný zápas) podle měsíčního skóre. Podmínky: **aspoň 15 reálných zápasů za měsíc** (`promo_min_matches`) a **ELO aspoň medián ligy** (`promo_elo_gate`). Nevyužité místo zůstává prázdné.
- **Sestup:** spodní procento aktivních hráčů ligy podle tabulky. Neaktivní hráč (0 zápasů) sestupuje po 2 měsících o jednu ligu (design kap. 6).
- **Reset na konci sezóny:** měsíční skóre na 0 (dělá SGB perioda), liga ±1, ELO soft reset jen hráčům, kteří změnili ligu. Postup i sestup max o 1 ligu za sezónu.
- **Slučování malých lig:** když má liga méně než 200 aktivních hráčů za týden (`league_merge_min_weekly`), párování se slučuje se sousední ligou (nejdřív Diamant a Mistr). Žebříčky a odměny zůstávají per liga.

**Ligové odměny na konci sezóny** (k odměnám z žebříčků v kap. 7):

| Liga | Konec sezóny | Násobič měn a surovin v odměnách z žebříčků |
|---|---|---|
| Bronz | 300 surovin | x1,0 |
| Stříbro | truhla | x1,2 |
| Zlato | truhla + 20 gemů | x1,5 |
| Diamant | velká truhla + 50 gemů + rámeček Diamant | x2,0 |
| Mistr | prémiová truhla + 100 gemů + rámeček a titul Mistr (na měsíc) | x2,5 |

Gemy v odměnách se nenásobí, násobí se jen soft měna a suroviny.

## 6. Párování

| Čekání | Okno ELO | Okno síly (jen All-out-power, PowerProgress) |
|---|---|---|
| 0 s | ±100 | ±15 % |
| 10 s | ±200 | ±25 % |
| 20 s | ±300 | ±30 % |
| po 20 s | bot nebo ghost s hráčským profilem | |

- Okno roste o 10 ELO za sekundu, to je přesně současný vzorec v SGB (`ELO_BASE_WINDOW` 100, `ELO_EXPAND_PER_SEC` 10). Stačí přidat strop 300 a fallback na bota ve 20 s (`bot_fallback_sec`) místo současného vypadnutí z fronty po 120 s.
- **Bot nebo ghost** dostane ELO hráče − 50 a sílu (v All-out-power) hráče − 5 %, aby hráč vyhrával zhruba 60 % bot zápasů. Profil (jméno, avatar, rámeček) z poolu neaktivních reálných profilů nebo generovaný.
- **Onboarding boti:** 1. zápas cílený na výhru hráče (cca 90 %), 2. a 3. zápas cca 70 %, 4. a 5. zápas cca 60 %. Mapa Speed, Skill only preset.
- **Vzdálenost od posledního soupeře:** stejného soupeře znovu až po 2 jiných zápasech, pokud fronta dovolí.
- **Kolik front unese base?** Výpočet: 3 zápasy na PvP hráče denně, 10 % denního provozu ve špičkové hodině, polovina fronty v okně ELO, fallback ve 20 s. Podíl zápasů s reálným soupeřem:

| PvP DAU | 12 front (2 sub-režimy x Skill + 5 lig) | 6 front (sub-režimy sloučené) | 4 fronty (+ ligy sloučené do 3) | 2 fronty (jen segmenty) |
|---|---|---|---|---|
| 1 000 | 13 % | 23 % | 32 % | 51 % |
| 3 000 | 32 % | 51 % | 63 % | 83 % |
| 10 000 | 67 % | 86 % | 93 % | 99 % |

  Závěr: při launchi **párovat Speed a Normal přes jednu frontu ve dvou krocích** (nejdřív stejný sub-režim, po 10 s i druhý, hráč dostane režim toho, kdo čekal déle) a slučovat ligy, dokud PvP DAU nepřeleze cca 5 000. Design to už jako možnost má (kap. 14).

## 7. Odměny, truhly, achievementy, žebříčky

**Předpoklady k měnám:** Hexapolis má soft měnu (mince) a hard měnu (gemy), PvP přidává **suroviny do City V2** (design kap. 8). Kotva hodnoty: **60 gemů = 1 USD** (náš ceník, potvrzeno 5. 11.), tedy 300 gemů = 4,99 USD. Ve Skill only truhly obsahují suroviny, mince a fragmenty kosmetiky; v All-out-power navíc fragmenty jednotek a talentů. PvP nesmí stát energii.

### 7.1 Truhly

| Truhla | Mince | Suroviny City V2 | Gemy | Fragmenty |
|---|---|---|---|---|
| Malá | 200 | 50 | 10% šance na 5 | 1 |
| Truhla | 500 | 150 | 10 | 3 |
| Velká | 1 500 | 400 | 30 | 8 |
| Prémiová | 4 000 | 1 000 | 100 | 20 + šance na kosmetiku |

### 7.2 Za zápasy a denní a týdenní úkoly

| Odměna | Obsah | Strop |
|---|---|---|
| Výhra | 30 mincí + 10 surovin | prvních 20 zápasů za den |
| Prohra | 10 mincí + 5 surovin | prvních 20 zápasů za den |
| První výhra dne | malá truhla | 1 za den a segment |
| 3 zápasy za den | 50 surovin | 1 za den |
| Týdně: 15 zápasů | truhla | 1 za týden |
| Týdně: 5 výher v Normal | truhla | 1 za týden |

Bot zápasy se počítají do odměn i úkolů (design kap. 4).

### 7.3 Žebříčky

- **Žebříčky:** Skill only 1, All-out-power 5 (per liga), každý denní, týdenní a měsíční. Celkem 18 period žebříčků na SGB. V UI top 100 (SGB vrací max 100 na dotaz) plus "kolem mě" a přátelé.
- **Způsobilost na top 10** (pozice 1 až 10 jen z reálných zápasů, design kap. 4): v období aspoň 3 (denní), 10 (týdenní), 25 (měsíční) reálných zápasů a reálné zápasy tvoří aspoň 50 % odehraných. Nezpůsobilý hráč se v top 10 přeskočí a dostane odměnu za top 10 %.

| Pořadí | Denní | Týdenní | Měsíční |
|---|---|---|---|
| 1. | truhla + 50 gemů | velká truhla + 100 gemů + týdenní rámeček | prémiová truhla + 300 gemů + exkluzivní skin + titul |
| 2. až 3. | truhla + 20 gemů | velká truhla + 50 gemů | prémiová truhla + 150 gemů + titul |
| 4. až 10. | malá truhla + 10 gemů | truhla + 20 gemů | velká truhla + 50 gemů |
| top 10 % | 100 surovin | truhla | truhla |
| aspoň 1 zápas | 30 surovin | 200 surovin | 500 surovin |

Kontrola rozpočtu gemů: denní top 10 rozdá 160 gemů na žebříček, při 6 žebříčcích 960 gemů denně, tedy cca 29 000 gemů měsíčně pro celou base (cca 480 USD hodnoty, žádné riziko). Průměrný aktivní hráč (5 zápasů týdně) by měl z PvP dostat kolem **60 až 100 gemů měsíčně**, hráč v top 10 % kolem 300 až 500. Ladit přes `reward_*` podle reálné ekonomiky.

### 7.4 Achievementy

Umístění (jen reálné zápasy, design kap. 7), stupně per období a segment:

| Achievement | Denní | Týdenní | Měsíční |
|---|---|---|---|
| Top 10 | 20 gemů | 50 gemů | 100 gemů |
| Top 3 | 30 gemů | 75 gemů | 150 gemů |
| Stříbro (2. místo) | 40 gemů | 100 gemů | 200 gemů |
| Vítěz | 50 gemů + odznak | 150 gemů + odznak | 300 gemů + trofej do města |

Achievement se vyplácí jednou (první dosažení stupně), pak už jen odznak s počítadlem.

**Série:**

| Série | Kroky | Odměna za krok |
|---|---|---|
| Denní top 10 | 3, 7, 14 dní | 50, 150, 300 gemů |
| Týdenní top 10 | 2, 3, 4, 8 týdnů | 100, 150, 250, 500 gemů |
| Měsíční top 10 | 2, 3, 6 měsíců | 300, 500, 1 000 gemů + trofej |

**Progresní achievementy** *(návrh, nad rámec designu, pro hráče mimo top 10)*: reálné výhry 10 / 50 / 200 / 1 000, dobytí hlavního města 5 / 25 / 100, výhry ve Speed do 6 min 10 / 50. Odměny 20 až 200 gemů nebo kosmetika.

## 8. Napojení na City V2

- PvP je druhý zdroj surovin vedle kampaně. Aktivní PvP hráč (cca 22 zápasů měsíčně) dostane ze zápasů, úkolů a žebříčků kolem **1 500 až 2 500 surovin měsíčně**. Dorovnat s rychlostí upgradu budov v `DESIGN_CITY_V2.md`: cíl je, aby PvP pokrylo zhruba 30 až 40 % surovin aktivního hráče.
- Meta staty z města (kasárna, kovárna max +20 %) se projeví jen v All-out-power. Při +20 % HP i útoku je rozdíl mezi novým a maxovaným městem velký, proto okno síly v párování (kap. 6) a ligy.

## 9. Tresty: odpojení, AFK, vzdání

| RC parametr | Hodnota |
|---|---|
| `reconnect_window_sec` | 30 (čas tahu mezitím běží) |
| Propadlý tah | tah bez akce, který vypršel, nebo tah při odpojení |
| `afk_forfeit_consecutive` | 2 propadlé tahy po sobě = prohra |
| `afk_forfeit_total` | 3 propadlé tahy celkem = prohra |
| Vzdání | kdykoli; prohra, skóre 0, plná ztráta ELO |
| Opuštění | AFK prohra nebo vzdání do 2. tahu (Speed) nebo 3. tahu (Normal) |
| Ochrana proti pádu aplikace | první odpojení za den s návratem do 30 s bez trestu |

**Zákaz rankovaných zápasů za opouštění** (počítá se za posledních 24 h):

| Opuštění za 24 h | Zákaz |
|---|---|
| 2 | 5 min |
| 3 | 30 min |
| 5+ | 24 h |

Hra s přáteli trest nemá. Zákaz se ukáže s odpočtem a vysvětlením.

## 10. Monetizace (hypotézy)

| Nabídka | Cena (hypotéza) | Segment | Pozn. |
|---|---|---|---|
| PvP úkoly ve **stávajícím battle passu** | v ceně passu | oba | první krok, nefragmentovat; vlastní PvP pass až při podílu DAU v PvP nad 25 % |
| Vlastní PvP pass (měsíční sezóna, 30 úrovní) | 4,99 USD, premium+ 9,99 USD | oba | body pasu: výhra 10, prohra 4, denní úkol 20 |
| Předplatné (statistiky, replay, bez reklam, 1 kosmetika měsíčně) | 4,99 USD / měsíc | oba | Davidův ověřovací signál |
| Skin jednotky | 1,99 až 4,99 USD (120 až 300 gemů) | oba | bez vlivu na výsledek |
| Rámeček, emote balík | 0,99 až 2,99 USD | oba | |
| Starter PvP balík po onboardingu | 1,99 USD jednorázově | All-out-power | fragmenty jednotek + suroviny |
| Nabídka po postupu do ligy | 4,99 USD, 24 h | All-out-power | fragmenty + zrychlení města |
| Rewarded reklama: zdvojení první denní truhly | max 3x denně | oba | jen mimo zápas |

- **Google Play Pass:** Hexapolis je v Play Passu na Androidu. Reklamy tam nahrazují tickety a předplatitelé mají passy a nabídky zdarma, gemy si nekoupí. Monetizaci PvP proto měřit zvlášť pro iOS, Android mimo Play Pass a Play Pass.
- **Realita čísel:** při 10 000 PvP MAU a 2% konverzi na pass za 4,99 USD je to cca 1 000 USD měsíčně hrubého. Hlavní finanční efekt PvP čekáme přes retenci a útratu v All-out-power (jednotky, talenty, City V2), ne přes pass samotný. Hexapolis dnes dělá cca 15 000 USD měsíčně.

## 11. Simulace (sanity check)

**Model** (Python, numpy, skript v pracovním adresáři, ne v repu): 10 000 hráčů All-out-power při launchi, +1 500 nových hráčů měsíčně, odchod 40 / 20 / 8 % měsíčně podle aktivity. Každý hráč má skill a meta sílu (síla roste o 0,08 sd měsíčně, platící 4 % hráčů rychleji), aktivitu lognormálně s mediánem 18 zápasů měsíčně. Párování uvnitř ligy podle ELO, výsledek podle rozdílu skutečné síly. Skóre, K schéma, bot fallback, postup a sestup přesně podle tohoto dokumentu. 6 a 12 až 24 měsíců.

**Rozložení lig po měsících (zvolené nastavení: zařazení podle síly, postup top 10 % s ELO podmínkou, sestup 10 / 12 / 15 / 20 %):**

| Konec měsíce | Hráčů | Bronz | Stříbro | Zlato | Diamant | Mistr |
|---|---|---|---|---|---|---|
| 1 (leden) | 8 359 | 47,2 % | 31,2 % | 15,5 % | 5,5 % | 0,6 % |
| 2 | 8 330 | 44,8 % | 31,8 % | 16,3 % | 6,0 % | 1,0 % |
| 3 | 8 336 | 43,1 % | 32,5 % | 16,7 % | 6,4 % | 1,3 % |
| 4 | 8 422 | 41,6 % | 32,6 % | 17,4 % | 6,8 % | 1,6 % |
| 5 | 8 601 | 40,9 % | 32,4 % | 17,8 % | 7,0 % | 1,8 % |
| 6 (červen) | 8 655 | 40,3 % | 32,3 % | 18,2 % | 7,2 % | 2,0 % |

**Porovnání variant (stav po 12 až 24 měsících):**

| Varianta | Bronz | Stříbro | Zlato | Diamant | Mistr | Korelace liga a skill / aktivita / síla |
|---|---|---|---|---|---|---|
| Design doslova: top 10 % podle skóre, sestup 10 % všude, 12 m | 38,6 % | 32,0 % | 17,9 % | 7,9 % | 3,6 % a roste | 0,06 / 0,83 / 0,22 |
| ELO podmínka, sestup 10 % všude, 24 m | 41,5 % | 30,4 % | 16,5 % | 7,6 % | 4,1 % a roste | 0,35 / 0,59 / 0,49 |
| Bez zařazení podle síly, 12 m | 59,0 % | 29,4 % | 8,9 % | 2,2 % | 0,4 % | 0,08 / 0,78 / 0,12 |
| Bez ELO podmínky, sestup 10 / 15 / 20 / 30 %, 12 m | 38,9 % | 35,2 % | 17,6 % | 6,6 % | 1,8 % | 0,09 / 0,84 / 0,21 |
| **Zvoleno: ELO podmínka, sestup 10 / 12 / 15 / 20 %, 24 m** | 41,6 % | 32,7 % | 16,6 % | 6,7 % | **2,4 %** | **0,34 / 0,59 / 0,49** |
| Malá base (3 000 + 500 měsíčně), 6 m | 41,0 % | 32,4 % | 17,8 % | 7,0 % | 1,8 % | 0,33 / 0,56 / 0,49 |

**Skill only (jeden žebříček, 6 měsíců):** ELO hráčů s 10+ zápasy p1 830, p10 980, p25 1 090, medián 1 200, p75 1 310, p90 1 410, p99 1 615. Korelace ELO a skutečného skillu u hráčů s 30+ zápasy 0,96: K schéma ELO konverguje dobře.

**Co z toho plyne:**
- Mistr 2 až 3 % a Diamant kolem 7 % je zdravá špička. Rozložení se stabilizuje po 4 až 6 měsících, malá base na tvar nemá vliv.
- Aktivita bude vždycky hlavní složka měsíčního skóre (to je u kumulativních žebříčků normální a pro retenci žádoucí). ELO podmínka zajistí, že nahoru nejdou slabí grindeři.
- Simulace nemodeluje souběžnost hráčů ve frontě. Podíl bot zápasů řeší výpočet v kap. 6, ne tahle tabulka.

## 12. Co potřebuje SharedGameBackend

Kontrola proti současnému kódu SGB (`src/services/pvp`, `src/services/leaderboards`):

| Potřeba | Stav v SGB | Co doplnit |
|---|---|---|
| Kumulativní skóre za období | žebříček drží **nejlepší** skóre za periodu (`applyScore`) | režim součtu (`aggregate: sum`) nebo S2S increment |
| Anti-cheat limity | min, max, max_delta, podání za minutu, s2s_only, auto_flag (CODE-71 hotové) | nastavit: max_delta 540, max 1 podání za minutu na hráče, `s2s_only: true` (skóre posílá match server, ne klient) |
| K schéma | pevné K 32 | K podle počtu zápasů a ELO |
| Timeout tahu | vypršení tahu = prohra celého zápasu | tah propadá, AFK pravidlo 2 / 3, banka času |
| Fronty | klíč fronty: mód, typ mapy, časový koš; 30 s i 60 s padnou do stejného koše 60 | přidat sub-režim a ligu do klíče, nebo záměrně sloučit (kap. 6) |
| Fallback | fronta vyprší po 120 s | bot ve 20 s, okno ELO strop 300 |
| Remízy | nejsou | sedí, tiebreak řeší hra |
| Segmenty | módy `fairfield` a `all_out_war` | předpoklad: `fairfield` = Skill only, `all_out_war` = All-out-power, potvrdit |

## 13. KPI pro ladění

| KPI | Cíl | Když ne, ladit |
|---|---|---|
| Podíl zápasů s reálným soupeřem | 60 %+ do konce ledna, 80 %+ v únoru | slučování front a lig, `bot_fallback_sec` |
| Medián čekání ve frontě | do 15 s | okno ELO |
| Délka zápasu | Speed 5 až 8 min, Normal 15 až 25 min | `time_bank_sec`, velikost mapy |
| Podíl zápasů rozhodnutých po limitu tahů | 30 až 60 % | nad 70 %: víc tahů nebo menší mapa; pod 20 %: méně tahů |
| Win rate hráče, který táhne první | 47 až 53 % | startovní pozice, tiebreak |
| Win rate presetu národa (Skill only) | pod 55 % | staty presetu |
| Vzdání + AFK | pod 10 % zápasů | tresty, délka zápasu |
| Onboarding: hráčů, kteří po botech odehrají 1. reálný zápas | 70 %+ | obtížnost botů |
| Rozložení lig po 3 měsících | Mistr 1 až 3 %, Diamant 5 až 8 %, Bronz do 50 % | sestupová procenta |
| Rozptyl ELO (p10 až p90) | cca 1 000 až 1 400 | K schéma |
| Zápasů na PvP hráče týdně | 5+ | odměny za zápasy, úkoly |
| Podíl DAU v PvP | 25 %+ | design kap. 12 |
| Gemy z PvP na aktivního hráče měsíčně | 60 až 100 | `reward_*` |

## 14. Otevřené otázky

1. **Měny a hodnota gemu:** potvrdit názvy měn v původním Hexapolisu a obsah truhel. Kotva ceny je vyřešená: 60 gemů = 1 USD (5. 11.).
2. **Banka času:** souhlasí David s řešením 30 s na tah + banka 4 min (Speed), aby platilo "do 8 min"? Alternativa: 15 tahů celkem, ne na hráče.
3. **ELO podmínka postupu:** je to odchylka od "top 10 % postupuje" z designu. Přijmout, nebo nechat čisté skóre a smířit se s ligami podle aktivity?
4. **Sestup rostoucí s ligou** (10 / 12 / 15 / 20 %) místo 10 % všude. Text designu "Mistr bez sestupu pod top 50 %" chápeme jako ochranu horní poloviny Mistra; při 20% sestupu to platí automaticky.
5. **Sloučení Speed a Normal do jedné fronty při launchi:** ano, dokud PvP DAU nebude kolem 5 000?
6. **Normal x2:** držet, nebo dát Normal vyšší váhu, aby se nevyplácelo grindovat Speed?
7. **Odměny ze Skill only:** smí dávat suroviny do City V2, které pak posílí hráče v All-out-power? (Výhoda není koupená, ale přelévá se mezi segmenty.)
8. **SGB práce z kap. 12:** kdo udělá součtový režim žebříčku, K schéma a propadání tahů do 11. 12.
9. **Pool profilů pro boty:** generované, nebo neaktivní reálné profily (GDPR, souhlas)?
