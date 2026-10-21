# STATO — L194 · `bunrodea missions.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L194_20261019_195024` |
| Righe / unità | **152–203** / **18** — file al **72/77 (93,5%)** |
| Tipi | {'MISSION_TEXT': 18} |
| Tab · virgolette | **18** · **48** |
| Contesti | **1** (una sola missione) · **14** testi distinti |
| Parole | **488 EN → 479 IT** |
| Apici | **2** inglesi · **0** italiani |
| sha256 | `5b5071523577ff54…` |
| Esiti | `check.py` **21** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| le risposte | 1-4 | 152-158 | difesa, merito, scuse, «e allora?» |
| i tre ranghi | 5-11 | 162-179 | `Erabu`, `Megasa`, guardia reale |
| le code della Regina | 12-18 | 183-203 | la clemenza e l'ammonimento |

## Difficoltà

1. **Sette battute sono ripetizioni testuali di L193** (`I was only defending myself`, `I have, and for that I apologize`, `Okay, and?`, `Your what?`): il `check.py` **legge il `translation.json` di L193** e confronta.
2. **idx 15 e 16** condividono la coda del discorso; **idx 17 e 18** differiscono in una parola (`mentire` / `parlare`).
3. Due asserzioni sbagliate (mie): il conteggio dei testi distinti (**14**, non 18) e una catena `a in b == c` che in Python non significa quello che sembrava.

## Verifica

```bash
cd staging/editorial/L194_20261019_195024
python check.py     # FAIL totale: 0 (21 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessuna missione giocata; i testi non sono stati caricati nel gioco.
