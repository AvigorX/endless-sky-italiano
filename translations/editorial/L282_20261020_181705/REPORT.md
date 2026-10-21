# REPORT — L282 (`data/wanderer/wanderer missions.txt`, righe 16–41)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 13 (11 `MISSION_TEXT`, 1 `DESCRIPTION`, 1 `VALUE`) | 13 |
| parole | 449 | **420** (0,94) |
| tab | 9 | 9 · primo carattere |
| virgolette | 16 | **16**, per unità |
| alternative `[...]` | **9** | **9**, due opzioni ciascuna |
| segnaposto | 4 (2 famiglie) | **4** |
| apici | 4 | 5 |

Rapporto per unità **0,74 – 1,24**.

## 2. Le alternative fra parentesi quadre

Nove scelte a runtime, in tre unità (5, 8, 11). Sono la **logica** del testo, non una scelta stilistica:

```
"Ci hai aiutato a [difenderci, proteggerci] quando siamo stati attaccati."
"Ci hai portato i nostri [genitori? antenati?]."
"I nostri [insegnanti, mentori] dicono che non è [nativa, originaria] di questo mondo."
"…le piante che [coltiviamo, curiamo] su <planet>…"
"Ci saranno [differenze, complicazioni], ma è il [migliore, più probabile] [piano, approccio] nel breve periodo."
"…non possiamo [ospitare, coltivare] questa pianta lì per sempre."
```

Due dettagli da non sbagliare:

1. **il separatore** — otto coppie usano la **virgola**, una usa il **punto interrogativo** (`parents? ancestors?`): è il
   segno che nel gioco introduce una variante **incerta** (il testo «non sa» quale delle due sia giusta). La resa conserva `?`;
2. **l'ordine** — le alternative non si riordinano: il gioco sceglie a caso fra le opzioni, ma lo **stile** della frase dipende
   dalla posizione (verbo riflessivo, sostantivo, aggettivo).

Il `check.py` verifica numero, posizione e **numero di opzioni** per ognuna; il `verify.py` rifà lo stesso confronto in modo
indipendente, unità per unità.

## 3. `Unfettered` → «Slegati»

Nella prosa, `Unfettered` diventa **«Slegati»**: è la forma **maggioritaria del corpus** (221 occorrenze contro 61 che lasciano
l'inglese). Il `check.py` verifica che in questa unità l'inglese **non** compaia e che compaia la forma italiana. Nei `VALUE` il
nome resta invece invariato, come già stabilito.

## 4. Terminologia

| inglese | resa | nota |
|---|---|---|
| `greenhouses` | **serre** | |
| `drones` | **droni** | |
| `pot` | **vaso** | |
| `deep blue petals` / `teal leaves` | **petali blu intenso** / **foglie verde acqua** | |
| `mentors` | **'mentori'** | fra **apici semplici** nel sorgente, conservati |
| `Wanderer` / `Mereti` | **invariati** | |
| `Unfettered` | **Slegati** | forma maggioritaria (221) |

## 5. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 13 qui · 41 dopo la 41 · copertura 13/54 (24,1%)
```

Due rossi al primo giro, entrambi su **controlli miei troppo rigidi**:

1. il conteggio delle opzioni divideva solo sulla **virgola**, e `[genitori? antenati?]` (separatore `?`) risultava con tre
   opzioni: corretto dividendo su `[,?]` e scartando i segmenti vuoti;
2. cercavo «**droni**» nell'unità 3, che dice «qualche **drone** più piccolo» (singolare): corretto, e aggiunto il controllo su
   «droni» dove il plurale c'è davvero (unità 12).

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING`.
- **Nessun testo visto nel gioco**: le nove alternative sono verificate **per struttura**, non a schermo.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 13/54.
