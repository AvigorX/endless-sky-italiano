# STATO — L187 · `gegno outfits.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L187_20261019_193503` |
| Righe / unità | **459–728** / **7** — file al **34/60 (56,7%)** |
| Tipi | **7 `DESCRIPTION`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — asserzioni scritte |
| Tab | **0** |
| Contesti | **7** · **7** testi distinti |
| Parole | **453 EN → 469 IT** · rapporto **1.02–1.17**, media **1.1** |
| Apici | **4 inglesi** (idx 3: 1, idx 4: 1, idx 5: 1, idx 6: 1) · **3 italiani** (idx 3: 1, idx 6: 2) |
| sha256 | `6b36e485ac98788b…` |
| Esiti | `check.py` **23** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| cannoni Vi | 1-6 | 459-728 | `Irate` → `Choleric` → `Ballistic`, ognuno con la sua torretta |
| batteria Scin | 7 | 728 | la `Astuit Battery`, «simile agli Energy Blasters umani» |

## Verifica

```bash
cd staging/editorial/L187_20261019_193503
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
