# STATO — L120 · `data/human/campaign events.txt` (primo lotto: 52 unità, 3 contesti)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L120_20261019_065236` |
| Righe / unità | **28–242** / **52** — il lotto **apre** il file (0 unità prima) |
| Tipi | **41 `MISSION_TEXT`** · **9 `DESCRIPTION`** · **2 `LOGBOOK`** · **0 `VALUE`** |
| Stati | **52 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **3** — `remembrance day` (6), `war begins` (9), **`event: war begins` (37)** |
| Testi distinti | **45** per 52 unità — **7 coppie** ripetono l'inglese, la resa ripete |
| Parole | **2255 EN → 2193 IT** (0,972); per unità 0,69–1,39, media 1,00 |
| Tab | **41 unità** su 52 iniziano con `\t` — qui è la **norma**, non l'eccezione |
| Virgolette | **58**, tutte **dialogo** (si traducono), verificate per unità |
| Token | **5**: `<ship>` 4, `<planet>` 1 |
| Quadre · backtick | 0 · 0 |
| sha256 | `a4f3e6160ea73524…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** — invariante di **segmento** |

## La forma del file è un'altra cosa

| | L119 (`pirate jobs`) | **L120 (`campaign events`)** |
|---|---|---|
| `MISSION_TEXT` | 2 | **41** |
| `DESCRIPTION` | 17 | 9 |
| `DIALOG` | 32 | **0** (il dialogo è dentro `MISSION_TEXT`) |
| `CONVERSATION` | 12 | 0 |
| `LOGBOOK` | 0 | **2** (tipo non trattato da L68) |
| `VALUE` | 16 | **0** |
| unità con tab | 9 | **41** |
| virgolette | 6 | **58** |
| token | 106 | **5** |

Il controllo «i `VALUE` sono identici al sorgente» qui è un'**asserzione vuota** (`0 = 0`), scritta e non
omessa: un cambio di inventario che introducesse un nome di missione deve far fallire il lotto.

## Le 7 coppie ripetute

Le risposte del giocatore sono le stesse in due scene (`"Certo."`, `"Che succede?"`, `"E cosa ti fa pensare che tu
possa solo ordinarmi di andarmene?"`, `"Allora mi tolgo di mezzo."`, `"Scusa, non lo sapevo…"`, `"C'è qualcosa che
posso fare per aiutare?"`) e il paragrafo finale sulla guerra imminente compare due volte. **45 testi distinti**
per 52 unità, con una sola resa per testo.

## Il registro, corretto in corso d'opera

L'unità 41 (l'ufficiale che minaccia l'arresto) era stata resa con la **cortesia «lei»** («Senta, capitano… la sua
nave»), mentre tutto il resto del lotto usa il **«tu»** fissato dai tooltip. È stata riscritta al «tu» («Ascolta,
capitano… la tua nave… ti farò arrestare») **prima** della verifica, e il `check.py` ora controlla che nel lotto
non compaia nessuna forma di cortesia: un registro solo, non due.

## Contenuto

- **Giorno del Ricordo** (1–6): due voci di diario sugli Alphas e quattro paragrafi sulla commemorazione, la
  genetica e la pelle fotosintetica.
- **Geminus e Martini** (7–12): l'Arsenale distrutto, la Borsa Galattica, lo spazioporto di fortuna.
- **Bourne e i Mondi Liberi** (13–16): il mondo industriale, la capitale dei Mondi Liberi, la voce di diario sulla
  secessione.
- **L'attentato** (17–20): la piazza davanti allo schermo, l'ultimatum, le esplosioni nucleari.
- **La partenza forzata** (21–30): l'ufficiale di collegamento, il cannone al plasma, le risposte del giocatore.
- **Martini** (31–40): le nubi, l'ospedale da campo, la seconda scena.
- **L'arresto** (41–46): la legge marziale, la licenza revocata, la nave persa.
- **Il ritorno in orbita** (47–52): il telegiornale, le tre chiusure alternative.

## Verifica

```bash
cd staging/editorial/L120_20261019_065236
python mkparts.py   # 52 unità · 45 testi distinti · 41 tab · 58 virgolette · 5 token · 0 VALUE
python check.py     # FAIL totale: 0 (32 controlli)
python verify.py    # exit 0 (29 controlli)
```
