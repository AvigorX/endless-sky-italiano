# REPORT — L188 · `gegno outfits.txt`

## 1. Contenuto

Il lotto delle **armi e delle trivelle**: artiglieria plasma degli Scin, due sistemi di scavo, la torcia ionica e la mazza da duello dei Vi.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| artiglieria Scin | 1-6 | 739-886 | `Acuit Artillery`, `Acumen Bolt Cannon`, `Guile Pulse Laser` |
| trivelle | 7-9 | 886-933 | `Excavator` (macina) e `Burrower` (scava con cura) |
| torcia ionica | 10-12 | 949-987 | l'`Ion Torch`, che può anche servire da propulsore inverso |
| mazza da duello | 13 | 1012 | la `Savagery Bludgeon` delle navi `Dunite` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| counter to the Gegno Vi's huge cannon weaponry | **contraltare ai grandi cannoni dei Gegno Vi** | 2 |
| outrange most weapons in Gegno space | **superano in gittata la maggior parte delle armi dello spazio Gegno** | 2 |
| proof-of-concept neutron cannon | **cannone a neutroni sperimentale** | 3 |
| concentrated pulses of energy | **impulsi concentrati di energia** | 5 |
| rip materials out of asteroids | **estrarre materiali dagli asteroidi** | 7 |
| self-sustaining drill spars | **aste di trivellazione autosufficienti** | 8 |
| akin to a heated blade | **simile a una lama arroventata** | 11 |
| a makeshift reverse thruster | **propulsore inverso di fortuna** | 11 |

## 3. Difficoltà

1. **Due unità hanno lo stesso testo inglese** (idx 9 e idx 12, «This mining outfit requires a drill spar port…»): la resa deve essere **identica**, e il `check.py` confronta le due stringhe invece di fidarsi.
2. **4 tab** (idx 4, 6, 9, 12): il controllore li verifica in inglese **e** in italiano con `chr(9)`, dopo che un errore di escaping nel template li aveva fatti fallire per due giri.
3. **9 apici italiani** contro **3** inglesi: `dell'Acumen`, `quest'arma`, `un'arma`, `un'infrastruttura`… — nessuna corrispondenza fra le lingue.

## 4. Numeri osservati

```
unita' 13 · 11 DESCRIPTION · 2 VALUE · tutte PENDING
token 0 · 4 tab · 0 virgolette · 3 apici EN · 9 apici IT
12 testi distinti · 7 contesti · righe 739/1012
parole 492 -> 539 · rapporto 1.0 - 1.39, media 1.15
FAIL totale: 0 (25 controlli) · verify exit 0 (21 controlli) · sha256[:16] 887699ce0243bf5f
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (21 controlli) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
