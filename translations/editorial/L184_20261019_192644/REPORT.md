# REPORT — L184 · `human outfits.txt` (quinto lotto: **chiude il file**)

## 1. Contenuto

Tredici unità che chiudono il file su un tono basso e concreto: un **cane** (`"Puny"`, con le virgolette nel nome), **due
pietre** che si somigliano e si distinguono solo per il calore, una **mappa** locale, e poi la scala delle **licenze** —
dal pilota privato alle quattro della Marina, fino alla licenza della milizia e alla `City-Ship License`, che chiude il
file su una sagoma che non si riconosce.

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `a dubious racing complex` | **un losco complesso per le corse** | 2 |
| `formed a strong bond` | **stretto un forte legame** | 2 |
| `vastly less urine-prone` | **molto meno incline a fare i suoi bisogni in giro** | 3 |
| `it hums with energy and heat` | **Vibra di energia e calore** | 5 |
| `wrong turns` | **sbagliare strada** | 6 |
| `at the turn of the millennium` | **al volgere del millennio** | 7 |
| `for no small fee` | **per una cifra non certo modica** | 7 |
| `freelance merchant captains` | **capitani mercantili indipendenti** | 7 |
| `not unheard of` | **nemmeno inaudito** | 8 |
| `potent symbol` | **simbolo potente** | 10 |
| `the fledgling government` | **il giovane governo** | 12 |

## 3. Difficoltà

1. **Il `VALUE` con le virgolette**: `"Puny"`. Non è un errore da ripulire — è il dato. Il controllo verifica che le 2
   virgolette del lotto siano **tutte e sole** in idx 1 e che in italiano siano le stesse 2.
2. **Due asserzioni sbagliate (mie)**, entrambe bocciate al primo giro:
   - avevo scritto **3 apici italiani distribuiti su idx 3, 9, 13**; idx 3 non ne ha nessuno (la resa usa «di Pookie»).
     Il dato reale è **idx 9 (1) e idx 13 (2)**;
   - avevo scritto **11 contesti con Puny 3 e otto con 1**: i contesti con 1 unità sono **dieci** (3 + 10 = 13).
3. **L'invariante di FILE** sostituisce il confine: somma delle 5 finestre = **63/63** unità su **63 righe distinte**,
   `min 15`, `max 606`, nessuna unità dopo la 606. È il controllo che dice davvero «il file è finito».
4. **La fila delle licenze** ha una progressione di rarità esplicita (standard → raro → molto raro → «una manciata»):
   verificata per contenuto, non per ordine di riga.
5. **Gate**: 0,96–1,37, media 1,08. Le parole sono **identiche** (458 → 458).

## 4. Numeri osservati

```
unita' 13 · 12 DESCRIPTION · 1 VALUE (`"Puny"`) · tutte PENDING
token 0 · 1 tab (3) · 2 virgolette (tutte in idx 1) · 7 apici EN · 3 apici IT
13 testi distinti · 11 contesti (Puny 3 + dieci con 1) · righe 520/606
parole 458 -> 458 (1.000) · rapporto 0.96 - 1.37, media 1.08
FAIL totale: 0 (27 controlli) · verify exit 0 (21 controlli) · sha256[:16] cb00379ce130e0d0
FILE CHIUSO: 63/63 unita (100%) · 5 finestre · 2373 EN -> 2381 IT
```

## 5. Stato del progetto (dopo L184)

```
TOTALE staging: 28292 unità · 890350 EN · 847286 IT
human outfits.txt: CHIUSO 63/63 · 5 lotti
file completi in staging: 55 (54 prima di questo lotto)
residuo traducibile (formula state.py): 3638
residuo misurato: 4307 unità / 86754 parole su 110 file
endless-sky HEAD b4aa3bac3, 0 modifiche
```

**Correzione a un numero dei documenti precedenti**: L179 e L180 dichiaravano «55 file completi». Il conteggio corretto
era **54** prima di L184 (verificato ricalcolando tutte le finestre contro il database). Il documento attuale usa il
numero misurato.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (21 controlli, invariante di FILE) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 13 unità `PENDING` — il file è tradotto, non approvato.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Ultimo lotto del file**: il contratto successivo apre **`data/gegno/gegno outfits.txt`** (`HANDOFF_L185_20261019.md`).
