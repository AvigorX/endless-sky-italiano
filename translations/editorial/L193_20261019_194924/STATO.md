# STATO — L193 · `bunrodea missions.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L193_20261019_194924` |
| Righe / unità | **92–150** / **30** — file al **54/77 (70,1%)** |
| Tipi | {'MISSION_TEXT': 30} |
| Tab · virgolette | **30** · **60** |
| Contesti | **1** (una sola missione) · **27** testi distinti |
| Parole | **500 EN → 463 IT** |
| Apici | **7** inglesi · **4** italiani |
| sha256 | `0ba103f679e3b8cc…` |
| Esiti | `check.py` **23** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| l'interprete | 1-16 | 92-117 | la creatura a sei arti impara l'inglese, «Salve», i cento anni |
| il palazzo | 17-20 | 118-121 | le scale, i corridoi, la sala del trono |
| l'interrogatorio | 21-30 | 128-150 | Megasa, civili, guardia: tre accuse |

## Difficoltà

1. **30 unità, 30 tab, 60 virgolette**: il lotto più «parlato» della serie; ogni unità ha un numero pari di virgolette.
2. **Le tre battute ripetute** (idx 23=27, 24=28, 25=29) devono avere la stessa resa.
3. **`Megasa` resta invariato** (nome di specie).
4. Un'asserzione sbagliata (mia): contavo 4 occorrenze di «Umano» in idx 13; sono **5**, come gli `Human` inglesi.

## Verifica

```bash
cd staging/editorial/L193_20261019_194924
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # exit 0 (21 controlli)
```

**Non verificato**: nessuna missione giocata; i testi non sono stati caricati nel gioco.
