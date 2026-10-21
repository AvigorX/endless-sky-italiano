# REVIEW — L134 · `unfettered side missions.txt` (la folla, la consegna, la Lightning Bug)

Coppie EN→IT rilette in `translation.json` (`173cf3edac2a3208…`). Tutte le 8 unità sono **`PENDING`**. Il lotto
**chiude il file**: 159/159.

## 1. Voce

- **La folla** grida: «Non meriti di pilotare questo relitto del passato!», «Hai sprecato la tua occasione per una
  battaglia gloriosa che ti guadagnasse quel diritto!».
- **L'Unfettered importante** è minaccioso e poi affaristico: «Devi consegnarci immediatamente la nave… Ti daremo
  un'altra nave così potrai andartene, ma devi darci l'Anomalocaris!».
- **Il capo della milizia** finge disinvoltura: «Diciamo, per esempio, portarci un Jump Drive… o due…».
- **La narrazione** resta al presente e al «tu»: «Mentre atterri, innumerevoli Hai si dirigono in fretta verso la tua
  nave».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `relic of old` | **relitto del passato** | 1 |
| `You wasted your opportunity for a glorious battle` | **Hai sprecato la tua occasione per una battaglia gloriosa** | 2 |
| `the weapons of the savages` | **le armi dei selvaggi** | 3 |
| `a suitable replacement` | **un sostituto adeguato** | 6 |
| `the local Unfettered militia` | **la milizia locale degli Unfettered** | 6 |
| `blatantly forced casualness` | **una disinvoltura palesemente forzata** | 7 |
| `Jump Drive` | **Jump Drive** | 7 |
| `messy paperwork` | **qualche pratica pasticciata** | 8 |
| `Lightning Bug` | **Lightning Bug** | 8 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il file è chiuso** (159/159): i lotti futuri non lo toccano, e ogni `verify.py` nuovo non deve rivendicarne righe.
2. **Tre asserzioni vuote** in un lotto solo (`VALUE`, `UI_LABEL`, token): la forma da riusare quando un segmento non ha
   niente da controllare.
3. **`Jump Drive` resta inglese**: è il nome di un modulo. Se un revisore lo traducesse, cambierebbe il riferimento al
   bene di gioco.
4. **Il trattino lungo non è ammesso** dalla tipografia del progetto: in unità 6 è diventato una virgola.
5. **La battuta dell'unità 6 non si chiude**: è del sorgente, non un errore della resa.
6. **File nuovo al prossimo lotto**: `starts.txt` ha **18 `CONVERSATION`**, **8 `LOGBOOK`**, **4 `DESCRIPTION`**, **2
   `VALUE`** e **zero token** in 32 unità — e i `VALUE` sono i **nomi degli inizi** (`Endless Sky`, `Deep Desire`).

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 8 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la consegna della nave non è stata «giocata».
- **Nessuna revisione umana**.
- **`unfettered side missions.txt` è completo in staging, non nel gioco**: 159 unità, zero caricate.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (32 controlli, invariante di file) |
