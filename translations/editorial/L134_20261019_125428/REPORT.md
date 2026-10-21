# REPORT — L134 · `unfettered side missions.txt` (la coda: la folla, la consegna, la Lightning Bug)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'accusa | 1–2 | 494–495 | la folla armata, «non meriti di pilotare questo relitto», l'occasione sprecata |
| la richiesta | 3 | 498 | l'Unfettered importante, la consegna immediata, lo scambio con un'altra nave |
| le due scelte | 4–5 | 500–501 | consegnare / rifiutare |
| la consegna | 6 | 503 | l'uscita dall'equipaggio, la milizia informata, il capo che parla |
| la proposta | 7 | 504 | «portarci un Jump Drive… o due», il favore da guadagnare |
| l'accompagnamento | 8 | 510 | il bordo dello spazioporto, la frustrazione trattenuta, la `Lightning Bug` |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `relic of old` | **relitto del passato** | coerente con L132/L133 |
| `glorious battle` | **battaglia gloriosa** | |
| `You must surrender the ship to us immediately` | **Devi consegnarci immediatamente la nave** | |
| `the weapons of the savages` | **le armi dei selvaggi** | i Korath |
| `a suitable replacement` | **un sostituto adeguato** | |
| `the local Unfettered militia` | **la milizia locale degli Unfettered** | |
| `blatantly forced casualness` | **una disinvoltura palesemente forzata** | |
| `Jump Drive` | **Jump Drive** | nome del modulo: resta inglese |
| `messy paperwork` | **qualche pratica pasticciata** | |
| `Lightning Bug` | **Lightning Bug** | modello di nave: resta inglese |

## 3. Difficoltà

1. **Il lotto chiude il file**: `verify.py` con **invariante di file** (84 + 67 + 8 = 159, sovrapposti 0,
   `max(line) = 510`).
2. **Tre asserzioni vuote**: `VALUE`, `UI_LABEL`, token. È il primo lotto con tutte e tre insieme.
3. **Il lotto più corto del file** (8 unità, 356 parole): un `check.py` copiato da L133 avrebbe 67 unità attese e
   fallirebbe su tutto.
4. **Un'unità con una sola virgoletta** (6): battuta non chiusa dal sorgente, riprodotta.
5. **La tipografia ha bocciato il mio primo giro**: avevo usato un **trattino lungo** in unità 6 («tranne uno —
   probabilmente il capo»), e il controllo lo rifiuta. Riscritto con una virgola: il gate non si allarga.
6. **Nomi di equipaggiamento**: `Jump Drive` e `Lightning Bug` restano in inglese, come `Anomalocaris`.
7. **Gate**: minimo 0,90 (unità 4, «(Consegna l'Anomalocaris.)»), massimo 1,15 (unità 3).

## 4. Numeri osservati

```
unita' 8/8 · MISSION_TEXT 8 · VALUE 0 · UI_LABEL 0 · token 0 · tutte PENDING
contesti 1 · testi distinti 8
tab 7 unita · virgolette 13 (unita 6 con 1) · quadre 0
parole EN 356 -> IT 323 (0.907) · rapporto 0.90 - 1.15, media 1.02
righe 494/510 · 151 prima / 0 dopo · FILE CHIUSO 159/159
FAIL totale: 0 (27 controlli) · verify exit 0 (32 controlli)
sha256[:16] 173cf3edac2a3208
```

## 5. Stato del progetto

```
TOTALE staging: 27386 unità · 864613 EN · 821476 IT
unfettered side missions.txt: 159/159 (100,0%) · 3 lotti · 4418 EN -> 3994 IT
file completi: quarantotto · residuo traducibile (formula state.py): 4544
residuo misurato: 5211 unità / 112486 parole su 118 file
avanzamento: 27386/32924 unità (83,2%) · 864613/979975 parole (88,2%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (32 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 8 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **`unfettered side missions.txt` è completo solo in staging**: 159 unità tradotte, zero caricate nel gioco.
- **Prossimo lotto**: `HANDOFF_L135_20261019.md` — file **nuovo**, `data/starts.txt`, righe **18–134** (**32 unità**,
  **1.485 parole**, **4 contesti completi**, **18 `CONVERSATION`**, **14 virgolette**, **zero token**).
