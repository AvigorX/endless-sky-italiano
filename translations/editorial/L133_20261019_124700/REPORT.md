# REPORT — L133 · `unfettered side missions.txt` (la consegna con l'Anomalocaris e il duello di Mera)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `Hai Legacy 2` — il carico | 1–5 | 237–256 | `VALUE`, `DESCRIPTION` con `<planet>` e `<date>`, il carico già assegnato, il messaggio «porta l'Anomalocaris» |
| la consegna | 6–10 | 265–276 | gli Unfettered che smettono di sparare, i tre esiti, il pagamento, il diario |
| `Hai Legacy 3` — Mera | 11–17 | 283–298 | `VALUE`, `DESCRIPTION` con `<system>`, l'ingegnere, il relitto come segno, la sfida pubblica |
| le domande | 18–25 | 300–313 | «che ottengo se vinco», «posso vendertela», «è mia», le due risposte di Mera |
| le regole implicite | 26–34 | 313–325 | il campione, il capo, «non è una competizione amichevole», le cinque regole |
| il decollo | 35–39 | 328–350 | l'impazienza di Mera, la sola Anomalocaris, il messaggio a Ehma Ti, il «scimmia» |
| i forfait | 40–46 | 352–372 | troppe navi, flotta in orbita, relitto non in uso — tre rifiuti diversi |
| il duello | 47–58 | 380–448 | la fuga, la sconfitta, il cessate il fuoco finito, la resa, la distruzione della `Lightning Bug` |
| il congedo | 59–67 | 462–477 | il diario, «hai vinto davvero», le tre risposte, l'autorizzazione condizionata |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Heritage Reclaimed` · `Ancient Claim` | **identici** | `VALUE` |
| `too many ships` | **identico** | `UI_LABEL`, ripetuta in due unità |
| `bring aid` | **portare aiuto** | |
| `by <date>` | **entro il <date>** | token intatto |
| `outfits` · `shipyard` | **moduli** · **cantiere** | |
| `engineer` | **ingegnere** | Mera |
| `relic of our past` | **relitto del nostro passato** | |
| `challenge` · `duel` | **sfida** · **duello** | |
| `one-on-one` | **uno contro uno** | |
| `champion` | **campione** | |
| `being disabled counts as a loss` | **restare fuori uso conta come sconfitta** | |
| `To the victor go the spoils` | **Al vincitore vanno le spoglie** | |
| `True Hai` | **Veri Hai** | nome proprio di fazione |
| `monkey` | **scimmia** | insulto ricorrente degli Unfettered |
| `forfeit` | **annullato** | |
| `ceasefire` | **cessate il fuoco** | |
| `Lightning Bug` | **Lightning Bug** | nome di modello: resta inglese |
| `Ehma Ti` · `Firelode` | **invariati** | nomi di sistema e pianeta |
| `priceless artifact` | **artefatto inestimabile** | |

## 3. Difficoltà

1. **98 virgolette**: record del progetto, con **quattro unità dispari** (47, 48, 64, 65) a 1, 1, 3, 1 virgolette. Il
   totale da solo non le rivelerebbe.
2. **2 `VALUE`** con nomi di missione e **2 `UI_LABEL`** con lo stesso nome di nodo ripetuto: elencati entrambi.
3. **`<date>` e `<system>`** per la prima volta in questo file: parità verificata per unità.
4. **Incoerenza del sorgente**: il diario parla di `food shipment`, il testo di `medical supplies`. Le due rese sono
   fedeli a ciascuna frase, e il controllo le verifica entrambe.
5. **Nomi propri da non toccare**: `Ehma Ti`, `Firelode`, `Lightning Bug`, `Mera`, `Anomalocaris`, `True Hai`.
6. **Nove `DIALOG`** in un lotto: tipo che nei file precedenti compariva una o due volte per lotto.
7. **Registro**: gli Unfettered insultano (`scimmia`), Mera è pragmatica e sprezzante, il capo è cerimonioso. Le tre
   voci restano distinte.
8. **Gate**: minimo 0,80 (unità 61, «È stato divertente.»), massimo 1,57 (unità 10, il diario).

## 4. Numeri osservati

```
unita' 67/67 · MISSION_TEXT 50 · DIALOG 9 · VALUE 2 · DESCRIPTION 2 · LOGBOOK 2 · UI_LABEL 2 · tutte PENDING
contesti 2 (10/57) · testi distinti 64
tab 34 unita · virgolette 98 (18/44/1/3/1) · token 8 in 6 famiglie · quadre 0
parole EN 2007 -> IT 1821 (0.907) · rapporto 0.80 - 1.57, media 1.04
righe 237/477 · file 151/159 (95,0%) · 84 prima / 8 dopo · confine riga 494
FAIL totale: 0 (31 controlli) · verify exit 0 (32 controlli)
sha256[:16] c214c835e561be8e
```

## 5. Stato del progetto

```
TOTALE staging: 27378 unità · 864257 EN · 821153 IT
unfettered side missions.txt: 151/159 (95,0%) · 2 lotti · 4062 EN -> 3671 IT
file completi: quarantasette · residuo traducibile (formula state.py): 4552
residuo misurato: 5217 unità / 112836 parole su 119 file
avanzamento: 27378/32924 unità (83,2%) · 864257/979975 parole (88,2%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (32 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 67 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: restano **8 unità** (righe 494–510).
- **Prossimo lotto**: `HANDOFF_L134_20261019.md` — righe **494–510**, che **chiude il file**: **8 unità**, **356
  parole**, **1 contesto**, **7 unità con tab**, **13 virgolette**, **zero token**.
