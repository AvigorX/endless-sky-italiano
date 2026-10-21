# STATO — L68 · `data/successors/successor 2 ghosts myurej.txt`

**Lotto chiuso. Primo lotto su un file nuovo della linea Successors.** Il file prosegue: riga 118 apre
`mission:Successors: Ghosts Myurej 2`.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L68_20261018_191943` |
| File | `data/successors/successor 2 ghosts myurej.txt` (nuovo, primo lotto) |
| Unità | **49** (righe 16–113) |
| Parti | **2** — 25 · 24 |
| Contesti | **1** — `Successors: Ghosts Myurej 1` |
| Tipi | **44 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + 1 `UI_LABEL` + 2 `LOGBOOK`** |
| Parole | 1502 EN → 1447 IT (**0,963**) |
| Rapporto per unità | **0,61 – 1,50** (gate 0,55–1,90) |
| `UI_LABEL` | **1** — unità **20** (`label "follow up"`), resta identica |
| `LOGBOOK` | **2** — unità **23** (categoria `People`, resta identica) e **24** (testo, tradotto) |
| `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **10** in 5 famiglie: `<first>` 3, `<last>` 3, `<ship>` 2, `<destination>` 1, `<planet>` 1 |
| Tab · virgolette | **42** · **90** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **2 gruppi** (15/21, 16/22: stesse due battute di scelta nei due rami) |
| sha256 `translation.json` | `eaafbeb6e504c701…` |
| `check.py` | **37 controlli**, `FAIL totale: 0` |
| `verify.py` | **46 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 16 | **0** |
| Unità dopo la riga 113 | **162** |
| File | **211 unità**, `max(line) = 531` |
| Confine dopo | riga **118** apre `mission:Successors: Ghosts Myurej 2` |

L'invariante qui è **di segmento**, non di file (decisione 166): il `verify.py` asserisce `(16, 113)`,
**0 unità prima**, **162 dopo**, `max(line) = 531` e il confine alla riga 118. La copertura si stampa, non
si asserisce.

## Cosa è stato deciso qui

1. **Registro arcaico reso con «tu» moderno formale.** La voce di Casa Myurej parla in inglese arcaico
   (`thou / thee / thy / dost / shalt / thou'rt`); il progetto lo rende già così in L45–L47 («Cessa il tuo
   avvicinamento…», «Tieni ancora a freno la tua brama di sapere»). Qui la stessa scelta, senza arcaismi
   italiani: la cerimonia sta nella sintassi, non nei pronomi.
2. **`House X` → `Casa X`.** Misurato: in L45 `Casa Myurej` 4 volte contro `Casata Myurej` 2, e
   `Casa Kaatrij` 51, `Casa Sioeora` 8. Il plurale `Houses` → **`Casate`**, e `the People's Houses` →
   **`Casate del Popolo`** (forma già in staging). Le due occorrenze residue di «Casata Myurej» in L45
   restano: un lotto chiuso non si riscrive per allinearlo.
3. **La categoria di diario `People` resta identica** (unità 23) e va in `NT` insieme alla label 20. Non è
   prudenza stilistica: le altre categorie dello stesso file non sono inventariate, quindi tradurre questa
   sola creerebbe una categoria doppia nel diario del giocatore.
4. **La riga `log "People" "Riiria" "…"` perde il testo** (unità 23 = categoria). È la **settima** occorrenza
   della lacuna nota dell'estrattore protetto (L45 195/305/357/418, L46 62, L47 54, **L68 23**). Il testo
   descrittivo di Riiria non è in inventario: dichiarato, non riparabile qui.
5. **`log` a tre argomenti *tutti fra virgolette*** è una forma nuova per questo progetto: le forme
   asserite diventano quattro (`tre argomenti fra virgolette`, `tre con backtick`, `backtick`, `diretta`).
6. **Riiria parla in registro popolare**, non in quello cerimonioso di Casa Myurej: contrazioni e rabbia
   («li farà sanguinare come faccio sempre io»). Il capitano mercante è sarcastico e stanco, e usa il «tu»
   formale degli altri Successori.
7. **«13 token» dell'handoff L68 era un numero falso**: la sua stessa tabella somma 10 e il sorgente ne
   conta 10. Vince il workspace; il conteggio qui e nel `check.py` è **10**.
8. **Il numero di controlli si conta sull'output**, non si eredita: `check.py` 37 (38 righe `OK` meno
   l'intestazione), `verify.py` 46.

## Verifica

```bash
cd staging/editorial/L68_20261018_191943
python check.py                 # FAIL totale: 0   (37 controlli)
python verify.py                # exit 0           (46 controlli)
```

## Prossimo passo

**L69** continua lo stesso file: righe **114–197** (prima unità alla **118**), **31 unità**, **687 parole**,
**4 contesti** (`Successors: Ghosts Myurej 2` … `Successors: Ghosts Myurej 3 Checking`), tab **21**,
virgolette **4**, **10 token** in 4 famiglie (`<planet>` 2, `<destination>` 3, `<origin>` 3, `<ship>` 2),
tipi `23 MISSION_TEXT + 4 VALUE + 4 DESCRIPTION`, **0 `UI_LABEL`**, **0 `LOGBOOK`**, 1 gruppo di duplicati
inglesi (`Track down Riiria` due volte). Confine dopo: riga **215** apre `mission:Successors: Ghosts Myurej 4`.
