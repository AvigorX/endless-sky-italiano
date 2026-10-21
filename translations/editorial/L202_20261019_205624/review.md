# REVIEW — L202 · `hai outfits.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`2281312fe0da11a4…`). Tutte le 16 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **Tre `VALUE` identici (4, 6, 8)**: `Skipper Railgun Slug`, `Skipper Slug Rack`, `Skipper Railgun`. Sono nomi di
   munizione e d'arma: restano inglesi, e nel testo si declinano solo con l'articolo («i proiettili **dello** Skipper
   Railgun»).
2. **`outfitter` → «negozio di equipaggiamenti»** (unità 11 e 15): il glossario vieta il prestito e indica la forma di
   prosa. La stessa frase in due punti ha la stessa resa, verificata.
3. **`hit force` → «forza d'urto»**: resa già presente in staging per la statistica omonima.
4. **`homing` → «a ricerca»** (unità 14): in staging esistono anche «a inseguimento»; si sceglie la forma più diffusa e
   si usa una sola volta in questo lotto, quindi non c'è conflitto interno.
5. **`raw damage` → «danni grezzi»** (unità 1 e 2): il contrasto con i danni *da ioni* resta leggibile.
6. **`venerabile Ion Cannon`**: «venerabile» conserva l'ironia affettuosa dell'inglese; «venerando» sarebbe stato
   troppo solenne.
7. **`C'è probabilmente una componente culturale che molti non colgono`** (unità 10): *that many miss* non è «che molti
   perdono» — è «che molti non afferrano». Il verbo giusto evita un falso senso.
8. **`dalla parte sbagliata`** scartato a favore di **«così sfortunato da essere colpito»** (unità 14): più vicino a
   *on the receiving end* e senza metafora aggiunta.
9. **Il refuso del sorgente** — *weapon jamming affects* per *effects* (unità 2) — non si corregge nel gioco: la resa
   traduce il senso e l'anomalia è qui dichiarata.
10. **`prodotto in serie`** per *mass-produced* (unità 3) e **`esemplari realizzati`** per *those that have been
    produced*: la ripetizione italiana sarebbe stata pesante, e il senso resta distinto.

## 2. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 16 unità `PENDING`.
- **Nessun equipaggiamento installato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: il refuso su *affects* resta nel gioco.

## 3. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (17 controlli) |
