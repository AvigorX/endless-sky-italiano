# STATO — L247 (`data/human/syndicate jobs.txt`, righe 19–153)

**Stato: CHIUSO.** Primo lotto del file, **16 unità** (1 `VALUE` + 9 `DIALOG` + 6 `DESCRIPTION`). Il file resta **aperto a
16/94 (17,0%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L247_20261020_145010/` |
| file | `data/human/syndicate jobs.txt` (94 unità · 1.927 parole · righe 19–814) |
| righe | 19–153 |
| unità | **16** |
| parole | **488 EN → 510 IT** |
| rapporto | **0,97 – 1,23** (media 1,09), gate 0,55–1,90 |
| contesti | **6** — da `Transport executive to <planet>` a `Waste recycling on <planet>` |
| tab | **0** (asserzione negativa scritta) |
| virgolette | **2**, nella sola unità 12 (la citazione «Ci farà risparmiare mesi!») |
| apici | **6 EN** (6 unità) / **5 IT** (4 unità) |
| segnaposto | **39** in **11** famiglie, multiset e **ordine per unità** identici |
| copiati | **1** `VALUE` (nome del lavoro) |
| tradotti | **15** (9 `DIALOG` + 6 `DESCRIPTION`), di cui **3 coppie** con inglese identico |
| `check.py` | **32 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **27 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima · 16 qui · 78 dopo · confine riga **157** (`mission:Rush fuel Delivery`) |
| copertura del file | **16/94 (17,0%)**, stampata e non asserita |
| `sha256[:16]` | **`197077aa944ef85a`** |

## Comandi

```bash
python staging/editorial/L247_20261020_145010/check.py     # FAIL totale: 0 (32 controlli)
python staging/editorial/L247_20261020_145010/verify.py    # FAIL: 0 (27 controlli, 16/94)
```

## Cosa contiene

Sei lavori del Sindacato: il **trasporto di un dirigente** a una riunione urgente, il **ritiro aziendale** di una squadra di
ingegneri (presente **due volte**: il lavoro normale e la variante «Large», con la stessa prosa), la **spionaggio
aziendale** (intercettare un `<npc>` e scansionarne il carico), la **consegna di documenti** («ordinari», che finiscono in un
inceneritore industriale), e il **riciclaggio di rifiuti** dietro la facciata della «Iniziativa Verde» di Syndicated
Systems. Le 9 unità `DIALOG` sono le battute di chiudura di ogni missione.

## Limiti dichiarati

Nessuna approvazione (16 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file **non** è
completo: 16/94 (17,0%); restano 78 unità.
