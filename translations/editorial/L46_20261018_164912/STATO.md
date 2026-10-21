# L46 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L46_20261018_164912` · `data/successors/successor 1 prologue.txt` · righe 24–664 ·
**221/221 unità del segmento**. Il file **non è completo**: conta 345 unità e prosegue fino alla riga
1024 (124 unità dopo la 664). Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 221 unità, 6 contesti (`Successors: Entering the Scar`, `Safe at Last`,
  `First Contact 1`, `First Contact 2 Prompt`, `First Contact 2`, `First Contact 3`), kind
  187 `MISSION_TEXT` / 17 `UI_LABEL` / **9 `LOGBOOK`** / 3 `VALUE` / 3 `DESCRIPTION` / 2 `DIALOG`.
  Nessun `CONVERSATION`, nessun `TEXT`, nessuna quadra, nessun backtick.
- `check.py` derivato da L45 con **`NT` = 18** (17 `UI_LABEL` + 1 categoria di diario), **`LOGBOOK`
  positivo su 8 testi** con identificazione delle **tre forme di `log`** presenti, **asserzioni di
  assenza dichiarate** per `CONVERSATION`, quadre e virgolette dispari, costruttore dei tab riusato.
- 5 parti, tutte a fine contesto: 56 · 47 · 47 · 40 · 31. (Le prime due unità `Entering the Scar` e
  `Safe at Last` sono un contesto di 1 unità ciascuna: si chiudono dentro la parte 01.)
- `translation.json`: 221 unità, 7.180 EN → 6.973 IT (0,971), rapporto per unità 0,74–1,38,
  sha256[:16] `aa71c36e9b399505`.
- `verify.py`: **37 controlli**, `FAIL: 0`, exit 0. Copertura del **segmento** 221/221 (per righe, non per file),
  coppia di righe **(24, 664)**, **0 unità prima / 124 dopo** (segmento interno, non chiusura di file), `NT` 18,
  `LOGBOOK` 8 con le tre forme, assenze dichiarate.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **`NT` = 18, non 18 `UI_LABEL`**: 17 label di salto **più** l'unità 62, che è la categoria `People` di
  un `log "People" "Sieasej" "testo"` con il testo fra virgolette. La categoria resta identica; il testo
  del diario resta fuori dall'unità (lacuna di `tools/l10n.py`, protetto, documentata in `review.md` §2).
- **`LOGBOOK` 9 = 8 testi + 1 categoria.** Le tre forme convivono nel segmento e sono identificate sul
  `raw`: `log "testo"` (19, 21, 98, 100, 197, 204), `log \`testo\`` (25),
  `log "Categoria" "Nome" \`testo\`` (26). Un controllo che assumesse una sola forma sarebbe cieco su due.
- **Tab 175**: nessuna traduzione scritta con `\t`; il costruttore li aggiunge e la parità è verificata
  per unità (175 unità su 221 iniziano con tab).
- **Virgolette 278, tutte in coppia (0 dispari)**: il controllo è l'**insieme vuoto**, dichiarato, non un
  elenco ereditato da L45 (che ne aveva 15).
- **Nessuna quadra, nessun `CONVERSATION`**: asserzioni di assenza **dichiarate** nel `check.py` e
  ripetute nel `verify.py`; un lotto vicino non le rende vere per default.
- **Segmento interno**: `verify.py` asserisce `124` unità dopo la riga 664 e `345` unità nel file. Un
  `verify.py` copiato da L45 (che chiudeva il file) avrebbe asserito «0 dopo» e fallito — correttamente.
- **Lessico nuovo**: ottopodi, Casate Alte, *scions* → **eredi**, `House Sioeora` → **Casa Sioeora**,
  `scion` → **erede**, `translator` → **traduttore** (dispositivo), `iret` invariato (grado onorifico),
  `Kijran-Riitaa` / `Kijra-pet` / `Kijran-Khora` invariati, `Graveyard` invariato (372 occorrenze nel
  corpus contro 49 «Cimitero»), `the scar` → **la cicatrice** (descrittivo, non nome proprio).

## Verifica

```
python staging/editorial/L46_20261018_164912/check.py    → FAIL totale: 0 (27 controlli)
python staging/editorial/L46_20261018_164912/verify.py   → exit 0, 37 controlli, FAIL: 0
```

`state.py` dopo L46: **22.289 unità · 710.563 EN · 674.096 IT**, `ESITO: OK`, `successor 1 prologue.txt`
a **221/345 (64,1%)**, 50 directory con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 221 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: nessuna verifica a schermo dei 6 contesti.
- **Il file non è completo**: restano 124 unità (righe 680–1024, `Kaatrij Monoglot Prompt` … `Trusted`),
  previste in L47.
