# REPORT — L151 · `coalition jobs.txt` (corriere, carichi, medici, allievi)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| corriere veloce | 1–7 | 799–868 | tre livelli `Fast courier to <planet>` e il `TEXT` con `<commodity>` |
| carichi | 8–15 | 873–940 | quattro livelli `Cargo to <planet>` |
| carichi pesanti | 16–23 | 962–1029 | quattro livelli `Bulk cargo to <planet>`, stessa descrizione |
| consegne urgenti | 24–29 | 1051–1098 | tre livelli `Rush Delivery to <planet>` |
| medici | 30–33 | 1121–1139 | `Doctors to <planet>`, la descrizione dell'epidemia e il `DIALOG` |
| allievi | 34–37 | 1144–1171 | il `TEXT` degli allievi e due livelli `Cadets to <planet>` |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Fast courier to <planet>` · `Cargo to <planet>` · `Bulk cargo to <planet>` · `Rush Delivery to <planet>` | **identici** | `VALUE` |
| `Deliver <cargo> to <destination> by <date>. The payment is <payment>.` | **Consegna `<cargo>` a `<destination>` entro il `<date>`. Il compenso è `<payment>`.** | 3 copie |
| `Deliver <cargo> to <destination>. Payment is <payment>.` | **Consegna `<cargo>` a `<destination>`. Il compenso è `<payment>`.** | **8 copie**, una resa |
| `<destination> needs a shipment of <cargo> by <date>` | **`<destination>` ha bisogno di una partita di `<cargo>` entro il `<date>`** | 3 copie |
| `to address a viral outbreak` | **per fronteggiare un'epidemia virale** | |
| `From their lack of urgency, it appears…` | **Dalla loro mancanza di fretta sembra che…** | `DIALOG` |
| `the Academy on <destination>` | **l'Accademia su `<destination>`** | |
| `new recruits` | **reclute** | mentre `cadets` = **allievi** |

## 3. Difficoltà

1. **37 unità, 14 testi**: la mappa per stringa è l'unico modo per non far divergere le 8 copie di Cargo/Bulk.
2. **`<cargo>` contro `<commodity>`**: il primo è il carico della missione (14 volte), il secondo la merce del `TEXT`
   (una volta); la parità distingue i due.
3. **Un controllo sbagliato corretto in corsa**: «corriere» non è nel testo tradotto (è nel `VALUE` inglese), quindi il
   `check.py` ora **verifica l'assenza**.
4. **`cadets` e `recruits`** nello stesso lotto: «allievi» e «reclute», non lo stesso termine.
5. **Gate**: 0,90–1,20.

## 4. Numeri osservati

```
unita' 37/37 · VALUE 17 · DESCRIPTION 17 · TEXT 2 · DIALOG 1 · token 81 su 7 simboli · tutte PENDING
14 stringhe distinte · le 8 copie di Cargo/Bulk hanno UNA resa · 19 contesti
tab 0 · virgolette 0 · parole 302 -> 316 (1.046) · rapporto 0.90 - 1.20
righe 799/1171 · 78 prima / 82 dopo · confine riga 1191 (TEXT)
FAIL totale: 0 (27 controlli) · verify exit 0 (24 controlli) · sha256[:16] 8faf5d133a5b433c
```

## 5. Stato del progetto (dopo L151)

```
TOTALE staging: 27761 unità · 874330 EN · 830656 IT
coalition jobs.txt: 115/197 (58,4%) · 5 lotti
residuo misurato: 4838 unità / 102769 parole su 116 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (24 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 37 unità `PENDING`.
- **Nessun lavoro completato nel gioco**; il `DIALOG` dei medici non è stato visto.
- **Eseguito in batch**: contratto = piano del batch, nessun `HANDOFF_L151` separato (dichiarato qui).
- **Prossimo**: L152 dalla riga 1191 (`MISSION_TEXT` e `LOGBOOK`).
