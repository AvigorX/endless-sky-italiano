# STATO — L178 · `avgi ships.txt` (Akoustiki, Photikon, Vibratia, Undulon — e due boilerplate)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L178_20261019_190210` |
| Righe / unità | **2424–2667** / **14** — file al **97/102 (95,1%)** |
| Tipi | **10 `DESCRIPTION`** · **3 `TEXT`** · **1 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Contesti | **4** (2 + 5 + 3 + 4) · **12 testi distinti** su 14 |
| Parole | **418 EN → 448 IT** (1,072) · rapporto DESCRIPTION **1,06–1,24**, media **1,11** |
| Tab · virgolette | **6** (idx 2, 4, 5, 10, 13, 14) · **6** (2 per `TEXT`) |
| Apici | **0** in inglese · nessun possessivo in italiano |
| sha256 | `7cf03810fb0ffea8…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **23**, exit **0** |

## Il boilerplate, trattato come testo vero

Due coppie di righe identiche nel sorgente, ripetute nel gioco sotto ogni caccia e ogni drone:

| unità | testo | resa |
|---|---|---|
| 2 e 5 | `Fighters do not come equipped with a hyperdrive...` | **I caccia non sono dotati di iperguida...** (identiche) |
| 10 e 14 | `Drones do not come equipped with a hyperdrive...` | **I droni non sono dotati di iperguida...** (identiche) |

Un controllo pretende che **2 = 5** e **10 = 14**, e che **2 ≠ 10**: «caccia» e «droni» non si possono confondere, anche
se la frase è la stessa.

## Cosa contiene

| mezzo | unità | righe | contenuto |
|---|---|---|---|
| `Akoustiki Excursion Vehicle` | 1-2 | 2424-2425 | capsula di servizio, manutenzione, riprese come mezzo minerario |
| `Photikon` | 3-7 | 2500-2532 | bombardiere silurante, dottrina antisuperficie, siluro nucleare a corto raggio |
| `Vibratia` | 8-10 | 2532-2594 | intercettore d'attacco, fragile ma in sciami |
| `Undulon` | 11-14 | 2625-2667 | silo orbitale, cannone fisso, costruzione cava |

## Verifica

```bash
cd staging/editorial/L178_20261019_190210
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (23 controlli)
```

**Non verificato**: nessun mezzo visto a schermo; i testi non sono stati caricati nel gioco.
