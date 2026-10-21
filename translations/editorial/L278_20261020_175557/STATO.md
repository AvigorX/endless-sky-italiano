# STATO — L278 (`data/human/kestrel.txt`, righe 15–54)

**Stato: CHIUSO.** Primo lotto del file: **16 unità** nella missione `Kestrel Testing` — l'incontro con **Charles Atinoda**. Il
file è aperto a **16/51 (31,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L278_20261020_175557/` |
| file | `data/human/kestrel.txt` (51 unità · 1.064 parole · righe 15–402) |
| righe | 15–54 |
| unità | **16** — 14 `MISSION_TEXT` + 1 `DESCRIPTION` + 1 `VALUE` |
| parole | **458 EN → 422 IT** (0,92) |
| rapporto | **0,86 – 1,12** |
| contesti | **1** — `mission:Kestrel Testing` |
| tab | **13** (unità 4–16: tutte le battute tranne la prima) |
| virgolette | **42**, con lo **stesso numero per unità** (2 in inglese ⇒ 2 in italiano) |
| segnaposto | **5** — `<waypoints>` 1 · `<first>` 2 · `<last>` 2 |
| apici | **4 EN** / **9 IT** su 7 unità |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 0 prima (il lotto **apre** il file) · 16 qui · **35 dopo** la 54 |
| `sha256[:16]` | **`689dfc9e941857f3`** |

## Comandi

```bash
python staging/editorial/L278_20261020_175557/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L278_20261020_175557/verify.py    # FAIL: 0 (22 controlli, 16/51)
```

## La scena

Un **bar dello spazioporto**. Un uomo riconosce il giocatore, si presenta — **Charles Atinoda**, progettista capo della
**Tarazed Corporation** — e racconta un **colloquio con una visione**: sette anni prima, in crisi personale, vagò per la
galassia, fu accolto da una **comune anarchica**, e nella **capanna del sudore** vide «una spada fatta di luce», «un sole blu»
e «un Welsh Corgi che entrava in un computer». Da quella nave scura intravista in trance è nata la **Kestrel**.

Il registro è quello di un uomo che parla molto di sé: la resa conserva le pause (`Si ferma un momento.`), il passaggio dal
serio al ridicolo, e il **«...»** sospeso prima della battuta sul Corgi.

## La `DESCRIPTION` e la regola del collaudo

> «Recati nel sistema `<waypoints>` per combattere e **disabilitare** una nave da guerra prototipo… **Non distruggere** la
> nave, o perderai il pagamento e l'occasione di comprarne una.»

È la stessa distinzione già fissata in `remnant jobs.txt` (Dathnak A'awoj *disabilitata*, non distrutta): il `check.py` la
verifica esplicitamente, perché confonderla renderebbe la missione **impossibile da completare**.

## Limiti dichiarati

Nessuna approvazione (16 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **35 unità**.
