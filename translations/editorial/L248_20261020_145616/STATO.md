# STATO — L248 (`data/human/syndicate jobs.txt`, righe 157–275)

**Stato: CHIUSO.** Secondo lotto del file, **20 unità** (5 `VALUE` + 10 `DIALOG` + 5 `DESCRIPTION`). Il file sale a
**36/94 (38,3%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L248_20261020_145616/` |
| file | `data/human/syndicate jobs.txt` (94 unità · 1.927 parole · righe 19–814) |
| righe | 157–275 |
| unità | **20** |
| parole | **430 EN → 422 IT** |
| rapporto | **0,93 – 1,32** (media 1,03), gate 0,55–1,90 |
| contesti | **5** — `Rush fuel Delivery`, `Rush equipment Delivery`, `Syndicate target practice [0]/[1]/[2]` |
| tab / virgolette | **0** / **0** (due asserzioni negative scritte) |
| apici | **2 EN** (unità 10, 16: `You'll`) / **1 IT** (unità 2: `d'emergenza`) |
| segnaposto | **32** in **8** famiglie, multiset **e ordine per unità** identici |
| copiati | **5** `VALUE` (3 distinti) |
| tradotti | **15**, di cui **7 gruppi** di inglese identico con **una sola resa** |
| `check.py` | **33 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **28 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 16 prima · 20 qui · 58 dopo · confine riga **291** (parentesi quadre) |
| copertura del file | **36/94 (38,3%)** |
| `sha256[:16]` | **`fe1a653311604b88`** |

## Comandi

```bash
python staging/editorial/L248_20261020_145616/check.py     # FAIL totale: 0 (33 controlli)
python staging/editorial/L248_20261020_145616/verify.py    # FAIL: 0 (28 controlli, 36/94)
```

## Cosa contiene

Due **consegne urgenti** (carburante a un reattore civile, attrezzature ai tecnici del Sindacato) e la missione
**«Syndicate target practice»**, che compare **tre volte** con la stessa prosa in tre contesti `[0]`, `[1]`, `[2]`: la
scheda (disabilita la nave-bersaglio, scansionane il carico, atterra) e **cinque battute** (scansione riuscita; errore di
aver dimenticato la scansione; bersaglio distrutto con multa; consegna dei risultati).

## Limiti dichiarati

Nessuna approvazione (20 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file **non** è
completo: 36/94 (38,3%); restano 58 unità.
