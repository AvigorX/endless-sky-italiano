# STATO — L92 · `data/successors/successor culture conversations.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L92_20261018_212146` |
| Righe / unità | **230–351** (finestra 230–351) / **46** |
| Tipi | **46 `MISSION_TEXT`** — **0 `UI_LABEL`** (premessa asserita, non omissione) |
| Contesti | **5** in ordine di riga (`Stage Play` … `Armor Reconfiguration`) |
| Parole | **1848 EN → 1775 IT** (0,960); per unità 0,88–1,43 |
| Tab · virgolette · token | **42** (senza tab 21, 37, 44, 46) · **48** di cui **una sola** nelle unità 13 e 21 · **1** `<ship>` (41) |
| Ripetizione | **17/20**: stesso inglese, resa identica |
| sha256 | `ac367d9586bdaad5…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** (invariante di file) |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 230 | **68** (L90 + L91) |
| Unità dopo la riga 351 | **0** — il file finisce qui |
| File | **114 unità**, `max(line) = 351` |
| Copertura | **114/114 (100%)** — 114 id distinti su 114 righe, **0 sovrapposizioni** |
| Lotti | **3** — L90 (34), L91 (34), L92 (46) |
| Parole del file | **4.063 EN → 3.873 IT** |

`successor culture conversations.txt` è il **trentasettesimo file completo**, **non approvato**: 114 unità
`PENDING`.

## Contenuto

La **coda di `Stage Play`** (1–20): il treno per la costa, il pubblico sulle panche semicircolari attorno alla
vasca, l'introduzione con i contrassegni infilati sui fili, la battuta d'apertura «Myiara!», la scelta fra
seguire con attenzione, lasciar vagare la mente o uscire prima, e i due riassunti della trama (quello di chi
ha seguito e quello di chi si è distratto). **Sosrue** (21–36): il bambino che chiede di un mostro da una
poesia, i tre rami di risposta e la canzonatura finale («metà delle tue braccia sono state separate da te!»).
**Derelict Station Toy** (37–43): il modellino di navetta Kvelqde nel buio, e i tre esiti (lasciarlo, prenderlo,
calpestarlo). **Pet Commemoration** (44–45): la targa per «Mirja-Mirja». **Armor Reconfiguration** (46):
l'armatura in metamateriale che sembra liquida sotto i bracci meccanici.

## Verifica

```bash
cd staging/editorial/L92_20261018_212146
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (29 controlli, invariante di file)
```
