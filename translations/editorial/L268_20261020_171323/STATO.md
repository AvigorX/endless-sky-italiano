# STATO — L268 (`data/human/engines.txt`, righe 195–323)

**Stato: CHIUSO.** Secondo lotto del file: **15 `DESCRIPTION`**, nessun `VALUE`, **8 equipaggiamenti**. Il file è aperto a
**27/61 (44,3%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L268_20261020_171323/` |
| file | `data/human/engines.txt` (61 unità · 1.882 parole · righe 27–717) |
| righe | 195–323 |
| unità | **15** — tutte `DESCRIPTION` |
| parole | **450 EN → 459 IT** |
| rapporto | **0,96 – 1,28** |
| contesti | **8** — X4700, X5700 (propulsori), X1200, X2200, X3200, X4200, X5200 (sterzata), X1100 (inverso) |
| tab | **8** (unità 1, 3, 5, 7, 9, 11, 13, 15), primo carattere |
| virgolette / apici EN | **0 / 0** (asserzioni negative) |
| apici IT | **6** (unità 2, 4, 6, 10, 12, 14) |
| segnaposto | **0** (asserzione negativa) |
| `check.py` | **21 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 12 prima · 15 qui · **34 dopo** la 323 |
| `sha256[:16]` | **`60e7d90fa1230d16`** |

## Comandi

```bash
python staging/editorial/L268_20261020_171323/check.py     # FAIL totale: 0 (21 controlli)
python staging/editorial/L268_20261020_171323/verify.py    # FAIL: 0 (21 controlli, 27/61)
```

## Le due cose delicate

1. **La scheda ionica compare sette volte** (unità 1, 3, 5, 7, 9, 11, 13) ed è **identica a quella di L267**: ripresa alla
   lettera, e il `check.py` la confronta **rileggendo** `L267/translation.json`.
2. **`reverse thruster` → «propulsore inverso»**: termine **nuovo** nel corpus, fissato qui. La scheda spiega anche perché va
   montato nella **sezione delle armi** e non in quella dei motori — dettaglio funzionale che la resa conserva.

## Limiti dichiarati

Nessuna approvazione (15 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **34 unità**.
