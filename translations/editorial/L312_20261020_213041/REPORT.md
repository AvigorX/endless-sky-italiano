# REPORT — L312 (`data/bunrodea/bunrodea outfits.txt`, righe 135–236)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **23 controlli**. Il file è a **24/33
(72,7%)**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (1 `VALUE` + 11 `DESCRIPTION`) | 12 |
| parole | 445 | **433** (0,973) |
| tab | **4** | **4** |
| virgolette | **2** (una coppia) | **2** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 1 | 12 |

Rapporto per unità **0,98 – 1,20**: lotto regolare anche quando entra la **divulgazione scientifica** (le tre schede dei
reattori).

## 2. Invariante di segmento

```
PRIMA     12 unità (L311, righe 25–130)
QUI       12 unità, righe 135–236
DOPO      9 unità / 327 parole (la prossima alla 250)
COPERTURA 24/33 (72,7%) — STAMPATA, non asserita
```

Il `verify.py` asserisce **due limiti monotoni** (12 prima, 9 dopo, minima dopo = 250) e **nessuna copertura globale**.

## 3. Il lotto è fisica in tre passi

| passo | contenuto |
|---|---|
| **energia solare** | le batterie servono a **installare** le celle (ma funzionano anche senza); le celle sono **efficienti** ma producono **calore di scarto** che cresce con l'energia — pericoloso **vicino alle stelle luminose** |
| **il controllo del reattore** | `overclocker` → più energia, meno efficienza termica; `limiter` → il contrario. Lo **stesso scambio** di L311, applicato all'energia invece che agli scudi |
| **i nomi dei reattori** | `quark`, `electroweak`, `dark`: tre **stelle esotiche**, di cui una **scoperta** (Polaris, XXVIII secolo) e due **teoriche** |

Il filo è **coerente**: i Bunrodea nominano i reattori come l'umanità nomina le stelle che **non ha ancora visto**.

## 4. La famiglia delle note: qui è tutta identica

| unità | inglese | italiano |
|---|---|---|
| 204, 220, 236 | `...for these upgrades, though.` | «…per questi potenziamenti, però.» |

**Opposto di L311**, dove 114 diceva `though.` e 130 `however.`: là il test doveva **preservare una differenza**, qui deve
**preservare l'identità**. Le due situazioni hanno controlli diversi apposta.

## 5. Le due schede dei componenti sono speculari

```
prima frase    IDENTICA a meno del nome    («…è un componente che si può installare in un reattore Bunrodea per modificarne l'efficacia.»)
seconda frase  OPPOSTA                     (energia ↑ / termica ↓  contro  termica ↑ / energia ↓)
```

Il controllo confronta la **prima frase** e pretende la **differenza** della seconda: se qualcuno avesse "normalizzato" le due
schede rendendole uguali, il test lo vedrebbe.

## 6. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
copertura  24/33 (72,7%) — stampata, non asserita
```

**Un rosso al primo giro**, mio: il controllo «le due schede sono parallele» confrontava l'**intera** coda dopo il nome, che
include la **seconda frase** — che è **opposta per disegno**. Corretto confrontando **solo la prima frase** e aggiungendo
l'asserzione che le code **differiscono**.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; il lotto è **in staging**.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **La fisica è quella del SORGENTE**: la resa non corregge né verifica le affermazioni su stelle di quark, stelle elettrodeboli e
  stelle oscure.
- **Il file non è finito**: 24/33; restano **9 unità / 327 parole**.
