# STATO — L131 · `boarding missions.txt` (coda: **chiude il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L131_20261019_123356` |
| Righe / unità | **695–959** / **76** — ultima unità del file |
| Tipi | **75 `MISSION_TEXT`** · **1 `DESCRIPTION`** |
| `VALUE` · `UI_LABEL` | **0** · **0** — due **asserzioni vuote scritte** (`== []`) |
| Stati | **76 `PENDING`** — misurato e **asserito** |
| Contesti | **2** — 1 / 75 |
| Testi distinti | **52** per 76 unità — **24 ripetizioni** |
| Parole | **1632 EN → 1594 IT** (0,977); per unità 0,83–1,80, media 1,07 |
| Tab · virgolette | **74 unità** · **2** (unità 60, `"astronavi ostili"`) |
| Token | **22** in **2 famiglie**: `<origin>` 14, `<payment>` 8 |
| sha256 | `ec991eb6a0c3f258…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **31 controlli**, exit **0** — invariante di **file** |

## Il file è chiuso: 240/240

`verify.py` legge i **tre** `translation.json` del percorso e dimostra:

```
L129  89 unità (15–386)
L130  75 unità (417–686)
L131  76 unità (695–959)
-----------------------------
file 240/240 righe coperte · sovrapposti = 0 · max(line) = 959
```

Il conteggio viene dalla **somma dei tre lotti** (89 + 75 + 76), non da un numero scritto a mano. `boarding
missions.txt` è il **quarantasettesimo file completo** (4.571 EN → 4.480 IT).

## Le 24 ripetizioni sono la struttura del lotto

Il file genera varianti della stessa scena, quindi le stesse frasi tornano su rami diversi:

| frase | occorrenze |
|---|---|
| «Ci vuole un po', ma riesci a stabilizzare lo scafo…» (cavi rotti, sovratensione) | **4** |
| «Con qualche riparazione semplice riesci a rimettere in funzione…» | **4** |
| «Finite le riparazioni, vai alla cabina di pilotaggio…» | **3** |
| «La nave vibra e prende vita… Successo! La nave è tua.» | **3** |
| «(Fuggi dalla nave, temendo che le mie riparazioni…») | **6** |
| «Mentre ripari i sistemi dei motori, una valvola si apre di colpo…» (due varianti) | 3 + 3 |

Le parti comuni sono **costanti** nel costruttore (`POWER_OK`, `HULL_OK`, `COCKPIT`, `SUCCESS`, `VALVE_OK`,
`VALVE_POWER`, `FLEE`, `BREAK_UP`, `TEAR`), così restano identiche parola per parola e il confronto tra rami è
leggibile. Il `check.py` verifica che le due frasi più ripetute abbiano **quattro** occorrenze ciascuna.

## Due asserzioni vuote

`VALUE` e `UI_LABEL` non hanno unità in questa finestra. Entrambi i controlli sono **scritti**:

```python
ck('ZERO VALUE (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
```

Senza questa forma, «tutto verde» non avrebbe controllato niente.

## Contenuto

- **`Turn in Tarquin`** (unità 1): la `DESCRIPTION` che chiude la missione di L130.
- **`Boarding Derelict`** (unità 2–76): l'abbordaggio del relitto, la scelta tra saccheggiare e riparare, i tre
  ordini di riparazione (motori, scafo, alimentazione) con i loro successi e i loro disastri, la fuga dal relitto che
  esplode, la trappola dei pirati con l'avviso di `"astronavi ostili"` e il virus che svuota il conto.

## Verifica

```bash
cd staging/editorial/L131_20261019_123356
python mkparts.py   # 76 unità · 52 testi distinti · 74 tab · 2 virgolette · 22 token · zero VALUE/UI_LABEL
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # exit 0 (31 controlli, invariante di file)
```
