# REPORT — L145 · `unfettered 0 prologue.txt` (la loggia delle armi: la prova superata, il prototipo, il Blaster)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| la prova | 1–2 | 423–424 | il duello che non finisce, il colpo magistrale, Desneeparu si presenta (`<learned>`, `<last>`) |
| il diario | 3 | 427 | `LOGBOOK`: la guerriera che sa maneggiare una lama |
| il saluto | 4 | 428 | il pugno, «Spero che troverai l'arma che ti serve» |
| la loggia | 5 | 429 | `<The engineer>`, i prototipi, i collaudi a Firelode, la sezione avanzata |
| l'offerta | 6 | 430 | due `Tripulse Shredder` e la riconoscenza per un motore di salto |
| le domande | 7–10 | 433–444 | i Tripulse, il tripulse, l'arma ionica piccola, l'`Ion Cannon` su torretta |
| i rifiuti | 11 | 448 | «preferirei semplicemente il denaro» |
| il Blaster | 12–13 | 453–459 | il prediletto degli `Shield Beetle`, l'innovazione senza finezza, l'arma per disabilitare |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `<The engineer> proceeds…` | **`<The engineer>` ti conduce…** | token **a inizio frase**, confronto esatto |
| `a blade! <learned>I am Desneeparu` | **una lama! `<learned>`Sono Desneeparu** | token dopo il punto esclamativo |
| `Captain <last>!` | **capitano `<last>`!** | cognome del giocatore, minuscolo «capitano» |
| `Tripulse Shredder` · `Blaster` · `Ion Cannon` | **identici** | nomi di armi |
| `Shield Beetle` · `Firelode` | **identici** | nave e mondo |
| `testing on the field of battle` | **collaudi sul campo di battaglia** | |
| `overcharged, oppressive feel` | **sensazione sovraccarica e opprimente** | |
| `our sympathy` | **la nostra riconoscenza** | |
| `it can jam their weapons` | **riesce a inceppare le armi** | |
| `finezza` | **finezza** | il testo si interrompe con «la... finezza» |

## 3. Difficoltà

1. **Primo `LOGBOOK`** del tratto: diario, non dialogo, e il `Counter(kind)` deve dirlo.
2. **`<The engineer>`**: un segnaposto che contiene articolo e maiuscola. `.lower()` verificherebbe un **simbolo
   diverso**; il controllo è esatto e vieta anche la variante minuscola.
3. **Due virgolette dispari** (12, 13) riprodotte e **non chiuse**; il controllo verifica anche che il segno finale sia
   lo stesso dell'inglese.
4. **Unità 5 è lunga** (una sola unità da 128 parole) e contiene un discorso diretto: le virgolette restano due, non
   quattro, perché la battuta è una sola.
5. **Nomi tecnici** che nessuno traduce: tre armi e una nave, più il mondo `Firelode`.
6. **Gate**: minimo **0,93**, massimo **1,20**, media **1,03** — testo tecnico, quindi vicino all'originale.

## 4. Numeri osservati

```
unita' 13/13 · MISSION_TEXT 12 · LOGBOOK 1 · VALUE 0 · UI_LABEL 0 · token 3 · tutte PENDING
contesto 1 (aperto): Jump Drive Trading · 13 testi distinti
token: <learned> e <last> (unita 2) · <The engineer> (unita 5, esatto) · parita 1 = 1
tab 12 unita (il LOGBOOK no) · virgolette 20, dispari 12 e 13, lasciate aperte
parole EN 703 -> IT 635 (0.903) · rapporto 0.93 - 1.20, media 1.03
righe 423/459 · 115 prima / 19 dopo · confine riga 460, stessa missione
FAIL totale: 0 (32 controlli) · verify exit 0 (27 controlli)
sha256[:16] 56b7e47a1b3a8c72
```

## 5. Stato del progetto

```
TOTALE staging: 27627 unità · 872250 EN · 828651 IT
unfettered 0 prologue.txt: 128/147 (87,1%) · 6 lotti · 3401 EN -> 3081 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4303
residuo misurato: 4970 unità / 104849 parole su 117 file
avanzamento: 27627/32924 unità (83,9%) · 872250/979975 parole (89,0%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (27 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`, nessuna arma comprata.
- **Nessuna partita avviata**: il duello con Desneeparu non è stato giocato.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è all'87,1%**: restano **19 unità** (righe 460–530), l'ultimo tratto.
- **Prossimo lotto**: `HANDOFF_L146_20261019.md` — righe **460–530**, **19 unità**, **656 parole**, **17 `MISSION_TEXT`
  + 2 `UI_LABEL`**, **4 token** (`<origin>`, `<as before (run)>`, `<as before (flee)>`, `<leave>`) e **la chiusura del
  file** a 147/147, verificata con l'invariante di file.
