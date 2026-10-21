# L48 — rapporto del lotto

`data/avgi/avgi side missions.txt` · righe **26–499** · lotto `L48_20261018_170232` ·
**180/180 unità del segmento** · file **non completo** (436 unità totali, 256 dopo la riga 499) ·
chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **180 / 180** del segmento; file a **180 / 436** (41,3%) |
| parole | 5.627 EN → **5.297 IT** (0,941) |
| contesti | 2 (`Avgi Culture: Park Politics` 1–157, `Avgi Culture: Zapchannel Energy` 158–180) |
| parti | 4 — 45 · 45 · 45 · 45 |
| tab | **145 = 145** (145 unità che iniziano con tab) |
| virgolette | **252 = 252** |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **10 = 10** (4 famiglie: `<first>` 3, `<last>` 5, `<origin>` 1, `<ship>` 1) |
| quadre `[` `]` | **0 unità** (asserzione di assenza dichiarata) |
| `LOGBOOK` | **14**, tutte di testo (11 a tre argomenti, 3 dirette) |
| `CONVERSATION` / `DIALOG` / `VALUE` / `DESCRIPTION` | **0 / 0 / 0 / 0** (assenze dichiarate) |
| rapporto per unità | 0,60 – 1,30 |
| `check.py` | **FAIL totale: 0** (30 controlli) |
| `verify.py` | **40 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `fcb07ed0909aeb65` · `source.json` `98a4649210ab326a` · `check.py` `6e585a7100a0d5eb` · `verify.py` `426d4a26031b7887` |

Segmento **interno**: `verify.py` asserisce `(first, last) == (26, 499)`, `0` unità prima della 26 e
**`256` dopo la 499**.

## Tipi

152 `MISSION_TEXT` · 14 `UI_LABEL` · **14 `LOGBOOK`** · 0 `VALUE` · 0 `DESCRIPTION` · 0 `DIALOG` ·
0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 14

| idx | riga | label |
|---:|---:|---|
| 28 | 75 | `block wisteria 1` |
| 30 | 81 | `block foil 1` |
| 37 | 103 | `block wisteria 2` |
| 39 | 109 | `escape foil 2` |
| 46 | 129 | `hard life` |
| 61 | 185 | `block wisteria 3a` |
| 63 | 191 | `block wisteria 3b` |
| 65 | 197 | `block wisteria 3c` |
| 67 | 203 | `block foil 3` |
| 76 | 228 | `another way` |
| 94 | 263 | `next assembly` |
| 116 | 304 | `break wall 4a` |
| 118 | 310 | `break wall 4b` |
| 121 | 322 | `block wisteria 4` |

**Nessun riferimento di dato**: in questo lotto tutte le righe `LOGBOOK` hanno il testo estratto (fra
backtick), quindi non c'è nessuna categoria da lasciare in inglese.

## Le 14 righe `log` — tutte di testo

| idx | riga | forma | contenuto |
|---:|---:|---|---|
| 84 | 244 | 3 argomenti | le entità politiche Avgi e la Consonanza |
| 90 | 254 | 3 argomenti | gli Elettori, eletti e non |
| 99 | 274 | 3 argomenti | le fazioni dell'Assemblea |
| 100 | 275 | 3 argomenti | i Centralisti |
| 101 | 276 | 3 argomenti | i Tecnocrati |
| 102 | 277 | 3 argomenti | i Finanzieri |
| 103 | 278 | 3 argomenti | i Nazionalisti |
| 104 | 279 | 3 argomenti | gli Ecologisti |
| 105 | 280 | 3 argomenti | gli Indipendenti |
| 152 | 426 | diretta | la partita a Trefoil con Wisteria |
| 153 | 427 | 3 argomenti | la scheda di Wisteria |
| 158 | 445 | 3 argomenti | la scheda di Nikkio |
| 176 | 490 | diretta | il campione accettato (superpoteri) |
| 179 | 498 | diretta | l'offerta rifiutata |

## Verifica

```
python staging/editorial/L48_20261018_170232/check.py    → FAIL totale: 0
python staging/editorial/L48_20261018_170232/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **22.593 unità · 720.318 EN · 683.425 IT** in staging, 52 directory con
`translation.json`, integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 180 unità `PENDING`.
- **Nessun caricamento nel gioco**: la partita a Trefoil e la scena di Nikkio non sono mai state viste a
  schermo.
- **Il file resta aperto**: 256 unità (righe 524–1117) previste in L49.
