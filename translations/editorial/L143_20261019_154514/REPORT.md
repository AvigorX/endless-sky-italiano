# REPORT — L143 · `unfettered 0 prologue.txt` (il secondo e il terzo motore, e il segreto dei mondi perduti)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'offerta | 1–8 | 214–236 | `VALUE`, la promessa di informazioni, la folla, le due scelte, l'offerta di un milione e del ruolo di emissario |
| lo scambio | 9–12 | 243–248 | iperpropulsore al posto del motore, le bacheche dei lavori, «Non ancora» |
| la seconda vendita | 13–18 | 270–278 | l'altro motore, le due scelte, i capi locali, le due domande |
| il segreto | 19 | 282 | i mondi ai margini della galassia, fertili e quasi disabitati |
| le domande | 20–24 | 288–298 | come aiutare, «quasi disabitati?», i Wanderer, la guerra |
| la risposta | 25–26 | 302–304 | «Il tuo aiuto potrebbe esserci utile», «Non vedo l'ora» |
| lo sciacallo | 27–29 | 306–310 | i divoratori di carogne, le città fuse, «quei mondi sono nostri di diritto» |
| l'ultimo ordine | 30 | 317 | «visita la bacheca dei lavori», i guerrieri pronti |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `More Jump Drives` | **identico** | `VALUE`, ricompare da L142 |
| `another million credits` | **un altro milione di crediti** | |
| `emissaries to collect the payments` | **emissari per raccogliere i pagamenti** | |
| `our frail brothers` | **i nostri fragili fratelli** | i «fratelli» pacificati dai Drak |
| `job boards` | **bacheche dei lavori** | |
| `galactic fringe` | **margini della galassia** | |
| `nearly uninhabited` | **quasi disabitati** | |
| `scavengers` · `carrion-feeders` | **sciacalli** · **divoratori di carogne** | |
| `melting down our cities` | **fondendo le nostre città** | |
| `by right` | **di diritto** | |

## 3. Difficoltà

1. **Due missioni in un lotto**: entrambe si chiudono (12/12 e 18/18), e il `verify.py` verifica **due** chiusure.
2. **Il `VALUE` ricompare** identico a L142: si verifica qui, non si presume.
3. **`(No.)` identico ×2** in `ID_OK` e **`(Yes.)` tradotto ×2** con la stessa resa: due controlli distinti.
4. **26 unità con tab su 30** (senza: `VALUE`, `DESCRIPTION`, il testo d'apertura e quello della seconda vendita).
5. **46 virgolette**, tre unità con quattro.
6. **Il lessico degli Slegati** resta solenne e sprezzante insieme: «divoratori di carogne», «nostri di diritto».
7. **Gate**: minimo 0,72, massimo 1,12, media 0,96.

## 4. Numeri osservati

```
unita' 30/30 · MISSION_TEXT 28 · VALUE 1 · DESCRIPTION 1 · UI_LABEL 0 · token 0 · tutte PENDING
contesti 2, chiusi: 12/12 e 18/18 · 28 testi distinti · (No.) x2 identico · (Si.) x2
tab 26 unita · virgolette 46 (tre unita con 4), nessuna dispari · quadre 0
parole EN 723 -> IT 643 (0.889) · rapporto 0.72 - 1.12, media 0.96
righe 214/317 · 65 prima / 52 dopo · confine riga 367 (cambio di missione)
FAIL totale: 0 (30 controlli) · verify exit 0 (25 controlli)
sha256[:16] a6fdd67b2067eb90
```

## 5. Stato del progetto

```
TOTALE staging: 27594 unità · 871061 EN · 827610 IT
unfettered 0 prologue.txt: 95/147 (64,6%) · 4 lotti · 2212 EN -> 2040 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4336
residuo misurato: 5003 unità / 106038 parole su 117 file
avanzamento: 27594/32924 unità (83,8%) · 871061/979975 parole (88,9%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 30 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna partita avviata**: le due vendite non sono state giocate.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 64,6%**: restano **52 unità**, tutte in `Unfettered Jump Drive Trading`.
- **Prossimo lotto**: `HANDOFF_L144_20261019.md` — righe **367–420**, **20 unità**, 486 parole, **20 `MISSION_TEXT`**,
  **19 unità con tab**, **12 virgolette**, e **i primi due token** del file (`<hood>`, `<learned>`).
