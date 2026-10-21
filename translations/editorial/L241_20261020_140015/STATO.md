# STATO — L241 (`data/successors/successor jobs.txt`, righe 16–280)

**Stato: CHIUSO.** Primo lotto del file, **86 unità** (76 `TEXT` + 5 `VALUE` + 5 `DESCRIPTION`). Il file resta **aperto a
86/124 (69,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L241_20261020_140015/` |
| file | `data/successors/successor jobs.txt` (124 unità · 908 parole) |
| righe | 16–280 |
| unità | **86** — **76 `TEXT`** (di cui 66 frammenti) + **5 `VALUE`** (invariati) + **5 `DESCRIPTION`** |
| parole | **428 EN → 445 IT** |
| rapporto | **0,67 – 1,70** (media 1,05), gate 0,55–1,90 |
| contesti | **18** |
| tab / virgolette / apici | **0 / 0 / 0** (tre asserzioni negative scritte) |
| segnaposto | **45** in 8 famiglie: `<payment>` 15, `<planet>` 7, `<bunks>` 5, `<destination>` 5, `<date>` 5, **`<planet stopovers>` 3**, `<stopovers>` 3, `<commodity>` 2 |
| duplicati | **21 gruppi** di inglese identico, tutti con **una sola resa** |
| composizione | **1104 frasi** (48 + 48 + 648 + 360), verificate **una per una** |
| `check.py` | **33 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **28 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima · 86 qui · 38 dopo · confine riga **306** |
| copertura del file | **86/124 (69,4%)**, stampata e non asserita |
| `sha256[:16]` | **`19c694523a5473df`** |

## Comandi

```bash
python staging/editorial/L241_20261020_140015/check.py     # FAIL totale: 0 (33 controlli)
python staging/editorial/L241_20261020_140015/verify.py    # FAIL: 0 (28 controlli, 86/124)
```

## Cosa contiene

Le frasi di ringraziamento dei lavori Successors (turisti, studenti, operai, ricercatori) e **quattro blocchi di
frammenti** che il gioco concatena a caso: i **databank** («Tu consegni a mano le banche dati criptate e poi ricevi
`<payment>` in pagamento»), le **consegne per le Case** («Tu scarichi il carico di `<commodity>` a diversi ufficiali
Successors in ghingheri. Ti versano quanto pattuito, cioè il pagamento di `<payment>`»), e due blocchi di **ricercatori**
(«Consegni i ricercatori a `<planet stopovers>`, dove subito prendono a catalogare alcune formazioni rocciose vicine.»).
Chiudono cinque lavori con `VALUE` e `DESCRIPTION`: turisti, turisti audaci, spedizione, studenti.

## Limiti dichiarati

Nessuna approvazione (86 unità `PENDING`), nessun lavoro visto nel gioco, nessuna revisione umana. **L'opzione vuota** del
quarto gruppo dei due blocchi «researchers» non è inventariata (il database conserva 3 opzioni su 4): la lacuna è
dichiarata e non si ripara da un lotto.
