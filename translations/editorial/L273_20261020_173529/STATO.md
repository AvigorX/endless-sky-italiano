# STATO — L273 (`data/korath/korath ships.txt`, righe 95–360)

**Stato: CHIUSO.** Primo lotto del file delle navi Korath: **8 `DESCRIPTION`** lunghe su **quattro navi**. Il file è aperto a
**8/50 (16,0%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L273_20261020_173529/` |
| file | `data/korath/korath ships.txt` (50 unità · 2.049 parole · righe 95–2363) |
| righe | 95–360 |
| unità | **8** — tutte `DESCRIPTION` |
| parole | **458 EN → 523 IT** (1,14) |
| rapporto | **1,05 – 1,20** |
| contesti | **4** — `Rano'erek`, `Palavret`, `Tubfalet`, `'nra'ret` |
| tab | **4** (unità 2, 4, 6, 8), primo carattere |
| virgolette / segnaposto | **0 / 0** (asserzioni negative) |
| apici | **9 EN** (tutti nei nomi) / **15 IT** (nomi + elisioni) |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 8 qui · **42 dopo** la 360 |
| `sha256[:16]` | **`6e61f954c3436a8c`** |

## Comandi

```bash
python staging/editorial/L273_20261020_173529/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L273_20261020_173529/verify.py    # FAIL: 0 (22 controlli, 8/50)
```

## Le quattro navi

| nave | tipo | che cosa racconta |
|---|---|---|
| **Rano'erek** | nave dragante per asteroidi | nasce dopo l'esilio: le navi-mondo erano troppo preziose, ai razziatori mancava la stiva |
| **Palavret** | nave da razzia | intitolata a una capitana che morì per portare a casa un carico di **pesce rubato** |
| **Tubfalet** | nave da razzia (nuova) | intitolata a un ammiraglio ferito che restò sul **ponte ammiraglia** durante un attacco dei Remnant |
| **'nra'ret** | cacciatore | primo progetto **davvero nuovo** dopo l'Esodo, primo costruito **solo** per il combattimento |

## Lessico fissato (dal corpus, non inventato)

| inglese | resa | fonte |
|---|---|---|
| `Exile ships` / `the Exiles` | **navi dell'Esilio** / **gli Esiliati** | `esiliat` 49 unità, «in esilio» |
| `raiders` | **razziatori** | 127 unità, e L272 |
| `world-ships` | **navi-mondo** | `nave-mondo` |
| `raiding ship` | **nave da razzia** | «flotte di razzia» |
| `carried chaser` / `chaser` | **cacciatore imbarcato** / **cacciatore** | `cacciator` 32 unità |
| `langrage heavers` | **lanciatori di mitraglia** | `mitraglia` |
| `Fire-Lances` | **Lance di fuoco** | termine nuovo, dichiarato |
| `flag bridge` | **ponte ammiraglia** | `ammiraglia` 44 unità |

## Limiti dichiarati

Nessuna approvazione (8 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **42 unità**.
