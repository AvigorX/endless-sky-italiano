# STATO — L272 (`data/dialog phrases.txt`, righe 102–172)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 54/54 (100%)**, **diciottesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L272_20261020_172929/` |
| file | `data/dialog phrases.txt` (**54/54 unità · 876 parole · righe 16–172**) |
| righe | 102–172 |
| unità | **25** — tutte `TEXT` |
| parole | **446 EN → 438 IT** (0,98) |
| rapporto | **0,92 – 1,31** |
| contesti | **18** — taglie, flotte pirata, contrabbando, Free Worlds, tributo pacifista |
| segnaposto | **30** in **6 famiglie**, identici in inglese e italiano |
| tab / virgolette | **0 / 0** (asserzioni negative) |
| apici | **7 EN** / **4 IT** |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invarianti | **di segmento** (29 prima · 25 qui · **0 dopo**) **e di FILE** (54 unità · righe distinte · ultima 172 · somma dei 2 lotti = 54) |
| `sha256[:16]` | **`87672d3cd0cc297b`** |

## Comandi

```bash
python staging/editorial/L272_20261020_172929/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L272_20261020_172929/verify.py    # FAIL: 0 (21 controlli, 54/54)
```

## Il blocco pacifista: otto frasi, non tre

Il contratto L272 diceva «tre unità (165, 167, 171)»; il database ne ha **otto** (165–172), tutte nello stesso contesto
`phrase:tribute pacifist undefined`. **Vince il workspace**: i documenti sono stati corretti e il `check.py` verifica il
blocco come **otto frasi distinte**, di cui **una sola** nomina il tributo («non ti pagheremo nemmeno un solo credito di
tributo»).

## Le altre scelte

- **`<npc>` è una nave → femminile**: «<npc> è stata eliminata», «e la sua flotta sono state eliminate» (4 unità con «la sua
  flotta»);
- **`<bunks>` è un numero di cuccette**, nuovo nel corpus: «fanno sbarcare dalla tua nave **<bunks> schiavi**»;
- **contrabbando senza edulcorazione**: «merce altamente illegale», «schiavi», «spazioporto», «città principale»;
- **Free Worlds invariato**; `revert to the autosave` → «torna al salvataggio automatico», `snapshot of your pilot` →
  «istantanea precedente del tuo pilota».

## Limiti dichiarati

Nessuna approvazione (25 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non **approvato**.
