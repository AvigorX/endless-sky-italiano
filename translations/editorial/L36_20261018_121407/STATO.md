# L36 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L36_20261018_121407` · `data/human/free worlds 2 middle.txt` · righe 16–2336 · **552/552 unità**.
Sedicesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 552 unità, 52 contesti, kind 396 `MISSION_TEXT` / 46 `VALUE` / 45 `DESCRIPTION` /
  39 `DIALOG` / 23 `LOGBOOK` / **3 `UI_LABEL`**.
- `check.py` derivato da L35 con **`NT = {407, 501, 503}`**: tre `label` di salto (`me too`,
  `definitely surrender`, `definitely rescue`), bersagli di `goto`, lasciate identiche. In L35 la lista
  era `{513, 547}` (1 label + 1 categoria di diario): copiarla avrebbe fatto tradurre queste tre e
  rotto i salti. Verificato sul `raw` che tutte e tre siano `label "..."`.
- `TOKEN_EXC` vuoto, 10 famiglie di token di dati. Il controllo delle parentesi quadre resta **rimosso**
  (0 unità con `[a, b]`, misurato) e il `verify.py` asserisce che siano 0.
- 11 parti scritte a mano, tutte a fine contesto: 1–71, 72–122, 123–163, 164–207, 208–257, 258–318,
  319–386, 387–440, 441–471, 472–538, 539–552 (71, 51, 41, 44, 50, 61, 68, 54, 31, 67, 14).
  Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 552 unità, 16.290 EN → 15.323 IT (0,941), rapporto per unità 0,75–1,65,
  sha256[:16] `502a8f740d9181e9`.
- `verify.py`: **27 controlli**, `FAIL: 0`, exit 0. Copertura **552/552** asserita: il lotto è l'unico
  del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Continuità di voce con L34–L35, registro che cambia**: dopo la sospensione della fine di L35 il
  giocatore rientra in servizio, quindi il tono è operativo; ma la frattura fra Consiglio e Senato resta
  sullo sfondo e diventa visibile nel bivio di Greenrock (L35) prima e in quello dei prigionieri e di
  Bloodsea (L36) poi. Nel frattempo il giocatore **entra nel Consiglio** (unità 221): da quel punto le
  decisioni sono sue e il testo lo dice («Ora sei tu nel Consiglio. Lascio decidere a te.»).
- **Si riproduce il sorgente**: tab 341/341, virgolette 919/919, token 139/139. **Tre unità** hanno un
  numero dispari di virgolette (76, 77, 355: battute aperte dal sorgente): riprodotte, e il `verify.py`
  confronta l'insieme degli idx.
- **Nessun controllo allentato**: 123 e 138 riscritte perché il rapporto usciva dalla banda comoda
  (1,81 e 1,895), 247 riscritta perché superava il gate (1,909); 543 riscritta per ripristinare le
  quattro virgolette del sorgente (`"..."` spezzato da «he says»).
- **Numeri dai file, non dalla memoria**: kind, 21 controlli di `check.py`, 27 di `verify.py` e tutti i
  totali vengono dai JSON del lotto e da `state.db` in sola lettura.

## Verifica

```
python staging/editorial/L36_20261018_121407/check.py    → FAIL totale: 0 (21 controlli)
python staging/editorial/L36_20261018_121407/verify.py   → exit 0, 27 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 552 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato come vengano impaginati i due monologhi lunghi (unità 476 e 480) e le
  scene di combattimento corpo a corpo (§ *review* 5).
- **Nessun test di gameplay** sui due bivi di questo file (prigionieri rilasciati o tenuti; Bloodsea
  diplomatica o invasa).
