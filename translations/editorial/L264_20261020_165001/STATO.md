# STATO — L264 (`data/remnant/remnant jobs.txt`, righe 703–741) — LOTTO TERMINALE

**Stato: CHIUSO — LOTTO TERMINALE.** Quarto e ultimo lotto del file, **9 unità**. Con questo lotto
**`data/remnant/remnant jobs.txt` è COMPLETO a 87/87 (100%)**: **quindicesimo file chiuso** della campagna.

| voce | valore |
|---|---|
| directory | `staging/editorial/L264_20261020_165001/` |
| file | `data/remnant/remnant jobs.txt` (87 unità · 1.462 parole · righe 19–741) — **CHIUSO 87/87** |
| righe | 703–741 |
| unità | **9** — 5 `DIALOG` + 2 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` |
| parole | **203 EN → 196 IT** |
| rapporto | **0,87 – 1,13** |
| contesti | **2** — `Remnant: Rescue 5` (2) → `Remnant: Disable 1` (7) |
| tab / virgolette | **0 / 0** in entrambe le lingue |
| apici | **7 EN** (6 da `A'awoj`, 1 da `You've`) / **8 IT** |
| segnaposto | **8** — `<payment>` 3, `<planet>` 3, `<npc>` 2 |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 78 prima · 9 qui · **0 dopo** la 741 · **87 righe distinte su 87** |
| `sha256[:16]` | **`941b0ec0fdf96ef4`** |

## Comandi

```bash
python staging/editorial/L264_20261020_165001/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L264_20261020_165001/verify.py    # FAIL: 0 (20 controlli, FILE 87/87)
```

## Il conto del file

```
L261  25 · L262  29 · L263  24 · L264   9  =  87 unità = 87 righe distinte · completo
```

## Le due missioni

1. **`Rescue 5`** (unità 1–2): la nave dispersa torna; il capitano ringrazia **prima** che arrivi l'assegnazione di risorse.
2. **`Disable 1`** (unità 3–9): una **Dathnak A'awoj** danneggiata è bloccata vicino a **Postverta** e va **disabilitata,
   non distrutta**, perché ha a bordo una popolazione civile. Il ramo del fallimento (unità 8) è l'unico in cui compare
   «distruggere», e il `check.py` lo verifica: `[u for u in cov if 'distrugger' in ...] == [8]`.

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **«Completo» significa
completo in staging.**
