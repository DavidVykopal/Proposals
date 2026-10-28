# Model odměňování 2027 jmenovitě · důvěrné · k poradě 29. 10. 2026

> Generuje `model_odmenovani_2027.py`. Jen pro Davida a Martina B. (finanční dopad), nesdílet na hub.
> Dnes = Ø skutečně vyplacená odměna za práci 1–10/2026 z NoxHubu, bez coworkingu (průtokový náklad na kancelář).
> Roky = dokončené roky ve firmě k 1. 1. 2027 podle data nástupu v hubu (tenure achievementy).

## 1. Jak číst tabulky

- **H** = hodnota role: základ podle rolí a podílu × úroveň × (1 + 2 % za rok ve firmě, strop 10 %) + aktivní příplatky (nejvýš 40 % základu) + pasivní složka z achievementů (nejvýš 8).
- **Fix 2027** = H, nikdy pod dnešek (rozdíl drží osobní garance). U exekutivy společný základ 110 + příplatky.
- **Strop** základu ve firmě je 150 tis. Kč. Nikdo pod exekutivou nemá fix ani s plným bonusem vyšší než nejnižší fix exekutivy.
- **1. 1. 2027** = první krok. Narovnání nad 10 tis. jde ve dvou krocích, druhý 1. 7. 2027.
- **Plán** = fix + polovina bonusu.

## 2. Tým pod exekutivou

| Člověk | Role (podíl), úroveň · příplatky | Roky | H | Dnes | Fix 2027 | Δ | 1. 1. 2027 | Pásmo | Bonus max | Malus max | Plán |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Čoud** | Programátor, senior · +5 zástup B2B delivery a autority tech; pasivní +2,0 | 7 | 95,0 | 82,5 | 95,0 | +12,5 | 92,5 | Jistota | +9,5 | −4,8 | 99,8 |
| **Milan** | Programátor, senior · bez příplatku | 0 | 80,0 | 71,4 | 87,1 (dohoda 3 600 EUR (Milan chtěl 3 700 až 4 000, zápis 21. 9.)) | +15,7 | 87,1 | Jistota | +8,7 | −4,4 | 91,5 |
| **Aldy** | Game designer 80 %, Grafik DEV 20 %, senior · +12 project lead (Sektor); +6 druhý aktivní projekt (Mecha); +5 zástup vlastníka za plán a kapacity; +4 mentor 2 lidí (strop 40 %: 24,3) | 2 | 85,0 | 73,4 | 85,0 | +11,6 | 83,4 | Lead | +12,8 | −6,4 | 91,4 |
| **Karlík** | Game designer 80 %, Grafik DEV 20 %, senior · +12 project lead (Red Command) | 7 | 76,2 | 49,1 | 76,2 | +27,1 | 62,7 | Lead | +11,4 | −5,7 | 82,0 |
| **Akimo** | Publishing a LiveOps, senior · +10 Publishing a LiveOps lead; +5 správa kanceláří (Operations) | 4 | 77,6 | 62,9 | 77,6 | +14,7 | 72,9 | Lead | +11,6 | −5,8 | 83,5 |
| **Hutis** | QA 53 %, Programátor 27 %, DevOps a IT 20 %, senior · +8 QA lead | 3 | 72,8 | 45,3 | 72,8 | +27,5 | 59,1 | Lead | +10,9 | −5,5 | 78,3 |
| **David Č.** | Grafik DEV, junior · bez příplatku | 0 | 41,6 | 36,8 | 41,6 | +4,8 | 41,6 | Jistota | +4,2 | −2,1 | 43,7 |
| **Richi** | UA manager, senior · bez příplatku | 4 | 67,0 | 59,4 | 67,0 | +7,6 | 67,0 | Jistota | +6,7 | −3,3 | 70,3 |
| **Ondra** | Grafik MKT, senior · bez příplatku | 4 | 60,5 | 58,8 | 60,5 | +1,7 | 60,5 | Jistota | +6,0 | −3,0 | 63,5 |
| **Ruda** | Video a motion, senior · bez příplatku | 2 | 54,1 | 42,8 | 54,1 | +11,3 | 52,8 | Jistota | +5,4 | −2,7 | 56,8 |

## 3. Exekutiva

| Člověk | Základ | Lidé pod sebou | Rozpočet (% OPEX) | Role navíc | Pasivní | Fix 2027 | Dnes | Δ | 1. 1. 2027 | Bonus max | Malus max | Plán |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **David** | 110 | 7 → +6,0 | 45 % → +4,5 | +5 consigliere: agenda exekutivy, plány a strategie | +7,0 | 132,5 | 105,5 | +27,0 | 119,0 | +53,0 | −13,3 | 159,0 |
| **DJ** | 110 | 1 → +1,0 | 24 % → +2,4 | +5 finance, rozpočet a smlouvy celé firmy | +0,0 | 118,4 | 77,7 | +40,7 | 98,1 | +47,4 | −11,8 | 142,1 |
| **Kuba** | 110 | 3 → +3,0 | 20 % → +2,0 | +2 analytika pro Produkci (přechodně) | +0,0 | 117,0 | 81,4 | +35,6 | 99,2 | +46,8 | −11,7 | 140,4 |

Kontrola stropu: nejvyšší možná odměna v týmu (fix + plný bonus) je 104,5, nejnižší fix exekutivy 117,0.

## 4. Souhrn nákladů (mil. Kč za rok 2027)

| Skupina | Dnes | Špatný rok | Plán | Vše splněno |
|---|---|---|---|---|
| Tým | 6,99 | 8,38 | 8,90 | 9,43 |
| Exekutiva | 3,18 | 3,66 | 4,99 | 5,87 |
| Celkem | 10,16 | 12,04 | 13,89 | 15,30 |

Fix v roce 2027 počítá narovnání ve dvou krocích. Od 2028 plný fix po celý rok.

## 5. Varianty (mil. Kč za 2027, plán)

| Varianta | Plán | Δ proti dnešku |
|---|---|---|
| 1 · Tři pásma Jistota / Lead / Dynamika (doporučeno) | 13,89 | +3,73 |
| 2 · Dvě pásma (lídři v Jistotě) | 13,80 | +3,63 |
| 3 · Zmrazit dnešní odměnu jako fix, jen přidat variabilní složku | 11,22 | +1,05 |

## 6. Index ke stropu (základ role jako % ze 150)

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

## 7. Foundeři, CEO a podíly na zisku

- **Mirek, Peko, Jirka (CEO):** úplně mimo model. Jejich odměnu schvaluje rada tří (Majitelé).
- **Podíl na zisku** má exekutiva (David, Kuba, DJ, Jirka) a foundeři Peko a Mirek. Nikdo z nich není v poolu pro tým. Exekutiva si bonus vyplácí průběžně podle KPI, pololetní a roční pool je jen pro lidi pod exekutivou.

## 8. Co ještě doplnit

- **Pasivní složka:** podle Davida 28. 10. má historii leadů a přednášky David (+7), vedení projektu Čoud (+2). Přednášky má jinak jen Jirka (mimo model). Chybí DJ a Kuba. V hubu doplnit odznaky `speaker` a nové „vedl projekt“, ať to sedí se systémem.
- **Milan:** hodnota role 80 (3 300 EUR po zkušebce), dohoda 3 600 EUR = cca 87 tis. od 1. 1. Zápis z 21. 9. uvádí požadavek „4 000 EUR, resp. 90 tis. Kč“ (90 tis. je cca 3 700 EUR). Nad 3 600 si může vydělat bonusem (Jistota až +10 %). Pod Čoudem zůstává ve fixu i na plánu. 10. 9. padlo rozhodnutí plat zmrazit a revidovat za 3 měsíce, dohoda 3 600 je tedy zároveň ta revize.
- **Lidé pod DJ v Operations:** potvrzeno 1. Až Operations poroste (např. happy office), příplatek se posune při roční evaluaci.
- **Odstup v exekutivě:** s pasivní složkou je David o 14 tis. nad DJ. Pokud má rozdíl zůstat malý, dá se pasivní složka exekutivy vynechat (David by měl 125,5).
- **Aldy** naráží na strop příplatků 40 % základu. Buď to tak nechat, nebo zástup vlastníka přesunout do pasivní složky.

