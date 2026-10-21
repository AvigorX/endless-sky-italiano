# STATO — L294 (`data/human/marauders.txt`, righe 62–484)

**Stato: CHIUSO.** Primo lotto del file: **quattro serie da tre** di navi pirata modificate. File aperto a **12/29 (41,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L294_20261020_193921/` |
| file | `data/human/marauders.txt` (**29 unità · 1.492 parole · righe 62–1.146 · 29 `DESCRIPTION`**) |
| righe | 62–484 |
| unità | **12**, tutte `DESCRIPTION` |
| serie | **4 × 3** — `Arrow` (62, 84, 111) · `Bounder` (166, 193, 223) · `Falcon` (288, 325, 364) · `Firebird` (423, 453, 484) |
| parole | **493 EN → 549 IT** (1,11) |
| rapporto | **1,08 – 1,29** |
| tab / virgolette / segnaposto / alternative | **0 / 0 / 0 / 0** (asserzioni vuote) |
| apici | **5 EN / 7 IT** |
| seconda persona | **4 unità** (1, 8, 9, 10) |
| `check.py` | **19 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 12 qui · **17 dopo** la 484 |
| `sha256[:16]` | **`a6077032b4a171fb`** |

## Comandi

```bash
python staging/editorial/L294_20261020_193921/check.py     # FAIL totale: 0 (19 controlli)
python staging/editorial/L294_20261020_193921/verify.py    # FAIL: 0 (21 controlli)
```

## Quattro modelli, tre allestimenti

| modello | righe | tre varianti |
|---|---|---|
| `Arrow` | 62 / 84 / 111 | combattimento · **motori** («missile sovradimensionato») · **armi** (competere con la `Headhunter`) |
| `Bounder` | 166 / 193 / 223 | scorta pesante · **motori enormi** · **«il più letale e il più elegante»** |
| `Falcon` | 288 / 325 / 364 | artigiani scrupolosi · **velocità** («hot-rodding») · **potenza di fuoco** |
| `Firebird` | 423 / 453 / 484 | nessun pezzo originale · **motore in più** · **armamento ancora più pesante** |

Il test verifica che le **tre varianti di ogni serie** si distinguano per contenuto (parole chiave diverse), non solo per numero:
quattro descrizioni identiche sarebbero un errore invisibile a un controllo di sola lunghezza.

## Il registro: tecnico, ma non impersonale

Le schede sono in **terza persona**, ma **quattro** si rivolgono al lettore:

> «…uno degli intercettori più pesanti che **possiate** trovare» · «Se il **tuo** sogno è sfrecciare…» · «…quasi qualsiasi
> insieme di armi **tu** possa immaginare» · «A giudicare dalle modifiche… **sospetti** che…»

È l'opposto delle schede Gegno (L286–L289), dove il «tu» era **vietato**. Il test elenca le **righe ammesse** (1, 8, 9, 10) invece
di applicare l'una o l'altra regola alla cieca.

## Terminologia del corpus

| inglese | resa | nota |
|---|---|---|
| `gun port` | **porto per cannoni** | forma del corpus (11 occorrenze), non «feritoia» |
| `turret mount` | **supporto per torrette** | |
| `hull plating` | **corazzatura** | |
| `interceptor` | **intercettore** | 58 occorrenze nel corpus |
| `outfit space` | **spazio per gli equipaggiamenti** | |
| `shield emitters` | **emettitori di scudi** | |
| `courier-scout` | **corriere-esploratore** | |
| `Megaparsec`, `Tarazed`, `Betelgeuse`, `Lionheart`, `Headhunter`, `Flivver` | **invariati** | cantieri, marchi, modelli |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **17 unità**.
