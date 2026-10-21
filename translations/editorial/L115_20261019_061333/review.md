# REVIEW — L115 · `_ui/tooltips.txt` (avvisi, comandi, opzioni: 72 contesti per 104 unità)

Coppie EN→IT rilette in `translation.json` (`1c8c5a0ff94ca5b2…`). Tutte le 104 unità sono **`PENDING`**.

## 1. Voce e registro

- **Avvisi**: periodo dichiarativo con conseguenza («Se partisse, non potrebbe lasciare questo sistema
  stellare»), non imperativo: il gioco descrive la nave, non impartisce ordini.
- **Etichette di comando**: imperativo diretto al giocatore, con «tu» («Accelera l'ammiraglia in avanti»,
  «Fai virare l'ammiraglia a sinistra», «Apri il pannello della mappa stellare»). Il sostantivo del comando resta
  nel contesto (`tip:Forward thrust`), non nel testo.
- **Opzioni**: presente indicativo impersonale, come le schede di impostazione («Imposta l'allineamento
  orizzontale dei paragrafi nell'interfaccia», «Regola la visualizzazione delle icone…»).
- Nessun «voi» (verificato nei due script).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `no means of generating energy` | **nessun modo di generare energia** | 1 | |
| `run the thrusters / the steering at full power` | **azionare i propulsori / il governo alla massima potenza** | 2–4 | |
| `movement will be diminished` | **la mobilità sarà ridotta** | 4 | |
| `powered entirely by solar energy` | **alimentata interamente da energia solare** | 5 | |
| `insufficient storage` (carburante) | **serbatoio insufficiente** | 6 | |
| `insufficient bays` | **abbastanza baie** | 9 | baie = spazio per le navi trasportate |
| `"surge" energy` | **energia di "picco"** | 10 | etichetta già resa da L113 |
| `considered an atrocity` | **equipaggiamento atroce** | 11 | contesto: `This outfit is considered an atrocity.` |
| `Accelerate your flagship forward` | **Accelera l'ammiraglia in avanti** | 12 | |
| `Turn your flagship opposite its current direction of flight` | **Fai virare l'ammiraglia nella direzione opposta a quella di volo** | 15 | |
| `With <shift>, …` | **Con `<shift>`, …** | 16, 21, 25, 27, 29, 31, 50, 54 | 8 occorrenze, token intatto |
| `double tapping` | **un doppio tocco** | 19 | |
| `travel plan` | **piano di viaggio** | 20–21 | |
| `hail` | **chiamare** | 28–29 | |
| `boardable ship` | **nave abbordabile** | 30 | |
| `Boarding target priority` · `Target asteroid based on` | invariati fra virgolette | 30, 32 | chiavi di `Preferences` |
| `automatic firing` · `Turret tracking` · `focused` · `opportunistic` | invariati fra virgolette | 34, 35 | valori del menu |
| `Settings tab` | **scheda Impostazioni** | 35 | |
| `secondary weapon` | **arma secondaria** | 36–37 | |
| `carried ships`, `carriers`, `bays` | **navi trasportate**, **navi portatrici**, **baie** | 48–49 | |
| `focus fire` · `hold fire` · `gather around me` · `hold position` | **concentrare il fuoco** · **cessate il fuoco** · **radunarsi intorno all'ammiraglia** · **mantenere la posizione** | 51–55 | ordini di flotta |
| `harvest flotsam` | **raccogliere il detrito** | 57 | |
| `zoom factor` | **fattore di zoom** | 59–60 | |
| `text alignment` · `justified` | **allineamento del testo** · `"justified"` invariato | 61–65 | |
| `vsync` · `adaptive` | **vsync** · **adattivo** | 68 | |
| `camera trails behind` · `speeds ahead` | **la visuale resta indietro** · **si porta avanti** | 71–72 | |
| `frames/second` · `ticks/second` | **fotogrammi al secondo** · **cicli al secondo** | 73 | |
| `sobel filter` | **filtro di Sobel** | 88, 91 | nome proprio dell'algoritmo |
| `interpolation method` · `linear` · `nearest` | **metodo di interpolazione** · valori invariati | 96–98 | |
| `status overlays` | **sovrapposizioni di stato** | 99–104 | mostrano scudi e scafo |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le citazioni restano in inglese perché sono chiavi e valori di preferenza**, non prosa: il gioco le usa
   come identificatori (`Preferences::Has("Escorts expend ammo")`) e le mostra così nel menu. I due script lo
   verificano confrontando i testi fra virgolette **per unità**; una traduzione «gentile» delle stesse
   romperebbe il riferimento e il controllo.
2. **Eccezione dichiarata**: unità 10, `"surge"` → **`"picco"`**, perché L113 ha già tradotto quell'etichetta
   nello stesso pannello di potenza. Due nomi per la stessa voce sarebbero un difetto visibile.
3. **72 contesti per 104 unità**: 56 singole, 7 coppie, 5 terne, 2 quaterne, una da cinque (`Text alignment`) e
   una da sei (`Show status overlays`). Un controllo «un contesto per unità» (L114) qui è rosso con la
   traduzione giusta.
4. **I `<shift>` sono 8 e stanno in unità con lo stesso contesto ripetuto** (`Reverse`, `Initiate hyperspace
   jump`, `Select nearest hostile ship`, `Select next ship`, `Talk to selected ship`, `Board selected ship`,
   `Deploy / recall fighters`, `Fleet: Gather around me`): la seconda unità del gruppo è sempre l'alternativa con
   Shift, e il token va lasciato intatto.
5. **23 unità sono voci di elenco** (`- "off": …`): trattino, due punti e citazione sono formato, non stile.
6. **Una ripetizione identica** (89/92) fra due contesti diversi (`Ship outlines in shops` e `in HUD`): resa
   identica, come il sorgente.
7. **La prossima finestra chiude il file** (133 unità, righe 1569–1865): 80 contesti, 144 virgolette, 1 token
   `<shift>`, e il confine è `fine file`, non un contesto. Il `verify.py` di L115, che pretende un'unità
   successiva, va riscritto con l'invariante di **file** (copertura totale su tutti i lotti dello stesso path).

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 104 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun tooltip è stato visto nel pannello; non è verificato che le
  impostazioni citate compaiano davvero con quei nomi inglesi nel menu italiano (la scelta è dichiarata, non
  osservata).
- **Nessuna revisione umana**.
- **Il file non è completo**: 133 unità residue, un solo segmento.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (38 controlli), `verify.py` exit **0** (47 controlli) |
