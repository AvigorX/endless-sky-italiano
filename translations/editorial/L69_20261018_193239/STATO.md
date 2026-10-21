# STATO — L69 · `data/successors/successor 2 ghosts myurej.txt`

**Lotto chiuso.** Secondo lotto sul file (dopo L68): il file prosegue, riga 215 apre
`mission:Successors: Ghosts Myurej 4`.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L69_20261018_193239` |
| File | `data/successors/successor 2 ghosts myurej.txt` (secondo lotto) |
| Unità | **31** (righe 118–197; finestra 114–197, prima unità alla 118) |
| Parti | **2** — 16 · 15 |
| Contesti | **4** — `Successors: Ghosts Myurej 2`, `… 3`, `… 3 Direct`, `… 3 Checking` |
| Tipi | **23 `MISSION_TEXT` + 4 `VALUE` + 4 `DESCRIPTION`** |
| Parole | 687 EN → 704 IT (**1,025**) |
| Rapporto per unità | **0,75 – 1,56** (gate 0,55–1,90) |
| `NT` | **vuoto** — 0 `UI_LABEL`, 0 riferimenti di dato (assenza dichiarata) |
| `LOGBOOK` | **0** — nessuna riga `log` nel segmento (assenza dichiarata) |
| `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **10** in 4 famiglie: `<destination>` 3, `<origin>` 3, `<planet>` 2, `<ship>` 2 |
| Tab · virgolette | **27** su 21 unità con tab iniziale · **4** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **1 gruppo** (28/30, `Track down Riiria`) con resa identica |
| sha256 `translation.json` | `7ab0a2bee4dc90a6…` |
| `check.py` | **35 controlli**, `FAIL totale: 0` |
| `verify.py` | **46 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 118 | **49** (L68) |
| Unità dopo la riga 197 | **131** |
| File | **211 unità**, `max(line) = 531` |
| Confine dopo | riga **215** apre `mission:Successors: Ghosts Myurej 4` |

Invariante di **segmento**: `(118, 197)`, 49 prima, 131 dopo, `max(line) = 531`, confine alla riga 215.
La copertura del file (80/211 = 37,9%) si stampa, non si asserisce.

## Cosa è stato deciso qui

1. **`NT` e `LOGBOOK` tornano a zero**: due **assenze dichiarate** con `== []`, non controlli omessi. Il
   `check.py` asserisce anche che nel `raw` del lotto non esista **nessuna** riga `log`, così un cambio di
   inventario non passa in silenzio.
2. **`<origin>` entra per la prima volta in questo file** (3 occorrenze): parità per **simbolo**, non solo
   sul totale (decisione 219), e il `verify.py` confronta il `Counter` per famiglia.
3. **`Track down Riiria` compare due volte** (unità 28 e 30) perché due missioni diverse hanno lo stesso
   nome: resa identica **perché l'inglese è identico**, non per pigrizia. Il controllo distingue questo caso
   dalla «resa ripetuta fra inglesi diversi».
4. **Refuso del sorgente**: unità 12 dice «Not longer after» (per «Not long after»); reso col senso giusto
   («Poco dopo…») senza replicare l'errore, e annotato nel `review.md`.
5. **Il manifesto di carico è una lista di dati, non prosa** (unità 18–23): si traduce la voce, si tengono
   numero, unità di misura e parentesi; `(in stasis, require constant power supply)` resta una nota tecnica.
6. **`Ojde` resta invariato** (nome della nave), come `Maspa-Viir-Kella` e `Osolaa-Uuoru` (toponimi).
7. **Messaggio dialettale** (unità 7): contrazioni inglesi (`shan't`, `icons'f`, `daren't`, `Houses're
   so fond'f`) rese con italiano popolare e spaventato, senza arcaismi: è un Successore comune, non Casa
   Myurej.

## Verifica

```bash
cd staging/editorial/L69_20261018_193239
python check.py                 # FAIL totale: 0   (35 controlli)
python verify.py                # exit 0           (46 controlli)
```

## Prossimo passo

**L70** continua lo stesso file: righe **198–307** (prima unità alla **215**), **39 unità**, **1.028 parole**,
**1 contesto** (`Successors: Ghosts Myurej 4`), tab **28** su 28 unità, virgolette **64**, **5 token** in
4 famiglie (`<destination>` 1, `<origin>` 1, `<planet>` 1, `<ship>` 2), tipi `33 MISSION_TEXT + 1 VALUE +
1 DESCRIPTION + 3 LOGBOOK + 1 UI_LABEL`. Confine dopo: riga **311** apre
`mission:Successors: Ghosts Myurej 5`.
