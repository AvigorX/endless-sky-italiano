# L42 — revisione editoriale

Lotto `L42_20261018_155050` · `data/remnant/remnant 2 cognizance.txt` · righe 16–1747 · 572 unità ·
22.761 parole EN → 21.522 IT · `check.py` `FAIL totale: 0` · `verify.py` 33 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

Le 40 missioni della serie **Cognizance** dei Remnant, dalla prima (Plume che chiede un secondo
sopralluogo sui giganti gassosi di Nenia) fino alla rivelazione su Ssil Vida: la caccia ai Korath che
colpiscono gli spettri del vuoto, il primo contatto con la creatura che disegna costellazioni, l'evacuazione
di uno stormo di spettri del vuoto su Esquiline, la stazione nascosta nel gigante gassoso, i caveau
profondi di Viminal, la prima nave viva (`Merganser`, poi `Peregrine`), il combustibile per il reattore,
la bolla dimensionale di Postverta e il ritorno. È **trama**, non lavoro ripetibile: i personaggi
(Plume, Chilia, Taely, Dusk, Gavriil, Aeolus, Torza) tornano per centinaia di unità.

## 2. Ricognizione (misurata sul `source.json`)

```
MISSION_TEXT 438 · VALUE 39 · DESCRIPTION 39 · DIALOG 19 · UI_LABEL 35 · LOGBOOK 2
contesti 40 · tab 342 · virgolette 909 · token 174 (16 famiglie) · quadre 0
unità con virgolette dispari: 11 (32, 48, 50, 201, 240, 241, 245, 246, 342, 485, 558)
15 gruppi di inglese identico (32 unità su 572)
```

Cinque fatti che hanno richiesto preparazione e **non** si potevano copiare da L41:

- **`NT` = 35 `UI_LABEL`** (in L41 era vuoto). Sono tutte `label` di salto, bersagli di `goto`.
- **Tab 342**: l'indentazione torna; il costruttore del `check.py` antepone `'\t' * ntab`.
- **11 virgolette dispari**: nel `verify.py` il confronto è fra **insiemi di idx**.
- **2 `LOGBOOK`**: una delle due righe è un `log` a tre argomenti, con la lacuna di inventario nota.
- **Token 174 su 16 famiglie**, con `<first>` (30) e `<last>` (6) che sono il nome del giocatore.

## 3. Metodo

1. `export_section.py` su righe 16–1747 → 572 unità, 40 contesti.
2. Ricognizione dei tipi, delle 35 label (`raw`), delle 2 `LOGBOOK`, dei duplicati, dei token.
3. `check.py` derivato da L41: `NT` con le 35 label, docstring riscritta, `TITLES` esteso ai nomi dei
   Remnant, e **costruttore con i tab**.
4. Traduzione in 14 parti, tutte a fine contesto; dopo ogni parte `check.py --range` e, dopo ogni due
   parti, il controllo **completo** (i duplicati fra parti si vedono solo lì).
5. `check.py` completo e `verify.py` indipendente.

## 4. La voce: ereditata, non reinventata

La voce dei Remnant è già stabilita in L21/L24 (`remnant 1 introduction.txt`). Ho riusato il lessico
misurato là, e solo dove serve l'ho esteso:

| inglese | italiano | nota |
|---|---|---|
| Remnant | **Remnant** | invariato, come in tutti i lotti della serie |
| Ember Waste | **Distesa di Braci** | da L24 |
| void sprites | **spettri del vuoto** | da L24 |
| "May the Embers burn bright" | «Che le Braci brucino luminose» | da L24, ripetuto 6 volte in L42 |
| Prefect (Chilia, Taely) | **Prefetto** | titolo, con la maiuscola quando è appellativo |
| chants / sings / signs | «intona» / «canta» / «segna» | distinzione già fissata in L24 |
| gaslined ship | nave **con rivestimento per gas** | da L24, in L42 anche fra virgolette singole |
| Aeon Cell | **Cella Aeon** | `Cell` tradotto, `Aeon` resta nome del modello |
| liveship | **nave viva** | Taely lo definisce nel testo: la resa deve reggere la definizione |
| tackling (spazio) | **aggancio** | «capacità di aggancio», spiegata nel dialogo |
| Ember Node | **Nodo di Braci** | nome della creatura; coerente con «Distesa di Braci» |
| Remnant Logistics | **Remnant Logistics** | nome di un'organizzazione, resta in inglese |
| 'olofez, Palavret, Merganser, Starling, Puffin, Pelican, Ibis, Albatross, Peregrine | invariati | nomi di nave |
| Ssil Vida, Esquiline, Aventine, Viminal, Caelian, Nenia, Nasqueron, Slylandro, Postverta, Patir, Parca, Baianus, Peragenor, Convector, Antevorta | invariati | toponimi |
| Archon, Korath, Sheragi, Hai, Deep | invariati | fazioni e specie |

## 5. Il problema Gavriil: genere non deducibile

Gavriil è indicato nel testo con **`they/them`** e le didascalie lo trattano senza genere. In italiano
questo non è neutro per costruzione, quindi ho scelto una linea unica e l'ho tenuta per tutte le unità:

- niente participi o aggettivi concordati sul soggetto quando si può evitare («Annuisce», «Sorride»,
  «Gesticola», «sembrano fiduciosi» al plurale);
- presentazione senza genere: «Ti presento Gavriil, del nostro team tecnico: è tra le nostre menti
  migliori e conosce bene l'astrobiologia» invece di «un tecnico / una tecnica»;
- la scheda di diario (idx 101) dice «Un tecnico che lavora con Plume, e un talento dell'astrobiologia»
  — nessun «abile astrobiologo/a»;
- dove il genere era inevitabile (dimostrativi, «chi comandava» della Shadow Step) ho usato forme
  invariabili.

Non è una scelta stilistica: il testo sorgente non attribuisce un genere, e attribuirne uno in traduzione
sarebbe un'informazione inventata.

## 6. Le 35 `UI_LABEL`: identiche, e il perché va scritto

Sono tutte `label "..."` di salto. Il `check.py` le elenca una per una e il `verify.py` riasserisce
l'elenco: `void rifle`, `fleet killed`, `skip info`, `good idea`, `lets go`, `skip tech`,
`mission statement`, `mission choice`, `take mission`, `maybe later`, `dusk known`, `dusk name`,
`mission transition`, `mission description`, `science assistant`, `surface vault`, `build vault`,
`walk over`, `merganser intro`, `turn down`, `merganser mission`, `skip explanation`, `know gavriil`,
`remnant gain`, `moving on`, `gavriil end`, `cleared orbit`, `not thirsty`, `power briefing`,
`ssil vida emerald sword`, `ssil vida continue`, `lets fly`, `cut power`, `cognizance untrusted`,
`cognizance explanation`.

Tre di queste (`good idea`, `lets go`, `maybe later`, `turn down`, `not thirsty`) **sembrano** testo
visibile al giocatore, ed è la ragione per cui la docstring del `check.py` dice «label di salto» e non
«testo non traducibile»: metterle in `NT` è corretto in entrambi i casi, perché tradurle romperebbe il
`goto`, ma la motivazione va detta giusta.

## 7. Lacuna di inventario: la riga `log` a tre argomenti (riga 388)

```
log "People" "Gavriil" `A technician that works with Plume…`
```

Il `source.json` produce **una sola** unità (idx 101) ed è il **testo** del diario: categoria (`People`) e
nome (`Gavriil`) non sono inventariati. È il difetto noto di `tools/l10n.py`, che è **protetto**: non si
ripara e non si aggira. Conseguenza dichiarata: nel diario del giocatore la voce comparirà con categoria
e nome in inglese e il testo in italiano, esattamente come per le lacune di L30, L33, L34 e L35.

La seconda riga (`log "Successfully introduced a flock of void sprites…"`, riga 666) è a due argomenti e
il suo testo è inventariato regolarmente (idx 178): tradotta.

## 8. Cosa è stato corretto e perché

Tre errori reali, tutti presi dai controlli e non dalla rilettura:

1. **Unità 336 e 337** (`"No."`, `"Yes."`): scritte senza virgolette, quindi 0 virgolette contro 2.
   Il `--range 324 360` le ha fermate subito; corrette in `"No."` / `"Sì."`.
2. **Unità 469** (`(Agree.)`): resa «(Accetta.)» come 354/377 (`(Accept.)`). I tre inglesi sono due
   testi distinti, quindi l'italiano doveva differire: «(D'accordo.)». Il `--range` non lo vedeva, il
   `check.py` completo sì.
3. **Unità 384** (`"Why the rush?"`): la prima stesura («Perché tutta questa fretta?») stava a 1,88,
   dentro il gate ma a un passo dal limite. Riscritta «Perché tanta fretta?» (1,33) senza perdere nulla.

Una correzione ha riguardato lo **strumento**, non il testo: il primo `verify.py` confrontava le parti
con `translation.json` senza rimettere i tab che il costruttore aggiunge, e falliva su un lotto corretto.
Ora ricostruisce `'\t' * ntab + valore` prima di confrontare.

## 9. Controlli e limiti

`check.py` (21 controlli): copertura, unità vuote, `NT` (35), duplicati italiano spiegati dal sorgente,
tab per unità e come totale, tab iniziale, virgolette per unità e come totale, quadre, token, backtick,
spazi, rapporto, tipografia, caratteri non latini, parole residue, stato del database.

`verify.py` (33 controlli) ricostruisce tutto da `source.json`, dal file sorgente e da `state.db` in sola
lettura. In più asserisce: le 35 `UI_LABEL` identiche **come elenco**, le 2 `LOGBOOK` tradotte, l'assenza
di quadre in entrambe le lingue, l'insieme delle 11 virgolette dispari, la parità di tab e virgolette
**per unità**, la copertura 572/572 e la coppia di righe (16, 1747).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 572 unità `PENDING`.
- **Nessuna verifica a schermo.** Non ho visto una sola missione di Cognizance scorrere: i 35 salti `goto`
  sono intatti per costruzione (le label sono byte-identiche), ma il percorso non è stato giocato.
- **Il rapporto 0,60–1,77 non è un giudizio di qualità.**
- **La voce di Gavriil** è una scelta di resa, non una traduzione letterale: chi riprende la serie deve
  mantenerla, non rimettere «l'astrobiologo».
