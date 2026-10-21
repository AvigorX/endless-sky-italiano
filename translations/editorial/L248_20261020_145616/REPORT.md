# REPORT — L248 (`data/human/syndicate jobs.txt`, righe 157–275)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **33 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **28 controlli**
(invariante di segmento: 16 prima, 20 qui, 58 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 20 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Rush fuel Delivery` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | carburante d'emergenza a un reattore civile |
| `Rush equipment Delivery` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | attrezzature ai tecnici del Sindacato |
| `Syndicate target practice [0]` | 1 `VALUE` + 1 `DESCRIPTION` + 4 `DIALOG` | la missione completa: scheda e quattro esiti |
| `Syndicate target practice [1]` | 1 `VALUE` + 1 `DESCRIPTION` + 4 `DIALOG` | **la stessa prosa**, secondo contesto |
| `Syndicate target practice [2]` | 1 `VALUE` + 1 `DESCRIPTION` | **la stessa prosa**, terzo contesto (la finestra si chiude qui) |

## 2. Misure

```
unità             20            (5 VALUE + 10 DIALOG + 5 DESCRIPTION)
parole            430 EN -> 422 IT       rapporto 0,93 - 1,32 (media 1,03)
contesti          5             tre con parentesi quadre nel nome
tab               0             asserzione negativa scritta
virgolette        0             asserzione negativa scritta
apici             2 EN / 1 IT
segnaposto        32 in 8 famiglie, multiset E ordine per unità identici
gruppi identici   7             (uno con tre copie), una resa ciascuno
```

## 3. Le tre cose che il lotto ha di proprio

1. **Una missione, tre contesti, sette gruppi identici.** «Syndicate target practice» compare tre volte con la stessa
   scheda e le stesse quattro battute. Il controllo verifica **ogni gruppo** (uno solo con **tre** copie) e che la resa sia
   **una**, non tre simili: è il caso in cui un lotto può produrre tre varianti senza che nessun totale cambi.
2. **`<commodity>` non prende aggettivi concordati.** Il nome inserito dal motore non ha genere noto: «specialized
   `<commodity>`» diventa «`<commodity>` **per uso specialistico**», e il controllo asserisce le **tre forme misurate** che
   seguono il segnaposto (`alla`, `per`, `alla`) — mai un aggettivo. Stessa cautela di L242 con `<tons>`.
3. **Zero tab e zero virgolette**, scritte come asserzioni negative: in un lotto di soli lavori il rischio non è
   dimenticarle, è **aggiungerle** (un apostrofo tipografico in una battuta).

## 4. Difetti trovati

Tre rossi, **tutti nelle asserzioni** (nessuno nel testo):

1. la prima versione del `check.py` non compilava: avevo usato la variabile `t` sia come iteratore sia come stringa nel
   conteggio dei token (`UnboundLocalError` nel costruttore, non nel gioco);
2. il controllo «nessun aggettivo dopo `<commodity>`» usava `\w+(o|a|i|e)\b`, che colpisce **«alla»**: riscritto sulle tre
   forme misurate;
3. il `verify.py` aveva un `max(1 for …) == 3` che confronta **1** con **3**: riscritto con il `Counter` delle
   molteplicità (`mult.most_common()`).

## 5. Copertura del file

```
L247   16 unità   righe  19 - 153
L248   20 unità   righe 157 - 275
---------------------------------
36 unità su 94 (38,3%)

residuo 58 unità, righe 291 - 814
```

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 20 unità sono `PENDING`.
- **Nessun testo visto nel gioco**: i segnaposto sono verificati **sul testo**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 36/94 (38,3%).
