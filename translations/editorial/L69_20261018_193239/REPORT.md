# REPORT — L69 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Cosa contiene il lotto

La caccia a Riiria, in tre tempi.

**Tempo 1 — la stazione deserta** (unità 3–9). Il giocatore arriva su `<planet>` seguendo le indicazioni
del contatto di Casa Myurej e trova lo spazioporto quasi vuoto, con container aperti di recente e una
sacca di effetti personali abbandonata. Frugando trova una **sfera di dati ancora calda** con un messaggio
di un complice di Riiria, spaventato: le Casate non li troveranno perché non osano toccare i relitti che
considerano monumenti della propria follia — ma c'è uno straniero di cui le Casate si servono, e «gli stolti
sono più temibili dei saggi». Poi il giocatore si sposta a sud, verso l'altra stazione.

**Tempo 2 — il relitto** (unità 12–16 e 17–27, due rami della stessa scena). Una nave cargo dei Successori
senza alimentazione, corazzatura asportata e un foro praticato sopra il vano del generatore. Il numero di
identificazione la riconduce alla nave cercata; le stive sono vuote, ma un terminale quasi morto restituisce
il **manifesto di carico**: regali vari, gioielli in oro rosso, acqua programmata per le vasche del
Consiglio, armi cerimoniali, animali rari in stasi, e **16 tonnellate di filtri di lusso ad alta
pressione**. L'ultima voce è l'indizio: i filtri richiedono un ambiente pressurizzato, quindi servono un
mondo con atmosfera densa.

**Tempo 3 — la deduzione** (unità 24–31, con i due rami). Il terminale spiega cosa sono i filtri (unità
25). Poi due varianti: una in cui il giocatore non trova candidati e dovrà cercare a mano, una in cui pensa
subito a **Maspa-Viir-Kella**, mondo disabitato nel sistema di Osolaa-Uuoru. Chiude il lotto la descrizione
della missione successiva («Rintraccia Riiria»).

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `Search <planet>` / `Continue the search` / `Track down Riiria` | **verbo all'imperativo** («Cerca», «Continua la ricerca», «Rintraccia») | i nomi di missione vivono in una lista di cose da fare: è la forma già usata in L68 («Recupera i regali di nozze rubati») |
| `icons'f their folly` | «icone della propria follia» | il dialetto inglese è reso con italiano popolare, non con contrazioni artificiali |
| `that alien the Houses're so fond'f using` | «quello straniero che le Casate sono così felici di usare» | «straniero» è già la parola di L68 per il giocatore visto dai Successori |
| `fools're much more fearsome than the wise` | «gli stolti sono molto più temibili dei saggi» | massima del complice: resta sentenziosa, senza ammorbidirla |
| `freighter` | **nave cargo** | «cargo» è già la forma dello staging (269 occorrenze) |
| `cargo bays` / `cargo manifest` / `cargo scanner` | **stive** / **manifesto di carico** / **scanner di carico** | termini già presenti; «manifesto» è la parola del progetto |
| `disused landing pads` | **piazzole in disuso** | forma già in staging |
| `hulk` | **relitto** | idem |
| `programmed water (for Council pools)` | «acqua programmata (per le vasche del Consiglio)» | `Council` → **Consiglio**, istituzione già tradotta così |
| `high-pressure lux filters` | «filtri di lusso ad alta pressione» | `lux` è abbreviazione di *luxury*, e la descrizione lo dice: «Unità filtranti di lusso» |
| `Ojde`, `Maspa-Viir-Kella`, `Osolaa-Uuoru` | **invariati** | nome di nave e toponimi |
| `8 million credits per unit` | «8 milioni di crediti per unità» | nel testo tecnico la cifra resta numerica, come `8` nel sorgente |

## 3. Difficoltà incontrate

1. **`NT` e `LOGBOOK` spariti rispetto a L68.** Il `check.py` derivato li dichiara **vuoti** e lo asserisce
   (`== set()`, `== []`), più un controllo sul `raw`: nessuna riga `log` nel segmento. Un lotto che «non ha»
   un tipo deve dirlo, non tacerlo (decisione 160).
2. **Due missioni con lo stesso nome** (`Track down Riiria`, unità 28 e 30): la resa identica è corretta
   perché l'inglese è identico. Il controllo dei duplicati, che segnala solo le rese ripetute fra inglesi
   **diversi**, resta verde; il `verify.py` asserisce esattamente il gruppo `{28, 30}`.
3. **Il manifesto di carico è una tabella travestita da prosa.** Sei unità (18–23) con numero, unità di
   misura e nota fra parentesi: la tentazione è compattare o cambiare «tonnellate» in «t», che romperebbe
   la forma della lista. Sono rimaste voci separate, con la stessa punteggiatura.
4. **Due testi quasi identici con esito opposto** (unità 26 e 27): cominciano con la stessa frase («Mentre
   ti scolleghi dal terminale, pensi ai pianeti vicini…») e finiscono diversamente — «non te ne viene in
   mente nessuno» / «e uno ti viene in mente». Sono due rami dello stesso bivio e la ripetizione iniziale è
   nel sorgente: non è un duplicato, e il controllo italiano (che confronta l'intera stringa) non la segnala.
5. **Il refuso del sorgente** («Not longer after», unità 12): corretto nel senso, dichiarato nel `review.md`.

## 4. Numeri osservati (output letto, non dedotto)

```
unita' tradotte nell'intervallo   31/31
copertura del lotto               31/31
tab IT 27 / EN 27
virgolette IT 4 / EN 4
token IT 10 / EN 10
rapporto IT/EN 0.75 - 1.56
parole EN 687 -> IT 704
prima/ultima riga del segmento: 118/197
duplicati inglese: 1 gruppi (2 unita)
FAIL totale: 0                     (35 controlli)
verify.py exit 0                   (46 controlli)
sha256[:16] translation.json      7ab0a2bee4dc90a6
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24283 unita · 775601 EN · 735072 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 73
```

`successor 2 ghosts myurej.txt` è coperto **80/211 unità (37,9%)**: restano **131 unità** dopo la riga 197.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto per intero |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (35 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (46 controlli) |
