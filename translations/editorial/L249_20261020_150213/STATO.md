# STATO — L249 (`data/human/syndicate jobs.txt`, righe 291–431)

**Stato: CHIUSO.** Terzo lotto del file, **19 unità** (4 `VALUE` + 11 `DIALOG` + 4 `DESCRIPTION`). Il file sale a
**55/94 (58,5%)**. **Nove unità sono una ripetizione di L248** e sono state riprese **alla lettera**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L249_20261020_150213/` |
| file | `data/human/syndicate jobs.txt` (94 unità · 1.927 parole · righe 19–814) |
| righe | 291–431 |
| unità | **19** |
| parole | **438 EN → 419 IT** |
| rapporto | **0,93 – 1,18** (media 1,04), gate 0,55–1,90 |
| contesti | **5** — `Syndicate target practice [2]` e `[3]`, `Syndicate Prisoner Transport [0]/[1]/[2]` |
| tab | **0** (asserzione negativa scritta) |
| virgolette | **2**, unità 12: «"arresti domiciliari"» |
| apici | **2 EN** (unità 2, 8: `You'll`) / **0 IT** (reso «Dovrai») |
| segnaposto | **22** in **5** famiglie, multiset **e ordine per unità** identici |
| copiati | **4** `VALUE` |
| tradotti | **15** (di cui **9 ripresi da L248**, **6 nuovi**) |
| `check.py` | **32 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **28 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 36 prima · 19 qui · 39 dopo · confine riga **435** |
| copertura del file | **55/94 (58,5%)** |
| `sha256[:16]` | **`ebc4407313c132bf`** |

## Comandi

```bash
python staging/editorial/L249_20261020_150213/check.py     # FAIL totale: 0 (32 controlli)
python staging/editorial/L249_20261020_150213/verify.py    # FAIL: 0 (28 controlli, 55/94)
```

## Cosa contiene

La **coda della missione «Syndicate target practice»** (`[2]` e `[3]`, con le quattro battute già scritte in L248) e i primi
tre **trasporti di prigionieri**: un dirigente ai domiciliari con avvocati e collezione di `<cargo>`, un **sabotatore
industriale** condannato, un gruppo di **`<bunks>` spie aziendali**.

## Il controllo che conta

**Coerenza cross-lot**: le 10 unità che ripetono una stringa inglese di L248 devono avere la **stessa resa**, e il
`verify.py` rilegge il `translation.json` di L248 **da qui** — non si fida di quello che dice il `check.py`.

## Limiti dichiarati

Nessuna approvazione (19 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file **non** è
completo: 55/94 (58,5%); restano 39 unità.
