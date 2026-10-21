# L49 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L49_20261018_170618` · `data/avgi/avgi side missions.txt` · righe 524–1117 · **256/256 unità**.
Con L48 (**180**) il file è a **436/436**: **ventisettesimo file completo** dello staging. Tutti i numeri
sono misurati, non stimati.

## Fatto

- `source.json`: 256 unità, 5 contesti (`Avgi: Cylinder Construction` 1–35, `Avgi: Infocourier Encounter`
  36–67, `Avgi Culture: Twilight Tavern Guard` 68–147, `Avgi: Atomics Testing 1` 148–191,
  `Avgi: Atomics Testing 2` 192–256), kind 244 `MISSION_TEXT` / 5 `LOGBOOK` / 3 `UI_LABEL` /
  2 `VALUE` / 2 `DESCRIPTION`. Nessun `DIALOG`, nessun `CONVERSATION`, nessun `TEXT`.
- `check.py` derivato da L48 con **`NT` = 3** (`UI_LABEL`), **`LOGBOOK` positivo su 5 testi** tutte a tre
  argomenti, **7 virgolette dispari** riprodotte, **assenze dichiarate** per `CONVERSATION`, `DIALOG` e
  quadre, costruttore dei tab.
- 7 parti: 35 · 32 · 43 · 37 · 44 · 39 · 26.
- `translation.json`: 256 unità, 7.606 EN → 7.324 IT (0,963), rapporto per unità 0,65–1,46,
  sha256[:16] `0fe8cac3bf134108`.
- `verify.py`: **38 controlli**, `FAIL: 0`, exit 0. Copertura del **file** 436/436 su **due lotti**
  (L48 180 + L49 256), coppia **(524, 1117)**, **180 unità prima / 0 dopo** (fine file), `NT` 3,
  `LOGBOOK` 5 senza categorie, insieme delle 7 virgolette dispari.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **`NT` = 3 label, nessun riferimento di dato**: tutte le 5 righe `LOGBOOK` hanno il testo estratto.
  La lacuna dell'estrattore **non si presenta nemmeno qui** (come in L48): due lotti di fila in cui il
  difetto noto è assente, e in entrambi il `check.py` lo asserisce invece di darlo per scontato.
- **7 virgolette dispari** (22, 91, 101, 108, 109, 186, 218): battute aperte nel sorgente, riprodotte
  aperte. Sono **sei** le unità con una sola virgoletta di apertura e una che chiude a metà frase.
- **Tab 235**, virgolette **471**, token **13** su 6 famiglie: parità per unità.
- **Un errore vero intercettato dal controllo duplicati**: le unità 25 e 236 sono entrambe `"No."` in
  inglese, l'unità 95 è `"Nope."`. La prima stesura rendeva tutte e tre «No.»; 95 è stata corretta in
  **«Macché.»**, che è anche la risposta naturale a «non sei mica un Aberrante, vero?».
- **Lessico**: `Cylinder` → **Cilindro** (nome proprio: *Cilindro Aktina*) · `Infocourier` →
  **infocorriere** · `accounting` → **contabilità** (di materiali, non di crediti) · `memory diamond` →
  **diamante di memoria** · `Polari`, `Akoustiki Excursion Vehicle`, `Navigeo Yards`, `Ergastirio`,
  `Dokimi`, `Hekkedian`, `Freosi`, `Lieno-Drareg` invariati · `atomica` per `atomic` (arma) e
  **test atomico** per `atomics test` · `breeder reactors` → **reattori autofertilizzanti**.

## Verifica

```
python staging/editorial/L49_20261018_170618/check.py    → FAIL totale: 0 (28 controlli)
python staging/editorial/L49_20261018_170618/verify.py   → exit 0, 38 controlli, FAIL: 0
```

`state.py` dopo L49: **22.849 unità · 727.924 EN · 690.749 IT**, `ESITO: OK`,
`avgi side missions.txt` a **436/436 (100%, 2 lotti)**, 53 directory con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 436 unità del file sono `PENDING`.
- **Nessun caricamento nel gioco**: il test atomico su Dokimi e le scene del bar e della stazione
  Ergastirio non sono mai state viste a schermo.
- **Nessun test di gameplay** della linea Avgi.
