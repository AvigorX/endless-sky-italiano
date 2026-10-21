# STATO — L177 · `avgi ships.txt` (39 unità, 29 nomi: Interferos, Diaspersi, Refraktos, Difraktos, Atenuatia)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L177_20261019_185723` |
| Righe / unità | **1415–2337** / **39** — file all'**83/102 (81,4%)** |
| Tipi | **29 `TEXT`** (nomi) · **7 `DESCRIPTION`** · **3 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Contesti | **5** (7 + 8 + 7 + 11 + 6) · **15 testi distinti** su 39 |
| Parole | **467 EN → 509 IT** (1,090) · rapporto DESCRIPTION **1,06–1,30**, media **1,16** |
| Tab · virgolette | **2** (idx 19, 20) · **58** (= 2 per `TEXT`) |
| Apici | **0** in inglese · nessun possessivo in italiano |
| sha256 | `e962a9325deb075f…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **23**, exit **0** |

## I 29 nomi, contati

| nome | volte |
|---|---|
| `Z-333 "Spark" Fusion Torch` | **11** |
| `"Nettle" KKV` | **6** |
| `"Orchid" Nuclear Missile` | 5 |
| `Z-666 "Zap" Fusion Torch` | 5 |
| `"Ophrys" Nuclear Torpedo` | 2 |

**58 virgolette** = 29 × 2, esattamente 2 per nome, in entrambe le lingue. Zero virgolette fuori dai `TEXT`.

## Le sette `DESCRIPTION` (tradotte)

| nave | unità | righe | contenuto |
|---|---|---|---|
| `Interferos` | 3 | 1498 | fregata di supporto «usa e getta», venduta in licenza ai mercanti |
| `Diaspersi` | 10 | 1666 | portaerei di scorta leggera, due stormi di droni e uno di caccia |
| `Refraktos` | 18-20 | 1830-1832 | *laserstar*: radiatori enormi, corazza leggera, ruolo antimissile |
| `Difraktos` | 26 | 2002 | incrociatore multiruolo: cinetico, missilistico o via di mezzo |
| `Atenuatia` | 36 | 2316 | portaerei di flotta, sei stormi di droni e due di bombardieri |

## Verifica

```bash
cd staging/editorial/L177_20261019_185723
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (23 controlli)
```

**Non verificato**: nessuna astronave vista a schermo; i testi non sono stati caricati nel gioco.
