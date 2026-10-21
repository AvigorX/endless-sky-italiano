# L14 — Revisione editoriale del blocco `data/map planets.txt` 3239–3607

83 descrizioni, 4.470 parole inglesi → 4.534 italiane. Decimo lotto del tratto iniziale del file, nessun ID
in comune con L1–L13. Inizia con `planet:Livolua` e si chiude a fine pianeta con `planet:Midnight Diamond`
(riga 3607); la successiva (riga 3614) apre Midway Emerald.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–83), rilettura
del solo italiano.

Le 83 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 83 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Avgi` / `Hai` / `Arach` / `Kimek` / `Successors` / `Korath` | invariati | 5/4/5/1/2/1 | la quinta "Hai" italiana è il verbo *hai* (unità 69) |
| `Coalition` | Coalizione | 1 → 1 | — |
| `Syndicate` | Sindacato | 1 → 1 | — |
| `Republic's Navy` / `Navy flagship` | Marina della Repubblica / nave ammiraglia della Marina | 2 → 2 | — |
| **`Earth`, `Mars`, `the Moon`** | **Terra, Marte, la Luna** | 6 / 4 / 1 | corpi reali: eccezione deliberata già usata per Marte e Giove |
| `Earth families`, `Earth trends` | "famiglie terrestri", "mode terrestri" | — | due dei sei `Earth` diventano aggettivo |
| `House Mallob` | Casata Mallob | 3 → 3 | — |
| `the Rim` | il Rim | 3 → 3 | una resa è "mondi del Rim" (preposizione articolata) |
| `the Deep` | il Deep | 6 → 6 | invariato |
| `CCOR` | invariato | 1 → 1 | con "Bordo Esterno" già sciolto in L10 |
| `longcows` | bovini lunghi | 1 → 2 | l'italiano ripete il nome dove l'inglese usa il pronome |
| `Bulk Freighter`, `skyhook` | invariati | 1 / 1 | convenzioni L7 e L5 |
| `hyperdrive fuel` | carburante per iperpropulsore | 1 → 1 | glossario |
| `arcology` | arcologia | 1 → 1 | convenzione L3d |
| `ramscoops` | raccoglitori magnetici | 1 → 1 | — |
| `Aviskir`, `Ada`, `Ahr`, `Alpherg`, `Ritilas`, `Han Sizer`, `New Reykjavik` | invariati | — | nomi propri |

---

## 3. Intervento imposto dal controllo (un FAIL reale)

`check.py` ha segnalato **unità 26**: virgolette `2 vs 0`. L'originale dice `on platforms farther "inland,"`
e la mia resa aveva perso le virgolette. Ripristinate: "sulle piattaforme più **"all'interno"** atterrano le
astronavi". Dopo la correzione `FAIL totale: 0`, virgolette 14/14.

---

## 4. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 3 | `skyhook` invariato | convenzione L5, primo riuso in un contesto tecnico |
| 6 | `"Fourth Port"` → "Quarto Porto" fra virgolette | il nome è ironico e va conservato come citazione |
| 15 | `hothouse world` → "mondo serra" | evita "effetto serra" che indica il fenomeno |
| 17 | `"spaceport"` → `"spazioporto"` fra virgolette | l'ironia dell'originale resta |
| 39 | motto `"strong as the mountains, spacious as the skies"` → "forti come le montagne, spaziosi come i cieli" | virgolette conservate |
| 45 | `bone dry` → "asciutta fino all'osso" | — |
| 47 | `buffets your vessel with high winds` → "sbatte la tua nave con venti forti" | — |
| 55 | `genome modifications` → "modifiche al proprio genoma" | — |
| 67 | `city-ships` → "navi-città" | — |
| 74 | `ill-behaved species of multi-legged cattle` → "specie caratteristica e maleducata di bestiame dalle molte zampe" | registro ironico conservato |
| 79 | `"tributation"` → `"tributazione"`; `'elves:'` → `'elfi:'` | il termine inventato si rende con un calco trasparente; apici singoli e due punti conservati |
| 82 | `diamond rains` → "piogge di diamanti" | — |
| 83 | `"Midnight Star"` → "Stella di Mezzanotte" | soprannome tradotto, virgolette conservate |

---

## 5. Incoerenze e decisioni aperte (non bloccanti)

1. **`"tributation"` → "tributazione"** (1): termine inventato dal gioco. Il calco funziona ("tributo"),
   ma se il termine ricompare in testi di missione va tenuto identico.
2. **`skyhook` invariato** (1): secondo uso dopo L5; la scelta è ormai stabile.
3. **Coppie di unità quasi identiche** (23/24 Mainsail, 36/37 Mani, 48/49 Mavra-Sol-Kvel, 76/78 Midgard):
   sono varianti presenti nel sorgente. Differenze conservate — in 24 "come la tua", in 78 "ed è il mondo in
   cui sei nato", che è un riferimento al passato del giocatore.
4. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `Consigli Confederati` (L10/L12) vs
   `Confederated Councils` (L6), `caveau`, `ringroide`, `Halite`, `Bulk Freighter`, `Costruttori`,
   `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`, `Egemonia Bunrodean`, `Wanderers`, istituzioni in
   inglese.

---

## 6. Esito dei controlli

```
unità 83 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4470 -> 4534 · ratio 0.89-1.20
tab 27 (tutti gli iniziali conservati) · virgolette 14 (7 coppie) · token <...> 0
riga grezza identica al file: 83/83 · english/kind/path/state identici al DB: 83/83
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Primo passaggio: `FAIL totale: 1` (unità 26, virgolette). **Dopo la correzione: `FAIL totale: 0`.**

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
