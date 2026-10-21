# L3b — Revisione editoriale del blocco `data/map planets.txt` 5129–5456

84 descrizioni, 4.504 parole inglesi → 4.516 italiane. Continua la sezione 1 di L3 senza
sovrapposizioni (0 ID in comune, verificato). Il blocco inizia con `planet:Sarisa Fentra` e si chiude
con l'ultima descrizione di `planet:Silver`; l'unità successiva del file (riga 5465, `planet:Silwan`)
è fuori intervallo.

---

## 1. Metodo

Impianto identico a L1/L2/L3: lettura del contesto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–42, 43–63, 64–84), rilettura
del solo italiano, correzione dei calchi.

Le 84 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`) e la riga grezza
è stata riletta dal file: `raw` coincide con la riga del sorgente per tutte le 84 unità.

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Successors` | invariato | 6 → 7 | fazione/specie, con articolo italiano |
| `House Myurej` | Casata Myurej | 2 → 2 | convenzione L1 |
| `Predecessors` | Predecessori | 1 → 1 | eccezione deliberata |
| `Coalition` | Coalizione | 2 → 2 | decisione di L2 |
| `Syndicate` | Sindacato | 1 → 1 | convenzione L1 |
| `Earth` | Terra | 2 → 1 | eccezione deliberata; un caso reso con "umana" |
| `Remnant` | invariato | 1 → 1 | fazione |
| `Saryd`, `Kimek`, `Arachi`, `Korath`, `Avgi`, `Heliarch`, `Quarg`, `Hai`, `Vi`, `Gegno`, `Efreti`, `Kor Sestor` | invariati | — | specie e fazioni |
| `ringworld` | mondo ad anello | 1 → 1 | categoria descrittiva |
| `spaceport` | spazioporto | 26 → 26 | glossario |
| `landing pad` | piazzola di atterraggio | 3 → 3 | convenzione L1/L2 |
| `Bulk Freighters` | mercantili pesanti | 1 → 1 | convenzione L1 |
| `arcologies` | arcologie | 2 → 2 | prestito tecnico invalso |
| `ringroids` | ringroide / ringroidi | 2 → 2 | neologismo del gioco, adattato alla morfologia italiana |
| `world-ships` | navi-mondo | 1 → 1 | — |
| `automata` | automi | 1 → 1 | — |
| `blast furnace` | altoforno | 1 → 1 | — |
| `fissionable materials` | materiali fissili | 1 → 1 | — |
| `speleothems` | speleotemi | 1 → 1 | termine geologico italiano |
| `dry dock` | bacino di carenaggio | 1 → 1 | — |
| `strip mines` | miniere a cielo aperto | 1 → 1 | — |
| `alloy platings` | piastre in lega | 2 → 2 | — |
| `Starlit University` | invariato | 1 → 1 | nome di istituzione |
| `Shangri-La`, `Shih's Locker`, `Greenrock`, `Polaris` | invariati | — | nomi propri |

---

## 3. Correzioni fatte in rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 3 | "molti scelgono di dedicare" | "molti preferiscono dedicare" | evita la ripetizione di "scegliere" nella stessa frase |
| 41 | "solo una serie di spiazzi pianeggianti e sgombrati in cima a un altopiano isolato" | "solo spiazzi pianeggianti sgombrati in cima a un altopiano" | resa troppo lunga per una frase breve (rapporto 1,54 → 1,31) |
| 50 | "l'equivalente Korath del barbecue" | "l'equivalente Korath di una grigliata" | anglicismo evitabile |
| 58 | "quanto sei lontano dai margini della civiltà" | "quanto tu sia ai margini della civiltà" | calco di *how far on the fringes* |
| 63 | "l'infame capitano Shih" | "l'infame capitana Shih" | il testo inglese usa "her": capitana donna |
| 72 | "i pochi élite del pianeta" | "i pochi privilegiati del pianeta" | "élite" come sostantivo plurale è innaturale |
| 78 | "non sembrano esserci molti civili" | "non sembra esserci molto personale non militare" | aderenza a *non-military personnel* |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`ringroids` → ringroide/ringroidi** (3): neologismo del gioco assente dal glossario. Adattato alla
   morfologia italiana; l'alternativa è l'invariato "ringroid".
2. **`Starlit University` invariato** (1): nome di istituzione. Se si preferisce l'adattamento,
   "Università Stellata" — decisione da prendere una volta per tutto il corpus.
3. **`Vi` invariato** (5) con articolo italiano ("i Vi"): coerente con le altre specie.
4. Restano aperte da L3: `Successors` invariato vs "Successori"; `il Rim`; `caveau`; `wormhole`.
   **0 occorrenze in questo blocco**: `Consonance`, `Paradise World`, `New Houses`, `Dirt Belt`.

---

## 5. Esito dei controlli

```
unità 84 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4504 -> 4516 · ratio 0.93-1.36
tab 23 (tutti gli iniziali conservati) · virgolette 10 · token <...> 0
riga grezza identica al file: 84/84 · english/kind/path/state identici al DB: 84/84
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
