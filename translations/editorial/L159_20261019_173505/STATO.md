# STATO — L159 · `weapons.txt` (siluri, Typhoon e razzi pesanti)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L159_20261019_173505` |
| Righe / unità | **1263–1601** / **22** — file al **77/90 (85,6%)** |
| Tipi | 20 `DESCRIPTION` · 2 `VALUE` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **12** · **16 testi distinti** su 22 unità |
| Parole | **576 EN → 593 IT** (1.030); **0.96–1.27** |
| Tab · virgolette | **8 unità** · **0** |
| sha256 | `9e0b0c5d6a3f6cd3…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| siluri | 1-10 | 1263-1390 | `Javelin Turret`, `VALUE` `Torpedoes`, munizione, rack, lanciatore, pod |
| Typhoon | 11-18 | 1414-1521 | `VALUE` `Typhoon Torpedoes`, munizione, tubo, lanciatore, pod |
| razzi pesanti | 19-22 | 1552-1601 | munizione, rack, `Heavy Rocket Launcher` |

## Rese che contano

| EN | IT |
|---|---|
| `Torpedoes` · `Typhoon Torpedoes` | **identici** (2 `VALUE`) |
| `torpedoes` (prosa) | **siluri** |
| `capital ships` | **navi capitali** |
| `proximity trigger` | **detonatore di prossimità** |
| `blast radius` | **raggio d'esplosione** |
| `Heavy Rockets are…` | **I Heavy Rocket sono…** |

## Verifica

```bash
cd staging/editorial/L159_20261019_173505
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Il lotto porta il file all'85,6% e lascia 13 unità al successivo.**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
