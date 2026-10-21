# REPORT — L280 (`data/human/kestrel.txt`, righe 252–402) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **19 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 2 (1 `MISSION_TEXT`, 1 `DESCRIPTION`) | 2 |
| parole | 105 | **103** (0,98) |
| tab | 0 | 0 |
| virgolette | 2 | 2, dritte |
| segnaposto | 1 (`<last>`) | 1 |
| apici | 2 | 1 |

Rapporto per unità **1,02 – 1,05**.

## 2. Il lotto

| unità | riga | contenuto |
|---|---|---|
| 1 | 252 | **messaggio di Atinoda**: la Kestrel è in vendita su Wayfarer, i suggerimenti sono stati recepiti |
| 2 | 402 | **scheda della nave**: la trance nella capanna del sudore, la visione, sette anni di lavoro |

Sono le **due code** della missione: la **ricompensa** (il messaggio che arriva a missione compiuta) e la **scheda** che il
giocatore legge nel cantiere quando la nave è acquistabile.

## 3. La coerenza che il test difende

La `DESCRIPTION` racconta la stessa visione del dialogo di L278. Il `check.py` **riapre** `L278/translation.json` e verifica
che «capanna del sudore» e «trance» siano **le stesse forme**. Se la scheda avesse detto «tenda del sudore» o «estasi», il
giocatore avrebbe letto due versioni della stessa scena, e nessun conteggio se ne sarebbe accorto.

## 4. L'invariante di FILE

```
database:  51 unità, righe 15–402, ultima unità alla 402
somma dei tre lotti (L278 + L279 + L280): 51
righe distinte: 51 · prima 15 · ultima 402 · dopo la 402: 0
copertura: 51/51 (100%)
```

`verify.py` verifica tutte e cinque le righe in modo indipendente da `check.py`.

## 5. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  19 controlli · FAIL: 0 · exit 0
segmento   49 prima · 2 qui · 0 dopo (fine file) · 2 contesti
```

Due rossi al primo giro, entrambi su **riferimenti sbagliati miei**:

1. contavo **due** apici italiani; ce n'è **uno** (`un'astronave`) — l'unità 1 non ne ha nessuno;
2. la verifica di coerenza puntava a `L279` invece che a **`L278`**: la scena della visione è nel **primo** lotto del file, non
   nel secondo. Corretto il percorso, non l'asserzione.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 2 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging: 51 unità su 51, tutte `PENDING`.
