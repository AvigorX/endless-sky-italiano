# REPORT — L241 (`data/successors/successor jobs.txt`, righe 16–280)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **33 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **28 controlli**
(invariante di segmento: 0 prima, 86 qui, 38 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 86 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| parte | unità | contenuto |
|---|---|---|
| frasi intere | 10 | turisti (andata, ritorno, itinerario, itinerario «alquanto insolito»), studenti, operai, consegna di `<commodity>`, ricercatori al simposio |
| blocco `successor data` | 13 | frammenti: «Tu … le banche dati criptate … e poi … `<payment>` in pagamento.» |
| blocco `high houses delivery` | 14 | frammenti: «Tu … il carico/la partita di `<commodity>` a diversi ufficiali Successors in ghingheri. Ti danno/versano/consegnano … il pagamento di `<payment>`.» |
| blocco `predecessor researchers out` | 22 | frammenti: «Consegni i … a `<planet stopovers>`, dove … iniziano/prendono a … . Dopo qualche ora, sono pronti a tornare a casa.» |
| blocco `successor researchers out` | 18 | lo stesso blocco con meno varianti (`experimenters`, 5 oggetti) |
| lavori | 10 | 5 `VALUE` (invariati) + 5 `DESCRIPTION` (turisti, turisti audaci, spedizione, studenti) |

## 2. Misure

```
unità             86             (76 TEXT + 5 VALUE + 5 DESCRIPTION)
parole            428 EN -> 445 IT
rapporto          0,67 - 1,70 (media 1,05)   gate 0,55-1,90
contesti          18
tab / virgolette  0 / 0         asserzioni negative scritte
apici             0
segnaposto        45 su 8 famiglie, parità per simbolo e per ordine
duplicati         21 gruppi, una sola resa ciascuno
composizione      1104 frasi verificate (48 + 48 + 648 + 360)
```

## 3. Le tre cose che il lotto ha di proprio

1. **Non ci sono frasi: ci sono gruppi.** 66 unità sono frammenti che il gioco concatena (`Phrase::Get()` fa
   `result += …` senza separatore). Le frasi nascono solo scegliendo un'opzione per gruppo: **1104 combinazioni** in
   inglese e 1104 in italiano. Il controllo non poteva essere «ogni unità è sensata» ma «**ogni combinazione è
   composta bene**»: nessun doppio spazio, nessuno spazio prima della punteggiatura, iniziale maiuscola, punto finale,
   nessun segnaposto irrisolto. Il `check.py` e il `verify.py` lo fanno **in modo indipendente** (il secondo ricostruisce
   i gruppi leggendo i blocchi `phrase` del file del gioco).
2. **Quattro frammenti hanno uno spazio in meno dell'inglese** (43, 44, 65, 66: `begin `/`start ` → «iniziano a» /
   «prendono a»). Non è una svista: l'oggetto che segue **comincia con uno spazio** (` catalogare …`), e l'inglese
   produce «begin  cataloging» con **due** spazi. In italiano il verbo non porta lo spazio finale e la frase composta ne
   ha **uno solo**. La differenza è dichiarata, elencata per indice e verificata **componendo**.
3. **L'opzione vuota non è nell'inventario.** Il quarto gruppo dei due blocchi «researchers» ha **quattro** opzioni nel
   sorgente (`promptly `/`immediately `/`quickly `/``): la quarta è la stringa vuota e il database ne conserva tre. Il
   `verify.py` legge il **file del gioco** e trova l'opzione vuota; il `check.py` compone anche la variante senza avverbio
   («… dove iniziano a catalogare…») per dimostrare che la frase regge lo stesso. La lacuna è dichiarata, non riparabile
   da un lotto.

## 4. Copertura del file

```
L241   86 unità   righe  16 -  280
residuo 38 unità  righe 306 -  802
------------------------------------
86 + 38 = 124 = unità del file (min 16, max 802)
```

Copertura **86/124 (69,4%)**. Confine misurato: **riga 306**, `VALUE` di `mission:Successors: Students In`. Restano **38
unità in 19 contesti** (studenti che tornano, operai, consegne di ogni tipo, stabilizzatori sismici, corriere di dati,
ricercatori, simposio, Vecchie e Nuove Case): **L242 le prende tutte e chiude il file**.

## 5. Controlli che hanno morso

**Tre rossi al primo giro, tutti nell'asserzione**:

1. «le 71 TEXT+DESCRIPTION sono tutte tradotte»: il conto giusto è **81** (76 + 5), non 71 — avevo sottratto due volte i
   `VALUE`;
2. «confine: DESCRIPTION di Students In»: l'unità alla riga 306 è un **`VALUE`**, non una `DESCRIPTION`;
3. «i quattro blocchi phrase del lotto»: il `verify.py` leggeva **tutti** i blocchi `phrase` del file (13) e pretendeva
   che fossero 4. Corretto in «i quattro del lotto hanno 6 · 7 · 7 · 7 gruppi, gli altri 9 non sono nel lotto».

**Due difetti veri, trovati leggendo frasi composte dopo che entrambi gli script erano verdi**: «Tu consegni **i
scienziati**» (articolo sbagliato) e «Tu depositi **il tuo partita** di ferro» (genere sbagliato). Il controllo dei soli
spazi e della punteggiatura non li vedeva. Corretto il **testo** — l'articolo viaggia con il nome, e i due nomi
alternativi sono dello stesso genere («il carico» / «il lotto») — e aggiunto un controllo d'**accordo articolo+nome**,
provato **al negativo**: rimessi i due errori, il controllo diventa rosso e li nomina.

Nessuno dei tre rossi iniziali riguardava la traduzione; i due difetti veri sì. È la conferma della regola: un controllo
che non può fallire non è un controllo, e «composto senza doppi spazi» non significa «composto in italiano».

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 86 unità sono `PENDING`.
- **Nessuna frase vista nel gioco**: la composizione è verificata **sul testo**, con un campione di valori per i
  segnaposto, non osservata a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 86/124 (69,4%); restano 38 unità.
