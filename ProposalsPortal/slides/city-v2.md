# City V2: město jako v Clash of Clans
Co nejbližší klon Clash of Clans a Rise of Kingdoms. První verze: stavění, suroviny a upgrady; budovy zvyšují meta staty.
!! I 2027 | první hráči v původním Hexu
!! 2 | stavitelé na start
!! 5 | budov s vlivem na meta staty
---
## Klonujeme ověřenou smyčku, ne art
- Smyčka CoC a RoK drží hráče roky a monetizuje
- Hráči ji **znají**, nemusí se nic učit
- Přebíráme **mechaniky a strukturu**, art a názvy jsou naše
- Jeden modul pro Hex, MF reskiny a strategickou větev
→ `DESIGN_CITY_V2.md`
---
## Verze 1: radnice, stavitelé, sběr, upgrady
- **Radnice** určuje max level ostatních budov
- **Stavitelé:** 2 na start, další za prémiovou měnu
- Farma, pila, lom a důl vyrábí, hráč **sbírá klepnutím**
- Upgrady s časovači, **zrychlení**, sklady, překážky
- Questy kapitol vedou hráče stavbou
→ `DESIGN_CITY_V2.md`
---
## V MF město nahradí dnešní mapu, s refundem
- **Rozhodnuto 6. 11.:** City V2 nahradí Gold Mine, Gem Mine a další budovy na mapě MF
- Refund *(návrh)*: utracená HardCurrency zpět jako gemy, startovní radnice podle nejvyšší budovy (max 5)
- Za gemy: **startovní bundle surovin** (60 gemů) a **City VIP** (450 gemů na 30 dní)
- VIP průměrnému hráči zkrátí cestu na radnici 10 jen z 50 na 47 dní, tempo nerozbije
→ `BALANC_CITY_V2.md`
---
## Hloubka: plné město za 10 až 100 tis. USD
| Obsah | Kdy *(návrh)* | Plné město za gemy |
|---|---|---|
| V1: Radnice 10 | leden 2027 | cca 440 USD |
| Radnice 15 + výzkum, věže, hradby | Q2 2027 | cca 5 tis. USD |
| Radnice 20 | Q4 2027 | cca 20 tis. USD |
| Radnice 25 | 2028 | cca 58 tis. USD |
- Ceny se nemění, hloubku dává obsah. Velryby nesmí narazit na strop V1
→ `BALANC_CITY_V2.md`
---
## Kolik to přinese
- **Průměrný platící hráč** cca 36 USD za 90 dní, cca 100 USD za rok
- Platí 1 až 3 % hráčů města, na každého hráče 0,1 až 0,9 USD měsíčně
- Hex: **1,3 / 2,8 / 9,5 tis. USD měsíčně** (nízký / základ / vysoký), základ +34 % IAP
- MF čistý přírůstek 0,9 / 2 / 6,8 tis. USD měsíčně po kanibalizaci dnešní mapy
→ `BALANC_CITY_V2.md`
---
## Budovy zvyšují meta staty ve hře
| Budova | Stat |
|---|---|
| Kasárna | HP jednotek |
| Kovárna | útok jednotek |
| Akademie | talentové body |
| Svatyně, Tržiště | XP a odměny ze zápasů |
→ `DESIGN_CITY_V2.md`
---
## Jednotky, mapa a boje přijdou později
- **Ve V1 není:** výroba jednotek, globální mapa, boje mezi hráči
- V2: výzkum v akademii, obranné věže, hradby, radnice 11 až 15, VIP úrovně
- V3: globální mapa, útoky na města (nejdřív fake), aliance
- Vše za RC flagem, sociální vrstvy podle SharedGameBackendu
→ `DESIGN_CITY_V2.md`
---
## Co je potřeba rozhodnout
- Roadmapa hloubky: kdy Radnice 11 až 15 a nové vrstvy (vlastník Kubík)
- City V2 nahradí mapu v MF na začátku roku 2027; potvrdit pravidlo refundu a přesný release
- Které meta staty v Hexu a jaké stropy bonusů
- Ceny bundle a City VIP, VIP už ve V1 *(návrh: ano)*
→ `DESIGN_CITY_V2.md`
