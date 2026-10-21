# STATO — L150 · `coalition jobs.txt` (turisti in partenza e in rientro, corriere veloce)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L150_20261019_182440` |
| Righe / unità | **639–794** / **14** — file al **39,6%** (78/197) |
| Tipi | **6 `VALUE`** (identici) · **6 `DESCRIPTION`** · **2 `TEXT`** |
| `LOGBOOK` · `DIALOG` · `UI_LABEL` | **0** · **0** · **0** |
| Token | **33** su **6** simboli — `<commodity>` **una volta sola** |
| Contesti | **8** · **5 testi distinti** |
| Parole | **234 EN → 216 IT** (0,923); **1,00–1,10** |
| Tab · virgolette | **0** · **0** |
| sha256 | `160a1592a36efff5…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **24**, exit **0** |

## Due famiglie che differiscono per due parole

`bring them to <destination>` / `bring them **home** to <destination>`. La resa non si copia: la seconda dice «riportarli
**a casa** a `<destination>`», la prima no. Un controllo verifica che le due rese siano **diverse** e che «riportarli a
casa» compaia solo in quella di rientro.

## `<commodity>`: una volta su 33

Se un errore spostasse `<commodity>`, il totale resterebbe 33 compensato da un altro simbolo. Il controllo lo isola:
una sola occorrenza, e **nell'unità 14**.

## Verifica

```bash
cd staging/editorial/L150_20261019_182440
python mkparts.py   # 14 unità · 6 VALUE + 6 DESCRIPTION + 2 TEXT · 33 token · zero tab · zero virgolette
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (24 controlli, invariante di segmento)
```

**Non verificato**: nessun turista trasportato nel gioco.
