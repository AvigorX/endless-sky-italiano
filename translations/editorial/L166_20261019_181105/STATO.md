# STATO — L166 · `avgi outfits.txt` (fucile laser, tavola di Trefoil, due oggetti strani) — **chiude il file**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L166_20261019_181105` |
| Righe / unità | **616–654** / **6** — file al **63/63 (100%)** |
| Tipi | **6 `DESCRIPTION`** · **0 `VALUE`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **4** (Optical 2, Trefoil 2, Damselflyman 1, Lancet 1) · **6 testi distinti** |
| Parole | **314 EN → 343 IT** (1,092); **1,02–1,40**, media **1,18** |
| Tab · virgolette | **2 unità** · **0** |
| sha256 | `5fbd18fba31ba060…` |
| Esiti | `check.py` **21** (`FAIL 0`) · `verify.py` **21**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| fucile laser | 1-2 | 616-617 | `Optical Laser Rifle`, lo spettro e la sicurezza per gli occhi, il cannocchiale |
| tavola di Trefoil | 3-4 | 631-632 | la tavola intarsiata di `Speaker Wisteria`, l'idea di usarla come arma contundente |
| tumore radioattivo | 5 | 641 | il `Damselflyman` e l'avvertenza che non dovresti vederlo |
| lancia cerimoniale | 6 | 654 | `Lancet Adamant`, adamantino e nanodiamante |

## Rese che contano

| EN | IT |
|---|---|
| `eye-safe` · `diffuse reflection` | **sicuro per gli occhi** · **riflessione diffusa** |
| `goggles that darken` | **occhiali che si scuriscono** |
| `scope parallax` | **parallasse del cannocchiale** |
| `blunt weapon` · `melee combat` | **arma contundente** · **rissa** |
| `disabled starship` | **astronave in avaria** |
| `shortspear` · `nanodiamond` | **lancia corta** · **nanodiamante** |

## Verifica

```bash
cd staging/editorial/L166_20261019_181105
python check.py     # FAIL totale: 0 (21 controlli)
python verify.py    # exit 0 (21 controlli, invariante di FILE)
```

**File CHIUSO**: 6 finestre (L161…L166) = **63 unità su 63 righe distinte**, `min(line) = 18`, `max(line) = 654`,
zero sovrapposizioni, zero unità dopo la 654.

**Non verificato**: nessun oggetto visto a schermo; i testi non sono stati caricati nel gioco.
