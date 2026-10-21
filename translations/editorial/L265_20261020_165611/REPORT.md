# REPORT — L265 (`data/kahet/aberrant ships.txt`, righe 16–685)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 43 (26 `VALUE`, 17 `DESCRIPTION`) | 43 |
| parole | 429 | **418** (0,97) |
| virgolette | **32** | **32**, per unità identiche |
| tab / apici | 0 / 0 | 0 / **10** |
| segnaposto | 0 | 0 |

Rapporto per unità **1,00 – 1,32** (le `VALUE` copiate sono a 1,00 per definizione; le schede stanno fra 1,07 e 1,32).

## 2. Nove navi, nove contesti

```
Aberrant Latte        16- 82      Aberrant Chomper      87-160
Aberrant Pileup      165-232      Aberrant Hugger      237-306
Aberrant Longfellow  311-386      Aberrant Dancer      391-464
Aberrant Junior      469-539      Aberrant Icebreaker  544-615
Aberrant Pike        620-685
```

Ogni blocco ha la stessa forma: **due `VALUE`** in testa (designazione con virgolette, plurale), **due `DESCRIPTION`**
(nota organo-metallica + frase sulla variante), **un `VALUE`** in coda (designazione ripetuta). Il `check.py` verifica le
**righe di apertura e chiusura** di ogni blocco: un blocco spostato di una riga cambierebbe la mappa dei contesti.

## 3. Le 17 schede sono 9 stringhe

La nota organo-metallica compare **9 volte identica** e ha **una sola resa** (verificata come insieme con un solo
elemento). Le altre **8** sono frasi distinte sulla variante, ognuna con la sua resa: il test verifica che l'insieme abbia
**8 elementi**, così due varianti appiattite su una sola resa diventano rosse.

## 4. Le virgolette, e l'irregolarità da conservare

| tipo | unità | virgolette |
|---|---|---|
| designazione con virgolette (`K-IA "Latte"`) | 16 | 32 |
| plurale (`Lattes`, `Chompers`, …) | 9 | 0 |
| **sigla nuda** (`K-IC Pileup`) | **1** | **0** |

La sigla nuda è un'**irregolarità del sorgente**: tutte le altre designazioni hanno le virgolette. La resa la conserva, e il
controllo asserisce che gli unici `VALUE` senza virgolette siano **i nove plurali e la riga 15** — non «almeno uno».

## 5. Lessico

| inglese | resa |
|---|---|
| `organo-metallic entity` | **entità organo-metallica** |
| `strange mosaic of organic tissue, conventional material, and an exotic matter` | **strano mosaico di tessuto organico, materiale convenzionale e una materia esotica** |
| `defies conventional analysis` | **sfugge all'analisi convenzionale** |
| `variant` | **variante** |
| `baseline` | **modello di base** |
| `fuselage` | **fusoliera** |
| `hardpoints designed to mount turrets` | **punti di attacco progettati per montare torrette** |
| `hull` | **scafo** |
| `armament` | **armamento** |
| `Aberrant` | **invariato** (classe di navi; come `Ka'het` nel corpus) |

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 43 qui · 22 dopo la 685 · copertura 43/65 (66,2%)
```

Un rosso al primo giro, sul controllo delle virgolette: asserivo che l'unico `VALUE` **senza** virgolette fosse la riga 15,
ma i **nove plurali** (`Lattes`, `Chompers`…) non ne hanno per costruzione. Corretto in «i nove plurali **più** la riga 15»,
con la lista esplicita e il vincolo che, fra quelli, **solo la 15** cominci con `K-`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 43 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 43/65; restano 22 unità (Pike, Mole, Whiskers, Trip, Triplet).
