# REPORT — L104 · `quarg missions.txt` (il Quarg parla della Coalizione, e l'avvertimento sulla nave Pug)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Ask Quarg About Coalition Early` | 265–284 | 11 | la versione dei Quarg sulla Coalizione, le due domande del giocatore, il congedo |
| `Quarg Pug Arfecta Warning` | 302–334 | 16 | l'attesa all'atterraggio, il drago, le quattro risposte, l'avvertimento, i Quarg dell'anello |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `foolish Coalition` | **stolta Coalizione** | |
| `usurpation of the great deeds of others` | **usurpare le grandi imprese altrui** | |
| `petty thieves` | **ladruncoli** | |
| `fanatical military` | **esercito fanatico** | |
| `wretched Heliarchs` | **miseri Heliarch** | |
| `hindered their development` | **ostacolavate il loro sviluppo** | |
| `slaughter billions` | **massacrare miliardi di esseri** | |
| `maintaining our position` | **mantenere la nostra posizione** | |
| `fabricated an excuse` | **si sono inventati una scusa** | |
| `one of your escorts, the Pug Arfecta` | **una delle vostre scorte, il Pug Arfecta** | nome di nave, invariato |
| `a baby in swaddling has tamed a dragon` | **un bambino in fasce avesse addomesticato un drago** | |
| `spewing fire with reckless abandon` | **sputando fuoco con abbandono sconsiderato** | |
| `without breaking its gaze, unblinking` | **senza distogliere lo sguardo, senza battere ciglio** | |
| `act of righteous defiance` | **atto di giusta ribellione** | |
| `God is dead` | **Dio è morto** | riferimento nietzscheano, conservato |
| `scoffs` | **sbuffa** | |
| `savior or a revolutionary` | **un salvatore o un rivoluzionario** | |
| `deign to prove them wrong` | **ti degni di dimostrare che si sbagliano** | |
| `burdens and dangers that follow it` | **fardelli e pericoli che ne seguono** | |
| `directs this power, and not it you` | **a dirigere questo potere, e non lui a dirigere voi** | l'inversione è nel testo |
| `curt farewell motion` | **breve cenno di commiato** | |
| `glare` | **sguardo torvo** | resa già usata in L99 |

## 3. Difficoltà

1. **Cinque citazioni aperte** (5, 19, 22, 23, 24): il discorso del Quarg continua nell'unità successiva. L'unità
   5 ne ha **tre** (apre, chiude una frase, riapre). Il `check.py` e il `verify.py` asseriscono l'insieme esatto
   e, per ciascuna, che l'unità **finisca senza virgoletta**.
2. **Un'unità identica al sorgente**: `(No.)` in italiano è `(No.)`. Il controllo «tutte tradotte» sarebbe
   diventato rosso su una traduzione **corretta**. È stato reso esplicito — «identica solo l'unità 3, per
   coincidenza linguistica» — invece di essere allentato: la differenza conta, perché un controllo generico
   lascerebbe passare anche una battuta dimenticata.
3. **Il trattino isolato dell'unità 23** (`umano - quale arma`): nel sorgente è un `-` con spazi, non un em dash.
   Riprodotto com'è; la tipografia del progetto vieta `—`.
4. **Le due varianti dell'arrivo** (12 e 13) dipendono dalla presenza della scorta Pug: la prima ha il capitano
   che vi indica, la seconda ha il Quarg che vi blocca l'uscita. Non sono varianti di stile, sono due scene.
5. **Le quattro risposte** (15–18) portano a due repliche del Quarg (20, 21): il tono cambia («tono sarcastico» /
   «quasi divertito, o forse incredulo») e la resa lo segue.

## 4. Numeri osservati

```
unita' 27/27 · 27 MISSION_TEXT · tab 24 · virgolette 37 = 37 (cinque citazioni aperte)
token 0 · quadre 0 · nessuna ripetizione · una sola unita identica al sorgente (3)
parole EN 631 -> IT 597 · rapporto 0.86 - 1.22
righe 265/334 · file 178 unita · max(line) 506 · 90 prima / 61 dopo
FAIL totale: 0 (27 controlli) · verify exit 0 (27 controlli)
sha256[:16] 1186c7b9ae462081 · copertura file 117/178 (65,7%)
```

## 5. Stato del progetto

```
TOTALE staging: 25408 unita · 814631 EN · 772240 IT
quarg missions.txt: 117/178 (65,7%) · 3 lotti
file completi: 39 · residuo traducibile (formula state.py): 6522
residuo misurato: 7097 unità / 161416 parole su 127 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (27 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 27 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: restano **61 unità** sulle righe 356–506 (`Ask Quarg About Coalition Late`), con
  **4 `UI_LABEL`**, **1 `LOGBOOK`** e **cinque token, due dei quali nuovi** (`<start planet>`, `<start system>`);
  prossimo contratto `HANDOFF_L105_20261018.md`, che chiude il file.
- **Nessuna revisione umana**.
