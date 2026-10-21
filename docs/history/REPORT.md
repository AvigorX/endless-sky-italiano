# Pipeline di localizzazione IT — stato e risultati

Generato: 2026-10-17 11:49 UTC

## 1. Cosa fa il pipeline

Stato in SQLite, batch deterministici, traduzione, validazione meccanica, applicazione su **copia** con verifica strutturale. Il repository di gioco è aperto in sola lettura.

## 2. Numeri

- Unità in inventario: **32924**
- Approvate: **352** (1.069%)
- Parole tradotte: **3530**
- Con caratteri accentati (bloccati dal font attuale): **61**
- Batch: 5

| batch | ambito | unità | stato |
|---|---|---:|---|
| B001 | UI labels (interfaces.txt) | 244 | APPROVED |
| B002 | UI tooltips (sample 40) | 40 | APPROVED |
| B003 | In-game help (part 1/3) | 40 | APPROVED |
| B004 | In-game help (part 2) | 25 | APPROVED |
| B005 | Help smoke test | 3 | APPROVED |

## 3. Validazione

| codice | severità | occorrenze |
|---|---|---:|
| NON_ASCII | warning | 61 |
| GLOSSARY | info | 16 |

Controlli bloccanti: `UNKNOWN_ID`, `EMPTY`, `CONTROL_CHAR`, `BACKTICK`, `DOUBLE_QUOTE`, `PLACEHOLDER_MISMATCH`, `TAB_LOST`, `MISSING_RESULT`, `DUPLICATE_ID`.
Consultivi: `UNTRANSLATED`, `LENGTH_RATIO`, `NON_ASCII`, `GLOSSARY`.

## 4. Integrazione

| file | unità | esito |
|---|---:|---|
| `data/_ui/help.txt` | 68 | OK — 68 lines |
| `data/_ui/interfaces.txt` | 244 | OK — 244 lines |
| `data/_ui/tooltips.txt` | 40 | OK — 40 lines |

Verifica: dopo la sostituzione il file viene ri-tokenizzato e confrontato riga per riga con l'originale. Deve cambiare **un solo token per riga**, con lo stesso delimitatore e lo stesso numero di token. Un fallimento annulla la scrittura del file.

## 5. Limiti (dichiarati)

1. **Il gioco non è stato avviato**: nessuna build disponibile. La validazione è strutturale, non visiva.
2. **Il font non renderizza le lettere accentate** (audit IT-002): i testi sono corretti ma illeggibili finché l'atlante non viene esteso. Il pipeline lo segnala come `NON_ASCII`.
3. **Nessun selettore di lingua** nel motore: l'output è una copia modificata dei dati, non un plugin attivo.
4. La copertura è **0,86%** (lotto pilota): non è una localizzazione completa.
5. I giudizi di qualità linguistica sono miei, non di un revisore umano.

## 6. Prossimo passo

Estendere l'atlante font e il selettore lingua (fase 1 del piano di remediation), poi proseguire con i lotti per famiglia: `_ui/` è già coperto al 26% (284/1089), il resto è `PENDING` e ripartibile con `l10n.py build`.
