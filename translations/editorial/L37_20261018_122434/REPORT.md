# L37 — rapporto del lotto

`data/human/free worlds 3 checkmate.txt` · righe **16–2463** · lotto `L37_20261018_122434` ·
**482/482 unità** · diciassettesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **482 / 482** (file completo) |
| parole | 16.244 EN → **15.239 IT** (0,938) |
| contesti | 37 (`FWC Scouting 1` … `FWC End`) |
| parti | 11 — 49, 60, 38, 63, 59, 56, 36, 31, 30, 37, 23 |
| tab | 305 = 305 |
| virgolette | 900 = 900 (nessuna unità con conteggio dispari) |
| token `<...>` | 121 = 121 |
| quadre `[` `]` | **1 unità** (143): una coppia conservata, testo tradotto integralmente |
| rapporto per unità | 0,77 – 1,62 |
| `check.py` | **FAIL totale: 0** (22 controlli) |
| `verify.py` | **28 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `8a12ed7b7d904c04` · `source.json` `13b7a18d736ceb7a` · `check.py` `bc0b029c2a595ae5` · `verify.py` `a2877ee2119ef450` |

## Tipi

356 `MISSION_TEXT` · 36 `VALUE` · 36 `DESCRIPTION` · 27 `LOGBOOK` · 27 `DIALOG` · **0 `UI_LABEL`**.

## Unità non traducibili (`NT`)

**Nessuna.** Il file non contiene `UI_LABEL`, non ci sono categorie di diario emerse dall'inventario e
nessun riferimento di dato non traducibile. Il `verify.py` asserisce che le `UI_LABEL` siano zero: se ne
comparisse una, `NT` andrebbe rimisurato invece di lasciar passare il lotto.

## Controlli eseguiti

`check.py` (22 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab per unità e come totale, virgolette per unità e come totale, **quadre per unità**, token
`<...>`, backtick, spazi iniziali/finali e doppi, rapporto lunghezze, tipografia, caratteri non latini,
parole inglesi residue, stato del database.

`verify.py` (28 controlli): riga grezza contro il file sorgente, `english`/`kind`/`path` contro
`state.db`, stato `PENDING`, id univoci e ordine, collocazione 16–2463, copertura totale 482/482 da un
solo lotto, distribuzione dei kind, `NT` vuoto con asserzione sulle `UI_LABEL`, **quadre** (la sola 143,
con una coppia conservata), token, tab/virgolette/backtick, insieme delle virgolette dispari (vuoto),
italiano non vuoto, caratteri non latini, trattini lunghi, rapporto, e ricostruzione di
`translation.json` dalle 11 parti.

## Nota di inventario

27 righe `log` → 27 unità `LOGBOOK` (1:1). Nessuna a tre argomenti, nessuna categoria emersa:
l'inventario è completo rispetto al file. La lacuna resta in `tools/l10n.py`, che è protetto e non è
stata toccata.

## Non fatto (dichiarato)

- Nessuna approvazione nel database: 482 unità `PENDING`.
- Nessun caricamento nel gioco, nessuna verifica a schermo.
- Nessun test dei bivi del lotto (testate nucleari accettate o rifiutate; deviazione verso i Quarg).
