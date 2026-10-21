# REVIEW — L198 · `hai jobs.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`7465d06d0b238ebf…`). Tutte le 51 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`VALUE` identici all'inglese (22/22)**: `Delivery to <planet>`, `Bulk delivery to <planet>`, `Large bulk delivery to <planet>`, `Rush delivery to <planet>`, `Large rush delivery to <planet>`, `Hai "prison" cruise to <planet>`, `<planet> business convention`. Sono nomi di lavoro in bacheca: la convenzione misurata da L117 in poi li lascia inglesi.
2. **`operai tessili`** (unità 2): la resa esiste già in staging per la stessa stringa e si riusa **alla lettera** — nessuna variante.
3. **`operai di fabbrica`** (unità 4): la stringa non aveva precedente; si applica la cornice già fissata (`Questa famiglia di <bunks> X spera di trovare lavoro su <destination>, e ti pagherà <payment> per portarla lì.`), cambiando solo il mestiere.
4. **`Consegna <cargo> su <destination>. Il pagamento è <payment>.`** (11 copie): scelta fra tre rese precedenti. Motivi: è già in staging, è quella dei lotti L196–L197 dello stesso file, e `Il pagamento è` è la formula usata anche dalle unità 45 e 48 di questo lotto. `compenso` avrebbe introdotto due formule nello stesso lotto.
5. **`Consegna <cargo> su <destination> entro il <date>.`** (8 copie): fra le due rese precedenti si sceglie quella con l'articolo (`entro il <date>`) e con `Il pagamento è`, per la stessa ragione.
6. **`ogni fortuna … e incassi`** (unità 1, 3, 5): è la resa di L22 per le tre varianti sorelle (minatori, contadini, operai). L'ho adottata qui **e** ho riallineato L197, che aveva deviato.
7. **`in una cella`** per *in a brig*: è la resa già usata in staging per `brig`.
8. **`cinguettando`** per *chittering*: gli Hai «cinguettano» nei testi già tradotti.
9. **`convention d'affari`** per *business convention*: prestito d'uso comune in italiano, più preciso di «congresso» (che è politico/scientifico). Nessun precedente in staging: è la prima occorrenza, e la scelta è dichiarata.
10. **`i <bunks> del gruppo`** (unità 45): l'inglese `the <bunks> of them` è ellittico; il genitivo italiano lo rende esplicito senza aggiungere informazione.

## 2. Due correzioni fatte prima di dichiarare il lotto

1. **L197 unità 35**, riallineata alla resa di L22 (`Auguri alla famiglia di minatori ogni fortuna… e incassi…`). Era una divergenza mia, non rilevata dal `check.py` di L197 perché confrontava con lo staging solo due stringhe. L197 è stato rieseguito: `check.py` e `verify.py` a exit 0, sha `f03d5d9459bc4414` → `0ff30f8bb315b0ad`, documenti aggiornati.
2. **`verify.py` di L198**: corretto un confronto a catena (`sum(...) == 1 == 3 - 2`) **prima** di eseguirlo. La trappola 51 è già nel repertorio e stavolta l'ho presa in tempo.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 51 unità `PENDING`.
- **Nessun lavoro accettato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le incoerenze del gioco si conservano.
- **`deep jobs.txt` non toccato**: il vecchio «3 sospette» resta da verificare a mano.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/part01.json` + `part02.json`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (21 controlli) |
