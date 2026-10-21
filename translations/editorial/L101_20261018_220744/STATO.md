# STATO — L101 · `data/hai/hai culture conversations.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L101_20261018_220744` |
| Righe / unità | **321–386** / **26** |
| Tipi | **26 `MISSION_TEXT`** — **0 `UI_LABEL`** (premessa asserita) |
| Contesti | **2** in ordine di riga: `Hai Film Release` (321–331), `Sick of Acorn Bread` (346–386) |
| Parole | **971 EN → 938 IT** (0,966); per unità 0,75–1,39 |
| Tab · virgolette | **24** · **34** (8 nell'unità 25, tre battute lunghe) |
| Token · quadre | **0** · **1 coppia** (unità 13: `[a sedere, a riposare]`, voce del traduttore) |
| Ripetizioni · virgolette dispari | **nessuna** · **nessuna** |
| sha256 | `b32aaa185052d185…` |
| `check.py` | **26 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** (invariante di file) |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 321 | **121** (L98–L100) |
| Unità dopo la riga 386 | **0** — il file finisce qui |
| File | **147 unità**, `max(line) = 386` |
| Copertura | **147/147 (100%)** — 147 id distinti su 147 righe, **0 sovrapposizioni** |
| Lotti | **4** — L98 (39), L99 (38), L100 (44), L101 (26) |
| Parole del file | **5.003 EN → 4.781 IT** |

`hai culture conversations.txt` è il **trentanovesimo file completo**, **non approvato**: 147 unità `PENDING`.

## Contenuto

- **`Hai Film Release`**: la locandina del film di **Likeet** ambientato su **Darkrest**, il titolo tradotto
  «L'ultimo riposo», e le due varianti della visione — quella in cui si capisce qualcosa e quella in cui il
  traduttore non aiuta e i dialoghi sono «riferimenti criptici alla letteratura e alla filosofia Hai». In
  entrambe: un mostro invisibile, il pubblico che apprezza, l'uscita dalla sala «decisamente scossi».
- **`Sick of Acorn Bread`**: la scelta fra ristorante Hai e venditore ambulante umano, il cestino che incenerisce
  i rifiuti con un bip, la cameriera che si scusa («non sapevo che oggi avrei avuto il piacere di servire un
  umano»), il ristorante pieno di Hai in smoking e in tute con il buco per la coda, e il vicino di sgabello che
  rimpiange la panificazione tradizionale: **hayipp**, **yur ki**, e il **pane di ghiande** che ha spazzato via
  tutto il resto dai menù degli spazioporti.

## Verifica

```bash
cd staging/editorial/L101_20261018_220744
python check.py   # FAIL totale: 0 (26 controlli)
python verify.py  # exit 0 (29 controlli, invariante di file: 147/147)
```
