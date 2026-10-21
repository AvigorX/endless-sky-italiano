# REPORT — L243 (`data/hai/hai ships.txt`, righe 15–332)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **30 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **23 controlli**
(invariante di segmento: 0 prima, 29 qui, 128 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 29 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Anomalocaris` | 1 `VALUE` + 6 `TEXT` + 2 `DESCRIPTION` | il nome della nave al plurale, sei nomi di equipaggiamento, e **due schede**: quella normale e quella del relitto rimasto a lungo sott'acqua |
| `Aphid` | 9 `TEXT` + 1 `DESCRIPTION` | nove nomi di equipaggiamento, la scheda del mercantile più leggero degli Hai |
| `Centipede` | 6 `TEXT` + 1 `DESCRIPTION` | il trasporto di lusso nato dalla cooperazione umano-Hai |
| `Cicada` | 3 `TEXT` + 1 `DESCRIPTION` | la scheda più lunga, con il motto del cantiere Yeer e Ki fra virgolette |

## 2. Misure

```
unità             29            (1 VALUE + 23 TEXT + 5 DESCRIPTION)
parole            451 EN -> 456 IT  (solo le 5 descrizioni si traducono: 451 parole in tutto il lotto)
rapporto          1,00 - 1,09 (media 1,01)   gate 0,55-1,90
contesti          4
tab               0             asserzione negativa scritta
virgolette        48            = 2 × 23 nomi + 2 del motto, per unità
apici             4 EN (possessivi) / 19 IT (elisioni)
segnaposto        0             asserzione negativa scritta
copiati           24 unità identiche all'inglese (i nomi sono dati)
```

## 3. Le tre cose che il lotto ha di proprio

1. **File misto: si copia e si traduce nello stesso lotto.** 24 unità sono **dati** (un nome di nave al plurale e 23 nomi
   di equipaggiamento con le virgolette dentro) e restano identiche all'inglese; 5 sono prosa e si traducono. Il
   `check.py` confronta **per indice** quali sono identiche, non solo quante: una traduzione infilata in un nome (o un
   nome «tradotto» per distrazione) diventa rossa.
2. **Le 48 virgolette stanno nei nomi e in un motto.** Il confronto è **per unità**: 23 nomi con 2 virgolette ciascuno
   più la scheda della Cicada, che ne ha 2 per il motto `"Al servizio per tutta la vita."`. Un controllo sul solo totale
   (48 = 48) passerebbe anche con una virgoletta spostata da un nome all'altro.
3. **I 4 possessivi inglesi diventano elisioni italiane.** `Hai's` (4, 7), `project's` (20) e `shipyard's` (29) non
   esistono in italiano: la resa usa «degli Hai», «il suo», «del cantiere». Gli apici salgono da 4 a 19 (e compaiono in
   un'unità che in inglese non ne aveva, la 10, per `L'Aphid` e `dell'economia`): la differenza è **elencata per unità**
   e spiegata nel `review.md`.

## 4. Copertura del file

```
L243   29 unità   righe  15 -  332
residuo 128 unità righe 362 - 1860
------------------------------------
29 + 128 = 157 = unità del file (min 15, max 1860)
```

Copertura **29/157 (18,5%)**. Confine misurato: **riga 362**, `ship:Flea`. Restano **128 unità in 13 contesti**: il file
si chiuderà in altri quattro/cinque lotti.

## 5. Controlli che hanno morso

Due rossi, entrambi **nell'asserzione** (e uno era un errore di sintassi):

1. il primo `check.py` non compilava: avevo scritto un'assegnazione walrus dentro un confronto (`... and by_len := 23`),
   che in quella posizione è un `SyntaxError`. Riscritta come due condizioni normali;
2. il controllo «parole comuni tradotte» cercava **«nave da guerra»** al singolare, ma il testo dice «**navi** da
   guerra». Corretto il controllo (e aggiunta «spina dorsale»), non il testo.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 29 unità sono `PENDING`.
- **Nessuna scheda di nave vista nel gioco**.
- **Nessuna revisione umana**.
- **Il file non è completo**: 29/157 (18,5%); restano 128 unità.
