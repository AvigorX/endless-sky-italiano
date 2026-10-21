# STATO — L277 (`data/korath/korath ships.txt`, righe 2010–2363)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 50/50 (100%)**, **diciannovesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L277_20261020_174922/` |
| file | `data/korath/korath ships.txt` (**50/50 unità · 2.049 parole · righe 95–2363**) |
| righe | 2010–2363 |
| unità | **7** — tutte `DESCRIPTION`, una per contesto |
| parole | **213 EN → 230 IT** (1,08) |
| rapporto | **0,98 – 1,18** |
| contesti | **7** — `Model 8`, `16`, `32`, `64`, `128`, `256`, `512` |
| tab / virgolette / segnaposto | **0 / 0 / 0** (tre asserzioni negative) |
| apici | **0 EN** / **4 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| invarianti | **di segmento** (43 prima · 7 qui · **0 dopo**) **e di FILE** (50 unità · righe distinte · ultima 2363 · somma dei 5 lotti = 50) |
| `sha256[:16]` | **`fa3db55b5821855f`** |

## Comandi

```bash
python staging/editorial/L277_20261020_174922/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L277_20261020_174922/verify.py    # FAIL: 0 (19 controlli, 50/50)
```

## La serie `Model`: un drone che cresce

| unità | modello | stadio |
|---|---|---|
| 1 | `Model 8` | **minerario**: estrazione sugli asteroidi, laser riadattati ad arma |
| 2 | `Model 16` | **modulare**: cresce aggiungendo materiali |
| 3 | `Model 32` | **imitando la vita**: le fabbriche automatiche lo riconfigurano |
| 4 | `Model 64` | **fregata**: come una fregata umana, ma con più potenza di fuoco |
| 5 | `Model 128` | **si divide a metà**; scudi e armi si rafforzano |
| 6 | `Model 256` | **il detto dei Quarg**: l'arma che sopravvive ai creatori |
| 7 | `Model 512` | **anello perfetto**, torrette in ogni direzione |

Le sette schede non sono testi indipendenti: sono **un ciclo di vita**. Il `check.py` verifica che tutte e sette parlino di
**droni** e che le sei tappe-chiave (minerario, modulare, vita, fregata, scissione, arma che sopravvive, anello) siano
presenti — se una scheda avesse perso il proprio posto nella progressione, il test sarebbe rosso.

## Limiti dichiarati

Nessuna approvazione (7 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non **approvato**.
