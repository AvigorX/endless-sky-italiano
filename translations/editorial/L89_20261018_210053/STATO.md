# STATO — L89 · `data/successors/successor outfits.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L89_20261018_210053` |
| Righe / unità | **574–647** (finestra 561–700) / **12** |
| Tipi | **12 `DESCRIPTION`** — nessun dato |
| Contesti | **6** in ordine di riga (`Multimodal Armor: Light` … `Radiant Shield Shunt`) |
| Parole | **347 EN → 388 IT** (1,118); per unità 1,01–1,27 |
| Tab · virgolette | **6** (unità 2, 4, 6, 8, 11, 12) · **0** |
| Duplicato legittimo | **1 / 3 / 5 / 7**: la frase sull'armatura in metamateriale, resa identica |
| Token | **0** |
| sha256 | `c49081b925bee187…` |
| `check.py` | **23 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 574 | **44** (L86–L88) |
| Unità dopo la riga 647 | **0** |
| File | **56 unità**, `max(line) = 647` |
| Copertura | **56/56 (100%)** — 56 id distinti, 56 righe |
| Lotti | **4** — L86 (21), L87 (13), L88 (10), L89 (12) |
| Parole del file | **2.269 EN → 2.364 IT** |

`successor outfits.txt` è il **trentaseiesimo file completo**, **non approvato**: 56 unità `PENDING`.

## Contenuto

Le quattro varianti dell'**armatura in metamateriale** (`Light`: vuoti nanometrici che riducono la massa;
`Heavy`: legami atomici rafforzati; `Regen`: plasticità che migliora le riparazioni in combattimento;
`Keystone`: attraversamento sicuro dei wormhole instabili, a costo di interferenze sulle scansioni), il
**fucile railgun** «particolarmente terrificante» che perfora armature personali e paratie, e lo **shunt di
scudi radioso** concesso da Casa Kaatrij — «non somiglia a nulla di ciò che avete visto, punto».

## Verifica

```bash
cd staging/editorial/L89_20261018_210053
python check.py   # FAIL totale: 0
python verify.py  # exit 0 (invariante di file)
```
