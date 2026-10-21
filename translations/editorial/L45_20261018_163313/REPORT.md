# L45 — rapporto del lotto

`data/successors/successor 2 ghosts.txt` · righe **37–2167** · lotto `L45_20261018_163313` ·
**680/680 unità** · venticinquesimo file completo dello staging · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **680 / 680** (file completo) |
| parole | 18.302 EN → **17.736 IT** (0,969) |
| contesti | 36 (`Successors: Ghosts Prelude Wedding` … `Successors: Ghosts Reincarnation`) |
| parti | 14 — 45 · 55 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 50 · 30 |
| tab | **526 = 526** (526 unità che iniziano con tab) |
| virgolette | **1107 = 1107** |
| virgolette dispari | **15 unità** (15, 95, 159, 163, 479, 524, 525, 611, 612, 651, 652, 657, 666, 667, 669), stessi idx in italiano |
| token `<...>` | **102 = 102** (14 famiglie) |
| quadre `[` `]` | **11 unità** (651, 652, 653, 655, 657, 664, 666, 667, 668, 669, 670), conteggio invariato per unità |
| `LOGBOOK` | **23** (19 di testo + 4 categorie) |
| `CONVERSATION` | **16** (135–138, 256–267) |
| rapporto per unità | 0,59 – 1,79 |
| `check.py` | **FAIL totale: 0** (25 controlli) |
| `verify.py` | **39 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `480ff95bd7e2d97b` · `source.json` `0ece3e62f137a130` · `check.py` `4e0f4e9be48a34b0` · `verify.py` `c22ba40bdcf2c764` |

Il file parte dalla riga **37**; il `verify.py` asserisce `(first, last) == (37, 2167)` e 0 unità prima
e dopo.

## Tipi

559 `MISSION_TEXT` · 26 `UI_LABEL` · **23 `LOGBOOK`** · 21 `DESCRIPTION` · 20 `VALUE` ·
**16 `CONVERSATION`** · 15 `DIALOG` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 34

### 26 `UI_LABEL` (label di salto, bersagli di `goto`)

| idx | riga | label |
|---:|---:|---|
| 12 | 74 | `seen this before` |
| 51 | 189 | `saajret of somber sejra` |
| 56 | 197 | `who are you` |
| 99 | 320 | `isn't` |
| 186 | 621 | `visited before` |
| 206 | 692 | `kaatrij kijran` |
| 208 | 696 | `final choice` |
| 218 | 721 | `friend to animals` |
| 221 | 734 | `killed riiria` |
| 349 | 1105 | `was discreet` |
| 434 | 1371 | `prototypes only` |
| 473 | 1524 | `questions 1` |
| 533 | 1725 | `no cloak` |
| 536 | 1738 | `still no cloak` |
| 574 | 1844 | `what now` |
| 578 | 1855 | `wedding preparations` |
| 616 | 1967 | `kaatrij patron` |
| 627 | 1985 | `saajret and tiliia` |
| 632 | 2002 | `getting along` |
| 636 | 2011 | `collaboration` |
| 639 | 2022 | `low openness` |
| 641 | 2026 | `uncertain` |
| 643 | 2035 | `high forgiveness` |
| 654 | 2076 | `no resja` |
| 656 | 2083 | `no queru` |
| 658 | 2090 | `no hasur` |

### 8 riferimenti di dato

| idx | riga | tipo | valore |
|---:|---:|---|---|
| 195 | 648 | `LOGBOOK` | `People` (categoria di diario) |
| 305 | 977 | `LOGBOOK` | `Factions` (categoria di diario) |
| 357 | 1125 | `LOGBOOK` | `People` (categoria di diario) |
| 418 | 1311 | `LOGBOOK` | `People` (categoria di diario) |
| 355 | 1119 | `MISSION_TEXT` | `House Kaatrij` (nome di governo) |
| 467 | 1513 | `MISSION_TEXT` | `House Kaatrij` (nome di governo) |
| 513 | 1628 | `MISSION_TEXT` | `House Kaatrij` (nome di governo) |
| 552 | 1783 | `MISSION_TEXT` | `High Houses (Unknown)` (nome di governo) |

## Le 19 righe `log` di testo (controllo positivo)

| idx | riga | contenuto (italiano) |
|---:|---:|---|
| 1 | 37 | matrimonio imminente tra eredi delle Casate |
| 7 | 64 | l'incidente sulla luna di Casa Kaatrij |
| 25 | 122 | atterraggio negato su Qasa-Sija-Iri |
| 59 | 203 | tentativo di contatto con Saajret |
| 125 | 383 | droni sensore schierati nello spazio dei Predecessori |
| 151 | 473 | accordo di informazione con Casa Seineq |
| 231 | 770 | Saajret su Osolaa-Val-Mavra |
| 252 | 810 | la storia delle pratiche di caccia |
| 255 | 829 | la storia delle pratiche di caccia (variante) |
| 282 | 920 | avvicinamento occultato alla base |
| 304 | 976 | i Quarg e la sorveglianza sui Successori |
| 356 | 1124 | vassallaggio formale di Casa Kaatrij |
| 554 | 1803 | la nave da guerra di famiglia distrutta |
| 586 | 1908 | il matrimonio Chydiyi–Myurej, la licenza |
| 651 | 2072 | `(FILE "Persa")` frammento redatto |
| 652 | 2073 | `(FILE "Cuore")` frammento redatto |
| 653 | 2074 | `(FILE [...])` frammento redatto |
| 655 | 2081 | `(FILE "Processo")` frammento redatto |
| 657 | 2088 | `(FILE "Vuoto")` frammento redatto |

Le altre **4** righe `LOGBOOK` (195, 305, 357, 418) non hanno testo tradotto nell'unità: il sorgente è
`log "Categoria" "Nome" "testo"` con il **testo fra virgolette** invece che fra backtick, e
`tools/l10n.py` estrae la sola categoria. Lacuna di inventario del tool protetto, documentata in
`review.md` §2.

## I 16 nodi `CONVERSATION`

| idx | riga | contenuto (italiano) |
|---:|---:|---|
| 135 | 430 | richiesta di Seineq, schieramento dei droni |
| 136 | 432 | `(Sì.)` |
| 137 | 433 | `(No.)` — **identico al sorgente per necessità** |
| 138 | 437 | l'hub delle comunicazioni |
| 256 | 839 | rientro allo spazioporto |
| 257 | 842 | il deposito atteso |
| 258 | 846 | il deposito atteso (variante con importo) |
| 259 | 849 | Saajret osserva un lavoratore del porto |
| 260 | 851 | «Come dici?» |
| 261 | 852 | «Un po' troppo da vicino, in realtà.» |
| 262 | 853 | il colore che continua a scin… |
| 263 | 855 | «Perché mi stai raccontando questo?» |
| 264 | 856 | «Stai cercando di dirmi qualcosa?» |
| 265 | 858 | lo scintillio che si spegne |
| 266 | 862 | lo scintillio che si intensifica |
| 267 | 865 | lo sguardo di nuovo verso lo spazioporto |

## Le 11 unità con quadre

| idx | riga | marcatore |
|---:|---:|---|
| 651 | 2072 | `(FILE "Persa"): [...]` |
| 652 | 2073 | `(FILE "Cuore"): [...]` |
| 653 | 2074 | `(FILE [...]): [...]` |
| 655 | 2081 | `(FILE "Processo"): [...]` |
| 657 | 2088 | `(FILE "Vuoto"): [...]` |
| 664 | 2111 | `(FILE [...])` |
| 666 | 2119 | frammento «Persa» senza intestazione |
| 667 | 2123 | frammento «Cuore» senza intestazione |
| 668 | 2127 | frammento «Processo» senza intestazione |
| 669 | 2131 | frammento «Vuoto» senza intestazione |
| 670 | 2137 | frammento senza intestazione (Saajret) |

## Verifica

```
python staging/editorial/L45_20261018_163313/check.py    → FAIL totale: 0
python staging/editorial/L45_20261018_163313/verify.py   → exit 0, FAIL: 0
```

`state.py` dopo la chiusura: **22.068 unità · 703.383 EN · 667.123 IT** in staging, `ESITO: OK`,
integrità dei cinque file protetti e del repository (`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 680 unità `PENDING`.
- **Nessun caricamento nel gioco**: nessuna verifica a schermo dei 36 contesti né dei 16 nodi di
  conversazione.
- **Nessun test di gameplay** della linea Successors: il lotto è verificato come testo, non come gioco.
