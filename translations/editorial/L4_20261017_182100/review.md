# L4 — Revisione editoriale del blocco `data/map planets.txt` 6383–6802

83 descrizioni, 4.734 parole inglesi → 4.752 italiane. Continua L3d senza sovrapposizioni (0 ID in
comune con L1, L2, L3, L3b, L3c, L3d). Il blocco inizia con `planet:Varu K'prai` e chiude il file con
`planet:Zydee` (riga 6802, ultima unità di `map planets.txt`).

**Il lotto include anche la coda di 4 unità (6783–6802)** che il checkpoint indicava come residuo separato:
così la parte di `map planets.txt` a partire dalla riga 3851 è tradotta per intero.

**Attenzione, verifica che smentisce una prima stesura:** `map planets.txt` **non** è tradotto per intero.
Le 1544 unità `PENDING` del file si dividono in **673 tradotte** (righe 3851–6802, L1 + L2 + L3 + L4) e
**871 mai affrontate** (righe 17–3845, 48.092 parole), che precedono il punto in cui L1 è iniziato.
Quelle 871 unità restano il lavoro principale sul file.

---

## 1. Metodo

Impianto identico ai lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–83), rilettura
del solo italiano.

Le 83 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 83 (verificato in `verify.py`, che conferma anche **0 unità residue dopo
la riga 6802**).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Wanderers` | invariato | 4 → 12 | l'inglese usa anche la forma aggettivale e possessiva; l'italiano ripete il sostantivo |
| `the Unfettered Hai` | gli Hai Unfettered | 1 → 1 | fazione, invariata |
| `Remnant` | invariato | 5 → 5 | fazione |
| `defense prefects` | prefetti della difesa | 1 → 1 | gerarchia Remnant |
| `Key Stones` | Pietre Chiave | 1 → 1 | nome di oggetto; da allineare se il nome dell'equipaggiamento viene localizzato |
| `wormhole` | invariato | 1 → 1 | termine tecnico (decisione L3 §7) |
| `Ember Waste`, `Tangled Shroud` | invariati | 1 / 3 | nomi di regione |
| `the Incursion` | l'Incursione | 1 → 1 | convenzione L2 |
| `Aberrant` | invariato | 1 → 1 | fazione Avgi |
| `House Seineq`, `Houses Aqrabe and Kaatrij` | Casata Seineq, Casate Aqrabe e Kaatrij | 2 → 5 | convenzione L1; l'italiano ripete "Casata/Casate" |
| `New Houses` | Nuove Casate | 2 → 2 | convenzione L1 |
| `Republic` | Repubblica | 2 → 2 | — |
| `Earth` | Terra | 2 → 1 | eccezione deliberata; un caso reso con "terrestri" |
| `Alpha Wars` | invariato | 1 → 1 | convenzione L1 |
| `Hot Jupiter` | Giove caldo | 2 → 2 | classe astronomica, non nome proprio |
| `gas dwarf` | nano gassoso | 1 → 1 | termine astronomico italiano |
| `spaceport` | spazioporto | 20 → 19 | unità 36: "spaceport facilities" → "strutture portuali" |
| `landing pad` | piazzola di atterraggio | 8 → 7 | unità 42: secondo caso reso con pronome ("alcune sono dotate di…") |
| `kelp` | laminarie | 1 → 2 | unità 43 rende *seaweed* con "laminarie", da cui il conteggio maggiore |

---

## 3. Interventi fatti in stesura e rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 5 | "un mondo già morto e senza vita - molto meglio" | "…senza vita: molto meglio" | trattino lungo non ammesso dal set Latin-1 |
| 8 | "dove il bedrock circostante è più fresco" | "dove il basamento roccioso circostante è più fresco" | anglicismo |
| 10 | "Veiuye … Veiyue" | "Veiuye" in entrambi i casi | il sorgente ha un refuso; si uniforma al nome del nodo |
| 42 | "Le piazzole di atterraggio sporgono… Alcune sono dotate…" | invariato dopo verifica | il pronome evita la ripetizione, conteggio verificato |
| 61 | "classificato come Hot Jupiter" | "\"Giove caldo\"" | classe astronomica tradotta, virgolette conservate |
| 81 | "con un'architettura più audace e un design più moderno" | "…e una linea più moderna" | anglicismo |
| 21 | boilerplate "mothballed" | **identico** all'unità 21 di L3 | stesso inglese → stessa traduzione (memoria di traduzione) |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Key Stones` → Pietre Chiave** (1): è un oggetto che abilita i viaggi nei wormhole dell'Ember Waste.
   Se il nome dell'equipaggiamento compare nella UI, la resa deve essere la stessa; altrimenti resta
   invariato "Key Stone".
2. **`Wanderers` invariato** (4 nell'inglese): confermata la scelta di L3d.
3. **Coerenza inter-lotto verificata:** l'unico testo inglese ripetuto fra lotti è il boilerplate della
   stazione in disarmo; l'unità 21 di L4 (Violetwake) ha la **stessa** traduzione dell'unità 21 di L3
   (Redwatch). Resta l'unica divergenza nota e documentata: unità 70 di L3, variante lessicale volontaria.
4. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `longcows`.

---

## 5. Esito dei controlli

```
unità 83 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4734 -> 4752 · ratio 0.93-1.28
tab 23 (tutti gli iniziali conservati) · virgolette 8 · token <...> 0
riga grezza identica al file: 83/83 · english/kind/path/state identici al DB: 83/83
unità residue dopo la riga 6802: 0 (file esaurito)
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
