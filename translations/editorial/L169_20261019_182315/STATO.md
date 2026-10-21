# STATO — L169 · `paradise world jobs.txt` (turisti ricchi, crociera, tre lavori sui passeggeri)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L169_20261019_182315` |
| Righe / unità | **376–522** / **17** — file al **69/131 (52,7%)** |
| Tipi | **3 `VALUE`** · **6 `DESCRIPTION`** · **8 `DIALOG`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **38** su **8** simboli, con **`<npc>`** 4 (segnaposto, non nome proprio) |
| Contesti | **6** · **15 testi distinti** su 17 (coppie 1/3 e 2/4) |
| Parole | **493 EN → 505 IT** (1,024); **0,90–1,24**, media **1,05** |
| Tab · virgolette | **0** · **2** (in idx 13) · **2 apici semplici** (idx 1 e 3) |
| sha256 | `150e46846747c2d3…` |
| Esiti | `check.py` **26** (`FAIL 0`) · `verify.py` **22**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| turisti di lusso | 1-4 | 376-414 | due missioni identiche (`tourists` e `tourist group`), le brochure contro la realtà |
| crociera di piacere | 5-8 | 419-447 | scorta al `<npc>`, andata, fallimento se manca la tappa, ritorno |
| passeggeri | 9-17 | 453-522 | liberati sulla parola, debitori, pensionati benestanti |

## Token

| simbolo | occorrenze |
|---|---|
| `<payment>` | 12 |
| `<destination>` | 7 |
| `<planet>` | 5 |
| `<bunks>` | 5 |
| **`<npc>`** | **4** |
| `<stopovers>` | 2 |
| `<tons>` | 2 |
| `<commodity>` | 1 |

## Rese che contano

| EN | IT |
|---|---|
| `outrageously wealthy tourists` | **turisti sfacciatamente ricchi** |
| `'appropriate facilities'` | **'strutture adeguate'** (apici conservati) |
| `glossy photos in the brochures` | **foto patinate delle brochure** |
| `non-violent repeat offenders` | **recidivi non violenti** |
| `live beyond their means` | **vivere al di sopra dei propri mezzi** |
| `"make themselves useful."` | **"si rendano utili"** (virgolette conservate) |

## Verifica

```bash
cd staging/editorial/L169_20261019_182315
python check.py     # FAIL totale: 0 (26 controlli)
python verify.py    # exit 0 (22 controlli)
```

**Non verificato**: nessuna missione vista a schermo; i testi non sono stati caricati nel gioco.
