# L21a — report di chiusura

**Segmento:** coda di `data/human/human missions.txt`, righe **10812–11777** (file esaurito)
**Directory:** `staging/editorial/L21a_20261017_205715/`
**Sorgente:** `endless-sky/data/human/human missions.txt`, commit `b4aa3bac3` (non modificato)

## 1. Volume

| misura | valore |
|---|---|
| parole inglesi | **11.046** |
| parole italiane | **10.356** (93,8%) |
| unità tradotte | **465 / 465** |
| contesti | **16** (8 missioni `Ice Queen`, 2 missioni `A Dead Man's Path`, 2 conversazioni, 4 contesti di raccordo) |
| tab / virgolette / token | 417 / 548 / 64 — identici al sorgente |
| rapporto IT/EN | min 0,69 · max 1,71 |

Tipi: `MISSION_TEXT` 346 · `CONVERSATION` 80 · `UI_LABEL` 12 · `VALUE` 10 ·
`DESCRIPTION` 10 · `DIALOG` 5 · `LOGBOOK` 2.

**Nota sul target:** L21 puntava a ~40.000 parole. Questo segmento ne copre 11.046 perché è
tutto ciò che resta nel file. Il lotto L21 prosegue nel file successivo (`L21b`, in preparazione);
questo report riguarda solo il segmento `human missions.txt`.

## 2. Controlli

`python staging/editorial/L21a_20261017_205715/check.py`

```
parole EN 11046 -> IT 10356
tab IT 417 / EN 417
virgolette IT 548 / EN 548
token IT 64 / EN 64
parti caricate: 5 · duplicati inglese: 13 gruppi (26 unita)
unita mancanti nel lotto: 0
FAIL totale: 0
```

`python staging/editorial/L21a_20261017_205715/verify.py` → **22 controlli, 0 FAIL, exit 0**

Il controllo più significativo: **copertura del file 4.253 / 4.253**. `human missions.txt` è
tradotto per intero in staging (L16 181 · L17 133 · L18 187 · L19 1.611 · L20 1.676 · L21a 465),
senza sovrapposizioni fra lotti e con tutti gli intervalli dentro il file.

## 3. File esaurito: implicazioni per i lotti successivi

- Non esiste un'unità dopo la riga 11777: il confine «fine file» è verificato dal codice, non
  dedotto.
- Il prossimo lotto **non** può restare in questo file: `L21b` apre
  `data/human/intro missions.txt` (righe 23–2319, 637 unità, 19.451 parole).
- `next_section.py` su questo file con inizio 11778 esce 2 («nessuna unità dopo la riga»):
  è il comportamento atteso, non un errore da aggirare.

## 4. Integrità

| verifica | esito |
|---|---|
| repository `endless-sky` (`b4aa3bac3`) | non modificato |
| `state.db` | non scritto; 465 unità restano `PENDING` |
| batch, glossario, inventario, output approvati | non toccati |
| patch K4 / build / test di gioco / applicazione | non eseguiti |
| rendering nel gioco | **non verificato** |

## 5. Prossimo passo

`L21b` — `data/human/intro missions.txt`, da riga 23. Comando di misura:

```bash
python staging/editorial/tools/next_section.py "data/human/intro missions.txt" 23 19000 21000
```
