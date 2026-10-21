# L21b — report di chiusura

**File:** `data/human/intro missions.txt`, righe **23–2319** (file completo)
**Directory:** `staging/editorial/L21b_20261017_210204/`
**Sorgente:** `endless-sky/data/human/intro missions.txt`, commit `b4aa3bac3` (non modificato)

## 1. Volume

| misura | valore |
|---|---|
| parole inglesi | **19.451** |
| parole italiane | **17.681** (90,9%) |
| unità tradotte | **637 / 637** |
| contesti | **67** (4 alberi di missione introduttiva + conversazioni) |
| parti | **7** |
| tab / virgolette | 380 / 1.089 — identici al sorgente |
| token `<…>` | 426 in italiano contro 433 in inglese: **7 pronomi inglesi** resi con costruzione italiana (eccezione enumerata, vedi `review.md` §2) |
| rapporto IT/EN | min 0,62 · max 1,54 |

Tipi: `CONVERSATION` 209 · `MISSION_TEXT` 288 · `VALUE` 50 · `DESCRIPTION` 50 · `LOGBOOK` 36 · `DIALOG` 4.

## 2. Controlli

```
check.py     FAIL totale: 0    · 7 parti · duplicati inglese 70 gruppi (297 unità) · 0 mancanti
verify.py    24 controlli, 0 FAIL, exit 0
```

Il controllo più significativo: **copertura del file 637 / 637**. `intro missions.txt` è tradotto
per intero, senza sovrapposizioni con altri lotti (nessun altro lotto tocca questo file).

Verifica indipendente dei token: le unità con token diversi sono **esattamente** {54, 84, 85, 145, 148},
in ognuna si perdono **solo** pronomi, il totale perso è **7**. Un solo token perso altrove
farebbe fallire `verify.py`.

## 3. Integrità

| verifica | esito |
|---|---|
| repository `endless-sky` (`b4aa3bac3`) | non modificato |
| `state.db` | non scritto; 637 unità restano `PENDING` |
| batch, glossario, inventario, output approvati | non toccati |
| patch K4 / build / test di gioco / applicazione | non eseguiti |
| rendering nel gioco | **non verificato** |

`translation.json` sha256[:16] = `70d260bc3fcec51b` (rigenerato da `check.py` dalle 7 parti).

## 4. Bilancio del lotto L21

| segmento | file | righe | unità | EN | IT |
|---|---|---|---:|---:|---:|
| L21a | `human missions.txt` | 10812–11777 | 465 | 11.046 | 10.356 |
| L21b | `intro missions.txt` | 23–2319 | 637 | 19.451 | 17.681 |
| **L21** | | | **1.102** | **30.497** | **28.037** |

**Deviazione dal target dichiarata:** 30.497 parole contro un obiettivo di ~40.000 (−23,8%).
Motivo: entrambi i file si sono esauriti (L21a chiude `human missions.txt`, L21b chiude
`intro missions.txt`). Non è stato allungato il lotto con un terzo file parziale solo per
raggiungere la cifra; il lotto successivo (L22) riparte da `data/human/jobs.txt`.

## 5. Prossimo passo

`data/human/jobs.txt` — 390 unità `PENDING`, 5.823 parole. Misurare prima di aprire:

```bash
python staging/editorial/tools/next_section.py "data/human/jobs.txt" 1 5000 8000
```
