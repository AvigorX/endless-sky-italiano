# L55 — rapporto del lotto

`data/gegno/gegno intro missions.txt` · righe **677–954** · lotto `L55_20261018_173904` ·
**28/28 unità** · **file completo 276/276** con L53 (89) e L54 (159) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **28 / 28** del segmento; **file 276 / 276** (L53 89 + L54 159 + L55 28) |
| parole | 1.061 EN → **1.009 IT** (0,951) |
| contesti | 4 — `Gegno Exploration Nudge` (6) · `Gegno Genocide Defense` (18) · `Gegno Unwelcoming` (3) · **`conversation:interfered with duel`** (1) |
| parti | 1 (28 unità) |
| tab | **14 = 14** |
| virgolette | **34 = 34** |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **0** (assenza dichiarata) |
| quadre `[` `]` · backtick | **0 / 0** (assenze dichiarate) |
| `LOGBOOK` | **0** (assenza dichiarata) |
| `DIALOG` | **0** (assenza dichiarata) |
| `TEXT` | **0** (assenza dichiarata) |
| `CONVERSATION` | **1** (unità 28) — controllo positivo |
| `UI_LABEL` | **4** (12, 14, 16, 21) → `NT` = 4 |
| duplicati inglesi | **1 gruppo** (10, 19: `"I do not care."`) |
| rapporto per unità | 0,88 – 1,09 |
| `check.py` | **FAIL totale: 0** (33 controlli) |
| `verify.py` | **40 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `69eaa9d886a113f0` · `source.json` `1f7ad4a3ee77c55d` · `check.py` `050dc69b856c99f9` · `verify.py` `9971c5c901bf29bf` |

Il segmento **chiude il file**: `verify.py` asserisce `(first, last) == (706, 954)`, **248** unità prima,
**0** dopo, `tot = 276`, `max(line) = 954`, e la copertura **276/276 su tre lotti** senza sovrapposizioni.

## Tipi

21 `MISSION_TEXT` · 4 `UI_LABEL` · 1 `VALUE` · 1 `DESCRIPTION` · **1 `CONVERSATION`**.

## Unità non traducibili (`NT`) — 4

| idx | riga | label |
|---:|---:|---|
| 12 | 801 | `what` |
| 14 | 804 | `care` |
| 16 | 808 | `corroboration provocation` |
| 21 | 819 | `corroboration provocation homeworld` |

Le ultime due sono etichette **composte da più parole**: restano identiche in blocco, non parola per
parola. Nessun riferimento di dato.

## Le 4 missioni/conversazioni del segmento

| idx | riga | contesto | cosa accade |
|---:|---:|---|---|
| 1–6 | 706 | `Gegno Exploration Nudge` | nudge dopo il primo contatto: altre occasioni, ma prudenza |
| 7–24 | 792 | `Gegno Genocide Defense` | l'accusa dei Quarg per aver colpito civili e guardiani, con tre rami di risposta |
| 25–27 | 847 | `Gegno Unwelcoming` | accoglienza ostile e morte del giocatore dopo un assalto ai civili |
| 28 | 954 | `conversation:interfered with duel` | le navi Vi ostili per un duello interrotto |

L'unità 28 è l'unica **`CONVERSATION`** di tutto il file: `verify.py` la controlla come tipo presente
(`CONVERSATION: 1 unita (28), controllo positivo`) e verifica che il contesto cominci per `conversation:`.

## Verifica

```
python staging/editorial/L55_20261018_173904/check.py    → FAIL totale: 0
python staging/editorial/L55_20261018_173904/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **23.531 unità · 751.498 EN · 712.411 IT**, **59 directory** con `translation.json`,
integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica). I file completi sono
**ventinove**.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 28 unità `PENDING` (276 con L53–L54).
- **Nessun caricamento nel gioco**: l'accusa dei Quarg e la scena finale (morte del giocatore sulla
  superficie) non sono mai state viste a schermo.
- **Nessun test della conversazione** (unità 28): è tradotta, ma il suo innesco in gioco non è stato
  verificato.
