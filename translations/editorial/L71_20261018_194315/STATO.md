# STATO — L71 · `data/successors/successor 2 ghosts myurej.txt`

**Lotto chiuso.** Quarto lotto sul file: la cripta di Myurej su <planet>, con Ijaset. Il file prosegue
(riga 407 apre `Myurej 6`).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L71_20261018_194315` |
| File | `data/successors/successor 2 ghosts myurej.txt` (quarto lotto) |
| Unità | **42** (righe 311–401; finestra 308–401) |
| Parti | **2** — 21 · 21 |
| Contesti | **1** — `Successors: Ghosts Myurej 5` |
| Tipi | **40 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION`** |
| Parole | 1632 EN → 1546 IT (**0,947**) |
| Rapporto per unità | **0,59 – 1,33** (gate 0,55–1,90) |
| `NT` | **vuoto** — 0 `UI_LABEL`, 0 riferimenti di dato (asserito anche sul `raw`) |
| `LOGBOOK` | **0** — nessuna riga `log` (asserita l'assenza nel `raw`) |
| `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **9** in 4 famiglie: `<ship>` 3, `<last>` 3, `<planet>` 2, `<destination>` 1 |
| Tab · virgolette | **38** su 38 unità · **72** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **0 gruppi** (controllo negativo dichiarato) |
| sha256 `translation.json` | `9bdce0c7e02de186…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **45 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 311 | **119** (L68–L70) |
| Unità dopo la riga 401 | **50** |
| File | **211 unità**, `max(line) = 531` |
| Confine dopo | riga **407** apre `mission:Successors: Ghosts Myurej 6` |

Copertura del file: **161/211 = 76,3%**. Invariante di segmento: `(311, 401)`, 119 prima, 50 dopo.

## Cosa è stato deciso qui

1. **La cripta è un luogo, non una cassaforte**: `vault` → **cripta** (scelta nuova, dichiarata nel
   glossario), coerente con «cripta nascosta», «sala della cripta», «cripte come questa».
2. **`wormhole` resta invariato**: in staging il termine è sempre in inglese; tradurlo creerebbe una
   seconda nomenclatura per lo stesso oggetto.
3. **Ijaset non ha genere**: l'inglese usa `they`. In italiano ho evitato i participi concordati
   («La posizione e la chiave… sono state impresse in me» invece di «sono stata creata con»), e dove serve
   il riflessivo ho usato «si» («Ijaset si irrigidisce»). Eccezione dichiarata: nessun pronome di terza
   persona riferito a Ijaset nel lotto.
4. **`fashioned with`** (unità 15) non diventa «fabbricato»: è la voce di chi è stato *progettato* per una
   missione, e la resa impersonale («sono state impresse in me») tiene il senso senza inventare una
   biografia.
5. **Il bombardamento è descritto, non enfatizzato**: nessun trattino lungo, nessun punto esclamativo
   aggiunto; il testo inglese è asciutto e la traduzione lo resta.
6. **`coilgun` → cannone a bobina**, **`repulsors` → repulsori**, **`data-sphere` → sfera di dati**:
   termini già in staging.
7. **`highborn` → «nobili»**, **`despoilers` → «saccheggiatori»**, **`insets` → «incassi»**: parole comuni,
   nessun neologismo.

## Verifica

```bash
cd staging/editorial/L71_20261018_194315
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (45 controlli)
```

## Prossimo passo

**L72** copre **due contesti corti** dello stesso file: righe **402–464** (prima unità alla **407**),
**20 unità**, **453 parole**, contesti `Successors: Ghosts Myurej 6` e `… 7`, tab **11** su 11 unità,
virgolette **24**, **9 token** in 6 famiglie (`<last>` 3, `<planet>` 2, `<ship>` 1, `<payment>` 1,
`<destination>` 1, `<first>` 1), tipi `13 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION + 2 DIALOG + 1 LOGBOOK`.
**Primo `DIALOG` del file**: va ricognito sul `raw` prima di tradurre. Confine dopo: riga **469** apre
`mission:Successors: Ghosts Myurej 8`.
