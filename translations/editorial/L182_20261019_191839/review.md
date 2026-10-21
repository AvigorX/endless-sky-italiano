# REVIEW — L182 · `human outfits.txt` (scanner, espansioni, celle)

Coppie EN→IT rilette in `translation.json` (`227c7d7ef6b392c9…`). Tutte le 14 unità sono **`PENDING`**.

## 1. Voce

Il lotto più **variabile** del file finora: quattro schede tecniche quasi identiche (gli scanner), **una battuta** (`Cloaking
Device`), due schede da «fai da te» (le cuccette: il letto dietro il generatore, le amache ai motori) e una chiusa
**cupa** (la `Brig`: criminali, prigionieri, commercio di schiavi). La traduzione non appiattisce le quattro voci.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `taking of target` | **prendendo di mira** | 3, 4 |
| `willing to risk flying close enough to get a reading` | **disposto a rischiare di volarle abbastanza vicino da ottenere una lettura** | 4 |
| `valuable materials` | **materiali pregiati** | 5 |
| `fuel, energy, heat, and crew complement` | **carburante, energia, calore e numero di membri dell'equipaggio** | 6 |
| `the outputs are fairly standard` | **le uscite sono piuttosto standard** | 7 |
| `sacrifice some cargo space` | **sacrificare un po' di spazio cargo** | 9 |
| `in such a fundamental way` | **in modo così radicale** | 10 |
| `usually reserved for outfits` | **di solito riservata agli equipaggiamenti** | 12 |
| `makeshift way` | **come ripiego** | 13 |
| `highly illegal galactic slave trade` | **commercio interstellare di schiavi, che è altamente illegale** | 14 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Jump Drives (Broken)` è un `VALUE`**: si copia alla lettera, **parentesi comprese**, e il plurale resta plurale.
2. **`Republic` → «Repubblica»** e `Navy` → «Marina»: già fissati nei lotti precedenti.
3. **`Cloaking Device` è l'eccezione**: reso in prosa perché la frase è una battuta. Il nome dell'oggetto resta nel contesto
   (`outfit:Cloaking Device`), che non si traduce.
4. **Gli apici non si trasferiscono**: 6 inglesi → 0 (possessivi resi con «di + articolo»); 9 italiani → tutti da elisione e
   dal troncamento `po'`. Un controllo futuro che pretendesse «stesso numero di apici» sarebbe **sbagliato**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 14 unità `PENDING`.
- **Nessun equipaggiamento visto a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Terzo lotto del file**: 28 unità ancora da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (20 controlli) |
