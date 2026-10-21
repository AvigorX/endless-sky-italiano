# STATO — L125 · `data/human/ships.txt` (terzo lotto, **chiude il file**: 20 unità)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L125_20261019_072624` |
| Righe / unità | **3491–4266** / **20** — ultima unità del file |
| Tipi | **20 `DESCRIPTION`** · **nessun `VALUE`** |
| Stati | **20 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **15** — 10×1, 5×2 |
| Testi distinti | **20** per 20 unità; **1 nota** ripresa da L123/L124 (droni) |
| Parole | **1180 EN → 1200 IT** (1,017); per unità 0,93–1,25, media 1,07 |
| Tab | **5 unità** (6, 9, 12, 14, 17) |
| Virgolette | **14**: 6 nell'unità 1, 2 nell'unità 6, 6 nell'unità 7 |
| Token · `VALUE` · quadre | **0** · **0** · **0** — asserzioni scritte |
| sha256 | `e2309e1d7fee3d39…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** — invariante **di file** |

## Il file è chiuso

```
data/human/ships.txt   103/103 unità (100,0%) · 5083 EN -> 5286 IT · 3 lotti
L123 78–2044 (54) · L124 2102–3422 (29) · L125 3491–4266 (20)
verify L125: 103/103 righe coperte · sovrapposti = 0 · max(line) = 4266
```

`ships.txt` è il **quinto file di grandi dimensioni chiuso** della campagna recente e porta i **file completi a
quarantacinque**.

## Tre asserzioni vuote, scritte

Questo lotto non ha né `VALUE` né token: entrambi i controlli sono **asserzioni** (`not [...]`, `== {}`), non
omissioni. Con un file di sole descrizioni la tentazione di saltarli è massima, ed è esattamente il caso in cui un
token o un nome di nave tradotto per errore passerebbe inosservato.

## Le virgolette restano inglesi dove sono nomi

L'unità 1 ha **6 virgolette** (`"Nest"`, `"Hauler II: Type F"`, `"Roost"`), l'unità 7 ne ha **6** (`"Type F"`,
`"Hauler III: Type F"`, `"Skein"`), l'unità 6 ne ha **2** (il detto «inutile come un cannone blaster su uno
shuttle»). I nomi dei pod e dei modelli restano inglesi; il detto è tradotto.

## Contenuto

- **Portatrici civili**: Roost (Hauler II Type F), Skein (Hauler III Type F).
- **Navi da guerra**: Saber, Splinter, Vanguard, Valkyrie (Aerie modificate).
- **Piccole e diffuse**: Scoutship, Shuttle, Sparrow, Wasp, Scrapper.
- **Carico e miniera**: CT-50 Star Barge, Sunder, Surveillance Drone.
- **Lusso e nostalgia**: Star Queen.

## Verifica

```bash
cd staging/editorial/L125_20261019_072624
python mkparts.py   # 20 unità · 20 testi distinti · 0 VALUE · 0 token · 1 nota da L123/L124
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # exit 0 (29 controlli) — 103/103 righe coperte, sovrapposti 0
```
