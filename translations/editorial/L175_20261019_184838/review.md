# REVIEW — L175 · `avgi ships.txt` (Phononos, Frequentia, Polari, Entasi)

Coppie EN→IT rilette in `translation.json` (`0bb78b20aa2af987…`). Tutte le 10 unità sono **`PENDING`**.

## 1. Voce

Quattro schede con **umori diversi**: il Phononos è **cupo e tecnico** (un bombardiere riciclato, «vulnerabile alla
pirateria», «tassi di incidenti più alti»); la Frequentia è **autoironica** (la porta di stiva «notoriamente piccola»
rende il carico «un processo estremamente penoso»); la Polari è **istituzionale** (laboratorio, sensori, richieste alla
`Twilight Guard`); l'Entasi è **brutale e concreto** (tagliare asteroidi, raccogliere minerali). La resa segue ciascun
registro invece di uniformarli.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `automated freighter` | **mercantile automatizzato** | 2 |
| `an expanded internal tank` | **un serbatoio interno ampliato** | 2 |
| `ungainly cargo receptacle` | **sgraziato vano di carico** | 5 |
| `exquisitely painful process` | **processo estremamente penoso** | 5 |
| `contested battlespace` | **spazio conteso** | 8 |
| `post-Incursion Avgi cluster` | **cluster Avgi successivo all'Incursione** | 8 |
| `mid-sized mining vessel` | **nave mineraria di medie dimensioni** | 9 |
| `a potent warship` | **una potente nave da guerra** | 10 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`TEXT` può essere un nome**: `Z-333 "Spark" Fusion Torch` resta identico, virgolette comprese.
2. **`Dissonance` e `Aberrant` sono nomi di fazione**, non aggettivi: non si traducono e non si declinano.
3. **`Twilight Guard` resta inglese**: è un'istituzione.
4. **I possessivi inglesi non hanno equivalente italiano**: 3 apici in inglese, zero possessivi in italiano.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 10 unità `PENDING`.
- **Nessuna astronave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Secondo lotto di `avgi ships.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (22 controlli) |
