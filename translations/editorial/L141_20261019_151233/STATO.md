# STATO — L141 · `unfettered 0 prologue.txt` (chiude la prima missione)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L141_20261019_151233` |
| Righe / unità | **83–132** / **20** — file al **30,6%** (45/147) |
| Tipi | **18 `MISSION_TEXT`** · **2 `LOGBOOK`** |
| `VALUE` · `UI_LABEL` · token | **0** · **0** · **0** — tre asserzioni vuote scritte |
| Stati | **20 `PENDING`** — misurato e **asserito** |
| Contesto | **1**, e si **chiude**: `First Contact: Unfettered` 45/45 (25 in L140 + 20 qui) |
| Testi | **19 propri + 1 riletto** da L138 (unità 19) |
| Parole | **591 EN → 566 IT** (0,958); per unità 0,80–1,21, media 1,05 |
| Tab · virgolette | **18 unità** (le due di diario no) · **58**, con nove unità da quattro |
| sha256 | `2abdd856e427930b…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** — invariante di **segmento** |

## La storia degli Slegati, e la voce telegrafica

Il racconto della caduta: i centomila anni, i popoli-drago a sud con l'iperpropulsore, le scimmie umane che battono le
pietre, il divieto dei Drak, la malattia («febbre rapida, strana sensazione di fragilità, come essere ossa fragili con
la bocca piena di terra»), la gabbia che i Drak preparano per tutti.

Gli Slegati parlano **senza articoli e senza cortesia**: «Scimmia sciocca», «Una volta, centomila anni ormai passati»,
«Una specie che non si espande diventa come acqua salmastra, come albero rinsecchito». La resa **tiene il ritmo
spezzato**: un controllo verifica che il motto non sia stato «migliorato» con un articolo di troppo.

## Una voce di diario riletta, una variante resa di nuovo

| unità | inglese | trattamento |
|---|---|---|
| 19 | identica a L138 unità 16 | **riletta** dal `translation.json` di L138, confronto dell'inglese prima |
| 20 | variante (comincia «The Unfettered Hai say that…») | **resa di nuovo**, con lo stesso lessico ma senza copiare |

Distinguere i due casi è il punto: la prima è la **stessa frase**, la seconda è **la stessa informazione detta in modo
diverso**. Copiare la seconda avrebbe prodotto un diario che ripete una frase già letta; riscriverla da capo avrebbe
fatto divergere due voci che devono suonare coerenti.

## La frase che si ripete dentro il lotto

`only their dumb ancestors survive, just as monkeys will outlast the thinking humans` compare nelle unità **3 e 5**,
con la stessa resa («sopravvivono solo i loro antenati ottusi, proprio come le scimmie sopravvivranno agli umani
pensanti»), verificata per stringa.

## Verifica

```bash
cd staging/editorial/L141_20261019_151233
python mkparts.py   # 20 unità · 19 proprie + 1 riletta · 1 contesto chiuso · 18 tab · 58 virgolette
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna missione giocata; il dialogo con gli Slegati non è stato visto a schermo.
