# L30 — rapporto di chiusura

Lotto `L30_20261018_105244` · `data/coalition/lunarium intro.txt` · righe 21–2111 · 730 unità ·
tradotto a mano, chiuso il 2026-10-18.

## 1. Che cosa contiene il lotto

Questo è l'intero `lunarium intro.txt`: 730 unità, 35 contesti, dalla voce di diario che apre il file
all'ultima missione di adesione. È la porta d'ingresso alla fazione della resistenza dentro la
Coalizione, e i nuclei narrativi, nell'ordine in cui compaiono, sono:

- **La copertura caritatevole** (`Lunarium: Smuggling: Charity 1–3`): una Kimek in uniforme blu assume
  il capitano per consegnare provviste a un mondo povero. Il lavoro è vero, ma è anche il pretesto per
  testare un contrabbandiere.
- **Le granate** (`Grenades`): il capitano viene incappucciato e portato in un seminterrato pieno di
  cubicoli. Chiree si presenta togliendosi le protesi: due zampe le mancano per un «incidente in
  fabbrica» che è una pattuglia degli Heliarchs. Prima richiesta esplicita: armi dallo spazio umano.
- **Gli antimissili** (`AM`): un Arach con un distintivo falso degli Heliarchs «ispeziona» la nave e
  installa un dispositivo di comunicazione su rete separata. È il meccanismo che apre tutte le missioni
  successive del Lunarium.
- **Siluri, calore, reattori** (`Torpedoes`, `Heat`, `Reactors`): tre consegne con ostacoli diversi
  (campo innevato, pianeta di nebbia, finestra di cinque giorni prima del cambio di pattuglia). I
  Saryd che le ricevono parlano con la stessa sintassi marcata dei Kimek e degli Arachi.
- **Casa Bebliss** (`House Bebliss 1-A … 7-FW`): la casata Arach che finanzia il Lunarium. Incontri,
  rifiuto, ripensamento, un pranzo in cui nessuno mangia, e la richiesta di portare Freya a studiare
  i manufatti dei Pug con loro, con un motore di salto fornito dal capitano.
- **Il ponte con i Mondi Liberi** (`3-FW`, `4-FW`): il capitano racconta tutto a JJ, con e senza il
  Lunarium. La conversazione sui Quarg, i tre anelli presi, il sospetto che la guerra sia solo
  rimandata di qualche millennio.
- **Le evacuazioni** (`Evacuation 1–6`): Elirom, che dice di possedere un'agenzia di trasporti, in
  realtà salva membri del Lunarium dalle retate. Studenti, mandriani, immigrati. L'unità più dura del
  lotto è quella dei 116 passeggeri attesi e <bunks> imbarcati: la ragazza Saryd che piange, il vecchio
  che stringe i pugni e non riesce a dire niente.
- **La propaganda** (`Propaganda 1–4`): Tummug, i manifesti-spettacolo, i droni che scrivono nel cielo
  e fanno piovere volantini, la folla che si divide, gli Heliarchs che cancellano la scritta e
  sgomberano le strade. Il vero obiettivo non erano i manifesti ma i registri delle sparizioni.
- **L'addestramento** (`Combat Training 1–4`): Pyakri e 53 membri comprano navi umane e imparano a
  combattere contro i pirati. Nessun morto, molta improvvisazione.
- **L'intervista ai Quarg** (`Quarg Interview`): Oobat intervista un Quarg davanti a una telecamera.
  L'ultima domanda («volete tornare a riprendervi gli anelli?») ottiene un sì immediato, il corpo del
  Quarg diventa nero e la stazione si riempie di Quarg in cerchio. La risposta che il Lunarium sperava
  di usare come prova contro la propaganda degli Heliarchs si ritorce contro di loro.
- **L'adesione** (`Join`, `Coalition Intro Join Patch`): la scatola con il dispositivo di traduzione,
  Chiree che mostra i bulloni delle protesi, e la patch che risolve l'adesione doppia a Heliarchs e
  Lunarium.

## 2. Numeri misurati

| voce | valore |
|---|---|
| unità | 730 / 730 (100.0%) |
| parole | 29.208 EN → 28.079 IT (0,961) |
| contesti | 35 |
| parti | 13 (57, 47, 54, 81, 71, 32, 60, 77, 48, 47, 67, 59, 30 unità) |
| tab / virgolette / token | 550 / 1.449 / 334 |
| non traducibili (`NT`) | 9 (7 `UI_LABEL` + 2 categorie di diario) |
| virgolette dispari | 1 unità (idx 13, riprodotta) |
| `check.py` | `FAIL totale: 0` |
| `verify.py` | 25 controlli, exit 0 |
| `sha256[:16]` di `translation.json` | `5adcc2bfda276f8f` |

Distribuzione dei tipi, misurata sul `source.json` esportato: `MISSION_TEXT` 619 · `VALUE` 33 ·
`DESCRIPTION` 33 · `DIALOG` 26 · `LOGBOOK` 12 · `UI_LABEL` 7. Nessuna `CONVERSATION`.
Token: 13 famiglie, tutte di dati (`<cargo>`, `<destination>`, `<planet>`, `<payment>`, `<bunks>`,
`<origin>`, `<last>`, `<ship>`, `<first>`, `<capacity>`, `<system>`, `<date>`, `<waypoints>`); nessun
pronome-token, quindi `TOKEN_EXC` resta vuoto e la parità dei token è esatta su tutte le unità.

## 3. Metodo

`export_section.py` → ricognizione dei `kind` e del `raw` delle 111 unità non `MISSION_TEXT` →
`check.py` derivato da L29 (`NT` riscritto dopo la ricognizione, docstring con i numeri nuovi) →
13 parti a fine missione, ognuna con normalizzazione dei tab derivata dal sorgente e `check.py --range`
verde → controllo completo dopo le parti → `verify.py` indipendente → questi tre documenti.

Il costruttore delle parti (`l30_build_part.py`, nella scratch dell'agente) scriveva le traduzioni
senza tab e aggiungeva `\t` iniziali leggendoli dal `source.json`: i tab non sono mai stati digitati a
mano. Risultato: 550 tab IT = 550 EN su 730 unità, e nessuno scarto di tab in nessuna parte.

## 4. Difetti e limiti dichiarati

- **Due voci di diario non tradotte** (righe 21 e 467: `log "Factions" "Lunarium Redoubt" "…"`). Il
  nome e il testo non sono nell'inventario di `state.db`: restano in inglese. Dettaglio e causa in
  `review.md` §7. Non correggibile qui: `tools/l10n.py` e `state.db` sono protetti.
- **Nessun rendering nel gioco**: le righe lunghe (fino a oltre 1.500 caratteri) non sono mai state
  viste in una schermata di dialogo di Endless Sky.
- **Nessuna approvazione**: le 730 unità restano `PENDING`; `state.db` aperto in sola lettura.
- **`Factions` lasciato in inglese** per non spezzare il raggruppamento del diario con gli altri file
  non ancora tradotti: scelta dichiarata, non verificata a schermo.
