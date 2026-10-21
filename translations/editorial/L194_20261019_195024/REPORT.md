# REPORT — L194 · `bunrodea missions.txt`

## 1. Contenuto

Le risposte al trono: i tre ranghi offesi e i tre discorsi della Regina, che condividono la seconda metà.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| le risposte | 1-4 | 152-158 | difesa, merito, scuse, «e allora?» |
| i tre ranghi | 5-11 | 162-179 | `Erabu`, `Megasa`, guardia reale |
| le code della Regina | 12-18 | 183-203 | la clemenza e l'ammonimento |

## 2. Difficoltà

1. **Sette battute sono ripetizioni testuali di L193** (`I was only defending myself`, `I have, and for that I apologize`, `Okay, and?`, `Your what?`): il `check.py` **legge il `translation.json` di L193** e confronta.
2. **idx 15 e 16** condividono la coda del discorso; **idx 17 e 18** differiscono in una parola (`mentire` / `parlare`).
3. Due asserzioni sbagliate (mie): il conteggio dei testi distinti (**14**, non 18) e una catena `a in b == c` che in Python non significa quello che sembrava.

## 3. Numeri osservati

```
unita' 18 · {'MISSION_TEXT': 18} · tutte PENDING
18 tab · 48 virgolette · 2 apici EN · 0 apici IT
14 testi distinti · 1 contesto · righe 152/203
parole 488 -> 479
FAIL totale: 0 (21 controlli) · verify exit 0 (21 controlli) · sha256[:16] 5b5071523577ff54
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (21 controlli), `verify.py` exit **0** (21 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 18 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
