# L42 — rapporto del lotto

`data/remnant/remnant 2 cognizance.txt` · righe **16–1747** · lotto `L42_20261018_155050` ·
**572/572 unità** · ventiduesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **572 / 572** (file completo) |
| parole | 22.761 EN → **21.522 IT** (0,945) |
| contesti | 40 (`Remnant: Cognizance 1` … `Remnant: Cognizance 38`) |
| parti | 14 — 58, 39, 49, 41, 38, 52, 46, 37, 39, 35, 22, 50, 40, 26 |
| tab | **342 = 342** (342 unità che iniziano con tab) |
| virgolette | **909 = 909** |
| virgolette dispari | **11 unità**, stessi idx in italiano (32, 48, 50, 201, 240, 241, 245, 246, 342, 485, 558) |
| token `<...>` | **174 = 174** (16 famiglie) |
| quadre `[` `]` | **0 unità** (asserito in `verify.py`) |
| backtick | **0** nell'`english` (stanno nel `raw`) e 0 nell'italiano |
| rapporto per unità | 0,60 – 1,77 |
| `check.py` | **FAIL totale: 0** (21 controlli) |
| `verify.py` | **33 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `1115f51df15d6704` · `source.json` `1aee305d06ec18a5` · `check.py` `940cf534f74e7aba` · `verify.py` `08cf6e342980ceea` |

Il file parte dalla riga **16**; il `verify.py` asserisce `(first, last) == (16, 1747)` e 0 unità prima
e dopo.

## Tipi

438 `MISSION_TEXT` · 39 `VALUE` · 39 `DESCRIPTION` · 19 `DIALOG` · **35 `UI_LABEL`** · 2 `LOGBOOK` ·
0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 35 `UI_LABEL`

Sono tutte `label "..."` di salto, bersagli di `goto`: restano **identiche**, e il `verify.py` le
asserisce una per una.

| idx | label | idx | label |
|---:|---|---:|---|
| 49 | `void rifle` | 343 | `turn down` |
| 62 | `fleet killed` | 352 | `merganser mission` |
| 110 | `skip info` | 369 | `skip explanation` |
| 173 | `good idea` | 374 | `know gavriil` |
| 175 | `lets go` | 394 | `remnant gain` |
| 202 | `skip tech` | 396 | `moving on` |
| 204 | `mission statement` | 398 | `gavriil end` |
| 214 | `mission choice` | 428 | `cleared orbit` |
| 218 | `take mission` | 445 | `not thirsty` |
| 220 | `maybe later` | 447 | `power briefing` |
| 232 | `dusk known` | 465 | `ssil vida emerald sword` |
| 236 | `dusk name` | 468 | `ssil vida continue` |
| 255 | `mission transition` | 479 | `lets fly` |
| 257 | `mission description` | 530 | `cut power` |
| 266 | `science assistant` | 565 | `cognizance untrusted` |
| 296 | `surface vault` | 569 | `cognizance explanation` |
| 320 | `build vault` | | |
| 331 | `walk over` | | |
| 333 | `merganser intro` | | |

## Le 16 famiglie di token

| token | volte | token | volte |
|---|---:|---|---:|
| `<planet>` | 40 | `<tons>` | 6 |
| `<first>` | 30 | `<last>` | 6 |
| `<ship>` | 27 | `<waypoints>` | 4 |
| `<destination>` | 19 | `<system>` | 2 |
| `<stopovers>` | 12 | `<day>` | 2 |
| `<payment>` | 8 | `<npc>` | 1 |
| `<origin>` | 8 | `<cargo>` | 1 |
| `<date>` | 7 | `<fare>` | 1 |

`<first>` e `<last>` sono nome e cognome del giocatore: mai tradotti, mai spostati rispetto agli
articoli.

## Controlli eseguiti

`check.py` (21 controlli): copertura, unità vuote, `NT` (35 identiche), duplicati italiano spiegati dal
sorgente, tab per unità e come totale, tab iniziale conservato, virgolette per unità e come totale,
quadre per unità, token `<...>`, backtick, spazi iniziali/finali e doppi, rapporto lunghezze, tipografia,
caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (33 controlli) **non riusa** la logica di `check.py`: riga grezza contro il file sorgente,
`english`/`kind`/`path` contro `state.db`, stato `PENDING`, id univoci e ordine, collocazione 16–1747,
copertura totale 572/572 da un solo lotto, distribuzione dei kind, 35 `UI_LABEL` tutte in `NT` e identiche,
2 `LOGBOOK` tradotte, assenza di quadre (sorgente e italiano), token a parità esatta, tab e virgolette
come totali **e per unità**, insieme delle 11 virgolette dispari, italiano non vuoto, caratteri non
latini, trattini lunghi e virgolette curve, rapporto, e ricostruzione di `translation.json` dalle 14
parti con i tab del costruttore rimessi.

## Duplicati

15 gruppi di inglese identico per **32 unità su 572**. Sono risposte di dialogo e testi di missione
ripetuti in contesti diversi (`Cognizance 36`/`36 Patir 3`/`37`/`37 Patir 3` sono quattro missioni
parallele con lo stesso testo):

| unità | inglese | italiano |
|---|---|---|
| 7, 11 | `Not right now, but I could later.` | «Non adesso, ma potrei più tardi.» |
| 56, 58 | assegnazione `<payment>` da Remnant Logistics | identici |
| 168, 171 | `Are we sure this is a good idea?` | «Siamo sicuri che sia una buona idea?» |
| 216, 337, 403 | `Yes.` | «Sì.» |
| 336, 404 | `No.` | «No.» |
| 354, 377 | `(Accept.)` | «(Accetta.)» |
| 355, 378, 470 | `(Decline.)` | «(Rifiuta.)» |
| 420, 424 | `Recover equipment from Baianus` | «Recupera l'attrezzatura da Baianus» |
| 535, 538 | `De-activate Ssil Vida Power` | «Disattiva l'energia di Ssil Vida» |
| 536, 539 | `Accept this to signal everyone to cut the power.` | identici |
| 537, 540 | «shudder… prior, barren, form» | identici |
| 541, 544 | `Activate Ssil Vida Power` | «Attiva l'energia di Ssil Vida» |
| 542, 545 | `Accept this to signal everyone to restore the power.` | identici |
| 543, 546 | «shudder… overflowing with life» | identici |
| 550, 553 | `(Explain everything that happened.)` | «(Spiega tutto quello che è successo.)» |

Un quasi-duplicato è stato differenziato: **469** (`(Agree.)`) non è identico a 354/377
(`(Accept.)`), quindi l'italiano è «(D'accordo.)» e non «(Accetta.)». Il controllo dei duplicati l'ha
trovato al primo `check.py` completo, non nel `--range`.

## Nota di inventario

Il file ha **2 righe `log`**:

- riga 388, `log "People" "Gavriil" \`A technician that works with Plume…\`` → il `source.json` produce
  **una sola** unità (idx 101), che è il **testo**. Categoria (`People`) e nome (`Gavriil`) non sono
  inventariati: lacuna di `tools/l10n.py` (protetto), documentata nel `review.md` §7.
- riga 666, `log "Successfully introduced a flock of void sprites…"` → una unità (idx 178), regolarmente
  inventariata e tradotta.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 572 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo del percorso di Cognizance con i salti `goto`.
- Nessun test di gameplay della campagna Remnant.
