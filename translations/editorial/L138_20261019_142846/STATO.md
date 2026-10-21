# STATO — L138 · `data/starts.txt` (quarto inizio: gli Hai)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L138_20261019_142846` |
| Righe / unità | **215–358** / **47** — file al **98,2%** (111/113) |
| Tipi | **32 `CONVERSATION`** · **7 `LOGBOOK`** · **6 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Stati | **47 `PENDING`** — misurato e **asserito** |
| Contesti | **2 completi** — `start:hai space` 8, `conversation:hai intro` 39 |
| Testi | **42 propri + 5 riletti** da L135 (unità 10–14), **45 distinti** |
| Parole | **1356 EN → 1295 IT** (0,955); per unità 0,71–1,78, media 1,06 |
| Tab · virgolette | **32 unità** · **56**, con **quattro unità dispari** (26, 36, 37, 38) |
| sha256 | `ab536b2d9a5a2c29…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **31 controlli**, exit **0** — invariante di **segmento** |

## Due inizi con lo stesso nome

`start:hai space` contiene **due** blocchi `VALUE` identici, `Hai Origins`, alle righe 215 e 227. Non è un doppione: il
primo è la versione **bloccata** («Questo inizio è bloccato»), il secondo quella **sbloccabile** («Per sbloccare questo
inizio devi completare la campagna umana principale»), e le due `DESCRIPTION` iniziali differiscono nella coda.

Il controllo li verifica come **lista di coppie**, non con un conteggio:

```python
ck('DUE VALUE identici, entrambi Hai Origins (unita 1 e 5)',
   [(v['idx'], v['italian']) for v in cov if v['kind'] == 'VALUE'] == [(1, 'Hai Origins'), (5, 'Hai Origins')])
ck('i due inizi sono diversi: «Questo inizio è bloccato» contro «Per sbloccare questo inizio»', ...)
```

## Quattro battute che il sorgente lascia aperte

Le unità **26, 36, 37, 38** hanno **una sola** virgoletta: l'Hai parla e la citazione non si chiude. La resa riproduce
il difetto, e un controllo verifica che quelle quattro unità **non finiscano** con una virgoletta — cioè che nessuno le
abbia «riparate»:

```python
ck('le quattro dispari restano aperte (nessuna riparazione)',
   all(u['italian'].count('"') == 1 and not u['italian'].rstrip().endswith('"')
       for u in tu if u['idx'] in (26, 36, 37, 38)))
```

## Il mondo Hai

| EN | IT | nota |
|---|---|---|
| `Hai Origins` | **identico** | nome dell'inizio (due `VALUE`) |
| `giant, intelligent rodents` | **roditori giganti e intelligenti** | |
| `the "Unfettered"` | **gli "Unfettered"** | fazione: nome inglese fra virgolette |
| `the "prison"` | **la "prigione"** | virgolette del parlante, tradotte |
| `Sheragi` · `Drak` · `Aphid` | **invariati** | specie e modelli |
| `Pristine Jewel` | **invariato** | nome proprio della nave |
| `pay it forward` | **restituire il favore** | |
| `1.431 million credits` | **1,431 milioni di crediti** | separatore italiano, valore intatto |
| `0.3%` · `4,836` · `1.132 million` | **0,3%** · **4.836** · **1,132 milioni** | idem |

## Verifica

```bash
cd staging/editorial/L138_20261019_142846
python mkparts.py   # 47 unità · 42 proprie + 5 rilette · 2 VALUE · 32 tab · 56 virgolette · 4 dispari
python check.py     # FAIL totale: 0 (32 controlli)
python verify.py    # exit 0 (31 controlli, invariante di segmento)
```

**Non verificato**: nessun inizio avviato nel gioco; la scena di Greenwater non è stata vista.
