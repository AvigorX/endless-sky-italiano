# STATO — L58 · `data/human/culture conversations.txt`

**Lotto chiuso.** 43/43 unità tradotte, righe **25–209**.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L58_20261018_175847` |
| File | `data/human/culture conversations.txt` (**file nuovo**) |
| Unità | **43** (righe 25–209) |
| Parti | **3** — 16 · 16 · 11 |
| Contesti | **9** — `Sad Gamblers - Republic` 1–2, `Sad Gamblers - Syndicate` 3–4, `Foiled Kidnapping Witnessed` 5–6, `Gift Store Interaction` 7–14, `New China Mourners` 15–16, `New Holland Foibles` 17–27, `Trash Fire Crops` 28–32, `Worker's Occasion` 33–40, `Paradise Cleaner Incident` 41–43 |
| Tipi | **43 `MISSION_TEXT`** e nient'altro |
| Parole | 1.610 EN → 1.532 IT (**0,952**) |
| Rapporto per unità | **0,82 – 1,40** (gate 0,55–1,90) |
| `UI_LABEL` / `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0 / 0** — assenze dichiarate |
| Tab · virgolette | **34** · **8** (0 dispari, 0 quadre, 0 backtick) |
| Token `<…>` | **0** (parità 0/0 asserita) |
| Duplicati inglesi | **3 gruppi / 6 unità** (1/3, 2/4, 21/24) |
| sha256 `translation.json` | `0a66e11210f15963…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **35 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Prima unità del file | riga **25** (il lotto la copre) |
| Unità dopo la 209 | **331** |
| Unità totali del file | **374** |
| `max(line)` | **1122** |

Il lotto **apre** il file e **non lo chiude**: la copertura del file non è un invariante qui
(decisione 158), e `verify.py` asserisce `0 prima / 331 dopo / 374 totali`.

## Cosa è stato deciso qui

1. **`NT` vuoto, quattro tipi assenti, zero token.** Il `check.py` di L57 aveva 17 `UI_LABEL`, 3
   `DIALOG`, 13 token: qui tutte queste righe sono state **sostituite da asserzioni di assenza**, non
   lasciate in eredità (decisione 190).
2. **Registro quotidiano, non cerimoniale.** Nove micro-scene di gente comune: una lotteria, un posto di
   blocco, un negozio di souvenir, un funerale, una discarica di rottami, un raccolto bruciato, un
   ristorante, una donna delle pulizie umiliata. Il narratore osserva e non giudica: la traduzione non
   aggiunge commento dove l'inglese è asciutto.
3. **«Deep»** resta invariato: è il nome della regione, non un aggettivo. La scritta sulla tazza
   (`"Peace, Prosperity, Progress"`) è tradotta **fra virgolette dritte** («Pace, Prosperità,
   Progresso»), mantenendo la parità delle virgolette (8 = 8).
4. **Il discorso del caposquadra** (unità 25) è pieno di volgarità attenuate e di orgoglio di classe:
   «Senti, straniero», «levati di torno», «non ci serve il tuo naso nei nostri affari». Il registro
   resta popolare ma non volgare, perché il testo inglese è scontroso, non osceno.
5. **`Rik`** resta invariato, come ogni nome proprio, anche quando è solo un operaio citato una volta.
6. **La scena del ristorante** (33–40) ha tre esiti: offrire, compatire in silenzio, sorridere. Il terzo
   è l'unico che non umilia l'uomo, e la traduzione mantiene la differenza fra «compatire» e «sorridere»
   senza spiegarla.

## Verifica

```bash
cd staging/editorial/L58_20261018_175847
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (35 controlli)
```

`verify.py` non riusa la logica di `check.py`: rilegge il file sorgente riga per riga, interroga
`state.db` in sola lettura, ricostruisce `translation.json` dalle parti e asserisce le assenze come insiemi
vuoti espliciti (`== []`, `== ()`), non come «nessuna riga rossa».

## Prossimo passo

**L59** — stesso file, righe **225–423**, **42 unità**, 12 contesti, primo `Curious Waiter`, ultimo
`Sojourn Sunday Sales`. Non chiude il file.
