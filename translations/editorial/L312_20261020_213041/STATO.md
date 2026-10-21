# STATO — L312 (`data/bunrodea/bunrodea outfits.txt`, righe 135–236)

**Stato: CHIUSO.** Secondo lotto del file: **24 unità su 33** (**72,7%**). `check.py` esce 0 con **25 controlli**; `verify.py` esce
0 con **23 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L312_20261020_213041/` |
| file | `data/bunrodea/bunrodea outfits.txt` (33 unità · 1.252 parole · righe 25–402) |
| righe | 135–236 |
| unità | **12** — **1 `VALUE` + 11 `DESCRIPTION`** |
| contesti | **7** — da `Solar Battery` a `Dark Reactor` |
| parole | **445 EN → 433 IT** (0,973) |
| rapporto | **0,98 – 1,20** |
| tab | **4** — 160, 204, 220, 236 |
| virgolette | **2** — **una coppia sola**, riga **235** (`"dark star"`) |
| segnaposto / alternative | **0 / 0** |
| apici | **1 EN / 12 IT** |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **12 prima** (L311) · 12 qui · **9 dopo la 236** (la prossima alla 250) |
| copertura | **24/33 (72,7%)** — **stampata, non asserita** |
| `sha256[:16]` | **`af2956256bea6c7a`** |

## Comandi

```bash
python staging/editorial/L312_20261020_213041/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L312_20261020_213041/verify.py    # FAIL: 0 (23 controlli, 24/33)
```

## Com'è fatto il lotto

| righe | contesto | che cosa |
|---|---|---|
| 135–160 | `Solar Battery`, `Solar Cell` | **batterie e celle solari**: le celle vanno montate sulla **piattaforma** della batteria (tab 160) |
| 175–188 | `Reactor Overclocker`, `Reactor Limiter` | **due componenti opposti**, stesso incipit, seconda frase invertita |
| 203–236 | `Quark`, `Electroweak`, `Dark Reactor` | **tre reattori** intitolati a **stelle esotiche**, ognuno con la **nota degli upgrade** (tab 204, 220, 236) |

## La famiglia delle note: qui è **tutta identica**

```
204 == 220 == 236     in inglese (tutte chiudono con `though.`)
204 == 220 == 236     in italiano (tutte chiudono con «però.»)
```

L'**opposto** di L311, dove 114 e 130 divergevano (`though.` / `however.`). Il test verifica l'uguaglianza **su tre lati**, in
entrambe le lingue: se una delle tre note fosse stata resa diversamente, il controllo fallirebbe.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| `VALUE` | `Solar Batteries` **copiato per identità** |
| famiglia | 204 = 220 = 236 **in italiano e in inglese**; tutte chiudono con «però.» |
| tab | righe esatte `[160, 204, 220, 236]` |
| virgolette | **una coppia** nella **sola** riga 235 |
| componenti | prima frase **identica** a meno del nome, seconda frase **opposta** |
| scienza | `Polaris`, `XXVIII secolo`, `materia di quark`, `elettrodebole`, `leptoni`, `nucleazione` |
| vuote | 0 segnaposto, 0 alternative |
| segmento | 12 prima · 12 qui · **9 dopo** |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **Il file non è finito**: mancano
**9 unità / 327 parole** (righe 250–402), che chiudono il file in **L313**.
