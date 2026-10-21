# REPORT — L311 (`data/bunrodea/bunrodea outfits.txt`, righe 25–130)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **18 controlli**. Il file è a **12/33**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (`DESCRIPTION`) | 12 |
| parole | 480 | **449** (0,935) |
| tab | **4** | **4** |
| virgolette | 0 | 0 |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 1 | 9 |

Rapporto per unità **0,90 – 1,15**: il lotto è **molto regolare** — sono schede tecniche di equipaggiamento, parallele fra loro.

## 2. Invariante di segmento (il file non è finito)

```
PRIMA     zero unità prima della 25
QUI       12 unità, righe distinte 25–130
DOPO      21 unità / 772 parole (la prossima alla 135)
COPERTURA 12/33 (36,4%) — STAMPATA, non asserita
```

Il `verify.py` asserisce solo **fatti locali** al segmento e un **limite monotòno** (`21 unità dopo`, `min = 135`): non pretende
mai la copertura globale del file.

## 3. Il lotto è una griglia

Quattro coppie di equipaggiamenti + quattro schede singole, e le due schede singole di ogni coppia di concetti sono **parallele**:

| concetto | «potenzia» | «limita» |
|---|---|---|
| **relay di scudi** | `Shield Relay Booster`: **più scudi**, meno efficienza | `Shield Relay Limiter`: **più efficienza**, meno scudi |
| **fabbricatore di naniti** | `Nanite Enhancer`: **più riparazione**, meno efficienza | `Nanite Limiter`: **più efficienza energetica e termica**, meno riparazione |

La **simmetria** è la cosa da conservare: chi legge le quattro schede deve vedere **lo stesso scambio** applicato a due sistemi
diversi.

## 4. La famiglia della nota degli upgrade

| unità | inglese | italiano |
|---|---|---|
| 54, 70 | **identiche**: `...for these upgrades, though.` | **identiche**: «…per questi potenziamenti, però.» |
| 114 | `...for these upgrades, though.` | «…per questi potenziamenti, però.» |
| 130 | `...for these upgrades, however.` | «…per questi potenziamenti, tuttavia.» |

Tre controlli distinti: `54 == 70`, `114 != 130`, e **la differenza è solo l'ultima parola** — con il confronto
`rsplit(' ', 1)[0]` che deve combaciare. La variazione del sorgente si conserva **nello stesso punto in cui sta**.

## 5. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  18 controlli · FAIL: 0 · exit 0
copertura  12/33 (36,4%) — stampata, non asserita
```

**Due rossi al primo giro**, entrambi **miei**:
1. il controllo «le identiche restano identiche» concatenava nella stessa catena di uguaglianza **italiano e inglese** (`it54 ==
   it70 == en54 == en70`): ovviamente falso. Corretto in **due** confronti separati;
2. apici italiani dichiarati **8**, misurati **9**.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; il lotto è **in staging**.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file non è finito**: 12/33; restano **21 unità / 772 parole**, di cui **445** nel prossimo lotto (L312).
