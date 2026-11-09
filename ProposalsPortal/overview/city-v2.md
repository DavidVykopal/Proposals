## Shrnutí
City V2 je co nejbližší klon mechanik Clash of Clans a Rise of Kingdoms: radnice, stavitelé, produkční budovy se sběrem, sklady a upgrady s časovači. Verze 1 obsahuje jen vlastní město. Výroba jednotek, globální mapa a boje mezi hráči přijdou v dalších verzích. Budovy jako kasárna, kovárna nebo akademie zvyšují meta staty ve hře.

Modul vyvíjíme jednou v Mecha Fortress jako staging a pak ho importujeme do dalších her. V Hexapolisu bude v testu a připravený do 11. 12. 2026 za RC flagem, hráči ho dostanou v lednu 2027. V MF City V2 nahradí dnešní budovy na mapě (Gold Mine, Gem Mine a další) a hráči dostanou refund investic (rozhodnuto 6. 11.). Za gemy si hráč koupí startovní bundle surovin a City VIP. Klonujeme mechaniky a strukturu, art, názvy a UI jsou naše.

## Výhody
- **Ověřená smyčka:** mechaniky CoC a RoK drží hráče roky a monetizují, nemusíme je vymýšlet.
- **Hráči ji znají,** radnici, stavitele a sběr pochopí bez učení.
- **Jeden modul pro všechny hry:** MF reskiny, Hexapolis, Hexapolis 2 i strategická větev, vývoj se platí jednou.
- **Nové monetizační sinky:** zrychlení, další stavitelé, startovní bundle surovin, dekorace a City VIP (návrh 450 gemů na 30 dní: o 15 % rychlejší stavby, stavitelská fronta navíc, denní zrychlení zdarma).
- **Jedna stavební meta v MF:** město nahradí dnešní mapu na začátku roku 2027, žádné dvě paralelní mety.
- **Hloubka monetizace bez stropu pro velryby:** plné město za gemy cca 20 tis. USD na Radnici 20 a 58 tis. na Radnici 25 *(návrh 9. 11.)*, průměrný platící hráč cca 36 USD za 90 dní.
- **Dává hloubku mety mimo zápas,** kterou MF ani Hex dnes nemají, a krmí PvP All-out-power.

## Nevýhody
- Laťka CoC a RoK je vysoká, mají roky obsahu, naše V1 bude malá.
- Meta staty zasahují do balancu PvE i PvP All-out-power.
- Ekonomika se ladí ve dvou hrách naráz (MF a Hex) a vyžaduje config per titul.
- Sociální část (globální mapa, útoky, aliance), která nese soutěžní útratu, přijde až ve V3 od Q2 2027.
- Náhrada mapy v MF znamená refund investic a ztrátu produkce dnešního Gem Mine, obojí je potřeba spočítat z dat.
- Verze 1 má hloubku jen cca 440 USD; cíl 10 až 100 tis. USD vyžaduje další verze (Radnice 11 až 25, výzkum, věže, hradby), tedy další vývoj v roce 2027.

## Rizika
| Riziko | Pravděpodobnost | Dopad | Jak ho snížíme |
|---|---|---|---|
| Termín (implementace do 11. 12., hráči v lednu) při běžícím live ops Q4 | vysoká | vysoká | malá V1 (méně budov, víc levelů), vše za RC flagem, release po procentech |
| Meta staty rozbijí balanc PvE nebo PvP | střední | střední | hodnoty v remote configu, strop bonusů, telemetrie; Skill only meta ignoruje |
| Import do starého Hexapolisu narazí na technické problémy | střední | vysoká | modul jen přes kontrakt vstupů a výstupů, ověřit při CODE-65 |
| V1 bez sociální vrstvy nezlepší retenci ani monetizaci | střední | střední | A/B test s City a bez přes Firebased, rychlá V2 podle dat |
| Klon působí jako převzatý obsah | nízká | střední | vlastní art, názvy a UI, klonujeme jen mechaniky |
| Refund z mapy MF rozhodí tempo nebo příjem gemů | střední | střední | návrh: 100 % utracené HardCurrency zpět jako gemy, startovní Radnice max 5; před releasem ověřit z dat |
| Velryby dojdou na strop verze 1 dřív, než přijde Radnice 11+ | střední | střední | Radnice 11 až 15 co nejdřív po lednu; strop V1 při plném nákupu cca 29. den |
| City VIP zkrátí obsah | nízká | střední | průměrnému hráči VIP zkrátí cestu na Radnici 10 jen z 50 na 47 dní, strop kolem 29. dne pro platící hráče, efekty v RC |

## Co nám to přinese
- City V2 verze 1 v původním Hexapolisu u hráčů v lednu 2027: radnice, 2 stavitelé na start, 4 produkční budovy, sklad, 5 budov s meta staty, dekorace, questy.
- Data pro gate Hexapolis 2: podíl DAU v City, D7 a D30 s City proti bez, konverze na zrychlení a stavitele.
- Hotový modul pro reskiny MF od února 2027, náhradu mapy v MF a pro strategickou větev.
- Srovnání s referencí MF (D1 26,5 %, D7 10,1 %, D30 4,2 %), cíl D7 a D30 nahoru bez poklesu D1.
- Výnos v Hexu odhadem 1,3 až 9,5 tis. USD měsíčně (základ 2,8 tis., +34 % IAP), v MF čistě 0,9 až 6,8 tis. USD měsíčně *(odhad, `BALANC_CITY_V2.md` kap. 8.3)*.
- Základ pro V2 (výzkum, Radnice 11+, výroba jednotek) a V3 (globální mapa, útoky, aliance) v roce 2027.

→ `DESIGN_CITY_V2.md`
