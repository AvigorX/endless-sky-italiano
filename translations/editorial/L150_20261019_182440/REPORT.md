# REPORT — L150 · `coalition jobs.txt` (turisti e corriere)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| turisti in partenza | 1–7 | 639–714 | tre livelli `Vacationers to <planet>` e il `TEXT` del rientro a casa |
| turisti in rientro | 8–13 | 719–770 | tre livelli con «home», resa distinta |
| corriere veloce | 14 | 794 | il `TEXT` con `<commodity>` |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Vacationers to <planet>` | **identico** | `VALUE`, sei volte |
| `bring them to <destination>` | **portarli a `<destination>`** | |
| `bring them home to <destination>` | **riportarli a casa a `<destination>`** | due parole in più, resa diversa |
| `travel in a very comfortable ship` | **viaggiare su una nave molto confortevole** | |
| `Payment is void if they do not arrive by <date>` | **Il compenso decade se non arrivano entro il `<date>`** | |
| `The recipient thanks you … so quickly` | **Il destinatario ti ringrazia … così in fretta** | |

## 3. Difficoltà

1. **Famiglie quasi identiche**: `Tourists Out` e `Tourists Home` divergono per «home»; la resa le distingue, e il
   `verify.py` confronta le due stringhe per asserire che siano **diverse**.
2. **`<commodity>` una volta su 33**: isolato da un controllo dedicato.
3. **Lotto piccolo** (14 unità, 234 parole): chiuso in un passaggio, nessun taglio a metà coppia.
4. **Gate**: 1,00–1,10 — il lotto più «vicino» all'inglese finora, perché il testo è formulaico.

## 4. Numeri osservati

```
unita' 14/14 · VALUE 6 · DESCRIPTION 6 · TEXT 2 · token 33 su 6 simboli · tutte PENDING
<commodity> = 1, nell'unita 14 · 8 contesti · 5 testi distinti
tab 0 · virgolette 0 · parole 234 -> 216 (0.923) · rapporto 1.00 - 1.10
righe 639/794 · 64 prima / 119 dopo · confine riga 799 (Fast Courier 1)
FAIL totale: 0 (27 controlli) · verify exit 0 (24 controlli) · sha256[:16] 160a1592a36efff5
```

## 5. Stato del progetto (dopo L150)

```
TOTALE staging: 27724 unità · 874028 EN · 830340 IT
coalition jobs.txt: 78/197 (39,6%) · 4 lotti
residuo misurato: 4875 unità / 103071 parole su 116 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (24 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessuna partita avviata**.
- **Lotto eseguito in batch**: il contratto è il piano del batch (L150 era già descritto da `HANDOFF_L150_20261019.md`).
- **Prossimo**: L151 continua dalla riga 799 (corriere veloce, cargo, trasporti).
