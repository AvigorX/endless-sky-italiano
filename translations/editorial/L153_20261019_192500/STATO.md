# STATO — L153 · `coalition jobs.txt` (la delegazione delle tre specie e i tre «Contain Criminals»)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L153_20261019_192500` |
| Righe / unità | **1360–1469** / **20** — file al **79,2%** (156/197) |
| Tipi | **1 `LOGBOOK`** · **7 `MISSION_TEXT`** · **4 `VALUE`** · **4 `DESCRIPTION`** · **4 `DIALOG`** |
| `UI_LABEL` | **0** — una sola asserzione vuota |
| Token | **16** su **4** simboli |
| Contesti | **2** (`Heliarchs Buy Jump Drive Job 1`, `Contain`) · **17 testi distinti** |
| Parole | **582 EN → 601 IT** (1,033); **0,77–1,27**, media **1,05** |
| Tab · virgolette | **7 unità** · **20**, nessuna dispari |
| sha256 | `7b5d3d976e20fb6c…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **25**, exit **0** |

## L'inversione è una firma, non un errore

Nella delegazione il Saryd e l'Arach parlano con l'ordine delle parole rovesciato:

> «L'esercito Heliarch, ben addestrato a usare le armi solo per difesa e solo per giustizia, **è**.»
> «…a te le nostre armi e le nostre navi da guerra **ancora non possiamo vendere**.»

Normalizzarle sarebbe un errore: è la voce della specie, come in L152. Due controlli distinti la verificano nel testo
tradotto.

## Tre lavori, una parola di differenza

| riga | inglese | italiano |
|---|---|---|
| 1404 | `combat criminals **on site**` | **sul posto** |
| 1428 | `combat criminals **on site**` | **sul posto** (stringa identica → stessa resa) |
| 1451 | `combat criminals **on the site**` | **sul luogo** |

Un controllo pretende che le due **rese siano diverse** e che «sul posto» non compaia in quella di «on the site». I tre
`DIALOG` raccontano esiti diversi — successo, fuga, sorpresa — e sono tre testi distinti, non tre copie.

## Una frase riletta, una riscritta

`Sell a jump drive to the Heliarchs for <payment>.` esisteva già in L152: **riletta** dopo aver verificato che la stringa
inglese fosse identica. Non «simile»: identica.

## Verifica

```bash
cd staging/editorial/L153_20261019_192500
python mkparts.py   # 20 unità · 1 LOGBOOK + 7 MISSION_TEXT + 4 VALUE + 4 DESCRIPTION + 4 DIALOG
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna missione giocata; i tre esiti dei `Contain` non sono stati visti a schermo.
