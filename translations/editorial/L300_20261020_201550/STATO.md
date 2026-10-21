# STATO — L300 (`data/coalition/coalition outfits.txt`, righe 516–533)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 49/49 (100%)**, **ventiseiesimo file interamente tradotto**
(**85** su 167 nel progetto).

| voce | valore |
|---|---|
| directory | `staging/editorial/L300_20261020_201550/` |
| file | `data/coalition/coalition outfits.txt` (**49/49 unità · 1.608 parole · righe 26–533**) |
| righe | 516–533 |
| unità | **5**, tutte `DESCRIPTION` |
| contesti | **3** — `Coalition License` (516/517) · `Heliarch License` (524) · `Beyond the Hyperdrive` (532/533) |
| parole | **209 EN → 195 IT** (0,93) |
| rapporto | **0,93 – 1,28** |
| tab | **2** — righe **517, 533** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **2 EN / 5 IT** |
| seconda persona | **1 unità** (4) — **narrativa**, non istruzione |
| `check.py` | **21 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 49 unità · somma **15+15+14+5** · righe distinte · prima **26** · ultima **533** · **0 dopo** |
| `sha256[:16]` | **`3c9e7d59af2f404c`** |

## Comandi

```bash
python staging/editorial/L300_20261020_201550/check.py     # FAIL totale: 0 (21 controlli)
python staging/editorial/L300_20261020_201550/verify.py    # FAIL: 0 (21 controlli, FILE 49/49)
```

## La seconda persona narrativa

La riga **532** dice «A book **gifted to you** by Anna Fangvin». **Non è un'istruzione di montaggio** come quelle di L299 («va
installato nella sezione armi della **tua** nave»): è un **dono**, la voce del narratore che parla al giocatore.

| riga | tipo | resa |
|---|---|---|
| 532 | **narrativa** | «Un libro che **ti** ha regalato Anna Fangvin… È una copia autografata.» |

Il test elenca `[4]` e il documento distingue esplicitamente i **due tipi**: un controllo unico avrebbe confuso un dono con un
manuale.

## Gli atti di legge

Nessuno di questi titoli esiste nel corpus: sono **atti inventati** della burocrazia Heliarch, e la resa li rende
**descrittivi in italiano**, invece di lasciarli in inglese come nomi propri:

| inglese | resa |
|---|---|
| `the third Civil Goods and Fares Act` | **la terza Legge sui Beni e sulle Tariffe Civili** |
| `the War of Independence` | **la Guerra d'Indipendenza** (corpus, 5 occorrenze) |
| `the twenty-sixth addendum to the second article of the Ninth Rectification on Commerce and Traffic` | **il ventiseiesimo addendum al secondo articolo della Nona Rettifica su Commercio e Traffico** |

Il test **rifiuta** che `Rectification` o `Civil Goods` restino in inglese: sono **atti**, non nomi di prodotto.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `jump drive` | **motore di salto** | corpus (298) |
| `hyperlanes` | **ipervie** | corpus |
| `signed copy` | **copia autografata** | |
| `circlet of gold and platinum` | **fascia ornata d'oro e di platino** | |
| `Anna Fangvin`, `Beyond the Hyperdrive` | **invariati** | persona e titolo |

## Limiti dichiarati

Nessuna approvazione (5 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
