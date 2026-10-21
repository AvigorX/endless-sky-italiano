# L39 — rapporto del lotto

`data/human/free worlds 4 epilogue.txt` · righe **22–341** · lotto `L39_20261018_124057` ·
**114/114 unità** · diciannovesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **114 / 114** (file completo) |
| parole | 3.487 EN → **3.209 IT** (0,920) |
| contesti | 6 (`FW Epilogue: Ijs and Katya` … `edward epilogue`) |
| parti | 2 — 63, 51 |
| tab | 105 = 105 |
| virgolette | 258 = 258 (nessuna unità con conteggio dispari) |
| token `<...>` | 16 = 16 |
| quadre `[` `]` | **0 unità** (asserito: nessuna nel sorgente, nessuna nell'italiano) |
| rapporto per unità | 0,72 – 1,50 |
| `check.py` | **FAIL totale: 0** (22 controlli) |
| `verify.py` | **29 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `b41df1b6b2b9dec7` · `source.json` `41d281ecc10a6a3c` · `check.py` `2c9d5707bfb2178b` · `verify.py` `d2e166d3642e221c` |

**Inizio del file**: le prime unità sono alla **riga 22**, non 16 (le righe 1–21 sono intestazione senza
testo traducibile). Il `verify.py` asserisce `(first, last) == (22, 341)`.

## Tipi

77 `MISSION_TEXT` · **34 `CONVERSATION`** · 1 `VALUE` · 1 `DESCRIPTION` · 1 `LOGBOOK` · **0 `UI_LABEL`**.

Le 34 `CONVERSATION` coprono l'intero secondo atto del file (unità 81–114, `edward epilogue`): la visita a
Barmy Edward alla Kraz Cybernetics, la prova dell'arma e la serata al bar. È il lotto con la più alta
percentuale di questo tipo dell'intera serie (30% delle unità). Tradotte come dialogo continuo; il
`verify.py` asserisce che siano 34 e tutte non vuote.

## Unità non traducibili (`NT`)

**Nessuna.** Il file non contiene `UI_LABEL`, non ci sono categorie di diario emerse dall'inventario e
nessun riferimento di dato non traducibile. Il `verify.py` asserisce che le `UI_LABEL` siano zero: se ne
comparisse una, `NT` andrebbe rimisurato invece di lasciar passare il lotto.

## Controlli eseguiti

`check.py` (22 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab per unità e come totale, virgolette per unità e come totale, quadre per unità, token
`<...>`, backtick, spazi iniziali/finali e doppi, rapporto lunghezze, tipografia, caratteri non latini,
parole inglesi residue, stato del database.

`verify.py` (29 controlli): riga grezza contro il file sorgente, `english`/`kind`/`path` contro
`state.db`, stato `PENDING`, id univoci e ordine, collocazione **22–341**, copertura totale 114/114 da un
solo lotto, distribuzione dei kind, `NT` con asserzione sulle `UI_LABEL` (zero), **CONVERSATION** (34,
tutte tradotte), **quadre** (nessuna, in entrambe le lingue), token, tab/virgolette/backtick, insieme
delle virgolette dispari (vuoto), italiano non vuoto, caratteri non latini, trattini lunghi, rapporto, e
ricostruzione di `translation.json` dalle 2 parti.

## Nota di inventario

1 riga `log` → 1 unità `LOGBOOK`. Nessuna lacuna in questo file: l'inventario è completo rispetto al
sorgente. La lacuna generale resta in `tools/l10n.py`, che è protetto.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 114 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo.
- Nessun test delle quattro visite facoltative dell'epilogo.
