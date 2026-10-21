# REPORT — L266 (`data/kahet/aberrant ships.txt`, righe 686–1007) — LOTTO TERMINALE

**Esito: lotto CHIUSO, file COMPLETO.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **21 controlli**
(invariante di **file**: 65/65). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

**`data/kahet/aberrant ships.txt` è il sedicesimo file chiuso: 65/65 unità.**

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 22 (13 `VALUE`, 9 `DESCRIPTION`) | 22 |
| parole | 217 | **210** (0,97) |
| virgolette | 18 | 18 |
| tab / apici | 0 / 0 | 0 / **6** |
| segnaposto | 0 | 0 |

Rapporto per unità **0,97 – 1,33**.

## 2. Cinque navi

```
Aberrant Pike      686- 690   (solo la DESCRIPTION di chiusura: le altre due unità sono in L265)
Aberrant Mole      695- 767
Aberrant Whiskers  772- 837
Aberrant Trip      842- 919
Aberrant Triplet   924-1007
```

`Aberrant Pike` è **a cavallo dei due lotti**: la sua scheda di variante (riga 686) è la prima unità di L266, mentre le altre
sue due unità sono in L265. Non è una sovrapposizione — le righe sono distinte — ma è un **confine di nave**, non di
missione, e il `verify.py` lo verifica (`select ... line<686` → contesto `ship:Aberrant Pike`).

## 3. La formula ripresa da L265

La nota organo-metallica compare **4 volte** (unità 5, 10, 15, 20) e la resa è **identica a quella di L265**, verificata
rileggendo `L265/translation.json` e confrontando l'insieme delle rese con la stringa inglese corrispondente. Senza quel
controllo, due varianti della stessa frase sarebbero passate: i conteggi di parole e virgolette sarebbero rimasti identici.

## 4. La scheda anomala (Trip)

> `Something appears to have gone terribly wrong in the germination of this variant. It is a lopsided, deformed mass of
> malformed material, which survives only through sheer luck.`
> «Qualcosa sembra essere andato terribilmente storto nella germinazione di questa variante. È una massa sbilenca e deforme
> di materiale malformato, che sopravvive solo grazie alla pura fortuna.»

È l'unica scheda del file che **non** descrive una variante riuscita: descrive un **errore di crescita**. Il `check.py`
verifica le quattro parole che portano quel senso, perché una resa «neutra» («questa variante ha una forma irregolare»)
avrebbe rispettato i conteggi e perso il testo.

## 5. Lessico

| inglese | resa |
|---|---|
| `grown into a sleek, elongated shape` | **cresciuta fino a diventare una forma snella e allungata** |
| `sharp, bladed prow … more forward weapons` | **prua affilata a lama … più armi frontali** |
| `tail-like structure, increasing its agility` | **struttura a coda, che ne aumenta l'agilità** |
| `germination` | **germinazione** |
| `lopsided, deformed mass of malformed material` | **massa sbilenca e deforme di materiale malformato** |
| `survives only through sheer luck` | **sopravvive solo grazie alla pura fortuna** |
| `a composite of two or three individuals, fused together into a single mass` | **un composto di due o tre individui, fusi insieme in un'unica massa** |

## 6. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
FILE       65/65 unità · 2 lotti (43 + 22) · 65 righe distinte · ultima riga 1007 · 0 dopo
```

Nessun rosso: entrambi gli script verdi al **primo** giro.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 22 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **«Completo» significa completo in staging**: 65 unità tradotte, 0 caricate.
