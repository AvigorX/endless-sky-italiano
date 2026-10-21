# L47 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L47_20261018_165449` · `data/successors/successor 1 prologue.txt` · righe 680–1024 ·
**124/124 unità**. Con L46 (**221**) il file è a **345/345**: **ventiseiesimo file completo** dello
staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 124 unità, 3 contesti (`Successors: Kaatrij Monoglot Prompt`,
  `Kaatrij First Contact`, `Trusted`), kind 108 `MISSION_TEXT` / 8 `UI_LABEL` / **4 `LOGBOOK`** /
  2 `VALUE` / 2 `DESCRIPTION`. Nessun `DIALOG`, nessun `CONVERSATION`, nessun `TEXT`.
- `check.py` derivato da L46 con **`NT` = 9** (8 `UI_LABEL` + 1 categoria di diario), **`LOGBOOK`
  positivo su 3 testi** con **due forme** identificate sul `raw`, **1 unità con quadre** (21), **2
  virgolette dispari** (46, 63), asserzione di assenza `CONVERSATION`.
- 3 parti: 45 · 40 · 39.
- `translation.json`: 124 unità, 4.128 EN → 4.032 IT (0,977), rapporto per unità 0,70–1,69,
  sha256[:16] `d783356009cbb44d`.
- `verify.py`: **38 controlli**, `FAIL: 0`, exit 0. Copertura del **file** 345/345 su **due lotti**
  (L46 221 + L47 124), coppia di righe **(680, 1024)**, **221 unità prima / 0 dopo** (fine file),
  `NT` 9, `LOGBOOK` 3 con le due forme, quadre per unità, insieme delle 2 virgolette dispari.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **`NT` = 9**: 8 label di salto **più** l'unità 54, categoria `People` di un
  `log "People" "Saajret, of Somber Sejra" "testo"` con il testo fra virgolette. Categoria identica,
  testo del diario fuori dall'unità (lacuna di `tools/l10n.py`, protetta, `review.md` §2).
- **`LOGBOOK` 4 = 3 testi + 1 categoria.** Due forme nel segmento: `log "testo"` (59, 67) e
  `log "Categoria" "Nome" \`testo\`` (68). Il `verify.py` le identifica entrambe sul `raw`.
- **Tab 102 caratteri su 100 unità** (98 con un tab iniziale, 2 con due): il costruttore antepone i tab
  del sorgente, le parti si scrivono senza. Parità verificata per unità.
- **2 virgolette dispari** (46, 63): battute aperte nel sorgente, riprodotte aperte; confronto come
  insieme di idx.
- **1 unità con quadre** (21): `HOUSE KAATRIJ [REQUESTS, REQUIRES] AUDIENCE OF HUMAN CAPTAIN`, annuncio
  in maiuscolo. Conteggio di `[` e `]` invariato per unità.
- **Duplicato italiano non giustificato dal sorgente, corretto**: le unità 94 e 103 erano rese identiche
  («Casa Sioeora. Casa Chydiyi vede bene…»), ma l'inglese differisce solo nel vocativo
  (`House Sioeora.` / `House Kaatrij.`). Il `check.py` l'ha segnalato sul lotto completo; 103 è stata
  corretta in **«Casa Kaatrij.»**. Il difetto era **reale**, non dello strumento.
- **Lessico**: `Old and New Houses` → **Casate Vecchie e Casate Nuove**, `House Sejra` → **Casa Sejra**
  (caduta), `Jaasii`/`Vejret`/`Ijridanii` invariati, `Coalition` invariato, `Hai` invariato,
  `Tempest` → **la Tempesta**, `pin of tongues` → **spilla da traduzione**, `petty technologies` →
  **tecnologie minori**, `device of tongues` → **dispositivo delle lingue**.

## Verifica

```
python staging/editorial/L47_20261018_165449/check.py    → FAIL totale: 0 (26 controlli)
python staging/editorial/L47_20261018_165449/verify.py   → exit 0, 38 controlli, FAIL: 0
```

`state.py` dopo L47: **22.413 unità · 714.691 EN · 678.128 IT**, `ESITO: OK`,
`successor 1 prologue.txt` a **345/345 (100%, 2 lotti)**, 51 directory con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 345 unità del file sono `PENDING`.
- **Nessun caricamento nel gioco**: nessuna verifica a schermo dei dialoghi al consiglio delle Casate.
- **Nessun test di gameplay** della linea Successors.
