# STATO — L270 (`data/human/engines.txt`, righe 488–717)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file `data/human/engines.txt` è **completo: 61/61 (100%)**, **diciassettesimo file
interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L270_20261020_172309/` |
| file | `data/human/engines.txt` (**61/61 unità · 1.882 parole · righe 27–717**) |
| righe | 488–717 |
| unità | **17** — tutte `DESCRIPTION` |
| parole | **545 EN → 527 IT** (0,97) |
| rapporto | **0,81 – 1,24** |
| contesti | **14** — Orca e Tyrant steering, Capybara e AR120 reverse, la serie **Atomica** (A120–A860, A125–A865) |
| tab | **4** (unità 1, 3, 5, 17) |
| virgolette / segnaposto | **0 / 0** (asserzioni negative) |
| apici | **7 EN** / **8 IT** |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invarianti | **di segmento** (44 prima · 17 qui · **0 dopo**) **e di FILE** (61 unità · righe distinte · ultima 717 · somma dei 4 lotti = 61) |
| `sha256[:16]` | **`dfffe22b6a49a5c1`** |

## Comandi

```bash
python staging/editorial/L270_20261020_172309/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L270_20261020_172309/verify.py    # FAIL: 0 (23 controlli, 61/61)
```

## Le tre cose delicate

1. **Due stringhe ripetute e riprese alla lettera**: la nota del plasma (unità 1 e 3, da L269) e la nota del **montaggio del
   propulsore inverso** (unità 5 e 17, da L268). Il `check.py` le confronta **rileggendo** i `translation.json` di quei lotti.
2. **Invariante di FILE**: ora è legittimo asserire il futuro — il file **finisce**. Somma dei quattro lotti = **61**, righe
   distinte = **61**, ultima riga = **717**, zero unità dopo.
3. **Un solo numero di modello compare nel testo** (`A860`, unità 10): gli altri nove stanno solo nel **contesto**, che non si
   traduce. Il primo giro li cercava nel testo e dava `1 FAIL`; corretto misurando dove i numeri stanno davvero.

## La serie Atomica

Dieci modelli (A120, A250, A370, A520, A860 propulsori; A125, A255, A375, A525, A865 sterzate) della **Deep Sky**. Il testo li
vende come **capolavoro** e come **lusso**: «pochi capitani non sognano di installarne un set un giorno», e un set può costare
più della nave. La resa conserva il tono pubblicitario e il **compromesso** (energia e raffreddamento).

## Limiti dichiarati

Nessuna approvazione (17 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non **approvato**.
