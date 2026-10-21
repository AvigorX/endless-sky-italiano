# STATO — L297 (`data/coalition/coalition outfits.txt`, righe 26–187)

**Stato: CHIUSO.** Primo lotto del file: **quindici moduli** della Coalizione in **dodici contesti**, con **tre coppie** in cui la
seconda scheda continua sulla riga successiva **dopo una tabulazione**. File a **15/49 (30,6%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L297_20261020_200012/` |
| file | `data/coalition/coalition outfits.txt` (**49 unità · 1.608 parole · righe 26–533 · 49 `DESCRIPTION`**) |
| righe | 26–187 |
| unità | **15**, tutte `DESCRIPTION` |
| contesti | **12** — **nove** con una sola unità, **tre** con due |
| coppie | `Small Reactor Module` (54/55) · `Large Reactor Module` (69/70) · `Small Cogeneration Module` (84/85) |
| parole | **461 EN → 487 IT** (1,06) |
| rapporto | **1,00 – 1,35** |
| tab | **3** — righe **55, 70, 85**, **primo carattere** dell'unità |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **1 EN / 9 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** · 15 qui · **34 dopo** la 187 |
| `sha256[:16]` | **`77085abfe85d1e13`** |

## Comandi

```bash
python staging/editorial/L297_20261020_200012/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L297_20261020_200012/verify.py    # FAIL: 0 (23 controlli)
```

## La tabulazione è struttura, non decorazione

Nei tre contesti con due unità, il gioco spezza la scheda in **due stringhe**: la seconda **inizia con `\t`**, così il pannello
mostra un rientro. Il test verifica tre cose distinte:

1. **solo tre unità** iniziano con la tab (righe 55, 70, 85);
2. la tab è il **primo carattere** anche in italiano, e il totale resta **3**;
3. ogni unità con tab ha **il compagno dello stesso contesto alla riga precedente**.

Se avessi «ripulito» la tab, le tre schede sarebbero diventate un blocco unico nel pannello del gioco.

## La citazione interna

L'unità 14 (`Overcharged Shield Module`) nomina **`Large Shield Module`**, cioè il modulo descritto dall'**unità 13** (riga 156),
che invece **non nomina se stesso**. Il test verifica la relazione sui contesti, non la semplice presenza della stringa: è la
differenza fra «il nome compare» e «il nome compare dove deve».

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `merchant marine` | **marina mercantile** | corpus |
| `solar panels` | **pannelli solari** | corpus |
| `hunger towers` | **torri della fame** | corpus (`"torri della fame"` con virgolette, altrove) |
| `fuel cell` | **cella a combustibile** | |
| `shield generators` | **generatori di scudi** | |
| `emitters` | **emettitori** | |
| `hull plating` | **corazzatura** | |
| `repair modules` | **moduli di riparazione** | |
| `Heliarch` / `Kimek` / `Quarg` / `Arach` | **invariati** | |
| `Coalition` | **Coalizione** | |

## Limiti dichiarati

Nessuna approvazione (15 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **34 unità** nel file.
