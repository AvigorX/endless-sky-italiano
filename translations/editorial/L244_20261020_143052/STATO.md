# STATO — L244 (`data/hai/hai ships.txt`, righe 362–885)

**Stato: CHIUSO.** Secondo lotto del file, **45 unità** (1 `VALUE` + 36 `TEXT` + 8 `DESCRIPTION`). Il file sale a
**74/157 (47,1%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L244_20261020_143052/` |
| file | `data/hai/hai ships.txt` (157 unità · 1.686 parole) |
| righe | 362–885 |
| unità | **45** |
| parole | **466 EN → 498 IT** |
| rapporto | **1,00 – 1,21** (media 1,02), gate 0,55–1,90 |
| contesti | **6** — `Flea`, `Geocoris`, `Grasshopper`, `Lightning Bug`, `Ladybug`, `Pond Strider` |
| tab | **1**, all'inizio dell'unità 3 (nota sui droni), conservato in entrambe le lingue |
| virgolette | **72** (2 per ciascuno dei 36 nomi, nessun altro uso) |
| apici | **0 EN** / **3 IT** (unità 9, 34, 35: elisioni) |
| segnaposto | **0** (asserzione negativa scritta) |
| copiati | **37** (1 `VALUE` + 36 nomi di equipaggiamento) |
| tradotti | **8** `DESCRIPTION` |
| `check.py` | **33 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 29 prima · 45 qui · 83 dopo · confine riga **901** (`ship:Pond Strider`) |
| copertura del file | **74/157 (47,1%)** |
| `sha256[:16]` | **`2121d513cf0c67e2`** |

## Comandi

```bash
python staging/editorial/L244_20261020_143052/check.py     # FAIL totale: 0 (33 controlli)
python staging/editorial/L244_20261020_143052/verify.py    # FAIL: 0 (25 controlli, 74/157 cumulati)
```

## Cosa contiene

Sei schede di navi Hai, cinque delle quali sono **droni o piccole unità** (Flea, Lightning Bug, Ladybug), la Geocoris
(mercattile pesante nato per competere con i mercantili umani), la Grasshopper (ricognizione veloce) e il Pond Strider
(dopo l'acquisizione della tecnologia di riparazione dello scafo). Il tab è **uno solo** e apre la nota che il gioco
mostra sotto la scheda del Flea: «I droni non escono equipaggiati con un iperpropulsore…».

## Limiti dichiarati

Nessuna approvazione (45 unità `PENDING`), nessuna scheda vista nel gioco, nessuna revisione umana. Il file **non** è
completo: 74/157 (47,1%), restano 83 unità.
