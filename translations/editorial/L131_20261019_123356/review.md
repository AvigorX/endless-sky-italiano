# REVIEW — L131 · `boarding missions.txt` (la coda: il relitto, le riparazioni, la trappola)

Coppie EN→IT rilette in `translation.json` (`ec991eb6a0c3f258…`). Tutte le 76 unità sono **`PENDING`**. Il lotto
**chiude il file**: 240/240.

## 1. Voce

- **La narrazione** è al presente e al «tu»: «Sali a bordo della <origin> e ti guardi attorno nel suo scafo
  abbandonato».
- **La procedura di riparazione** ha un lessico fisso, ripetuto su ogni ramo: *scafo*, *motori*, *alimentazione*,
  *valvola secondaria*, *refrigerante*, *sovratensione*. La coerenza è verificata con parole-spia.
- **Il tono da manuale** convive con il momento comico: «sei sicuro di sembrare un eroe d'azione mentre attraversi il
  portello a tutta velocità verso la salvezza».
- **La trappola dei pirati** cambia registro: «avverte dell'arrivo di "astronavi ostili" nel sistema».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `repair the power` | **riparare l'alimentazione** | 8, 14, 16, 26, 28 |
| `repair the hull` / `the engines` | **riparare lo scafo** / **i motori** | 6, 7, 10, 11, 13, 19, 25, 31, 37, 40 |
| `powersurge` | **sovratensione** | 12, 15, 18, 21 |
| `secondary valve is mechanical` | **la valvola secondaria è meccanica** | 24, 27 |
| `restored power` | **hai ripristinato l'alimentazione** | 30, 33 |
| `coolant` | **refrigerante** | 24, 27, 30, 33, 47 |
| `thrums to life` | **vibra e prende vita** | 23, 35, 44, 50 |
| `with bated breath` | **con il fiato sospeso** | 23, 35, 44 |
| `bolt for the airlock` | **scattare verso il portello** | 22, 34, 43 |
| `action hero` | **eroe d'azione** | 56, 57, 58 |
| `loot and pilfer some outfits` | **saccheggiare e portarti via qualche modulo** | 59 |
| `hostile spacecraft` | **"astronavi ostili"** | 60 |
| `malicious software` | **software malevolo** | 61 |
| `rigged to blow` | **preparata a esplodere** | 60 |
| `derelict hunters` | **cacciatori di relitti** | 71 |
| `creak and groan` | **scricchiolare e gemere** | 72, 74 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il file è chiuso** (240/240): i lotti futuri non lo toccano, e ogni `verify.py` nuovo non deve rivendicarne righe.
2. **Le frasi di riparazione sono costanti**: se un revisore cambia «scafo» in «carena», deve farlo in tutte le
   occorrenze insieme, perché il controllo confronta i rami.
3. **Le virgolette doppie** (`"astronavi ostili"`) sono nel testo e restano: non diventano caporali.
4. **Zero `VALUE` e zero `UI_LABEL`**: due asserzioni vuote scritte; un lotto che ne introducesse uno le farebbe
   scattare.
5. **Il registro tecnico** (`alimentazione`, non «energia») è una scelta di coerenza con i lotti precedenti del
   progetto: va mantenuta nei file di navi e missioni.
6. **File nuovo al prossimo lotto**: `unfettered side missions.txt` ha **3 `UI_LABEL`**, **1 `LOGBOOK`**, **1
   `DIALOG`**, **89 virgolette** in una finestra di 84 unità — forma da misurare da zero.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 76 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: il relitto non è stato abbordato, i rami di riparazione non sono stati «giocati».
- **Nessuna revisione umana**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (31 controlli, invariante di file) |
