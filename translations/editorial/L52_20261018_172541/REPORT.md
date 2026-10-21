# L52 — rapporto del lotto

`data/avgi/avgi 0 first contact.txt` · righe **873–1120** · lotto `L52_20261018_172541` ·
**135/135 unità** · **file completo 406/406** con L50 (119) e L51 (152) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **135 / 135** del segmento; **file 406 / 406** (L50 119 + L51 152 + L52 135) |
| parole | 3.538 EN → **3.373 IT** (0,953) |
| contesti | 5 — `Dissonance Outreach` (16) · `Twilight Escape 1` (60) · `Twilight Escape 2` (15) · `Twilight Escape 3` (42) · `Discovery of Decet Magnetar` (2) |
| parti | 4 — 40 · 36 · 33 · 26 |
| tab | **94 = 94** |
| virgolette | **212 = 212** |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **28 = 28** (6 famiglie: `<first>` 10, `<ship>` 7, `<capacity>` 4, `<last>` 3, `<planet>` 3, `<destination>` 1) |
| quadre `[` `]` · backtick | **0 / 0** (assenze dichiarate) |
| `LOGBOOK` | **17** (10 a tre argomenti, 7 fra backtick, 0 dirette) |
| `DIALOG` | **3** (76, 91, 133) — controllo positivo |
| `UI_LABEL` | **1** (57, `unknown ember waste`) → `NT` = 1 |
| `TEXT` / `CONVERSATION` | **0 / 0** (assenze dichiarate) |
| duplicati inglesi | **0 gruppi** |
| rapporto per unità | 0,68 – 1,60 |
| `check.py` | **FAIL totale: 0** (31 controlli) |
| `verify.py` | **44 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `d529e6f657dc9aef` · `source.json` `6906ea9541620b0e` · `check.py` `238734a884f123eb` · `verify.py` `220b06157231c218` |

Il segmento **chiude il file**: `verify.py` asserisce `(first, last) == (873, 1120)`, **271** unità
prima, **0** dopo, `tot = 406`, `max(line) = 1120`, e la copertura **406/406 su tre lotti** senza
sovrapposizioni.

## Tipi

106 `MISSION_TEXT` · 17 `LOGBOOK` · 4 `VALUE` · 4 `DESCRIPTION` · 3 `DIALOG` · 1 `UI_LABEL` ·
0 `TEXT` · 0 `CONVERSATION`.

## Unità non traducibili (`NT`) — 1

| idx | riga | label |
|---:|---:|---|
| 57 | 975 | `unknown ember waste` |

Nessun riferimento di dato: tutte le 17 righe `LOGBOOK` hanno il testo nell'unità.

## Le 17 righe `log`

| idx | riga | forma | contenuto |
|---:|---:|---|---|
| 4 | 885 | 3 argomenti | **People / Hriso**: diplomatico, simpatia per la Dissonanza |
| 5 | 886 | 3 argomenti | **People / Sora Kun**: giudizio negativo sulla Dissonanza |
| 6 | 887 | 3 argomenti | **Factions / Avgi Consonance**: adesione volontaria e varia |
| 7 | 888 | 3 argomenti | **Factions / Avgi Dissonance**: movimento ampio, non centralizzato |
| 16 | 905 | backtick | accordo per trasportare Hriso alla stazione mineraria |
| 20 | 919 | backtick | la possibile via d'uscita a est, oltre la catena dei sistemi |
| 21 | 920 | 3 argomenti | controlli sui prezzi dei minerali e malcontento dei minatori |
| 22 | 921 | 3 argomenti | **People / Leon Shez**: scienziato, incolpa Darius |
| 67 | 995 | backtick | fuga dal Twilight riuscita |
| 68 | 996 | 3 argomenti | **People / Leon Shez**: gratitudine e contatto su Vinci |
| 89 | 1036 | backtick | accordo per portare Sora alla fattoria dei genitori |
| 90 | 1037 | 3 argomenti | **People / Darius Caldwell**: senso di colpa residuo |
| 95 | 1053 | 3 argomenti | **People / Darius Caldwell**: devozione a Katrina |
| 107 | 1073 | backtick | accordo per cercare Katrina su Valhalla |
| 108 | 1076 | backtick | ricongiungimento con Katrina |
| 109 | 1077 | 3 argomenti | **Minor People / Katrina Caldwell** |
| 134 | 1117 | backtick | la scoperta del magnetar nel sistema Decet |

## Le 3 righe `dialog`

| idx | riga | quando compare |
|---:|---:|---|
| 76 | 1010 | atterrato ma la scorta con Darius, Sora e Leon non è entrata nel sistema |
| 91 | 1039 | atterrato ma la scorta con Darius e Sora non è arrivata |
| 133 | 1107 | atterrato ma la scorta con Darius non è arrivata |

## Verifica

```
python staging/editorial/L52_20261018_172541/check.py    → FAIL totale: 0
python staging/editorial/L52_20261018_172541/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **23.255 unità · 740.175 EN · 702.232 IT**, **56 directory** con `translation.json`,
integrità dei file protetti e del repository (`b4aa3bac3`, nessuna modifica). I file completi sono
**ventotto**.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 135 unità `PENDING` (406 con L50–L51).
- **Nessun caricamento nel gioco**: nessuna delle cinque missioni è stata percorsa; in particolare non è
  verificata a schermo la scena finale del ricongiungimento con Katrina.
- **Nessun test del magnetar**: la modifica della portata del motore di salto (unità 134–135) è
  tradotta, non provata in gioco.
