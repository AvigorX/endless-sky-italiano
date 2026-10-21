# L22 — report di chiusura

**File:** `data/human/jobs.txt`, righe **15–4600** (file completo)
**Directory:** `staging/editorial/L22_20261017_211319/`
**Sorgente:** `endless-sky/data/human/jobs.txt`, commit `b4aa3bac3` (non modificato)

## 1. Volume

| misura | valore |
|---|---|
| parole inglesi | **5.823** |
| parole italiane | **5.969** (102,5%) |
| unità tradotte | **390 / 390** |
| contesti | **161** |
| parti | **4** |
| tab / virgolette | 10 / 18 — identici al sorgente |
| token `<…>` | **840 / 840, parità esatta** (nessun pronome, nessuna eccezione) |
| unità non traducibili | **0** (`NT` vuoto) |
| rapporto IT/EN | min 0,70 · max 1,65 |

Tipi: `DESCRIPTION` 161 · `VALUE` 157 · `DIALOG` 52 · `MISSION_TEXT` 20.

## 2. Controlli

```
check.py     FAIL totale: 0    · 4 parti · 0 unità mancanti
verify.py    24 controlli, 0 FAIL, exit 0
```

Il controllo più significativo: **copertura del file 390 / 390**, nessun altro lotto tocca
`jobs.txt`, nessuna unità prima della riga 15 né dopo la 4600.

## 3. Deviazione dal target — dichiarata

**5.823 parole contro un obiettivo di ~40.000 (−85,4%).** Il file intero è questo: 390 unità,
4.600 righe. Non esiste un confine a 40.000 parole dentro `jobs.txt`, e allargare il lotto ai file
di job board successivi non porta al target (kestrel 1.064 · marauders 1.492 · message buoys 210 ·
near earth jobs 470 · news 716 · outfits 2.373 — tutti insieme altri 6.325). Le due alternative
erano: (a) dichiarare un lotto da 12.000 parole misto di sette file diversi, (b) chiudere il file
da solo e ripartire con un lotto che il target lo raggiunge davvero. Scelta **(b)**: un lotto
coerente per file, e L23 su un file da 38.724 parole.

## 4. Integrità

| verifica | esito |
|---|---|
| repository `endless-sky` (`b4aa3bac3`) | non modificato |
| `state.db` | non scritto; 390 unità restano `PENDING` |
| batch, glossario, inventario, output approvati | non toccati |
| patch K4 / build / test di gioco / applicazione | non eseguiti |
| rendering nel gioco | **non verificato** |

`translation.json` sha256[:16] = `24e9b400b5c5cb75`.

## 5. Stato complessivo dopo L22

```
human missions.txt   4253/ 4253 (100.0%) · 104495 EN ->  98511 IT · 6 lotti
intro missions.txt    637/  637 (100.0%) ·  19451 EN ->  17681 IT · 1 lotto
jobs.txt              390/  390 (100.0%) ·   5823 EN ->   5969 IT · 1 lotto
map planets.txt      1544/ 1544 (100.0%) ·  83687 EN ->  83453 IT · 18 lotti
TOTALE staging: 6.824 unità · 213.456 EN · 205.614 IT
residuo traducibile: 25.106 unità
```

## 6. Prossimo passo — L23

`data/human/deep missions.txt` **da solo** vale il target:

| Voce | Valore |
|---|---|
| Righe | **16–4293** |
| Unità | **1.355** (di cui 22 `UI_LABEL` non traducibili → 1.333 traducibili) |
| Parole | **38.724** (38.676 traducibili) |
| Contesti | **83** (da `Deep: Syndicate Convoy` a `The Book of Skadenga`) |
| Tab / virgolette | **1.043 / 1.816** |
| Tipi | `MISSION_TEXT` 1.041 · `CONVERSATION` 122 · `DESCRIPTION` 54 · `VALUE` 52 · `DIALOG` 43 · `LOGBOOK` 19 · `TEXT` 2 · `UI_LABEL` 22 |
| Confine dopo | fine file (nessuna unità dopo la riga 4293) |

Attenzione: **`TEXT` 2** è un tipo mai incontrato nei lotti L1–L22; va ispezionato sul `raw` prima
di decidere se è prosa traducibile.
