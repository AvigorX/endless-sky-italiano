# STATO — L80 · `data/successors/successor side missions.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L80_20261018_202613` |
| Righe / unità | **416–453** (finestra 401–460) / **19** |
| Parti | **1** — 19 unità |
| Contesto | **1 intero** — `Unified Defense` |
| Tipi | **15 `MISSION_TEXT` + 4 `UI_LABEL`** |
| Parole | 363 EN → 354 IT (**0,975**) |
| Rapporto per unità | **0,93 – 1,14** |
| `NT` | **4** — unità **2**, **9**, **15**, **17**, identiche |
| Assenze | `VALUE`, `DESCRIPTION`, `LOGBOOK`, `DIALOG`, `CONVERSATION`, `TEXT` = **0** |
| Token / dispari | **0** / **0** — due assenze asserite |
| Tab · virgolette | **11** su **11** unità · **20** |
| Duplicati | **3 gruppi** — 5/11, 6/12, 7/13 |
| sha256 | `0cc5130f4bba902e…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 416 | **145** (L77 + L78 + L79) |
| Unità dopo la riga 453 | **0** |
| File | **164 unità**, `max(line) = 453` |
| Copertura | **164/164 (100%)** — 164 id distinti in staging, 164 righe |
| Lotti del file | **4** — L77 (63), L78 (53), L79 (29), L80 (19) |
| Parole del file | **4.001 EN → 3.854 IT** |

`successor side missions.txt` è il **trentaquattresimo file completo**, **non approvato**: 164 unità `PENDING`.

## Cosa è stato deciso qui

1. **Le quattro `label` restano identiche** (`populated language`, `uninhabited language`, `never again`,
   `deserved it`): bersagli di salto, in `NT`.
2. **`Thy recent actions against our people` → «Le tue recenti azioni contro il nostro popolo»**: stessa
   formula in 4 e 10, resa identica.
3. **`the Houses have decreed in council` → «le Casate hanno decretato in consiglio»**: `Houses` senza
   aggettivo = le Casate in generale, non le Nuove.
4. **`hereforth` → «da ora in poi»**: arcaico reso in italiano corrente.
5. **`Any creature prone to such 'accidents'`**: le virgolette semplici dell'ironia restano semplici.
6. **`bristling black` → «nero irto»**: la pelle dei Successori si irrigidisce, non si «arruffa».

## Verifica

```bash
cd staging/editorial/L80_20261018_202613
python check.py   # FAIL totale: 0   (32 controlli)
python verify.py  # exit 0           (36 controlli, invariante di file)
```

## Prossimo passo

**L81 apre un file nuovo**: `data/successors/predecessors.txt` (59 unità), righe **1–200** (prima unità alla
**17**), **22 unità** in **2 contesti** (`ship:Hasur, Vowsworn`, `ship:Resja, of the Nine Eyes`), **106 parole**,
tipi `15 TEXT + 5 DESCRIPTION + 2 VALUE`, **0 tab**, virgolette **12**, **0 token**, contesti di **nave** e non
di missione.
