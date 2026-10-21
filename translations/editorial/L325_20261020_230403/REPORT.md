# REPORT — L325 (`data/kahet/kahet outfits.txt`, righe 54–573) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 25/25.** `check.py` esce 0 con **27 controlli**; `verify.py` esce 0 con **20 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 25 (22 `DESCRIPTION` + 3 `VALUE`) | 25 |
| parole | 848 | **870** (**1,026**) |
| contesti | 20 | **20** |
| tab | **2** | **2** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **17** (15 unità) | 26 |

Il rapporto complessivo **supera 1** (1,026): è il primo lotto del ciclo in cui l'italiano è **più lungo** dell'inglese. La causa non è
il registro ma la **morfologia**: articoli e preposizioni articolate (`del`, `della`, `nei`, `alla`) che l'inglese non ha.

Estremi: **0,98** (riga 372, `Ka'het Primary Cooling`) e **1,27** (riga 285, la nota dei rifornimenti).

## 2. Invariante di FILE

```
FILE   25/25 (100%) · zero unità prima della 54 · zero dopo la 573
RIGHE  25 distinte · prima 54 · ultima 573 · un solo lotto
TIPI   22 DESCRIPTION + 3 VALUE
```

`data/kahet/kahet outfits.txt` è il **trentanovesimo** file chiuso (**98** su 167).

## 3. La genealogia: tre civiltà in un file

Il file descrive la tecnologia **Ka'het** come **stratificazione di tre popoli**:

| popolo | che cosa | dove |
|---|---|---|
| **Ka'mar** | i **droni** dei Costruttori: il `Reserve Accumulator` e il `Compact Engine` nascono per loro | 425, 561 |
| **Het** | le **navi** che riusano la tecnologia dei Costruttori: `MHD Generator` come fonte secondaria, scudi per necessità | 359, 386, 399, 414 |
| **Ka'het** | i **successori**: le gondole standardizzate, il `Nullifier` portato in battaglia dai `Vareti` | 54, 465, 489 |

La direzione è **una sola** e il testo la dichiara in modo obliquo: il `Compact Engine` è «molto prima che i Ka'het esistessero e che il
loro progetto di gondole fosse standardizzato». La resa conserva l'**ordine** (Ka'mar → Ka'het) e non lo inverte.

## 4. La nota dei rifornimenti: quinta occorrenza

```
L318  korath weapons.txt   473
L319  korath weapons.txt   659, 1051, 1222
L320  wanderer outfits.txt 271
L324  incipias outfits.txt 135
L325  kahet outfits.txt    285
```

Sette occorrenze, **quattro file**, **cinque lotti**. Resa unica: «Le munizioni per quest'arma possono essere rifornite presso
qualsiasi emporio.» — verificata **nel corpus intero**.

## 5. `nacelle` → «gondole», ma `Maeri Engine Nacelles` resta inglese

| contesto | tipo | resa |
|---|---|---|
| prosa («These nacelles used to comprise the entire engine block…») | `DESCRIPTION` | **«Queste gondole costituivano l'intero blocco motore…»** |
| nome dell'equipaggiamento (444, 468, 492) | `VALUE` | **`Maeri Engine Nacelles`** (copiato) |

Le due scelte convivono senza contraddirsi: il **nome proprio** di un oggetto non si traduce, il **lessico comune** sì. Il test lo rende
esplicito in **due** asserzioni distinte, e vieta che la resa dei `VALUE` contenga «gondol» o «motore».

Il termine «gondole» viene dal **corpus** (righe 809 e 815 dei lotti precedenti, `Maeri'het` e `Telis'het`): non l'ho scelto io.

## 6. Due errori di metodo, uno grave

| # | errore | correzione |
|---|---|---|
| 1 | `Ka'mar` atteso **4**, misurato **3** | valore corretto al misurato |
| 2 | seconda persona: confronto fra l'italiano (`tu/tua`) e l'**inglese** con la **stessa** regex | due regex distinte: `tua|tuo|…` per l'italiano, `your|you` per l'inglese |
| 3 | `\\b` dentro un heredoc → **byte `0x08` (backspace)** nel file | regex riscritta senza `\b`; **verifica dei byte** dopo ogni patch generata |

Il terzo **non è stato intercettato da `ast.parse`**: un carattere di controllo dentro una stringa è sintatticamente valido. La regex
diventata `r'<BS>(your|you)<BS>'` non corrispondeva a nulla e la seconda persona risultava **assente dall'inglese**, cioè il test
falliva su un fatto vero. Regola nuova: dopo una patch generata da uno script, si controlla **anche** `open(...,'rb').read().count(8)`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **`sustainer` → «motore di sostentamento»**: **nessuna occorrenza precedente** nel corpus. È una scelta **nuova**, non una coerenza
  verificata; se in futuro il corpus userà un'altra forma, questo lotto andrà riallineato.
- **`Vareti`, `Maeri`, `Telis`, `Ka'mar`, `Het`, `Ka'het`** restano invariati: sono nomi di popoli e di navi.
