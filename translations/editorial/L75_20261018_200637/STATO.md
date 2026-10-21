# STATO — L75 · `data/successors/successor 2 ghosts aqrabe.txt`

**Lotto chiuso.** Terzo lotto sul file: la consegna del Vujlet a Kasii-Cavasaa-Oa, l'osservatore di Kaatrij,
la nuova corazzatura, il giardino di statue e la tradizione di famiglia di Tiliia. Copre **due contesti
interi** (`Aqrabe 5` 53 unità, `Aqrabe 6` 8).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L75_20261018_200637` |
| Righe | **259–400** (finestra 256–400; la 255 è l'ultima unità di L74) |
| Unità | **61** |
| Parti | **4** — 15 · 15 · 15 · 16 |
| Contesti | **2 interi** — `Ghosts Aqrabe 5` (53), `Ghosts Aqrabe 6` (8) |
| Tipi | **55 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION` + 1 `DIALOG` + 1 `LOGBOOK`** |
| Parole | 1889 EN → 1796 IT (**0,951**) |
| Rapporto per unità | **0,72 – 1,48** (gate 0,55–1,90) |
| `NT` | **1** — unità **27**, categoria di diario `People` (`log "People" "Tiliia" "…"`) |
| `LOGBOOK` | **1** — sola **categoria**; il testo della riga **non è nel lotto** (ottavo caso della lacuna) |
| `DIALOG` | **1** — unità **15**, testo, tradotto |
| `UI_LABEL` / `CONVERSATION` / `TEXT` | **0 / 0 / 0** — assenze dichiarate (in L74 `UI_LABEL` era 1) |
| Token `<…>` | **8** in 7 famiglie: `<destination>` 2, `<origin>`/`<first>`/`<last>`/`<planet>`/`<system>`/`<capacity>` 1 |
| Tab · virgolette | **51** su **51** unità · **130** — **dispari: insieme (5, 6, 7, 8)** |
| Duplicati inglesi | **1 gruppo** — unità **6** e **8**, stessa firma, resa identica **voluta** |
| sha256 `translation.json` | `83744e86d2da8682…` |
| `check.py` | **37 controlli**, `FAIL totale: 0` |
| `verify.py` | **47 controlli**, exit **0** |

## Le virgolette dispari (5, 6, 7, 8)

Due battute di **K- I- Saajret, di Somber Sejra** spezzate a metà frase:

| unità | inglese | italiano |
|---|---|---|
| 5 | `"Please bear well this craft, captain. …` | `"Abbi cura di questa nave, capitano. …` |
| 6 | `This I myself attest as K- I- Saajret, of Somber Sejra."` | `Questo io stesso attesto, come K- I- Saajret, di Somber Sejra."` |
| 7 | `"Apologies, dear captain, …` | `"Scuse, caro capitano, …` |
| 8 | `This I myself attest as K- I- Saajret, of Somber Sejra."` | `Questo io stesso attesto, come K- I- Saajret, di Somber Sejra."` |

Il `verify.py` confronta l'**insieme** degli indici dispari **e** il fatto che la virgoletta chiuda nelle
unità 6 e 8 e **non** in 5 e 7.

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 259 | **89** (L73 + L74) |
| Unità dopo la riga 400 | **30** |
| File | **180 unità**, `max(line) = 478` |
| Confine dopo | riga **404** apre `mission:Successors: Ghosts Aqrabe 7` |
| Copertura del file | **150/180 (83,3%)** |

## Cosa è stato deciso qui

1. **`Kasii-Cavasaa-Oa`** è scritto così nel file (L74 diceva `Kasii-Cavaasa`): **non unifico** un'incoerenza
   del sorgente, la dichiaro.
2. **`Kasii-Cavaasa` resta la stella**, `Kasii-Cavasaa-Oa` è la **stazione**: due nomi diversi, due cose
   diverse, nessuna correzione.
3. **La categoria `People`** (27) resta in inglese, come in L68 e L73; il testo della stessa riga non è
   estraibile e non è nel lotto.
4. **`data-sphere` → «sfera di dati»**, coerente con L71–L72.
5. **`archivist` → «archivista»**; `K- I- Saajret` e `Somber Sejra` invariati.
6. **`thou / thee / thy / hast / shalt / 'tis / thou'rt`** resi con il «tu» moderno formale.
7. **`scions` → «eredi»** (forma fissa da L70), **`trinket` → «ninnolo»**.
8. **La «riva luminosa»** (`waves upon the bright shore`) è un'immagine ricorrente di Tiliia: resa sempre
   uguale, anche quando torna due volte nello stesso lotto.

## Verifica

```bash
cd staging/editorial/L75_20261018_200637
python check.py                 # FAIL totale: 0   (37 controlli)
python verify.py                # exit 0           (47 controlli)
```

## Prossimo passo

**L76 chiude il file**: righe **401–478** (prima unità alla **404**), **30 unità**, **822 parole**,
**1 contesto** (`Aqrabe 7`), tab **21** su 21 unità, virgolette **43**, **1 unità con virgolette dispari**
(la 25), **6 token** in 5 famiglie, tipi `24 MISSION_TEXT + 1 VALUE + 1 DESCRIPTION + 2 DIALOG +
1 LOGBOOK + 1 UI_LABEL`. Invariante **di file**: `180/180`, `max(line) = 478`, **0 unità dopo**.
