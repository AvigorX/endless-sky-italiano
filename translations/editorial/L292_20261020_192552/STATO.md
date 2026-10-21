# STATO — L292 (`data/avgi/avgi culture conversations.txt`, righe 229–259)

**Stato: CHIUSO.** Terzo lotto del file: **l'albero di dialogo della scherma Avgi**, in **un solo contesto**, con i **primi due
`LOGBOOK` del progetto**. File a **37/46 (80,4%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L292_20261020_192552/` |
| righe | 229–259 |
| unità | **17** — **15 `MISSION_TEXT` + 2 `LOGBOOK`** (righe 255, 256) |
| parole | **464 EN → 436 IT** (0,94) |
| rapporto | **0,80 – 1,27** |
| contesto | **1** — `mission:Avgi Culture: Fencing` |
| tab | **15** (tutte le `MISSION_TEXT`; i `LOGBOOK` **no**) |
| virgolette | **26**, per unità |
| scelte del giocatore | **2** — `(Avvicinati.)` / `(Ignorali.)`, punto dentro |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| apici | **5 EN / 17 IT** |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **25 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 20 prima · 17 qui · **9 dopo** la 259 |
| `sha256[:16]` | **`1b567ec16d25227d`** |

## Comandi

```bash
python staging/editorial/L292_20261020_192552/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L292_20261020_192552/verify.py    # FAIL: 0 (25 controlli)
```

## I primi due `LOGBOOK` del progetto

| riga | inglese | resa |
|---|---|---|
| 255 | `Zomp is a muted teal Avgi who defeated the reigning champion Razmatazz in a fencing match.` | **Zomp è un Avgi di verde acqua spento che ha sconfitto il campione in carica, Razmatazz, in un incontro di scherma.** |
| 256 | `Watched a fencing match between two Avgi onboard a Dissonance station…` | **Ho assistito a un incontro di scherma fra due Avgi a bordo di una stazione della Dissonanza…** |

Sono **prosa di diario**: la 256 ha il soggetto **sottinteso** («ho assistito», non «Watched»), e la resa lo **esplicita** in
**prima persona**. I due logbook **non hanno tab** (non sono né dialoghi né scelte), ed è la prima volta che il progetto
incontra il tipo `LOGBOOK`: il test li distingue **per tipo**, non per posizione.

## Il tic delle domande

Gli Avgi chiudono le domande con la parola **`question?`**:

> «Invito. Umano, sei forse interessato ad assistere all'antico sport Avgi della scherma, **domanda**?»

Non è retorica: è la loro **etichetta**. La resa la conserva **in fondo alla frase**, e il test verifica che le **due** battute
che la contengono (righe 232 e 258) finiscano con `domanda?"`.

## La scena ripetuta 248 / 251

La 251 è la 248 **più un cartello**:

> «…tifare per uno o per l'altro dei partecipanti. **Un cartello in particolare dice "ZOMP PER SCHIACCIARLI COME L'ASSEMBLEA!"**»

Il test verifica che la resa della 251 **inizi** con quella della 248 — non solo che si somiglino: il testo comune deve essere
**prefisso esatto**.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `fencing` | **scherma** | |
| `rapiers` | **stocchi** | come in L291 |
| `bleachers` / `rails` | **gradinate** / **ringhiere** | |
| `pedestals` | **piedistalli** | |
| `copper wires` | **fili di rame** | |
| `the reigning champion` | **il campione in carica** | |
| `paragons of the blade` | **paradigmi della lama** | |
| `Dissonance station` | **stazione della Dissonanza** | corpus |
| `Zomp`, `Razmatazz` | **invariati** | |
| `the Assembly` | **l'Assemblea** | istituzione |

## Limiti dichiarati

Nessuna approvazione (17 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **9 unità**, tutte
`MISSION_TEXT`, nello stesso contesto: l'**epilogo** dello scontro.
