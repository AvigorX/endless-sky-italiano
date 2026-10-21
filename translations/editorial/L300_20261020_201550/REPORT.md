# REPORT — L300 (`data/coalition/coalition outfits.txt`, righe 516–533) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 49/49.** `check.py` esce 0 con **21 controlli**; `verify.py` esce 0 con **21 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 5 (tutte `DESCRIPTION`) | 5 |
| parole | 209 | **195** (0,93) |
| tab | **2** | **2** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 2 | 5 |
| contesti | **3** (2 doppi + 1 singola) | invariati |

Rapporto per unità **0,93 – 1,28**.

## 2. Invariante di FILE

```
FILE         49/49 (100%) · 49 righe distinte · prima 26 · ultima 533 · zero dopo
SOMMA LOTTI  15 (L297) + 15 (L298) + 14 (L299) + 5 (L300) = 49
OVERLAP      nessun altro lotto rivendica le righe 516-533
```

Il file `data/coalition/coalition outfits.txt` è il **ventiseiesimo** chiuso nel progetto (**85** su 167).

## 3. Che cosa chiude il file

Le ultime cinque schede sono **tre oggetti che non sono tecnologia da combattimento**:

| riga | oggetto | idea |
|---|---|---|
| 516/517 | **licenza civile** | un chip-distintivo che autorizza a **commerciare** tecnologia civile; la 517 racconta **secoli di polemiche legislative** Heliarch |
| 524 | **licenza Heliarch** | una **fascia d'oro e platino**, simbolo di rango e chiave d'accesso; «fatta su misura per la testa di un umano» |
| 532/533 | **un libro** | `Beyond the Hyperdrive`, regalato da **Anna Fangvin**; la storia dentro parla di un capitano che **ruba un motore di salto ai Quarg** |

È un finale **coerente** con il file: la Coalizione è una civiltà di **commercianti, burocrati e lettori**, non di guerrieri.

## 4. Gli atti di legge: tradotti, non traslitterati

La riga 517 è il **passo più difficile del lotto**: una catena di **tre atti** con numeri, articoli e addenda. La resa è
**descrittiva in italiano**:

> «La discussione è cominciata con la **terza Legge sui Beni e sulle Tariffe Civili**, emanata appena qualche decennio dopo la
> **Guerra d'Indipendenza**. È proseguita fino al relativamente recente **ventiseiesimo addendum al secondo articolo della Nona
> Rettifica su Commercio e Traffico**, approvato duecento anni fa…»

Il test **rifiuta** che `Rectification` o `Civil Goods` sopravvivano in inglese: sono atti normativi, non nomi di prodotto. Restano
in inglese, invece, **`Beyond the Hyperdrive`** (titolo di un libro) e **`Anna Fangvin`** (persona).

## 5. La seconda persona è un dono, non un'istruzione

La 532 dice «A book **gifted to you**». In L299 la seconda persona era un'**istruzione di montaggio**; qui è il **narratore** che
si rivolge al giocatore. Il test elenca `[4]` **e** il documento dichiara il tipo: due casi diversi, due trattamenti diversi,
entrambi verificati.

## 6. Verifica

```
check.py   21 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
FILE       49/49 (100%) · ventiseiesimo file completo
```

**Un rosso al primo giro** (controllo mio): un'asserzione sul titolo del libro era scritta in modo **contorto** e non verificava
nulla di utile; sostituita con «il titolo **non** compare in prosa e il nome dell'autrice **sì**».

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 5 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è completo al 100%** solo in staging.
