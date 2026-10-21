# STATO — L239 (`data/avgi/avgi jobs.txt`, righe 20–656)

**Stato: CHIUSO.** Primo lotto del file, **62 unità** (31 `VALUE` + 31 `DESCRIPTION`). Il file resta **aperto a 62/102
(60,8%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L239_20261020_134411/` |
| file | `data/avgi/avgi jobs.txt` (102 unità · 902 parole; 51 `VALUE` + 51 `DESCRIPTION`) |
| righe | 20–656 |
| unità | **62** — **31 `VALUE`** (invariati) + **31 `DESCRIPTION`** (tradotte) |
| parole | **432 EN → 483 IT** |
| rapporto | **0,97 – 1,22** (media 1,06), gate 0,55–1,90 |
| contesti | **31**, due unità ciascuno — da `Avgi: Small Cargo 1 (Generic)` a `Avgi: Outpost Diplomats 3` |
| tab / virgolette / apici | **0 / 0 / 0** (tre asserzioni negative scritte) |
| segnaposto | **133** in 6 famiglie: `<planet>` 31, `<destination>` 31, `<payment>` 31, `<cargo>` 24, `<date>` 9, `<bunks>` 7 |
| famiglie `DESCRIPTION` | **6** (15 · 9 · 2 · 2 · 1 · 2), una sola resa ciascuna |
| famiglie `VALUE` | **6** (9 · 6 · 9 · 2 · 2 · 3), tutte invariate |
| `check.py` | **30 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima · 62 qui · 40 dopo · confine riga **684** |
| copertura del file | **62/102 (60,8%)**, stampata e non asserita |
| `sha256[:16]` | **`09003f2358701239`** |

## Comandi

```bash
python staging/editorial/L239_20261020_134411/check.py     # FAIL totale: 0 (30 controlli)
python staging/editorial/L239_20261020_134411/verify.py    # FAIL: 0 (22 controlli, 62/102)
```

## Cosa contiene

Trentuno lavori della bacheca Avgi, in sei famiglie: **carico piccolo** (9 contesti `Cargo to <planet>`), **carico
sfuso** (6 `Bulk cargo to <planet>`), **consegna urgente** (9 `Rush delivery to <planet>` con `<date>`), **specialisti**
(2), **ricercatori** (2, alla stazione di ricerca), **diplomatici** (3: negoziare con operai scontenti, placare gli Avgi
scontenti, e la terza variante identica alla seconda). Le `DESCRIPTION` sono sei stringhe distinte: quindici copie di
«Consegna `<cargo>` su `<destination>`. Il pagamento è `<payment>`.», nove di «`<destination>` ha urgente bisogno di una
partita di `<cargo>` entro il `<date>`. …», e le quattro formule con `<bunks>`.

## Limiti dichiarati

Nessuna approvazione (62 unità `PENDING`), nessun lavoro visto nel gioco, nessuna revisione umana.
