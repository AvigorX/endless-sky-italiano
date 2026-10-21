# STATO — L77 · `data/successors/successor side missions.txt` (primo lotto, file nuovo)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L77_20261018_201509` |
| Righe | **17–220** (finestra 1–220: il file apre con i tag della prima missione) |
| Unità | **63** |
| Parti | **4** — 16 · 16 · 16 · 15 |
| Contesti | **2 interi** — `Predecessor Research 1` (37), `Biology Research 1` (26) |
| Tipi | **58 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION` + 1 `UI_LABEL`** |
| Parole | 1909 EN → 1829 IT (**0,958**) |
| Rapporto per unità | **0,78 – 1,30** |
| `NT` | **1** — unità **12**, `label "has deferred"` (identica) |
| `LOGBOOK` / `DIALOG` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate (in L76: 1, 2, 0, 0) |
| Token `<…>` | **13** in 6 famiglie: `<destination>` 4, **`<planet stopovers>` 3**, `<date>` 2, `<payment>` 2, `<bunks>` 1, `<stopovers>` 1 |
| Tab · virgolette | **53** su **53** unità · **68** — **2 dispari (56, 57)** |
| Duplicati inglesi | **3 gruppi** — 7/42, 9/43, 28/55 (le stesse opzioni in due missioni), resa identica **voluta** |
| sha256 `translation.json` | `5e8d1c0e38c05612…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **45 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 17 | **0** (il lotto apre il file) |
| Unità dopo la riga 220 | **101** |
| File | **164 unità**, `max(line) = 453` |
| Confine dopo | riga **224** apre `mission:Successors: Stargazing 1` |
| Copertura | **63/164 (38,4%)** |

## Cosa è stato deciso qui

1. **`has deferred` resta identica**: è una `label` di salto, non prosa.
2. **Due battute non chiudono la virgoletta** (56, 57): il biologo parla per tre unità e la chiusura arriva
   solo in 58. Riprodotto; il `verify.py` verifica insieme **e** direzione (aprono, non chiudono).
3. **Tre coppie di opzioni identiche** (7/42, 9/43, 28/55) fra le due missioni: stessa resa, dichiarata come
   gruppo. Ma **22 ≠ 50**: `(Don't ask them anything.)` → «(Non chiedere loro nulla.)» e `(Don't ask
   anything.)` → «(Non chiedere nulla.)» — due inglesi diversi, due rese diverse (decisione 216). Il primo
   giro era rosso proprio lì.
4. **`Katiiora` (61) è un refuso del sorgente per `Kaatiora`**: reso **Kaatiora**, senza replicare il refuso.
5. **`Sieasej`** invariato; **`House Sioeora` → «Casa Sioeora»**; **`Academy` → «Accademia»**.
6. **`fifteen hundred years` → «millecinquecento anni»**: avevo scritto «milletrecento», corretto prima di
   chiudere (numero nel testo, non solo cifra).
7. **`hermaphroditic` → «ermafrodita»**, **`xenobiology` → «xenobiologia»**, **`research leave` → «congedo di
   ricerca»**.

## Verifica

```bash
cd staging/editorial/L77_20261018_201509
python check.py                 # FAIL totale: 0   (32 controlli)
python verify.py                # exit 0           (45 controlli)
```

## Prossimo passo

**L78** continua lo stesso file: righe **221–325** (prima unità alla **224**), **53 unità** in **un contesto
intero** (`Stargazing 1`), **1.109 parole**, tab **46** su 46 unità, virgolette **86**, **0 dispari**,
**13 token** in 7 famiglie (`<ship>` 4, `<home system>` 4), tipi `49 MISSION_TEXT + 1 VALUE +
1 DESCRIPTION + 2 UI_LABEL`.
