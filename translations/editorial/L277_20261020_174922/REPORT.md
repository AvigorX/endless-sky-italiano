# REPORT — L277 (`data/korath/korath ships.txt`, righe 2010–2363) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **19 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 7 (tutte `DESCRIPTION`) | 7 |
| parole | 213 | **230** (1,08) |
| tab / virgolette / segnaposto | 0 / 0 / 0 | 0 / 0 / 0 |
| apici | 0 | 4 |

Rapporto per unità **0,98 – 1,18**.

## 2. Il lotto

Sette navi `Model` dei **Kor Mereti**, le più piccole della flotta robotica. La serie è numerata a **potenze di due** e
racconta **un'unica storia**: un drone minerario che cresce, si riconfigura, si divide e diventa un **anello da guerra**.

| unità | modello | stadio |
|---|---|---|
| 1 | `Model 8` | estrazione mineraria; i laser diventano armi «quando serve» |
| 2 | `Model 16` | costruzione **modulare**: cresce con i materiali disponibili |
| 3 | `Model 32` | «**imitando la vita**»: fabbriche automatiche che lo riconfigurano |
| 4 | `Model 64` | come una **fregata** umana, ma con potenza di fuoco superiore |
| 5 | `Model 128` | **si divide a metà**; scudi e armi si rafforzano |
| 6 | `Model 256` | il **detto dei Quarg** sull'arma che sopravvive ai creatori |
| 7 | `Model 512` | **anello perfetto**, torrette che sparano in ogni direzione |

## 3. Perché il «continuum» conta

Sei delle sette schede, prese da sole, sono descrizioni di navi. **Insieme** sono la biografia di un'arma: si parte da un
mineratore e si arriva a qualcosa che, secondo i Quarg, «ha quasi superato i suoi creatori». La resa conserva i **nessi**:

- unità 2 → 3: «costruiti in modo modulare» … «**costruirono i loro droni imitando la vita**» (stesso verbo, stesso soggetto);
- unità 5: «**si dividono a metà**» — il drone non viene sostituito, **si sdoppia**;
- unità 6: la frase dei Quarg è **generale** («ogni specie che insista nello studiare la guerra»), e solo dopo si applica ai
  Korath — l'ordine delle due frasi è stato mantenuto.

## 4. Il `Model 512`

«Questo è lo stadio **finale** dell'evoluzione di un drone da guerra Kor Mereti: un **anello perfetto**, con scudi
incredibilmente potenti e torrette che sparano in **ogni direzione**.» La forma (anello) e la copertura (ogni direzione) sono
le due informazioni che rendono l'oggetto riconoscibile a schermo: nessuna delle due è stata omessa.

## 5. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  19 controlli · FAIL: 0 · exit 0
segmento   43 prima · 7 qui · 0 dopo (fine file) · 7 contesti
FILE       50/50 (100%) · somma dei cinque lotti 50 · righe distinte 50 · ultima 2363
```

Un rosso al primo giro, di nuovo su un **divieto lessicale scritto male**: vietavo la parola `drone`, che **in italiano è
corretta** (e l'unità 1 usa «droni»). Il divieto ora riguarda solo `frigate`, `shields`, `turrets`, `firepower`, e in più
**pretende** «droni», «drone» e «fregata».

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 7 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging: 50 unità su 50, tutte `PENDING`.
