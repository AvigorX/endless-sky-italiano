# STATO — L176 · `avgi ships.txt` (**il lotto dei nomi**: 10 su 20 unità sono equipaggiamento)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L176_20261019_185224` |
| Righe / unità | **930–1399** / **20** — file al **44/102 (43,1%)** |
| Tipi | **10 `TEXT`** (nomi) · **8 `DESCRIPTION`** · **2 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Contesti | **4** (6 + 3 + 4 + 7) · **14 testi distinti** su 20 |
| Parole | **463 EN → 493 IT** (1,065) · rapporto DESCRIPTION **1,06–1,24**, media **1,15** |
| Tab · virgolette | **4** (idx 3, 4, 9, 13) · **20** (tutte nei `TEXT`, 2 ciascuno) |
| Apici | **3**, uno in idx 2, 3 e 4 (`Undsyni's`) · **nessun possessivo in italiano** |
| sha256 | `e2d7853a434cdf00…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **25**, exit **0** |

## Cosa è stato **copiato** e cosa **tradotto**

| tipo | unità | trattamento |
|---|---|---|
| `TEXT` (nomi di equipaggiamento) | 1, 5, 6, 7, 11, 15, 16, 18, 19, 20 | **identici al sorgente**, virgolette comprese |
| `VALUE` (nomi di nave) | 10 `Tremoros`, 14 `Prismaios` | **identici al sorgente** |
| `DESCRIPTION` (prosa) | 2, 3, 4, 8, 9, 12, 13, 17 | **tradotte** |

I 10 nomi: `Z-333 "Spark" Fusion Torch` ×6, `"Nettle" KKV` ×2, `A-3600 "Beam" Amat Drive`, `"Orchid" Nuclear Missile`.
Le **20 virgolette** del lotto sono tutte lì.

## I due refusi del sorgente, non propagati

| unità | sorgente | italiano |
|---|---|---|
| 9 | `habitatation` | **cilindri abitativi** (scritto correttamente) |
| 2, 3, 4 | `Undsyni's` | **dell'Undsyni / lo avevano reso / della nave** (nessun possessivo) |

## Verifica

```bash
cd staging/editorial/L176_20261019_185224
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (25 controlli)
```

**Non verificato**: nessuna astronave vista a schermo; i testi non sono stati caricati nel gioco.
