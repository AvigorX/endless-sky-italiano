# STATO — L245 (`data/hai/hai ships.txt`, righe 901–1516)

**Stato: CHIUSO.** Terzo lotto del file, **46 unità** (41 `TEXT` + 5 `DESCRIPTION`, **nessun `VALUE`**). Il file sale a
**120/157 (76,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L245_20261020_143746/` |
| file | `data/hai/hai ships.txt` (157 unità · 1.686 parole) |
| righe | 901–1516 |
| unità | **46** |
| parole | **442 EN → 441 IT** |
| rapporto | **0,98 – 1,10** (media 1,00), gate 0,55–1,90 |
| contesti | **5** — `Pond Strider` 8, `Sea Scorpion` 13, `Scarab` 3, `Shield Beetle` 20, `Emperor Beetle` 2 |
| tab | **1**, all'inizio dell'unità 46 (secondo paragrafo della scheda dell'Emperor Beetle) |
| virgolette | **82** (2 per ciascuno dei 41 nomi, nessuna nella prosa) |
| apici | **0 EN** / **2 IT** (unità 27, 45) |
| segnaposto | **0** (asserzione negativa scritta) |
| copiati | **41** `TEXT` |
| tradotti | **5** `DESCRIPTION` |
| `check.py` | **32 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **26 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 74 prima · 46 qui · 37 dopo · confine riga **1517** (`ship:Emperor Beetle`, stesso contesto) |
| copertura del file | **120/157 (76,4%)** |
| `sha256[:16]` | **`b2a073e1977f8e1f`** |

## Comandi

```bash
python staging/editorial/L245_20261020_143746/check.py     # FAIL totale: 0 (32 controlli)
python staging/editorial/L245_20261020_143746/verify.py    # FAIL: 0 (26 controlli, 120/157 cumulati)
```

## Cosa contiene

Cinque schede: la **Sea Scorpion** (piattaforma mobile per lanciare Tracker, prodotta in serie dagli Slegati), la
**Scarab** (la cugina laboriosa della Lightning Bug, scelta dai piloti di Grasshopper), lo **Shield Beetle** (l'unica nave
da guerra pesante degli Hai, usata anche dagli Slegati contro i convogli), e le due parti della scheda dell'**Emperor
Beetle** (un Titan corazzato, usato con parsimonia come ammiraglia e nave trofeo). Le altre 41 unità sono nomi di
equipaggiamento.

## Limiti dichiarati

Nessuna approvazione (46 unità `PENDING`), nessuna scheda vista nel gioco, nessuna revisione umana. Il file **non** è
completo: 120/157 (76,4%); **restano 37 unità**, che sono un lotto **terminale**.
