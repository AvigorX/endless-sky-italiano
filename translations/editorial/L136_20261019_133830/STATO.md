# STATO — L136 · `data/starts.txt` (secondo inizio: `Birthday Surprise`)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L136_20261019_133830` |
| Righe / unità | **135–167** / **15** — file al **41,6%** (47/113) |
| Tipi | **8 `CONVERSATION`** · **4 `LOGBOOK`** · **2 `DESCRIPTION`** · **1 `VALUE`** (`Birthday Surprise`) |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Stati | **15 `PENDING`** — misurato e **asserito** |
| Contesti | **2 completi** — `start:paradise` 3, `conversation:paradise intro` 12 |
| Testi | **10 propri + 5 riletti** da L135 (unità 5–9), **15 distinti** |
| Parole | **587 EN → 559 IT** (0,952); per unità 0,85–1,12, media 1,01 |
| Tab · virgolette | **6 unità** · **14** (6:2, 10:4, 11:2, 12:4, 13:2), nessuna dispari |
| sha256 | `adbc2022515e8753…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** — invariante di **segmento** |

## Cinque frasi non si riscrivono: si rileggono

Le unità **5–9** sono le stesse di L135 (che le aveva alle 5–9 e 21–25): la storia della Repubblica, il Parlamento, il
Sindacato, il suo impatto ambientale, i pirati. Invece di ricopiarle, il costruttore le **rilegge** dal
`translation.json` di L135 con una mappa `SHARED`, dopo aver verificato che l'inglese sia identico:

```python
for k, p in SHARED.items():
    assert KEY[k] in prev, ('condivisa assente da L135', k, KEY[k][:50])
...
for k, p in SHARED.items():
    assert T[k] == prev[KEY[k]], k        # rilettura verificata, non supposta
```

## Una previsione dell'handoff era sbagliata

`HANDOFF_L136` diceva: «**15 testi distinti**: nessuna delle cinque frasi condivise ricade qui». È **falso**: le
cinque frasi condivise sono proprio le unità **5–9** di questo lotto. Il `verify.py` lo misura confrontando l'inglese
con i lotti precedenti, e la resa viene riletta. La lezione: *distinti dentro il lotto* non significa *nuovi rispetto
ai lotti precedenti* — sono due misure diverse, e la prima non dice niente sulla seconda.

## La battuta troncata

L'unità 12 finisce con `before-"`: il sorgente **tronca** la frase a metà parola. La resa riproduce il taglio
(«...prima di-"»), e un controllo verifica che non sia stato «riparato» in un punto fermo.

## I numeri e le scelte

| EN | IT | nota |
|---|---|---|
| `Birthday Surprise` | **identico** | nome dell'inizio (`VALUE`) |
| `500,000 credits` | **500.000 crediti** | due occorrenze (4, 15), valore intatto |
| `Mainsail` | **Mainsail** | pianeta |
| `Paradise World` | **Mondo del Paradiso** | forma già in uso |
| `financier` | **finanziere** | |
| `credit chip` | **gettone di credito** | |
| `stylus and a pad` | **stilo e una tavoletta** | |
| `child` | **figlio** | maschile generico: l'italiano non ha forma neutra (dichiarato in `review.md`) |
| `Is it that time of year already?` | — | non presente: nessuna unità |

## Verifica

```bash
cd staging/editorial/L136_20261019_133830
python mkparts.py   # 15 unità · 10 proprie + 5 rilette · 2 contesti completi · 6 tab · 14 virgolette
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # exit 0 (28 controlli, invariante di segmento)
```

**Non verificato**: nessun inizio avviato nel gioco.
