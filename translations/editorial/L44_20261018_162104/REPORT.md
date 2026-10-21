# L44 — rapporto del lotto

`data/sheragi/archaeology missions.txt` · righe **16–1718** · lotto `L44_20261018_162104` ·
**625/625 unità** · ventiquattresimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **625 / 625** (file completo) |
| parole | 18.966 EN → **17.522 IT** (0,924) |
| contesti | 33 (`Deep Archaeology 1` … `Sheragi Archaeology: Epilogue`) |
| parti | 13 — 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 25 |
| tab | **483 = 483** (483 unità che iniziano con tab) |
| virgolette | **921 = 921** |
| virgolette dispari | **17 unità** (209, 249, 260, 262, 269, 302, 322, 367, 369, 379, 383, 388, 477, 478, 502, 522, 542), stessi idx in italiano |
| token `<...>` | **73 = 73** (8 famiglie) |
| quadre `[` `]` | **0 unità** (asserito) |
| `LOGBOOK` | **12** (5 delle quali a tre argomenti) |
| `CONVERSATION` | **0** (asserito) |
| rapporto per unità | 0,61 – 1,77 |
| `check.py` | **FAIL totale: 0** (25 controlli) |
| `verify.py` | **37 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `2a83b689b3604483` · `source.json` `9dc2f6740203722e` · `check.py` `ec7f39dc299c8c93` · `verify.py` `1e81dc72d5f947de` |

Il file parte dalla riga **16**; il `verify.py` asserisce `(first, last) == (16, 1718)` e 0 unità prima
e dopo.

## Tipi

535 `MISSION_TEXT` · 30 `DESCRIPTION` · 28 `VALUE` · **12 `LOGBOOK`** · 10 `DIALOG` · **10 `UI_LABEL`** ·
0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 10 `UI_LABEL`

Sono tutte `label "..."` di salto, bersagli di `goto`: restano **identiche**, e il `verify.py` le
asserisce una per una.

| idx | riga | label |
|---:|---:|---|
| 204 | 753 | `off limit` |
| 216 | 770 | `final choice` |
| 244 | 832 | `what now` |
| 286 | 942 | `haggled cash` |
| 290 | 951 | `no money` |
| 453 | 1356 | `not anymore` |
| 459 | 1366 | `ask keep ship` |
| 510 | 1499 | `foster end` |
| 569 | 1606 | `bad idea` |
| 576 | 1622 | `desyo end` |

## Le 12 righe `log` (controllo positivo)

| idx | riga | argomenti | contenuto (italiano) |
|---:|---:|---|---|
| 37 | 136 | 1 | legno della chiesa di Midgard, datazione al carbonio |
| 49 | 162 | **3** (`People`, `Albert Foster`) | scheda dell'archeologo |
| 69 | 250 | 1 | ritorno a Midgard, singolarità artificiale |
| 96 | 359 | 1 | la visione a Ildaria |
| 122 | 443 | 1 | Foster e la città sepolta |
| 176 | 653 | 1 | difesa dello scavo dai ladri di antichità |
| 180 | 690 | **3** (`Factions`, `Sheragi`) | voce enciclopedica sugli Sheragi |
| 221 | 783 | 1 | il cubo dati portato a John |
| 409 | 1274 | **3** (`People`, `Desyo`) | scheda di Desyo |
| 410 | 1275 | **3** (`People`, `Rakei`) | scheda di Rakei |
| 411 | 1276 | **3** (`People`, `Eyama`) | scheda di Eyama |
| 605 | 1689 | 1 | la Spada di Smeraldo e il Cannone Fiamma di Drago |

Le cinque a tre argomenti hanno **categoria e nome fuori dall'unità**: restano in inglese nel gioco
(lacuna di `tools/l10n.py`, protetto). Sono tutti nomi propri invarianti, quindi il difetto è cosmetico,
ma è dichiarato in `review.md` §7.

## Le 8 famiglie di token

| token | volte | token | volte |
|---|---:|---|---:|
| `<destination>` | 20 | `<origin>` | 8 |
| `<planet>` | 17 | `<payment>` | 2 |
| `<last>` | 12 | `<capacity>` | 2 |
| `<first>` | 11 | `<system>` | 1 |

## Controlli eseguiti

`check.py` (25 controlli): copertura, unità vuote, `NT` (10 identiche), **righe `log` 12/12 tradotte**,
righe `log` con tab del sorgente, duplicati italiano spiegati dal sorgente, tab per unità e come totale,
tab iniziale conservato, virgolette per unità e come totale, quadre per unità, token `<...>`, backtick,
spazi, rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (37 controlli) **non riusa** la logica di `check.py`: riga grezza contro il file sorgente,
`english`/`kind`/`path` contro `state.db`, stato `PENDING`, id e ordine, collocazione 16–1718, copertura
totale 625/625 da un solo lotto, distribuzione dei kind, 10 `UI_LABEL` tutte in `NT`, **`LOGBOOK` 12 con
identificazione delle 5 a tre argomenti**, assenza di `CONVERSATION` e di quadre, token a parità esatta,
tab e virgolette come totali e per unità, insieme delle 17 virgolette dispari, italiano non vuoto,
caratteri non latini, trattini e virgolette curve, rapporto, ricostruzione di `translation.json` dalle 13
parti con i tab del costruttore.

## Duplicati

15 gruppi di inglese identico per **37 unità su 625**: titoli di missione ripetuti in contesti diversi,
risposte di dialogo, e le due coppie `(Yes.)`/`(No.)` del confronto con Mammon.

| unità | inglese | italiano |
|---|---|---|
| 1, 22, 25, 47, 56 | `Deep Archaeology` | «Archeologia nel Deep» |
| 55, 68 | `You land on <planet>, … hasn't entered the system yet…` | stessa frase, stessa resa |
| 72, 74 | `"For what purpose?"` | «"Con quale scopo?"» |
| 111, 114 | `"I had this dream about dragon-people on Zug."` | «"Ho fatto un sogno su uomini-drago su Zug."» |
| 112, 115, 117 | `"I think a telepathic space alien spoke to me."` | «"Credo che un alieno telepatico dello spazio mi abbia parlato."» |
| 129, 137, 142, 146 | `Archaeological Equipment` | «Attrezzatura archeologica» |
| 130, 143 | `Fetch some excavation equipment…` | stessa resa |
| 152, 156 | `Transport a Xenobiologist` | «Trasporta uno xenobiologo» |
| 274, 465 | `(Yes.)` | «(Sì.)» |
| 275, 466 | `(No.)` | «(No.)» |
| 279, 281 | `"You should know that I don't have that much money to spare."` | stessa resa |
| 282, 288 | `"How about you tell me what I want…"` | stessa resa |
| 283, 287 | `"I need to think about this. Give me some time."` | stessa resa |
| 285, 289 | `"Here's the money."` | «"Ecco i soldi."» |
| 438, 461, 583 | `The Emerald Sword` | «La Spada di Smeraldo» |

## Nota di inventario

Il file ha **12 righe `log`**, di cui **5 a tre argomenti**. L'unità estratta è solo il testo fra
backtick: categoria (`People`, `Factions`) e nome (`Albert Foster`, `Sheragi`, `Desyo`, `Rakei`, `Eyama`)
restano in inglese nel gioco. È lo stesso difetto documentato in L30/L33/L34/L35/L42; qui riguarda solo
nomi propri invarianti.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 625 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo della linea Sheragi.
- Nessun test di gameplay (Deep Archaeology, difesa di Zug, Mammon, recupero della Spada di Smeraldo).
