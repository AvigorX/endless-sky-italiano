# STATO — L296 (`data/human/marauders.txt`, righe 884–1146)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 29/29 (100%)**, **venticinquesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L296_20261020_195122/` |
| file | `data/human/marauders.txt` (**29/29 unità · 1.492 parole · righe 62–1.146**) |
| righe | 884–1146 |
| unità | **8**, tutte `DESCRIPTION` |
| contesti | **3** — `Quicksilver` (884, 910) · `Raven` (968, 996, 1026) · `Splinter` (1083, 1114, 1146) |
| parole | **505 EN → 532 IT** (1,05) |
| rapporto | **1,03 – 1,21** |
| tab / virgolette / segnaposto / alternative | **0 / 0 / 0 / 0** (asserzioni vuote) |
| apici | **10 EN / 10 IT** |
| ripetizione | **unità 1 e 2 identiche** (righe 884 e 910) |
| seconda persona | **3 unità** (3, 5, 7) — il contratto ne prevedeva **una** |
| `check.py` | **21 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 29 unità · somma lotti **12+9+8** · righe distinte · prima **62** · ultima **1.146** · **0 dopo** |
| `sha256[:16]` | **`69471807998be973`** |

## Comandi

```bash
python staging/editorial/L296_20261020_195122/check.py     # FAIL totale: 0 (21 controlli)
python staging/editorial/L296_20261020_195122/verify.py    # FAIL: 0 (23 controlli, FILE 29/29)
```

## La seconda persona era in tre unità, non una

Il contratto diceva: «se compare la seconda persona (riga 1114) va elencata come eccezione». Misurato, compare in **tre**:

| unità | riga | inglese | resa |
|---|---|---|---|
| 3 | 968 | `the patchwork that **you** expect` | «quel patchwork che **ti** aspetti» |
| 5 | 1026 | `making **you** wonder` | «il che fa chiedere» (impersonale, ma la frase è rivolta al lettore) |
| 7 | 1114 | `**You're** not likely to find` | «Non è probabile che **tu** trovi» |

Il test elenca `[3, 5, 7]`: **vince il workspace**, e la correzione è scritta qui.

## I tre motivi delle serie

| serie | motivo ricorrente | verifica |
|---|---|---|
| `Raven` (968, 996, 1026) | «lo scafo centrale si riconosce **solo grazie alle ali**» | **tutte e tre** contengono «ali» |
| `Splinter` (1083, 1114, 1146) | «**ampie sezioni dello scafo**» coperte di scudi e corazzatura | **tutte e tre** contengono l'espressione |

Sono **formule del sorgente**, e il test le richiede in ogni variante: se una sola le avesse perse, la serie si sarebbe sfaldata.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `hard points` | **punti di attacco** | corpus (L288) |
| `bulkheads` | **paratie** | |
| `engine bays` | **baie motore** | |
| `engine port` | **porto motore** | coerente con «porto per cannoni» |
| `sub-kiloton warship` | **nave da guerra sotto il kilotonnellaggio** | |
| `mimicry of Lionheart's Headhunter` | **imitazione della Headhunter della Lionheart** | |

## Limiti dichiarati

Nessuna approvazione (8 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
