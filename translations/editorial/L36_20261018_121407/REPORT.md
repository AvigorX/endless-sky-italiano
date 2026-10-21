# L36 — rapporto del lotto

`data/human/free worlds 2 middle.txt` · righe **16–2336** · lotto `L36_20261018_121407` ·
**552/552 unità** · sedicesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **552 / 552** (file completo) |
| parole | 16.290 EN → **15.323 IT** (0,941) |
| contesti | 52 (`FW Diplomacy 1` … `FW Liberate Delta Sagittarii`) |
| parti | 11 — 71, 51, 41, 44, 50, 61, 68, 54, 31, 67, 14 |
| tab | 341 = 341 |
| virgolette | 919 = 919 (3 unità con conteggio dispari riprodotte: 76, 77, 355) |
| token `<...>` | 139 = 139 |
| parentesi quadre `[a, b]` | **0 unità** (asserito nel `verify.py`) |
| rapporto per unità | 0,75 – 1,65 |
| `check.py` | **FAIL totale: 0** (21 controlli) |
| `verify.py` | **27 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `502a8f740d9181e9` · `source.json` `a9217b4b08f3d131` · `check.py` `af014c29fde595fd` · `verify.py` `a6f741cb06e7aa38` |

## Tipi

396 `MISSION_TEXT` · 46 `VALUE` · 45 `DESCRIPTION` · 39 `DIALOG` · 23 `LOGBOOK` · 3 `UI_LABEL`.

## Unità non traducibili (`NT`)

| idx | testo | riga | perché |
|---|---|---|---|
| 407 | `me too` | 1791 | `label "me too"`, bersaglio di `goto`: tradurla romperebbe il salto |
| 501 | `definitely surrender` | 2187 | `label`, bersaglio di `goto` |
| 503 | `definitely rescue` | 2193 | `label`, bersaglio di `goto` |

Le tre `UI_LABEL` del file sono **esattamente queste**: il `verify.py` lo asserisce, così un cambio di
inventario rende il lotto rosso invece di passare inosservato.

## Controlli eseguiti

`check.py` (21 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab per unità e come totale, virgolette per unità e come totale, token `<...>`, backtick,
spazi iniziali/finali e doppi, rapporto lunghezze, tipografia, caratteri non latini, parole inglesi
residue, stato del database.

`verify.py` (27 controlli): riga grezza contro il file sorgente, `english`/`kind`/`path` contro
`state.db`, stato `PENDING`, id univoci e ordine, collocazione 16–2336, copertura totale 552/552 da un
solo lotto, distribuzione dei kind, `NT`, 0 parentesi quadre, token, tab/virgolette/backtick, insieme
delle virgolette dispari, italiano non vuoto, caratteri non latini, trattini lunghi, rapporto, e
ricostruzione di `translation.json` dalle 11 parti.

## Nota di inventario

23 righe `log` → 23 unità `LOGBOOK` (1:1). **Nessuna** ha la forma a tre argomenti e **nessuna** ha
prodotto una categoria: in questo file l'inventario non perde niente. La lacuna resta in
`tools/l10n.py`, che è protetto e non è stata toccata.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 552 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo.
- Nessun test dei due bivi del lotto (prigionieri rilasciati o tenuti; Bloodsea diplomatica o invasa).
