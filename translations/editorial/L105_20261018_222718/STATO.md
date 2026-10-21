# STATO — L105 · `data/quarg/quarg missions.txt` — **ULTIMO LOTTO, CHIUDE IL FILE**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L105_20261018_222718` |
| Righe / unità | **335–506** / **61** |
| Tipi | **56 `MISSION_TEXT`** + **4 `UI_LABEL`** + **1 `LOGBOOK`** |
| `UI_LABEL` (identiche) | `heliarch 2` (29), `heliarch ask` (31), `lunarium 2` (36), `lunarium ask` (38) |
| `LOGBOOK` (tradotto) | unità 58: «Nome completo: Gohl Salyi Memt-Wrik Laz…» |
| Contesti | **1** (`Ask Quarg About Coalition Late`, 356–506) |
| Parole | **2155 EN → 2073 IT** (0,962); per unità 0,73–1,32 |
| Tab · virgolette | **54** · **99**, con **una citazione aperta** (unità 26) |
| Token · quadre | **7** in cinque famiglie (`<origin>`; `<first>`+`<last>` ×2; `<start planet>`, `<start system>`) · **0** |
| Ripetizioni | **5 gruppi**: 2/6, 3/7, 4/8, **17/20/24** (tripla), 21/25 |
| sha256 | `4ae2c9e490a62867…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **31 controlli**, exit **0** (invariante di file) |

## Invariante di FILE

| Voce | Valore |
|---|---|
| Unità prima della riga 356 | **117** (L102–L104) |
| Unità dopo la riga 506 | **0** — il file finisce qui |
| File | **178 unità**, `max(line) = 506` |
| Copertura | **178/178 (100%)** — 178 id distinti su 178 righe, **0 sovrapposizioni** |
| Lotti | **4** — L102 (48), L103 (42), L104 (27), L105 (61) |
| Parole del file | **5.417 EN → 5.184 IT** |

`quarg missions.txt` è il **quarantesimo file completo**, **non approvato**.

## Contenuto

Un solo contesto, lunghissimo: l'incontro con **Gohl Salyi Memt-Wrik Laz**, il Quarg anziano con la cicatrice e la
veste bianca. Attraverso due domande d'apertura (chi ha il grado di Heliarch, chi si è unito al Lunarium), la
conversazione ricostruisce la storia della Coalizione dalla parte dei Quarg: il rapido sorgere delle tre specie, i
Saryd «molto simili a noi Quarg nei nostri anni giovani», la carestia dei Kimek, l'arrivo degli Arach; poi la
guerra, «un millennio di combattimenti», la perdita degli anelli e la resa — «Non fummo più visti come protettori,
ma come coloro da cui dovevano proteggersi».

Poi le due diramazioni (Heliarch e Lunarium), l'avvertimento — «Non essere arrogante. Non sottovalutarli» — e la
domanda finale: **«Dov'è la tua casa?»**, con sette risposte possibili, da New Boston a «La mia nave è la mia
casa», fino al commiato: la dozzina di Quarg corazzati che si materializzano dalle pareti per seguirlo.

## Verifica

```bash
cd staging/editorial/L105_20261018_222718
python check.py   # FAIL totale: 0 (29 controlli)
python verify.py  # exit 0 (31 controlli, invariante di file: 178/178)
```
