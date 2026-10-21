# Lacuna dell'estrattore sulle news — stato reale, causa, intervento minimo

Fase: revisione post-traduzione. Data: 2026-10-21.
Nessun file dell'estrattore è stato modificato. `state.db` non è stato scritto.

## 1. Cosa diceva la consegna, cosa risulta misurato

La consegna dichiarava che cinque file di news producevano come unità «soltanto il carattere `.`».
Misura: le unità prodotte sono il carattere `"` (virgolette), **non** `.`, e la lacuna è molto più
ampia — non riguarda solo quei cinque file.

| file | unità estratte | di cui `"` | righe-testo non estratte | parole non estratte |
|---|---:|---:|---:|---:|
| `data/human/news.txt` | 202 | 26 | 1 320 | 20 438 |
| `data/hai/hai news.txt` | 46 | 46 | 246 | 4 146 |
| `data/wanderer/wanderer news.txt` | 24 | 24 | 115 | 1 771 |
| `data/remnant/remnant news.txt` | 8 | 8 | 213 | 413 |
| `data/korath/korath news.txt` | 2 | 2 | 44 | 669 |
| `data/successors/successor news.txt` | 14 | 2 | 123 | 1 173 |

Totale: **2 061 righe di testo non estratte, 28 610 parole** (2,9% delle 979 975 parole dell'inventario).

Ripartizione per blocco (misurata, `review/gap_extractor_by_block.txt`):

| blocco contenitore | righe | parole | natura |
|---|---:|---:|---|
| `message > word` | 1 577 | 27 974 | corpo delle notizie: testo visibile al giocatore |
| `name > word` | 344 | 633 | nome del personaggio che parla: visibile |
| `phrase > word` | 144 | 521 | parole composte in frasi: in parte tecniche (`00`…`07` dell'orologio Remnant) |
| `phrase > phrase`, `message > phrase`, `name > phrase` | 34 | 79 | **riferimenti** ad altri oggetti `phrase`: non sono testo |

Quindi: **2 065 righe / 29 128 parole di testo effettivo**, più 34 righe di riferimenti da non toccare.

## 2. Causa dimostrata

Il tokenizer di `endless-sky-l10n-audit/tools/l10n_inventory.py` (`tokenize`, righe 64-87) spezza la riga in
token; poi (righe 213-230) costruisce i candidati così:

```python
bt = [t for t in toks if t[1] == "backtick"]
values = [t for t in toks[1:] if t[1] in ("quoted", "backtick")]
if bt:
    candidates.extend((t[0], "backtick") for t in bt)
elif key in TEXT_KEYS and values and not is_phrase_ref:
    ...
```

Due difetti, entrambi necessari:

1. **Manca il caso "riga = una sola stringa, senza chiave".** Le news sono scritte così:

   ```
   news "food in Hai space"
       message
           word
               `"`                              <- separatore: unica cosa estratta oggi
           word
               "This may sound odd, but the acorn..."   <- corpo: MAI estratto
   ```

   La riga del corpo ha un solo token, di tipo `quoted`; `key` diventa il testo stesso, `values` è vuoto,
   nessun ramo scatta → l'unità non nasce.

2. **`if bt:` scarta tutto il resto della riga** quando c'è un backtick: è il motivo per cui le unità
   estratte sono esattamente il carattere `"`.

Prova che la causa è questa e non una mancata copertura: i file con la stessa struttura ma senza `word`
interposto (missioni, dialoghi) sono coperti al 100%; le righe mancanti sono tutte e sole quelle con un
unico token stringa.

## 3. Intervento minimo proposto (NON applicato)

Una sola modifica in `l10n_inventory.py`, prima del ramo `if bt:` (riga 223), più l'uso della chiave del
blocco contenitore per `kind` e per l'`unit_id`:

```python
                # Una riga composta da UNA sola stringa non ha chiave: è un'alternativa
                # del blocco contenitore (`word`, `sentence`). Le news e gli hail sono
                # costruiti così. Una stringa sola dentro `phrase` è invece un
                # riferimento a un altro oggetto phrase, non testo.
                value_only = len(toks) == 1 and toks[0][1] in ("quoted", "backtick")
                parent_key = stack[-1][1] if stack else ""
                if value_only and parent_key != "phrase":
                    candidates.append((toks[0][0], toks[0][1]))
                elif bt:
                    candidates.extend((t[0], "backtick") for t in bt)
```

e, nel ciclo `for idx, (text, how) in enumerate(candidates):`:

```python
-                    kind = "VALUE" if key in NAME_KEYS else kind_for(key, ptype, pname)
+                    eff_key = parent_key if value_only else key
+                    kind = "VALUE" if key in NAME_KEYS else kind_for(eff_key, ptype, pname)
...
-                    unit_id = f"{ctx}|{key}|{lineno}|{idx}"
+                    unit_id = f"{ctx}|{eff_key}|{lineno}|{idx}"
```

Con questa condizione i 34 riferimenti (`phrase > phrase`, `message > phrase`, `name > phrase`) restano
esclusi automaticamente, perché il loro parent immediato è `phrase`.

## 4. Perché non è stato applicato

- `l10n_inventory.py` genera `LOCALIZATION_COVERAGE.csv`, da cui `tools/l10n.py init` costruisce
  `state.db` — che è nella lista dei **file protetti** (`staging/editorial/tools/protected.sha256`, sha
  verificato integro in questa fase). Rigenerare l'inventario impone di riscrivere `state.db`.
- Il mandato di questa fase vieta di scrivere in `state.db` e di approvare unità, e impone di fermarsi
  prima di modificare l'estrattore.
- Le nuove unità non esistono oggi in nessuna forma: inventarne gli ID a mano significherebbe creare unità
  che il prossimo `init` non riconoscerebbe.

## 5. Rischio per la build

| conseguenza | gravità | nota |
|---|---|---|
| le notizie e le frasi degli hail dei 6 file restano **in inglese** nel gioco | media | è il 2,9% delle parole; il resto della localizzazione non ne è toccato |
| la build non si blocca | — | `apply_translations.py` sostituisce solo le unità presenti in staging e salta quelle identiche; le righe mancanti non vengono toccate |
| copertura dichiarata | alta | la copertura «per ID» è vera ma **non** è copertura del testo: il denominatore attuale non contiene quelle 2 065 righe |
| frammenti con interpolazione | media | in `remnant news.txt` alcune alternative sono frammenti (`Incoming Korath Fleet in ` + `${00-07} days`): tradurli come frasi intere romperebbe la composizione |

**Decisione richiesta:** autorizzare la modifica all'estrattore e la rigenerazione dell'inventario
(con nuovo `state.db`), oppure accettare la lacuna e dichiararla nella copertura. In questa fase la lacuna
resta **documentata come blocco noto**, non risolta.
