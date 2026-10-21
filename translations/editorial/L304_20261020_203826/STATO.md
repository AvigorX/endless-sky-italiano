# STATO — L304 (`data/quarg/quarg outfits.txt`, righe 37–137)

**Stato: CHIUSO.** Primo lotto del file: **undici schede** Quarg in **sei contesti** — **cinque coppie** e la **prima metà** della
sesta. Il secondo paragrafo compare **quattro volte identico** e **una con variante**. File a **11/31 (35,5%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L304_20261020_203826/` |
| file | `data/quarg/quarg outfits.txt` (**31 unità · 1.506 parole · righe 37–579 · 31 `DESCRIPTION`**) |
| righe | 37–137 |
| unità | **11**, tutte `DESCRIPTION` |
| contesti | **6** — 5 coppie + **1 prima metà** (`Large Graviton Steering`, 137) |
| coppie | `Small Graviton Thruster` 37/38 · `Small Graviton Steering` 54/55 · `Medium Graviton Thruster` 77/78 · `Medium Graviton Steering` 95/96 · `Large Graviton Thruster` 119/120 |
| parole | **466 EN → 473 IT** (1,02) |
| rapporto | **0,99 – 1,16** |
| tab | **5** — righe **38, 55, 78, 96, 120** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **1 EN / 11 IT** |
| ripetizione | **unità 4, 6, 8, 10 identiche** + **variante** all'unità 2 (riga 38) |
| `check.py` | **21 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** · 11 qui · **20 dopo** la 137 |
| `sha256[:16]` | **`20e913ff49c84acc`** |

## Comandi

```bash
python staging/editorial/L304_20261020_203826/check.py     # FAIL totale: 0 (21 controlli)
python staging/editorial/L304_20261020_203826/verify.py    # FAIL: 0 (22 controlli)
```

## Quattro identiche e una variante: entrambe conservate

Il secondo paragrafo dei moduli Quarg è un **ritornello**: «Hanno anche strane capacità che sembrano violare le leggi della
fisica…».

| righe | inglese | resa |
|---|---|---|
| **38** | `**These engines** also have… Ships **equipped with them** accelerate…` | «**Questi motori** hanno anche… Le navi che **ne sono dotate** accelerano…» |
| **55, 78, 96, 120** | `**They** also have… Ships **with these engines** accelerate…` | «**Hanno** anche… Le navi **con questi motori** accelerano…» |

La variante **non è un errore**: è il testo del primo modulo, scritto quando il **soggetto** era ancora «questi motori», mentre
nelle altre quattro il soggetto è diventato «loro». Il test verifica le **quattro con `set()`** e la variante **separatamente**:
uniformare tutto avrebbe cancellato una differenza del sorgente.

## Il confine taglia una coppia, ma non dentro il lotto

La **137** (`Large Graviton Steering`) è la **prima** metà di una coppia, la **138** la seconda: il segmento finisce **esattamente
fra le due**. Il test verifica che la 137 **non** inizi con la tab e che la 138 sia la prima unità dopo il confine — il taglio è
**dichiarato**, non accidentale.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `thrusters` | **propulsori** | corpus |
| `steering engines` | **motori di governo** | corpus («governo» = steering) |
| `steering thrusters` | **propulsori di governo** | |
| `center of mass` | **centro di massa** | |
| `gyroscope` | **giroscopio** | |
| `gravitational wave antenna` | **antenna per onde gravitazionali** | |
| `Quarg` | **Quarg** | invariato |
| `humanity` | **umanità** | |

## Limiti dichiarati

Nessuna approvazione (11 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **20 unità**.
