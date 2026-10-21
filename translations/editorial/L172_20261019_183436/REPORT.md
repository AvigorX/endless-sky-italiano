# REPORT — L172 · `paradise world jobs.txt` (sesto lotto: soccorso a Martini)

## 1. Contenuto

Sei missioni di soccorso, generate dallo stesso stampo: cure mediche (due varianti identiche), materiali per la
ricostruzione, cibo, pastiglie per purificare l'acqua, ritardante antincendio. Tutte richiedono di **contattare via radio
il controllore dello spazioporto**.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `disaster relief` | **soccorso** (nel `VALUE`, lasciato in inglese) | 1, 3 |
| `treat the wounded` | **curare i feriti** | 2, 4 |
| `reconstruction efforts` | **sforzi di ricostruzione** | 6 |
| `keep up supply` | **mantenere le scorte** | 8, 10, 12 |
| `hail the spaceport controller` | **chiamare via radio il controllore dello spazioporto** | 2-12 |
| `gain clearance to the planet` | **ottenere il permesso di scendere sul pianeta** | 2-12 |

## 3. Difficoltà

1. **Monotonia**: sei testi quasi uguali. Il rischio non è sbagliare una parola, è **divergere** nella coda comune. Un
   controllo isola la parte dopo «Dovrai» e pretende che sia **una sola stringa** in tutte e sei le `DESCRIPTION`.
2. **Tre varianti di scopo** (feriti / ricostruzione / scorte) che non vanno mai intercambiate: verificate in positivo e
   in negativo.
3. **Ripetizioni**: 1 = 3, 2 = 4, 8 = 10 = 12. Resa identica pretesa, e **8 testi distinti** contati.
4. **Solo 3 simboli**: `<cargo>`, `<planet>`, `<payment>`, 6 volte ciascuno. Nessun segnaposto composto.
5. **Confine misurato**: riga 1356 = **`VALUE`**.
6. **Gate**: 1,00–1,29, media **1,13** — l'italiano è più lungo perché la coda «chiamare via radio il controllore dello
   spazioporto» è più esplicita dell'inglese `hail the spaceport controller`.

## 4. Numeri osservati

```
unita' 12 · 6 VALUE · 6 DESCRIPTION · tutte PENDING
token 18 su 3 simboli · 0 tab · 0 virgolette · 0 apici
8 testi distinti · 6 contesti · righe 1230/1336
parole 217 -> 247 (1.138) · rapporto 1.00 - 1.29, media 1.13
FAIL totale: 0 (25 controlli) · verify exit 0 (20 controlli) · sha256[:16] ef8c776e39355c03
```

## 5. Stato del progetto (dopo L172)

```
TOTALE staging: 28121 unità · 885321 EN · 842089 IT
paradise world jobs.txt: 125/131 (95,4%) · 6 lotti — restano 6 unità, si chiude in L173
residuo traducibile (formula state.py): 3809
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (20 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Sesto lotto del file**: resta **L173**, che chiude `paradise world jobs.txt` (`HANDOFF_L173_20261019.md`).
