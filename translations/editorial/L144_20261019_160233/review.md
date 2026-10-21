# REVIEW — L144 · `unfettered 0 prologue.txt` (la prova della lama)

Coppie EN→IT rilette in `translation.json` (`794b9584fd67c6a0…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce

- **L'ingegnere** è pratico e sprezzante: «Abbiamo armi da mostrarti, per il tuo aiuto nel procurarci motori di salto»,
  «Che maleducazione. Meglio che speri ci sia qualcun altro a guidarti la prossima volta!».
- **Desneeparu** parla per aforismi marziali: «non c'è onore più alto che sopravvivere sul campo di battaglia, perché
  solo allora puoi portare il bottino a chi ne ha bisogno!».
- **La narrazione** è asciutta e osserva il ridicolo: «Non si fermano mai a chiedere se le nuove armi ti interessano
  davvero», «deve adorare lanciare lame alla gente».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `an Unfettered Hai<hood>` | **un Hai Slegato`<hood>`** | 1 |
| `<learned>I am Desneeparu` | **`<learned>`Sono Desneeparu** | 20 |
| `outfitter` | **fornitore** | 8, 14 |
| `this one` (arma) | **una** | 8 |
| `Honestly, I have no real interest in Hai weaponry.` | **Le armi Hai non mi interessano davvero.** | 10 |
| `your unorthodox tactics` | **le tue tattiche poco ortodosse** | 20 |
| `you get a chance to cut the spoils` | **puoi portare il bottino a chi ne ha bisogno** | 20 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Due token, due posizioni diverse**: il suffisso incollato e l'apertura di frase. La parola italiana si costruisce
   **intorno** al segnaposto, che non si sposta.
2. **`(No.)` identico** in `ID_OK`, **`(Yes.)` → «(Sì.)»**: convenzione di L142–L143, tenuta.
3. **`outfitter` → «fornitore»** per maggioranza misurata (45 contro 2 e 1), non per preferenza.
4. **Le quattro reazioni** (afferrarla, schivarla, usare l'arma, fuggire) sono etichette fra parentesi, come
   nell'originale: si traducono, non si riscrivono come voci di menu.
5. **`Desneeparu` resta**: nome proprio, nessuna traslitterazione.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità restano `PENDING`.
- **Nessun equipaggiamento sbloccato** e nessuna lama schivata: la scena non è stata giocata.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 78,2%**: 32 unità da fare, tutte in `Jump Drive Trading`.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (25 controlli, invariante di segmento) |
