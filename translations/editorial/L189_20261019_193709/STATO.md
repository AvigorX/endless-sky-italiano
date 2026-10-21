# STATO — L189 · `gegno outfits.txt` (quinto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L189_20261019_193709` |
| Righe / unità | **1034–1130** / **12** — file al **59/60 (98,3%)** |
| Tipi | **11 `DESCRIPTION`** · **1 `VALUE`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — asserzioni scritte |
| Tab | **0** |
| Contesti | **11** · **12** testi distinti |
| Parole | **443 EN → 472 IT** · rapporto **0.97–1.18**, media **1.07** |
| Apici | **6 inglesi** (idx 2: 1, idx 3: 1, idx 8: 1, idx 9: 2, idx 12: 1) · **11 italiani** (idx 1: 5, idx 2: 1, idx 5: 1, idx 6: 1, idx 9: 2, idx 11: 1) |
| sha256 | `ad29d24c33d43d52…` |
| Esiti | `check.py` **23** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| armi da abbordaggio | 1-5 | 1034-1077 | `Savagery Pike`, `Irate Carronade`, `Plasmasickle`, `Plasma Grenades` |
| licenze Gegno | 6-7 | 1088-1095 | civile e trivellatore |
| licenze Vi | 8-10 | 1102-1116 | `Lord`, `Centurion`, `Evocati` |
| licenze Scin | 11-12 | 1123-1130 | `Hoplologist`, `Architect` |

## Verifica

```bash
cd staging/editorial/L189_20261019_193709
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
