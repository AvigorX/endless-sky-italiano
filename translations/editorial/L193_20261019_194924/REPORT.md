# REPORT — L193 · `bunrodea missions.txt`

## 1. Contenuto

Il cuore della missione: l'interprete che impara la lingua, la traversata del palazzo e l'inizio dell'interrogatorio.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| l'interprete | 1-16 | 92-117 | la creatura a sei arti impara l'inglese, «Salve», i cento anni |
| il palazzo | 17-20 | 118-121 | le scale, i corridoi, la sala del trono |
| l'interrogatorio | 21-30 | 128-150 | Megasa, civili, guardia: tre accuse |

## 2. Difficoltà

1. **30 unità, 30 tab, 60 virgolette**: il lotto più «parlato» della serie; ogni unità ha un numero pari di virgolette.
2. **Le tre battute ripetute** (idx 23=27, 24=28, 25=29) devono avere la stessa resa.
3. **`Megasa` resta invariato** (nome di specie).
4. Un'asserzione sbagliata (mia): contavo 4 occorrenze di «Umano» in idx 13; sono **5**, come gli `Human` inglesi.

## 3. Numeri osservati

```
unita' 30 · {'MISSION_TEXT': 30} · tutte PENDING
30 tab · 60 virgolette · 7 apici EN · 4 apici IT
27 testi distinti · 1 contesto · righe 92/150
parole 500 -> 463
FAIL totale: 0 (23 controlli) · verify exit 0 (21 controlli) · sha256[:16] 0ba103f679e3b8cc
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23 controlli), `verify.py` exit **0** (21 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 30 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
