# REPORT — L128 · `incipias first contact.txt` (la coda: gli Incipias salvati, i capi-governatori)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `Fix Saves Missing Language` | 1–2 | 343–344 | l'avviso sul pannello e la voce di diario recuperata |
| `No Help For The Stranded` | 3 | 360 | la nave ritrovata e lasciata al suo destino |
| la discesa nel gigante gassoso | 4–12 | 364–387 | il `VALUE`, il `DESCRIPTION`, lo spazio passeggeri, le nuvole, i due portelli |
| il salvataggio | 14–17 | 390–393 | le due battute, i composti degli Incipias, la partenza in tempo |
| la stazione e i capi-governatori | 18–21 | 396–400 | Hicemus e Conlatio, l'aiutante-esterno, la stanza con vista |
| le domande | 22–35 | 402–425 | lo scambio, le due versioni della spiegazione, le quattro domande |
| le risposte | 36–43 | 427–439 | il mondo-origine, il ponte-stellare, la vita su un gigante gassoso, il congedo |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Bring Incipias back to <planet>` | **identico** | `VALUE`, nome di missione con token |
| `has incipias ship` · `initial choice` · `odd question` · `end no time` | **identici** | `UI_LABEL` |
| `day-moment` | **giorno-momento** | |
| `life-protector` | **protettore-di-vite** | |
| `weather-calamity` | **calamità-meteo** | |
| `outer-helper` | **aiutante-esterno** | coerente con «essere-esterno» di L127 |
| `leader-governers` | **capi-governatori** | |
| `question-queries` | **domande-quesiti** | |
| `time-patience` | **tempo-pazienza** | |
| `space-void` | **vuoto-spazio** | |
| `observing-studying` | **osservare-studiare** | |
| `raise-strengthens` | **accresce-rafforza** | |
| `profound-depth insight` | **visione-profonda** | |
| `determination-will` | **determinazione-volontà** | |
| `origin-world` | **mondo-origine** | |
| `future-point` | **punto-futuro** | |
| `aged-time values` | **valori di tempi-antichi** | |
| `action-pride` | **orgoglio-azione** | |
| `star-bridge` | **ponte-stellare** | |
| `odd-reasonable` | **strano-ragionevole** | |
| `reasoning-origin` | **origine-ragione** | |
| `cloud-halls` · `home-sky` | **sale-nuvole** · **cielo-casa** | |
| `color-sings` · `color-lifeful` | **canti-di-colore** · **color-vitali** | |
| `poetic-gradient` | **gradiente-poetico** | |
| `meeting-talk` | **incontro-colloquio** | |
| `understanding-sad` | **comprensione-triste** | |
| `Hicemus` · `Conlatio` | **invariati** | nomi dei due gruppi |
| `claw-like attachments` | **attaccamenti simili ad artigli** | |
| `pillar-clouds` | **nuvole-pilastro** | |

## 3. Difficoltà

1. **Il lotto chiude il file**: `verify.py` passa a **invariante di file** (55 + 63 + 43 = 161, sovrapposti 0,
   `max(line) = 439`). Il conteggio viene dalla somma dei tre `translation.json`, non da un numero a mano.
2. **4 `UI_LABEL`** e **1 `VALUE`** identici: il `VALUE` contiene un **token** e il confronto è sulla stringa intera.
3. **6 token in 5 famiglie** sparsi su cinque unità (1, 4, 5, 6, 19): parità per unità, non per somma.
4. **Tre battute non chiuse** (28, 30, 36): riprodotte con una sola virgoletta; il controllo verifica che le unità
   dispari siano esattamente quelle.
5. **Una voce di diario identica a L127**: riletta dal `translation.json` precedente e confrontata, non ricopiata.
6. **26 composti con trattino**: lo stile degli Incipias è la parte più delicata; 15 sono verificati dal controllo.
7. **Un controllo di cortesia sbagliato**: cercava `\blei\b` e bocciava «come se non avessero alcun effetto su di
   lei», dove `lei` è la **nave**. Corretto: la cortesia si scrive con la maiuscola (`Lei`, `Suo`), il pronome no.
8. **Gate**: minimo 0,67 (unità 11, la label), massimo 1,33.

## 4. Numeri osservati

```
unita' 43/43 · MISSION_TEXT 33 · UI_LABEL 4 · LOGBOOK 3 · DIALOG 1 · VALUE 1 · DESCRIPTION 1 · tutte PENDING
contesti 3 (2/1/40) · testi distinti 43 · nessuna ripetizione interna
tab 30 unita · virgolette 43 (una sola nelle unita 28/30/36) · token 6 in 5 famiglie · quadre 0
parole EN 1177 -> IT 1100 (0.935) · rapporto 0.67 - 1.33, media 1.05
righe 343/439 · 118 prima / 0 dopo · FILE CHIUSO 161/161
FAIL totale: 0 (30 controlli) · verify exit 0 (33 controlli)
sha256[:16] 2efab055b9515fde
```

## 5. Stato del progetto

```
TOTALE staging: 26987 unità · 855624 EN · 813002 IT
incipias first contact.txt: 161/161 (100,0%) · 3 lotti · 4662 EN -> 4282 IT
file completi: quarantasei · residuo traducibile (formula state.py): 4946
residuo misurato: 5583 unità / 121378 parole su 120 file
avanzamento: 26987/32924 unità (82,0%) · 855624/979975 parole (87,3%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (33 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 43 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **`incipias first contact.txt` è completo solo in staging**: 161 unità tradotte, zero caricate nel gioco.
- **Prossimo lotto**: `HANDOFF_L129_20261019.md` — file **nuovo**, `data/human/boarding missions.txt`, righe **15–386**
  (**89 unità**, **852 parole**, **18 contesti**, **48 `TEXT`**, **6 `CONVERSATION`**, **43 token in 7 famiglie**).
