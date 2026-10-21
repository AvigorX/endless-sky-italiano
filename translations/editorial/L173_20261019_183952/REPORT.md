# REPORT — L173 · `paradise world jobs.txt` (settimo lotto: **chiude il file**)

## 1. Contenuto

Tre missioni di soccorso per il personale di aiuto (`Relief workers`): chi arriva per **alleggerire gli ospedali**, chi
per gli **sforzi di soccorso**, chi per **accoglienza e ricostruzione**. Le tre `DESCRIPTION` sono per il resto identiche,
compresa la coda sullo spazioporto.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `release demand from overloaded hospitals` | **alleggerire la pressione sugli ospedali sovraccarichi** | 2 |
| `assist in Martini's relief efforts` | **dare man forte agli sforzi di soccorso di Martini** | 4 |
| `accommodation and reconstruction efforts` | **sforzi di accoglienza e ricostruzione** | 6 |
| `Relief workers to Martini` | **identico** (`VALUE`) | 1, 3, 5 |

## 3. Difficoltà

1. **Tre `VALUE` identici**: l'unica cella che distingue le missioni è il contesto. Il controllo pretende che la resa sia
   una sola.
2. **Tre `DESCRIPTION` che differiscono solo per lo scopo**: verificate in **positivo** (ogni scopo c'è dove deve stare) e
   in **negativo** (nessuno scopo compare nell'unità sbagliata), più una prova strutturale: rimuovendo la frase dello
   scopo, le tre stringhe devono diventare **una sola**.
3. **`<martini relief occupations>`** (3 volte): segnaposto **composto**, da confrontare intero.
4. **Errore in corsa (mio)**: il controllo negativo usava `r'<martini\s+relief'`, che combacia con il **segnaposto
   integro** (contiene uno spazio) → FAIL su una resa corretta. Corretto in `r'<martini>\s+relief'` più l'assenza della
   parola `relief` **fuori** dai tag.
5. **`Martini's` → «di Martini»**: l'apostrofo inglese sparisce. Verificato come **causa** (1 in EN, 0 in IT), non come
   uguaglianza fra le lingue.
6. **Invariante di FILE**: 7 finestre = 131 unità su 131 righe distinte, `min 16`, `max 1413`, zero sovrapposizioni,
   copertura esatta dell'insieme delle righe del file.

## 4. Numeri osservati

```
unita' 6 · 3 VALUE · 3 DESCRIPTION · tutte PENDING
token 12 su 4 simboli · 0 tab · 0 virgolette
4 testi distinti · 3 contesti · righe 1356/1413
parole 128 -> 147 (1.148) · rapporto 1.00 - 1.24, media 1.11
FAIL totale: 0 (24 controlli) · verify exit 0 (23 controlli) · sha256[:16] 5a289568b9f21fbf
FILE CHIUSO: 131/131 unita (100%) · 2918 EN -> 3044 IT
```

## 5. Stato del progetto (dopo L173)

```
TOTALE staging: 28127 unità · 885449 EN · 842236 IT
paradise world jobs.txt: 131/131 (100%) · 7 lotti — CHIUSO
file completi in staging: 54 (0 parziali) — misurato dai translation.json contro il DB
residuo traducibile (formula state.py): 3803
residuo misurato: 4472 unità / 91655 parole su 112 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (23 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 6 unità `PENDING` (il file è tradotto, non approvato).
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Ultimo lotto del file**: il contratto successivo apre **`data/avgi/avgi ships.txt`** (`HANDOFF_L174_20261019.md`).
