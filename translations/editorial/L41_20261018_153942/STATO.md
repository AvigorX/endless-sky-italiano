# L41 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L41_20261018_153942` · `data/human/free worlds war jobs.txt` · righe 16–927 · **72/72 unità**.
Ventunesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 72 unità, 34 contesti, kind 29 `VALUE` / 29 `DESCRIPTION` / 8 `DIALOG` / **6 `TEXT`**.
- `check.py` derivato da L40 con **`NT` vuoto**: 0 `UI_LABEL` nel file. In L40 conteneva la label di
  salto `brower death`; copiarla qui avrebbe messo in `NT` un indice inesistente.
- 2 parti, a fine contesto: 1–40 e 41–72 (40, 32).
- `translation.json`: 72 unità, 1.124 EN → 1.140 IT (1,014), rapporto per unità 0,81–1,25,
  sha256[:16] `17727c643c46cd38`.
- `verify.py`: **30 controlli**, `FAIL: 0`, exit 0. Copertura **72/72** asserita, coppia di righe
  **(16, 927)**.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **`TEXT` è un tipo nuovo**: 6 unità sono testi di `phrase` (il primo contesto è
  `free worlds scanner payment`). Tradotti come frasi, con il backtick di cornice conservato dal
  costruttore perché sta nel `raw` e non nell'`english`; il `verify.py` asserisce che le 6 `TEXT` siano
  tradotte e che nell'italiano non compaia nessun backtick.
- **Tab 0 e virgolette 0**: il file non ha indentazione né battute. I due controlli sono rimasti e
  asseriscono la parità su zero — è la prima volta nella serie.
- **Token densissimi**: 172 token su 72 unità (10 famiglie, `<planet>` 46, `<payment>` 35, `<date>` 29,
  `<destination>` 28). Il controllo dei token è il più importante del lotto ed è a parità esatta.
- **Duplicati**: 17 gruppi di inglese identico (64 unità su 72). Sono lavori parametrici ripetuti per
  sistema: dove l'inglese è identico, l'italiano è identico; dove differisce per una parola (27/28
  «capitano»/«capitani», 57/59 e 61/63 «Free Worlds»/«Repubblica»), l'italiano differisce.

## Verifica

```
python staging/editorial/L41_20261018_153942/check.py    → FAIL totale: 0 (22 controlli)
python staging/editorial/L41_20261018_153942/verify.py   → exit 0, 30 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 72 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a
  schermo. In particolare non è verificato che i lavori compaiano nella lista lavori con i titoli
  tradotti (`Ricognizione`, `Convoglio per <planet>`, …).
- **Nessun test di gameplay** dei lavori di guerra ripetibili.
