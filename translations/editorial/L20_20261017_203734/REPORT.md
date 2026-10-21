# L20 — report di chiusura

**Lotto:** L20, quinto lotto di `data/human/human missions.txt`
**Directory:** `staging/editorial/L20_20261017_203734/`
**Sorgente:** `endless-sky/data/human/human missions.txt`, commit `b4aa3bac3` (non modificato)
**Righe:** 6432–10806 · **Unità:** 1.676 · **Contesti:** 62 (60 missioni, 2 schede nave)

## 1. Volume

| misura | valore |
|---|---|
| parole inglesi | **40.112** |
| parole italiane | **38.248** (95,4% dell'inglese) |
| unità tradotte | **1.676 / 1.676** |
| tab / virgolette / token `<…>` | 1.391 / 1.922 / 303 — identici al sorgente |
| rapporti IT/EN | min 0,57 · max 1,88 · nessun valore fuori da [0,55; 1,90] |

Target dichiarato: ~40.000 parole. Scostamento: **+112 parole (+0,28%)**, accettato perché il
confine 10806 chiude `mission:Stone to Hope` e l'unità successiva (10812) apre
`mission:Stone to Ice Queen`. Tagliare a 40.000 esatte avrebbe spezzato una missione.

## 2. Tipi di unità

| tipo | n |
|---|---|
| `MISSION_TEXT` | 1.463 |
| `UI_LABEL` | 71 |
| `LOGBOOK` | 51 |
| `DESCRIPTION` | 42 |
| `VALUE` | 39 |
| `DIALOG` | 10 |

Le 71 `UI_LABEL` sono rimaste **identiche all'inglese** (sono chiavi di stato delle missioni,
non testo visibile). `check.py` le elenca in `NT` e `verify.py` ne verifica l'identità una per una.

## 3. Controlli

`python staging/editorial/L20_20261017_203734/check.py`

```
parole EN 40112 -> IT 38248
tab IT 1391 / EN 1391
virgolette IT 1922 / EN 1922
token IT 303 / EN 303
parti caricate: 19 · duplicati inglese: 98 gruppi (244 unita)
unita mancanti nel lotto: 0
FAIL totale: 0
```

`python staging/editorial/L20_20261017_203734/verify.py` → **22 controlli, 0 FAIL, exit 0**

Controlli indipendenti (non riusano `check.py`): riga grezza identica al file sorgente ·
english/kind/path identici a `state.db` · stato `PENDING` · nessuna unità `APPROVED` ·
id univoci e ordine = sorgente · collocazione del lotto · unità successiva 10812 ·
unità precedente 6428 · copertura del file · 71 label identiche · token/tab/virgolette ·
nessun italiano vuoto · nessun carattere non latino · rapporti definiti · le parti su disco
ricostruiscono `translation.json`.

## 3-bis. Nota su `translation.json`

`check.py` di L20 **rigenera** `translation.json` dalle parti a ogni esecuzione (serializzazione
propria, `indent=1`). L'hash citato nell'handoff è quindi quello che si ottiene **dopo l'ultima
esecuzione di `check.py`**, non quello del primo merge manuale: `sha256[:16] = b955f643f2acd399`.
Nessun contenuto cambia (le parti sono la fonte), cambia solo la forma del file.

## 4. Correzioni

- **40 unità** con citazione aperta nel sorgente: allineate al conteggio dispari dell'inglese
  invece di «normalizzarle» (elenco in `review.md` §4.2).
- **6 gruppi** di duplicati italiani non giustificati dal sorgente: differenziati
  (832/837/844, 280/357/577, 377/1093/1591, 1510/1550, 1570/1573).
- 137 punteggiatura · 216 refuso `Limítati` · 209 frase ridondante · 278 «concourse» ·
  517 refuso `senzaintoppi` · rimossa la chiave spuria `1189b` dal file di parte 13.

Nessun controllo è stato allentato e nessuna regex è stata modificata per ottenere `FAIL 0`.
L'unica modifica a `check.py` rispetto a L19 è `TITLES` con `'they/them'` (unità 214:
autodichiarazione di identità del personaggio, documentata in `review.md` §4.1).

## 5. Integrità

| verifica | esito |
|---|---|
| repository `endless-sky` (commit `b4aa3bac3`) | **non modificato** — nessuna scrittura |
| `state.db` | **non scritto** — 32.924 unità, 364 `APPROVED`, 32.560 `PENDING` |
| batch, glossario, inventario, output approvati | non toccati |
| patch K4 | non applicata |
| build, test di gioco, packaging, applicazione al gioco | non eseguiti |
| rendering nel gioco | **non verificato** — fuori dal perimetro di questo workflow |

`python staging/editorial/tools/state.py` → exit 0 (dopo l'aggiornamento del checkpoint).
`python staging/editorial/tools/check_handoff.py` → 0 FAIL (dopo l'aggiornamento dell'handoff).

## 6. Stato dello staging

| voce | valore |
|---|---|
| unità in staging (tutti i lotti) | **5.332** |
| parole EN → IT in staging | **177.136 → 171.608** |
| lotti | 23 (L1–L20 incluso L3b–L3d) |
| unità `PENDING` non ancora in staging | **27.228** |
| `human missions.txt` tradotto | **3.788 / 4.253 (89,1%)** |
| residuo nel file dopo la riga 10806 | **465 unità / 11.046 parole** |

Le 1.676 unità di L20 restano **`PENDING`**: sono tradotte solo in staging e non vanno
considerate approvate né applicabili al gioco.

## 7. Prossimo passo

- **File:** `data/human/human missions.txt`
- **Confine esatto:** riga **10812**, contesto `mission:Stone to Ice Queen`
- Comando di ricognizione:
  `python staging/editorial/tools/next_section.py "data/human/human missions.txt" 10812 40000 44000`

Nota per il prossimo lotto: dopo la riga 10806 restano solo **465 unità / 11.046 parole** in
questo file. Un lotto da ~40.000 parole non può essere completato qui: **L21 dovrà proseguire
nel file successivo** dopo aver verificato il confine, oppure chiudere il file e aprire un
lotto ridotto con deviazione documentata. Non inventare intervalli nel file seguente senza
averne misurato i confini con gli strumenti.
