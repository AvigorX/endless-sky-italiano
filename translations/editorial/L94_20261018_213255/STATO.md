# STATO — L94 · `data/coalition/coalition culture conversations.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L94_20261018_213255` |
| Righe / unità | **81–133** (finestra 67–133) / **36** |
| Tipi | **36 `MISSION_TEXT`** — **0 `UI_LABEL`** in questa finestra |
| Contesti | **1** (`Coalition Folklore: Arach`) |
| Parole | **2321 EN → 2115 IT** (0,911); per unità 0,88–1,39 |
| Tab · virgolette · token | **35** (tutte tranne la 1) · **64** (6 nelle unità 1 e 7) · **0** (asserzione) |
| Ripetizioni | **16/22** `(Resta per il prossimo spettacolo.)` · **17/23/29** `(Vai via.)` — rese identiche |
| sha256 | `2413e9527696c61a…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 81 | **31** (L93, righe 24–66) |
| Unità dopo la riga 133 | **90** (riga 148, contesto `Kimek`) |
| File | **157 unità**, `max(line) = 462` |
| Copertura | **67/157 (42,7%)** · 4065 EN → 3731 IT · 2 lotti |

## Contenuto

La serata culturale degli **Arach**: l'incontro con la signora **Matlub** e il suo invito; il teatro-operatorio
con sei ordini di balconate e le telecamere per la diretta; la platea mista di Arach, Kimek e Saryd. Tre opere:
**«Toccato dalla Luna»** (il minatore che raggiunge la luna), **«Bebliss Balbettante»** (la farsa volgare
commissionata da una Casata in rivalità) e **«Fino alla Morte»** (il giardiniere che muore di tosse). Poi una
**quarta «rappresentazione» non annunciata**: la figura di legno appesa ai fili, la musica senza parole di
nessuna lingua della Coalizione, il finale in ginocchio. Matlub non risponde alle domande.

## Verifica

```bash
cd staging/editorial/L94_20261018_213255
python check.py   # FAIL totale: 0 (29 controlli)
python verify.py  # exit 0 (28 controlli)
```
