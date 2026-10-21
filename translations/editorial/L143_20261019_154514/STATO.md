# STATO — L143 · `unfettered 0 prologue.txt` (due missioni intere: Jump Drive 2 e 3)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L143_20261019_154514` |
| Righe / unità | **214–317** / **30** — file al **64,6%** (95/147) |
| Tipi | **28 `MISSION_TEXT`** · **1 `VALUE`** (`More Jump Drives`) · **1 `DESCRIPTION`** |
| `UI_LABEL` · token | **0** · **0** — due asserzioni vuote scritte |
| Stati | **30 `PENDING`** — misurato e **asserito** |
| Contesti | **2**, entrambi **chiusi**: `Unfettered Jump Drive 2` 12/12, `Jump Drive 3` 18/18 |
| Testi | **28 distinti** — `(No.)` e `(Sì.)` due volte ciascuno |
| Parole | **723 EN → 643 IT** (0,889); per unità 0,72–1,12, media 0,96 |
| Tab · virgolette | **26 unità** · **46** (unità 9, 25, 30 con quattro) |
| sha256 | `a6fdd67b2067eb90…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** — invariante di **segmento** |

## Due missioni in un lotto, perché da sole erano troppo sottili

`Unfettered Jump Drive 2` (12 unità, 269 parole) e `Unfettered Jump Drive 3` (18, 454) sarebbero stati due lotti
sottili, ognuno con il suo giro di apertura, verifica e documenti. Insieme sono **una revisione con due scene**, e
nessuno dei due contesti resta a metà.

## Il `VALUE` che ricompare

`More Jump Drives` era già il nome della missione di L142. Qui **ricompare alla riga 214**, identico. La ricomparsa non
si presume dal lotto precedente: la si verifica nel lotto nuovo, e il controllo è una lista esatta di una coppia.

## Due scelte vicine, due trattamenti

| scelta | unità | trattamento |
|---|---|---|
| `(No.)` | 4, 14 | **identico**: in italiano «No» è la stessa parola → `ID_OK` con controllo proprio |
| `(Yes.)` | 5, 15 | **tradotto** «(Sì.)», con l'accento, e **la stessa resa** in entrambe le missioni |

Un controllo unico per le due scelte sarebbe sbagliato in un verso o nell'altro: il primo confronta con l'inglese, il
secondo confronta le due occorrenze italiane fra loro.

## Il segreto degli Slegati

La rivelazione è doppia: prima il piano («Quei mondi sono fertili e quasi disabitati. Li rivendicheremo come nostri»),
poi il disprezzo per chi li abita — «una specie di sciacalli, che banchettano sulle rovine di civiltà orgogliose…
divoratori di carogne». Il giocatore capisce da solo di chi si parla: **i Wanderer**, e la narrazione lo dice in una
riga sola («Sospetti che stiano parlando del territorio oggi abitato dai Wanderer»).

## Verifica

```bash
cd staging/editorial/L143_20261019_154514
python mkparts.py   # 30 unità · 2 contesti · 28 distinti · (No.) ×2 identico · (Sì.) ×2 · 26 tab · 46 virgolette
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna delle due missioni è stata giocata.
