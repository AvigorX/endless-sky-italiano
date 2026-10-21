# REPORT — L251 (`data/human/syndicate jobs.txt`, righe 701–814) — LOTTO TERMINALE

**Esito: lotto CHIUSO, file COMPLETO.** `check.py` esce 0 con **30 controlli**; `verify.py` esce 0 con **25 controlli**
(invariante di **file**: 94/94). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

**`data/human/syndicate jobs.txt` è il dodicesimo file chiuso della campagna: 94/94 unità.**

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Megaparsec Shipment [0]` | 1 `VALUE` + 1 `DESCRIPTION` | spedizione al cantiere Megaparsec Inc. |
| `Megaparsec Shipment [1]` | 1 `VALUE` + 1 `DESCRIPTION` | **la stessa scheda e lo stesso nome** |
| `Megaparsec Shipment [2]` | 1 `VALUE` + 1 `DESCRIPTION` | **la stessa scheda e lo stesso nome** |
| `Syndicate Hovercraft Racer Transport` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | un pilota e il suo hovercraft a una gara |
| `Syndicate Hovercraft Large Racer Transport` | 1 `VALUE` + 1 `DESCRIPTION` + 1 `DIALOG` | una squadra di `<passengers>` membri con il carico |

## 2. Misure

```
unità             12            (5 VALUE + 5 DESCRIPTION + 2 DIALOG)
parole            139 EN -> 150 IT       rapporto 0,88 - 1,28 (media 1,08)
contesti          5
tab               0             asserzione negativa scritta
virgolette        0             asserzione negativa scritta
apici             0             asserzione negativa scritta (in entrambe le lingue)
segnaposto        24 in 6 famiglie, multiset E ordine per unità
gruppi identici   2             con tre copie ciascuno
```

## 3. Le tre cose che il lotto ha di proprio

1. **Invariante di FILE, non di segmento.** Cinque lotti coprono 94 righe distinte su 94 (`16 + 20 + 19 + 27 + 12`), e il
   `verify.py` confronta **quelle righe con quelle del database**: un buco interno, non solo una coda mancante, diventa
   rosso. L'ultima riga è la **814** e dopo non c'è nulla.
2. **Zero tab, zero virgolette, zero apici in entrambe le lingue**: tre asserzioni negative scritte. In un lotto così corto
   il rischio non è dimenticare un segno, è aggiungerne uno.
3. **Due gruppi con tre copie**: `Shipment to <planet>` e la scheda Megaparsec compaiono tre volte, una resa per gruppo. Le
   copie sono verificate con la **molteplicità** (`max(mult.values()) == 3`), non solo con l'unicità della resa.

## 4. Difetti trovati

Un rosso, **nell'asserzione**: dichiaravo `hovercraft` quattro volte; misurate **tre** («il suo hovercraft» ×2 e «i suoi
hovercraft» ×1). Corretto il numero e aggiunta l'asserzione della forma plurale, che è quella che conta (l'inglese dice
`their hovercraft` per una squadra: in italiano il possessivo cambia, il nome no).

## 5. Copertura del file

```
L247   16 unità   righe  19 - 153
L248   20 unità   righe 157 - 275
L249   19 unità   righe 291 - 431
L250   27 unità   righe 435 - 678
L251   12 unità   righe 701 - 814
----------------------------------
94 unità = 94 righe distinte · COMPLETO
```

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 94 unità del file sono `PENDING` come tutte le altre.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **«Completo» significa completo in staging**, non nel gioco.
