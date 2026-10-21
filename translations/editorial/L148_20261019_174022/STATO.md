# STATO — L148 · `coalition jobs.txt` (gli interpreti, i peacekeeper, i coloni Saryd)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L148_20261019_174022` |
| Righe / unità | **309–435** / **16** — file al **23,4%** (46/197) |
| Tipi | **1 `DIALOG`** (il primo del file) · **3 `TEXT`** · **6 `VALUE`** · **6 `DESCRIPTION`** |
| `LOGBOOK` · `UI_LABEL` | **0** · **0** — asserzioni vuote |
| Token | **31** su **4** simboli: `<payment>` 10, `<planet>` 9, `<bunks>` 6, **`<destination>` 6** |
| Stati | **16 `PENDING`** — misurato e **asserito** |
| Contesti | **10** |
| Testi | **10 distinti** — 3 interpreti uguali, 2 peacekeeper uguali |
| Parole | **205 EN → 207 IT** (1,010); per unità **0,85–1,12**, media **1,01** |
| Tab · virgolette | **0** · **0** |
| sha256 | `6f4f67af7faeeb38…` |
| `check.py` | **27 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** — invariante di **segmento** |

## Due cose nuove in una finestra

**1. Il primo `DIALOG` del file** (unità 1): la cerimonia in cui gli agenti Heliarch ricevono il candidato. Tono
narrativo al presente, non burocratico come le `DESCRIPTION`. Il `Counter(kind)` lo isola e il controllo verifica che
sia **tradotto**, non solo presente.

**2. Il simbolo `<destination>`**, che in L147 non esisteva:

| simbolo | dove sta | occorrenze |
|---|---|---|
| `<planet>` | nei `TEXT` («Scarichi gli interpreti su `<planet>`») | 9 |
| `<destination>` | nelle `DESCRIPTION` («…a `<destination>`») | 6 |

Sono **due cose diverse**: il primo è il mondo dove si scarica, il secondo la destinazione dichiarata della missione.
Il controllo confronta l'**ordine dei simboli per unità**, e in più verifica che nell'unità 4 ci sia `<destination>` e
**non** `<planet>`, e viceversa nell'unità 2.

## Sei `VALUE` senza «the»

`Interpreters to <planet>` ×3, `Peacekeepers to <planet>` ×2, `Saryds to <planet>`. A differenza di L147
(`Workers to **the** <planet>`) qui l'inglese **non ha l'articolo**: il `VALUE` resta com'è, e un controllo esplicito
rifiuta `the <planet>` — chi «corregge» aggiungendo l'articolo cambia il nome del lavoro mostrato in UI.

## Verifica

```bash
cd staging/editorial/L148_20261019_174022
python mkparts.py   # 16 unità · 1 DIALOG + 3 TEXT + 6 VALUE + 6 DESCRIPTION · 31 token · zero tab · zero virgolette
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna missione giocata; il `DIALOG` della cerimonia non è stato visto a schermo.
