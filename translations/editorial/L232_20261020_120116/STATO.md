# STATO — L232 (`data/korath/korath outfits.txt`, righe 809–908) · **CHIUSO**

**Quinto e ultimo lotto del file: `data/korath/korath outfits.txt` è COMPLETO, 92/92 unità.**
Lotto **terminale**: la finestra finisce con l'ultima unità del file (riga 908), e l'invariante è **di file**,
non di segmento.

| voce | valore misurato |
|---|---|
| file | `data/korath/korath outfits.txt` |
| righe | 809–908 |
| unità | **10** |
| parole | **454 EN → 508 IT** |
| rapporto | 1,04 – 1,25 (media 1,12) |
| tipi | **10 `DESCRIPTION`**, **zero `VALUE`** |
| contesti | **7** |
| tab | **4** (unità 1, 5, 7, 10 — sempre iniziali) |
| virgolette | **2**, entrambe nell'unità 10 |
| apici | **5 EN** (3:1, 5:1, 8:3) / **3 IT** (1, 3, 6) |
| segnaposto | **0** |
| `check.py` | **31 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **19 controlli, `FAIL: 0`**, exit 0 |
| `sha256[:16]` di `translation.json` | **`f0ac63cba4ffbcb3`** |
| stato | **CHIUSO** |

## Copertura del file (invariante di FILE)

| lotto | righe | unità | EN → IT | check / verify | sha256[:16] |
|---|---|---|---|---|---|
| L228 | 16–195 | 20 | 434 → 474 | 27 / 20 | `49228f599876094f` |
| L229 | 208–318 | 15 | 431 → 442 | 27 / 18 | `b85fa00ea11fb613` |
| L230 | 319–581 | 26 | 430 → 448 | 27 / 19 | `d246b4e6c38a2e78` |
| L231 | 596–808 | 21 | 455 → 498 | 27 / 19 | `39c7cbdeb1825d8b` |
| **L232** | **809–908** | **10** | **454 → 508** | **31 / 19** | **`f0ac63cba4ffbcb3`** |
| **totale** | **16–908** | **92** | **2.204 → 2.370** | | |

`20 + 15 + 26 + 21 + 10 = 92` unità su **92 righe distinte**, `sovrapposti = 0`, `min(line) = 16`,
`max(line) = 908`. La riga 908 è l'ultima riga di **contenuto** del file (la 909 è vuota): dopo di lei il
database non ha nessuna unità di questo percorso.

## Cosa cambia rispetto a L231

1. **Primo lotto della campagna con sole `DESCRIPTION`**: zero `VALUE`, quindi il confronto è **0 identiche /
   10 tradotte** e il `check.py` asserisce che *nessuna* unità resti identica all'inglese.
2. **I tab risalgono a 4** dopo lo zero di L231: quinto conteggio consecutivo diverso nello stesso file —
   0 (L228) · 3 (L229) · 7 (L230) · 0 (L231) · **4 (L232)**.
3. **Le virgolette tornano a 2** dopo sei lotti a zero, e stanno entrambe in una sola unità (`"escape,"`):
   la virgola è **dentro** le virgolette e si riproduce.
4. **5 apici inglesi contro 3 italiani**, per ragioni opposte: l'inglese contrae (`engineers'`, `system's`,
   `aren't`, `user's`, `won't`), l'italiano elide (`all'inefficienza`, `l'influenza`, `l'abbandono`).
5. **Chiude il settimo file** della campagna, dopo `hai jobs.txt`, `hai outfits.txt`, `coalition news.txt`,
   `deep jobs.txt`, `successor ships.txt` e `remnant outfits.txt`.

## Comandi di verifica

```bash
python staging/editorial/L232_20261020_120116/check.py     # FAIL totale: 0 (31 controlli)
python staging/editorial/L232_20261020_120116/verify.py    # FAIL: 0 (19 controlli), FILE CHIUSO 92/92
```
