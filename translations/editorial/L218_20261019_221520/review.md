# REVIEW — L218 · `successor ships.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`9e3e6ea15d7e3638…`). Tutte le 45 unità sono **`PENDING`**.

## 1. Le 39 unità copiate: perché

| gruppo | unità | esempio | motivo |
|---|---|---|---|
| `TEXT` equipaggiamento | 35 | `"Ojet" Bimodal Coilgun` | nome di prodotto nella schermata di allestimento |
| `VALUE` specie | 4 | `Aaulqran` | nome mostrato nella bacheca della nave |

Un nome di prodotto non si traduce: se lo si traducesse, il giocatore vedrebbe due nomi diversi per lo stesso oggetto in
due schermate. Il criterio è il **ruolo nel gioco**, non il tipo di record.

## 2. Decisioni di resa delle 6 `DESCRIPTION`

1. **`High Houses`** → **Alte Case**; **`People's Houses`** → **Case del Popolo**; **`Successors`** → **Successori**;
   **`Successor space`** → «spazio dei Successori». Istituzioni e popolo si traducono; `Aaulqra`, `Ejniisde`, `Kaskhorade`
   restano.
2. **`recognizable lineage continuing back several thousand years to early in the old empire`** → «una discendenza
   riconoscibile che risale a diverse migliaia di anni fa, ai primi tempi del vecchio impero». `old empire` è un'era, non
   un'entità politica del gioco: minuscolo.
3. **`compact, fast, and durable for a ship of its class`** → «compatta, veloce e resistente per una nave della sua
   classe» — la formula torna **due volte**, in 15 e in 16, e va tenuta identica.
4. **`up-and-coming Successor officers hoping to prove themselves`** → «ufficiali dei Successori in ascesa che sperano di
   dimostrare il proprio valore». Evitato «emergenti» (gergo aziendale).
5. **`ubiquitous presence`** → «presenza ubiqua»: registro saggistico coerente con il resto della scheda.
6. **`dedicated transport ship`** → «nave da trasporto dedicata»; **`unarmed by default`** → «disarmata di serie»:
   `by default` qui è *di fabbrica*, non *per impostazione predefinita*.
7. **`the star liner's lightweight hull`** → «lo scafo leggero della nave di linea»: `star liner` è la nave di linea, e
   `Ejniisde` è il nome proprio che resta.
8. **`laid over with heavy, multi-layered armor`** → «rivestito con una corazzatura pesante e multistrato».
9. **`illegal warships such as these … has been a noted concern in many recent councils`** → «navi da guerra illegali come
   queste … è stata motivo di preoccupazione in molti consigli recenti». `councils` sono le sedi di governo delle Alte
   Case, non «concili».
10. **`trades some of the maneuverability of its smaller siblings for greater flexibility`** → «baratta parte della
    manovrabilità delle sue sorelle minori in cambio di una maggiore versatilità». `siblings` sono le navi della stessa
    famiglia progettuale: «sorelle» conserva la metafora.

## 3. Un errore mio, corretto prima di chiudere

Il controllo sugli apici pretendeva le **stesse unità** in inglese e in italiano. Non è così: in inglese stanno in 15
(*ship's*), 31 (*People's*, *liner's*) e 32 (*People's*); in italiano in 15 (*L'Aaulqra*), 31 (*all'interno*,
*dell'Ejniisde*) e 45 (*un'ampia*). Il totale coincide per caso — 4 e 4 — e il totale è esattamente ciò che non basta:
ora il controllo confronta le **coppie (unità, conteggio)**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 45 unità `PENDING`.
- **Nessuna schermata di allestimento aperta**: la classificazione «nome di prodotto» è dedotta dal file, non osservata.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (17), 39 identici / 6 tradotti |
