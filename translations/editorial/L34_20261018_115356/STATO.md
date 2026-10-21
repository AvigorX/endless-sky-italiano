# L34 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L34_20261018_115356` · `data/human/free worlds 0 prologue.txt` · righe 16–2502 · **703/703 unità**.
Quattordicesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 703 unità, 43 contesti, kind 520 `MISSION_TEXT` / 59 `LOGBOOK` / 44 `DIALOG` /
  40 `VALUE` / 40 `DESCRIPTION`, **0 `UI_LABEL`**, **0 `CONVERSATION`**.
- `check.py` derivato da L33 con **`NT` vuoto**: questo file non ha unità non traducibili misurate
  (0 `UI_LABEL`, 0 `CONVERSATION`, nessun riferimento di dato, nessuna `label` di salto).
  `TOKEN_EXC` vuoto, 13 famiglie di token di dati.
- **Il controllo delle parentesi quadre è stato rimosso**, non nascosto: le unità con `[a, b]` in questo
  file sono **0** (misurato). Un confronto fra due liste vuote passa sempre e darebbe l'illusione di una
  verifica che non esiste; il `verify.py` invece **asserisce** che le unità con parentesi quadre siano 0,
  così se il file cambiasse il lotto fallirebbe invece di passare in silenzio.
- 11 parti scritte a mano, tutte a fine missione: 1–75, 76–133, 134–190, 191–243, 244–309, 310–386,
  387–438, 439–491, 492–551, 552–628, 629–703
  (75, 58, 57, 53, 66, 77, 52, 53, 60, 77, 75). Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 703 unità, 18.612 EN → 17.855 IT (0,959), rapporto per unità 0,71–1,69,
  sha256[:16] `50fbd52f12326484`.
- `verify.py`: **27 controlli**, `FAIL: 0`, exit 0. Copertura **703/703** asserita: il lotto è l'unico
  del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce nuova, ricavata dal testo**: questo file apre l'arco delle Free Worlds, quindi non si porta
  dietro né la voce dei Wanderers (L32–L33) né quella della Coalizione (L24–L26). Le cinque voci del
  lotto sono in `review.md` §4.
- **Il registro religioso non si appiattisce**: Freya Winters dice «I pray» come formula di cortesia
  devota, JJ dice «I pray» e «God willing» in senso pieno, i monaci pregano davvero. In italiano:
  «Confido» per Freya, «Prego» per JJ, litania per i monaci (`review.md` §6).
- **Si riproduce il sorgente**: tab 483/483 (468 unità con tab iniziale), virgolette 1.274/1.274,
  token 191/191. **Dodici unità** hanno un numero dispari di virgolette (battute che il sorgente apre e
  non chiude sulla stessa riga): sono state riprodotte, e il `verify.py` confronta l'insieme degli idx.
- **Nessun controllo allentato**: 118 e 394 avevano lo stesso italiano con inglesi diversi e sono state
  differenziate («Certo, lo farò volentieri.» / «Certo, con piacere.»); 243, 391, 543 e 585 riscritte per
  il rapporto minimo.
- **Numeri dai file, non dalla memoria**: kind, 21 controlli di `check.py`, 27 di `verify.py` e tutti i
  totali vengono da misure.
- **Nessuna scrittura sul database**: `state.db` in sola lettura, 703 unità `PENDING`.

## Glossario del lotto

| inglese | italiano | nota |
|---|---|---|
| Southern Mutual Defense Pact | Patto di Difesa Reciproca del Sud | nome dell'organizzazione prima delle Free Worlds |
| Free Worlds | Free Worlds | nome proprio, invariato |
| Free Worlds Council | Consiglio delle Free Worlds | |
| Dirt Belt | Fascia di Terra | regione |
| Paradise Planets / Paradise World | Mondi Paradisiaci / Mondo Paradisiaco | |
| Rim | Bordo | regione |
| Core | Nucleo | regione |
| Thousand Eyes | Mille Occhi | programma di sorveglianza |
| Cruiser / Carrier / Falcon / Osprey | invariati | modelli di nave |
| Mr. Eyes | Mr. Eyes | soprannome, invariato (vedi `review.md` §6) |
| Brother (Greg, David) | fratello (Greg, David) | titolo monastico |
| the Brothers | i Fratelli | comunità monastica |
| terraforming | terraformaggio | invariato dai lotti precedenti |
| salvage | recupero | termine legale della Legge 2976 |
| janitor | inserviente | |
| Dereliction and Salvage Act of 2976 | Legge sull'abbandono e il recupero del 2976 | |

## Verifica

```
check.py   → FAIL totale: 0     (21 controlli, copertura 703/703)
verify.py  → FAIL: 0, exit 0    (27 controlli)
```

Comandi:

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/L34_20261018_115356/check.py     # atteso: FAIL totale: 0
python staging/editorial/L34_20261018_115356/verify.py    # atteso: exit 0, FAIL: 0
```

## Residuo

Lo staging contiene ora **17.202 unità** su 14 file completi; il residuo misurato è **14.728 unità**
secondo la formula di `state.py` (che sottrae due volte le `UI_LABEL` già in staging: decisione 99).
Prossimo lotto: `data/human/free worlds 1 start.txt`, righe 16–2343, 663 unità, 21.140 parole,
37 contesti, **fine file** — la continuazione diretta di questo arco narrativo.
