# STATO — L195 · `bunrodea missions.txt` (quinto lotto: **chiude il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L195_20261019_195116` |
| Righe / unità | **207–219** / **5** — file al **77/77 (100%)** |
| Tipi | {'MISSION_TEXT': 5} |
| Tab · virgolette | **5** · **10** |
| Contesti | **1** (una sola missione) · **5** testi distinti |
| Parole | **397 EN → 361 IT** |
| Apici | **1** inglesi · **0** italiani |
| sha256 | `a75a3d4708ee72a5…` |
| Esiti | `check.py` **20** (`FAIL 0`) · `verify.py` **17**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| le scuse accettate | 1 | 207 | «Una scusa. Una risposta davvero... inattesa» |
| le tre concessioni | 2-4 | 208-216 | scuse, clemenza, guardie: stessa coda, aperture diverse |
| l'uscita | 5 | 219 | le scale, di nuovo, e la lunga discesa |

## Difficoltà

1. **Il lotto chiude il file**: il `verify.py` usa l'**invariante di FILE** sulle 5 finestre L191…L195 = **77/77** unità su 77 righe distinte.
2. **idx 2, 3 e 4** hanno la stessa coda e aperture diverse: il controllo confronta le code, non solo le aperture.
3. Nessun testo dopo la riga 219: l'asserzione terminale sostituisce il confronto con il confine.

## Verifica

```bash
cd staging/editorial/L195_20261019_195116
python check.py     # FAIL totale: 0 (20 controlli)
python verify.py    # exit 0 (17 controlli)
```

**Non verificato**: nessuna missione giocata; i testi non sono stati caricati nel gioco.
