# STATO — L243 (`data/hai/hai ships.txt`, righe 15–332)

**Stato: CHIUSO.** Primo lotto del file, **29 unità** (1 `VALUE` + 23 `TEXT` + 5 `DESCRIPTION`). Il file resta **aperto a
29/157 (18,5%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L243_20261020_142300/` |
| file | `data/hai/hai ships.txt` (157 unità · 1.686 parole; 132 `TEXT` + 23 `DESCRIPTION` + 2 `VALUE`) |
| righe | 15–332 |
| unità | **29** |
| parole | **451 EN → 456 IT** |
| rapporto | **1,00 – 1,09** (media 1,01), gate 0,55–1,90 |
| contesti | **4** — `Anomalocaris`, `Aphid`, `Centipede`, `Cicada` |
| tab / virgolette | **0** / **48** (2 per unità, 24 unità su 29) |
| apici | **4 EN** (possessivi) · **19 IT** (elisioni) |
| segnaposto | **0** (asserzione negativa scritta) |
| copiati | **24** (1 `VALUE` + 23 nomi di equipaggiamento, virgolette comprese) |
| tradotti | **5** `DESCRIPTION` |
| `check.py` | **30 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima · 29 qui · 128 dopo · confine riga **362** (`ship:Flea`) |
| copertura del file | **29/157 (18,5%)**, stampata e non asserita |
| `sha256[:16]` | **`b21c7a4b97f7f745`** |

## Comandi

```bash
python staging/editorial/L243_20261020_142300/check.py     # FAIL totale: 0 (30 controlli)
python staging/editorial/L243_20261020_142300/verify.py    # FAIL: 0 (23 controlli, 29/157)
```

## Cosa contiene

Le schede di **quattro navi Hai**: l'**Anomalocaris** (due versioni: la scheda normale e quella del relitto rimasto a lungo
sott'acqua), l'**Aphid** (il mercantile più leggero, spina dorsale dell'economia interplanetaria), il **Centipede** (il
trasporto di lusso nato dalla cooperazione umano-Hai, con la battuta sulle ghiande in salamoia) e la **Cicada** (vecchia
quanto l'Aphid, così affidabile che il mercato dell'usato ne è saturo: chiude col motto del cantiere Yeer e Ki, «Al
servizio per tutta la vita.»). I 23 `TEXT` sono i nomi degli equipaggiamenti installati (`"Biroo" Atomic Thruster`,
`"Basrem" Atomic Steering`…), copiati con le virgolette.

## Limiti dichiarati

Nessuna approvazione (29 unità `PENDING`), nessuna scheda vista nel gioco, nessuna revisione umana. Il file **non** è
completo: 29/157.
