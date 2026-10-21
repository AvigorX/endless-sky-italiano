# REPORT — L154 · `coalition jobs.txt` (i lavori Heliarch e le nove consegne del Lunarium (chiude il file))

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| prigionieri | 1-3 | 1475-1493 | `Transport Prisoners`, la scorta, il pagamento |
| indagine | 4-7 | 1499-1517 | `Investigate signs of criminal activity`, gli agenti, le prove |
| evacuazione riuscita | 8-11 | 1523-1550 | `Rescue Lunarium Members`, l'imbarco, il ringraziamento |
| evacuazione fallita | 12-14 | 1555-1576 | stesso lavoro, gli Heliarch arrivati prima |
| nove consegne Lunarium | 15-41 | 1583-1807 | reattori, lanciatori, torrette, granate: nove `VALUE` + nove `DESCRIPTION` + nove `DIALOG` |

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `Transport Prisoners` · `Investigate…` · `Rescue Lunarium Members` · `X Delivery` | **identici** (13 `VALUE`) | 1, 4, 8, 12, 15…39 |
| `Payment is <payment>.` | **Il compenso è di `<payment>`.** | 2 |
| `Pick up <bunks> … by <date>.` | **Preleva `<bunks>` … entro il `<date>`.** | 9, 13 |
| `The Lunarium is offering <payment> for you to deliver …` | **Il Lunarium offre `<payment>` per consegnare …** | 16, 19, 22, 25, 28, 31, 34, 37, 40 |
| `as instructed` | **come richiesto** | 17…41 |
| `quietly transporting the reactor / the turret / the grenades / the cargo away` | **portare via il reattore / la torretta / le granate / il carico in silenzio** | 17, 20, 23, 26, 29, 32, 35, 38, 41 |

## 3. Difficoltà

1. **Zero tab e zero virgolette** nel lotto: due asserzioni vuote scritte (`== []`, `== 0`), non omesse.
2. **`<destination>` ≠ `<planet>`**: i 9 `DIALOG` di consegna hanno solo `<planet>`, le 8 `DESCRIPTION` solo `<destination>`; il controllo verifica l'**assenza incrociata**, non solo i totali.
3. **Le due `Rescue Lunarium Members`** sono lo stesso `VALUE` con descrizioni diverse per un articolo («Pick up the» / «Pick up»): la resa distingue «Preleva» da «Preleva i» e il controllo pretende che siano **diverse**.
4. **Nove famiglie regolari**: il controllo esige che tutte e nove condividano le tre giunture fisse e che ciascuna nomini il proprio oggetto e la propria coda.
5. **Errore in corsa (due volte)**: un controllo cercava `completo di` nell'inglese (che dice `complete with`) e le 7 descrizioni semplici erano confuse con le 2 con complemento. Corretto il controllo, non la resa.

## 4. Numeri osservati

```
unita' 41 · 15 DIALOG · 13 VALUE · 13 DESCRIPTION · tutte PENDING
token 57 su 7 simboli: <payment> 23, <destination> 14, <planet> 9, <bunks> 4, <stopovers> 3, <origin> 2, <date> 2
40 testi distinti · 13 contesti · tab 0 · virgolette 0
parole 725 -> 721 (0.994) · rapporto 0.87 - 1.20
righe 1475/1807
FAIL totale: 0 (29 controlli) · verify exit 0 (28 controlli) · sha256[:16] 38054e95406a979e
```

## 5. Stato del progetto (dopo L154)

```
TOTALE staging: 27843 unità · 876164 EN · 832509 IT
residuo traducibile (formula state.py): 4087
file completi: 51
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 41 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Lotto del batch L154–L160**: contratto = piano del batch, nessun `HANDOFF_L154` separato.
