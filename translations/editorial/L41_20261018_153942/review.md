# L41 — revisione editoriale

Lotto `L41_20261018_153942` · `data/human/free worlds war jobs.txt` · righe 16–927 · 72 unità ·
1.124 parole EN → 1.140 IT · `check.py` `FAIL totale: 0` · `verify.py` 30 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

I lavori di guerra delle Free Worlds: la ricognizione di sistemi in cerca della Marina; il convoglio di
rifornimenti al cantiere; il trasporto di soldati al fronte; i rifornimenti al banco degli equipaggiamenti;
i pacchi di conforto fra le due parti del conflitto; i profughi in fuga dal fronte.

Sono **lavori ripetibili**, non trama: nessun personaggio ricorrente, nessun arco. Il giocatore li vede
molte volte, e questo cambia il criterio di traduzione: **la frase deve reggere alla ventesima lettura**.
Ho preferito una sintassi piana e priva di effetti a una più brillante che stanca.

## 2. Ricognizione (misurata sul `source.json`)

```
VALUE 29 · DESCRIPTION 29 · DIALOG 8 · TEXT 6 · UI_LABEL 0 · CONVERSATION 0 · LOGBOOK 0
contesti 34 · tab 0 · virgolette 0 · token 172 (10 famiglie)
unità con virgolette dispari: 0 · unità con quadre: 0
17 gruppi di inglese identico (64 unità su 72)
```

Tre fatti che hanno richiesto preparazione e **non** si potevano copiare da L40:

- **`NT` torna vuoto** (in L40 era `{80}`): 0 `UI_LABEL`. Copiare `{80}` avrebbe messo in `NT` un
  indice inesistente e fatto fallire il controllo.
- **Tab 0 e virgolette 0**: prima volta nella serie. I controlli restano e asseriscono la parità su zero.
- **`TEXT` 6**: tipo mai incontrato. Sono testi di `phrase`, con la cornice di backtick nel `raw`.

## 3. Metodo

1. `export_section.py` su righe 16–927 → 72 unità, 34 contesti.
2. Ricognizione dei tipi, dei 6 `TEXT`, dei duplicati, dei token.
3. `check.py` derivato da L40 con `NT = set()` e `TITLES` esteso.
4. Traduzione in 2 parti a fine contesto (1–40, 41–72), ciascuna chiusa con il controllo del rapporto e
   dei token.
5. `check.py` completo (verde al primo colpo) e `verify.py` indipendente.

## 4. La voce di un lavoro ripetibile

Il testo inglese è **burocratico e impersonale**: «These N soldiers of the Free Worlds request immediate
transport…», «The outfitter on <planet> is low on supplies and needs to be resupplied immediately.»

Ho tenuto il registro **amministrativo** e la voce passiva, senza colorire:
- «Questi `<bunks>` soldati delle Free Worlds richiedono un trasporto immediato…»
- «Il banco degli equipaggiamenti su <planet> è a corto di scorte e deve essere rifornito subito.»

L'unico punto in cui il testo si scalda è il pacco di conforto, dove c'è una persona che si preoccupa per
i familiari dall'altra parte del fronte: «Un cittadino delle Free Worlds è in pena per i familiari nella
Repubblica.» Lì ho lasciato «in pena», che è più umano di «preoccupato» e non aggiunge retorica.

## 5. I titoli: la scelta più delicata

I titoli (`Scouting Run`, `Convoy to <planet>`, `Reinforcements to <planet>`, `Resupply <planet>`,
`Care package to <planet>`, `Refugees to <planet>`) compaiono nella lista lavori, dove lo spazio è poco e
il confronto fra lavori è immediato.

| inglese | italiano | nota |
|---|---|---|
| Scouting Run | **Ricognizione** | più corto dell'inglese, e la parola dice esattamente il lavoro |
| Convoy to `<planet>` | **Convoglio per `<planet>`** | «per» regge sia la destinazione sia il committente |
| Reinforcements to `<planet>` | **Rinforzi per `<planet>`** | |
| Resupply `<planet>` | **Rifornisci `<planet>`** | qui il verbo all'imperativo è più chiaro del sostantivo, ed è coerente con la `DESCRIPTION` che ordina l'azione |
| Care package to `<planet>` | **Pacco di conforto per `<planet>`** | «care package» non ha equivalente breve: «pacco di conforto» è la resa standard e resta comprensibile |
| Refugees to `<planet>` | **Profughi per `<planet>`** | |

`Resupply <planet>` è l'unico caso in cui ho cambiato la categoria grammaticale (sostantivo → verbo):
in italiano «Rifornimento `<planet>`» sembra un nome di prodotto, e la lista lavori è fatta di frasi che
dicono cosa farai.

## 6. Le differenze che l'inglese marca e l'italiano deve marcare

Il file è parametrico e ripetitivo, ma non identico: le differenze sono **il contenuto informativo**, e
vanno conservate.

- **27 / 28**: `A captain … thanks you` / `The captains … thank you`. In italiano la differenza si porta
  su tre parole: «Un capitano delle Free Worlds … ti ringrazia» / «I capitani delle Free Worlds … ti
  ringraziano». Senza il plurale del verbo la differenza sparirebbe.
- **57/59 vs 61/63**: le prime due dicono «un cittadino delle Free Worlds … familiari nella Repubblica»,
  le seconde l'opposto. Ho invertito le fazioni, non solo le parole: «delle Free Worlds»/«nella
  Repubblica» e «della Repubblica»/«nelle Free Worlds».
- **30 vs 34–40**: alcune `DESCRIPTION` dicono «a `<destination>`», altre no, perché la destinazione è il
  pianeta corrente. L'italiano conserva l'omissione: «Consegna `<tons>` di `<commodity>` smontato entro il
  `<date>`» senza «a» — e la frase resta grammaticale.
- **14 / 17 / 20** (gli avvisi di convoglio incompleto) sono identici fra loro: qui l'italiano **deve**
  essere identico, perché il gioco mostra lo stesso messaggio.

## 7. Il caso `TEXT`

Le 6 unità `TEXT` sono frasi di `phrase`, e il `raw` le mostra fra backtick:

```
`A Free Worlds captain is waiting for you when you land and takes a copy of your scanner logs, and you collect the payment of <payment>.`
```

L'`english` non contiene i backtick: la cornice sta nel `raw`. Il costruttore la ricostruisce, e il
`verify.py` asserisce che (a) le 6 `TEXT` siano tradotte, (b) nell'italiano **non** compaia nessun
backtick (se comparisse, sarebbe un errore di costruzione). Questa è la ragione per cui il controllo dei
backtick è rimasto nel `check.py` anche se il file ha 0 backtick nell'`english`.

## 8. Cosa è stato corretto e perché

Niente è stato riscritto per il gate: **tutte le 72 unità sono passate al primo `check.py` completo**.
I controlli di banda comoda hanno dato 0 unità fuori (0,81–1,25), i duplicati 0 FAIL, i token 172 = 172.

Le uniche decisioni prese in scrittura, prima dei controlli:

- **2 (`Ricognizione`)**: 11 caratteri contro 12 dell'inglese, e il testo della `DESCRIPTION` dice
  «esplora» — il titolo dice la stessa cosa con la parola tecnica che usa il gioco.
- **14/17/20**: «una parte o tutto il convoglio» per `part or all of the convoy`; «Meglio ripartire e
  aspettare che arrivino in questo sistema» conserva l'imperativo del sorgente.
- **55**: «Consegni il pacco di conforto di `<commodity>` all'indirizzo indicato e spieghi alla gente da
  dove viene.» Il sorgente dice `explain to the people where it came from`: «alla gente» è più naturale
  di «alle persone», e il resto della frase resta impersonale.

## 9. Controlli e limiti

`check.py` (22 controlli): copertura, unità vuote, `NT`, duplicati italiano spiegati dal sorgente, tab e
virgolette per unità e come totale (qui **zero**), quadre per unità, token `<...>`, backtick, spazi,
rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (30 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) `NT` vuoto come assenza, (b) le 6
`TEXT` tradotte e senza backtick nell'italiano, (c) tab e virgolette a zero in entrambe le lingue, (d)
nessuna virgoletta dispari, (e) le 2 parti ricostruiscono `translation.json`, (f) la copertura totale
72/72 e la coppia di righe (16, 927).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 72 unità `PENDING`.
- **Nessuna verifica nell'editor.** In particolare non ho visto i sei titoli nella lista lavori, dove lo
  spazio è poco e «Pacco di conforto per `<planet>`» è il più lungo: potrebbe andare a capo.
- **Il rapporto 0,81–1,25 non è un giudizio di qualità.**
