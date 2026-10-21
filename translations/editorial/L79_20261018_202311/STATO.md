# STATO — L79 · `data/successors/successor side missions.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L79_20261018_202311` |
| Righe / unità | **336–381** (finestra 326–400) / **29** |
| Parti | **2** — 15 · 14 |
| Contesto | **1 intero** — `People's Houses: First Contact` |
| Tipi | **29 `MISSION_TEXT`** — nessun altro tipo |
| Parole | 620 EN → 611 IT (**0,985**) |
| Rapporto per unità | **0,75 – 1,25** |
| Assenze dichiarate | `VALUE`, `DESCRIPTION`, `UI_LABEL`, `LOGBOOK`, `DIALOG`, `CONVERSATION`, `TEXT` = **0** |
| Virgolette dispari | **3 — (10, 22, 27)**, tutte aprono e non chiudono |
| Token `<…>` | **0 — `0 = 0`** (assenza asserita) |
| Tab · virgolette | **28** su **28** unità · **33** |
| Duplicati | **3 gruppi** — 22/27, 23/28, 18/24/29 |
| sha256 | `54af11093d844256…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 336 | **116** (L77 + L78) |
| Unità dopo la riga 381 | **19** |
| File | **164 unità**, `max(line) = 453` |
| Confine dopo | riga **416** apre `mission:Successors: Unified Defense` |
| Copertura | **145/164 (88,4%)** |

## Cosa è stato deciso qui

1. **`Old Houses` → «Vecchie Casate»**, **`New Houses` → «Nuove Casate»**, **`People's Houses` → «Casate del
   Popolo»** (forma fissa da L45/L68): il lotto le mette tutte e tre in opposizione, e le tiene distinte.
2. **`outcasts of the Houses New` → «reietti delle Casate Nuove»**: l'ordine aggettivale inglese si scioglie,
   il disprezzo resta nella parola «reietti».
3. **`indolent fool` → «stolto indolente»**, **`buried fool` → «stolto sepolto»**: due insulti diversi, due
   rese diverse — e il secondo torna in 23/28, identico perché l'inglese è identico.
4. **Tre virgolette dispari** (10, 22, 27): tre battute che aprono e non chiudono. Riprodotte; il
   `verify.py` verifica l'insieme, la direzione, e che **le altre** siano bilanciate.
5. **`flight knave`/`flighty knave` → «furfante volubile»**; **`toe the line` → «startene in riga»**.
6. **`their dagger nests` → «il loro pugnale ti niderà nella schiena»**: metafora cruda, mantenuta.

## Verifica

```bash
cd staging/editorial/L79_20261018_202311
python check.py   # FAIL totale: 0   (32 controlli)
python verify.py  # exit 0           (36 controlli)
```

## Prossimo passo

**L80 chiude il file**: righe **401–460** (prima unità alla **416**), **19 unità** in **un contesto**
(`Unified Defense`), **363 parole**, tab **11** su 11 unità, virgolette **20**, **0 dispari**, **0 token**,
**4 `UI_LABEL`**. Invariante **di file**: `164/164`, `max(line) = 453`, **0 unità dopo**.
