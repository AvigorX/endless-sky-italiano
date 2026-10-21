# STATO — L258 (`data/human/post-war reactions.txt`, righe 152–215)

**Stato: CHIUSO.** Terzo lotto del file: **20 unità**, `MISSION_TEXT`, **due contesti** — chiude `Navy and Free Worlds
Captains` e apre `Syndicate Orphan`. Il file è aperto a **65/87 (74,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L258_20261020_155239/` |
| file | `data/human/post-war reactions.txt` (87 unità · 1.925 parole · righe 40–264) |
| righe | 152–215 |
| unità | **20** |
| parole | **422 EN → 403 IT** |
| rapporto | **0,81 – 1,26** |
| contesti | **2** — `Navy and Free Worlds Captains` (**11**) → `Syndicate Orphan` (**9**) |
| tab | **19** in inglese, **19** in italiano, **stesse** unità; la **12** è l'unica senza |
| virgolette | **45** in inglese, **45** in italiano, mappa **per unità identica** (e la **5 ne ha 3**) |
| apici | **18 EN** su 10 unità / **12 IT** su 7 unità (1, 3, 10, 12, 15, 16, 18) |
| segnaposto | **0** (asserzione negativa doppia) |
| tipi | **20 `MISSION_TEXT`** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 45 prima · 20 qui · **22 dopo** la 215 · cambio missione alla riga **196** |
| `sha256[:16]` | **`3b8455b11a9d8aca`** |

## Comandi

```bash
python staging/editorial/L258_20261020_155239/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L258_20261020_155239/verify.py    # FAIL: 0 (24 controlli, 65/87)
```

## Le due metà

| metà | unità | contenuto |
|---|---|---|
| prima | 1–11 | le due sorelle raccontano: pattuglia congiunta, Senato e Parlamento in allarme, la corazzata, l'ausiliaria, la milizia di Longjump |
| seconda | 12–20 | **Gus**, l'orfano picchiato davanti all'officina, e il capitano che interviene |

La **12** è l'unica senza tab: è la descrizione d'ambiente che apre la missione (`Quando esci dall'area di atterraggio…`).

## Lessico nuovo, fissato qui

`Dreadnought` → **corazzata** · `Auxiliary` → **ausiliaria** · `Cruiser` → **incrociatore** · `Navy Academy` → **Accademia
della Marina** · `Republic Parliament` → **Parlamento della Repubblica** · `Free Worlds Senate` → **Senato dei Free
Worlds** · `Longjump`, `Earth`→«la Terra», `Gus`, `Rain`, `Fiona` invariati o resi come nomi comuni d'uso.

## Limiti dichiarati

Nessuna approvazione (20 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è a **65/87**:
restano **22 unità**, che saranno due lotti (L259 e L260, quest'ultimo **terminale**).
