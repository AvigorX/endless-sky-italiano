# REPORT — L242 (`data/successors/successor jobs.txt`, righe 306–802)

**Esito: lotto CHIUSO, e con lui il file.** `check.py` esce 0 con **30 controlli** (`FAIL totale: 0`); `verify.py` esce 0
con **24 controlli** e l'**invariante di FILE** `86 + 38 = 124`. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 38 unità restano `PENDING`.

`data/successors/successor jobs.txt` è **completo in staging: 124/124 (100%)**, 908 EN → 880 IT, **due lotti**
(L241–L242). È il **decimo file chiuso** della campagna.

## 1. Cosa contiene il lotto

| famiglia | unità | contenuto |
|---|---|---|
| studenti all'università | 1 | `<bunks>` studenti che tornano, pagano `<payment>`, entro il `<date>` |
| operai in cerca di lavoro | 2 | due taglie dello stesso lavoro |
| consegne di provviste | 4 | `<tons>` di provviste da `<origin>` a `<planet>`, pagamento alla consegna |
| carichi preziosi | 1 | `<cargo>` da `<origin>` a `<planet>` |
| aiuti | 1 | `<tons>` di provviste di soccorso, con `<date>` |
| materiali sfusi | 2 | due copie della formula delle provviste |
| spedizioni urgenti | 2 | «spedizione urgente di `<tons>` di provviste… entro il `<date>`» |
| stabilizzatori sismici | 1 | dopo un lieve terremoto su `<planet>` |
| corriere di dati | 1 | dati riservati su `<tons>` di banche dati |
| ricercatori | 3 | Predecessori (2) e ricerche sul posto (1) |
| simposio | 1 | ricercatori diretti a un simposio, prima dell'inizio |
| Vecchie e Nuove Casate | 2 | le stesse provviste di alta qualità, richieste dalle due fazioni |

## 2. Misure

```
unità             38            (19 VALUE invariati + 19 DESCRIPTION tradotte)
parole            480 EN -> 435 IT
rapporto          0,92 - 1,09 (media 1,00)   gate 0,55-1,90
contesti          19            due unità ciascuno
tab / virgolette / apici   0 / 0 / 0
segnaposto        98 su 10 famiglie, parità per simbolo e per ordine
famiglie          14 DESCRIPTION (4 + 2 + 2 + undici da 1)
```

## 3. Le tre cose che il lotto ha di proprio

1. **`<tons>` entra per la prima volta** (11 unità). È una quantità **prodotta dal motore**: la si usa senza articolo e
   senza concordanza («`<tons>` di provviste»), come i **75 precedenti** del corpus. Il `check.py` vieta esplicitamente
   `il/la/i/gli/un/una` davanti al segnaposto.
2. **`<origin>` e `<planet>` nella stessa frase** (11 unità): la partenza non si inverte, e il confronto è sulle
   **posizioni** dentro l'unità, non sui totali (`<planet>` 28 contro `<origin>` 11 passerebbe anche con uno scambio).
3. **Vecchie e Nuove Casate**: tradotte con la maiuscola **nella prosa** («Le Vecchie Casate richiedono…»), inglesi **nei
   `VALUE`** (`Old Houses courier to <planet>`). Il `verify.py` verifica entrambe le cose nello stesso lotto: una resa
   giusta nella prosa e un nome lasciato nei dati.

## 4. Copertura del file (invariante di FILE)

```
L241   86 unità   righe  16 -  280
L242   38 unità   righe 306 -  802
------------------------------------
86 + 38 = 124 = unità del file (min 16, max 802)
```

La copertura si legge dai **due** `translation.json`, si confronta con il database e pretende **124 id distinti su 124
righe distinte**, `max(line) = 802`, `line > 802` vuoto.

## 5. Controlli che hanno morso

Un solo rosso, **nell'asserzione**: il controllo di coerenza cross-lot pretendeva «`Riceverai <payment>` 15 volte», ma la
forma compare **12** volte (11 con «alla consegna», 1 da sola) e «`entro il <date>`» **10**. Corretto il numero, non il
testo; il conteggio è ora scritto nel messaggio del controllo, così chi lo rilegge sa cosa aspettarsi.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 38 unità sono `PENDING`; il file è completo **in staging**, non nel database.
- **Nessun lavoro visto nel gioco**: i segnaposto sono verificati sul **testo**, non a schermo; in particolare il valore
  che il motore dà a `<tons>` include l'unità di misura in inglese («tons»), che la traduzione non può cambiare.
- **Nessuna revisione umana**.
