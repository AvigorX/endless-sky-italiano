# STATO — L163 · `avgi outfits.txt` (celle solari, il Lantern, ultracapacitori, propulsione elettrica)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L163_20261019_175632` |
| Righe / unità | **209–315** / **14** — file al **35/63 (55,6%)** |
| Tipi | **13 `DESCRIPTION`** · **1 `VALUE`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **7** (Cell 1, Array 2, Photoelectric 3, Lantern 2, Ultracapacitor Cell 2, Bank 2, Drive 2) · **14 testi distinti** |
| Parole | **558 EN → 611 IT** (1,095); **0,96–1,30**, media **1,13** |
| Tab · virgolette | **6 unità** · **0** |
| sha256 | `46d5a2a9c3f0dee5…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **19**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| celle solari | 1-6 | 209-238 | `Concentrating Solar Cell`, `Concentrating Solar Array`, `Photoelectric Laminae` |
| reattore | 7-8 | 252-253 | il `Lantern`, reattore a fissione a nucleo gassoso |
| accumulo | 9-12 | 266-281 | `Ultracapacitor Cell` e `Ultracapacitor Bank` |
| propulsione | 13-14 | 314-315 | il `Magnetoplasma Drive` |

## Rese che contano

| EN | IT |
|---|---|
| `film solar cells` | **celle solari a film sottile** |
| `waste heat` | **calore di scarto** |
| `electrostatic gas core fission reactor` | **reattore a fissione a nucleo gassoso elettrostatico** |
| `magnetohydrodynamic generator` | **generatore magnetoidrodinamico** |
| `molecule-thin graphene sheets` | **fogli di grafene spessi una molecola** |
| `surface area to volume ratio` | **rapporto fra superficie e volume** |
| `magnetoplasmadynamic thrusters` | **propulsori magnetoplasmadinamici** |
| `six-axis control` | **controllo su sei assi** |

## Verifica

```bash
cd staging/editorial/L163_20261019_175632
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (19 controlli)
```

**Segmento**: 21 unità prima della riga 209, 14 nel lotto, 28 dopo la 315; confine alla riga 337.
**Fedeltà al sorgente**: idx 6 dice `Photovoltaic Laminae` mentre il `VALUE` è `Photoelectric Laminae` — la resa non
normalizza l'incoerenza, e un controllo la pretende.

**Non verificato**: nessuna nave o equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
