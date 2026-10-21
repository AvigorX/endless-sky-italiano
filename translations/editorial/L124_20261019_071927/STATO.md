# STATO — L124 · `data/human/ships.txt` (secondo lotto: 29 unità, 24 contesti)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L124_20261019_071927` |
| Righe / unità | **2102–3422** / **29** |
| Tipi | **28 `DESCRIPTION`** · **1 `VALUE`** |
| Stati | **29 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **24** — 19×1, 5×2 |
| Testi distinti | **29** per 29 unità — **nessuna ripetizione** nel segmento |
| Parole | **1539 EN → 1603 IT** (1,042); per unità 0,88–1,29, media 1,07 |
| Tab | **3 unità** (9, 12, 17) |
| Virgolette | **14**, nelle unità 8, 9, 10, 20, 23 e 26 |
| Token · quadre | **0** · **0** — asserzioni scritte |
| sha256 | `5b6c5456b299d979…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** — invariante di **segmento** |

## Un solo `VALUE`, due note riprese

L'unico nome di nave del segmento è `Modified Argosies` (unità 18, riga 2822): **plurale**, **identico** al sorgente
per la decisione 259. Il `check.py` lo elenca esattamente (`VAL == [18]`), non con un «tutti i `VALUE` tranne…».

Le due note tecniche — «Fighters do not come equipped with a hyperdrive…» (unità 12) e «Drones do not come equipped…»
(unità 17) — sono **le stesse di L123**, e la resa è stata **riletta** dal `translation.json` di quel lotto e
confrontata: la stessa nota non cambia forma a un lotto di distanza.

## La forma si alleggerisce

| | L123 | **L124** |
|---|---|---|
| unità | 54 | **29** |
| contesti | 33 | **24** (19 da una sola nave) |
| tab | 14 | **3** |
| virgolette | 16 | 14 |
| testi distinti | 48 su 54 | **29 su 29** |
| `VALUE` | 6 | **1** |

## Contenuto

- **Marina**: Gunboat, Lance, Monitor, Rainmaker.
- **Navi da carico**: Hauler, Hauler II, Hauler III, Nest, Mule.
- **Caccia e droni**: Lance, Mining Drone, Nest (portatrice di Finch).
- **Pirati e contrabbandieri**: Jackal, Mammoth, Modified Argosy, Nighthawk.
- **Civili**: Heavy Shuttle, Hogshead, Hawk, Headhunter, Leviathan, Manta, Osprey, Protector, Quicksilver, Raven.

## Verifica

```bash
cd staging/editorial/L124_20261019_071927
python mkparts.py   # 29 unità · 29 testi distinti · 1 VALUE · 2 note da L123 · 3 tab · 14 virgolette
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # exit 0 (27 controlli)
```
