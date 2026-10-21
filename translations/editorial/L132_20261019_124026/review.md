# REVIEW — L132 · `unfettered side missions.txt` (il disertore Hai e l'Anomalocaris)

Coppie EN→IT rilette in `translation.json` (`4fcdf80f4d1d3888…`). Tutte le 84 unità sono **`PENDING`**.

## 1. Voce

- **Il giovane Hai** parla in modo semplice e diretto: «Sei tu il <first> <last>, vero?», «Mi porterai su
  Hai-home?».
- **I due incappucciati** parlano per enigmi e mezze verità: «La meno sai, meglio è per tutti noi, capitano», «È
  difficile trovare una goccia di pioggia in una tempesta, ma la goccia può vedere tutto mentre cade».
- **La narrazione** è al presente e al «tu»: «Durante la notte senti un leggero rumore di graffi sul portello
  principale della tua nave».
- **Il registro tecnico** resta coerente con i lotti precedenti: *portello*, *cabine*, *scorte*, *cantiere*,
  *pilota automatico*.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Hai-home` | **Hai-home** | 6, 12, 16, 18 |
| `the "tribute"` | **il "tributo"** | 6 |
| `'Hai-home is your home too. Rejoin your people.'` | **'Hai-home è casa tua. Torna al tuo popolo.'** | 6 |
| `Anomalocaris` | **Anomalocaris** | 59, 84 |
| `the savage Korath` | **i selvaggi Korath** | 61 |
| `ten million credits in cash` | **dieci milioni di crediti in contanti** | 27 |
| `hooded figure` | **figura incappucciata** | 19, 23, 26, 34 |
| `lucrative business proposition` | **lucrosa proposta d'affari** | 24 |
| `solitary affair` | **faccenda solitaria** | 25 |
| `relic of the past` | **relitto del passato** | 59 |
| `geyser of sand` | **geyser di sabbia** | 79 |
| `autopilot` | **pilota automatico** | 77 |
| `a loan was issued in lieu of a conventional purchase` | **è stato emesso un prestito al posto di un acquisto convenzionale** | 84 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Hai-home` non si traduce**: è il nome del pianeta. Un lotto futuro che lo rendesse «casa degli Hai» romperebbe
   il riferimento, e il controllo lo vieta esplicitamente.
2. **Le virgolette possono annidarsi**: singole dentro doppie (unità 6). Il conteggio per unità è l'unico modo per non
   perdere le une o le altre.
3. **Tre unità con una sola virgoletta** (57, 62, 73): sono battute non chiuse dal sorgente, non sviste della resa.
4. **`(No.)` è identico** in italiano: è dichiarato, non dimenticato.
5. **Il file ha ancora 75 unità**: `Hai Legacy 2` (10), `Hai Legacy 3` (57), `Undeserved Anomalocaris` (8). Il lotto
   successivo ne prende 67 e ne lascia 8, che chiudono il file.
6. **`<date>` e `<system>`** compaiono solo nei lotti successivi: due famiglie di token nuove per questo file.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 84 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la missione non è stata vista, e l'Anomalocaris non è stato comprato davvero.
- **Nessuna revisione umana**.
- **Il file non è completo**: restano 75 unità (righe 237–510).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (32 controlli) |
