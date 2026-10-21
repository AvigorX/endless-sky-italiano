# L42 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L42_20261018_155050` · `data/remnant/remnant 2 cognizance.txt` · righe 16–1747 · **572/572 unità**.
Ventiduesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 572 unità, 40 contesti (`Remnant: Cognizance 1` … `Remnant: Cognizance 38`),
  kind 438 `MISSION_TEXT` / 39 `VALUE` / 39 `DESCRIPTION` / 19 `DIALOG` / **35 `UI_LABEL`** / 2 `LOGBOOK`.
- `check.py` derivato da L41 con **`NT` = le 35 `UI_LABEL`** (label di salto, bersagli di `goto`),
  elencate una per una, e col **costruttore che antepone i tab iniziali del sorgente** (342).
- 14 parti, tutte a fine contesto: 58 · 39 · 49 · 41 · 38 · 52 · 46 · 37 · 39 · 35 · 22 · 50 · 40 · 26.
- `translation.json`: 572 unità, 22.761 EN → 21.522 IT (0,945), rapporto per unità 0,60–1,77,
  sha256[:16] `1115f51df15d6704`.
- `verify.py`: **33 controlli**, `FAIL: 0`, exit 0. Copertura **572/572** asserita, coppia di righe
  **(16, 1747)**, insieme delle 11 virgolette dispari asserito.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **35 `UI_LABEL`, il numero più alto della serie**: tutte lasciate identiche e messe in `NT` una per una
  (`void rifle`, `fleet kill…`, `cognizance explanation`). Una deroga generale («salta le non
  traducibili») avrebbe nascosto le omissioni vere.
- **Tab 342**: nessuna traduzione è stata scritta con `\t` nel valore; i tab li aggiunge il costruttore
  leggendo il numero di tab iniziali dell'inglese, e il controllo per unità verifica la parità.
- **11 virgolette dispari** (32, 48, 50, 201, 240, 241, 245, 246, 342, 485, 558): sono battute aperte nel
  sorgente e sono state riprodotte aperte. Il `verify.py` confronta **l'insieme degli idx**, non il
  totale: in L41 l'insieme era vuoto e il confronto passava per caso.
- **2 `LOGBOOK`**: il testo della scheda di Gavriil (riga 388) e la voce «stormo introdotto a Esquiline»
  (riga 666), entrambi tradotti. La categoria `People` e il nome `Gavriil` della prima riga **non sono
  inventariati** (lacuna di `tools/l10n.py`, protetto): documentata in `review.md` §7.
- **Voce ereditata da L21/L24** (`remnant 1 introduction.txt`): Remnant, spettri del vuoto, Distesa di
  Braci, Prefetto, Ssil Vida, Esquiline, Gavriil, Dusk, Taely, Plume, Chilia, Aeolus, «Che le Braci
  brucino luminose».

## Verifica

```
python staging/editorial/L42_20261018_155050/check.py    → FAIL totale: 0 (21 controlli)
python staging/editorial/L42_20261018_155050/verify.py   → exit 0, 33 controlli, FAIL: 0
```

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 572 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
  In particolare non è verificato che la conversazione di Cognizance 1–38 scorra con i salti `goto`
  intatti: le 35 label sono identiche per costruzione, ma il percorso non è stato giocato.
- **Nessun test di gameplay** della campagna Remnant.
