# STATO — L172 · `paradise world jobs.txt` (sei missioni di soccorso per Martini)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L172_20261019_183436` |
| Righe / unità | **1230–1336** / **12** — file al **125/131 (95,4%)** |
| Tipi | **6 `VALUE`** · **6 `DESCRIPTION`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **18** su **3 soli simboli**: `<cargo>` 6, `<planet>` 6, `<payment>` 6 |
| Contesti | **6** · **8 testi distinti** su 12 |
| Parole | **217 EN → 247 IT** (1,138); **1,00–1,29**, media **1,13** |
| Tab · virgolette · apici | **0** · **0** · **0** |
| sha256 | `ef8c776e39355c03…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **20**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| cure mediche | 1-4 | 1230-1272 | due missioni identiche (`Medical [0]` e `[1]`): curare i feriti |
| ricostruzione | 5-6 | 1272-1293 | materiali da costruzione |
| scorte | 7-12 | 1293-1336 | cibo, pastiglie per l'acqua, ritardante antincendio |

## La formula (identica in tutte e sei le coppie)

```
A causa dei recenti bombardamenti nucleari, porta <cargo> su <planet> per <SCOPO>.
Dovrai chiamare via radio il controllore dello spazioporto per ottenere il permesso di scendere sul pianeta.
Il compenso è di <payment>.
```

| scopo | unità |
|---|---|
| `help treat the wounded` | **aiutare a curare i feriti** | 2, 4 |
| `help the reconstruction efforts` | **aiutare gli sforzi di ricostruzione** | 6 |
| `help keep up supply` | **aiutare a mantenere le scorte** | 8, 10, 12 |

## Ripetizioni verificate

- **`VALUE`**: 1 = 3 (`Disaster relief to Martini`) → 5 distinti su 6;
- **`DESCRIPTION`**: 2 = 4 (Medical `[0]`/`[1]`), 8 = 10 = 12 (le tre «scorte») → **3 distinte su 6**;
- totale: **8 testi distinti** su 12 unità.

## Verifica

```bash
cd staging/editorial/L172_20261019_183436
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (20 controlli)
```

**Non verificato**: nessuna missione vista a schermo; i testi non sono stati caricati nel gioco.
