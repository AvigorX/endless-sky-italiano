# STATO — L240 (`data/avgi/avgi jobs.txt`, righe 684–1156)

**Stato: CHIUSO.** Secondo e **ultimo** lotto del file, **40 unità** (20 `VALUE` + 20 `DESCRIPTION`).
**`data/avgi/avgi jobs.txt` è COMPLETO: 102/102 (100%)**, 902 EN → 959 IT in due lotti — **nono file chiuso** della
campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L240_20261020_135130/` |
| file | `data/avgi/avgi jobs.txt` (102 unità · 902 parole) |
| righe | 684–1156 (**1156 = ultima del file**) |
| unità | **40** — **20 `VALUE`** (invariati) + **20 `DESCRIPTION`** (tradotte) |
| parole | **470 EN → 476 IT** |
| rapporto | **0,90 – 1,14** (media 0,99), gate 0,55–1,90 |
| contesti | **20**, due unità ciascuno — da `Avgi: Doctors 1` a `Avgi: Twilight Guard Relief 3` |
| tab / virgolette | **0 / 0** (due asserzioni negative scritte) |
| apici | **2 EN** (il possessivo `<planet>'s`, righe 988 e 1009) · **0 IT** |
| segnaposto | **99** in 7 famiglie: `<destination>` 26, `<planet>` 22, `<payment>` 20, `<cargo>` 11, `<bunks>` 9, `<origin>` 6, `<date>` 5 |
| famiglie `DESCRIPTION` | **8** (6 · 3 · 3 · 3 · 2 · 1 · 1 · 1), una sola resa ciascuna |
| famiglie `VALUE` | **9** (3 · 3 · 3 · 3 · 2 · 1 · 1 · 1 · 3), tutte invariate |
| `check.py` | **31 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 62 + 40 = **102/102**, riga 1156 ultima, 0 dopo, 0 sovrapposizioni |
| `sha256[:16]` | **`50d99adb0435c12d`** |

## Comandi

```bash
python staging/editorial/L240_20261020_135130/check.py     # FAIL totale: 0 (31 controlli)
python staging/editorial/L240_20261020_135130/verify.py    # FAIL: 0 (25 controlli, FILE 102/102)
```

## Cosa contiene

**Medici** (tre lavori), **materiali da costruzione** e **materiali sfusi** (sei lavori con `<origin>` → `<destination>`),
**materiali nucleari speciali** (tre, con l'avvertimento sui pirati), **corriere di informazioni** (due, con i supporti di
memoria e la rete locale), i **Twilight Guard** in quattro gradi (tre trasporti e tre licenze), e la **licenza a terra**
per le Guardie che tornano dal fronte.

## Limiti dichiarati

Nessuna approvazione (40 unità `PENDING`), nessun lavoro visto nel gioco, nessuna revisione umana. Il file è completo
**in staging**, non nel database.
