# L40 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L40_20261018_124513` · `data/human/free worlds side plots.txt` · righe 18–888 · **211/211 unità**.
Ventesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 211 unità, 19 contesti, kind 154 `MISSION_TEXT` / 19 `DIALOG` / 15 `VALUE` /
  15 `DESCRIPTION` / 7 `LOGBOOK` / **1 `UI_LABEL`**.
- `check.py` derivato da L39 con **`NT = {80}`**: la `label` di salto `brower death` (riga 322), bersaglio
  di `goto`. In L39 la lista era vuota: copiarla avrebbe lasciato la label in inglese e rotto il salto.
- 4 parti, a fine contesto: 1–66, 67–112, 113–166, 167–211 (66, 46, 54, 45).
- `translation.json`: 211 unità, 5.683 EN → 5.339 IT (0,939), rapporto per unità 0,72–1,61,
  sha256[:16] `516c1b1a59c9cfe0`.
- `verify.py`: **29 controlli**, `FAIL: 0`, exit 0. Copertura **211/211** asserita, coppia di righe
  **(18, 888)**: il file non parte dalla riga 16.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Personaggi nuovi, tono da trama secondaria**: il monaco David, il capitano della milizia di
  Greenrock, Rex e Fido del Branco di Lupi, l'Agente Falco, il quartiermastro di Zug. Nessuno di loro
  ha la voce dei cinque del Consiglio: si presentano e si definiscono in poche battute, e la traduzione
  non ha importato il registro dei personaggi principali.
- **Si riproduce il sorgente**: virgolette 352/352 e token 59/59. Il conteggio dei tab nel `source.json`
  è 133 (l'export ne riportava 129: il numero che conta è quello del `check.py`, che confronta IT e EN
  unità per unità).
- **Due battute aperte** (56, 202): riprodotte, e il `verify.py` confronta l'insieme degli idx.
- **Duplicati differenziati**: le tre varianti di «Hai raggiunto <planet>, ma hai lasciato indietro una
  parte del (tuo) convoglio» hanno inglesi diversi per una parola o per il punto finale, e sono state
  rese con tre formulazioni distinte (unità 15, 65/69, 190).
- **Nessun controllo allentato**: 33 e 77 riscritte per il rapporto minimo.

## Verifica

```
python staging/editorial/L40_20261018_124513/check.py    → FAIL totale: 0 (22 controlli)
python staging/editorial/L40_20261018_124513/verify.py   → exit 0, 29 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 211 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato il memoriale di guerra (unità 79–84), che usa rientri multipli.
- **Nessun test di gameplay** delle trame secondarie, comprese le tre missioni del Branco di Lupi.
