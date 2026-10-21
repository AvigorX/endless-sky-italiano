# STATO — L134 · `unfettered side missions.txt` (coda: **chiude il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L134_20261019_125428` |
| Righe / unità | **494–510** / **8** — ultima unità del file |
| Tipi | **8 `MISSION_TEXT`** |
| `VALUE` · `UI_LABEL` · token | **0** · **0** · **0** — **tre asserzioni vuote scritte** |
| Stati | **8 `PENDING`** — misurato e **asserito** |
| Contesti | **1** — `Undeserved Anomalocaris` |
| Testi distinti | **8** per 8 unità |
| Parole | **356 EN → 323 IT** (0,907); per unità 0,90–1,15, media 1,02 |
| Tab · virgolette | **7 unità** · **13** (unità 6 con **una sola**) |
| sha256 | `173cf3edac2a3208…` |
| `check.py` | **27 controlli**, `FAIL totale: 0` |
| `verify.py` | **32 controlli**, exit **0** — invariante di **file** |

## Il file è chiuso: 159/159

```
L132  84 unità (17–229)
L133  67 unità (237–477)
L134   8 unità (494–510)
-----------------------------
file 159/159 righe coperte · sovrapposti = 0 · max(line) = 510
```

`unfettered side missions.txt` è il **quarantottesimo file completo** (4.418 EN → 3.994 IT, tre lotti). Il conteggio
viene dalla **somma dei tre lotti** (84 + 67 + 8), non da un numero scritto a mano.

## Tre asserzioni vuote, scritte

Questo lotto non ha `VALUE`, non ha `UI_LABEL`, non ha token. Tre controlli di natura diversa, tutti **scritti**:

```python
ck('ZERO VALUE (asserzione vuota scritta)',  [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('ZERO UI_LABEL (asserzione vuota scritta)', [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == [])
ck('ZERO token (asserzione vuota scritta)', collections.Counter(...) == {})
```

Senza questa forma, «tutto verde» non avrebbe controllato niente. È il primo lotto del progetto con **tre** asserzioni
vuote insieme.

## La battuta non chiusa

L'unità 6 apre le virgolette e non le chiude (`"Siamo felici che tu abbia saputo ragionare… adeguato.`). La resa
riproduce **una sola** virgoletta, e il `check.py` verifica che l'unica unità dispari sia quella.

## I nomi che restano

| nome | che cos'è | resa |
|---|---|---|
| `Anomalocaris` | classe di nave Hai | **Anomalocaris** |
| `Lightning Bug` | modello di nave | **Lightning Bug** |
| `Jump Drive` | modulo | **Jump Drive** |
| `Unfettered` · `Hai` | fazioni e specie | invariati |

`Jump Drive` resta in inglese: è il **nome del modulo**, non una descrizione («motore di salto» sarebbe
un'invenzione).

## Contenuto

La folla che accusa il giocatore di non meritare il relitto, l'Unfettered più importante che intima la consegna, le due
scelte (consegnare / rifiutare), la milizia che prende in carico la nave, il capo che propone di portare un `Jump
Drive` «o due» per guadagnare favore, e l'accompagnamento allo spazioporto dove viene consegnata una `Lightning Bug`.

## Verifica

```bash
cd staging/editorial/L134_20261019_125428
python mkparts.py   # 8 unità · 8 testi distinti · 1 contesto · 7 tab · 13 virgolette
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (32 controlli, invariante di file)
```
