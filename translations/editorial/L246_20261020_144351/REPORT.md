# REPORT — L246 (`data/hai/hai ships.txt`, righe 1517–1860) — LOTTO TERMINALE

**Esito: lotto CHIUSO, file COMPLETO.** `check.py` esce 0 con **33 controlli**; `verify.py` esce 0 con **27 controlli**
(invariante di **file**: 157/157). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

**`data/hai/hai ships.txt` è l'undicesimo file chiuso della campagna: 157/157 unità.**

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Emperor Beetle` | 1 `DESCRIPTION` (col tab) | la chiusura della scheda aperta in L245: la nave come strumento di terrore |
| `Solifuge` | 18 `TEXT` + 1 `DESCRIPTION` | il porta-caccia degli Slegati, nato dopo aver visto il `"Giftbringer"` degli Alphas |
| `Violin Spider` | 4 `TEXT` + 2 `DESCRIPTION` | il caccia Hai e la **nota sui caccia** col tab |
| `Water Bug` | 10 `TEXT` + 1 `DESCRIPTION` | il mercantile Hai più diffuso, cresciuto sulle aggressioni degli Slegati |

## 2. Misure

```
unità             37            (32 TEXT + 5 DESCRIPTION · NESSUN VALUE)
parole            327 EN -> 324 IT       rapporto 0,99 - 1,23 (media 1,02)
contesti          4             (1 + 19 + 6 + 11 = 37)
tab               2             unità 1 e 24, primo carattere in inglese e in italiano
virgolette        66            = 2 × 32 nomi + 2 intorno a "Giftbringer"
apici             2 EN / 5 IT   (possessivi contro elisioni)
segnaposto        0             asserzione negativa scritta
```

## 3. Le tre cose che il lotto ha di proprio

1. **Invariante di FILE, non di segmento.** Il lotto chiude il file, quindi il controllo non guarda «quante unità dopo»
   ma **l'intero**: `29 + 45 + 46 + 37 = 157`, **157 righe distinte**, **0 dopo la 1860**, e — in più — che queste 157
   righe siano **esattamente** quelle del database (`righe == {line dei units}`): un buco interno, non solo una coda
   mancante, diventa rosso.
2. **Le due note rientrate si copiano dal corpus, non si reinventano.** La stringa inglese della nota sui caccia compare in
   **8 lotti precedenti** con **due** rese (6 contro 2): il `check.py` confronta la mia con la **forma più frequente**,
   calcolata in quel momento leggendo i `translation.json`, non con una costante scritta a mano. È il controllo che ha
   fatto emergere il difetto descritto al §4.
3. **Due tab, due controlli distinti**: presenza come primo carattere (`tabs == [(1,1,1), (24,1,1)]`) e **contenuto**
   («capi militari» nell'unità 1, «baia di caccia» nella 24), così una traduzione che azzera il rientro o che svuota il
   paragrafo non passa.

## 4. Difetto trovato e corretto (retroattivo su L244)

La nota sui **droni** era stata resa in L244 con una frase **mia**:

> «I droni non escono equipaggiati con un iperpropulsore. Non puoi trasportare un drone se non hai nella tua flotta una
> nave con una baia per droni.» — **1 occorrenza**

mentre il corpus ne aveva già **7** con un'altra forma:

> «I droni **non sono dotati di iperguida**. Non puoi trasportare un drone **a meno che tu non abbia** nella tua flotta una
> nave con una baia per droni.»

In L244 nessun altro testo conteneva quella nota, quindi il `check.py` non poteva accorgersene: la divergenza è emersa
**qui**, dove la nota gemella sui caccia esiste in mezza dozzina di lotti. Applicata la regola della **forma dominante**:

| cosa | prima | dopo |
|---|---|---|
| unità 3 di L244 | frase mia | **frase del corpus** (7 occorrenze) |
| `L244/check.py`, `verify.py` | verdi | **verdi** (asseriscono «baia per droni», soddisfatta da entrambe) |
| parole IT di L244 | 496 | **498** |
| `sha256[:16]` di L244 | `f1ecbcda503f2d0d` | **`2121d513cf0c67e2`** |

Aggiornati `L244/STATO.md`, `L244/REPORT.md` (§5-bis con la tabella delle occorrenze), questo contratto e i checkpoint.

## 5. Controlli che hanno morso

Due rossi al primo giro, **entrambi nelle asserzioni**:

1. il controllo dei nomi propri pretendeva che **ogni** nome dell'elenco comparisse almeno una volta: ma la scheda della
   Solifuge nomina il `Giftbringer` e gli `Alphas`, **non** sé stessa, e quella della Violin Spider dice «the Hai
   fighter». Sostituito con un **dizionario atteso** che dichiara gli **zeri** (`Solifuge: 0`, `Violin Spider: 0`);
2. l'invariante di file confrontava `157` con `len(units)`, che è **37** (le unità del lotto, non del file). Riscritto
   contando le righe di **tutti** i `translation.json`.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 157 unità del file sono `PENDING` come tutte le altre.
- **Nessuna scheda vista nel gioco**: tab e virgolette sono verificati **sul carattere**.
- **Nessuna revisione umana**.
- **«Completo» significa completo in staging**, non nel gioco.
