# REPORT — L101 · `hai culture conversations.txt` (chiude il file)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Hai Film Release` | 321–331 | 5 | la locandina di Likeet, il titolo «L'ultimo riposo», le due varianti della visione |
| `Sick of Acorn Bread` | 346–386 | 21 | ristorante o venditore ambulante, la cameriera, il vicino e la memoria dei pani perduti |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Darkrest` · `Likeet` · `Newhome` | **invariati** | nomi propri (stazione, persona, pianeta) |
| `"The Final Rest"` | **«L'ultimo riposo»** | calco del gioco di parole su *Darkrest* |
| `hayipp bread` · `yur ki bread` | **pane hayipp** · **pane yur ki** | nomi di cibi Hai, invariati |
| `acorn bread` | **pane di ghiande** | coerente con «burro di ghiande» (L100) |
| `'corn'` · `'sheep'` | **'granturco'** · **'pecora'** | fra apici come nel sorgente, è il traduttore che cita |
| `hostess` | **cameriera** | `hostess` di sala; «padrona di casa» sarebbe fuori registro |
| `tuxedos` · `overalls with holes for their tails` | **smoking** · **tute da lavoro con un buco dietro per la coda** | |
| `grunts noncommittally` | **grugnisce in modo evasivo** | |
| `scampers off` | **sgambetta via** | stesso verbo di *caper* in L100 |
| `buttery and tender` | **burroso e tenero** | |
| `beeps melodically, incinerating the refuse` | **emette un bip melodioso mentre incenerisce i rifiuti** | |
| `wholesome ruddy brown flour` | **farina integra di un bruno rossastro** | |
| `rich and decadent` | **ricco e sontuoso** | |
| `wistful look` · `downcast` | **sguardo malinconico** · **abbattuto** | |
| `displaced … from high traffic areas` | **ha spostato … dalle zone ad alto passaggio** | |
| `[seat, rest]` | **[a sedere, a riposare]** | alternativa del dispositivo: le quadre restano |
| `sparse on dialog` | **scarso di dialoghi** | |
| `distinctly unnerved` | **decisamente scossi** | |

## 3. Difficoltà

1. **Le quadre in un solo punto**: l'unità 13 le aveva, la mia prima stesura le aveva **perse** («Si accomodi
   pure dove preferisce!»). L'asserzione del costruttore ha fermato la build **prima** che il difetto arrivasse
   nel `translation.json`: è il caso in cui il controllo vale più di dieci riletture.
2. **Due trattini lunghi** nelle unità 19 e 25: la tipografia del progetto li vieta. Sostituiti con virgole e
   congiunzione; il `check.py` li ha segnalati come `em dash` e come «caratteri non latini» (due controlli, un
   solo difetto).
3. **`hostess` = cameriera**: in inglese è chi accoglie e assegna il tavolo, ma qui prende anche l'ordine — la
   resa «cameriera» copre entrambe le funzioni, e il testo la chiama una volta sola.
4. **Il vicino parla per tre unità** (19, 23, 25) e il suo tono cambia: risentimento → scuse → memoria. La resa
   segue il cambio, non lo appiattisce.
5. **Chiusura del file**: il `verify.py` legge i `translation.json` di tutti e quattro i lotti del path e
   asserisce 147 id distinti su 147 righe, 0 sovrapposizioni, 39 + 38 + 44 + 26.

## 4. Numeri osservati

```
unita' 26/26 · tab 24 · virgolette 34 = 34 (8 nella 25) · token 0 · quadre 1 coppia (unita 13)
parole EN 971 -> IT 938 · rapporto 0.75 - 1.39
righe 321/386 · file 147 unita · max(line) 386 · 121 prima / 0 dopo
FAIL totale: 0 (26 controlli) · verify exit 0 (29 controlli, invariante di file)
sha256[:16] b32aaa185052d185 · file 147/147 · 4 lotti · 5003 EN -> 4781 IT
```

## 5. Stato del progetto

```
TOTALE staging: 25291 unita · 811369 EN · 769129 IT
hai culture conversations.txt: 147/147 (100%) · 4 lotti · CHIUSO
file completi: 39 · residuo traducibile (formula state.py): 6639
residuo misurato: 7214 unità / 164678 parole su 127 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (29 controlli), file **147/147** |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 26 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file è chiuso, la campagna no**: restano **7.214 unità / 164.678 parole** su **127 file**; il prossimo
  contratto è `HANDOFF_L102_20261018.md` (`quarg missions.txt`, righe 1–117, un **tipo nuovo**: `LOGBOOK`).
- **Nessuna revisione umana**.
