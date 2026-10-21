# STATO — L88 · `data/successors/successor outfits.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L88_20261018_205811` |
| Righe / unità | **429–560** (finestra 421–560) / **10** |
| Tipi | **10 `DESCRIPTION`** — nessun dato |
| Contesti | **7** in ordine di riga (`"Aqra" Inductive Reverser` … `"Veusa" Inductive Reverser`) |
| Parole | **329 EN → 343 IT** (1,043); per unità 0,91–1,19 |
| Tab · virgolette | **3** (unità 2, 6, 10) · **0** |
| Duplicato legittimo | **2 / 6 / 10**: stessa frase sul propulsore di retro, resa identica |
| Token | **0** |
| sha256 | `40dafd350a29f440…` |
| `check.py` | **24 controlli**, `FAIL totale: 0` |
| `verify.py` | **24 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 429 | **34** (L86 + L87) |
| Unità dopo la riga 560 | **12** |
| File | **56 unità**, `max(line) = 647` |
| Confine dopo | riga **574** apre `Multimodal Armor: Light` |
| Copertura | **44/56 (78,6%)** |

## Contenuto e decisioni

I propulsori `Aqra` (spinta e retro), `Chyyra` (spinta, manovra, retro) e `Veusa` (i più grandi, per navi da
guerra e mercantili). Il messaggio tecnico sul **propulsore di retro** — «va installato nella sezione armi
invece che in quella motori» — compare tre volte identico: **reso identico**, come in L74.

Scelte: `reverse thruster` → **propulsore di retro**; `steering engines` → **propulsori di manovra** (L87);
`pulsed inductive thrusters` → **propulsori induttivi pulsati**; `shield power` → **energia degli scudi**;
`g-force stress` → **sollecitazioni da forza g**.

## Verifica

```bash
cd staging/editorial/L88_20261018_205811
python check.py   # FAIL totale: 0
python verify.py  # exit 0
```
