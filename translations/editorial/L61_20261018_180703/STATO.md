# STATO — L61 · `data/human/culture conversations.txt`

**Lotto chiuso.** 26/26 unità tradotte, righe **511–552**.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L61_20261018_180703` |
| File | `data/human/culture conversations.txt` (quarto lotto sul file) |
| Unità | **26** (righe 511–552) |
| Parti | **2** — 12 · 14 |
| Contesti | **1** — `News Reporter - Paradise` (1–26) |
| Tipi | **26 `MISSION_TEXT`** |
| Parole | 394 EN → 355 IT (**0,901**) |
| Rapporto per unità | **0,83 – 1,24** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **0** — assenza dichiarata |
| `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **1** — `<origin>` (unità 11), parità 1/1 |
| Tab · virgolette | **25** · **38** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **2 gruppi / 4 unità** — 18/24 (`"I would prefer to not answer."`), 20/26 (coda dei droni) |
| sha256 `translation.json` | `8b7278d41edd723f…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **35 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 511 | **116** (L58+L59+L60) |
| Unità dopo la 552 | **232** |
| Unità totali del file | **374** |
| Copertura | **142/374 (38,0%)** |
| `max(line)` | **1122** |

## Cosa è stato deciso qui

1. **`NT` torna vuoto** dopo il `NT` positivo di L60 (6, 20): l'asserzione è di nuovo negativa ed
   esplicita. Il segno del controllo segue il lotto (decisione 190).
2. **Il token `<origin>`** è l'unico del lotto e sta **dentro** il discorso diretto della giornalista
   («Sono qui su `<origin>` per riferire…»). Parità 1/1 verificata; il simbolo resta invariato.
3. **Il lessico politico è quello del gioco**: `Parliament` → **Parlamento**, `Free Worlds` → **Free
   Worlds** (invariato, è una fazione), `Navy` → **Marina**, `ultimatum` → **ultimatum**.
4. **Le due risposte di rifiuto sono identiche nel sorgente** (18 e 24) e restano identiche in italiano:
   sono la stessa opzione in due punti dell'albero. Il controllo dei duplicati lo asserisce.
5. **Il registro è giornalistico, non narrativo**: la reporter parla in frasi brevi e complete, il
   giocatore risponde per frasi singole. La traduzione non aggiunge subordinate dove l'inglese non ne ha.
6. **`I'd rather not` / `I would prefer to not answer`**: due formule diverse nel sorgente (9 e 18/24),
   rese diversamente («No, preferirei di no» / «Preferirei non rispondere»): non sono la stessa battuta e
   non vanno unificate.

## Verifica

```bash
cd staging/editorial/L61_20261018_180703
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (35 controlli)
```

## Prossimo passo

**L62** — stesso file, righe **555–611**, **30 unità**, 1 contesto (`Scientists at the Pub after a
Conference`), 674 parole, tab 26, virgolette 36, **3 `UI_LABEL`** (unità 4, 15, 26), 0 token.
