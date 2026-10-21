# REPORT — L320 (`data/wanderer/wanderer outfits.txt`, righe 40–450)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **19 controlli**. Il file è a **18/31
(58,1%)**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 18 (`DESCRIPTION`) | 18 |
| parole | 478 | **471** (0,985) |
| tab | **1** | **1** |
| virgolette | **0** | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | **2** | 6 |

Rapporto per unità **0,91 – 1,27**. Il minimo è la riga 82 (0,909): l'inglese ha due frasi lunghe con participi
(`capable of carrying turret-mounted weapons`, `because of the sheer size`), che l'italiano comprime in «capaci di portare armi in
torretta» e «Data la dimensione stessa». Il massimo è la nota dei rifornimenti (1,274), come in L318 e L319: una frase **corta**
inglese che in italiano chiede articolo e verbo.

## 2. Invariante di segmento (il file non è finito)

```
PRIMA     zero unità prima della 40: il lotto APRE il file
QUI       18 unità, righe distinte 40–450
DOPO      13 unità / 514 parole (la prossima alla 463)
COPERTURA 18/31 (58,1%) — STAMPATA, non asserita
```

## 3. I Wanderer non amano le armi — ma le fanno bene

La prima scheda è **l'autoritratto del popolo**:

> «I Wanderer non dedicano molto tempo allo sviluppo della tecnologia delle armi, preferendo concentrare l'attenzione su imprese più
> costruttive. Le poche armi che hanno creato, però, sono efficienti e letali.»

Il «però» è **del sorgente** (`However`) e la resa lo tiene **in quella posizione**: senza, la frase diventerebbe una vanteria, con,
resta **una concessione**. E il resto del lotto lo conferma: ogni arma nasce da **un problema specifico** —

| arma | il problema | la soluzione |
|---|---|---|
| `Sunbeam Turret` | la transizione dalla pace alla guerra con gli **Hai Slegati** | navi con **armi in torretta** |
| `Moonbeam` | i `Sunbeam` **non passano** la corazza dei droni Korath | un raggio **contro la corazzatura** |
| `Anti-Missile` | i **pod inseguitori** degli Hai Slegati | abbattere **quasi qualsiasi missile con un colpo** |

## 4. Due economie: la biomassa e il nucleare

| riga | fonte | come |
|---|---|---|
| 346, 361 | **microrganismi** | sottoprodotti metabolici; coltura che produce **una piccola carica** |
| 376–421 | **nucleare** | quattro reattori, **quattro scale** |

I Wanderer usano **entrambe**, e il testo non dice quale sia migliore: sono **taglie** diverse per **navi** diverse. La resa non
ordina ciò che il testo non ordina.

## 5. Lo scambio replicato negli scudi

```
Bright Cloud  →  ricarica «a una velocità considerevole»  /  «consuma anche più energia»
Dark Storm    →  «più in fretta di qualsiasi tecnologia umana»  /  «assorbe anche molta più energia»
```

Il test verifica **entrambi** i costi. Un controllo sul solo guadagno avrebbe lasciato passare uno scudo **gratis**, che nel gioco
cambierebbe il bilanciamento.

## 6. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  19 controlli · FAIL: 0 · exit 0
copertura  18/31 (58,1%) — stampata, non asserita
```

**Nessun rosso**: primo giro verde. La nota dei rifornimenti è la **terza** occorrenza in tre lotti consecutivi (L318, L319, L320) e
la verifica a due meccanismi ha funzionato senza modifiche.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 18 unità `PENDING`; il lotto è **in staging**.
- **Nessun testo visto nel gioco**: le percentuali (`50%`) e le quantità (`40` munizioni) sono verificate **nei dati**.
- **`tracker pods` → «pod inseguitori»**: prima occorrenza nel corpus, scelta **dichiarata**.
- **Il file non è finito**: 18/31; restano **13 unità / 514 parole**.
