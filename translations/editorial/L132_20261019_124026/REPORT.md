# REPORT — L132 · `unfettered side missions.txt` (il disertore Hai e l'Anomalocaris)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `Unfettered returning home` — il portello | 1–5 | 17–33 | la `DESCRIPTION`, i graffi notturni, la torcia, il giovane con la sacca |
| la scritta nel tributo | 6–9 | 34–39 | l'involucro di carta stagnola, l'alfabeto spigoloso degli Hai, il dubbio |
| le due risposte | 10–18 | 41–63 | «non posso fare nulla», «vieni con me», il rifiuto, la cabina, Hai-home |
| `Hai Legacy 1` — il cantiere | 19–27 | 88–105 | i tre «sì / un'altra volta / mai», la figura incappucciata, la proposta, i dieci milioni |
| il viaggio | 28–33 | 108–116 | il biglietto del treno, la stazione sotterranea, la camminata fino alla spiaggia |
| le due figure | 34–42 | 117–130 | i cappucci, «come mi conosci?», gli scontri con gli Unfettered |
| la nave che emerge | 43–54 | 133–152 | il ruggito, le armi puntate, «se avesse voluto ucciderti saresti già morto» |
| la grotta e l'Anomalocaris | 59–63 | 160–166 | i cristalli, la seconda nave, i dieci milioni, le armi dei Korath |
| le quattro strade e gli esiti | 64–83 | 169–222 | accettare, l'equipaggio, la nave nascosta, il rifiuto, le tre varianti di sparo |
| il diario | 84 | 229 | il prestito al posto dell'acquisto |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `smuggle him out` | **farlo uscire di nascosto** | |
| `main hatch` | **portello principale** | |
| `juvenile Hai` | **giovane Hai** | |
| `foil paper` · `wrapper` | **carta stagnola** · **involucro** | |
| `food rations` · `tribute` | **razioni alimentari** · **tributo** | |
| `angular alphabet` | **alfabeto spigoloso** | |
| `defector` | **disertore** | |
| `bunk rooms` | **cabine** | |
| `escorts` | **scorte** | |
| `hooded figure` | **figura incappucciata** | ripetuto 4 volte |
| `lucrative business proposition` | **lucrosa proposta d'affari** | |
| `solitary affair` | **faccenda solitaria** | |
| `Anomalocaris` | **Anomalocaris** | nome della nave-classe |
| `relic of the past` | **relitto del passato** | |
| `the savage Korath` | **i selvaggi Korath** | |
| `your brethren, the Unfettered Hai` | **i nostri fratelli, gli Hai Unfettered** | |
| `geyser of sand` | **geyser di sabbia** | |
| `with the aid of the autopilot` | **con l'aiuto del pilota automatico** | |
| `a loan was issued in lieu of a conventional purchase` | **è stato emesso un prestito al posto di un acquisto convenzionale** | `LOGBOOK` |

## 3. Difficoltà

1. **89 virgolette**: il numero più alto finora, con **tre unità a una sola** (57, 62, 73): la distribuzione
   (43 / 33 / 5 / 3) è misurata e asserita.
2. **`Hai-home` è un nome proprio**: tradurlo come «casa degli Hai» avrebbe rotto il riferimento al pianeta. Il
   controllo verifica che resti «Hai-home» e che la forma tradotta **non** compaia.
3. **Virgolette annidate**: il messaggio dentro l'involucro usa **virgolette singole** dentro la battuta
   (`"Dice: 'Hai-home è casa tua…'"`), come il sorgente.
4. **Una resa identica dichiarata**: `(No.)` → `(No.)`. Senza `ID_OK` il controllo «tutte tradotte» la boccerebbe.
5. **3 `UI_LABEL`** e **zero `VALUE`**: due controlli di natura diversa, il secondo è un'asserzione vuota scritta.
6. **8 token in 4 famiglie** con `<last>` quattro volte; sequenza verificata per unità.
7. **74 tab su 84**: quasi tutti i testi sono battute o opzioni indentate.
8. **Gate**: minimo 0,58 (unità 3, «(Sì.)»), massimo 1,53 (unità 28, «Ci andrai?»).

## 4. Numeri osservati

```
unita' 84/84 · MISSION_TEXT 78 · UI_LABEL 3 (identiche) · DESCRIPTION 1 · DIALOG 1 · LOGBOOK 1 · VALUE 0
contesti 2 (18/66) · testi distinti 82 · tutte PENDING
tab 74 unita · virgolette 89 (43/33/5/3) · token 8 in 4 famiglie · quadre 0
parole EN 2055 -> IT 1850 (0.900) · rapporto 0.58 - 1.53, media 1.01
righe 17/229 · file 84/159 (52,8%) · 0 prima / 75 dopo · confine riga 237
FAIL totale: 0 (30 controlli) · verify exit 0 (32 controlli)
sha256[:16] 4fcdf80f4d1d3888
```

## 5. Stato del progetto

```
TOTALE staging: 27311 unità · 862250 EN · 819332 IT
unfettered side missions.txt: 84/159 (52,8%) · 1 lotto · 2055 EN -> 1850 IT
file completi: quarantasette · residuo traducibile (formula state.py): 4608
residuo misurato: 5281 unità / 114837 parole su 119 file
avanzamento: 27311/32924 unità (83,0%) · 862250/979975 parole (88,0%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (32 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 84 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: restano **75 unità** (righe 237–510).
- **Prossimo lotto**: `HANDOFF_L133_20261019.md` — righe **237–477**: **67 unità**, **2.007 parole**, **2 contesti**,
  **2 `VALUE`**, **2 `UI_LABEL`**, **9 `DIALOG`**, **98 virgolette**, **8 token in 6 famiglie**.
