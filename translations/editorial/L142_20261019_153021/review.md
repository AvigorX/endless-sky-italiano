# REVIEW — L142 · `unfettered 0 prologue.txt` (la vendita del motore di salto)

Coppie EN→IT rilette in `translation.json` (`1e2c9c50567e62e1…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce

- **Gli Slegati** trattano con la solennità di chi compra un regno: «Un milione di crediti, e l'amicizia del vero popolo
  Hai. Questa è la nostra offerta, per il motore di salto.»
- **La minaccia** è implicita, e la narrazione la nomina: «Non puoi fare a meno di chiederti se proveranno a prendere la
  tua nave con la forza se non accetti l'accordo.»
- **L'addio** è da cerimonia: «che la fortuna ti assista, amico umano».
- **Il giocatore** resta pratico: «"Come farà la mia nave a partire senza il mio motore di salto?"»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `More Jump Drives` | **identico** | 1 |
| `One million credits` | **Un milione di crediti** | 6 |
| `the true Hai people` | **il vero popolo Hai** | 6 |
| `hyperdrive` · `jump drive` | **iperpropulsore** · **motore di salto** | 10, 16, 17 |
| `in working condition` | **in condizioni di funzionare** | 11 |
| `under threat of violence` | **sotto minaccia di violenza** | 10 |
| `may fortune favor you, human friend` | **che la fortuna ti assista, amico umano** | 19, 20 |
| `(No.)` | **`(No.)`** | 4 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il rifiuto (13 e 18) deve restare identico**: due strade portano alla stessa frase.
2. **`(No.)` è identico per necessità**: è in `ID_OK`; tradurlo sarebbe sbagliato, escluderlo dai controlli lo
   nasconderebbe.
3. **La missione è chiusa** (20/20): i lotti futuri partono da `Unfettered Jump Drive 2`, riga 214.
4. **`More Jump Drives` ricomparirà** come `VALUE` anche nella missione 2: stesso nome, stesso trattamento.
5. **`The Unfettered engineers retrieve…` vs `remove… and replace…`**: le due chiusure differiscono di un gesto, e la
   resa lo rispetta («recuperano» contro «rimuovono e sostituiscono»).

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità restano `PENDING`.
- **Nessuna missione giocata**: lo scambio non è stato visto a schermo.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 44,2%**: 82 unità da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (26 controlli, invariante di segmento) |
