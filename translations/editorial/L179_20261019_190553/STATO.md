# STATO — L179 · `avgi ships.txt` (Optikon, Sonikis) — **CHIUDE IL FILE: 102/102**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L179_20261019_190553` |
| Righe / unità | **2716–2770** / **5** — file al **102/102 (100%)** |
| Tipi | **4 `DESCRIPTION`** · **1 `VALUE`** |
| `UI_LABEL` · token · virgolette | **0** · **0** · **0** — tre asserzioni vuote scritte |
| Contesti | **2** (2 + 3) · **4 testi distinti** su 5 |
| Parole | **213 EN → 226 IT** (1,061) · rapporto **1,12–1,18**, media **1,14** |
| Tab | **2** (idx 2 e 5) |
| Apici | **0** in inglese · nessun possessivo in italiano |
| sha256 | `70939f2fd79d9f22…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **23**, exit **0** (**invariante di file**) |

## Il boilerplate, verificato **contro L178**

Le due righe sui droni (idx 2 e 5) sono le stesse che il gioco ripete in L178 (idx 10 e 14). La resa è **identica alla
lettera**: il `check.py` **legge il `translation.json` di L178** e confronta, invece di fidarsi della memoria. Il campo
`english` contiene il **tab iniziale**, quindi il confronto si fa con `lstrip('\t')` — dettaglio che al primo giro ha
fatto fallire il controllo (e non la resa).

## Cosa contiene

| mezzo | unità | righe | contenuto |
|---|---|---|---|
| `Optikon Sensor Platform` | 1-2 | 2716-2717 | dalle sonde `starwisp` a propulsione laser alla piattaforma sensoriale dispiegabile |
| `Sonikis Utility Drone` | 3-5 | 2721-2770 | drone cargo interorbitale economico, oggi usato per carico e minerali |

## File CHIUSO

```
102/102 unità (100%) · 6 finestre (L174…L179) · 97 prima / 5 nel lotto / 0 dopo
102 righe rivendicate, 102 distinte · min(line) 120 · max(line) 2770 · nessun buco
2528 EN -> 2669 IT su tutto il file
```

## Verifica

```bash
cd staging/editorial/L179_20261019_190553
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (23 controlli, invariante di FILE)
```

**Non verificato**: nessun mezzo visto a schermo; i testi non sono stati caricati nel gioco.
