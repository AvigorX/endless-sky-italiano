# REPORT — L141 · `unfettered 0 prologue.txt` (la caduta degli Hai, e la richiesta del motore di salto)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| la storia | 1–5 | 83–92 | i mondi perduti, i popoli-drago, l'iperpropulsore, «Scimmia sciocca» e gli antenati ottusi |
| l'alterazione | 6–9 | 95–100 | «Come siete stati alterati?», la malattia dei Drak, le due domande |
| la gabbia | 10–11 | 104–108 | «la galassia sia uno zoo», la verità tramandata |
| le risposte | 12–13 | 113–115 | «È una storia spaventosa», «C'è qualcosa che posso fare?» |
| la richiesta | 14–18 | 118–127 | venderci un motore di salto, «Nessun essere umano lo conosce», «lasciaci in pace», «ti conteremo fra i nostri amici» |
| il diario | 19–20 | 131–132 | la voce riletta da L138 e la variante |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Once, many worlds beyond wormhole were ours` | **Una volta, molti mondi oltre il wormhole erano nostri** | `wormhole` resta, come nei file chiusi |
| `dragonfolk` | **popoli-drago** | parola degli Slegati per gli Sheragi |
| `banging rocks together` | **battere le pietre l'una contro l'altra** | |
| `like brackish water, like stunted tree` | **come acqua salmastra, come albero rinsecchito** | senza articoli: voce telegrafica |
| `Silly monkey` | **Scimmia sciocca** | |
| `their dumb ancestors` | **i loro antenati ottusi** | «antenati» è del sorgente, non un lapsus della resa |
| `quick fever, strange feeling of frailness` | **febbre rapida, strana sensazione di fragilità** | |
| `brittle bones with mouth full of dirt` | **ossa fragili con la bocca piena di terra** | |
| `the galaxy to be a zoo` | **la galassia sia uno zoo** | |
| `jump drive` | **motore di salto** | eccezione deliberata del glossario |
| `share of the plunder` | **una parte del bottino** | |

## 3. Difficoltà

1. **Un contesto che si chiude**: `First Contact: Unfettered` arriva a **45/45** (25 in L140, 20 qui) e il `verify.py`
   controlla che dopo la riga 132 la missione **cambi**.
2. **Voce telegrafica** da mantenere: frasi senza articoli, nessuna cortesia, sintassi spezzata. Un controllo verifica
   che il motto non sia stato «normalizzato».
3. **Una voce di diario identica a L138** (unità 19): riletta e confrontata, non ricopiata.
4. **Una variante della stessa voce** (unità 20): resa di nuovo, con lessico coerente e senza copiare.
5. **La frase sugli antenati ottusi** in due unità (3 e 5) con la stessa resa, verificata per stringa.
6. **58 virgolette** in 20 unità, nove unità da quattro.
7. **`jump drive` → motore di salto**: eccezione già fissata nel glossario editoriale, applicata qui per la prima volta
   in un dialogo lungo.

## 4. Numeri osservati

```
unita' 20/20 · MISSION_TEXT 18 · LOGBOOK 2 · VALUE 0 · UI_LABEL 0 · token 0 · tutte PENDING
contesto 1, chiuso: 45/45 · 19 testi propri + 1 riletto da L138 · 20 distinti
tab 18 unita · virgolette 58 (nove unita con 4), nessuna dispari · quadre 0
parole EN 591 -> IT 566 (0.958) · rapporto 0.80 - 1.21, media 1.05
righe 83/132 · 25 prima / 102 dopo · confine riga 139 (cambio di missione)
FAIL totale: 0 (30 controlli) · verify exit 0 (25 controlli)
sha256[:16] 2abdd856e427930b
```

## 5. Stato del progetto

```
TOTALE staging: 27544 unità · 869845 EN · 826511 IT
unfettered 0 prologue.txt: 45/147 (30,6%) · 2 lotti · 996 EN -> 941 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4386
residuo misurato: 5053 unità / 107254 parole su 117 file
avanzamento: 27544/32924 unità (83,7%) · 869845/979975 parole (88,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna partita avviata**: il dialogo con gli Slegati non è stato visto a schermo.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 30,6%**: restano **102 unità** su quattro missioni.
- **Prossimo lotto**: `HANDOFF_L142_20261019.md` — righe **139–201**, **20 unità**, 493 parole, **1 contesto completo**
  (`Unfettered Jump Drive 1`), **1 `VALUE`** (`More Jump Drives`), **1 `DESCRIPTION`**, 18 `MISSION_TEXT`, 17 unità con
  tab, **38 virgolette**.
