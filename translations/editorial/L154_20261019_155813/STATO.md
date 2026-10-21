# STATO — L154 · `coalition jobs.txt` (i lavori Heliarch e le nove consegne del Lunarium (chiude il file))

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L154_20261019_155813` |
| Righe / unità | **1475–1807** / **41** — file al **197/197 (100%)** |
| Tipi | 15 `DIALOG` · 13 `VALUE` · 13 `DESCRIPTION` |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **57** su **7** simboli |
| Contesti | **13** · **40 testi distinti** su 41 unità |
| Parole | **725 EN → 721 IT** (0.994); **0.87–1.20** |
| Tab · virgolette | **0 unità** · **0** |
| sha256 | `38054e95406a979e…` |
| Esiti | `check.py` **29** (`FAIL 0`) · `verify.py` **28**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| prigionieri | 1-3 | 1475-1493 | `Transport Prisoners`, la scorta, il pagamento |
| indagine | 4-7 | 1499-1517 | `Investigate signs of criminal activity`, gli agenti, le prove |
| evacuazione riuscita | 8-11 | 1523-1550 | `Rescue Lunarium Members`, l'imbarco, il ringraziamento |
| evacuazione fallita | 12-14 | 1555-1576 | stesso lavoro, gli Heliarch arrivati prima |
| nove consegne Lunarium | 15-41 | 1583-1807 | reattori, lanciatori, torrette, granate: nove `VALUE` + nove `DESCRIPTION` + nove `DIALOG` |

## Rese che contano

| EN | IT |
|---|---|
| `Transport Prisoners` · `Investigate…` · `Rescue Lunarium Members` · `X Delivery` | **identici** (13 `VALUE`) |
| `Payment is <payment>.` | **Il compenso è di `<payment>`.** |
| `Pick up <bunks> … by <date>.` | **Preleva `<bunks>` … entro il `<date>`.** |
| `The Lunarium is offering <payment> for you to deliver …` | **Il Lunarium offre `<payment>` per consegnare …** |
| `as instructed` | **come richiesto** |
| `quietly transporting the reactor / the turret / the grenades / the cargo away` | **portare via il reattore / la torretta / le granate / il carico in silenzio** |

## Verifica

```bash
cd staging/editorial/L154_20261019_155813
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (28 controlli)
```

**Il lotto **chiude** `coalition jobs.txt`: l'invariante è di **file** (8 finestre = 197 righe distinte, `max(line) = 1807`).**

**Non verificato**: nessuna missione o arma vista a schermo; i testi non sono stati caricati nel gioco.
