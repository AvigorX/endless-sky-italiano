# STATO — L74 · `data/successors/successor 2 ghosts aqrabe.txt`

**Lotto chiuso.** Secondo lotto sul file: il giardino di metallo stellare, l'immersione nella stella
Kasii-Cavaasa e il Vujlet modificato di Casa Kaatrij. Copre **due contesti interi** (`Aqrabe 3` e `Aqrabe 4`).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L74_20261018_200143` |
| Righe | **161–255** (finestra 159–255; la 158 è l'ultima unità di L73) |
| Unità | **38** |
| Parti | **3** — 13 · 12 · 13 |
| Contesti | **2** — `Ghosts Aqrabe 3` (23 unità), `Ghosts Aqrabe 4` (15) |
| Tipi | **32 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION` + 1 `LOGBOOK` + 1 `UI_LABEL`** |
| Parole | 1106 EN → 1077 IT (**0,974**) |
| Rapporto per unità | **0,67 – 1,70** (gate 0,55–1,90) |
| `NT` | **1** — unità **19**, `label "no shields"` (identica) |
| `LOGBOOK` | **1** — unità **21**, forma **diretta** `log "…"`, testo tradotto |
| `VALUE` / `DESCRIPTION` | **2 / 2** — unità 1 e 24 (nomi), 2 e 25 (descrizioni) |
| `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** — assenze dichiarate (in L73 erano 1 e 6) |
| Token `<…>` | **10** in 4 famiglie: `<ship>` 6, `<planet>` 2, `<origin>` 1, `<destination>` 1 |
| Tab · virgolette | **28** su **28** unità con tab iniziale · **68** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **1 gruppo** — `\t(Retreat.)` unità **12** e **16**, resa identica **voluta** |
| sha256 `translation.json` | `3928a76816c49f89…` |
| `check.py` | **34 controlli**, `FAIL totale: 0` |
| `verify.py` | **44 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 161 | **51** (L73, righe 23–158) |
| Unità dopo la riga 255 | **91** |
| File | **180 unità**, `max(line) = 478` |
| Confine dopo | riga **259** apre `mission:Successors: Ghosts Aqrabe 5` |
| Copertura del file | **89/180 (49,4%)** |

## Cosa è stato deciso qui

1. **Due `(Retreat.)` identici** (12 e 16): stesso inglese, stessa resa «(Ritirata.)». È l'unico caso in cui
   la ripetizione è corretta, e il `check.py` lo dichiara come **gruppo** con l'elenco degli indici.
2. **Le due scelte opposte sono distinte**: `(Press on.)` → «(Insisti.)» e `(Keep going.)` → «(Continua.)».
   Due inglesi diversi non diventano la stessa frase (decisione 216).
3. **`no shields` resta identica** (unità 19): è il nome di un nodo di salto, non prosa.
4. **L'inglese arcaico** (`thee`, `thy`, `hath`, `thou needest`, `'tis`) resta reso con il «tu» moderno
   formale già fissato in L45–L73; nessun arcaismo italiano.
5. **`New Houses` → «Nuove Casate»** (nuova forma, coerente con `Casa X` / `Casate`).
6. **`Tangles` non si traduce** (nome di regione), come `Shroud` e `Deep`.
7. **`Vujlet` / `Vujleten`** invariati; «un Vujlet modificato» non prende l'articolo inglese.
8. **Il tema del suicidio involontario** (unità 18, eruzione solare): reso letteralmente, senza edulcorare.

## Verifica

```bash
cd staging/editorial/L74_20261018_200143
python check.py                 # FAIL totale: 0   (34 controlli)
python verify.py                # exit 0           (44 controlli)
```

## Prossimo passo

**L75** chiude il file in due tappe: righe **256–400** (prima unità alla **259**), **61 unità**,
**1.889 parole**, **2 contesti interi** (`Aqrabe 5` 53 unità e `Aqrabe 6` 8), tab **51** su 51 unità,
virgolette **130**, **8 token** in 7 famiglie, tipi `55 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION +
1 DIALOG + 1 LOGBOOK`; **4 unità con virgolette dispari** (5, 6, 7, 8) da riprodurre. Poi L76 con
`Aqrabe 7` (30 unità, fino alla 478) chiude il file.
