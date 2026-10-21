# L5 — Revisione editoriale del blocco `data/map planets.txt` 17–356

84 descrizioni, 4.632 parole inglesi → 4.578 italiane. È il **primo lotto che copre il tratto iniziale del
file** (righe 17–3845), rimasto intatto fino a ora: 0 ID in comune con L1–L4. Inizia con
`planet:Aava-Aasa-Khora` e si chiude a fine pianeta con `planet:Arroharg` (riga 356); l'unità 357
appartiene ancora ad Arroharg ed è esclusa.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–84), rilettura
del solo italiano.

Le 84 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 84 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Old Houses` / `New Houses` | Vecchie / Nuove Casate | 1 / 1 | convenzione L3c–L3d |
| `Predecessors` | Predecessori | 1 → 1 | eccezione deliberata |
| `Successors` | invariato | 3 → 3 | fazione |
| `Coalition` | Coalizione | 2 → 2 | decisione L2 |
| `Avgi`, `Quarg`, `Hai`, `Kimek`, `Arach`, `Bunrodean`, `Korath`, `Remnant`, `Aberrant`, `Heliarch` | invariati | 11/6/3/1/3/2/2/1/2/1 | specie e fazioni |
| `Tangled Shroud`, `Ember Waste`, `the Deep` | invariati | 1 / 2 / 1 | nomi di regione |
| `the Incursion` | l'Incursione | 4 → 4 | convenzione L2 |
| `hyperdrive` | iperpropulsore | 3 → 3 | decisione L2 |
| `Remembrance Day`, `Alpha Wars` | invariati | 2 / 2 | convenzioni L1 |
| `Earth` | Terra | 1 → 1 | eccezione deliberata |
| `ringworld` | mondo ad anello | 1 → 1 | unità 42; "anello" da solo indica la struttura fisica |
| `antimatter` | antimateria | 9 → 10 | unità 66–69; una ripetizione in più per chiarezza del periodo |
| `regolith` | regolite | 2 → 2 | termine geologico italiano |
| `spaceport` | spazioporto | 24 → 23 | unità 26: "spaceport town" → "cittadina portuale" |
| `landing pad` | piazzola di atterraggio | 2 → 2 | glossario |

---

## 3. Interventi fatti in stesura e rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 27 | `"Niente tassi, donnole o puzzole"` | `"Niente tassi, donnole o polecat"` | la battuta finale ("non hai idea di cosa sia un polecat") funziona solo se il termine resta opaco al lettore italiano |
| 27 | virgolette mancanti sull'ultima occorrenza | `"polecat"` | il controllo ha segnalato 6 virgolette nell'inglese contro 4: ripristinata la terza coppia |
| 35 | "torri petrolifere" | "torri di perforazione" | *oil derricks* |
| 44 | "mobili" (arte) | "sculture cinetiche" | *mobiles* nel senso artistico |
| 46 | "i pezzi di artiglieria erano posizionati" | "vede dove erano posizionati i pezzi d'artiglieria" | sintassi più naturale |
| 58 | "aurote vellutate" | "aurore verde smeraldo e vellutate" | resa di *emerald and velvet auroras* |
| 66 | "acceleratore sincrotrone" | "acceleratore di particelle di tipo sincrotrone" | precisione tecnica |
| 80 | "raso al suolo dall'orbita" | "polverizzato dall'orbita" | *razed from orbit* riguarda il bombardamento, non il suolo |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`polecat` lasciato in inglese** (1, unità 27): unico caso in cui un termine inglese resta nel testo
   per non distruggere una battuta. Va registrato come eccezione stilistica, non come svista: il glossario
   non lo copre.
2. **`skyhook` lasciato invariato** (1, unità 80): termine tecnico orbital; l'alternativa italiana è
   "gancio celeste". Da decidere se tradurlo quando ricorre in altri file.
3. **Coerenza interna dei doppioni di Antipode:** le unità 59 e 61 condividono la seconda frase inglese e
   hanno la stessa resa italiana; 60 e 63 sono varianti e sono state tradotte con lo stesso incipit.
4. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `longcows`,
   `Key Stones`, `Pietre Chiave`.

---

## 5. Esito dei controlli

```
unità 84 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4632 -> 4578 · ratio 0.85-1.22
tab 33 (tutti gli iniziali conservati) · virgolette 14 · token <...> 0
riga grezza identica al file: 84/84 · english/kind/path/state identici al DB: 84/84
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Un errore trovato e corretto dal controllo: unità 27, virgolette 6 → 4 (poi ripristinate a 6).

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
