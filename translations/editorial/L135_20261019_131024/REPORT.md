# REPORT — L135 · `data/starts.txt` (gli inizi di partita: la banca, il treno, il cantiere)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'inizio classico | 1–3 | 18–20 | nome `Endless Sky`, il ragazzo di New Boston, la tessitura, il mutuo, la nota «esperienza classica» |
| la storia del mondo | 4–9 | 74–79 | la licenza appena comprata, la Repubblica, il Parlamento, il Sindacato, i pirati |
| la banca | 10–14 | 81–85 | l'edificio «futuristico», il mediatore, la penna, i 480.000 crediti, la firma |
| l'uscita | 15–16 | 87–88 | l'ascensore, il sorriso, il cantiere navale, tre modelli |
| il secondo inizio | 17–19 | 93–95 | nome `Deep Desire`, Midgard, il programma del Deep, il prestito agevolato |
| di nuovo la storia | 20–25 | 116–121 | la domanda accettata e le cinque frasi già viste (21–25 = 5–9) |
| New Reykjavik | 26–32 | 123–130 | il treno, l'ufficio, l'emblema dell'albero, le due tessere, lo sportello automatico, il cantiere |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Endless Sky` · `Deep Desire` | **identici** | nomi degli inizi (`VALUE`) |
| `textile mill` | **tessitura** | |
| `mortgage` | **mutuo** | |
| `Deep` · `Dirt Belt` | **Deep** · **Dirt Belt** | nomi di regione: restano inglesi |
| `megacorporation` | **megacorporazione** | |
| `factory worlds` | **mondi-fabbrica** | |
| `Truth in Lending statement` | **il prospetto sulla verità del prestito** | |
| `480,000 credits` | **480.000 crediti** | separatore italiano, valore intatto |
| `0.4%` · `2,503` · `433,567` | **0,4%** · **2.503** · **433.567** | idem |
| `Certificate of Eligibility` | **Certificato di idoneità** | |
| `a red tree with branches forming the shape of a brain` | **un albero rosso i cui rami formano la sagoma di un cervello** | emblema del Deep |
| `Peace. Prosperity. Progress.` | **Pace. Prosperità. Progresso.** | motto |
| `shabby` | **sciatto** | |

## 3. Difficoltà

1. **Tipo di file nuovo**: `VALUE` = **nome dell'inizio**, non nome di missione. Il controllo lo verifica come lista
   esatta `[(1, 'Endless Sky'), (17, 'Deep Desire')]`.
2. **Zero token in tutto il file** (113 unità): asserzione vuota `== {}`, più forte di una lista vuota.
3. **Cinque frasi ripetute** fra i due inizi, rese con **costanti** e verificate per confronto diretto.
4. **Numeri**: la convenzione italiana cambia i separatori (`480,000` → `480.000`, `0.4%` → `0,4%`). Due controlli, uno
   che pretende le forme italiane e uno che **vieta** le inglesi.
5. **Nomi di regione**: `Deep` e `Dirt Belt` restano inglesi; un controllo verifica anche che «Profondo» **non**
   compaia.
6. **Una sola ripetizione non ovvia**: `New Reykjavik` è capitale del Deep, e resta traslitterata come nel resto dello
   staging.
7. **Gate**: minimo **0,94** (unità **15**, «L'ascensore è così ben calibrato che non ti accorgi nemmeno che si
   muove…»), massimo **1,28** (unità **4**, la voce di diario sulla licenza).

## 4. Numeri osservati

```
unita' 32/32 · CONVERSATION 18 · LOGBOOK 8 · DESCRIPTION 4 · VALUE 2 · UI_LABEL 0 · token 0
contesti 4 completi (3 / 13 / 3 / 13) · testi distinti 27 (5 ripetizioni)
tab 14 unita · virgolette 14, nessuna dispari · quadre 0
parole EN 1485 -> IT 1448 (0.975) · rapporto 0.94 - 1.28, media 1.05
righe 18/130 · 0 prima / 81 dopo · confine riga 135 (start:paradise)
FAIL totale: 0 (29 controlli) · verify exit 0 (29 controlli)
sha256[:16] f897bd0f3d943382
```

## 5. Stato del progetto

```
TOTALE staging: 27418 unità · 866098 EN · 822924 IT
starts.txt: 32/113 (28,3%) · 1 lotto · 1485 EN -> 1448 IT
file completi: quarantotto · residuo traducibile (formula state.py): 4512
residuo misurato: 5179 unità / 111001 parole su 118 file
avanzamento: 27418/32924 unità (83,3%) · 866098/979975 parole (88,4%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 32 unità `PENDING`, nessun inizio caricato nel gioco.
- **Nessuna partita avviata**: non ho visto il menu di scelta dell'inizio, né la scena della banca.
- **Nessuna revisione umana**.
- **`starts.txt` è al 28,3%**: restano **81 unità** (7 inizi).
- **Prossimo lotto**: `HANDOFF_L136_20261019.md` — stesso file, righe **135–171** (**15 unità**, 587 parole, **2 contesti
  completi**, 8 `CONVERSATION`, 4 `LOGBOOK`, 2 `DESCRIPTION`, 1 `VALUE` `Birthday Surprise`, **14 virgolette**, 6 tab).
