# REPORT — L247 (`data/human/syndicate jobs.txt`, righe 19–153)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **32 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **27 controlli**
(invariante di segmento: 0 prima, 16 qui, 78 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 16 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Transport executive to <planet>` | 1 `DESCRIPTION` + 1 `DIALOG` | dirigente del Sindacato a una riunione urgente |
| `Corporate retreat to <planet stopovers>` | 1 `DESCRIPTION` + 2 `DIALOG` | ritiro aziendale di una squadra di ingegneri |
| `Large Corporate retreat` | 1 `VALUE` + 1 `DESCRIPTION` + 2 `DIALOG` | la **stessa** prosa, in una seconda missione: **una sola resa** |
| `Corporate espionage` | 1 `DESCRIPTION` + 2 `DIALOG` | intercettare un `<npc>` e scansionarne il carico |
| `Document delivery to <planet>` | 1 `DESCRIPTION` + 1 `DIALOG` | documenti «ordinari» che finiscono in un inceneritore |
| `Waste recycling on <planet>` | 1 `DESCRIPTION` + 1 `DIALOG` | la «Iniziativa Verde» di Syndicated Systems |

## 2. Misure

```
unità             16            (1 VALUE + 9 DIALOG + 6 DESCRIPTION)
parole            488 EN -> 510 IT       rapporto 0,97 - 1,23 (media 1,09)
contesti          6
tab               0             asserzione negativa scritta
virgolette        2             unità 12, una citazione
apici             6 EN / 5 IT   possessivi contro elisioni
segnaposto        39 in 11 famiglie, multiset E ordine per unità identici
coppie identiche  3             (3/7, 4/8, 5/9), una resa ciascuna
```

## 3. Le tre cose che il lotto ha di proprio

1. **Il primo lotto con `DIALOG`.** Nove battute oltre alle schede: la prosa non è solo descrizione del lavoro, ma quello
   che il giocatore legge alla consegna — e quindi va resa con lo stesso registro dei testi di missione già chiusi.
2. **39 segnaposto in 11 famiglie, confrontati due volte**: multiset **e** ordine dentro ogni unità. `<planet stopovers>`
   contiene uno **spazio** ed è un simbolo intero: il controllo asserisce che compaia **una volta** come tale e che
   `<stopovers>` ne compaia due, così uno `split` sbagliato si vede.
3. **Tre coppie di inglese identico** (la missione «Large» riusa la prosa della normale): una sola resa, verificata come
   famiglia. Le coppie sono **3/7**, **4/8**, **5/9**.

## 4. Difetti trovati

**Nel contratto (`HANDOFF_L247`)**: dichiaravo **33** segnaposto; misurati **39**
(`4+4+12+2+2+5+1+2+3+2+2`). `check_handoff.py` non controlla i token, quindi la cifra sbagliata era passata. Corretta nel
contratto e nella ripresa, con la nota del perché.

**Nel `check.py`, tre asserzioni sbagliate** (tutte mie, nessuna nel testo):

1. «Il pagamento è `<payment>`.» contata **4** volte: sono **5** unità (1, 3, 7, 13, 15) — la coppia 3/7 ne aggiunge una.
   Sostituito il conteggio con l'**elenco degli indici**;
2. `<tons>` «senza concordanza» usava `\w+(i|e)\b`, che colpisce **«di»**: riscritta come «nessun articolo davanti e sempre
   seguito da «di»»;
3. `'Syndicate' not in prosa` falliva per **`Syndicated Systems`**, che è un nome proprio e **deve** restare: riscritto con
   `\bSyndicate\b`.

## 5. Copertura del file

```
L247   16 unità   righe  19 - 153
residuo 78 unità  righe 157 - 814
---------------------------------
16 + 78 = 94 = unità del file
```

Copertura **16/94 (17,0%)**. Confine misurato: **riga 157**, `mission:Rush fuel Delivery`.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 16 unità sono `PENDING`.
- **Nessun testo visto nel gioco**: i segnaposto sono verificati **sul testo**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 16/94 (17,0%).
