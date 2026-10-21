# STATO — L97 · `data/coalition/coalition culture conversations.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L97_20261018_214757` |
| Righe / unità | **251–462** / **36** |
| Tipi | **36 `MISSION_TEXT`** — **0 `UI_LABEL`** (premessa asserita) |
| Contesti | **7** in ordine di riga (`Departing Trouble - A/B/C` … `Incident: Ring of Wisdom`) |
| Parole | **2269 EN → 2142 IT** (0,944); per unità 0,85–1,26 |
| Tab · virgolette · token | **29** · **24** (6 nell'unità 19; 4 in 22 e 25) · **14** (`<origin>` ×8, `<ship>` ×5, `<last>` ×1) |
| Ripetizione | **7/9/11** tripla, resa identica; le varianti 15/17 differiscono per la virgola (`"collaborazione,"` / `"collaborazione",`) |
| sha256 | `cc6086592132277e…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** (invariante di file) |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 251 | **121** (L93–L96) |
| Unità dopo la riga 462 | **0** — il file finisce qui |
| File | **157 unità**, `max(line) = 462` |
| Copertura | **157/157 (100%)** — 157 id distinti su 157 righe, **0 sovrapposizioni** |
| Lotti | **5** — L93 (31), L94 (36), L95 (27), L96 (27), L97 (36) |
| Parole del file | **9.964 EN → 9.138 IT** |

`coalition culture conversations.txt` è il **trentottesimo file completo**, **non approvato**: 157 unità
`PENDING`.

## Contenuto

Sette scene brevi, tutte dal punto di vista di chi parte da un pianeta della Coalizione:

- **Departing Trouble - A/B/C**: la partenza disturbata — navi civili inseguite da navi da guerra Heliarch,
  l'abbordaggio delle superstiti, e infine l'ispezione di routine di un **Punisher** («Saluti, Capitano
  `<last>`… un'ispezione di routine, stiamo facendo»), con i suoi due esiti (il contegno calmo e la ricerca di
  cimici a bordo).
- **Incident: Secret Sky**: il capitano Arach che cerca un passeggero Kimek scomparso nella nebbia di
  `<origin>`.
- **Hunger Tower**: la protesta dei Kimek per il convoglio di cibo mancante, gli Heliarch in difficoltà e i
  droni che distribuiscono i pasti dalla torre.
- **Incident: Arach Store**: la confisca dei capi «illegali» e la proprietaria che assiste alla distruzione
  della merce.
- **Incident: Ring of Wisdom**: l'allarme nell'anello, la quarantena, il Saryd che esce urlando dal passaggio e
  spara alle spalle, il sacco e la barella.

## Verifica

```bash
cd staging/editorial/L97_20261018_214757
python check.py   # FAIL totale: 0 (30 controlli)
python verify.py  # exit 0 (29 controlli, invariante di file)
```
