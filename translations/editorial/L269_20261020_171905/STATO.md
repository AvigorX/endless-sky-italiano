# STATO — L269 (`data/human/engines.txt`, righe 342–487)

**Stato: CHIUSO.** Terzo lotto del file: **17 `DESCRIPTION`**, nessun `VALUE`, **9 equipaggiamenti al plasma**. Il file è
aperto a **44/61 (72,1%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L269_20261020_171905/` |
| file | `data/human/engines.txt` (61 unità · 1.882 parole · righe 27–717) |
| righe | 342–487 |
| unità | **17** — tutte `DESCRIPTION` |
| parole | **449 EN → 511 IT** (1,14) |
| rapporto | **1,00 – 1,24** |
| contesti | **9** — Chipmunk, Greyhound, Impala, Orca, Tyrant (propulsori) · Chipmunk, Greyhound, Impala, Orca (sterzate) |
| tab | **8** (unità 2, 4, 6, 8, 10, 12, 14, 16), primo carattere |
| virgolette / segnaposto | **0 / 0** (asserzioni negative) |
| apici | **1 EN** (`Delta V's`) / **11 IT** |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 27 prima · 17 qui · **17 dopo** la 487 |
| `sha256[:16]` | **`dda3b3d775c7cced`** |

## Comandi

```bash
python staging/editorial/L269_20261020_171905/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L269_20261020_171905/verify.py    # FAIL: 0 (22 controlli, 44/61)
```

## Le tre cose delicate

1. **La nota del plasma compare otto volte** (unità pari) ed è **una sola stringa**: «I motori al plasma sono un po' più
   potenti dei motori ionici della stessa dimensione, ma sono meno efficienti dal punto di vista energetico e producono più
   calore.» Una resa, verificata come insieme.
2. **Otto tab, e solo sulle note**: la scheda del modello non è mai rientrata. L'ultimo blocco (Orca steering, riga 487) ha
   **solo** la nota — conseguenza del confine di lotto, verificata come tale.
3. **Tre nomi generici non sono nomi di modello**: `greyhound` (il cane del disegno sulla cassa), `Tyrannosaurus Rex` (la
   figura sulla cassa), `rodent` (il roditore carico di caffeina). Restano tradotti come nomi comuni, mentre `Greyhound`,
   `Impala`, `Orca`, `Tyrant` restano dove l'inglese li nomina.

## Limiti dichiarati

Nessuna approvazione (17 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **17 unità** (L270,
terminale).
