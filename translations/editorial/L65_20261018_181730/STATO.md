# STATO — L65 · `data/human/culture conversations.txt`

**Lotto chiuso.** 43/43 unità tradotte, righe **819–920**.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L65_20261018_181730` |
| File | `data/human/culture conversations.txt` (ottavo lotto sul file) |
| Unità | **43** (righe 819–920) |
| Parti | **2** — 21 · 22 |
| Contesti | **4** — `Raider returning to Mordente-Bridi` 1–3, `Militia returning to Solace` 4–6, `Republic 300 Year Anniversary` 7–21, `Exotic Life: Buccaneer Bay` 22–43 |
| Tipi | **39 `MISSION_TEXT` + 4 `UI_LABEL`** |
| Parole | 1.666 EN → 1.676 IT (**1,006**) |
| Rapporto per unità | **0,91 – 1,58** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **4** — unità **10** `war ongoing`, **12** `war over`, **14** `zenith bombed`, **16** `sestor beaten at farpoint` |
| `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **2** — `<origin>` (7), `<ship>` (21); parità 2/2 per simbolo |
| Tab · virgolette | **45** (35 righe con tab iniziale) · **22** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **1 gruppo / 2 unità** (26/30, `"No thanks."`) |
| sha256 `translation.json` | `8cde7537201a63c9…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 819 | **251** (L58–L64) |
| Unità dopo la 920 | **80** |
| Copertura | **294/374 (78,6%)** |

## Cosa è stato deciso qui

1. **Quattro `UI_LABEL` che sono chiavi di stato del mondo**: `war ongoing`, `war over`, `zenith bombed`,
   `sestor beaten at farpoint` selezionano quattro varianti dello stesso anniversario. Restano identiche.
2. **Due token diversi** (`<origin>`, `<ship>`): la parità è verificata **per simbolo**, non solo sul
   totale — un `<origin>` diventato `<ship>` passerebbe un controllo di solo conteggio.
3. **Il titolo `300 Year Anniversary`** non può usare il simbolo `°` (vietato dal controllo): l'unità 18
   dice «trecentesimo anniversario», che è anche la forma corretta in italiano.
4. **Il registro cambia tre volte**: cronaca di spazioporto (1–6), servizio giornalistico sull'anniversario
   (7–21), commedia commerciale con il «Pesce Piatto» (22–43). Non si uniformano.
5. **`Dish Fish`** → **«Pesce Piatto»**: il gioco di parole è *fish that's a dish* → «il pesce che è un
   piatto», e in italiano funziona perché *piatto* è sia il recipiente sia l'aggettivo.
6. **Il menù truffa** (31) elenca cinque voci di addebito: «posto a sedere», «servizio di comodità»,
   «pulizia del pesce», «montaggio del piatto», «oneri di servizio». La comicità è nella burocrazia: la
   traduzione non la rende più divertente di quanto sia.

## Verifica

```bash
cd staging/editorial/L65_20261018_181730
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (36 controlli)
```

## Prossimo passo

**L66** — stesso file, righe **921–1053**, **45 unità**, 4 contesti (`Exotic Life: New Greenland`,
`Exotic Life: Mainsail`, `Struggling Author Gone Missing`, `Exotic Life: Bloodsea`), 1.239 parole,
tab 41, virgolette 52 con **2 dispari** (unità 10, 34), **0 `UI_LABEL`**, 0 token.
