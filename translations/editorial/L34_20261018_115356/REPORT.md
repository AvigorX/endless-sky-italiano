# L34 — REPORT (chiuso 2026-10-18)

`data/human/free worlds 0 prologue.txt`, righe 16–2502 — **703/703 unità**, file completo.

## Numeri misurati

| voce | valore |
|---|---|
| unità | 703 / 703 |
| contesti | 43 |
| parole | 18.612 EN → 17.855 IT (0,959) |
| parti | 11 (75, 58, 57, 53, 66, 77, 52, 53, 60, 77, 75) |
| tab | 483 caratteri IT = 483 EN · 468 unità con tab iniziale |
| virgolette | 1.274 IT = 1.274 EN · 12 unità con conteggio dispari, riprodotte |
| token `<...>` | 191 IT = 191 EN |
| parentesi quadre | **0 unità** (controllo strutturale non applicabile, asserito) |
| rapporto per unità | 0,71 – 1,69 (gate 0,55–1,90) |
| `NT` | **vuoto** (0 `UI_LABEL`, 0 `CONVERSATION`, 0 riferimenti di dato) |
| `check.py` | `FAIL totale: 0` (21 controlli) |
| `verify.py` | 27 controlli, exit 0, `FAIL: 0` |
| sha256[:16] `translation.json` | `50fbd52f12326484` |
| sha256[:16] `source.json` | `e4d6df47c3e829e4` |
| sha256[:16] `check.py` | `ccc86ccb34831d8f` |
| sha256[:16] `verify.py` | `036ee7a0f8cc5095` |
| dimensione directory | 1,2 MB (11 parti) |

## Tipi presenti (misurati sul `source.json`)

```
MISSION_TEXT 520 · LOGBOOK 59 · DIALOG 44 · VALUE 40 · DESCRIPTION 40 · UI_LABEL 0 · CONVERSATION 0
```

Rispetto a L33 cambia tutto il profilo: non ci sono `UI_LABEL` da mettere in `NT`, ci sono 59 `LOGBOOK`
(uno per riga `log`) e 44 `DIALOG` con molte battute aperte. La lista `NT` di L33 (11 `skip unmark`) qui
sarebbe stata **dannosa**: avrebbe lasciato in inglese 11 unità di prosa e fatto fallire il controllo
«non traducibili lasciate identiche».

## Comandi di verifica

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n

# 1. coerenza interna del lotto (21 controlli + copertura)
python staging/editorial/L34_20261018_115356/check.py        # atteso: FAIL totale: 0

# 2. verifica indipendente, senza riusare la logica di check.py (27 controlli)
python staging/editorial/L34_20261018_115356/verify.py       # atteso: exit 0, FAIL: 0

# 3. preflight del workspace e integrità dei file protetti
python staging/editorial/tools/state.py                      # atteso: ESITO: OK
```

## Cosa è stato corretto in questo lotto

| unità | problema | correzione |
|---|---|---|
| 118 / 394 | stesso italiano per due inglesi diversi (`I'd be glad to do that` / `I would be glad to`) | «Certo, lo farò volentieri.» / «Certo, con piacere.» |
| 243 | rapporto 0,67 sotto la banda comoda | «Sì, questo risponde» |
| 543 | rapporto 0,65 | «Qualcos'altro?» |
| 585 | rapporto 0,56 | «Giusto, mi sembra ragionevole. Proviamo.» |
| 365 | refuso «della depistaggio» | «del depistaggio» |

## Limiti dichiarati

- **Non verificato nell'editor, non caricato nel gioco, non approvato nel database.** Il lotto è staging
  editoriale: `state.db` resta in sola lettura e le 703 unità sono `PENDING`.
- **La lacuna `log` non è riparabile da questo lotto.** Qui la forma è quella di L32/L33 (l'unità
  prodotta è il testo, categoria e nome si perdono) ed è documentata in `review.md` §7;
  `tools/l10n.py` e `state.db` sono protetti.
- **Residuo**: 14.728 unità secondo la formula di `state.py`; il valore misurato e la differenza sono nel
  checkpoint editoriale (decisione 99).
- **Lunghezza delle frasi**: il gate 0,55–1,90 non dice nulla sulla qualità della resa. Le decisioni
  editoriali che lo hanno reso possibile sono in `review.md`, non in questo rapporto.
