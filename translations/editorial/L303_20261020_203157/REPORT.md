# REPORT — L303 (`data/remnant/remnant ships.txt`, righe 1378–1826) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 38/38.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **26 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 14 (tutte `DESCRIPTION`) | 14 |
| parole | 670 | **701** (1,05) |
| tab | **8** | **8** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 3 | 12 |
| contesti | **6** (3 terzine + 2 coppie + 1 singola) | invariati |

Rapporto per unità **0,99 – 1,18**.

## 2. Invariante di FILE

```
FILE         38/38 (100%) · 38 righe distinte · prima 17 · ultima 1826 · zero dopo
SOMMA LOTTI  12 (L301) + 12 (L302) + 14 (L303) = 38
OVERLAP      nessun altro lotto rivendica le righe 1378-1826
```

`data/remnant/remnant ships.txt` è il **ventisettesimo** file chiuso nel progetto (**86** su 167).

## 3. Gli avvisi di gioco: la forma giusta era **già nel corpus**

Tre unità (1380, 1490, 1826) contengono l'avviso sull'iperguida. **Non** ho inventato una resa: il progetto aveva già tradotto
quella frase in altri file, e le forme ricorrenti sono:

| forma | occorrenze | scelta |
|---|---|---|
| «…una nave con una **baia di caccia**» | **maggioranza** | ✅ |
| «…una nave con una **baia per caccia**» | 2 | ✗ |
| «…una nave con una **baia per droni**» | **unanime** | ✅ |

Il `check.py` confronta le unità con le **costanti** `AVVISO_CACCIA` e `AVVISO_DRONI`: se qualcuno cambia una parola, il lotto
fallisce. È il tipo di coerenza che un traduttore umano perde e un test mantiene.

## 4. La famiglia dell'occultamento: cinque navi, una frase

| riga | nave | lotto |
|---|---|---|
| 549 | `Gull` | L301 |
| 982 | `Merganser` | L302 |
| 1202 | `Penguin` | L302 |
| 1291 | `Peregrine` | L302 |
| **1595** | **`Starling`** | **L303** |

Il `verify.py` **riapre L301 e L302** e confronta le stringhe con il nome sostituito da `X`. Cinque occorrenze, **una sola
frase**: è la verifica più forte del progetto sulla coerenza delle formule.

## 5. Le tre terzine

`Petrel` (caccia multiruolo), `Smew` (scialuppa diventata ibrido mercantile-caccia), `Tern` (drone da raccolta). Ognuna ha **tre
stringhe**: descrizione, secondo paragrafo, **avviso pratico**. Le due tab consecutive sono la struttura con cui il gioco spezza
il pannello.

## 6. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  26 controlli · FAIL: 0 · exit 0
FILE       38/38 (100%) · ventisettesimo file completo
```

**Un rosso al primo giro** (controllo mio): avevo asserito che la variante droni si ottenesse dalla caccia con una catena di
`replace`, ma «baia **per** droni» non deriva da «baia **di** caccia». Sostituito con un confronto **strutturale**:
`rsplit('una nave con una')` e verificazione esplicita delle due code.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **`Ember Waste` resta invariato** (anomalia aperta, serve autorizzazione).
