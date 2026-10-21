# L43 — rapporto del lotto

`data/remnant/remnant 2 side missions.txt` · righe **17–775** · lotto `L43_20261018_160846` ·
**299/299 unità** · ventitreesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **299 / 299** (file completo) |
| parole | 10.539 EN → **9.870 IT** (0,936) |
| contesti | 11 (`Remnant: Visit to Paradise 1` … `Remnant: Will Not Someone Please Think Of The Children`) |
| parti | 8 — 41, 30, 38, 39, 36, 45, 29, 41 |
| tab | **208 = 208** (208 unità che iniziano con tab) |
| virgolette | **445 = 445** |
| virgolette dispari | **11 unità** (133, 188, 190, 225, 227, 229, 245, 247, 280, 285, 286), stessi idx in italiano |
| token `<...>` | **47 = 47** (9 famiglie) |
| quadre `[` `]` | **0 unità** (asserito) |
| `LOGBOOK` / `CONVERSATION` | **0 / 0** (asserzioni di assenza) |
| rapporto per unità | 0,65 – 1,40 |
| `check.py` | **FAIL totale: 0** (21 controlli) |
| `verify.py` | **33 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `018217f1aac1ba49` · `source.json` `7ab3e03cffff70db` · `check.py` `c2e4fca2916cc572` · `verify.py` `590829623fcb9152` |

Il file parte dalla riga **17**; il `verify.py` asserisce `(first, last) == (17, 775)` e 0 unità prima
e dopo.

## Tipi

235 `MISSION_TEXT` · **36 `UI_LABEL`** · 10 `VALUE` · 10 `DESCRIPTION` · 8 `DIALOG` · 0 `LOGBOOK` ·
0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 36 `UI_LABEL`

Sono tutte `label "..."` di salto, bersagli di `goto`: restano **identiche**, e il `verify.py` le
asserisce una per una. Due compaiono due volte ciascuna (`shattered help` 226/253, `rather not`
268/291), perché servono due rami diversi della stessa conversazione.

| idx | label | idx | label |
|---:|---|---:|---|
| 10 | `vail later` | 135 | `ceremony omitted` |
| 12 | `ask question` | 137 | `celebration crime` |
| 18 | `vail fun` | 139 | `ask crying` |
| 22 | `vail landing` | 142 | `celebration request` |
| 27 | `have hoverboarded` | 164 | `emp no` |
| 29 | `vail head home` | 207 | `living ship` |
| 46 | `our destination` | 209 | `drop success` |
| 52 | `question loop` | 212 | `living clear` |
| 58 | `wood products` | 226 | `shattered help` |
| 60 | `camel cart` | 253 | `shattered help` |
| 64 | `stone walls` | 255 | `shattered request` |
| 67 | `wind turbine` | 262 | `scent ssil vida` |
| 69 | `main return` | 264 | `scent of rain choice` |
| 79 | `celebration declined` | 268 | `rather not` |
| 81 | `celebration definition` | 281 | `scanning payment` |
| 85 | `celebration attendance` | 291 | `rather not` |
| 89 | `celebration begin` | | |
| 122 | `celebration questions` | | |
| 130 | `celebration rehearsed` | | |
| 132 | `ceremony leader` | | |

## Le 9 famiglie di token

| token | volte | token | volte |
|---|---:|---|---:|
| `<first>` | 20 | `<planet>` | 2 |
| `<ship>` | 11 | `<last>` | 2 |
| `<destination>` | 6 | `<stopovers>` | 1 |
| `<payment>` | 3 | `<origin>` | 1 |
| | | `<waypoints>` | 1 |

## Controlli eseguiti

`check.py` (21 controlli): copertura, unità vuote, `NT` (36 identiche), duplicati italiano spiegati dal
sorgente, tab per unità e come totale, tab iniziale conservato, virgolette per unità e come totale,
quadre per unità, token `<...>`, backtick, spazi, rapporto lunghezze, tipografia, caratteri non latini,
parole inglesi residue, stato del database.

`verify.py` (33 controlli) **non riusa** la logica di `check.py`: riga grezza contro il file sorgente,
`english`/`kind`/`path` contro `state.db`, stato `PENDING`, id e ordine, collocazione 17–775, copertura
totale 299/299 da un solo lotto, distribuzione dei kind, 36 `UI_LABEL` tutte in `NT`, **assenza di
`LOGBOOK` e `CONVERSATION`**, assenza di quadre, token a parità esatta, tab e virgolette come totali e
per unità, insieme delle 11 virgolette dispari, italiano non vuoto, caratteri non latini, trattini e
virgolette curve, rapporto, ricostruzione di `translation.json` dalle 8 parti con i tab del costruttore.

## Duplicati

9 gruppi di inglese identico per **22 unità su 299**: sono risposte di dialogo, il battito dei tamburi
(`Thump.` ×4, `Thump-thump.` ×4) e due nomi di missione ripetuti in contesti diversi.

| unità | inglese | italiano |
|---|---|---|
| 42, 161 | `Thanks for the explanation.` | «Grazie della spiegazione.» |
| 76, 83 | `Yes, I would.` | «Sì, mi va.» |
| 78, 84 | `No thanks.` | «No, grazie.» |
| 94, 95, 96, 97 | `Thump.` | «Tump.» |
| 102, 103, 104, 105 | `Thump-thump.` | «Tump-tump.» |
| 144, 153 | `Yes.` | «Sì.» |
| 202, 233 | `Shattered Light` | «Shattered Light» |
| 226, 253 | `shattered help` | `shattered help` (label) |
| 268, 291 | `rather not` | `rather not` (label) |

## Nota di inventario

Il file **non ha righe `log`**: 0 `LOGBOOK`. Nessuna lacuna di inventario possibile; è la stessa
condizione di L41 ed è una misura, non un'omissione del controllo (il `verify.py` asserisce `log == []`).

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 299 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo della Celebrazione né delle due missioni
  Shattered Light.
- Nessun test di gameplay delle trame secondarie Remnant.
