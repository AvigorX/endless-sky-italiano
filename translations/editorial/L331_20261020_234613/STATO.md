# STATO — L331 (`data/human/power.txt`, righe 23–272) — **TERMINALE, FILE INTERO**

`check.py` exit 0 (**14 controlli**), `verify.py` exit 0 (**9 controlli**), `state.py` `ESITO: OK`. Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L331_20261020_234613/` |
| righe | 23–272 (**tutto il file**) |
| unità | **22 `DESCRIPTION`**, 22 contesti (uno per unità), tutte `PENDING` |
| parole | **842 EN → 829 IT** (0,985) |
| tab / virgolette / segnaposto | **0 / 0 / 0** |
| invariante | **di FILE**: 22/22, prima 23, ultima 272, zero prima e dopo |
| `sha256[:16]` | **`48c8ef78b4d66af7`** |

**Centoduesimo file completo** (**102** su 167). Residuo: **1.376 unità / 18.519 parole su 65 file**.

## Due rossi al primo giro, entrambi del test

1. `Supercapacitor` era nella lista dei **nomi invariati**, ma in prosa è un **nome comune** («Supercapacitors provide…»): reso
   «supercondensatori», e il controllo ora lo verifica come traduzione.
2. la scala delle batterie cercava «modello più elementare» **nell'unità sbagliata** (34 invece di 45): la frase appartiene al
   modello superiore che lo confronta.

## Limiti

Nessuna approvazione (22 `PENDING` invariate), nessun testo visto nel gioco, nessuna revisione umana.
