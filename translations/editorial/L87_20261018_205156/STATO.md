# STATO — L87 · `data/successors/successor outfits.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L87_20261018_205156` |
| Righe / unità | **251–409** (finestra 241–420) / **13** |
| Tipi | **12 `DESCRIPTION` + 1 `VALUE`** (unità 10, `"Niis" Inductive Engines`, identico) |
| Contesti | **9**, in ordine di riga (`"Ryuit" Fusion Core` … `"Aqra" Inductive Steering`) |
| Parole | **572 EN → 591 IT** (1,033); per unità 1,00–1,33 |
| Tab · virgolette | **3** (unità 2, 7, 9) · **2** (0 dispari) |
| Token · duplicati | **0 = 0** · **0** |
| sha256 | `667d024aa8548de4…` |
| `check.py` | **24 controlli**, `FAIL totale: 0` |
| `verify.py` | **24 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 251 | **21** (L86) |
| Unità dopo la riga 409 | **22** |
| File | **56 unità**, `max(line) = 647` |
| Confine dopo | riga **429** apre `outfit:"Aqra" Inductive Reverser` |
| Copertura | **34/56 (60,7%)** |

## Contenuto e decisioni

I due **reattori a fusione** (`Ryuit`, e quello più grande a forma di **pianta fiorita**, `Uoret`), il
**raffreddamento** bimodale, la **vela solare** che raccoglie idrogeno «più elegantemente di un ramscoop», i
due **scanner** (`Veldt` da combattimento, `Tuur` per l'analisi planetaria), i **motori induttivi** `Niis` e i
**propulsori** `Aqra` (spinta e manovra, con il **postbruciatore**).

- `VALUE` unità 10: **identico** (`"Niis" Inductive Engines`);
- `stellarator` → **stellator**; `ramscoop` → **ramscoop** (nome di tecnologia, invariato);
- `afterburner` → **postbruciatore**; `steering thrusters` → **propulsori di manovra**;
- `bimodal` → **bimodale**; `draw` → **consumo**.

## Verifica

```bash
cd staging/editorial/L87_20261018_205156
python check.py   # FAIL totale: 0
python verify.py  # exit 0
```
