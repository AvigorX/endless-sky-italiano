# L39 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L39_20261018_124057` · `data/human/free worlds 4 epilogue.txt` · righe 22–341 · **114/114 unità**.
Diciannovesimo file completo dello staging, e **ultimo della campagna principale delle Free Worlds**.
Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 114 unità, 6 contesti, kind 77 `MISSION_TEXT` / **34 `CONVERSATION`** / 1 `VALUE` /
  1 `DESCRIPTION` / 1 `LOGBOOK` / **0 `UI_LABEL`**.
- `check.py` derivato da L38 con **`NT` vuoto**: 0 `UI_LABEL` nel file. In L38 conteneva due `label` di
  salto: copiarla avrebbe messo in `NT` due unità che qui sono testo normale.
- **34 `CONVERSATION`** (unità 81–114, il blocco `edward epilogue`): quasi tutto il secondo atto del file
  è dialogo con Barmy Edward. Tradotto come colloquio continuo, e il `verify.py` asserisce che siano 34
  e tutte non vuote.
- 2 parti, a fine contesto: 1–63 (Ijs e Katya, Alondo, Freya) e 64–114 (Danforth, Edward).
- `translation.json`: 114 unità, 3.487 EN → 3.209 IT (0,920), rapporto per unità 0,72–1,50,
  sha256[:16] `b41df1b6b2b9dec7`.
- `verify.py`: **29 controlli**, `FAIL: 0`, exit 0. Copertura **114/114** asserita, e la coppia di righe
  attesa è **(22, 341)**: questo file **non** parte dalla riga 16.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce: l'epilogo.** Ogni personaggio è ripreso uno per uno con il registro che aveva nella guerra, ma
  alleggerito: Ijs e Katya professori, Alondo burocrate soddisfatto, Freya ancora ossessionata dai Pug,
  Danforth che non andrà mai in pensione, Barmy Edward che vuole solo far provare un'arma nuova.
- **La quarta parete si rompe due volte** (unità 9 e 12) e in italiano si rompe allo stesso modo: «a
  quanto pare quella parte del gioco non è ancora stata implementata del tutto» e «ora l'hai fatto, è
  caduta la quarta parete».
- **Si riproduce il sorgente**: tab 105/105, virgolette 258/258, token 16/16. **Nessuna** unità con numero
  dispari di virgolette: il controllo resta attivo e confronta insiemi vuoti.
- **Nessun controllo allentato**: nessuna unità fuori dal gate; 16 riscritture di rifinitura sono elencate
  in `review.md` §8 (la più importante: «cugini di secondo grado», non «cugini»).
- **Numeri dai file, non dalla memoria**: kind, 22 controlli di `check.py`, 29 di `verify.py` e tutti i
  totali vengono dai JSON del lotto e da `state.db` in sola lettura.

## Verifica

```
python staging/editorial/L39_20261018_124057/check.py    → FAIL totale: 0 (22 controlli)
python staging/editorial/L39_20261018_124057/verify.py   → exit 0, 29 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 114 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato come venga reso il blocco `CONVERSATION` 81–114, che nel gioco ha
  un'interfaccia propria.
- **Nessun test di gameplay** delle quattro visite facoltative dell'epilogo.
