# REPORT — L275 (`data/korath/korath ships.txt`, righe 606–1311)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 14 (9 `DESCRIPTION` + 5 `VALUE`) | 14 |
| parole | 495 | **545** (1,10) |
| tab | 2 | 2 · primo carattere |
| virgolette | 2 | 2, dritte |
| apici | 9 | 16 |
| segnaposto | 0 | 0 |

Rapporto per unità (solo `DESCRIPTION`) **1,06 – 1,17**.

## 2. Il lotto

| contesto | `VALUE` | scheda |
|---|---|---|
| `Lor'kas Ik 577` | **Karek A'awoj** | trasporto materiali fra raffinazione e fabbriche |
| `Ra'gru Ik 618` | **Sapira A'awoj** | razzie pesanti, difesa di altri vascelli |
| `Kas'lor Ik 582` | **Dathnak A'awoj** | raccolta, raffinazione e trasporto di **carburante per l'iperspazio** |
| `Lor'nag Ik 590` | **Spera A'awoj** | passeggeri e **gruppi d'abbordaggio** |
| `Ra'at Ik 621` | **Ikfar A'awoj** | **portatrici**: caccia e mezzi minerari |
| `Kasichara A'awoj` | — | l'abitazione di lusso diventata nave-mondo |
| `Korsmanath A'awoj` | — | le città volanti e la loro politica |

## 3. La formula ripetuta

Le cinque schede da produzione cominciano **tutte** con la stessa frase:

> «Le più grandi navi da produzione Korath derivano da un telaio comune e antico.»

Il `check.py` confronta la **prima frase delle cinque** e verifica che l'insieme abbia un solo elemento. È la stessa tecnica
usata per la nota del plasma nei motori e per la scheda ionica: se una copia diventa «un po' diversa», i conteggi di parole
restano simili e nessun altro controllo se ne accorge.

## 4. Le virgolette di `"navi-mondo"`

Unità 11: le due virgolette sono **nel sorgente** e sono **dritte**. La resa le conserva — e con esse l'effetto: il testo
mette il termine **fra virgolette** perché è un nome che i Korath hanno dato **dopo**, per nostalgia, a navi nate per altro
scopo.

## 5. Terminologia

| inglese | resa | fonte |
|---|---|---|
| `chassis` | **telaio** | termine nuovo, dichiarato |
| `production vessels` | **navi da produzione** | termine nuovo |
| `jump drive` | **motore di salto** | 321 unità del corpus |
| `hyperdrive` | **iperguida** | 76 unità |
| `carriers` | **portatrici** | 48 unità |
| `boarding parties` | **gruppi d'abbordaggio** | 11 unità (`boarding party`) |
| `hangars` | **hangar** | 190 unità |
| `world-ships` | **navi-mondo** | da L273 |
| `city ships` | **navi-città** | termine nuovo |
| `navarchs` | **navarchi** | termine nuovo (greco ναύαρχος) |

## 6. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   17 prima · 14 qui · 19 dopo la 1311 · copertura 31/50 (62,0%)
```

Un rosso al primo giro, su un divieto scritto male: vietavo le parole `hangar` e `navarch`, ma **`hangar` e `navarchi` sono
parole italiane**. Il divieto ora riguarda solo i termini inglesi veri (`chassis`, `jump drive`, `world-ship`, `city ship`,
`production vessel`) e in più **pretende** le forme italiane corrette.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 31/50.
