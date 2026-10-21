# STATO — L76 · `data/successors/successor 2 ghosts aqrabe.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L76_20261018_201110` |
| Righe | **404–478** (finestra 401–478; la 400 è l'ultima unità di L75) |
| Unità | **30** |
| Parti | **2** — 15 · 15 |
| Contesti | **1** — `Ghosts Aqrabe 7` |
| Tipi | **24 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + 2 `DIALOG` + 1 `LOGBOOK` + 1 `UI_LABEL`** |
| Parole | 822 EN → 788 IT (**0,959**) |
| Rapporto per unità | **0,75 – 1,26** |
| `NT` | **1** — unità **28**, `label "not confronted"` (identica) |
| `LOGBOOK` | **1** — unità **14**, forma diretta, tradotto |
| `DIALOG` | **2** — unità **12** (backtick nel `raw`) e **13** (virgolette), testi tradotti |
| `UI_LABEL` | **1** — unità **28** |
| `CONVERSATION` / `TEXT` | **0 / 0** — assenze dichiarate |
| Token `<…>` | **6** in 5 famiglie: `<ship>` 2, `<destination>`/`<capacity>`/`<planet>`/`<payment>` 1 |
| Tab · virgolette | **21** su **21** unità · **43** — **1 dispari (25)** |
| Duplicati inglesi | **0 gruppi**; **coppia quasi identica 23/25** (differisce solo per la virgoletta finale) |
| sha256 `translation.json` | `44a954ecdc2aac76…` |
| `check.py` | **35 controlli**, `FAIL totale: 0` |
| `verify.py` | **49 controlli**, exit **0** |

## Invariante di FILE (non di segmento)

| Voce | Valore |
|---|---|
| Unità prima della riga 404 | **150** (L73 + L74 + L75) |
| Unità dopo la riga 478 | **0** |
| File | **180 unità**, `max(line) = 478` |
| Copertura | **180/180 (100%)** — tutte le righe del file hanno un'unità in staging |
| Lotti del file | **4** — L73 (51), L74 (38), L75 (61), L76 (30) |
| Parole del file | **5.147 EN → 4.942 IT** |

`successor 2 ghosts aqrabe.txt` è il **trentatreesimo file completo** dello staging, e **non è approvato**:
180 unità restano `PENDING`.

## Cosa è stato deciso qui

1. **La virgoletta non chiude** in unità 25 (`"E questa nave? Posso tenermela?`): riprodotta, e il controllo
   verifica che la coppia **23/25** differisca **solo** per la virgoletta finale.
2. **`not confronted` resta identica**: è una `label` di salto, non prosa.
3. **`Kaatrij's aggressor` → «l'aggressore di Kaatrij»**, senza ipotizzare chi sia.
4. **`bounty` → «bottino»** (il carico di metallo), **`heirlooms` → «cimeli»**.
5. **`the ghosts of others` → «i fantasmi degli altri»**: è il titolo della linea (`Ghosts`) e va tenuto.
6. **`thine account flusher` → «il tuo conto più pieno»**: forma arcaica resa in italiano corrente.
7. **`Quarg` invariato**; **`drone ship` → «nave drone»**, **`guardian` → «guardiano»**.

## Verifica

```bash
cd staging/editorial/L76_20261018_201110
python check.py                 # FAIL totale: 0   (35 controlli)
python verify.py                # exit 0           (49 controlli, invariante di file)
```

## Prossimo passo

**L77 apre un file nuovo**: `data/successors/successor side missions.txt` (164 unità, 4.002 parole), righe
**1–220** (prima unità alla **17**), **63 unità** in **due contesti interi** (`Predecessor Research 1` 37,
`Biology Research 1` 26), **1.909 parole**, tab **53** su 53 unità, virgolette **68**, **2 unità con
virgoletta dispari** (56, 57), **13 token** in 6 famiglie.
