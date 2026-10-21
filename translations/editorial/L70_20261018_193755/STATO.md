# STATO — L70 · `data/successors/successor 2 ghosts myurej.txt`

**Lotto chiuso.** Terzo lotto sul file: la battaglia contro Riiria su Maspa-Viir-Kella e la resa dei conti
con Casa Myurej. Il file prosegue (riga 311 apre `Myurej 5`).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L70_20261018_193755` |
| File | `data/successors/successor 2 ghosts myurej.txt` (terzo lotto) |
| Unità | **39** (righe 215–307; finestra 198–307) |
| Parti | **2** — 20 · 19 |
| Contesti | **1** — `Successors: Ghosts Myurej 4` |
| Tipi | **33 `MISSION_TEXT` + 1 `VALUE` + 1 `DESCRIPTION` + 3 `LOGBOOK` + 1 `UI_LABEL`** |
| Parole | 1028 EN → 953 IT (**0,927**) |
| Rapporto per unità | **0,82 – 1,41** (gate 0,55–1,90) |
| `NT` | **3** — unità **30** (`label "not met solitude enforcers"`) + unità **7 e 10** (`government` con backtick) |
| `LOGBOOK` | **3** — unità **8, 35, 37**, tutte forma **diretta** (`log "testo"`), testo tradotto |
| `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **5** in 4 famiglie: `<ship>` 2, `<destination>` 1, `<origin>` 1, `<planet>` 1 |
| Tab · virgolette | **28** su 28 unità con tab iniziale · **64** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **1 gruppo** (7/10, il riferimento `government`) con resa identica |
| sha256 `translation.json` | `a767223f993886ef…` |
| `check.py` | **38 controlli**, `FAIL totale: 0` |
| `verify.py` | **48 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 215 | **80** (L68 + L69) |
| Unità dopo la riga 307 | **92** |
| File | **211 unità**, `max(line) = 531` |
| Confine dopo | riga **311** apre `mission:Successors: Ghosts Myurej 5` |

Copertura del file: **119/211 = 56,4%**. Invariante di **segmento**: `(215, 307)`, 80 prima, 92 dopo.

## Cosa è stato deciso qui

1. **Due riferimenti di dato travestiti da testo** (unità 7 e 10): `government \`People's Houses
   (Hostile)\`` è un nome di governo che il parser classifica `MISSION_TEXT`. Tradurlo romperebbe la logica
   della missione: resta **identico** ed è in `NT` con la label 30. Il `verify.py` verifica che le due righe
   siano davvero `government` nel `raw`, non lo deduce dal tipo.
2. **Tre `LOGBOOK`, tutti forma diretta** (8, 35, 37): nessuna categoria emersa, `LOG_CAT` vuoto e
   asserito. I due diari alternativi (accettato 35 / rifiutato 37) restano **distinti**.
3. **La voce cerimoniosa di Casa Myurej accusa**: «Ti avevamo dato un compito semplice», «Hai un'abitudine,
   ci pare». Il registro resta formale e moderno (decisione 228), senza arcaismi italiani, anche quando la
   Casa minaccia o si fa melliflua («Non sei uno strumento da gettare via… ma da coltivare»).
4. **`Shroud` resta invariato** («il gorgo dello Shroud»): in staging il toponimo è sempre in inglese
   (`Tangled Shroud`).
5. **`Predecessori`** → parola già fissata per `Predecessors`; **`manufatti`** è la resa di `artifacts`.
6. **`Raaqa-Kvelq-Ryuit`** invariato (toponimo); `Raaqa` ricorre 26 volte in staging.

## Verifica

```bash
cd staging/editorial/L70_20261018_193755
python check.py                 # FAIL totale: 0   (38 controlli)
python verify.py                # exit 0           (49 controlli)
```

## Prossimo passo

**L71** continua lo stesso file: righe **308–401** (prima unità alla **311**), **42 unità**, **1.632 parole**,
**1 contesto** (`Successors: Ghosts Myurej 5`), tab **38** su 38 unità, virgolette **72**, **9 token** in
4 famiglie (`<ship>` 3, `<last>` 3, `<planet>` 2, `<destination>` 1), tipi `40 MISSION_TEXT + 1 VALUE +
1 DESCRIPTION`, **0 `LOGBOOK`**, **0 `UI_LABEL`**. Confine dopo: riga **407** apre
`mission:Successors: Ghosts Myurej 6`.
