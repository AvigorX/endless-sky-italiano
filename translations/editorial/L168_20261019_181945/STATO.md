# STATO — L168 · `paradise world jobs.txt` (sette lavori «di beneficenza», 55 token)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L168_20261019_181945` |
| Righe / unità | **225–372** / **24** — file al **52/131 (39,7%)** |
| Tipi | **7 `VALUE`** · **7 `DESCRIPTION`** · **10 `DIALOG`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **55** su **11** simboli, incluso **`<planet stopovers>`** (2, segnaposto unico) |
| Contesti | **7** · **24 testi distinti** |
| Parole | **521 EN → 555 IT** (1,065); **0,95–1,21**, media **1,07** |
| Tab · virgolette | **0** · **0** — asserzioni vuote scritte |
| sha256 | `f7f0a3fc5708fb85…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| sette lavori | 1-24 | 225-372 | vestiti, cure mediche, beni di beneficenza, feste, patrimonio ereditario, braccianti a contratto, smaltimento rifiuti |

## Il segnaposto composto

| simbolo | occorrenze |
|---|---|
| `<payment>` | 14 |
| `<commodity>` | 9 |
| `<planet>` | 8 |
| `<destination>` | 6 |
| `<origin>` | 5 |
| `<cargo>` | 5 |
| `<stopovers>` | 3 |
| **`<planet stopovers>`** | **2** |
| `<tons>` · `<date>` · `<bunks>` | 1 · 1 · 1 |

`<planet stopovers>` **contiene** la parola `stopovers`: spezzarlo in `<planet>` + ` stopovers` cambierebbe il multiset,
e tre controlli lo impediscono (multiset, presenza intera in idx 10 e 18, assenza del pattern spezzato).

## Rese che contano

| EN | IT |
|---|---|
| `under-dressed and fashion-deprived souls` | **anime malvestite e prive di stile** |
| `the suffering souls` · `culturally-underexposed` | **anime sofferenti** · **culturalmente digiune** |
| `novelty castles` · `sharply-dressed stewards` | **castelli decorativi** · **maggiordomi in abiti eleganti** |
| `estate sale` · `trustees` | **vendita all'asta** · **esecutori testamentari** |
| `the shabbily-dressed young men and women` | **i giovani uomini e donne vestiti male** |
| `exceptionally foul shipment` | **spedizione eccezionalmente fetida** |

## Verifica

```bash
cd staging/editorial/L168_20261019_181945
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (21 controlli, confine riga 376 misurato: DESCRIPTION)
```

**Non verificato**: nessun lavoro visto a schermo; i testi non sono stati caricati nel gioco.
