# REPORT — L136 · `data/starts.txt` (secondo inizio: il padre, la licenza comprata, il cantiere)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'inizio | 1–3 | 135–137 | nome `Birthday Surprise`, Mainsail, il padre finanziere, la festa dei diciotto anni |
| la storia del mondo | 4–9 | 154–159 | la licenza e i 500.000 crediti; poi le **cinque frasi rilette** da L135 |
| il regalo | 10 | 161 | il padre offre licenza e nave; la risposta immediata |
| il dipartimento | 11–12 | 162–163 | la fila saltata con due gettoni, la procedura «tramite la rete», la battuta troncata |
| la firma | 13–14 | 164–165 | il secondo gettone, lo stilo, le pagine legali saltate |
| il cantiere | 15 | 167 | licenza in una mano, 500.000 nell'altra, quattro modelli abbordabili |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Birthday Surprise` | **identico** | `VALUE`: nome dell'inizio |
| `oceanic Paradise World terraformed to perfection` | **un Mondo del Paradiso oceanico terraformato alla perfezione** | |
| `pampered life` | **vita viziata** | |
| `your eighteenth birthday party winds down` | **la festa per il tuo diciottesimo compleanno volge al termine** | |
| `has no mortgage` | **non prevede mutui** | |
| `500,000 credits` | **500.000 crediti** | unità 4 e 15 |
| `Republic Department of Starship Licensing` | **Dipartimento Repubblicano per le Licenze di Astronave** | |
| `credit chip` | **gettone di credito** | |
| `flicks a credit chip at each of them` | **lancia un gettone di credito a ciascuna di loro** | «ciascuna»: le due persone sono la cliente e l'impiegata |
| `through the net` | **tramite la rete** | |
| `three to five business days` | **da tre a cinque giorni lavorativi** | |
| `stylus and a pad` | **stilo e una tavoletta** | |
| `skipping past a number of pages of legal text` | **dopo aver saltato diverse pagine di testo legale** | |

## 3. Difficoltà

1. **Cinque frasi condivise con L135** (unità 5–9): rilette dal `translation.json` precedente e verificate identiche.
2. **La previsione dell'handoff era sbagliata**: diceva che nessuna delle condivise ricadeva qui. Il `verify.py` la
   smentisce con una query, non con un'opinione.
3. **Battuta troncata dal sorgente** (`before-"`): riprodotta, con un controllo che vieta di «ripararla».
4. **Distribuzione delle virgolette** irregolare (2, 4, 2, 4, 2): si confronta la sequenza per unità.
5. **`child` senza genere in italiano**: reso «figlio», scelta dichiarata.
6. **Due gettoni, due destinatari**: «ciascuna di loro» invece di «ciascuno», perché le due persone nominate sono
   femminili nel contesto (cliente in fila, impiegata).
7. **Gate**: minimo 0,85 (unità 14, «Senza esitare e dopo aver saltato diverse pagine di testo legale, firmi il tuo
   nome:»), massimo 1,12.

## 4. Numeri osservati

```
unita' 15/15 · CONVERSATION 8 · LOGBOOK 4 · DESCRIPTION 2 · VALUE 1 · UI_LABEL 0 · token 0
contesti 2 completi (3 / 12) · 10 testi propri + 5 riletti · 15 distinti
tab 6 unita · virgolette 14 (6:2, 10:4, 11:2, 12:4, 13:2), nessuna dispari · quadre 0
parole EN 587 -> IT 559 (0.952) · rapporto 0.85 - 1.12, media 1.01
righe 135/167 · 32 prima / 66 dopo · confine riga 172 (start:syndicate)
FAIL totale: 0 (28 controlli) · verify exit 0 (28 controlli)
sha256[:16] adbc2022515e8753
```

## 5. Stato del progetto

```
TOTALE staging: 27433 unità · 866685 EN · 823483 IT
starts.txt: 47/113 (41,6%) · 2 lotti · 2072 EN -> 2007 IT
file completi: quarantotto · residuo traducibile (formula state.py): 4497
residuo misurato: 5164 unità / 110414 parole su 118 file
avanzamento: 27433/32924 unità (83,3%) · 866685/979975 parole (88,4%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`, nessun inizio caricato nel gioco.
- **Nessuna partita avviata**: non ho visto il menu degli inizi né la scena del padre.
- **Nessuna revisione umana**.
- **`starts.txt` è al 41,6%**: restano **66 unità** (cinque inizi).
- **Prossimo lotto**: `HANDOFF_L137_20261019.md` — righe **172–214**, **17 unità**, 802 parole, **2 contesti
  completi**, **1 `VALUE`** (`Escaping Squalor`), **12 virgolette**, **8 tab**, **5 frasi rilette da L135**.
