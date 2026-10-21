# REPORT — L140 · `data/hai/unfettered 0 prologue.txt` (il primo contatto con gli Slegati)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'approccio | 1–3 | 22–26 | il pianeta degli «scoiattoli giganti», la domanda, due scelte |
| il primo dialogo | 4–7 | 30–36 | «la scimmia è curiosa», le tre domande del giocatore |
| il secondo approccio | 8–10 | 40–43 | gli Hai in guerra fra loro, le stesse due scelte |
| il secondo dialogo | 11–14 | 45–51 | «molti dei tuoi simili a sud», «veri Hai», la guerra |
| la rivelazione | 15–17 | 55–63 | «gli inalterati», «gli Hai conquistatori», il motto |
| l'estinzione | 18–23 | 67–75 | «Combattiamo per difenderci dall'estinzione», le due varianti della stessa risposta |
| le domande | 24–25 | 80–81 | il territorio, «gli Hai sono stati alterati» |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `giant, intelligent squirrels` | **scoiattoli giganti e intelligenti** | |
| `the monkey is curious` | **la scimmia è curiosa** | `monkey` → scimmia, come nei file già chiusi |
| `a true Hai` | **un vero Hai** | |
| `'true Hai'` | **'veri Hai'** | virgolette singole interne, riprodotte |
| `They hiss` | **Sibila** | |
| `the unaltered` | **gli inalterati** | |
| `Hai the conquerors` | **gli Hai conquistatori** | |
| `masters of a hundred worlds` | **padroni di cento mondi** | |
| `before human monkeys had learned the use of thumbs` | **quando le scimmie umane non avevano ancora imparato a usare i pollici** | |
| `We fight to defend ourselves from extinction` | **Combattiamo per difenderci dall'estinzione** | |
| `your brethren` | **i tuoi simili** | |
| `Although despite their hostility` | **Sebbene, nonostante** la loro ostilità | sgrammaticatura riprodotta |

## 3. Difficoltà

1. **File nuovo, missione nuova**: tutte e 25 le unità sono `MISSION_TEXT`, in un contesto solo.
2. **Due rami paralleli**: le scelte e due battute si ripetono (unità 2/9, 3/10, 6/13, 18/21) e devono avere **la stessa
   resa**, altrimenti i due percorsi divergono.
3. **Il motto cinque volte** (15, 16, 17, 20, 23): costante unica, verificata per occorrenza.
4. **`monkey` è un insulto**: reso «scimmia», non addolcito.
5. **Le virgolette singole interne** (`'true Hai'`) fanno parte della battuta: il conteggio delle doppie resta 2.
6. **50 virgolette**, sei unità con quattro: distribuzione verificata per unità.
7. **Sgrammaticatura del sorgente** (`Although despite`): riprodotta come «Sebbene, nonostante».
8. **Un errore mio nel controllo**: la verifica sulle due scelte ripetute confrontava `'\t(Certo.)'` con `'(Certo.)'`;
   corretto con `.lstrip('\t')`. La traduzione non è stata toccata.

## 4. Numeri osservati

```
unita' 25/25 · MISSION_TEXT 25 · VALUE 0 · UI_LABEL 0 · token 0 · tutte PENDING
contesto 1 · 21 testi distinti (4 coppie ripetute) · motto x5
tab 23 unita (senza tab: 1 e 8) · virgolette 50 (sei unita con 4), nessuna dispari · quadre 0
parole EN 405 -> IT 375 (0.926) · rapporto 0.76 - 1.29, media 1.05
righe 22/81 · 0 prima / 122 dopo · confine riga 83 (stessa missione)
FAIL totale: 0 (31 controlli) · verify exit 0 (25 controlli)
sha256[:16] ed2e17388b122b8f
```

## 5. Stato del progetto

```
TOTALE staging: 27524 unità · 869254 EN · 825945 IT
unfettered 0 prologue.txt: 25/147 (17,0%) · 1 lotto · 405 EN -> 375 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4406
residuo misurato: 5073 unità / 107845 parole su 117 file
avanzamento: 27524/32924 unità (83,6%) · 869254/979975 parole (88,7%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna partita avviata**: il primo contatto non è stato visto a schermo.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 17,0%**: restano **122 unità** su quattro contesti.
- **Prossimo lotto**: `HANDOFF_L141_20261019.md` — righe **83–132**, **20 unità**, 591 parole, **1 contesto completo**
  (`First Contact: Unfettered`, che si chiude), **18 `MISSION_TEXT`** e **2 `LOGBOOK`**, **18 unità con tab**, **58
  virgolette**.
