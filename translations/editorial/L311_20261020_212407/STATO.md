# STATO — L311 (`data/bunrodea/bunrodea outfits.txt`, righe 25–130)

**Stato: CHIUSO.** Primo lotto del file: **12 unità su 33** (**36,4%**). `check.py` esce 0 con **22 controlli**; `verify.py` esce
0 con **18 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L311_20261020_212407/` |
| file | `data/bunrodea/bunrodea outfits.txt` (33 unità · 1.252 parole · righe 25–402) |
| righe | 25–130 |
| unità | **12** — tutte `DESCRIPTION` |
| contesti | **8** — **4 coppie** + **4 schede singole** |
| parole | **480 EN → 449 IT** (0,935) |
| rapporto | **0,90 – 1,15** |
| tab | **4** — 54, 70, 114, 130 (la **seconda** unità di ogni coppia) |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **1 EN / 9 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **18 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima della 25 · 12 qui · **21 dopo la 130** (limite monotòno) |
| copertura | **12/33** — **stampata, non asserita**: il file non è finito |
| `sha256[:16]` | **`f5639f821a4e7bef`** |

## Comandi

```bash
python staging/editorial/L311_20261020_212407/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L311_20261020_212407/verify.py    # FAIL: 0 (18 controlli, 12/33)
```

## Com'è fatto il lotto

Otto contesti, ognuno un equipaggiamento Bunrodea:

| righe | contesto | forma |
|---|---|---|
| 25 | `Shield Relay Booster` | scheda singola |
| 38 | `Shield Relay Limiter` | scheda singola |
| 53–54 | `Small Shield Relay` | **coppia**: scheda + nota degli upgrade |
| 69–70 | `Large Shield Relay` | **coppia**: storia + nota degli upgrade |
| 85 | `Nanite Enhancer` | scheda singola |
| 98 | `Nanite Limiter` | scheda singola |
| 113–114 | `Small Nanite Fabricator` | **coppia**: scheda + nota degli upgrade |
| 129–130 | `Large Nanite Fabricator` | **coppia**: storia + nota degli upgrade |

## La famiglia della nota degli upgrade

Il test difende **tre** fatti distinti, non uno:

```
54 == 70     identiche in inglese  ->  identiche in italiano  («..., però.»)
114 != 130   diverse in inglese    ->  diverse in italiano    («..., però.» / «..., tuttavia.»)
```

La differenza **è del sorgente** (`though.` / `however.`) e sta **nell'ultima parola**: la resa la mette **nello stesso punto**,
così la variazione non si perde.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| coppie | la **tab** sulla **seconda** unità, righe esatte `[54, 70, 114, 130]` |
| nota | 54 = 70; 114 ≠ 130 **solo nell'ultima parola**; `però` / `tuttavia` |
| nomi | i **8 nomi** degli equipaggiamenti **invariati** dove compaiono |
| vuote | 0 virgolette, 0 segnaposto, 0 alternative |
| lessico | relay, scudi, potenziatori, limitatori, fabbricatore di naniti, scafo |
| segmento | 0 prima · 12 qui · **21 dopo** (il file non è finito) |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **Il file non è finito**: mancano
**21 unità / 772 parole**.
