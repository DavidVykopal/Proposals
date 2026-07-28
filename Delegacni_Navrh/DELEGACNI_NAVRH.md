# Delegační návrh — NOXGAMES / indie tým 15 lidí

> Pracovní dokument. Návrh struktury kompletně nezávislého (indie) týmu o 15 lidech,
> včetně delegace rozhodování, fixních platů, měsíčních výkonnostních bonusů a provizí ze sales.
> Stav: **první draft k diskuzi** - čísla jsou orientační a čekají na kalibraci.

---

## 1. Principy návrhu

1. **Malý tým = ploché vedení.** Maximálně 2 úrovně: studio lead a 3 leadi (tech, art, produkce). Žádný middle management navíc.
2. **Každá oblast má jednoho vlastníka.** Kdo oblast vlastní, rozhoduje v ní bez eskalace až do definovaného limitu.
3. **Plat je fixní a předvídatelný, bonus je za výkon.** Nikdo nehádá, kolik dostane - pravidla bonusů jsou veřejná uvnitř týmu.
4. **Sales je motivovaný z výsledku, ne z aktivity.** Provize se počítá ze zisku dealu, ne z obratu, aby se nevyplácely ztrátové zakázky.
5. **Leady může nosit kdokoliv.** 5% provize za sehnaný lead není vázaná na roli - programátor, který přivede klienta, ji dostane taky.

---

## 2. Struktura týmu (15 lidí)

```
Studio lead (David)
├── Producer ................ delivery, roadmapa, priority
├── Tech lead ............... architektura, code review, odhady
│   ├── Gameplay dev 1
│   ├── Gameplay dev 2
│   ├── Backend / liveops dev
│   └── Playables / H5 dev
├── Art lead ................ vizuální směr, pipeline, outsourcing
│   ├── 2D / UI artist
│   ├── 3D artist
│   └── VFX / animátor
├── Game designer ........... design, ekonomika hry, balance
├── QA / analytik ........... testování, data, AB testy
├── Marketing / UA .......... kampaně, kreativy, ASO
└── Sales / BizDev .......... B2B dealy (playables, zakázky)
```

Počet: 1 + 1 + 1 + 4 + 1 + 3 + 1 + 1 + 1 + 1 = **15**

Poznámky:

- Producer a studio lead nejsou totéž: studio lead drží vizi, finance a finální slovo, producer drží každodenní delivery. Tohle je hlavní delegační krok - bez něj visí denní provoz na majiteli.
- Playables/H5 dev je zároveň hlavní kapacita pro B2B zakázky, které nosí sales.
- QA a analytik v jedné osobě funguje do velikosti ~2 souběžných projektů, pak se role dělí.

---

## 3. Delegace rozhodování

| Rozhodnutí | Vlastní | Bez eskalace do | Eskalace na |
|---|---|---|---|
| Denní priority a sprint | Producer | rámec schválené roadmapy | Studio lead |
| Technické řešení, stack, refactor | Tech lead | 5 dní práce navíc | Producer + studio lead |
| Vizuální směr, outsourcing artu | Art lead | 30 000 Kč / měsíc | Studio lead |
| Game design změny | Game designer | změny bez dopadu na monetizaci | Studio lead |
| UA rozpočet | Marketing | schválený měsíční budget | Studio lead |
| Cenotvorba B2B nabídek | Sales | marže min. 40 % | Studio lead |
| Nábor, platy, ukončení | Studio lead | - | - |
| Roadmapa, nové projekty, finance | Studio lead | - | - |

Pravidlo: co není v tabulce, rozhoduje vlastník nejbližší oblasti. Eskalace je výjimka, ne default.

---

## 4. Fixní platy (orientační, hrubá mzda / měsíc, CZK)

Čísla vycházejí z českého game-dev trhu, kalibrovat podle regionu a seniority konkrétních lidí.

| Role | Junior | Medior | Senior / Lead |
|---|---|---|---|
| Producer | - | 65 000 | 85 000 - 110 000 |
| Tech lead | - | - | 110 000 - 140 000 |
| Programátor | 45 000 - 60 000 | 60 000 - 85 000 | 85 000 - 115 000 |
| Art lead | - | - | 85 000 - 110 000 |
| Artist (2D/3D/VFX) | 40 000 - 55 000 | 55 000 - 75 000 | 75 000 - 95 000 |
| Game designer | 45 000 - 60 000 | 60 000 - 80 000 | 80 000 - 100 000 |
| QA / analytik | 40 000 - 50 000 | 50 000 - 65 000 | 65 000 - 80 000 |
| Marketing / UA | 45 000 - 60 000 | 60 000 - 80 000 | 80 000 - 100 000 |
| Sales / BizDev | 40 000 - 50 000 (základ) | 50 000 - 65 000 (základ) | 65 000 - 80 000 (základ) |

Zásady:

- Platová pásma jsou interní, ale **pravidla postupu mezi pásmy jsou veřejná** (co musí člověk umět/dodat pro posun).
- Revize platů 1x ročně + mimořádně při změně role.
- Sales má záměrně nižší fix - hlavní příjem má z provizí (viz kap. 6).

---

## 5. Měsíční výkonnostní bonusy

Bonus je **0 - 15 % fixního platu měsíčně**, skládá se ze dvou složek:

| Složka | Váha | Kdo hodnotí | Podle čeho |
|---|---|---|---|
| Týmová | 60 % bonusu | automaticky | splnění milestone/sprint cílů měsíce (dodáno vs. plán) |
| Osobní | 40 % bonusu | přímý lead | kvalita, spolehlivost, iniciativa - krátké písemné zdůvodnění |

Pravidla:

1. Cíle měsíce se definují **předem** (první pracovní den měsíce), ne zpětně.
2. Týmová složka je binární po cílech: každý splněný cíl = poměrná část. Žádné "skoro hotovo".
3. Osobní složku lead zdůvodňuje jednou větou - transparentnost brání pocitu protekce.
4. Bonus leadi dostávají podle výsledků svého úseku, producer podle delivery celého studia.
5. Vyplácí se s výplatou za daný měsíc, žádné odkládání.

Alternativa k diskuzi: místo měsíčního cyklu kvartální bonus s vyšším stropem (0 - 25 %). Měsíční cyklus víc motivuje, ale stojí víc administrativy.

---

## 6. Provize ze sales dealů (B2B zakázky)

| Role v dealu | Provize | Z čeho |
|---|---|---|
| Salesman, který deal uzavřel | **10 %** | ze zisku offeru |
| Člověk, který sehnal lead | **5 %** | ze zisku offeru |

Pravidla:

1. **Zisk offeru** = fakturovaná částka minus přímé náklady (odpracované hodiny × interní sazba, licence, outsourcing). Definici zisku zveřejnit předem, aby se o ní nediskutovalo po dealu.
2. **Lead může přinést kdokoliv** z týmu, 5 % není vázáno na sales roli. Pokud salesman lead sám sehnal i uzavřel, bere 15 %.
3. Provize se vyplácí **po zaplacení faktury klientem**, ne po podpisu.
4. U opakovaných zakázek od stejného klienta: provize v plné výši z prvního dealu, z navazujících dealů 50 % sazby po dobu 12 měsíců, pak klient patří studiu. (K diskuzi - viz otevřené otázky.)
5. Deal pod minimální marží (40 %, viz kap. 3) musí schválit studio lead a provize se počítá až ze skutečného zisku.

Příklad: zakázka na playable za 200 000 Kč, přímé náklady 110 000 Kč, zisk 90 000 Kč.
Salesman (uzavřel): 9 000 Kč. Kolega, co přivedl kontakt: 4 500 Kč. Studio: 76 500 Kč.

---

## 7. Přechodový plán (pokud se restrukturalizuje stávající tým)

1. **Měsíc 1:** potvrdit obsazení leadů (producer, tech, art), zveřejnit delegační tabulku (kap. 3).
2. **Měsíc 2:** spustit bonusový systém nanečisto - cíle se definují a vyhodnotí, ale první měsíc se vyplácí plný bonus všem (kalibrace pravidel bez rizika).
3. **Měsíc 3:** ostrý provoz bonusů + provizní řád pro sales podepsaný jako dodatek smluv.
4. **Průběžně:** kvartální retrospektiva struktury - co se eskaluje moc často, tam se posunou limity.

---

## 8. Otevřené otázky

- [ ] Kalibrace platových pásem na skutečné lidi a region (čísla v kap. 4 jsou tržní odhad).
- [ ] Bonusy měsíčně (0-15 %) vs. kvartálně (0-25 %)?
- [ ] Provize z opakovaných zakázek: návrh 50 % sazby po 12 měsíců - souhlas?
- [ ] Interní hodinová sazba pro výpočet zisku offeru (nákladová vs. nákladová + režie?).
- [ ] Má sales cílit jen playables/B2B, nebo i publishing a co-dev dealy? (Mění to velikost provizí.)
- [ ] Vztah k současné struktuře NOXGAMES (33+ lidí) - je tohle návrh pro samostatnou buňku, nový projekt, nebo cílový stav po zeštíhlení?

---

## Log iterací

| Iterace | Datum | HTML | Změny |
|---|---|---|---|
| v1 | 2026-07-28 | `delegacni-navrh-v1.html` | První draft: struktura 15 lidí, delegační tabulka, platy, bonusy 0-15 %, provize 10 % + 5 % ze zisku offeru |
