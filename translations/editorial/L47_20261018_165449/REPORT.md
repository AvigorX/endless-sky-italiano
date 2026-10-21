# L47 — rapporto del lotto

`data/successors/successor 1 prologue.txt` · righe **680–1024** · lotto `L47_20261018_165449` ·
**124/124 unità** · **file completo 345/345** con L46 (221 + 124) · chiuso il 2026-10-18.

## Numeri

| voce | valore |
|---|---|
| unità | **124 / 124** del segmento; **file 345 / 345** (L46 221 + L47 124) |
| parole | 4.128 EN → **4.032 IT** (0,977) |
| contesti | 3 (`Successors: Kaatrij Monoglot Prompt`, `Kaatrij First Contact`, `Trusted`) |
| parti | 3 — 45 · 40 · 39 |
| tab | **102 caratteri su 100 unità** (98 con 1 tab, 2 con 2) |
| virgolette | **124 = 124** |
| virgolette dispari | **2** (46, 63), stessi idx in italiano |
| token `<...>` | **24 = 24** (9 famiglie) |
| quadre `[` `]` | **1 unità** (21), conteggio invariato per unità |
| `LOGBOOK` | **4** (3 testi + 1 categoria) |
| `DIALOG` / `CONVERSATION` | **0 / 0** (asserzione di assenza per `CONVERSATION`) |
| rapporto per unità | 0,70 – 1,69 |
| `check.py` | **FAIL totale: 0** (26 controlli) |
| `verify.py` | **38 controlli**, exit 0, `FAIL: 0` |
| sha256[:16] | `translation.json` `d783356009cbb44d` · `source.json` `5b3176095f06afad` · `check.py` `476f337e6f5a2848` · `verify.py` `850b1b38e3015dfd` |

Il segmento **chiude il file**: `verify.py` asserisce `(first, last) == (680, 1024)`, **221** unità prima
della 680 (L46) e **0** dopo la 1024 (`max(line) = 1024`).

## Tipi

108 `MISSION_TEXT` · 8 `UI_LABEL` · **4 `LOGBOOK`** · 2 `VALUE` · 2 `DESCRIPTION` ·
0 `DIALOG` · 0 `CONVERSATION` · 0 `TEXT`.

## Unità non traducibili (`NT`) — 9

| idx | riga | tipo | valore |
|---:|---:|---|---|
| 6 | 728 | `UI_LABEL` | `was monoglot` |
| 12 | 740 | `UI_LABEL` | `hai monoglot` |
| 18 | 750 | `UI_LABEL` | `message coalition` |
| 20 | 753 | `UI_LABEL` | `message hai` |
| 79 | 937 | `UI_LABEL` | `sioeora opposed` |
| 81 | 939 | `UI_LABEL` | `sioeora choice` |
| 85 | 951 | `UI_LABEL` | `about you` |
| 112 | 999 | `UI_LABEL` | `no kaatrij` |
| 54 | 838 | `LOGBOOK` | `People` (categoria di diario) |

## Le 4 righe `log` — due forme

| idx | riga | forma | contenuto (italiano) |
|---:|---:|---|---|
| 54 | 838 | `log "Categoria" "Nome" "testo"` | **categoria `People`** (testo fuori dall'unità) |
| 59 | 852 | `log "testo"` | la convocazione di Kaatrij, il dono, i dati culturali |
| 67 | 902 | `log "testo"` | la convocazione al consiglio, il diritto d'acquisto |
| 68 | 903 | `log "Categoria" "Nome" `testo`` | le Casate Vecchie e Nuove, il consiglio |

## L'unica unità con quadre

| idx | riga | testo (italiano) |
|---:|---:|---|
| 21 | 754 | `CASA KAATRIJ [RICHIEDE, ESIGE] UDIENZA DEL CAPITANO UMANO` |

Annuncio in maiuscolo proiettato dalla sfera di dati: le parentesi quadre **non** sono marcatori di testo
redatto ma parte del messaggio, e il conteggio è invariato (1 `[`, 1 `]`).

## Verifica

```
python staging/editorial/L47_20261018_165449/check.py    → FAIL totale: 0
python staging/editorial/L47_20261018_165449/verify.py   → exit 0, FAIL: 0
```

`state.py` dopo la chiusura: **22.413 unità · 714.691 EN · 678.128 IT**, `ESITO: OK`, integrità dei file
protetti e del repository (`b4aa3bac3`, nessuna modifica). Il file `successor 1 prologue.txt` è al
**100%** su due lotti: i file completi dello staging sono **ventisei**.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: 124 unità `PENDING` (345 con L46).
- **Nessun caricamento nel gioco**: la scena del consiglio delle Casate non è mai stata vista a schermo.
- **Nessun test di gameplay** della linea Successors.
