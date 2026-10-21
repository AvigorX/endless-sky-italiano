# STATO — L186 · `gegno outfits.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L186_20261019_193316` |
| Righe / unità | **179–427** / **14** — file al **27/60 (45,0%)** |
| Tipi | **12 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — asserzioni scritte |
| Tab | **0** |
| Contesti | **12** · **14** testi distinti |
| Parole | **462 EN → 512 IT** · rapporto **1.0–1.25**, media **1.12** |
| Apici | **5 inglesi** (idx 1: 1, idx 5: 1, idx 8: 1, idx 11: 1, idx 14: 1) · **6 italiani** (idx 1: 1, idx 3: 2, idx 8: 1, idx 11: 1, idx 14: 1) |
| sha256 | `6a678083062012e4…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| propulsori e timoni Vi | 1-6 | 179-285 | `RG15`, `RG18`, `RG3` — ionici, pesanti, i più antichi |
| motori Scin | 7-12 | 289-398 | `SC-1`, `SC-12`, `SC-14` — plasma, compatti, più potenti |
| la retromarcia | 13-14 | 402-427 | l'`SC-15` integra spinta inversa e diretta |

## Verifica

```bash
cd staging/editorial/L186_20261019_193316
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
