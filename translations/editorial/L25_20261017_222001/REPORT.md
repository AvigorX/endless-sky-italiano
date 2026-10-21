# REPORT — L25

**Lotto:** L25
**File:** `data/coalition/coalition missions.txt`
**Intervallo:** righe **16–2907** (unità 1–1.174 del file)
**Data di chiusura:** 2026-10-17
**Stato:** CHIUSO — `check.py` `FAIL totale: 0`, `verify.py` exit 0

## 1. Consegna

| voce | valore misurato |
|---|---|
| unità tradotte | **1.174** |
| di cui non traducibili (`UI_LABEL`) | **16** |
| di cui traducibili | **1.158** |
| parole inglesi | **37.459** |
| parole italiane | **35.851** |
| rapporto complessivo IT/EN | **0,957** |
| contesti distinti | **65** |
| parti | **13** (`part01.json` … `part13.json`) |
| riga iniziale / finale del lotto | **16 / 2907** |
| unità residue nello stesso file | **406** (righe 2913–3868, 10.765 parole) |

Il lotto è più piccolo del target (−37.459 parole contro ~40.000, **−6,4%**) perché il confine è stato
misurato con `next_section.py` su un cambio di contesto reale, non scelto a naso.

## 2. Composizione per tipo

| tipo | unità |
|---|---|
| `MISSION_TEXT` | 975 |
| `DIALOG` | 64 |
| `VALUE` | 56 |
| `DESCRIPTION` | 56 |
| `UI_LABEL` (NT) | 16 |
| `LOGBOOK` | 7 |

## 3. Misure di conformità (esecuzione completa, non per intervallo)

```
FAIL totale .............. 0
tab .................... 869 / 869
virgolette ........... 1746 / 1746
token <...> ............. 331 / 331
backtick .................. 0 / 0
traduzioni vuote ......... 0
duplicati non spiegati ... 0
caratteri non latini ..... nessuno
trattini lunghi/en-dash .. nessuno
rapporto lunghezze ....... 0,64 – 1,89
```

## 4. Duplicati e virgolette

- **42 gruppi** di inglese identico, **110 unità** coinvolte: risposte alternative con lo stesso esito,
  `DIALOG` di scorta mancante, blocchi ripetuti di Drugub, righe di capacità.
- **2 unità con virgolette dispari** nel sorgente, riprodotte esattamente:
  - **800**: una sola virgoletta (aperta, mai chiusa);
  - **1004**: cinque virgolette, ultima battuta non chiusa.

## 5. Verifica indipendente

`verify.py` (**24 controlli**, exit **0**) rilegge il file sorgente, `state.db` e le parti su disco
senza riusare la logica di `check.py`:

- riga grezza identica al file;
- `english`/`kind`/`path` identici al database;
- stato `PENDING` per tutte, **nessuna** `APPROVED`;
- id univoci, ordine uguale al sorgente, stesse unità nei due JSON;
- collocazione: 1.174 unità, righe 16–2907, **0** unità prima, **406** dopo;
- lotto dentro il file (1.174 su 1.580 unità) e **nessuna unità duplicata** fra lotti dello stesso file
  (dal 2026-10-17 esiste anche L26 sullo stesso file, e il controllo è stato reso indipendente dalla
  copertura cumulativa proprio per questo);
- 16 NT identiche al sorgente;
- parità esatta dei token; tab, virgolette, backtick uguali al sorgente;
- italiano mai vuoto, nessun carattere non latino sospetto, nessun trattino lungo;
- rapporto definito per tutte le unità;
- le 13 parti ricostruiscono `translation.json`.

**sha256[:16] di `translation.json`:** `fc850daffc4363da`

## 6. Stato del progetto dopo L25

| voce | valore |
|---|---|
| unità in staging | **10.603** (29 directory con `translation.json`) |
| parole EN → IT in staging | **330.726 → 315.924** |
| unità `PENDING` nel DB | **32.560** |
| unità `APPROVED` nel DB | **364** (nessuna di questo lotto) |
| unità non traducibili nel DB | **630** |
| residuo traducibile | **21.327** |
| `coalition missions.txt` | **1.174 / 1.580** (74,3%) |

## 7. Che cosa questo report non dimostra

- **Non** dimostra che la traduzione sia corretta: dimostra che è **completa, coerente e conforme** ai
  controlli definiti.
- **Non** c'è rendering nel gioco: nessuna stringa è stata vista a schermo.
- **Non** c'è approvazione nel database: lo staging non è approvazione.
- **Non** c'è revisione umana terza.

## 8. Prossimo passo

L26: `data/coalition/coalition missions.txt`, righe **2913–3868** — le **406 unità / 10.765 parole**
che chiudono il file (1580/1580). Va dichiarata la deviazione di dimensione: è un lotto corto per
scelta, perché chiudere il file vale più che lasciare un troncone.
