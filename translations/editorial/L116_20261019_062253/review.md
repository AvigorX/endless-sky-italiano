# REVIEW — L116 · `_ui/tooltips.txt` (chiude il file: interfaccia, regole di gioco, abbordaggio)

Coppie EN→IT rilette in `translation.json` (`9a630cfede888bed…`). Tutte le 133 unità sono **`PENDING`**.

## 1. Voce e registro

- **Impostazioni e regole di gioco**: presente indicativo impersonale o «tu» quando l'effetto ricade sul
  giocatore («non potrai catturare navi che ti porterebbero oltre la capacità», «devi restare il più vicino
  possibile a una stella»).
- **Descrizioni di effetto HUD**: «Mostra le sovrapposizioni di stato sopra le tue scorte in volo».
- **Pannello di abbordaggio**: due frasi brevi e fattuali («Questo oggetto è installato sulla nave. Rimuoverlo
  può rendere la nave inutilizzabile»).
- Nessun «voi» (verificato nei due script).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `status overlay over top of` | **sovrapposizione di stato sopra** | 1–4 | |
| `more powerful missiles relative to your flagship's HP` | **più un missile è potente rispetto ai punti vita dell'ammiraglia** | 5 | |
| `blindspots` · `"blindspots only"` | **angoli morti** · valore invariato | 6 | |
| `highlighted` · `"owned ships"` | **evidenziate** · valore invariato | 8–11 | |
| `mini-map` · `"when jumping"` | **mini-mappa** · valore invariato | 14–17 | |
| `alert indicator` · `"both"` | **indicatore di allarme** · valore invariato | 19–23 | |
| `under-crewed` | **a corto di equipaggio** | 24 | |
| `fixed weapons` · `non-homing weapons` | **armi fisse** · **armi non a inseguimento** | 27–29 | |
| `"focused"` · `"opportunistic"` | invariati | 32–33 | |
| `"expected value"` · `"quality"` | invariati | 36–37 | |
| `"proximity"` · `"value"` · `"mixed"` | invariati | 39–41 | |
| `"never"` · `"frugal"` · `"always"` | invariati | 43–45 | |
| `flotsam` | **detrito** | 46–50 | glossario |
| `"series"` · `"parallel"` | invariati | 52–53 | |
| `carrier` · `docked` | **portatrice** · **attraccate** | 51–56 | |
| `their health drops below 50%` | **la loro salute scende sotto il 50%** | 54 | |
| `ship becomes disabled` | **nave venga messa fuori uso** | 56 | glossario |
| `unpark` | **uscire dal parcheggio** | 59 | |
| `shroud` | **velo scuro** | 62 | |
| `"Sell Outfits"` | invariato | 68 | nome del pulsante |
| `Trading panel` | **pannello del commercio** | 68–70 | |
| `CapsLock` | **blocco maiuscole** | 71 | |
| `"system default"` · `Window rounding` | invariato · **angoli delle finestre** | 88–89 | |
| `"friendly only"` | invariato | 92 | |
| `depreciate` · `grace period` | **svalutarsi** · **periodo di tolleranza** | 94–97 | |
| `person ship` | **nave personaggio** | 98–99 | nave unica legata a un personaggio |
| `"weight"` | invariato | 99 | termine della definizione |
| `"mining"` · `"frugal"` | invariati | 100–101 | personalità delle navi |
| `universal ramscoop` | **`"universal ramscoop"`** invariato | 102 | `ramscoop` è invariante |
| `arrival / departure distance` | **distanza di arrivo / di partenza** | 103–108 | |
| `gamerule` | **regola di gioco** | 107–131 | 11 occorrenze |
| `raid fleets` · `deterrence` | **flotte di razzia** · **deterrenza** | 116 | |
| `"none"` · `"player"` · `"all"` | invariati | 112–114 | |
| `"ship cap,"` · `"crew cap,"` · `"admin cap,"` | invariati **con la virgola interna** | 122–124 | il sorgente la mette dentro le virgolette |
| `administrative capacity` · `administrative cost` | **capacità amministrativa** · `"administrative cost"` invariato | 121–124 | il primo è prosa, il secondo è citato |
| `permadeath` | **morte permanente** | 125 | |
| `"lock on death"` ecc. | invariati | 126–129 | valori di impostazione |
| `snapshots` · `autosaves` | **istantanee** · **salvataggi automatici** | 130 | |
| `cargo hold` | **stiva** | 132 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il file è chiuso**: 667 unità su 667, sei lotti (L111–L116), `sovrapposti = 0`. Il `verify.py` del lotto
   successivo **non** deve tornare «di segmento»: se un altro lotto toccasse questo path, i due invarianti
   dovrebbero convivere.
2. **I quattro contesti iniziali hanno tre spazi** (`tip:   Show flagship overlay`): sono un dato, non una
   distrazione di formattazione.
3. **La virgola dentro le virgolette** (122–124) è del sorgente: `"ship cap,"` resta così anche in italiano.
   Spostarla fuori fa fallire il controllo delle citazioni, e il controllo ha ragione.
4. **`"administrative cost"` resta in inglese perché è citato**, mentre «capacità amministrativa» è prosa e si
   traduce: nello stesso blocco convivono le due cose, e la distinzione è «è fra virgolette?».
5. **`"weight"`, `"mining"`, `"frugal"`** sono termini delle definizioni delle navi personaggio: restano
   invariati come le personalità (`"frugal"` è un valore, non un aggettivo da tradurre).
6. **`(unset)`** è un marcatore del gioco, non una parola: resta così.
7. **Prossimo file**: `data/human/pirate jobs.txt`, primo segmento 20–1624 — 98 unità, 31 contesti, **6 famiglie
   di token** (`<payment>` 36, `<planet>` 31, `<cargo>` 31, `<destination>` 31, `<passengers>` 4, `<bunks>` 3) e
   **31 `VALUE`** che restano identiche (nomi di missione). La tassonomia cambia del tutto: si riparte dalla
   ricognizione dei `kind`, non dal `check.py` di questo lotto.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 133 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: il file è completo in staging, non nel gioco; nessuna sovrapposizione è
  stata vista a schermo.
- **Nessuna revisione umana**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (38 controlli), `verify.py` exit **0** (47 controlli, 667/667 coperte) |
