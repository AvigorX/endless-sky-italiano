# STATO — L56 · `data/gegno/gegno I corroboration.txt`

**Lotto chiuso.** 171/171 unità tradotte, righe **29–904**.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L56_20261018_174346` |
| File | `data/gegno/gegno I corroboration.txt` |
| Unità | **171** (righe 29–904) |
| Parti | **5** — 27 · 33 · 42 · 38 · 31 |
| Contesti | **8** — `Passive-Aggressive Observations` 1–14 (14), `Foreign Spectator I` 15–15 (1), `Brief Bystander` 16–21 (6), `Scin on Cyife` 22–27 (6), `Battle over Zydee` 28–29 (2), `Gegno Suspicions` 30–60 (31), `Return to Giaru Gegno` 61–62 (2), `Gegno Anticipation` 63–171 (109) |
| Tipi | 137 `MISSION_TEXT` · 28 `UI_LABEL` · 3 `DIALOG` · 2 `DESCRIPTION` · 1 `VALUE` |
| Parole | 5.671 EN → 5.138 IT (**0,906**) |
| Rapporto per unità | **0,57 – 1,48** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **28** — 24, 26, 49, 77, 81, 89, 93, 100, 102, 104, 106, 108, 114, 116, 120, 122, 124, 126, 139, 143, 147, 151, 155, 157, 159, 161, 166, 168 |
| `DIALOG` | **3** — 62, 170, 171 (170 e 171 identiche nel sorgente) |
| `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** (assenze dichiarate) |
| Tab · virgolette | **129** · **238** (0 dispari, 0 quadre, 0 backtick) |
| Token `<…>` | **12** in 5 famiglie (`<first>` 4, `<last>` 4, `<destination>` 2, `<ship>` 1, `<planet>` 1) |
| Duplicati inglesi | **10 gruppi / 30 unità** |
| sha256 `translation.json` | `c2fe3862c23a294e…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **40 controlli**, exit **0** |

## Dove siamo nel file

Il lotto **apre** il file: 0 unità prima della riga 29, **127 dopo** la 904, file di 298 unità,
`max(line) = 1287`. La copertura del file **non** è un invariante di questo lotto (decisione 158):
la chiusura tocca a L57.

## Cosa è stato deciso qui

1. **`NT` 28 è il numero più alto della serie.** Molte sono verbi singoli (`ask`, `escort`, `work`,
   `alone`, `tech`, `interest`, `convince`, `before`, `unsure`, `upside`, `explain`, `understand`,
   `better`, `nothing`, `decision`, `home`, `tower`, `trio`, `board`, `accept`, `returned`, `negate`),
   altre composte (`negative rep` due volte, `quarg escort`, `no escort`, `visit a`, `visit b`,
   `epilogue a`, `epilogue b`, `end a`, `end b`, `dont know` senza apostrofo, `what does home mean`).
   Tutte restano **identiche** al sorgente: sono chiavi, non testo.
2. **`DIALOG` 3** (62, 170, 171). Le unità **170 e 171 sono identiche** nel sorgente: stessa scena,
   due esiti della missione. La traduzione è identica per necessità dichiarata.
3. **La voce di Adrauni** conserva la sintassi invertita a effetto cerimoniale («Otto rivoluzioni ti
   sono state date dai Gegno…», «Meddled in their affairs you have» → «Ti sei immischiato nei loro
   affari, una volta di troppo»). L'inversione si riproduce dove c'è, non si aggiunge dove non c'è
   (decisione 187).
4. **Il brano della flotta Vi che entra nel sistema** (29) non è un combattimento: è un'esercitazione
   osservata. I verbi restano al presente narrativo.
5. **I due rami dell'epilogo** (125–169) ripetono quasi per intero il discorso di Adrauni: le differenze
   sono solo nelle frasi finali. Non si uniformano: si traducono separatamente, e i duplicati
   coincidono **solo** dove coincidono in inglese.

## Verifica

```bash
cd staging/editorial/L56_20261018_174346
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (40 controlli)
```

`verify.py` non riusa la logica di `check.py`: rilegge il file sorgente riga per riga, interroga
`state.db` in sola lettura, ricostruisce `translation.json` dalle parti e confronta i multiset dei token.

## Prossimo passo

**L57** — stesse file, righe **905–1287**, **127 unità**, 3 contesti, chiude il file (298/298).
