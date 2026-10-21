# STATO — L322 (`data/human/frontier jobs.txt`, righe 16–318)

**Stato: CHIUSO — LOTTO TERMINALE, FILE INTERO.** Il file è **completo: 45/45 (100%)**, **trentaseiesimo file interamente tradotto**
(**95** su 167 nel progetto). `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L322_20261020_223939/` |
| file | `data/human/frontier jobs.txt` (**45/45 unità · 1.014 parole · righe 16–318**) |
| righe | 16–318 (**tutto il file**) |
| unità | **45** — **7 `VALUE` + 6 `UI_LABEL` + 8 `DESCRIPTION` + 4 `DIALOG` + 20 `MISSION_TEXT`** |
| contesti | **9** |
| parole | **1.014 EN → 999 IT** (0,985) |
| rapporto | **0,63 – 1,58** |
| tab | **19** |
| virgolette | **4** in **2** unità (277, 281) |
| segnaposto | **10 tipi**, identici per tipo |
| alternative | **0** |
| apici | **18 EN in 12 unità** / 13 IT |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 45 unità · **0 prima, 0 dopo** · 45 righe distinte · prima **16** · ultima **318** |
| `sha256[:16]` | **`e2cd7a9a14ff7c62`** |

## Comandi

```bash
python staging/editorial/L322_20261020_223939/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L322_20261020_223939/verify.py    # FAIL: 0 (21 controlli, FILE 45/45)
```

## Il primo lotto a **cinque tipi**, e perché i controlli sono **per gruppo**

| gruppo | tipi | unità | trattamento | verifica |
|---|---|---|---|---|
| **A — copiati** | `VALUE` (7), `UI_LABEL` (6) | **13** | **identici all'inglese** | per tipo, non in somma |
| **B — tradotti** | `DESCRIPTION` (8), `DIALOG` (4), `MISSION_TEXT` (20) | **32** | **diversi dall'inglese** | per tipo, non in somma |

La trappola dichiarata nel contratto — **le `UI_LABEL` sembrano prosa** — è la cosa più importante del lotto:

```
good luck   bad luck   shoot and die   shoot and run   grab and die   grab and run
```

Sono **etichette di salto** (`label`/`goto`) di una conversazione di missione: il giocatore **non le vede mai**. Il test le **elenca**
e le pretende **identiche** all'inglese. Se fossero state tradotte in «buona fortuna», «spara e muori», la conversazione avrebbe
**rotto i salti** — un danno silenzioso, che nessun controllo sul numero di parole avrebbe rilevato.

## Il contenuto: sei lavori, un casinò

| contesto | unità | che cosa |
|---|---|---|
| `Frontier delivery [0/1/2]` | 6 | tre consegne **identiche** a mondi di frontiera, con **pirateria** e pagamento |
| `Frontier Emigration [0/1/2]` | 6 | tre emigrazioni **identiche**: passeggeri che hanno **messo da parte** abbastanza per una nuova vita |
| `Disaster Relief` | 3 | una **catastrofe** in una colonia, con **scadenza** (`<date>`) |
| `Instruct Novice Pilot` | 4 | **istruzione** a un pilota alle prime armi, con **tre dialoghi** (uno dei quali è un **ammonimento**: hai dimenticato la `<npc>`) |
| `Small Pirate gambling` | 26 | il **casinò**: bevuta, sospetto, partita, quattro finali |

## I quattro finali del casinò: due coppie

```
(shoot first!)   →  muori  /  spari e scappi
(grab the pot)   →  muori  /  arraffi e scappi
```

I finali «scappa» (303 e 318) hanno **la stessa prima frase** e **diversa la seconda**: nel primo i due pirati **ti inseguono
insultandoti**, nel secondo le **autorità** ti avvisano che due sono stati fermati e due ti inseguono. Il test verifica **entrambe** le
cose — l'identità dell'esordio e la **differenza** del resto — perché due finali identici sarebbero un errore, e due finali
completamente diversi avrebbero perso la simmetria del sorgente.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| gruppi | **13 copiati** identici / **32 tradotti** diversi, **per tipo** |
| `UI_LABEL` | elenco esatto delle **6 etichette** |
| `VALUE` | conteggio dei **3 titoli ripetuti** |
| tab | **19** righe esatte |
| virgolette | **4** in **due** unità (277, 281) |
| apici | **18** in **12** unità, con i picchi (263:3, 281:4, 302:2) |
| segnaposto | **10 tipi**, per tipo |
| seconda persona | presente nei `MISSION_TEXT` |
| ripetizioni | le tre consegne **identiche**, le tre emigrazioni **identiche** |
| `<npc>` | **femminile**: «la `<npc>`» |
| FILE | **0 prima · 45 qui · 0 dopo** · prima 16 · ultima 318 · **45/45 asserita** |

## Limiti dichiarati

Nessuna approvazione (45 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato. **Il rapporto 0,63 – 1,58 è largo**: il minimo è la scelta del giocatore `(Say nothing and continue playing.)` →
«(Non dire nulla e continua a giocare.)», il massimo la scelta `(Join their game.)` → «(Unisciti alla loro partita.)» — frasi
**cortissime**, dove l'italiano può comprimere o allungare molto senza che nulla cambi.
