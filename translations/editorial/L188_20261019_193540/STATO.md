# STATO — L188 · `gegno outfits.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L188_20261019_193540` |
| Righe / unità | **739–1012** / **13** — file al **47/60 (78,3%)** |
| Tipi | **11 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — asserzioni scritte |
| Tab | **4** [4, 6, 9, 12] |
| Contesti | **7** · **12** testi distinti |
| Parole | **492 EN → 539 IT** · rapporto **1.0–1.39**, media **1.15** |
| Apici | **3 inglesi** (idx 2: 1, idx 13: 2) · **9 italiani** (idx 2: 1, idx 3: 1, idx 4: 1, idx 5: 1, idx 6: 1, idx 7: 1, idx 8: 1, idx 11: 1, idx 13: 1) |
| sha256 | `887699ce0243bf5f…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| artiglieria Scin | 1-6 | 739-886 | `Acuit Artillery`, `Acumen Bolt Cannon`, `Guile Pulse Laser` |
| trivelle | 7-9 | 886-933 | `Excavator` (macina) e `Burrower` (scava con cura) |
| torcia ionica | 10-12 | 949-987 | l'`Ion Torch`, che può anche servire da propulsore inverso |
| mazza da duello | 13 | 1012 | la `Savagery Bludgeon` delle navi `Dunite` |

## Verifica

```bash
cd staging/editorial/L188_20261019_193540
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
