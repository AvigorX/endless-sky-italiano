# STATO — L86 · `data/successors/successor outfits.txt` (primo lotto del file)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L86_20261018_204835` |
| Righe / unità | **19–235** (finestra 1–240) / **21** |
| Tipi | **17 `DESCRIPTION` + 4 `VALUE`** |
| Contesti | **15** (`Successor License` … `"Nnesa" Fusion Core`) |
| Parole | **1021 EN → 1042 IT** (1,021); per unità 0,98–1,23 |
| Dato / prosa | **4 `VALUE` identiche** (6, 8, 10, 12: `"Byiaa"/"Ej"/"Jaase"/"Jorv" Shield Cortices`) · **17 `DESCRIPTION` tradotte** |
| Tab · virgolette | **1** (unità 3) · **8** (0 dispari) |
| Token · duplicati | **0 = 0** · **0** |
| sha256 | `c3947926c8e088f1…` |
| `check.py` | **26 controlli**, `FAIL totale: 0` |
| `verify.py` | **24 controlli**, exit **0** |

## Dove siamo

| Voce | Valore |
|---|---|
| Unità prima della riga 19 | **0** (primo lotto del file) |
| Unità dopo la riga 235 | **35** |
| File | **56 unità**, `max(line) = 647` |
| Confine dopo | riga **251** apre `outfit:"Ryuit" Fusion Core` |
| Copertura | **21/56 (37,5%)** |

## Contenuto e decisioni

Le due **licenze** (Successori e Alte Casate), la **chiave armonica** che permette alle Nuove Casate di
moltiplicare per venti le loro cinquanta chiavi quantistiche, i **quattro cortex di scudi** (`Byiaa`, `Ej`,
`Jaase`, `Jorv`) con l'**interfaccia** che ne collega due, le **celle betavoltaiche** (`1-"Uurau"`,
`OC-"Mavra"`, `3-"Kaska"`, `6-"Ruuv"`), le due **riserve di energia** e il **reattore a fusione stellator**
`"Nnesa"`.

- i **4 `VALUE`** sono i plurali dei nomi (`"Byiaa" Shield Cortices`): **dato**, identici;
- `shield cortex` → **cortex di scudi** (decisione 264); `betavoltaic` → **betavoltaico/a**;
- `stellarator` → **stellator**; `High Houses` → **Alte Casate**;
- `bimodal engines` → **motori bimodali**; `hull repair systems` → **sistemi di riparazione dello scafo**.

## Verifica

```bash
cd staging/editorial/L86_20261018_204835
python check.py   # FAIL totale: 0
python verify.py  # exit 0
```
