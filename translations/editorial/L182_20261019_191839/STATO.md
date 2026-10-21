# STATO — L182 · `human outfits.txt` (scanner, espansioni, celle)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L182_20261019_191839` |
| Righe / unità | **236–387** / **14** — file al **35/63 (55,6%)** |
| Tipi | **13 `DESCRIPTION`** · **1 `VALUE`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — tre asserzioni vuote scritte |
| Tab | **1** (idx 10) |
| Contesti | **12** (`Jump Drive (Broken)` 2, `Outfits Expansion` 2, dieci con 1) · **14 testi distinti** |
| Parole | **497 EN → 498 IT** (1,002) · rapporto **0,99–1,33**, media **1,10** |
| Apici | **6 inglesi** (tutti legati alla causa) · **9 italiani** · i due conteggi **non coincidono** |
| sha256 | `227c7d7ef6b392c9…` |
| Esiti | `check.py` **29** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Il `VALUE` con le parentesi

Il contratto lo annunciava e il lotto lo conferma: **`Jump Drives (Broken)`** si copia **alla lettera**, parentesi
comprese. È l'unico `VALUE` del lotto e il primo della serie con una parentesi nel nome.

## Gli apici: 6 inglesi, 9 italiani

Il contratto chiedeva di legare **ogni** apice alla sua causa. Fatto:

| unità | inglese | causa | italiano |
|---|---|---|---|
| 7 | `ship's` | possessivo | «della tua nave» — nessun apice |
| 8 | `You're`, `can't` | elisione | «Sei sicuro», «non riesci» — nessun apice |
| 12 | `you're` | elisione | «stai cercando» — nessun apice |
| 14 | `ship's`, `Republic's` | possessivo | «della Repubblica» — nessun apice |
| 6, 9, 10, 11, 12, 14 | — | — | `dell'`, `po'` (×2), `l'`, `un'`, `nell'` — 9 in tutto |

**I 6 possessivi inglesi non producono un solo apice italiano** (l'italiano usa il di + articolo), e i 9 apici italiani
nascono da cause che l'inglese **non ha**. Il `check.py` verifica entrambi i conteggi e che siano **diversi**.

## Verifica

```bash
cd staging/editorial/L182_20261019_191839
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
