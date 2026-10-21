# REPORT — L195 · `bunrodea missions.txt`

## 1. Contenuto

La chiusura: la Regina accetta le scuse, concede la vita con tre formule diverse e caccia il giocatore dalla corte.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| le scuse accettate | 1 | 207 | «Una scusa. Una risposta davvero... inattesa» |
| le tre concessioni | 2-4 | 208-216 | scuse, clemenza, guardie: stessa coda, aperture diverse |
| l'uscita | 5 | 219 | le scale, di nuovo, e la lunga discesa |

## 2. Difficoltà

1. **Il lotto chiude il file**: il `verify.py` usa l'**invariante di FILE** sulle 5 finestre L191…L195 = **77/77** unità su 77 righe distinte.
2. **idx 2, 3 e 4** hanno la stessa coda e aperture diverse: il controllo confronta le code, non solo le aperture.
3. Nessun testo dopo la riga 219: l'asserzione terminale sostituisce il confronto con il confine.

## 3. Numeri osservati

```
unita' 5 · {'MISSION_TEXT': 5} · tutte PENDING
5 tab · 10 virgolette · 1 apici EN · 0 apici IT
5 testi distinti · 1 contesto · righe 207/219
parole 397 -> 361
FAIL totale: 0 (20 controlli) · verify exit 0 (17 controlli) · sha256[:16] a75a3d4708ee72a5
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (20 controlli), `verify.py` exit **0** (17 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 5 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
