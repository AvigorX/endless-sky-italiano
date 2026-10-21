# L51 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L51_20261018_171829` · `data/avgi/avgi 0 first contact.txt` · righe 413–869 ·
**152/152 unità**. Con L50 (**119**) il file è a **271/406 (66,7%)**: **non completo**, restano 135 unità
dopo la riga 869 (previste in L52).

## Fatto

- `source.json`: 152 unità, **5 contesti** (`Avgi: Defend Ensemble 1` 1–43, `Avgi: Defend Ensemble 2`
  44–104, `Avgi: Scout Rescue` 105–132, `Avgi: Frontline Combat` 133–143,
  `Avgi: Dissonance Outreach 0.5` 144–152), kind 126 `MISSION_TEXT` / 10 `LOGBOOK` / 6 `DIALOG` /
  5 `VALUE` / 5 `DESCRIPTION`. Nessun `UI_LABEL`, nessun `TEXT`, nessun `CONVERSATION`.
- `check.py` derivato da L50 con una differenza strutturale: **`NT` è vuoto** — 0 `UI_LABEL` e 0
  riferimenti di dato. Il controllo delle unità non traducibili è quindi un'**asserzione di assenza**,
  aggiunta esplicitamente (`unita UI_LABEL nel segmento (0 attese: NT vuoto)`), non un elenco vuoto
  lasciato passare.
- 5 parti: **43 · 32 · 29 · 39 · 9** (tagli a fine contesto, con `Defend Ensemble 2` spezzato in due).
- `translation.json`: 152 unità, 4.314 EN → 3.971 IT (0,921), rapporto per unità 0,60–1,38,
  sha256[:16] `62a89c1348ea5162`.
- `verify.py`: **45 controlli**, `FAIL: 0`, exit 0. Segmento interno (119 prima / 135 dopo), copertura
  delle righe 413–869, `NT` vuoto, `LOGBOOK` 10 (6 + 4 + 0), `DIALOG` 6, `TEXT` 0, parità di
  tab/virgolette/token per unità, duplicati inglesi con resa identica.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Primo lotto della serie senza unità non traducibili.** In tutti i precedenti c'erano `UI_LABEL` da
  elencare una per una. Qui non ce n'è nessuna: il `check.py` lo dichiara, e `verify.py` asserisce che
  nessuna unità del segmento è stata lasciata identica all'inglese per via di una dichiarazione di
  intraducibilità.
- **`DIALOG` 6 contro 2 di L50**: le sei righe `dialog \`…\`` sono i messaggi di blocco (scorta non
  arrivata, Aberranti ancora nel sistema, Albedo non trovata). Tutte tradotte e tutte distinte.
- **`LOGBOOK` 10**: quattro fra backtick (47, 61, 118, 142) e sei a tre argomenti (4, 48, 49, 62, 63,
  64: `People`/`Factions`). **Nessuna categoria estratta** — la lacuna dell'estrattore continua a non
  presentarsi.
- **Il nome del personaggio è incoerente nel sorgente**: `Darius Caldwell` (unità 4) e `Darius Calwell`
  (unità 129, 148, e in L50). Il nome proprio resta invariato **come nel sorgente**, quindi l'italiano
  riproduce entrambe le grafie. Non è una svista di traduzione: è un difetto inglese, registrato in
  `review.md` §4.
- **`<npc>`** compare per la prima volta nella serie (unità 106) ed è trattato come token:
  «l'equipaggio della <npc>», con `<npc>` invariato.
- **Lessico nuovo**: `bunk` → **cuccetta** (73 occorrenze nel corpus) · `atomics` → **atomiche** ·
  `Wardragon` → **Dragoguardia** · `space shoggoths` → **shoggoth spaziali** · `Fairyland` → **Paese
  delle Fate** · `Assemblyman` → **membro dell'Assemblea** · `Feo Platform` → **Piattaforma Feo**
  (già nel corpus) · `Deep Security` → **Sicurezza della Deep** · `Refraktos-class Laserstar` →
  **Laserstar classe Refraktos** · `Polari`, `Prismaios`, `Silver Albedo`, `Spectral Collision`,
  `Navigeo Yards`, `Peripheria`, `Weledos`, `Arche`, `Evanescence`, `Quintessence`, `Empyrean`,
  `Valhalla`, `Dabih`, `Sadr`, `Twirl` **invariati**.

## Verifica

```
python staging/editorial/L51_20261018_171829/check.py    → FAIL totale: 0 (31 controlli)
python staging/editorial/L51_20261018_171829/verify.py   → exit 0, 45 controlli, FAIL: 0
```

`state.py` dopo L51: **23.120 unità · 736.637 EN · 698.859 IT**, `ESITO: OK`,
`avgi 0 first contact.txt` a **271/406 (66,7%)**, **55 directory** con `translation.json`.

## Non fatto (dichiarato)

- **Nessuna approvazione nel database**: le 152 unità sono `PENDING`.
- **Nessun caricamento nel gioco**: la battaglia di Ensemble, il salvataggio della Silver Albedo e la
  caccia agli Aberranti non sono mai state viste a schermo.
- **Il file non è completo**: restano 135 unità dopo la riga 869, previste in L52.
