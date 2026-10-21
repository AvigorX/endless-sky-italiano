# L49 — rapporto del lotto

`data/avgi/avgi side missions.txt` · righe **524–1117** · lotto `L49_20261018_170618` ·
**256/256 unità** · **file completo 436/436** con L48 (180 + 256) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **256 / 256** del segmento; **file 436 / 436** (L48 180 + L49 256) |
| parole | 7.606 EN → **7.324 IT** (0,963) |
| contesti | 5 (`Cylinder Construction` 1–35, `Infocourier Encounter` 36–67, `Twilight Tavern Guard` 68–147, `Atomics Testing 1` 148–191, `Atomics Testing 2` 192–256) |
| parti | 7 — 35 · 32 · 43 · 37 · 44 · 39 · 26 |
| tab | **235 = 235** |
| virgolette | **471 = 471** |
| virgolette dispari | **7** (22, 91, 101, 108, 109, 186, 218), stessi idx in italiano |
| token `<...>` | **13 = 13** (6 famiglie) |
| quadre `[` `]` | **0 unità** (asserzione di assenza dichiarata) |
| `LOGBOOK` | **5**, tutte a tre argomenti con testo fra backtick |
| `CONVERSATION` / `DIALOG` | **0 / 0** (assenze dichiarate) |
| rapporto per unità | 0,65 – 1,46 |
| `check.py` | **FAIL totale: 0** (28 controlli) |
| `verify.py` | **38 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `0fe8cac3bf134108` · `source.json` `296e0620ccb7e1f0` · `check.py` `15f318d47135e13f` · `verify.py` `d568e421503319ed` |

Il segmento **chiude il file**: `verify.py` asserisce `(first, last) == (524, 1117)`, **180** unità prima
della 524 (L48) e **0** dopo la 1117 (`max(line) = 1117`).

## Tipi

244 `MISSION_TEXT` · 5 `LOGBOOK` · 3 `UI_LABEL` · 2 `VALUE` · 2 `DESCRIPTION` · 0 `DIALOG` ·
0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 3

| idx | riga | label |
|---:|---:|---|
| 12 | 554 | `when update` |
| 79 | 721 | `too much` |
| 167 | 921 | `wanna see` |

**Nessun riferimento di dato**: tutte le righe `LOGBOOK` hanno il testo nell'unità.

## Le 5 righe `log`

| idx | riga | personaggio | contenuto |
|---:|---:|---|---|
| 1 | 524 | Gamboge | dirige i lavori del Cilindro Aktina, frustrato dall'Assemblea |
| 36 | 625 | Hansa | infocorriere, comunicazioni senza iperspazio |
| 68 | 701 | Claret | membro della Twilight Guard, dottrina del combattimento |
| 151 | 891 | Aliza | scienziata di Ergastirio, armi nucleari e onde d'urto |
| 237 | 1074 | Yinmn | specialista della sicurezza dei materiali nucleari |

## Verifica

```
python staging/editorial/L49_20261018_170618/check.py    → FAIL totale: 0
python staging/editorial/L49_20261018_170618/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **22.849 unità · 727.924 EN · 690.749 IT**, 53 directory con `translation.json`,
integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica). Il file
`avgi side missions.txt` è al **100%** su due lotti: i file completi sono **ventisette**.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 256 unità `PENDING` (436 con L48).
- **Nessun caricamento nel gioco**: il test atomico su Dokimi, il bar di Twilight e la stazione Ergastirio
  non sono mai stati visti a schermo.
- **Nessun test di gameplay** della linea Avgi.
