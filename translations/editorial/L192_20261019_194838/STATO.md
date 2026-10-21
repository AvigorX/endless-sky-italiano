# STATO — L192 · `bunrodea missions.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L192_20261019_194838` |
| Righe / unità | **64–91** / **12** — file al **24/77 (31,2%)** |
| Tipi | {'MISSION_TEXT': 12} |
| Tab · virgolette | **11** · **0** |
| Contesti | **1** (una sola missione) · **12** testi distinti |
| Parole | **465 EN → 418 IT** |
| Apici | **10** inglesi · **13** italiani |
| sha256 | `6a45d9d51cb156e7…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| l'arrivo | 1-3 | 64-66 | due navi scorta, la metropoli, il palazzo con i gradini |
| le scelte | 4-8 | 68-76 | sedersi, rientrare, colpire il veicolo, uscire |
| le conseguenze | 9-12 | 83-91 | la fuga riuscita, l'attesa, la creatura a sei arti |

## Difficoltà

1. **11 tab** e **zero virgolette** (asserzione vuota scritta).
2. **Le tre scelte** (idx 4, 5, 7) restano brevi e fra parentesi; il controllo impone ≤ 8 parole.
3. **Il veicolo** non è un'arma: «disattiva tutti i repulsori nelle vicinanze», non «distrugge».

## Verifica

```bash
cd staging/editorial/L192_20261019_194838
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessuna missione giocata; i testi non sono stati caricati nel gioco.
