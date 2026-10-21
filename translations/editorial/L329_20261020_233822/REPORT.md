# REPORT — L329 (`_ui/help.txt` 119–212) — chiude il file a 113/113

`check.py` **15 controlli, FAIL 0**; `verify.py` **13 controlli, FAIL 0**; `state.db` non toccato (mtime).

## Misure

| | EN | IT |
|---|---|---|
| 60 unità `HELP` (15 approvate + 45 tradotte) | 1.322 parole | **1.265** (0,957) |
| tab | 6 | 6 (righe 124,125,126,129,130,147) |
| virgolette | 38 | 38 |
| segnaposto | 14 in 12 forme | 14, identici |

`data/_ui/help.txt`: **113/113 unità**, tre lotti (L327 28 approvate, L328 25 approvate, L329 15 approvate + 45 `PENDING`).

## Contenuto tradotto (45 unità)

| contesto | righe | che cosa |
|---|---|---|
| `fighters transfer cargo` | 140, 142 | la preferenza che fa trasferire il carico dai caccia alla portaerei |
| `navigation` | 151–153 | il salto si compie al **rilascio** del tasto (per far saltare le scorte insieme), atterraggio col tasto dedicato, niente collisioni con asteroidi |
| `outfitter` | 156–160 | spazio equipaggiamenti, **capacità motori/armi**, porto per cannoni, punto di montaggio per torretta; Shift/Control/Alt = 5/20/500; `F` per cercare |
| `shipyard` | 163–167 | idem, più `B`/`S`/`R` (comprare, vendere, vendere trattenendo gli equipaggiamenti) |
| `cargo management` | 170–178 | le sei scorciatoie `B`/`S`/`I`/`U`/`C`/`R` e l'ordine di priorità stiva → deposito → nave |
| `uninstalling and storage` | 181–184 | il deposito planetario e la **ricompra immediata allo stesso prezzo** |
| `outfitter with multiple ships` | 187–190 | Ctrl/Shift+clic sulle navi, gruppi di controllo |
| `stranded` | 193–194 | senza carburante in un sistema disabitato: chiamare una nave amica (più facile se sei quasi fermo) |
| `trading` | 197–199 | pannello commercio, moltiplicatori 5/20/500, «Vendi materiali» / «Vendi equipaggiamenti» |
| `friendly disabled` | 202 | abbordare una nave amica in avaria **senza fuoco incrociato** |
| `control ship with mouse` | 205–212 | prua verso il puntatore, `<Forward thrust>`, `<Reverse>`, clic destro, `<Mouse turning (hold)>`, comando «vai e mantieni la posizione» spostato al tasto centrale |

## Scelte

- **`outfitter` → «fornitore»** (7 unità), coerente col testo approvato dello stesso file; nessun «emporio».
- **Etichette tradotte**: «I caccia trasferiscono il carico», «Vendi materiali», «Vendi equipaggiamenti», «vai e mantieni la posizione».
- **`[buy]`/`[sell]`** → **[compra]/[vendi]**: sono le etichette dei pulsanti del pannello.
- **Tasti letterali**: `B`, `S`, `I`, `U`, `C`, `R`, `F`, `Shift`, `Control`, `Alt`, `Ctrl`, e i segnaposto `<…>` **identici**.

## Non verificato

Nessuna approvazione (45 `PENDING` invariate), nessun testo visto nel gioco, nessuna revisione umana.
