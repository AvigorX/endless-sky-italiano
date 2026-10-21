# REPORT — L264 (`data/remnant/remnant jobs.txt`, righe 703–741) — LOTTO TERMINALE

**Esito: lotto CHIUSO, file COMPLETO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **20 controlli**
(invariante di **file**: 87/87). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

**`data/remnant/remnant jobs.txt` è il quindicesimo file chiuso: 87/87 unità.**

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (5 `DIALOG`, 2 `MISSION_TEXT`, 1 `VALUE`, 1 `DESCRIPTION`) | 9 |
| parole | 203 | **196** (0,97) |
| tab / virgolette | 0 / 0 | 0 / 0 |
| apici | 7 | 8 |
| segnaposto | 8 (`<payment>` 3, `<planet>` 3, `<npc>` 2) | 8, stesso ordine |

Rapporto **0,87 – 1,13**.

## 2. `disable` ≠ `destroy`

Il compito è **disabilitare** la Dathnak A'awoj, non distruggerla: la nave ha a bordo una popolazione civile, e la scheda
chiede di evitare «un massacro». La parola **«distruggere» compare una volta sola**, nel ramo del fallimento (unità 8:
«Non sei riuscito a disabilitare la Dathnak A'awoj senza distruggerla... I Remnant non ne saranno contenti...»).

Entrambi gli script verificano che gli indici con «distrugger» siano **esattamente** `[8]`: se una resa avesse usato
«distruggere» nella scheda, il test sarebbe rosso. È l'invariante che protegge il **significato** della missione, non la
forma.

## 3. Traduzione manuale

Le 9 rese sono state scritte **a mano** dopo aver letto il sorgente; nessuno script ha generato o riscritto testo. L'unico
`VALUE` (`Disable Damaged Dathnak A'awoj`) è **copiato** con il suo apice, e il `check.py` lo confronta con la costante.

## 4. Il ritorno del soccorso

L'unità 1 chiude la sottotrama iniziata in L262: il capitano ringrazia **prima** della notifica ufficiale («ancora prima che
il tuo comunicatore ti notifichi un'assegnazione di risorse di `<payment>`»), e il dettaglio è conservato perché è il senso
della frase.

## 5. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
FILE       87/87 unità · 4 lotti (25 + 29 + 24 + 9) · 87 righe distinte · ultima riga 741 · 0 dopo
```

Nessun rosso: entrambi gli script verdi al **primo** giro.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **«Completo» significa completo in staging**: 87 unità tradotte, 0 caricate.
