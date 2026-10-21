# L46 — rapporto del lotto

`data/successors/successor 1 prologue.txt` · righe **24–664** · lotto `L46_20261018_164912` ·
**221/221 unità del segmento** · file **non completo** (345 unità totali, 124 dopo la riga 664) ·
chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **221 / 221** del segmento; file a **221 / 345** (64,1%) |
| parole | 7.180 EN → **6.973 IT** (0,971) |
| contesti | 6 (`Successors: Entering the Scar`, `Safe at Last`, `First Contact 1`, `First Contact 2 Prompt`, `First Contact 2`, `First Contact 3`) |
| parti | 5 — 56 · 47 · 47 · 40 · 31 |
| tab | **175 = 175** (175 unità che iniziano con tab) |
| virgolette | **278 = 278** |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **36 = 36** (8 famiglie) |
| quadre `[` `]` | **0 unità** (asserzione di assenza dichiarata) |
| `LOGBOOK` | **9** (8 testi + 1 categoria) |
| `CONVERSATION` | **0** (asserzione di assenza dichiarata) |
| rapporto per unità | 0,74 – 1,38 |
| `check.py` | **FAIL totale: 0** (27 controlli) |
| `verify.py` | **37 controlli**, exit 0, `FAIL: 0` (copertura del segmento per righe) |
| sha256[:16] | `translation.json` `aa71c36e9b399505` · `source.json` `526d91c35b570438` · `check.py` `ce8d23f86df99076` · `verify.py` `a30fbfac1bdf18b5` |

Segmento **interno**: `verify.py` asserisce `(first, last) == (24, 664)`, `0` unità prima della 24 e
**`124` dopo la 664** (`max(line) = 1024`). La copertura totale del file **non** è un invariante di
questo lotto.

## Tipi

187 `MISSION_TEXT` · 17 `UI_LABEL` · **9 `LOGBOOK`** · 3 `VALUE` · 3 `DESCRIPTION` · 2 `DIALOG` ·
0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 18

### 17 `UI_LABEL` (label di salto, bersagli di `goto`)

| idx | riga | label |
|---:|---:|---|
| 44 | 157 | `language short` |
| 54 | 194 | `what now` |
| 81 | 274 | `apologize tardiness` |
| 123 | 396 | `jump drives` |
| 126 | 406 | `you okay` |
| 128 | 411 | `watch out` |
| 134 | 436 | `retrieve tranqs` |
| 152 | 485 | `tranq friends` |
| 154 | 488 | `net friends alarmed` |
| 156 | 491 | `bring tranq` |
| 163 | 504 | `shoot ambush` |
| 172 | 524 | `ship shoot` |
| 175 | 534 | `release friends` |
| 183 | 553 | `take off` |
| 185 | 558 | `better late than never` |
| 191 | 571 | `back alive` |
| 193 | 573 | `released 2` |

### 1 riferimento di dato

| idx | riga | tipo | valore |
|---:|---:|---|---|
| 62 | 235 | `LOGBOOK` | `People` (categoria di diario) |

## Le 9 righe `log` — tre forme diverse

| idx | riga | forma | contenuto (italiano) |
|---:|---:|---|---|
| 19 | 77 | `log "testo"` | contatto con gli alieni, dispositivo accettato |
| 21 | 82 | `log "testo"` | contatto, dispositivo rifiutato |
| 25 | 104 | `` log `testo` `` | contatto con «i Successori», ritorno a Staja-Kella-Oa |
| 26 | 105 | `log "Categoria" "Nome" `testo`` | i Successori come società e come governo |
| 62 | 235 | `log "Categoria" "Nome" "testo"` | **categoria `People`** (testo fuori dall'unità) |
| 98 | 309 | `log "testo"` | l'animale di Raaqa-Uur-Kaav, offerta **accettata** |
| 100 | 314 | `log "testo"` | l'animale di Raaqa-Uur-Kaav, offerta **rifiutata** |
| 197 | 593 | `log "testo"` | l'animale **liberato**, rapporti con la Casa interrotti |
| 204 | 616 | `log "testo"` | l'animale **consegnato**, dispositivo e dati storici |

Le tre forme sono identificate **sul `raw`** da `verify.py`: 6 dirette, 1 con backtick, 1 a tre
argomenti. Un controllo che assumesse una forma sola sarebbe cieco sulle altre due.

## I 6 contesti, con le unità

| contesto | unità | righe |
|---|---:|---|
| `Successors: Entering the Scar` | 1 | 1 |
| `Successors: Safe at Last` | 1 | 2 |
| `Successors: First Contact 1` | 54 | 3–56 |
| `Successors: First Contact 2 Prompt` | 5 | 57–61 |
| `Successors: First Contact 2` | 42 | 62–103 |
| `Successors: First Contact 3` | 118 | 104–221 |

## Verifica

```
python staging/editorial/L46_20261018_164912/check.py    → FAIL totale: 0
python staging/editorial/L46_20261018_164912/verify.py   → exit 0, FAIL: 0
```

`state.py` dopo la chiusura: **22.289 unità · 710.563 EN · 674.096 IT**, `ESITO: OK`, integrità dei file
protetti e del repository (`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 221 unità `PENDING`.
- **Nessun caricamento nel gioco**: nessuna verifica a schermo dei dialoghi con Sieasej e Riijaaora.
- **Il file resta aperto**: 124 unità (righe 680–1024) previste in L47.
