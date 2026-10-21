# STATO — L301 (`data/remnant/remnant ships.txt`, righe 17–806)

**Stato: CHIUSO.** Primo lotto del file: **dodici unità** in **quattro contesti**, con **due gruppi da tre** e **due `VALUE`** che
sono **plurali di nomi di nave**. File a **12/38 (31,6%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L301_20261020_202040/` |
| file | `data/remnant/remnant ships.txt` (**38 unità · 1.633 parole · righe 17–1.826 · 35 `DESCRIPTION` + 3 `VALUE`**) |
| righe | 17–806 |
| unità | **12** — **10 `DESCRIPTION` + 2 `VALUE`** |
| contesti | **4** — `Modified Dromedary` (6) · `Gull` (3) · `Albatross` (2) · `Heron` (1) |
| terzine | **`Modified Dromedary` 350/351/352** · **`Gull` 547/548/549**, tab sulla 2ª e 3ª |
| coppia | `Modified Dromedary` 474/475 (tab sulla seconda) |
| `VALUE` | **`Albatrosses`** (17) · **`Modified Dromedaries`** (274) — **copiati** |
| parole | **477 EN → 483 IT** (1,01) |
| rapporto | **0,91 – 1,17** |
| tab | **5** — righe **351, 352, 475, 548, 549** |
| virgolette | **4** dritte (2 unità: 350, 474) su «"celle del sogno"» |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| apici | **6 EN / 14 IT** |
| ripetizione | **unità 4 e 7 identiche** (righe 350 e 474) |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** · 12 qui · **26 dopo** la 806 |
| `sha256[:16]` | **`a0e73ad200bf1785`** |

## Comandi

```bash
python staging/editorial/L301_20261020_202040/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L301_20261020_202040/verify.py    # FAIL: 0 (24 controlli)
```

## Il `DESCRIPTION` ripetuto sotto due stati della stessa nave

Le righe **350** e **474** hanno **lo stesso testo inglese**: è il **primo paragrafo** del `Modified Dromedary`, che il gioco
mostra sia per la nave **integra** sia per il **relitto**. Solo la parte dopo la tab cambia (351/352 descrivono la replica, 475
descrive il relitto).

La resa di 350 e 474 è quindi **identica**, verificata in **entrambe le lingue**: se le due fossero divergite, lo stesso
paragrafo sarebbe raccontato in due modi a seconda che la nave sia intera o distrutta.

## I due `VALUE` sono plurali e si copiano

| riga | inglese | italiano |
|---|---|---|
| 17 | `Albatrosses` | **`Albatrosses`** |
| 274 | `Modified Dromedaries` | **`Modified Dromedaries`** |

Sono i **nomi al plurale** usati dall'interfaccia del gioco. Tradurli («Albatros», «Dromedari modificati») avrebbe rotto il
collegamento con il nome singolare, che resta invariato in tutto il file.

## I due gruppi da tre

| gruppo | righe | tab |
|---|---|---|
| `Modified Dromedary` | 350, **351**, **352** | sulla 351 e sulla 352 |
| `Gull` | 547, **548**, **549** | sulla 548 e sulla 549 |

Due **tab consecutive** per gruppo: tre stringhe, **un** pannello. Il test verifica che le tre condividano il contesto e che le
tab siano sulla **seconda e terza**, non sulla prima.

## Il confine è un taglio dichiarato

La **806** è l'**unica** unità `Heron` del lotto, e la **807** (fuori segmento) è la **seconda** unità **dello stesso contesto**.
Non è una coppia spezzata *dentro* il lotto: è un confine **scelto** sul numero di parole. Il test verifica che il taglio sia
**dove è dichiarato** — 806 / 807 — e che non ci siano altre unità `Heron` nel segmento.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `city-ships` | **navi-città** | corpus (11) |
| `hydroponics` | **serre idroponiche** | |
| `dream cells` | **"celle del sogno"** | **virgolette dritte**, come il sorgente |
| `cloaking technology` | **tecnologia di occultamento** | corpus |
| `mobile starports` | **spazioporti mobili** | corpus («spazioporto») |
| `convoy routes` | **rotte dei convogli** | corpus |
| `Tycho Crater Cooperative`, `Shattered Light`, `Alphas` | **invariati** | |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **26 unità**.
