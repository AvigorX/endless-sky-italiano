# STATO — L298 (`data/coalition/coalition outfits.txt`, righe 202–337)

**Stato: CHIUSO.** Secondo lotto del file: **quindici schede** in **dieci contesti** — **cinque coppie** (seconda unità con `\t`)
e **cinque schede singole**. File a **30/49 (61,2%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L298_20261020_200550/` |
| file | `data/coalition/coalition outfits.txt` (**49 unità · 1.608 parole · righe 26–533 · 49 `DESCRIPTION`**) |
| righe | 202–337 |
| unità | **15**, tutte `DESCRIPTION` |
| contesti | **10** — 5 doppi + 5 singoli |
| coppie | `Fuel Module` 246/247 · `Decoy Plating` 259/260 · `Refueling Module` 273/274 · `Shield Refactor Module` 289/290 · `Outskirts Gauger` 336/337 |
| singole | `Large Repair` 202 · `Overclocked Repair` 218 · `Cooling` 232 · `Small Recovery` 306 · `Scanning` 323 |
| parole | **471 EN → 491 IT** (1,04) |
| rapporto | **0,94 – 1,30** |
| tab | **5** — righe **247, 260, 274, 290, 337** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **7 EN / 6 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **23 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **15 prima** · 15 qui · **19 dopo** la 337 |
| `sha256[:16]` | **`619c7e3eb590cdc6`** |

## Comandi

```bash
python staging/editorial/L298_20261020_200550/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L298_20261020_200550/verify.py    # FAIL: 0 (23 controlli)
```

## La coppia a cavallo del confine

`Outskirts Gauger` occupa le righe **336–337**: la **seconda** è l'ultima del lotto, e la prima unità dopo la 337 è alla **356**
(`Small Thrust Module`), **un altro contesto**. Il test verifica due cose distinte:

1. **336 e 337 stanno entrambe nel lotto** — la coppia non è stata spezzata;
2. **il contesto dopo il confine è diverso** — se un lotto futuro rivendicasse la 336, l'overlap lo segnalerebbe.

## Cinque coppie e cinque singole, verificate per riga

Il test non si accontenta del conteggio: elenca **le righe esatte** delle schede singole
(`[202, 218, 232, 306, 323]`) e verifica che ogni unità con tab sia la **seconda** del proprio contesto, con il compagno **alla
riga precedente**. Una coppia «inventata» o una tab su una scheda singola farebbero fallire il controllo.

## Le fazioni

| inglese | resa | nota |
|---|---|---|
| `Lunarium` | **Lunarium** | invariato (107 occorrenze nel corpus) |
| `House Idriss` | **Casa Idriss** | corpus (`House` → «Casa») |
| `Saryds` | **i Saryd** | forma invariata del corpus |
| `Saros` | **Saros** | pianeta |
| `Heliarchs` | **gli Heliarch** | |

## Terminologia

| inglese | resa |
|---|---|
| `plating` | **rivestimento** |
| `Heliarch torpedoes` | **siluri Heliarch** |
| `radar jamming systems` | **sistemi di disturbo radar** |
| `shield generators` | **generatori di scudi** |
| `hull plating` | **corazzatura** |
| `repair drones` | **droni riparatori** |
| `gauger` | **misuratore** |

## Limiti dichiarati

Nessuna approvazione (15 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **19 unità**.
