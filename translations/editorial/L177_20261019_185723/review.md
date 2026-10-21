# REVIEW — L177 · `avgi ships.txt` (Interferos, Diaspersi, Refraktos, Difraktos, Atenuatia)

Coppie EN→IT rilette in `translation.json` (`e962a9325deb075f…`). Tutte le 39 unità sono **`PENDING`**.

## 1. Voce

Cinque schede di **dottrina militare** più che di ingegneria: l'Interferos è **economico e sacrificabile** («i tassi di
perdita lasciano a desiderare»), la Diaspersi è **versatile**, la Refraktos è **specializzata** (un solo obiettivo: le
armi a energia diretta), la Difraktos è **modulare**, l'Atenuatia è **potenza bruta con un compromesso dichiarato**
(«può imbarcare relativamente poche armi pesanti per le sue dimensioni»).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `autonomous support ship` | **nave di supporto autonoma** | 3 |
| `frontline warships` | **navi da guerra di prima linea** | 3 |
| `combat drones` · `wing` | **droni da combattimento** · **stormo** | 10, 36 |
| `radiators` · `thermal loads` | **radiatori** · **carichi termici** | 18 |
| `antimissile coverage` | **copertura antimissile** | 20 |
| `torch drive` | **torcia motrice** | 26 |
| `close-range brawls` | **scontri ravvicinati** | 26 |
| `centerpiece` | **perno** | 36 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`TEXT` = nome, sempre**: 29 su 39 unità. Le 58 virgolette sono 2 per nome e non si toccano.
2. **`Consonance`, `Tangles`, `Diaspora`, `Guard`, `Avgi`** restano inglesi: sono fazione, regione, evento storico e
   istituzione, non aggettivi.
3. **`classe X`** davanti al nome della nave, come in L176.
4. **`Z-666 "Zap" Fusion Torch`** è lo stesso motore visto come `VALUE` in L164: qui è `TEXT` e si copia.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 39 unità `PENDING`.
- **Nessuna astronave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quarto lotto di `avgi ships.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (23 controlli) |
