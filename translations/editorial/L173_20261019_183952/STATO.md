# STATO — L173 · `paradise world jobs.txt` (**chiude il file**: 131/131)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L173_20261019_183952` |
| Righe / unità | **1356–1413** / **6** — file al **131/131 (100%)** |
| Tipi | **3 `VALUE`** · **3 `DESCRIPTION`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **12** su **4** simboli: `<bunks>` 3, **`<martini relief occupations>` 3**, `<planet>` 3, `<payment>` 3 |
| Contesti | **3** · **4 testi distinti** su 6 |
| Parole | **128 EN → 147 IT** (1,148); **1,00–1,24**, media **1,11** |
| Tab · virgolette · apici | **0** · **0** · **1 EN / 0 IT** |
| sha256 | `5a289568b9f21fbf…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **23**, exit **0** (**invariante di file**) |

## Cosa contiene

Tre missioni di soccorso con **lo stesso `VALUE`** (`Relief workers to Martini`) e tre `DESCRIPTION` che differiscono
**solo per lo scopo**:

| unità | scopo |
|---|---|
| 2 | `release demand from overloaded hospitals` → **alleggerire la pressione sugli ospedali sovraccarichi** |
| 4 | `assist in Martini's relief efforts` → **dare man forte agli sforzi di soccorso di Martini** |
| 6 | `assist in the accommodation and reconstruction efforts` → **dare man forte agli sforzi di accoglienza e ricostruzione** |

## File CHIUSO

```
131/131 unità (100%) · 7 finestre (L167…L173) · 125 prima / 6 nel lotto / 0 dopo
131 righe rivendicate, 131 distinte · min(line) 16 · max(line) 1413 · nessun buco
2918 EN -> 3044 IT su tutto il file
```

## Verifica

```bash
cd staging/editorial/L173_20261019_183952
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (23 controlli, invariante di FILE)
```

**Non verificato**: nessuna missione vista a schermo; i testi non sono stati caricati nel gioco.
