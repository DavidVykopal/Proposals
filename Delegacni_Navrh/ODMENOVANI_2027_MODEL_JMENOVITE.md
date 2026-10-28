# Model odměňování 2027 jmenovitě · důvěrné · k poradě 29. 10. 2026

> Generuje `model_odmenovani_2027.py`. Jen pro Davida a Martina B. (finanční dopad), nesdílet na hub.
> Dnes = Ø skutečně vyplacená odměna za práci 1–10/2026 z NoxHubu, bez coworkingu (průtokový náklad na kancelář).
> Roky = dokončené roky ve firmě k 1. 1. 2027 podle data nástupu v hubu (tenure achievementy).

## 1. Jak číst tabulky

- **H** = hodnota role: základ podle rolí a podílu × úroveň × (1 + 2 % za rok ve firmě, strop 20 % po 10 letech) + aktivní příplatky (nejvýš 40 % základu) + pasivní složka z achievementů (nejvýš 8).
- **Fix 2027** = H, nikdy pod dnešek (rozdíl drží osobní garance). U exekutivy společný základ 110 + příplatky.
- **Strop základu** je 150 tis. Kč pro tým i exekutivu (CEO a foundeři mimo). Variabilní složka a podíly se do něj nepočítají. Nikdo pod exekutivou nemá ani s plným bonusem víc než nejnižší fix exekutivy.
- **1. 1. 2027** = první krok. V týmu jde narovnání nad 10 tis. ve dvou krocích, druhý 1. 7. 2027. Exekutiva jednorázově od 1. 1.
- **Exekutiva** nemá bonus ani malus: fix + podíl na zisku pod čarou. Minimum = maximum = fix.
- **Plán** = fix + polovina bonusu.

## 2. Rozpis všech ve firmě

Tis. Kč měsíčně. Minimum = fix s plným malusem, maximum = fix s plným bonusem. Bez poolu (prasátka), který se dělí zvlášť. Exekutiva má jen fix, k tomu podíl na zisku.

**Z čeho je fix**

| Člověk | Základ role | Roky ve firmě | Aktivní příplatky | Pasivní (historie) | Fix 2027 |
|---|---|---|---|---|---|
| **Čoud** | prog, senior: 80,0 | 7 → +11,2 | zástup B2B delivery a autority tech +5 | vedl projekt +2,0 | **98,2** |
| **Milan** | prog, senior: 80,0 | 0 → +0,0 | – | – | **85,0** (dohoda, role 80,0) |
| **Aldy** | GD 80 % + grafik DEV 20 %, senior: 58,4 | 2 → +2,3 | project lead (Sektor) +12, druhý aktivní projekt (Mecha) +6, zástup vlastníka za plán a kapacity +5, mentor 2 lidí +4 (strop 40 %: +24,3) | – | **85,0** |
| **Karlík** | GD 80 % + grafik DEV 20 %, senior: 58,4 | 7 → +8,2 | project lead (Red Command) +12 | – | **78,6** |
| **Akimo** | publishing, senior: 58,0 | 4 → +4,6 | Publishing a LiveOps lead +10, správa kanceláří (Operations) +5 | – | **77,6** |
| **Hutis** | QA 53 % + prog 27 % + DevOps 20 %, senior: 61,2 | 3 → +3,7 | QA lead +8, zástup za NoxHub +5 | – | **77,8** |
| **David Č.** | grafik DEV, junior: 41,6 | 0 → +0,0 | – | – | **41,6** |
| **Richi** | UA, senior: 62,0 | 4 → +5,0 | – | – | **79,4** (garance 12,4) |
| **Ondra** | grafik MKT, senior: 56,0 | 4 → +4,5 | správa celého ASO +4 | – | **64,5** |
| **Ruda** | video, senior: 52,0 | 2 → +2,1 | – | – | **54,1** |
| **David** | společný základ exekutivy 110 | 6 (bez vlivu) | lidé pod sebou 7 → +6,0, rozpočet 45 % OPEX → +4,5, consigliere: agenda exekutivy, plány a strategie +5 | vedl projekt +4,0, přednášky +3,0 | **132,5** |
| **DJ** | společný základ exekutivy 110 | 9 (bez vlivu) | lidé pod sebou 1 → +1,0, rozpočet 24 % OPEX → +2,4, finance, rozpočet a smlouvy celé firmy +5 | vedl projekt +2,0 | **120,4** |
| **Kuba** | společný základ exekutivy 110 | 5 (bez vlivu) | lidé pod sebou 3 → +3,0, rozpočet 20 % OPEX → +2,0, analytika pro Produkci (přechodně) +2 | – | **117,0** |
| **Mirek** | návrh podle dneška: Ø hodiny × sazba 758 Kč, 1–9/2026 (cca 146 h) | 13 | – | – | **110,6** |
| **Peko** | návrh podle dneška: Ø fakturace 1–8/2026 bez hodin, míchá práci s dalšími plněními | 21 | – | – | **245,0** |
| **Jirka** | návrh podle dneška: mzda 16,1 + měsíční platby 83,5 (TM, royalties), 1–9/2026; k tomu podíl na zisku | 21 | – | – | **99,6** |

**Kolik může vydělat**

| Člověk | Pásmo | Dnes | Fix 2027 | Minimum (plný malus) | Plán | Maximum (plný bonus) | Δ fixu |
|---|---|---|---|---|---|---|---|
| **Čoud** | Jistota | 82,5 | **98,2** | 93,3 | 103,1 | 108,0 | +15,7 |
| **Milan** | Jistota | 71,4 | **85,0** | 80,8 | 89,3 | 93,5 | +13,6 |
| **Aldy** | Lead | 73,4 | **85,0** | 78,7 | 91,4 | 97,8 | +11,6 |
| **Karlík** | Lead | 49,1 | **78,6** | 72,7 | 84,5 | 90,4 | +29,5 |
| **Akimo** | Lead | 62,9 | **77,6** | 71,8 | 83,5 | 89,3 | +14,7 |
| **Hutis** | Lead | 45,3 | **77,8** | 72,0 | 83,7 | 89,5 | +32,5 |
| **David Č.** | Jistota | 36,8 | **41,6** | 39,5 | 43,7 | 45,8 | +4,8 |
| **Richi** | Jistota | 79,4 | **79,4** | 75,4 | 83,4 | 87,3 | +0,0 |
| **Ondra** | Jistota | 58,8 | **64,5** | 61,3 | 67,7 | 70,9 | +5,7 |
| **Ruda** | Jistota | 42,8 | **54,1** | 51,4 | 56,8 | 59,5 | +11,3 |
| **David** | fix + podíl na zisku | 105,5 | **132,5** | = fix | = fix | = fix | +27,0 |
| **DJ** | fix + podíl na zisku | 77,7 | **120,4** | = fix | = fix | = fix | +42,7 |
| **Kuba** | fix + podíl na zisku | 81,4 | **117,0** | = fix | = fix | = fix | +35,6 |
| **Mirek** | rada tří | 110,6 | **110,6** | – | – | – | 0 |
| **Peko** | rada tří | 245,0 | **245,0** | – | – | – | 0 |
| **Jirka** | rada tří | 99,6 | **99,6** | – | – | – | 0 |

### Narovnání ve dvou krocích

Kdo má nový fix o víc než 10 tis. nad dneškem, dostane 1. 1. 2027 dnešek plus polovinu rozdílu (aspoň +10 tis.) a 1. 7. 2027 zbytek. Druhý krok potvrdí vlastník segmentu v červnu. Kdo roli, za kterou má příplatek, opravdu nenese, zůstává na prvním kroku a příplatek se přepočítá při roční evaluaci.

Proč:

- **Rozpočet:** v roce 2027 to ušetří cca 0,3 mil. Kč a náklad roste postupně, ne skokem v lednu.
- **Ověření role:** příplatek se platí za odpovědnost, kterou člověk nese. Půl roku ukáže, že ji opravdu nese, a druhý krok je pak zasloužený, ne slíbený.
- **Pojistka proti chybě v modelu:** role a procenta se zapisují poprvé. Když se ukáže chyba, opraví se před druhým krokem, ne zpětným snižováním.
- **Zlepšení hned:** každý, kdo se narovnává, cítí rozdíl od ledna, aspoň +10 tis. nebo polovinu.
- **Jen pro tým:** exekutiva a foundeři mají jednorázový skok od 1. 1. Fix schválí hlasováním celé vedení do konce roku a platí na celý rok, nikdo nevyjednává individuálně. Celá od 1. 1. platí i individuální dohoda.

| Člověk | Dnes | 1. 1. 2027 | 1. 7. 2027 | Δ celkem |
|---|---|---|---|---|
| **Čoud** | 82,5 | 92,5 | 98,2 | +15,7 |
| **Aldy** | 73,4 | 83,4 | 85,0 | +11,6 |
| **Karlík** | 49,1 | 63,8 | 78,6 | +29,5 |
| **Akimo** | 62,9 | 72,9 | 77,6 | +14,7 |
| **Hutis** | 45,3 | 61,6 | 77,8 | +32,5 |
| **Ruda** | 42,8 | 52,8 | 54,1 | +11,3 |

## 3. Tým pod exekutivou: detail

| Člověk | Role (podíl), úroveň · příplatky | Roky | H | Dnes | Fix 2027 | Δ | 1. 1. 2027 | Pásmo | Bonus max | Malus max | Plán |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Čoud** | Programátor, senior · +5 zástup B2B delivery a autority tech; pasivní +2,0 | 7 | 98,2 | 82,5 | 98,2 | +15,7 | 92,5 | Jistota | +9,8 | −4,9 | 103,1 |
| **Milan** | Programátor, senior · bez příplatku | 0 | 80,0 | 71,4 | 85,0 (dohoda 85 tis., cca 3 510 EUR; Milan chtěl 3 700 až 4 000 EUR, zápis 21. 9.) | +13,6 | 85,0 | Jistota | +8,5 | −4,3 | 89,3 |
| **Aldy** | Game designer 80 %, Grafik DEV 20 %, senior · +12 project lead (Sektor); +6 druhý aktivní projekt (Mecha); +5 zástup vlastníka za plán a kapacity; +4 mentor 2 lidí (strop 40 %: 24,3) | 2 | 85,0 | 73,4 | 85,0 | +11,6 | 83,4 | Lead | +12,8 | −6,4 | 91,4 |
| **Karlík** | Game designer 80 %, Grafik DEV 20 %, senior · +12 project lead (Red Command) | 7 | 78,6 | 49,1 | 78,6 | +29,5 | 63,8 | Lead | +11,8 | −5,9 | 84,5 |
| **Akimo** | Publishing a LiveOps, senior · +10 Publishing a LiveOps lead; +5 správa kanceláří (Operations) | 4 | 77,6 | 62,9 | 77,6 | +14,7 | 72,9 | Lead | +11,6 | −5,8 | 83,5 |
| **Hutis** | QA 53 %, Programátor 27 %, DevOps a IT 20 %, senior · +8 QA lead; +5 zástup za NoxHub | 3 | 77,8 | 45,3 | 77,8 | +32,5 | 61,6 | Lead | +11,7 | −5,8 | 83,7 |
| **David Č.** | Grafik DEV, junior · bez příplatku | 0 | 41,6 | 36,8 | 41,6 | +4,8 | 41,6 | Jistota | +4,2 | −2,1 | 43,7 |
| **Richi** | UA manager, senior · bez příplatku | 4 | 67,0 | 79,4 | 79,4 (garance 12,4) | +0,0 | 79,4 | Jistota | +7,9 | −4,0 | 83,4 |
| **Ondra** | Grafik MKT, senior · +4 správa celého ASO | 4 | 64,5 | 58,8 | 64,5 | +5,7 | 64,5 | Jistota | +6,4 | −3,2 | 67,7 |
| **Ruda** | Video a motion, senior · bez příplatku | 2 | 54,1 | 42,8 | 54,1 | +11,3 | 52,8 | Jistota | +5,4 | −2,7 | 56,8 |

## 4. Exekutiva: detail

| Člověk | Základ | Lidé pod sebou | Rozpočet (% OPEX) | Role navíc | Pasivní | Fix 2027 od 1. 1. | Dnes | Δ |
|---|---|---|---|---|---|---|---|---|
| **David** | 110 | 7 → +6,0 | 45 % → +4,5 | +5 consigliere: agenda exekutivy, plány a strategie | +7,0 | **132,5** | 105,5 | +27,0 |
| **DJ** | 110 | 1 → +1,0 | 24 % → +2,4 | +5 finance, rozpočet a smlouvy celé firmy | +2,0 | **120,4** | 77,7 | +42,7 |
| **Kuba** | 110 | 3 → +3,0 | 20 % → +2,0 | +2 analytika pro Produkci (přechodně) | +0,0 | **117,0** | 81,4 | +35,6 |

Kontrola stropu: nejvyšší možná odměna v týmu (fix + plný bonus) je 108,0, nejnižší fix exekutivy 117,0.

## 5. Souhrn nákladů, varianta A (mil. Kč za rok 2027)

| Skupina | Dnes | Špatný rok | Plán | Vše splněno |
|---|---|---|---|---|
| Tým | 7,23 | 8,64 | 9,18 | 9,72 |
| Exekutiva | 3,18 | 4,44 | 4,44 | 4,44 |
| Celkem | 10,40 | 13,07 | 13,62 | 14,16 |
| Foundeři a CEO (návrh = dnešek, mimo součet) | 5,46 | 5,46 | 5,46 | 5,46 |

Tým v roce 2027 s narovnáním ve dvou krocích, exekutiva celý rok plný fix. Od 2028 plný fix všem. Bez poolu (prasátka) a podílů na zisku, ty jdou ze zisku.

## 6. Tři varianty narovnání

A je preferovaná a nejdražší: splní závazek nejlepšího možného ohodnocení. B a C rozkládají rozdíl mezi dneškem a plným fixem rovnoměrně (dvě třetiny, třetina). Realisticky se může skončit u B.

| Varianta | Jen fixy | Plán | Max | Δ plánu | Δ fixů 2027 | Δ fixů 2028 | Δ fixů / EBITDA |
|---|---|---|---|---|---|---|---|
| **A · plné narovnání (preferovaná)** | 13,07 | 13,62 | 14,16 | +3,21 | +2,67 | +2,94 | 27 až 53 % |
| B · dvě třetiny narovnání | 12,29 | 12,80 | 13,30 | +2,39 | +1,89 | +2,01 | 19 až 38 % |
| C · třetina narovnání | 11,49 | 11,96 | 12,43 | +1,56 | +1,08 | +1,09 | 11 až 22 % |
| Dnes | 10,40 | | | | | | |

Mil. Kč za rok 2027, 13 lidí bez foundrů a CEO, bez poolu a podílů na zisku. Jen fixy = nikdo nedostane bonus, max = všichni plný bonus, Δ proti dnešku. Poslední sloupec = přírůstek fixů jako podíl Adj. EBITDA ze scénářů Martina B. (5 až 10 mil. Kč).

- **Strop exekutivy** (nikdo v týmu ani s plným bonusem nad nejnižším fixem exekutivy): A (108,0 proti 117,0), B (102,3 proti 105,1), C (96,5 proti 91,9). Ve variantě C pravidlo neplatí, exekutiva by se musela narovnat víc než tým.
- **Ve všech variantách platí, že si nikdo nepohorší.** Fix každého je aspoň dnešek, liší se jen, o kolik se narovná. Individuální dohoda (85 tis.) je ve všech stejná.
- **Individuální dohoda v B a C:** pevných 85 tis. by předběhlo lídry, kteří se narovnávají jen částečně (lead dvou projektů B 81,2, C 77,3). Když se skončí u B nebo C, navrhuji dohodu snížit stejným poměrem (B 80,5, C 75,9) a zbytek nabídnout přes bonus.
- **Dvě pásma, nebo jedno:** dát lídry do Jistoty ušetří ve variantě A cca 0,10 mil. ročně. Doporučení zůstává u dvou pásem.

**Fix 2027 po lidech podle varianty** (tis. Kč měsíčně, v závorce rozdíl proti dnešku)

| Člověk | Dnes | A · plné | B · dvě třetiny | C · třetina |
|---|---|---|---|---|
| **Čoud** | 82,5 | **98,2 (+15,7)** | 93,0 (+10,5) | 87,7 (+5,2) |
| **Milan** | 71,4 | **85,0 (+13,6)** | 85,0 (+13,6) | 85,0 (+13,6) |
| **Aldy** | 73,4 | **85,0 (+11,6)** | 81,2 (+7,8) | 77,3 (+3,9) |
| **Karlík** | 49,1 | **78,6 (+29,5)** | 68,8 (+19,7) | 58,9 (+9,8) |
| **Akimo** | 62,9 | **77,6 (+14,7)** | 72,7 (+9,8) | 67,8 (+4,9) |
| **Hutis** | 45,3 | **77,8 (+32,5)** | 67,0 (+21,7) | 56,1 (+10,8) |
| **David Č.** | 36,8 | **41,6 (+4,8)** | 40,0 (+3,2) | 38,4 (+1,6) |
| **Richi** | 79,4 | **79,4 (+0,0)** | 79,4 (+0,0) | 79,4 (+0,0) |
| **Ondra** | 58,8 | **64,5 (+5,7)** | 62,6 (+3,8) | 60,7 (+1,9) |
| **Ruda** | 42,8 | **54,1 (+11,3)** | 50,3 (+7,5) | 46,6 (+3,8) |
| **David** | 105,5 | **132,5 (+27,0)** | 123,5 (+18,0) | 114,5 (+9,0) |
| **DJ** | 77,7 | **120,4 (+42,7)** | 106,2 (+28,5) | 91,9 (+14,2) |
| **Kuba** | 81,4 | **117,0 (+35,6)** | 105,1 (+23,7) | 93,3 (+11,9) |

## 7. Index ke stropu (základ role jako % ze 150)

| Role | Základ | % stropu |
|---|---|---|
| Programátor | 80 | 53 % |
| UA manager | 62 | 41 % |
| Game designer | 60 | 40 % |
| DevOps a IT | 60 | 40 % |
| Publishing a LiveOps | 58 | 39 % |
| Grafik MKT | 56 | 37 % |
| Video a motion | 52 | 35 % |
| Grafik DEV | 52 | 35 % |
| QA | 52 | 35 % |
| Vlastník segmentu (společný základ) | 110 | 73 % |

## 8. Foundeři, CEO a podíly na zisku

- **Mirek, Peko, Jirka (CEO):** mimo systém rolí i mimo strop základu. V rozpisu je návrh podle toho, co dnes mají. Schvaluje rada tří (Majitelé), na další rok si mohou dát víc.
- **Jirka:** dnešek 99,6 tis. měsíčně = mzda 16,1 + měsíční platby 83,5 (v bance „TM“, „Ochranné známky“, royalties; 9 plateb za 1–9/2026). Podíl na zisku navíc, mimo tento přehled.
- **Podíl na zisku** má exekutiva (David, Kuba, DJ, Jirka) a foundeři Peko a Mirek. Exekutiva se vzdává bonusů podle KPI: má fix, podíl na zisku, který se počítá až ze zisku pod čarou po poolu pro tým, a jako všichni podíl z dealů (5 % navrhovatel + 5 % majitel dealu nebo executor, ze zisku dealu). Bonusy týmu tak nic nesnižuje a nehrozí double dipping (R-22-06).

## 9. Co ještě doplnit

- **Pasivní složka:** David +7 (vedl projekty, přednášky), Čoud a DJ +2 (vedli projekt). Kuba nic. V hubu doplnit odznaky `speaker` a nové „vedl projekt“, ať to sedí se systémem.
- **Milan:** hodnota role 80 (3 300 EUR po zkušebce), dohoda 85 tis. (cca 3 510 EUR) od 1. 1., na plánu 89,3 (cca 3 690 EUR), s plným bonusem 93,5 (cca 3 860 EUR). Zápis z 21. 9.: požadavek „4 000 EUR, resp. 90 tis. Kč“. Pod Čoudem zůstává ve fixu i s plným bonusem. Dohoda 85 je zároveň revize z 10. 9. (zmrazit a revidovat za 3 měsíce).
- **Richi:** dnešek 79,4 = hodiny 59,4 + pravidelná dofakturace 20 tis. měsíčně (v záznamech „J“, „Dofakturace“). Fix drží garance nad hodnotou role 67, při roční evaluaci se dorovnává.
- **Lidé pod DJ v Operations:** potvrzeno 1. Až Operations poroste (např. happy office), příplatek se posune při roční evaluaci.
- **Odstup v exekutivě:** s pasivní složkou je David o 12 tis. nad DJ. Bez ní 125,5 / 118,4 / 117.
- **Aldy** naráží na strop příplatků 40 % základu. Buď to tak nechat, nebo zástup vlastníka přesunout do pasivní složky.

