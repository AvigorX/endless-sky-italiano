# L38 — rapporto del lotto

`data/human/free worlds 3 reconciliation.txt` · righe **31–2729** · lotto `L38_20261018_123202` ·
**596/596 unità** · diciottesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **596 / 596** (file completo) |
| parole | 21.021 EN → **20.228 IT** (0,962) |
| contesti | 51 (`FW Reconciliation 1` … `FW Syndicate Extremists 1C`) |
| parti | 14 — 58, 42, 40, 29, 32, 33, 51, 57, 42, 35, 38, 61, 40, 38 |
| tab | 361 = 361 |
| virgolette | 1.004 = 1.004 (2 unità con conteggio dispari riprodotte: 45, 546) |
| token `<...>` | 119 = 119 |
| quadre `[` `]` | **1 unità** (426): una coppia conservata, testo tradotto integralmente |
| rapporto per unità | 0,74 – 1,80 |
| `check.py` | **FAIL totale: 0** (22 controlli) |
| `verify.py` | **29 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `1cda2e18fc38b163` · `source.json` `983643fa239d1f96` · `check.py` `86091efbbfe04a04` · `verify.py` `b788d605c21be553` |

**Inizio del file**: le prime unità sono alla **riga 31**, non 16 (le righe 1–30 sono intestazione e
blocchi `mission` senza testo traducibile). Il `verify.py` asserisce `(first, last) == (31, 2729)`.

## Tipi

425 `MISSION_TEXT` · 42 `VALUE` · 42 `DESCRIPTION` · 41 `LOGBOOK` · 35 `DIALOG` · **2 `UI_LABEL`** ·
**9 `CONVERSATION`**.

Le 9 `CONVERSATION` sono il blocco unico 403–411 (la visita al Cantiere della Marina su Geminus): un
dialogo continuo con il supervisore, gli ingegneri e Freya. Tradotte come testo normale; il `verify.py`
asserisce che siano 9 e tutte non vuote.

## Unità non traducibili (`NT`)

| idx | testo | riga | perché |
|---|---|---|---|
| 139 | `star queen` | 599 | `label "star queen"`, bersaglio di `goto`: tradurla romperebbe il salto |
| 308 | `planet dweller questions` | 1438 | `label`, bersaglio di `goto` |

Le due `UI_LABEL` del file sono **esattamente queste**: il `verify.py` lo asserisce, così un cambio di
inventario rende il lotto rosso invece di passare inosservato.

## Controlli eseguiti

`check.py` (22 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab per unità e come totale, virgolette per unità e come totale, **quadre per unità**, token
`<...>`, backtick, spazi iniziali/finali e doppi, rapporto lunghezze, tipografia, caratteri non latini,
parole inglesi residue, stato del database.

`verify.py` (29 controlli): riga grezza contro il file sorgente, `english`/`kind`/`path` contro
`state.db`, stato `PENDING`, id univoci e ordine, collocazione **31–2729**, copertura totale 596/596 da un
solo lotto, distribuzione dei kind, `NT` con asserzione sulle due `UI_LABEL`, **quadre** (la sola 426,
con una coppia conservata), **CONVERSATION** (9, tutte tradotte), token, tab/virgolette/backtick, insieme
delle virgolette dispari, italiano non vuoto, caratteri non latini, trattini lunghi, rapporto, e
ricostruzione di `translation.json` dalle 14 parti.

## Nota di inventario

41 righe `log` → 41 unità `LOGBOOK` (1:1). Nessuna a tre argomenti, nessuna categoria emersa:
l'inventario è completo rispetto al file. La lacuna resta in `tools/l10n.py`, che è protetto.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 596 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo.
- Nessun test dei bivi del lotto (andare o no nel Sindacato; deviazione verso i Quarg o il Deep).
