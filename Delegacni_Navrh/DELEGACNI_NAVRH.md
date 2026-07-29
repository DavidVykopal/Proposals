# Delegační návrh — NOXGAMES

> Pracovní dokument. Návrh delegační struktury a úpravy organizační struktury v NOXGAMES (16 lidí).
> Stav: **iterace 02** - zapracované poznámky Davida z 29. 7. 2026.

---

## 1. Principy

1. **Ploché vedení, žádný izolující middle management.** Exec vrstva (CEO + operations, marketing a production chief) není klasický middle management - s leady a lidmi v týmech se pracuje napřímo, nikdo nestojí v cestě komunikaci.
2. **Každá oblast má jednoho vlastníka.** Kdo oblast vlastní, rozhoduje v ní bez eskalace až do definovaného limitu. Eskalace je výjimka, ne default.
3. **Fixní plat, ne tabulkový.** Fix vychází z měsíčního úhrnu času a rolí, které člověk reálně nese. Platy se normalizují (stejná pozice ≈ srovnatelný plat), ale nejde o tabulkový systém.
4. **Bonus za výkon, podíl za iniciativu.** Měsíční bonus za týmové a osobní cíle. Podíl ze zisku za nápady, leady a dealy, které firmě vydělají nebo ušetří.
5. **Více rolí = cíle ve všech rolích.** Kdo nese víc rolí (např. QA lead + office), má v každé z nich nastavené cíle a vstupuje mu to do platu i hodnocení.

## 2. Struktura NOXGAMES (16 lidí)

```
CEO · Jirka (majitel) ←→ Poradní rada: Mirek (tech, nejseniornější programátor),
│                                       Petr (art direction) — spolumajitelé
├── DJ · Operations chief ....... finance, chod firmy
│   ├── Office manager
│   └── Externí spolupráce (účetní a další)
├── Kuba · Marketing chief ...... marketing, UA
│   ├── Marketing grafici
│   └── UA manažeři
└── David · Production chief .... produkce = vše ostatní
    ├── Herní produkce (design · programování · art · testing)
    ├── Publishing
    ├── R&D
    └── Externí zakázky (playables, vývoj externích her)
```

Poznámky:

- **Poradní rada není řídicí vrstva.** Mirek a Petr jako spolumajitelé radí CEO a jsou zároveň nejseniornější tech a art autority ve firmě.
- **Exec vrstva není middle management.** CEO i chiefs pracují napřímo s leady projektů a jednotlivými lidmi.
- **Více rolí je norma.** Při hodnocení a nastavování cílů se počítá s tím, že člověk může zastávat víc rolí najednou.

## 3. Delegace rozhodování

| Rozhodnutí | Vlastní | Bez eskalace do | Eskalace na |
|---|---|---|---|
| Denní priority | Leadi týmů a projektů | rámec sprintu | Producer |
| Sprint (náplň a plán) | Producer | schválená roadmapa | CEO |
| Roadmapa, nové projekty | Producer | připravuje iniciální návrh | CEO (schvaluje) |
| Technické řešení, stack | Tech lead projektu | bez dopadu na termíny | Project lead, dál producer |
| Vizuální směr | Art lead projektu | rámec art directionu | Art director |
| Outsourcing (art i další) | Producer | na žádost project managera | CEO |
| Game design změny | Game designer projektu | bez dopadu na monetizaci | Project lead |
| UA rozpočet | UA manager | schválený měsíční budget | Operations chief (DJ) |
| Nábor, platy, ukončení | Producer (David) | - | CEO |

Pravidlo: co není v tabulce, rozhoduje vlastník nejbližší oblasti. Názvosloví: producer = produkční lead = production chief.

## 4. Fixní platy a normalizace

**Žádné tabulkové platy.** Fixní plat je nastavený na měsíční úhrn času a role, které člověk nese. Cíl je normalizace: rozdíly v platech musí jít vysvětlit pojmenovanými faktory, ne historií vyjednávání.

Faktory, ze kterých fix vychází:

- **Počet rolí** - kdo nese víc rolí, má to ve fixu (ne v přesčasech); cíle má ve všech rolích.
- **Důležitost rolí** - dopad role na firmu.
- **Délka ve firmě** - loajalita a nasbíraný kontext.
- **Skill v rolích** - úroveň, na jaké člověk roli drží (včetně extra skillů, které firma využívá).

Zásady přechodu:

1. Nikdo si nepohorší vůči svému průměrnému současnému výdělku.
2. Kdo se normalizací ukáže jako výrazně přetížený (víc nutných rolí, nejde to jinak), má být odměněn víc.
3. Bonusové složky jsou cesta, jak si vydělat navíc, když se daří.
4. Základní pásma se nastaví ze současné reality (úkol, viz kap. 8).

## 5. Výkonnostní bonusy

Bonus je **0 až 15 % fixního platu měsíčně**, složky **50 / 50**:

| Složka | Váha | Podle čeho |
|---|---|---|
| Týmová | 50 % | výsledek týmu / projektu za měsíc |
| Osobní | 50 % | splnění osobních cílů |

Pravidla:

1. Cíle se definují předem, první pracovní den měsíce. Nikdy zpětně.
2. Kdo má víc rolí, má cíle nastavené ve všech svých rolích.
3. Vyplácí se s výplatou za daný měsíc, žádné odkládání.

**Podíl na zisku (profit share):** nad rámec měsíčních bonusů běží systém podílu na zisku firmy vyplácený **2× ročně**. Je to samostatný systém - přesná pravidla doplnit (kap. 8).

## 6. Podíly z iniciativ a dealů

NOXGAMES nemá sales tým. Nosit nápady, leady a dealy - jak vydělat nebo ušetřit - je práce všech.

| Role | Podíl | Z čeho |
|---|---|---|
| Kdo přinese iniciativu (nápad, lead, deal) | **5 %** | ze zisku / úspory |
| Kdo deal nebo myšlenku dotáhne do konce | **10 %** | ze zisku / úspory |
| Kdo udělá obojí | **15 %** | ze zisku / úspory |

Pravidla:

1. **Zisk dealu** = výnos minus náklady na delivery spočítané podle interních tarifů. Tarify se nastaví v rámci delegace (kap. 8).
2. Podíl se vyplácí **po zaplacení klientem**; u úspor po jejich prokázání.
3. Opakované zakázky od stejného klienta už podíl nenesou. U rekurentního výnosu se podíl počítá **jen z prvního roku**.

Příklad: zakázka za 200 000 Kč, náklady na delivery dle tarifů 110 000 Kč, zisk 90 000 Kč.
Dotažení (10 %): 9 000 Kč. Iniciativa (5 %): 4 500 Kč. Firma: 76 500 Kč.

## 7. Přechodový plán

1. **Krok 1 - role shora dolů:** dodefinovat odpovědnosti od majitelů a CEO přes chiefy a leady až po základní pozice. Každá role: co dělá, za co ručí.
2. **Krok 2 - normalizace platů:** nastavit fixy ze současné reality podle faktorů z kap. 4. Nikdo si nepohorší, přetížení se dorovnají.
3. **Krok 3 - bonusy a podíly:** spustit měsíční bonusy (první měsíc nanečisto) a pravidla podílů z iniciativ a dealů.
4. **Průběžně:** retrospektiva delegace - co se eskaluje moc často, tam se posunou limity. Doplnit tarify a pravidla profit share.

## 8. Otevřené úkoly (TODO)

- [ ] Nastavit základní platová pásma ze současné reality (přechod bez pohoršení).
- [ ] Sepsat přesná pravidla pololetního podílu na zisku (profit share 2× ročně).
- [ ] Nastavit interní tarify pro výpočet nákladů na delivery (vstup pro podíly z dealů).
- [ ] Dopsat popisy rolí a odpovědností shora dolů: majitelé → CEO → chiefs → leadi → pozice.
- [ ] Sjednotit názvosloví rolí (producer = produkční lead = production chief).

---

## Log iterací

| Iterace | Datum | HTML | Změny |
|---|---|---|---|
| v1 | 2026-07-28 | `delegacni-navrh-v1.html` | První draft: hypotetický 15členný indie tým, delegační tabulka, tabulkové platy, bonusy 60/40, provize 10 % + 5 % |
| v2 | 2026-07-29 | `delegacni-navrh-v2.html` | Zapracované Davidovy poznámky: reálná struktura NOXGAMES (16 lidí, CEO Jirka, poradní rada Mirek + Petr, chiefs DJ/Kuba/David), delegační tabulka dle skutečných rolí, tabulkové platy nahrazeny normalizací (faktory: počet rolí, důležitost, délka, skill), bonusy 50/50 + zmínka profit share 2× ročně, provize přerámovány na podíly z iniciativ (5 % nápad, 10 % dotažení, i z úspor), rekurentní výnos jen první rok, přechodový plán shora dolů |
