# Q4 2026 plánování · 24. 9. 2026

> HTML render: `porada-2026-09-24-q4-plan.html`
>
> Navazuje na poradu **Q4 plan meet + Produktová porada 21. 9. 2026** (hub, Vedení → Meetings):
> poznámky Jirky, Martinův `Q4_2026_Strategicky_SITREP.html`, Kubův
> `kvartalni-porada-q4-kuba.html` a zápis z porady.
> Čísla o nákladech Sector Defense: `sector-defense-q3-naklady.html` (v této složce).
> Organizační část Q4 (karty lidí, pilot rozpočtů) je v samostatném podkladu
> `PORADA_2026-10-01_DELEGACE_4.md` (delegační porada čt 1. 10.).

---

## 1. O čem porada je

21. 9. proběhla retrospektiva Q3 a každý přinesl svůj pohled na Q4. Pohledy se v jádru
shodují: **Q4 je o monetizaci a škálování toho, co už máme, ne o otevírání dalšího drahého
produktu.** Neshodují se v tom, podle čeho poznáme, kdy přidat a kdy brzdit, a kolik na co
dáme lidí.

Porada proto nemá znovu sbírat názory. Má z nich udělat **Q4 plán s čísly, vlastníky
a gaty**: max 10 cílů, u každého jeden vlastník a jedno číslo, podle kterého se v prosinci
pozná, jestli se to povedlo.

## 2. Co má z porady vyjít

| # | Výstup |
|---|---|
| 01 | **Q4 cíle** (kap. 6): max 10, vlastník, číslo, termín |
| 02 | **Společné gaty pro Sector Defense**: marketing i produkce, scale / hold / iterate / stop |
| 03 | **Rozhodnutí o portfoliu**: co dostane kapacitu, co jde do údržby a co končí |
| 04 | **Pravidlo pro nový drahý produkt**: kdy se smí otevřít |
| 05 | **Priority nástrojů v hubu** na Q4, top 3 |
| 06 | **Zápis jako dekret do Wiki** a Q4 cíle v hubu (Cíle) |

## 3. Výchozí čísla

Stav k 20. až 23. 9. 2026. Revenue z finančního skladu (BigQuery), hodiny z time trackingu v hubu.

| Co | Číslo | Zdroj |
|---|---|---|
| Revenue studia Q3 (1. 7. až 20. 9.) | **$742 038** | finanční sklad |
| Z toho Red Command + Mecha Fortress + Hexapolis | **74,95 %** ($556 140) | finanční sklad |
| Red Command, náš 50% podíl na profitu Q3 | **$141 400** (od launche v květnu $151 000; profit hry se dělí 50/50 se sesterskou firmou, která RC publikuje) | finanční sklad |
| Red Command, profit měsíčně | cca **$50 000** (denně cca $1 500) | SITREP, zápis 21. 9. |
| Extra profit od července | něco přes **$100 000**, bez Indie | SITREP |
| Běžné náklady firmy mimo mzdy | cca **500 000 Kč měsíčně** (cca $24 000) | David; Jirka uvádí cca 25k měsíčně |
| **Sector Defense, náklad Q3** | **$82 600** (mandays) až **$146 500** (fokus firmy) | `sector-defense-q3-naklady.html` |
| Vykázané hodiny na Voldemort (srpen a září) | **1 596 h**, 8 lidí | time tracking |
| Hodiny bez tasku v Q3 | **1 681 h** z 5 192 h | time tracking |
| RON_India (India deal) | **$40 000 zaplaceno**, $60 000 na stole, plná hra $800 000 (100k započteno), H1 2027 | David |

**Dvě poznámky k číslům:**

- **Fokus 80 % na Sector Defense je odhad.** Time tracking ukazuje 1 596 h z 3 511 h přiřazených
  k projektu (45 %), protože třetina hodin nemá task. Pro výpočet nákladu to nevadí (stránka umí
  obojí), pro rozhodování o kapacitě v Q4 ano: od 1. 10. se timer zapisuje na task (Delegace 4, P8).
- **Red Command se zaplatil 1,5×.** Stál cca $100 000 včetně fixních nákladů (práce $24 969)
  a náš 50% podíl na profitu je $151 000 (celý profit hry cca $302 000). Sector Defense je po Q3 na 0,8 až 1,5násobku té investice a ještě nevyšel.

## 4. Retrospektiva Q3 v kostce

| Oblast | Stav | Závěr |
|---|---|---|
| **Sector Defense, vývoj** | převážně splněno | výběr tématu, CPI testy (4 862 instalací, vítěz V3_rpg), playtest; vizuálně o dvě třídy nad MF |
| **Red Command** | splněno | stabilní cashcow cca $50k měsíčně, prvních $100k vyplaceno; iOS pozdě, u break-even |
| **Mecha Fortress** | změna směru | revenue výrazně kleslo, A/B testy bez zásadního efektu; 21. 9. rozhodnuto: údržba |
| **Finanční cíle (OKR)** | nesplněno | kumulativní profit nesplněn (bronz jen s platbou z Indie), daily profit spadl ze silver na bronz, ROI 50 % nepřekročen |
| **LiveOps** | nejhorší stav | 0 % příjmů z LiveOps, hráči nekupují nabídky ani nesledují reklamy |
| **Finanční reporting** | nesplněno | týdenní a měsíční review se nedělalo, chyběl automatický datový základ |
| **Hub** | splněno | 16 z 16 lidí, cca 300 feedbacků, náklad cca $13 000, úspora licencí cca $5 000 ročně |
| **Kanceláře, tým** | splněno | stěhování levnější a lepší, tým funguje a je motivovaný |
| **Experimenty** | k vyhodnocení | Puppets, Tank Fortress, Capybara: jaký z toho plyne závěr? |

## 5. Bloky k rozhodnutí

Každý blok má jednu až tři otázky, na které porada musí odpovědět. Čísla a návrhy jsou z
podkladů 21. 9.

### 5.1 Sector Defense: launch a škálování · David + Kuba

- **Plán launche (Kuba):** struktura podle launche Red Command. Cca **€138 000** na první měsíc ve
  čtyřech tranších, zavázaná je jen tranše 1 (**€13 289**, zároveň maximální ztráta, když neprojde Gate 1).
- **iOS** v měsíci 2, jen když Android na D21 drží D7 ROAS nad 65 %.

**Gaty marketingu** (prahy jsou polovina toho, co dosáhl Red Command):

| Gate | Den | Podmínky | Uvolní |
|---|---|---|---|
| 1 | D7 | D1 ROAS ≥ 22 %, retence D1 ≥ 24 %, D3 ≥ 14 %, eCPI ≤ €0,60 | €28 010 |
| 2 | D14 | D7 ROAS ≥ 45 %, Google adROAS D7 ≥ 55 %, platící ≥ 0,6 % | €35 637 |
| 3 | D21 | D7 ROAS ≥ 65 %, D1 → D7 ≥ 1,8×, value kampaně ≥ 90 % delivery | €61 280 |

- **Rozhodnout:**
  1. **D0**, tedy datum launche (produkce).
  2. **Gaty produkce, zrcadlo ke gatům UA.** Když Gate 3 neprojde kvůli produktu (D7 ROAS pod 45 %),
     co se stane na straně vývoje: iterace o kolik sprintů, s kolika lidmi, a kdy stop.
  3. **LiveOps od prvního dne.** Jak se Sector Defense vyhne osudu MF, kde LiveOps nefunguje (Jirka:
     "dokážeme dostat hru do long-tail LiveOps fáze?").

### 5.2 Red Command · David

- **Cíl:** udržet economics, dokončit review monetizace a hooku (externí design), 1 až 2 A/B iterace,
  dál škálovat iOS (A/B test obtížnosti běží, iOS sbírá data pomalu).
- **Payout:** další vždy po dalších $100k pro naši stranu, první pravděpodobně začátkem listopadu.
- **Rozhodnout:** kolik dev a design kapacity se po launchi Sector Defense uvolní na RC a kdy přidat
  další sprint nebo dva podle výsledků A/B.

### 5.3 India deal (RON_India) · David

- **Stav:** MVP hotové, **$40 000 zaplaceno**, nabídnut balíček **$60 000** na další 4 týdny (assety,
  combat); klient má 14 dní na rozhodnutí. Pak nabídka plné hry za **$800 000** se započtením 100k,
  dodání v H1 2027.
- **Náklad zatím:** Davidův čas ($1 143) a cca $277 za Claude, tedy cca $1 400. ROI zatím 2 717 %. Marže je mimořádná.
- **Rozhodnout:**
  1. Když klient kývne, **z jaké kapacity se plná hra postaví**, aniž by spadl Sector Defense nebo RC.
  2. Jak se India deal promítne do bonusového tieru (SITREP: $500k a $1m závisí hlavně na SD a Indii).

### 5.4 Portfolio: kdo dostane kapacitu · Jirka

Jirkův odhad měsíčního potenciálu:

| Titul | Potenciál / měsíc | Stav | Návrh na Q4 |
|---|---|---|---|
| Red Command | $50k | stabilní | škálovat, monetizace |
| Sector Defense (Voldemort) | $50k až $150k | před launchem | hlavní fokus |
| Mecha Fortress | $20k | v poklesu | **údržba** (rozhodnuto 21. 9.), levné externí experimenty, R&D testbed pro RC a SD |
| Hexapolis 1 | $15k | drží | údržba s updaty |
| Hexapolis 2 | ? | rizika: PvP, cheateři, OP jednotky, PowerProgress | rozhodnout: pokračovat, zmrazit, nebo stop |
| Butter Chicken | čistý profit | podle kontextu India deal | kap. 5.3 |
| Puppet Sports | nezaplatí se z UA | chybí brainstorm partner | rozhodnout: partner, nebo stop |
| Tankzor | | | **vyřazen** (rozhodnuto 21. 9.) |

- **Rozhodnout:**
  1. **Pravidlo pro legacy:** kdy revenue titulu přestane vyvažovat QA, údržbu a režii, a jsme připraveni
     tu revenue vědomě pustit? (SITREP)
  2. **Jsme firma na 1 až 2 typy projektů?** (Jirka) Návrh: ano pro Q4, tedy mid-core strategie (RC, SD, Hex)
     + B2B. Závěry z Puppets, Tank Fortress a Capybara zapsat jako learning, ne jako otevřené projekty.

### 5.5 R&D a další produkt · David

- **Princip k potvrzení (SITREP):** nový drahý titul se neotevírá, dokud nejsou na stole reálné výnosy
  Sector Defense a India dealu. V Q4 jen **malé a levné testy s krátkým time-to-market**: rapid
  prototyping, CPI testy, trendy přes AppMagic.
- Platí hranice z tracker T01: experiment max **2 sprinty**, pak je to otevření produkce a schvaluje CEO.
- **Rozhodnout:** které 1 až 2 malé testy v Q4 a kdo je vlastní.

### 5.6 Finance, reporting a cíle · Martin

- **H2 tiery:** $200k / $500k / $1m kumulativního extra profitu; **bonusy se otevírají od $500k**.
- **Jirka:** cílit na **profit firmy $100k měsíčně**.
- **Reporting:** dashboard z účtů a cash flow na začátku Q4, pak týdenní a měsíční review.
- **Rozhodnout:**
  1. Je reporting od 1. 10. dost dobrý na řízení výdajů, ROI a bonusů? Kdo dělá týdenní review a kdy.
  2. Který cíl je Q4 cíl firmy: $100k měsíčně v prosinci, nebo kumulativní tier?

### 5.7 LiveOps a monetizace · David + designéři

- **Cíl z 21. 9.:** **25 % revenue projektu z LiveOps** (battle passy, eventy), dnes 0 %.
- **Retence:** D1 **+2 až 3 p. b.** (třeba úpravou nabídky hrdinů).
- Změny se od teď testují přísněji: 50% A/B testy nebo rollouty, ne malé změny, které nejdou vyhodnotit.
- **Rozhodnout:** na kterém titulu se LiveOps model postaví první (návrh: RC, pak převzít do SD).

### 5.8 Komunita a sociální sítě · Kuba + Jirka

- **Jirka:** LinkedIn, IG, FB; komunita k hlavním hrám s hráči jako moderátory; cross-promo, invite friends.
  "Sociální rozměr je nová měna."
- **Marketing:** PR a sociální sítě dnes nedělá nikdo, 0 % kapacity; Kuba bez externisty.
- **Rozhodnout:** tohle je kapacitní konflikt, ne názorový. Buď se to v Q4 vědomě nedělá, nebo se
  řekne, kdo to dělá a co za to padá. Cross-promo a invite friends jsou produktové feature (Shared
  Backend je hotový, jen nenasazený) a patří do plánu RC a SD.

### 5.9 Hub a nástroje · Martin

- **Priority (Martin):** ASO, UA a akvizice, competitor scraping, Asset Studio a reskin workflow.
- **Priority (Kuba):** UA, ASO, competitor scraping. Shoda na prvních třech.
- **Stav:** 16 z 16 lidí, 28 automatických úloh denně, cca 2 978 odpovědí na recenze bez člověka,
  náklad cca $13 000, návratnost cca 2,5 roku jen z licencí.
- **Rozhodnout:** top 3 na Q4 a kdo je zadavatel u každého. AMA bot do ověřitelného stavu (Kuba): úprava
  je připravená na stagingu (čeká na push), AMA pak čte skutečná cashflow data a exec vidí náklady
  z time trackingu.

### 5.10 Lidé a organizace · všichni

- Organizační Q4 (karty lidí, pilot rozpočtů a delegace od 1. 10.) je v podkladu **Delegace 4** na čtvrtek 1. 10.; rozhodnutí z dneška do něj vstupují.
- **Nábor:** interní senior system designer neúspěšný, pokračují externí kontraktoři (Mirek, Michal).
  Balík tří pozic čeká na rozhodnutí CEO (Delegace 4, kap. 6).
- **Riziko:** kapacita programátorů závisí na výsledku jednání z 21. 9. (Milan).
- **Kanceláře:** v Q4 bez priority (rozhodnuto 21. 9.).
- **Holding a právní framework:** vyhradit exec čas na strukturu firem a publisher → developer framework;
  určit, kdo drží návrh.

## 6. Návrh Q4 cílů (k úpravě na poradě)

Max 10 čísel, jeden vlastník na číslo (T43).

| # | Cíl | Číslo | Vlastník |
|---|---|---|---|
| 1 | Profit firmy | **$100k za prosinec**, nebo kumulativní tier $200k / $500k | Jirka |
| 2 | Sector Defense launch | D0 dodržen; rozhodnutí podle Gate 3 do D21 | David, Kuba |
| 3 | Sector Defense návratnost | D7 ROAS ≥ 65 % na Androidu | Kuba |
| 4 | LiveOps | 25 % revenue živého titulu z LiveOps (RC) | David |
| 5 | Retence | D1 +2 až 3 p. b. na RC a SD | David |
| 6 | Red Command | ≥ $50k měsíčně náš podíl, iOS v zisku | David |
| 7 | India deal | podepsaná další fáze ($60k) a rozhodnutí o plné hře | David |
| 8 | Reporting | týdenní review běží od října, ≥ 95 % hodin přiřazeno k tasku | Martin |
| 9 | Delegace a rozpočty | pilot Q4 běží, rozpočty segmentů schválené | Martin + vlastníci |
| 10 | Hub | top 3 nástroje z 5.9 v produkci | Martin |

## 7. Agenda (2,5 h)

| Čas | Blok |
|---|---|
| 10 min | Výchozí čísla (kap. 3) a retro v kostce (kap. 4), bez diskuse |
| 30 min | Sector Defense: D0, gaty marketingu a produkce, LiveOps od prvního dne (5.1) |
| 15 min | Red Command a India deal (5.2, 5.3) |
| 25 min | Portfolio a R&D: kdo dostane kapacitu, co končí, pravidlo pro drahý produkt (5.4, 5.5) |
| 15 min | Finance a reporting, cíl firmy (5.6) |
| 15 min | LiveOps a komunita (5.7, 5.8) |
| 10 min | Hub, top 3 (5.9) |
| 20 min | Q4 cíle: projít kap. 6, vlastník a číslo u každého |
| 10 min | Rekapitulace, dekret, co jde do hubu |

## 8. Po poradě

- [ ] Q4 cíle zapsat do hubu (Cíle) s vlastníky a čísly.
- [ ] Dekret do Wiki: portfolio rozhodnutí, gaty Sector Defense, pravidlo pro drahý produkt.
- [ ] Kuba + David: sjednocená tabulka gatů marketingu a produkce pro Sector Defense, před D0.
- [ ] Martin: termín prvního týdenního review.
- [ ] Aktualizovat `../Delegacni_Navrh/TRACKER_TEMAT.md`.
