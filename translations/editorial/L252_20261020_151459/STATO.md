# STATO — L252 (`data/wanderer/wanderer jobs.txt`, righe 15–261)

**Stato: CHIUSO.** Primo lotto del file, **26 unità** (10 `VALUE` + 10 `DESCRIPTION` + 6 `DIALOG`). Il file resta **aperto a
26/92 (28,3%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L252_20261020_151459/` |
| file | `data/wanderer/wanderer jobs.txt` (92 unità · 1.303 parole · righe 15–891) |
| righe | 15–261 |
| unità | **26** |
| parole | **430 EN → 426 IT** |
| rapporto | **0,93 – 1,12** (media 1,06), gate 0,55–1,90 |
| contesti | **10** — cinque missioni × due contatori, quattro con parentesi tonde |
| tab / virgolette | **0** / **0** (due asserzioni negative scritte) |
| apici | **0 EN** / **4 IT** (unità 10, 11, 13, 14) |
| segnaposto | **58** in **6** famiglie, multiset **e ordine per unità** identici |
| copiati | **10** `VALUE` (5 distinti) |
| tradotti | **16** (10 `DESCRIPTION` + 6 `DIALOG`), in **12 gruppi** identici |
| `check.py` | **32 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **27 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima · 26 qui · 66 dopo · confine riga **264** |
| copertura del file | **26/92 (28,3%)** |
| `sha256[:16]` | **`ef6589a611039978`** |

## Comandi

```bash
python staging/editorial/L252_20261020_151459/check.py     # FAIL totale: 0 (32 controlli)
python staging/editorial/L252_20261020_151459/verify.py    # FAIL: 0 (27 controlli, 26/92)
```

## Cosa contiene

Cinque lavori dei **Wanderer**, ognuno in **due contesti** con la stessa prosa:

| missione | unità | contenuto |
|---|---|---|
| `Wanderer Workers` | 2 `VALUE` + 2 `DESCRIPTION` | `<bunks>` lavoratori da trasportare |
| `Wanderer Farmers` | 2 + 2 | `<bunks>` agricoltori |
| `Wanderer Younglings` | 2 + 2 + 2 `DIALOG` | i piccoli in gita per studiare la terraformazione |
| `Wanderer Scientists (Pollution)` | 2 + 2 + 2 | scienziati con `<cargo>` a indagare un picco di inquinanti |
| `Wanderer Scientists (Phenomenon)` | 2 + 2 + 2 | scienziati a osservare un raro fenomeno naturale |

## Limiti dichiarati

Nessuna approvazione (26 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file **non** è
completo: 26/92 (28,3%); restano 66 unità.
