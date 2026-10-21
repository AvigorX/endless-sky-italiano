# STATO — L139 · `data/starts.txt` (le ultime due unità: **chiude il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L139_20261019_144407` |
| Righe / unità | **365–366** / **2** — ultima unità del file |
| Tipi | **2 `TEXT`** — nomi di equipaggiamento |
| `VALUE` · `UI_LABEL` · token | **0** · **0** · **0** — **tre asserzioni vuote scritte** |
| Stati | **2 `PENDING`** — misurato e **asserito** |
| Contesto | **1** — `ship:Grasshopper` |
| Testi | **2**, identici al sorgente (`ID_OK`) |
| Parole | **6 EN → 6 IT** (1,00) |
| Tab · virgolette | **0** · **4** (due per nome, e fanno parte del nome) |
| sha256 | `1ceb216ebf1e03c6…` |
| `check.py` | **21 controlli**, `FAIL totale: 0` |
| `verify.py` | **22 controlli**, exit **0** — invariante di **file** |

## Il file è chiuso: 113/113

```
L135   32 unità (18–130)
L136   15 unità (135–167)
L137   17 unità (172–210)
L138   47 unità (215–358)
L139    2 unità (365–366)
--------------------------------
file  113/113 righe coperte · sovrapposti = 0 · max(line) = 366
```

`starts.txt` è il **quarantanovesimo file completo** (4.236 EN → 4.094 IT, cinque lotti). Il totale viene dalla
**somma dei lotti**, non da un numero scritto a mano.

## Due nomi, non due traduzioni

| unità | sorgente | resa |
|---|---|---|
| 365 | `"Benga" Atomic Thruster` | **identico** |
| 366 | `"Biroo" Atomic Steering` | **identico** |

Sono **nomi di equipaggiamento** del Grasshopper. Le virgolette fanno parte del nome — non sono dialogo, e non si
traducono più di quanto si tradurrebbe `Grasshopper`. La lista `ID_OK` li dichiara identici e un controllo li verifica
**uno per uno**, invece di escluderli dal conteggio delle unità tradotte:

```python
ck('ID_OK dichiarata e usata (non esclusa dai controlli)',
   all(by[k]['italian'] == ID_OK[k] == by[k]['english'] for k in ID_OK))
```

## Il `raw` ha tab e backtick che il testo non ha

La riga del sorgente è:

```
\t\t`"Benga" Atomic Thruster`
```

Tab e backtick stanno **fuori** dal campo `english` (il gioco li usa per marcare il nome). Per questo il lotto ha
**zero tab** e **zero backtick** nel testo, e un controllo verifica che il campo `english` **non** inizi con un tab:
era il modo più facile per sbagliare questo lotto.

## Verifica

```bash
cd staging/editorial/L139_20261019_144407
python mkparts.py   # 2 unità · 2 testi identici (ID_OK) · 1 contesto · 4 virgolette
python check.py     # FAIL totale: 0 (21 controlli)
python verify.py    # exit 0 (22 controlli, invariante di file)
```

**Non verificato**: nessuna nave acquistata nel gioco; i nomi dei propulsori non sono stati visti a schermo.
