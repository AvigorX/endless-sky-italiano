# REPORT — L87 · `data/successors/successor outfits.txt`

## 1. Contenuto

Tredici schede in nove contesti: due reattori a fusione (`"Ryuit"`, e il più potente, a forma di pianta
fiorita, che sostiene la rete di distribuzione delle Alte Casate), il raffreddamento bimodale, la vela solare
«stranamente rustica», due scanner (`"Veldt"` da combattimento, `"Tuur"` per l'analisi planetaria), i motori
induttivi `"Niis"` e i tre propulsori `"Aqra"`.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `"Niis" Inductive Engines` | **identico** | `VALUE`: nome di dato |
| `stellarator` | **stellator** | nome di macchina (L86) |
| `ramscoop` | **ramscoop** | tecnologia, non un'immagine: tradurlo la renderebbe opaca |
| `afterburning modes` | **modalità di postbruciatore** | `afterburner` è il termine aeronautico italiano |
| `steering thrusters` | **propulsori di manovra** | distinti da quelli lineari |
| `fuel sail` | **vela** / `raccoglitore di carburante` | «vela solare» è il concetto, `fuel sail` il nome |
| `black markets` | **mercati neri** | forma corrente |
| trattino lungo (unità 7) | **due punti** | em dash vietato |
| `bimodal` | **bimodale** | coerente con L86 |

## 3. Difficoltà

1. **Tre tab** (unità 2, 7, 9): dopo l'unico tab di L86, il lotto ne ha tre, e il `verify.py` li elenca.
2. **Nove contesti in tredici unità**: la cella `Contesti` va in ordine di riga, non alfabetico — errore che
   avevo già fatto nell'handoff L87 e che il checker ha colto.
3. **Directory**: l'export ne ha creata una con timestamp diverso da quello che avevo scritto nei path; ho
   spostato parti e script nella directory reale e rimosso quella vuota, invece di dichiarare un lotto
   inesistente.
4. **`1,33`** (unità 3, la più lunga): il valore più alto del file, dentro il gate.

## 4. Numeri osservati

```
unita' 13/13 · tab 3 (2,7,9) · virgolette 2 = 2 · dispari 0
token 0 · duplicati 0 · rapporto 1.00 - 1.33
parole EN 572 -> IT 591 · righe 251/409
FAIL totale: 0 (24 controlli) · verify exit 0 (24 controlli)
sha256[:16] 667d024aa8548de4
```

## 5. Stato del progetto

```
TOTALE staging: 24851 unita · 791663 EN · 750606 IT
successor outfits.txt: 34/56 (60,7%) · 1593 EN -> 1633 IT · 2 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli) **e** `verify.py` exit **0** (24 controlli) |
