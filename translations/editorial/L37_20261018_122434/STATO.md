# L37 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L37_20261018_122434` · `data/human/free worlds 3 checkmate.txt` · righe 16–2463 · **482/482 unità**.
Diciassettesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 482 unità, 37 contesti, kind 356 `MISSION_TEXT` / 36 `VALUE` / 36 `DESCRIPTION` /
  27 `LOGBOOK` / 27 `DIALOG` / **0 `UI_LABEL`**.
- `check.py` derivato da L36 con **`NT` vuoto**: 0 `UI_LABEL`, 0 categorie di diario emerse, 0
  riferimenti di dato. In L35 erano 2, in L36 3: la lista vuota è una misura, e il `verify.py` asserisce
  che nel file non ci sia nessuna `UI_LABEL`.
- **Nuovo controllo `quadre [ ] per unita`** nel `check.py`, e doppia asserzione nel `verify.py`:
  l'unità **143** (riga 980) ha una coppia di quadre che racchiude l'intera riga, e non è il dispositivo
  `[a, b]` di L33. È la sintassi delle parentesi del motore (`source/text/Format.cpp`, `LPAREN`/`RPAREN`):
  la cornice va conservata e il testo dentro tradotto per intero.
- `TOKEN_EXC` vuoto, 8 famiglie di token di dati. 11 parti, tutte a fine contesto: 1–49, 50–109,
  110–147, 148–210, 211–269, 270–325, 326–361, 362–392, 393–422, 423–459, 460–482
  (49, 60, 38, 63, 59, 56, 36, 31, 30, 37, 23). Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 482 unità, 16.244 EN → 15.239 IT (0,938), rapporto per unità 0,77–1,62,
  sha256[:16] `8a12ed7b7d904c04`.
- `verify.py`: **28 controlli** (uno in più di L36, per le quadre), `FAIL: 0`, exit 0. Copertura
  **482/482** asserita: il lotto è l'unico del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce: ultimo atto.** Tomek torna reintegrato e riprende il suo registro asciutto; Katya torna
  prigioniera e poi consigliera, con la durezza di chi disapprova i mezzi usati; Danforth è il militare
  che vuole la pace e lo dice senza retorica («Non voglio il merito, voglio la pace»). I Quarg parlano in
  modo impersonale e spezzato, e il loro registro è documentato in `review.md` §4.
- **Si riproduce il sorgente**: tab 305/305, virgolette 900/900, token 121/121. **Nessuna** unità con
  numero dispari di virgolette: il controllo resta attivo e confronta insiemi vuoti, non si fida del
  totale.
- **Nessun controllo allentato**: 140 e 179 riscritte perché sotto la banda comoda (0,643 e 0,645);
  143 tradotta integralmente dentro le quadre, come richiede la struttura.
- **Numeri dai file, non dalla memoria**: kind, 22 controlli di `check.py`, 28 di `verify.py` e tutti i
  totali vengono dai JSON del lotto e da `state.db` in sola lettura.

## Verifica

```
python staging/editorial/L37_20261018_122434/check.py    → FAIL totale: 0 (22 controlli)
python staging/editorial/L37_20261018_122434/verify.py   → exit 0, 28 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 482 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato come venga reso il testo lungo dell'unità 143 fra le quadre, né la
  scena dei Pug olografici (unità 440–458).
- **Nessun test di gameplay** sui bivi di questo file (usare o rifiutare le testate nucleari; la
  deviazione dai Quarg).
