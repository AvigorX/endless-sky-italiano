# REPORT — L142 · `unfettered 0 prologue.txt` (la vendita del motore di salto)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'inizio | 1–2 | 139–140 | `VALUE` `More Jump Drives`, la promessa di ricompense |
| l'offerta | 3–6 | 152–157 | la folla, le due scelte, «Un milione di crediti e l'amicizia» |
| le domande | 7–11 | 159–166 | accetto / di più / come parto senza motore; l'iperpropulsore e l'Anomalocaris |
| il rifiuto | 12–14 | 170–176 | accetto l'offerta / il rifiuto paziente / «La nostra offerta resta valida» |
| l'insistenza | 15 | 180 | «Non sottovalutare il valore della nostra amicizia» |
| le varianti | 16–18 | 182–190 | con iperpropulsore / senza / di nuovo il rifiuto |
| lo scambio | 19–20 | 198–201 | motore rimosso e sostituito / motore solo prelevato |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `More Jump Drives` | **identico** | `VALUE`: nome della missione |
| `One million credits` | **Un milione di crediti** | |
| `the friendship of the true Hai people` | **l'amicizia del vero popolo Hai** | |
| `hyperdrive` | **iperpropulsore** | glossario |
| `jump drive` | **motore di salto** | eccezione dichiarata |
| `in working condition` | **in condizioni di funzionare** | |
| `under threat of violence` | **sotto minaccia di violenza** | |
| `may fortune favor you, human friend` | **che la fortuna ti assista, amico umano** | |
| `our offer stands` | **la nostra offerta resta valida** | |
| `(No.)` | **`(No.)`** | identico: `ID_OK` |

## 3. Difficoltà

1. **Un `VALUE` a metà file** (riga 139): nel lotto è l'unità 1, nel file la 139; il controllo si scrive sull'indice del
   lotto, la verifica sul file.
2. **Il rifiuto in due punti** (13 e 18): costante unica, verificata con `count`.
3. **`(No.)` identico**: dichiarato in `ID_OK` con controllo proprio — non escluso dai controlli.
4. **La missione si chiude**: 20/20, e il confine alla riga 214 è un cambio di missione.
5. **Un errore di misura mio**: «81 dopo la riga 201» invece di **82** (147 − 45 − 20). Il `verify.py` l'ha bocciato;
   corretto in `verify.py` e nell'handoff.
6. **Un errore di asserzione mio**: `(No.)` ha un tab davanti, quindi `txt == eng` falliva; corretto confrontando
   `txt` con `eng` (entrambi con tab) e `txt.lstrip('\t')` con `'(No.)'`. La traduzione non è stata toccata.
7. **Gate**: minimo 0,74, massimo 1,24, media 1,02.

## 4. Numeri osservati

```
unita' 20/20 · MISSION_TEXT 18 · VALUE 1 · DESCRIPTION 1 · UI_LABEL 0 · token 0 · tutte PENDING
contesto 1, chiuso: 20/20 · 19 testi distinti · rifiuto x2 · (No.) in ID_OK
tab 17 unita · virgolette 38 (quattro unita con 4), nessuna dispari · quadre 0
parole EN 493 -> IT 456 (0.925) · rapporto 0.74 - 1.24, media 1.02
righe 139/201 · 45 prima / 82 dopo · confine riga 214 (cambio di missione)
FAIL totale: 0 (29 controlli) · verify exit 0 (26 controlli)
sha256[:16] 1e2c9c50567e62e1
```

## 5. Stato del progetto

```
TOTALE staging: 27564 unità · 870338 EN · 826967 IT
unfettered 0 prologue.txt: 65/147 (44,2%) · 3 lotti · 1489 EN -> 1397 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4366
residuo misurato: 5033 unità / 106761 parole su 117 file
avanzamento: 27564/32924 unità (83,7%) · 870338/979975 parole (88,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (26 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna partita avviata**: la trattativa non è stata giocata.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 44,2%**: restano **82 unità** su due missioni.
- **Prossimo lotto**: `HANDOFF_L143_20261019.md` — righe **214–317**, **30 unità**, 723 parole, **2 contesti completi**
  (`Unfettered Jump Drive 2` 12, `Unfettered Jump Drive 3` 18), **26 unità con tab**, **46 virgolette**, e le due scelte
  `(No.)` / `(Yes.)` ripetute.
