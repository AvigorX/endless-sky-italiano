# STATO — L184 · `human outfits.txt` (licenze, le due pietre, Puny) — **CHIUDE IL FILE: 63/63**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L184_20261019_192644` |
| Righe / unità | **520–606** / **13** — file al **63/63 (100%)** |
| Tipi | **12 `DESCRIPTION`** · **1 `VALUE`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Tab | **1** (idx 3) |
| Virgolette | **2**, entrambe **dentro il nome**: il `VALUE` è `"Puny"` |
| Contesti | **11** (`Puny` **3**, dieci con 1) · **13 testi distinti** |
| Parole | **458 EN → 458 IT** (1,000) · rapporto **0,96–1,37**, media **1,08** |
| Apici | **7 inglesi** (possessivi + `can't`) · **3 italiani** (elisioni) |
| sha256 | `cb00379ce130e0d0…` |
| Esiti | `check.py` **27** (`FAIL 0`) · `verify.py` **21**, exit **0** (**invariante di FILE**) |

## Le due virgolette non sono tipografia

Il contratto le annunciava come «primo caso del file, da legare alla causa». La causa è **il nome stesso**: il `VALUE` è
`"Puny"`, virgolette comprese. Non è discorso diretto, non sono pollici: sono parte del dato, e si copiano. Il `check.py`
verifica che le 2 virgolette stiano **tutte e sole** in idx 1, in inglese e in italiano.

## Invariante di FILE — 63/63

```
finestre: L180 12 · L181 9 · L182 14 · L183 15 · L184 13 = 63
63 righe DISTINTE · nessuna rivendicata due volte
le 63 righe del database, senza buchi
min(line) = 15 · max(line) = 606 · nessuna unità dopo la 606
2373 EN -> 2381 IT su tutto il file
```

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| `Puny` | 1-3 | 520-525 | il barboncino salvato da un losco complesso per le corse su Freedom |
| le due pietre | 4-5 | 535-546 | `Tear of Skade` (fredda) e `Blood of Surtr` (calda) |
| mappa e licenze | 6-12 | 555-599 | `Local Map`, `Pilot's License`, le quattro licenze della Marina, `Militia` |
| `City-Ship License` | 13 | 606 | la sagoma che non si riconosce |

## Verifica

```bash
cd staging/editorial/L184_20261019_192644
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # exit 0 (21 controlli, invariante di FILE)
```

**Non verificato**: nessun equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
