# L48 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L48_20261018_170232` · `data/avgi/avgi side missions.txt` · righe 26–499 · **180/180 unità del
segmento**. Il file **non è completo**: conta 436 unità e prosegue fino alla riga 1117 (256 restano dopo
la 499). Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 180 unità, 2 contesti (`Avgi Culture: Park Politics` 1–157, `Avgi Culture: Zapchannel
  Energy` 158–180), kind 152 `MISSION_TEXT` / 14 `UI_LABEL` / **14 `LOGBOOK`**. Nessun `VALUE`,
  `DESCRIPTION`, `DIALOG`, `CONVERSATION`, `TEXT`.
- `check.py` derivato da L47 con **`NT` = 14** (solo `UI_LABEL`), **`LOGBOOK` positivo su 14 testi**,
  **tre assenze dichiarate** (`CONVERSATION`, `DIALOG`, `VALUE`, `DESCRIPTION`), **0 virgolette dispari,
  0 quadre** come asserzioni, costruttore dei tab.
- 4 parti: 45 · 45 · 45 · 45.
- `translation.json`: 180 unità, 5.627 EN → 5.297 IT (0,941), rapporto per unità 0,60–1,30,
  sha256[:16] `fcb07ed0909aeb65`.
- `verify.py`: **40 controlli**, `FAIL: 0`, exit 0. Copertura del **segmento** 180/180 (per righe), coppia
  **(26, 499)**, **0 unità prima / 256 dopo**, `NT` 14, `LOGBOOK` 14 (11 a tre argomenti + 3 dirette),
  nessuna categoria estratta.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Prima incursione nella linea Avgi**: la voce è costruita qui e registrata in `review.md`. La
  convenzione più evidente è che gli Avgi **etichettano ogni frase con la propria modalità** («Curiosità.»,
  «Divertimento.», «Approvazione.») e chiudono le domande con **«, domanda?»**. È stata riprodotta
  fedelmente, non normalizzata.
- **`NT` = 14 label, nessun riferimento di dato**: in questo lotto `tools/l10n.py` ha estratto il testo di
  tutte le 14 righe `LOGBOOK` (testo fra backtick). È il **primo lotto della serie in cui la lacuna
  dell'estrattore non si presenta**, e il `check.py` lo asserisce (`14 LOGBOOK = 14 testi`).
- **Tab 145**, virgolette **252**, token **10** su 4 famiglie: parità per unità su tutti.
- **Lessico nuovo**: `polities` → **entità politiche** (poi «entità») · `Assembly of Polities` →
  **Assemblea delle Entità** · `Consonance` → **la Consonanza** · `Dissonance` → **la Dissonanza** ·
  `Elector` → **Elettore** · `Speakers` → **Portavoce** · `Triumvirate` → **Triumvirato** ·
  `Twilight Guard`, `Twilight`, `Outer Limits` **invariati** (forme dominanti nel corpus: 10 e 4
  occorrenze contro 2 e 1) · `hyperdrive` **invariato** (75 contro 40) · `Aberrante` per `Aberrant` ·
  `Trefoil` e `il Foil` **invariati** come nomi del gioco e del terzo giocatore · `Freelancers` →
  **gli Indipendenti** · `Wisteria`, `Nikkio`, `Aviskir`, `Anax`, `Weledos`, `Peripheria` invariati ·
  `Zapchannel Ray Energy` invariato (marchio).

## Verifica

```
python staging/editorial/L48_20261018_170232/check.py    → FAIL totale: 0 (30 controlli)
python staging/editorial/L48_20261018_170232/verify.py   → exit 0, 40 controlli, FAIL: 0
```

`state.py` dopo L48: **22.593 unità · 720.318 EN · 683.425 IT**, `ESITO: OK`, `avgi side missions.txt` a
**180/436 (41,3%)**, 52 directory con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 180 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: nessuna verifica a schermo della partita a Trefoil né della scena di
  Nikkio.
- **Il file non è completo**: restano 256 unità (righe 524–1117), previste in L49.
