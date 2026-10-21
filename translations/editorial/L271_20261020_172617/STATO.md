# STATO — L271 (`data/dialog phrases.txt`, righe 16–98)

**Stato: CHIUSO.** Primo lotto del file delle **frasi generiche** delle missioni: **29 `TEXT`** in **20 contesti `phrase:`**. Il
file è aperto a **29/54 (53,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L271_20261020_172617/` |
| file | `data/dialog phrases.txt` (54 unità · 876 parole · righe 16–172) |
| righe | 16–98 |
| unità | **29** — tutte `TEXT` |
| parole | **430 EN → 400 IT** (0,93) |
| contesti | **20** `phrase:generic …` |
| segnaposto | **45** in **10 famiglie**, conteggi **identici** in inglese e italiano |
| tab / virgolette | **0 / 0** (asserzioni negative) |
| apici | **17 EN** su 10 unità / **0 IT** |
| `check.py` | **27 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 29 qui · **25 dopo** la 98 |
| `sha256[:16]` | **`f97f37769e07cdec`** |

## Comandi

```bash
python staging/editorial/L271_20261020_172617/check.py     # FAIL totale: 0 (27 controlli)
python staging/editorial/L271_20261020_172617/verify.py    # FAIL: 0 (20 controlli, 29/54)
```

## Le tre cose delicate

1. **Le unità 3–11 non sono frasi: sono frammenti** del `phrase "generic pirate attack payment dialog"`, che il gioco compone
   **concatenando senza separatore** sei blocchi alternativi (governo / ringraziamento **o** spazio / pagamento / modo /
   articolo / predone). Il `check.py` **compone tutte le 12 combinazioni** e verifica che nessuna abbia doppi spazi, spazio
   prima del punto o segnaposto mancanti. Perché l'articolo `i` funzioni con tutti e tre i sostantivi, il terzo è
   **«razziatori»** (`raiders`), non «aggressori» (che avrebbe voluto `gli`).
2. **Il blocco ` ` alla riga 24 non è nel database**: l'estrattore salta le stringhe di **solo spazio bianco**. È una
   **lacuna dichiarata** — quel frammento non è traducibile e resta uno spazio — e la resa italiana funziona **anche** con
   esso, grazie allo spazio finale del blocco ringraziamento.
3. **45 segnaposto in dieci famiglie**, verificati **per famiglia e per unità**: `<planet>` 17, `<payment>` 7, `<stopovers>` 5,
   `<waypoints>` 4, `<npc>` 4, `<passengers>` 2, `<amount>` 2, `<mineral>` 2, `<commodity>` 1, `<origin>` 1.

## Limiti dichiarati

Nessuna approvazione (29 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **25 unità** (L272,
che chiude il file).
