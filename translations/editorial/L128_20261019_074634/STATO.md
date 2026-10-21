# STATO — L128 · `data/incipias/incipias first contact.txt` (coda: **chiude il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L128_20261019_074634` |
| Righe / unità | **343–439** / **43** — ultima unità del file |
| Tipi | **33 `MISSION_TEXT`** · **4 `UI_LABEL`** · **3 `LOGBOOK`** · **1 `DIALOG`** · **1 `VALUE`** · **1 `DESCRIPTION`** |
| Stati | **43 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **3** — 2 / 1 / 40 |
| Testi distinti | **43** per 43 unità |
| Parole | **1177 EN → 1100 IT** (0,935); per unità 0,67–1,33, media 1,05 |
| Tab | **30 unità** su 43 |
| Virgolette | **43**, di cui **tre unità con una sola** (28, 30, 36 — battute non chiuse dal sorgente) |
| Token | **6** in **5 famiglie**: `<ship>` 2, `<planet>` 1, `<destination>` 1, `<origin>` 1, `<bunks>` 1 |
| sha256 | `2efab055b9515fde…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **33 controlli**, exit **0** — invariante di **file** |

## Il file è chiuso: 161/161

`verify.py` legge i **tre** `translation.json` del percorso e dimostra:

```
L126  55 unità (22–218)
L127  63 unità (224–331)
L128  43 unità (343–439)
-----------------------------
file 161/161 righe coperte · sovrapposti = 0 · max(line) = 439
```

Il conteggio viene dalla **somma dei tre lotti** (55 + 63 + 43), non da un numero scritto a mano: un lotto duplicato
farebbe scattare `sovrapposti != 0`, e una riga scoperta farebbe scattare «file coperto 161/161».

## Le 4 `UI_LABEL` isolate

`has incipias ship` · `initial choice` · `odd question` · `end no time` (unità 11, 13, 38, 42): **identiche al
sorgente**, escluse da «tutte tradotte», verificate con la lista esatta.

## Il `VALUE` con un token dentro

`Bring Incipias back to <planet>` è un **nome di missione** e resta identico, **token compreso**: il controllo confronta
la stringa intera, non solo la parte prima del token.

## La voce di diario riletta da L127

L'unità 2 ripete **alla lettera** la voce di diario di L127 unità 24. La resa non è stata riscritta a memoria: il
costruttore la **rilegge** dal `translation.json` di L127 e il `check.py` verifica che sia **identica**. Una
ripetizione fra lotti è una copia da dimostrare, non da ricordare.

## Le tre battute non chiuse

Le unità 28, 30 e 36 aprono le virgolette e non le chiudono (il sorgente è così). La resa riproduce **una sola**
virgoletta per unità, e il controllo verifica che le unità dispari siano esattamente quelle tre.

## Verifica

```bash
cd staging/editorial/L128_20261019_074634
python mkparts.py   # 43 unità · 38 prosaici + 4 UI_LABEL + 1 VALUE identici · 3 contesti · 30 tab · 43 virgolette
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (33 controlli, invariante di file)
```
