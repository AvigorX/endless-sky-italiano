# L40 — rapporto del lotto

`data/human/free worlds side plots.txt` · righe **18–888** · lotto `L40_20261018_124513` ·
**211/211 unità** · ventesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **211 / 211** (file completo) |
| parole | 5.683 EN → **5.339 IT** (0,939) |
| contesti | 19 (`FW Zug Expansion: Assisted` … `FW Greenrock Lost Announcement`) |
| parti | 4 — 66, 46, 54, 45 |
| tab | 133 = 133 |
| virgolette | 352 = 352 (2 unità con conteggio dispari riprodotte: 56, 202) |
| token `<...>` | 59 = 59 |
| quadre `[` `]` | **0 unità** (asserito) |
| rapporto per unità | 0,72 – 1,61 |
| `check.py` | **FAIL totale: 0** (22 controlli) |
| `verify.py` | **29 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `516c1b1a59c9cfe0` · `source.json` `80bf86b574acf133` · `check.py` `b337a546d605f77f` · `verify.py` `2a77265feeec4732` |

**Inizio del file**: le prime unità sono alla **riga 18**, non 16. Il `verify.py` asserisce
`(first, last) == (18, 888)`.

## Tipi

154 `MISSION_TEXT` · 19 `DIALOG` · 15 `VALUE` · 15 `DESCRIPTION` · 7 `LOGBOOK` · **1 `UI_LABEL`** ·
**0 `CONVERSATION`**.

## Unità non traducibili (`NT`)

| idx | testo | riga | perché |
|---|---|---|---|
| 80 | `brower death` | 322 | `label "brower death"`, bersaglio di `goto`: tradurla romperebbe il salto |

È l'unica `UI_LABEL` del file, e il `verify.py` lo asserisce.

## Controlli eseguiti

`check.py` (22 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab per unità e come totale, virgolette per unità e come totale, quadre per unità, token
`<...>`, backtick, spazi iniziali/finali e doppi, rapporto lunghezze, tipografia, caratteri non latini,
parole inglesi residue, stato del database.

`verify.py` (29 controlli): riga grezza contro il file sorgente, `english`/`kind`/`path` contro
`state.db`, stato `PENDING`, id univoci e ordine, collocazione **18–888**, copertura totale 211/211 da un
solo lotto, distribuzione dei kind, `NT` (la sola label 80), **CONVERSATION** (nessuna, asserzione di
assenza), **quadre** (nessuna in entrambe le lingue), token, tab/virgolette/backtick, insieme delle
virgolette dispari (56, 202), italiano non vuoto, caratteri non latini, trattini lunghi, rapporto, e
ricostruzione di `translation.json` dalle 4 parti.

## Nota di inventario

7 righe `log` → 7 unità `LOGBOOK` (1:1). Nessuna lacuna in questo file: l'inventario è completo rispetto
al sorgente. La lacuna generale resta in `tools/l10n.py`, che è protetto.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 211 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo.
- Nessun test delle tre missioni del Branco di Lupi né delle trame secondarie del Conservatorio.
