# STATO — L295 (`data/human/marauders.txt`, righe 548–858)

**Stato: CHIUSO.** Secondo lotto del file: **tre serie da tre** (`Leviathan`, `Manta`, `Quicksilver`), con **una descrizione
ripetuta due volte** nel sorgente. File a **21/29 (72,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L295_20261020_194529/` |
| righe | 548–858 |
| unità | **9**, tutte `DESCRIPTION` |
| serie | **3 × 3** — `Leviathan` (548, 580, 616) · `Manta` (676, 710, 747) · `Quicksilver` (799, 831, 858) |
| parole | **494 EN → 534 IT** (1,08) |
| rapporto | **1,08 – 1,21** |
| tab / virgolette / segnaposto / alternative | **0 / 0 / 0 / 0** (asserzioni vuote) |
| apici | **8 EN / 14 IT** |
| ripetizione | **unità 8 e 9 identiche** (righe 831 e 858) |
| `check.py` | **19 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 12 prima · 9 qui · **8 dopo** la 858 |
| `sha256[:16]` | **`5a651fec0023b77d`** |

## Comandi

```bash
python staging/editorial/L295_20261020_194529/check.py     # FAIL totale: 0 (19 controlli)
python staging/editorial/L295_20261020_194529/verify.py    # FAIL: 0 (22 controlli)
```

## La descrizione doppia

Le righe **831 e 858** hanno **lo stesso testo inglese**, parola per parola. Non è un errore dell'estrattore: il file contiene
davvero la stessa scheda due volte. La resa è quindi **identica**, e il test lo verifica in **entrambe le lingue**:

```python
at[831]['english'] == at[858]['english'] and at[831]['italian'] == at[858]['italian']
```

Se avessi reso le due unità con parole diverse, il giocatore avrebbe visto **lo stesso modello descritto in due modi**.

## Le frasi condivise dentro le serie

| serie | condivisione |
|---|---|
| `Manta` | la **5 e la 6** chiudono con la stessa frase («Se il suo tonnellaggio a vuoto fosse appena più alto…»); la **4** ha la variante «È solo il tonnellaggio a vuoto a impedirle…» |
| `Quicksilver` | la **7 e la 8** condividono «forse in risposta alla `Headhunter` della Lionheart» |

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `shield projectors` | **proiettori di scudi** | **distinto** da `shield emitters` → «emettitori di scudi» (L294) |
| `shield emitters` | **emettitori di scudi** | |
| `dry tonnage` | **tonnellaggio a vuoto** | |
| `forked tail` | **coda forcuta** | |
| `anti-missile turrets` | **torrette antimissile** | |
| `thruster port` | **porto per propulsori** | coerente con «porto per cannoni» |
| `bunk` | **cuccetta** | corpus |
| `hotrod` | **fuoriserie** | |
| `aftermarket model` | **modello post-vendita** | |
| `Betelgeuse Shipyards`, `Megaparsec`, `Lionheart`, `Headhunter`, `Vanguard Heavy Warship` | **invariati** | |

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **8 unità**.
