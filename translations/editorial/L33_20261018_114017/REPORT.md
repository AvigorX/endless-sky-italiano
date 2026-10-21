# L33 — REPORT (chiuso 2026-10-18)

`data/wanderer/wanderers middle.txt`, righe 22–3601 — **731/731 unità**, file completo.

## Numeri misurati

| voce | valore |
|---|---|
| unità | 731 / 731 |
| contesti | 75 |
| parole | 22.378 EN → 21.188 IT (0,947) |
| parti | 11 (43, 44, 62, 70, 73, 72, 79, 72, 81, 82, 53) |
| tab | 408 IT = 408 EN |
| virgolette | 1.002 IT = 1.002 EN |
| token `<...>` | 166 IT = 166 EN |
| parentesi quadre | 113 unità, struttura identica al sorgente |
| rapporto per unità | 0,72 – 1,44 (gate 0,55–1,90) |
| `NT` | 11 `UI_LABEL` (`skip unmark <stella>`) |
| `check.py` | `FAIL totale: 0` (22 controlli) |
| `verify.py` | 27 controlli, exit 0, `FAIL: 0` |
| sha256[:16] `translation.json` | `1bc292eafe08f311` |
| sha256[:16] `source.json` | `6cee150d40590017` |
| sha256[:16] `check.py` | `3c18f17051613ca9` |
| sha256[:16] `verify.py` | `6233f33a76edc797` |
| dimensione directory | 1,4 MB (11 parti) |

## Tipi presenti (misurati sul `source.json`)

```
MISSION_TEXT 494 · DESCRIPTION 68 · VALUE 61 · DIALOG 56 · LOGBOOK 41 · UI_LABEL 11 · CONVERSATION 0
```

Rispetto a L32 cambia la composizione: nessun `CONVERSATION` e undici `UI_LABEL` di salto, che sono le
uniche unità non traducibili del lotto. Il `NT` di L32 (`"Bondir" Atomic Thruster`, `alt start`,
`alt end`) **non** è valido qui: la lista è stata rifatta sulle unità di questo file.

## Comandi di verifica

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n

# 1. coerenza interna del lotto (22 controlli + copertura)
python staging/editorial/L33_20261018_114017/check.py        # atteso: FAIL totale: 0

# 2. verifica indipendente, senza riusare la logica di check.py (27 controlli)
python staging/editorial/L33_20261018_114017/verify.py       # atteso: exit 0, FAIL: 0

# 3. preflight del workspace e integrità dei file protetti
python staging/editorial/tools/state.py                      # atteso: ESITO: OK
```

## Cosa è stato corretto in questo lotto

| unità | problema | correzione |
|---|---|---|
| 18, 58 | rapporti fuori banda comoda | riscritte |
| 286 | ordine dei gruppi nelle parentesi quadre invertito | «la più [attraente, gradita] [linea d'azione?]» |
| 324 | un gruppo di parentesi quadre perso | reintrodotto `[saccheggiare, cacciare]` |
| 331 | rapporto 0,61 sotto il gate | «È proprio una serra.» |
| 391 | rapporto 0,44 sotto il gate | «E che cosa facciamo con i droni Sestor?» |
| 411/721 vs 593 | tre inglesi diversi resi con la stessa frase | «Certo, con piacere.» / «Naturalmente, ne sarò felice.» |
| 485 | refuso «lo metallo» | «il metallo» |
| 569 | virgoletta di troppo non presente nel sorgente | rimossa |
| 685 | un gruppo di parentesi quadre perso | reintrodotto `[tenteranno, porteranno a termine]` |

## Limiti dichiarati

- **Non verificato nell'editor, non caricato nel gioco, non approvato nel database.** Il lotto è staging
  editoriale: `state.db` resta in sola lettura e le 731 unità sono `PENDING`. Il caricamento è una fase
  separata, non richiesta qui.
- **La lacuna `log` non è riparabile da questo lotto.** In `wanderers middle.txt` la forma della perdita
  è documentata in `review.md` §7; `tools/l10n.py` e `state.db` sono file protetti (hash nel checkpoint).
- **Residuo**: 15.431 unità secondo la formula di `state.py`; il valore misurato è nel checkpoint
  editoriale, che riporta entrambi perché la formula sottrae due volte le `UI_LABEL` già in staging.
- **Lunghezza delle frasi**: il gate 0,55–1,90 non dice nulla sulla qualità della resa. Le decisioni
  editoriali che lo hanno reso possibile sono in `review.md`, non in questo rapporto.
