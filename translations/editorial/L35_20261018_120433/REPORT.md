# L35 — REPORT (chiuso 2026-10-18)

`data/human/free worlds 1 start.txt`, righe 16–2343 — **663/663 unità**, file completo.

## Numeri misurati

| voce | valore |
|---|---|
| unità | 663 / 663 |
| contesti | 37 |
| parole | 21.140 EN → 20.273 IT (0,959) |
| parti | 10 (76, 59, 59, 77, 74, 64, 62, 73, 76, 43) |
| tab | 518 caratteri IT = 518 EN · 500 unità con tab iniziale |
| virgolette | 1.346 IT = 1.346 EN · 10 unità con conteggio dispari, riprodotte |
| token `<...>` | 139 IT = 139 EN |
| parentesi quadre | **0 unità** (controllo strutturale non applicabile, asserito) |
| rapporto per unità | 0,71 – 1,67 (gate 0,55–1,90) |
| `NT` | 2 unità: `no casualties` (label di salto) + `People` (categoria di diario) |
| `check.py` | `FAIL totale: 0` (21 controlli) |
| `verify.py` | 27 controlli, exit 0, `FAIL: 0` |
| sha256[:16] `translation.json` | `3a434b106edfceb3` |
| sha256[:16] `source.json` | `a108c4ffb2423f8a` |
| sha256[:16] `check.py` | `8a8625cd7cb7645d` |
| sha256[:16] `verify.py` | `7d066f78e2404eb6` |
| dimensione directory | 1,3 MB (10 parti) |

## Tipi presenti (misurati sul `source.json`)

```
MISSION_TEXT 550 · DESCRIPTION 33 · VALUE 32 · LOGBOOK 25 · DIALOG 22 · UI_LABEL 1 · CONVERSATION 0
```

Rispetto a L34 il profilo cambia di poco (0 → 1 `UI_LABEL`), ma la **forma della lacuna `log` cambia**:
qui una delle 25 righe ha prodotto la *categoria* invece del testo (unità 547, `People`), mentre le altre
24 hanno prodotto il testo. È il primo file in cui le due forme convivono.

## Comandi di verifica

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n

# 1. coerenza interna del lotto (21 controlli + copertura)
python staging/editorial/L35_20261018_120433/check.py        # atteso: FAIL totale: 0

# 2. verifica indipendente, senza riusare la logica di check.py (27 controlli)
python staging/editorial/L35_20261018_120433/verify.py       # atteso: exit 0, FAIL: 0

# 3. preflight del workspace e integrità dei file protetti
python staging/editorial/tools/state.py                      # atteso: ESITO: OK
```

## Cosa è stato corretto in questo lotto

| unità | problema | correzione |
|---|---|---|
| 50 / 470 | stesso italiano per `what do we do now` / `what do we do next` | «Allora, che cosa facciamo adesso?» / «E allora qual è il prossimo passo?» |
| 197 | rapporto 0,69 | «(Certo, altroché!)» |
| 278 | rapporto 1,75, al limite alto | «Scorta rifornimenti» |
| 302 | rapporto 0,68 | «E i sistemi pirata che stanno a nord di Men?» |
| 355 | «shock and awe» lasciato in inglese | «un assalto di shock e terrore» |
| 502 | rapporto 0,69 | «(Entra pure.)» |
| 626 | rapporto 0,48 (sotto il gate) | «E come facciamo a farlo?» |
| 537 | refuso di stesura («Origlierai») | «(Metti l'orecchio alla porta.)» |

## Limiti dichiarati

- **Non verificato nell'editor, non caricato nel gioco, non approvato nel database.** Il lotto è staging
  editoriale: `state.db` resta in sola lettura e le 663 unità sono `PENDING`.
- **La lacuna `log` non è riparabile da questo lotto** ed è la prima volta che si presenta in due forme
  nello stesso file: documentata in `review.md` §7. `tools/l10n.py` e `state.db` sono protetti.
- **L'unità 547 (`People`) resta in inglese**: è una categoria di diario, tradurla da sola creerebbe una
  categoria doppia rispetto alle altre che il gioco mostra in inglese.
- **Residuo**: 14.065 unità secondo la formula di `state.py`; il valore misurato e la differenza sono nel
  checkpoint editoriale (decisione 99).
- **Lunghezza delle frasi**: il gate 0,55–1,90 non dice nulla sulla qualità della resa. Le decisioni
  editoriali sono in `review.md`.
