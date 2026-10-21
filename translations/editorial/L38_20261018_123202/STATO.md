# L38 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L38_20261018_123202` · `data/human/free worlds 3 reconciliation.txt` · righe 31–2729 ·
**596/596 unità**. Diciottesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 596 unità, 51 contesti, kind 425 `MISSION_TEXT` / 42 `VALUE` / 42 `DESCRIPTION` /
  41 `LOGBOOK` / 35 `DIALOG` / **2 `UI_LABEL`** / **9 `CONVERSATION`**.
- `check.py` derivato da L37 con **`NT = {139, 308}`**: due `label` di salto (`star queen`,
  `planet dweller questions`), bersagli di `goto`, lasciate identiche. In L37 la lista era vuota:
  copiarla avrebbe fatto tradurre le due label e rotto due salti.
- **`CONVERSATION` 9** (unità 403–411): il blocco della visita al Cantiere della Marina su Geminus.
  Tradotte come testo continuo; il `verify.py` asserisce che siano 9 e tutte non vuote.
- Controllo `quadre [ ] per unita`: l'unità **426** ha una coppia che racchiude la riga (cornice del
  motore), conservata e tradotta per intero.
- `TOKEN_EXC` vuoto, 6 famiglie di token di dati. 14 parti, tutte a fine contesto: 1–58, 59–100,
  101–140, 141–169, 170–201, 202–234, 235–285, 286–342, 343–384, 385–419, 420–457, 458–518,
  519–558, 559–596 (58, 42, 40, 29, 32, 33, 51, 57, 42, 35, 38, 61, 40, 38).
- `translation.json`: 596 unità, 21.021 EN → 20.228 IT (0,962), rapporto per unità 0,74–1,80,
  sha256[:16] `1cda2e18fc38b163`.
- `verify.py`: **29 controlli**, `FAIL: 0`, exit 0. Copertura **596/596** asserita, e la coppia di righe
  attesa è **(31, 2729)**: questo file **non** parte dalla riga 16.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce: la ricostruzione.** Dopo la guerra, il registro è più pacato e più politico: Alondo ricuce,
  JJ amministra, Freya indaga, Katya giudica. Raven ha poche battute e tutte definitive; Alastair
  Korban parla come un dirigente che ha già deciso di dimettersi. I Quarg e i Pug mantengono il
  registro stabilito in L37 (e alcune unità ripetono quasi alla lettera le scene di L37: dove l'inglese
  coincide, l'italiano coincide).
- **Si riproduce il sorgente**: tab 361/361, virgolette 1.004/1.004, token 119/119. **Due** unità hanno
  un numero dispari di virgolette (45, 546: battute aperte dal sorgente), riprodotte, e il `verify.py`
  confronta l'insieme degli idx.
- **Nessun controllo allentato**: 32, 89, 146 e 401 sono state riscritte per refusi e sgrammaticature
  italiane (elenco completo in `review.md` §8); il titolo 527 esce dalla banda comoda (1,80) ma resta
  dentro il gate 0,55–1,90, e il titolo è stato lasciato per esteso perché abbreviarlo perderebbe
  chiarezza.
- **Numeri dai file, non dalla memoria**: kind, 22 controlli di `check.py`, 29 di `verify.py` e tutti i
  totali vengono dai JSON del lotto e da `state.db` in sola lettura.

## Verifica

```
python staging/editorial/L38_20261018_123202/check.py    → FAIL totale: 0 (22 controlli)
python staging/editorial/L38_20261018_123202/verify.py   → exit 0, 29 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 596 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato come venga reso il blocco `CONVERSATION` 403–411 (nove unità di
  dialogo continuo) né il testo lungo dell'unità 426 fra le quadre.
- **Nessun test di gameplay** sui bivi di questo file (accettare o rifiutare di andare nel Sindacato,
  visitare o no i Quarg e il Deep).
