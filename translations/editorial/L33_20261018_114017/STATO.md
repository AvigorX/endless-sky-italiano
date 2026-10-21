# L33 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L33_20261018_114017` · `data/wanderer/wanderers middle.txt` · righe 22–3601 · **731/731 unità**.
Tredicesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 731 unità, 75 contesti, kind 494 `MISSION_TEXT` / 68 `DESCRIPTION` / 61 `VALUE` /
  56 `DIALOG` / 41 `LOGBOOK` / 11 `UI_LABEL`, **0 `CONVERSATION`**.
- `check.py` derivato da L32 con `NT = set(range(580, 591))`: le 11 `UI_LABEL` di salto
  `skip unmark <stella>` (alnitak, betelgeuse, canopus, capella, castor, kursa, mebsuta, miaplacidus,
  rigel, saiph, wazn). `TOKEN_EXC` vuoto, 7 famiglie di token di dati (`<planet>`, `<capacity>`,
  `<destination>`, `<last>`, `<origin>`, `<first>`, `<system>`).
- **Controllo delle parentesi quadre**: 113 unità con `[a, b]`; il checker verifica che numero di gruppi
  e numero di alternative per gruppo siano identici al sorgente.
- 11 parti scritte a mano, tutte a fine missione: 1–43, 44–87, 88–149, 150–219, 220–292, 293–364,
  365–443, 444–515, 516–596, 597–678, 679–731
  (43, 44, 62, 70, 73, 72, 79, 72, 81, 82, 53). Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 731 unità, 22.378 EN → 21.188 IT (0,947), rapporto per unità 0,72–1,44,
  sha256[:16] `1bc292eafe08f311`.
- `verify.py`: **27 controlli**, `FAIL: 0`, exit 0. Copertura **731/731** asserita: il lotto è l'unico
  del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Voce dei Wanderers tenuta da L32, non reinvenata**: il lotto è la continuazione diretta di
  `wanderers start.txt`, quindi la voce concordata in L32 (frase piana, cortesia formale, nessun ordine
  marcato) resta valida e non viene rinegoziata qui. Il dispositivo di traduzione continua a parlare in
  modo diverso: la scelta è in `review.md` §4.
- **La sintassi delle parentesi quadre è un dato, non stile**: 113 unità con `[parola, parola]`, e ogni
  alternativa deve reggere la frase da sola. Tre unità sono state riscritte perché la resa letterale
  produceva una frase che non stava in piedi (324, 685, 286).
- **Si riproduce il sorgente**: tab 408/408, virgolette 1.002/1.002, token 166/166.
- **Nessun controllo allentato**: le unità 33/38/194/390 hanno lo stesso inglese e possono avere lo
  stesso italiano; 411/721 e 593 hanno inglesi diversi e sono state differenziate. 331 riscritta per il
  rapporto minimo. 391 riscritta per il rapporto minimo. 485 corretta per un errore di articolo.
- **Numeri dai file, non dalla memoria**: kind, 22 controlli di `check.py`, 27 di `verify.py` e tutti i
  totali vengono da misure.
- **Nessuna scrittura sul database**: `state.db` in sola lettura, 731 unità `PENDING`.

## Glossario del lotto

| inglese | italiano | nota |
|---|---|---|
| Eye | Occhio | invariato da L32 |
| Molt | Muta | invariato da L32 |
| Unfettered (Hai) | Slegati | invariato da L32 |
| Archon(s) | Archon | invariato da L32 |
| Keeper / Custodian | Custode | solo dove il testo lo conferma |
| world-ship | nave-mondo | descrittivo |
| terraforming | terraformaggio | invariato da L32 |
| greenhouse | serre | struttura, non pianta |
| gestalt consciousness | coscienza gestaltica | termine tecnico dei Wanderers |
| artificial mind | mente artificiale | con la maiuscola quando è nome proprio ("la Mente") |
| self-replicating war machines | macchine da guerra autoriproducenti | descrizione dei droni Mereti |
| control center | centro di controllo | struttura Sestor |
| Oathkeepers | Oathkeepers | nome proprio, invariato |
| Alphas | Alphas | nome proprio, invariato |
| Zenith, Farpoint, Saiph, Alnilam, Mesuket, Sestor Ikfar | invariati | nomi propri |
| Heart of Gold | Heart of Gold | nome proprio di una singola nave, invariato |

## Verifica

```
check.py   → FAIL totale: 0     (22 controlli, copertura 731/731)
verify.py  → FAIL: 0, exit 0    (27 controlli)
```

Comandi:

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/L33_20261018_114017/check.py     # atteso: FAIL totale: 0
python staging/editorial/L33_20261018_114017/verify.py    # atteso: exit 0, FAIL: 0
```

## Residuo

Lo staging contiene ora **16.499 unità** su 13 file completi; il residuo misurato è **15.431 unità**
(la formula di `state.py` sottrae due volte le `UI_LABEL` già in staging: vedi la decisione 99 nel
checkpoint editoriale). Prossimo lotto: `data/human/free worlds 0 prologue.txt`, righe 16–2502,
703 unità, 18.612 parole, 43 contesti — **file intero in un solo lotto**.
