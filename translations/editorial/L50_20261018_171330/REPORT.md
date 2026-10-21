# L50 — rapporto del lotto

`data/avgi/avgi 0 first contact.txt` · righe **22–402** · lotto `L50_20261018_171330` ·
**119/119 unità** · **apre il file** (0 prima / 287 dopo; file di 406) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **119 / 119** del segmento; file a **119 / 406** (29,3%) |
| parole | 4.399 EN → **4.139 IT** (0,941) |
| contesti | 4 — `Avgi: Lost in Twilight` 1–2 · **`phrase:lost in twilight`** 3 · `Avgi: First Contact` 4–44 · `Avgi: Humans From the Deep` 45–119 |
| parti | 3 — 44 · 41 · 34 |
| tab | **96 = 96** (96 unità su 119 iniziano con tab) |
| virgolette | **118 = 118** |
| virgolette dispari | **0** (asserzione di assenza dichiarata) |
| token `<...>` | **14 = 14** (5 famiglie: `<ship>` 6, `<last>` 4, `<first>` 2, `<planet>` 1, `<destination>` 1) |
| quadre `[` `]` | **0 unità** (asserzione di assenza dichiarata) |
| backtick | **0** (asserzione di assenza dichiarata) |
| `LOGBOOK` | **7**, tutte di testo (5 a tre argomenti, 1 fra backtick, 1 diretta) |
| `DIALOG` | **2** (43, 44) — controllo **positivo** |
| `TEXT` | **1** (3) — contesto **`phrase:`**, copia esatta della missione 2 |
| `CONVERSATION` | **0** (assenza dichiarata) |
| rapporto per unità | 0,81 – 1,53 |
| `check.py` | **FAIL totale: 0** (29 controlli) |
| `verify.py` | **47 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `50c003eec1b5e9a3` · `source.json` `50e8720a30ec9b7f` · `check.py` `c36d7b2c320e69f2` · `verify.py` `c97f48935877b321` |

Il segmento è il **primo** del file: `verify.py` asserisce `(first, last) == (22, 402)`,
**`0` unità prima della 22** e **`287` dopo la 402** (`tot = 406`).

## Tipi

102 `MISSION_TEXT` · 7 `LOGBOOK` · 3 `UI_LABEL` · 2 `VALUE` · 2 `DESCRIPTION` · **2 `DIALOG`** ·
**1 `TEXT`** · 0 `CONVERSATION`.

## Unità non traducibili (`NT`) — 3

| idx | riga | label |
|---:|---:|---|
| 12 | 78 | `core world` |
| 89 | 337 | `human questions` |
| 113 | 396 | `buy stuff` |

**Nessun riferimento di dato**: tutte le 7 righe `LOGBOOK` hanno il testo nell'unità.

## Le 7 righe `log`

| idx | riga | forma | contenuto |
|---:|---:|---|---|
| 1 | 22 | diretta `log "…"` | «Sono rimasto intrappolato in una regione sconosciuta…» |
| 47 | 260 | `` log `…` `` | incontro con gli Avgi, il Tangled Shroud, l'accordo sulla tecnologia |
| 48 | 261 | 3 argomenti | **Factions / Avgi**: libellule variopinte, Twilight Nebula, l'invasione degli Aberranti |
| 49 | 262 | 3 argomenti | **Factions / Avgi Consonance**: il governo degli esiliati |
| 50 | 263 | 3 argomenti | **People / Asime**: uno dei tre Primi Portavoce |
| 51 | 264 | 3 argomenti | **People / Galano**: vecchio statista |
| 52 | 265 | 3 argomenti | **People / Prasinos**: critica della storia di divisione |

## Unità speciali

- **3 `TEXT`** (riga 30, contesto `phrase:lost in twilight`): ripete **parola per parola** l'unità 2
  (missione, riga 25). La traduzione è identica nelle due unità, come nel sorgente; `verify.py` lo
  asserisce in inglese e in italiano. È il testo che il gioco mostra quando si entra nel sistema senza
  avere la missione attiva.
- **43 `DIALOG`** (riga 237): «La nave aliena è stata distrutta…» — il messaggio che compare quando il
  fallimento chiude la storia.
- **44 `DIALOG`** (riga 240): hai raggiunto `<planet>` lasciando indietro la nave aliena.

## Verifica

```
python staging/editorial/L50_20261018_171330/check.py    → FAIL totale: 0
python staging/editorial/L50_20261018_171330/verify.py   → exit 0, FAIL: 0
```

Dopo la chiusura: **22.968 unità · 732.323 EN · 694.888 IT**, **54 directory** con `translation.json`,
residuo secondo la formula `state.py` **8962**, integrità dei file protetti e del repository
(`b4aa3bac3`, nessuna modifica).

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 119 unità `PENDING`.
- **Nessun caricamento nel gioco**: il primo contatto con Lait, la sala conferenze dei Primi Portavoce e
  il dono del traduttore non sono mai stati visti a schermo.
- **Il file resta aperto**: 287 unità (da riga 413 in poi) non sono state toccate.
