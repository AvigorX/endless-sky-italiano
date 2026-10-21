# REPORT — L287 (`data/gegno/gegno ships.txt`, righe 303–658)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 9 (tutte `DESCRIPTION`) | 9 |
| parole | 466 | **446** (0,96) |
| tab | 4 | 4 (unità 1, 4, 6, 9) |
| virgolette | 0 | **0** |
| segnaposto / alternative | 0 / 0 | **0 / 0** |
| apici | 4 | 10 |

Rapporto per unità **0,85 – 1,06**.

## 2. Tre descrizioni spezzate

Il contratto le aveva individuate: `Dunite` 417–418, `Augen` 553–554, `Schist` 657–658. In ognuna la **seconda unità
continua** e non ricomincia, con tre strategie diverse — e ognuna è quella che il testo inglese impone:

| coppia | inglese | resa | perché |
|---|---|---|---|
| `Dunite` | `Being a mangled mess of machinery…` | «**Essendo** un ammasso di macchinari…» | gerundio causale, soggetto implicito |
| `Augen` | `This project was meant to result in two sister-ship behemoths…` | «**Il progetto** doveva produrre due colossi gemelli…» | il soggetto **cambia**: è il progetto, non la nave |
| `Schist` | `Although is it lightly armed…` | «**Benché** siano armati in modo leggero…» | concessiva; l'inglese ha **l'inversione sbagliata** |

L'ultimo caso contiene un **secondo refuso del sorgente**: `Although is it lightly armed` (inversione di `is` e `it`). In
italiano la frase si rende correttamente; il refuso non si riproduce, e il `REPORT` lo dichiara come già fatto per `Gypusm's`.

## 3. La continuità cross-lot

L'unità 1 (riga 303) **continua** la scheda del `Corundum` aperta in L286 (riga 302). Il `verify.py` **riapre il
`translation.json` di L286**, prende quella unità e verifica due cose:

1. che la resa di L286 finisca con **«avanzati.»** (fine di frase, non troncata);
2. che questa unità cominci con **«Pur non potendo»**, cioè con una subordinata e **non** con «Il Corundum».

È il primo controllo di continuità **tra due lotti** costruito leggendo il lotto precedente dal disco.

## 4. Terminologia

| inglese | resa |
|---|---|
| `relic from another age` | **relitti di un'altra epoca** |
| `the Gegno home system of Heutesl` | **il sistema natale dei Gegno, Heutesl** |
| `canyon shipyard` | **cantiere del canyon** |
| `sister-ship behemoths` | **colossi gemelli** |
| `a hodgepodge of parts` | **un guazzabuglio di parti** |
| `without any regard to structural integrity` | **senza alcun riguardo per l'integrità strutturale** |
| `for jousting and ramming other duelists` | **per giostrare e speronare gli altri duellanti** |
| `angled guns` | **cannoni angolati** |
| `to flank the vessel` | **aggirare il vascello** |
| `the front lines` | **il fronte** |

## 5. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   7 prima · 9 qui · 21 dopo la 658 · 6 contesti · 3 coppie consecutive
```

**Un rosso al primo giro**, su un controllo mio: verificavo `"l'Augen-Class" in …` con la **minuscola**, mentre la frase
comincia con la maiuscola (`L'Augen-Class`). Corretto in `startswith("L'Augen-Class")` più il conteggio di `Augen-Class` e il
divieto di «La Augen».

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 9 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 16/37; restano **21 unità** (20 `DESCRIPTION` + **1 `VALUE`**).
