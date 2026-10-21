# STATO — L90 · `data/successors/successor culture conversations.txt` (primo lotto del file)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L90_20261018_210455` |
| Righe / unità | **23–142** (finestra 1–142) / **34** |
| Tipi | **34 `MISSION_TEXT`** — nessun altro tipo |
| Contesti | **6** (`Kua-Oa-Aava` … `Buskers`) |
| Parole | **1098 EN → 1014 IT** (0,923); per unità 0,77–1,70 |
| Tab · virgolette · token | **28** (3–10, 13–16, 19–34) · **2** (unità 23) · **3** `<ship>` (1, 10, 18) |
| Ripetizioni | **3/13** stesso inglese `(Take it.)` reso `(Prendilo.)`/`(Prendila.)` per il genere · **26/31** identiche |
| sha256 | `45fd22aca9b71868…` |
| `check.py` | **27 controlli**, `FAIL totale: 0` |
| `verify.py` | **26 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 23 | **0** (primo lotto del file) |
| Unità dopo la riga 142 | **80** |
| File | **114 unità**, `max(line) = 351` |
| Confine dopo | la prima unità dopo la 142 è `Graffiti` |
| Copertura | **34/114 (29,8%)** |

## Finestra ridotta — dichiarata

`HANDOFF_L90` prevedeva **76 unità / 2583 parole** in una finestra 1–240. Ho aperto **34 unità / 1098
parole** (righe 1–142): un lotto da quattro parti con 66 tab e 7 token non entrava nel budget di questa
sessione con verifica completa. La finestra residua (unità 35–76, contesti `Graffiti` … `Stage Play`) passa a
**L91**, non ancora scritto come contratto.

## Contenuto e decisioni

Sei conversazioni: l'**adattatore di carburante** stampato da una sfera di metallo morfico, il **boccone di
cibo** offerto e rifiutato o assaggiato («sa di pesce… troppo salato»), lo **spazioporto sott'acqua** con il
salotto a più livelli, la **mappa stellare** offerta oltre le barriere, la vasca con la **salamandra**
domestica, e i **musicisti** nella vasca — la melodia «impossibilmente alta o bassa», la pelle che cambia
colore e consistenza, la traduzione che restituisce solo frammenti («dolcissimo figlio… corrente cupa…»).

Scelte: `morphic metal sphere` → **sfera di metallo morfico**; `data-sphere` → **sfera di dati**; `trills` →
**trilla**; `hum` → **ronzio**; `(Take it.)` reso secondo il genere dell'oggetto; le virgolette del canto
restano due, come nel sorgente.

## Verifica

```bash
cd staging/editorial/L90_20261018_210455
python check.py   # FAIL totale: 0
python verify.py  # exit 0
```
