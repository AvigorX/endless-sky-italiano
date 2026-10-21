# STATO — L185 · `gegno outfits.txt` (primo lotto: **apre il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L185_20261019_193201` |
| Righe / unità | **17–157** / **13** — file al **21/60 (35,0%)** |
| Tipi | **9 `DESCRIPTION`** · **4 `VALUE`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — asserzioni scritte |
| Tab | **0** |
| Contesti | **9** · **13** testi distinti |
| Parole | **469 EN → 483 IT** · rapporto **1.0–1.19**, media **1.07** |
| Apici | **5 inglesi** (idx 4: 1, idx 9: 1, idx 11: 1, idx 12: 1, idx 13: 1) · **6 italiani** (idx 2: 2, idx 8: 1, idx 12: 1, idx 13: 2) |
| sha256 | `c2fcd9f6a88e97cc…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| batterie Vi | 1-8 | 17-76 | `R01` → `R04`: dalla batteria comune alla `Crusade`, "immensa" |
| celle e reattori | 9-12 | 91-139 | `Scrap Cell`, `Brawl Cell` (girata di lato), `Warzone Core`, `Campaign Core` |
| cellula Scin | 13 | 157 | la `I70 Ameliorate Cell` dei caccia `Halite` |

## Verifica

```bash
cd staging/editorial/L185_20261019_193201
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
