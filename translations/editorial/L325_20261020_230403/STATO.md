# STATO — L325 (`data/kahet/kahet outfits.txt`, righe 54–573)

**Stato: CHIUSO — LOTTO TERMINALE, FILE INTERO.** Il file è **completo: 25/25 (100%)**, **trentanovesimo file interamente tradotto**
(**98** su 167). `check.py` esce 0 con **27 controlli**; `verify.py` esce 0 con **20 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8).
Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L325_20261020_230403/` |
| file | `data/kahet/kahet outfits.txt` (**25/25 unità · 848 parole · righe 54–573**) |
| righe | 54–573 (**tutto il file**) |
| unità | **22 `DESCRIPTION` + 3 `VALUE`** |
| contesti | **20** — cinque con **due** unità, **quindici** con una |
| parole | **848 EN → 870 IT** (1,026) |
| rapporto | **0,98 – 1,27** |
| tab | **2** — righe **285** (nota) e **400** |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **17 EN in 15 unità** (425 e 561 ne hanno due) / 26 IT |
| `check.py` | **27 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 25 unità · **0 prima, 0 dopo** · prima **54** · ultima **573** |
| `sha256[:16]` | **`cd118d0935e22235`** |

## Comandi

```bash
python staging/editorial/L325_20261020_230403/check.py     # FAIL totale: 0 (27 controlli)
python staging/editorial/L325_20261020_230403/verify.py    # FAIL: 0 (20 controlli, FILE 25/25)
```

## I tre `VALUE` copiati

| riga | stringa | trattamento |
|---|---|---|
| 444 | `Maeri Engine Nacelles` | **copiata** |
| 468 | `Ka'het Sustainer Nacelles` | **copiata** |
| 492 | `Telis Engine Nacelles` | **copiata** |

Sono **nomi di equipaggiamento**, e restano inglesi **anche se** nel corpo delle schede `nacelle` diventa «gondole» (corpus: righe 809
e 815 dei lotti precedenti). La coerenza è con il **tipo** (`VALUE` = nome), non con il **lessico** della prosa: `check.py` verifica
l'identità e **vieta** che la resa contenga «gondol» o «motore», `verify.py` la verifica **sulla forma** (finisce per `Nacelles`, stesso
numero di parole).

## `Builders` → «Costruttori», e la genealogia

| nome | resa | occorrenze nel lotto |
|---|---|---|
| `Builders` | **«Costruttori»** | 11 (0 `Builders` in italiano) |
| `Ka'het` | invariato | 8 |
| `Ka'mar` | invariato | 3 |
| `Het` | invariato | 5 |
| `Telis'het` | invariato | 1 |

La genealogia del file è **Ka'mar** (droni) → **Het** (navi) → **Ka'het** (nate dopo, quando il progetto delle gondole viene
standardizzato). Il test verifica i tre passaggi **nei punti dove il testo li dichiara** (414, 561), non in astratto.

## Due errori di metodo, e uno che vale una regola nuova

| # | errore | conseguenza |
|---|---|---|
| 1 | `Ka'mar` atteso **4** volte | sono **3**: corretto al valore misurato |
| 2 | «la seconda persona italiana dove l'inglese dice `your`» confrontata con la **regex italiana** (`tu/tua/…`) | l'inglese dava insieme **vuoto**: servono **due regex**, una per lingua |
| 3 | `\\b` scritto dentro un heredoc Python | nel file sono finiti **byte `0x08` (backspace)**: la regex `r'<BS>(your\|you)<BS>'` non corrispondeva a nulla, e `ast.parse` **passava lo stesso** |

Il terzo è il più insidioso: **`ast.parse` non vede un carattere di controllo dentro una stringa**. Da oggi, dopo ogni patch generata da
uno script, si controlla anche il **contenuto in byte** (`open(...,'rb').read().count(8)`) — non basta il parser.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| tipi | **22 `DESCRIPTION` + 3 `VALUE`**, separati |
| `VALUE` | identità all'inglese **e** forma di nome (`Nacelles`, stesse parole) |
| contesti | **20**; cinque coppie esatte (EMP Deployer, Grand Restorer, Maeri, Ka'het Sustainer, Telis) |
| tab | **2** (285, 400), come primo carattere, e **identiche al numero di tab dell'inglese** riga per riga |
| nota | riga 285 identica al corpus, e presente in **≥2 altri lotti** |
| seconda persona | **solo** l'unità 573, dove l'inglese dice `your`/`you` |
| apici | **17** in **15** unità; 425 e 561 doppi |
| vuote | **0 virgolette**, **0 segnaposto**, **0 alternative** |
| FILE | **0 prima · 25 qui · 0 dopo** · prima 54 · ultima 573 · **25/25 asserita** |

## Limiti dichiarati

Nessuna approvazione (25 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. `sustainer` è reso **«motore di
sostentamento»**: il corpus non aveva occorrenze precedenti, quindi la scelta è nuova e **dichiarata** (non «corretta» da confronto).
