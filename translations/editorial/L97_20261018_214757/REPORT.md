# REPORT — L97 · `coalition culture conversations.txt` (chiude il file)

## 1. Contenuto

Ultimo segmento, righe 251–462, sette contesti:

- **Departing Trouble - A** (1–5): la partenza, le navi civili inseguite, le Heliarch che passano vicine; tre
  varianti dello stesso momento (una con l'Interdictor che si scusa, una con il pensiero del Lunarium);
- **Departing Trouble - B** (6–11): le navi civili che esplodono, l'abbordaggio delle superstiti, il saluto di
  una nave Heliarch; il pensiero dei capi del Lunarium a bordo;
- **Departing Trouble - C** (12–17): lo schermo di navi da guerra intorno a `<origin>`, l'ispezione di un
  **Punisher** con gli agenti che mettono la nave sottosopra, e le due varianti (con o senza il sospetto di
  cimici);
- **Incident: Secret Sky** (18–23): il capitano Arach e il passeggero Kimek scomparso;
- **Incident: Hunger Tower** (24–26): la protesta per il convoglio mancante e i droni che distribuiscono i pasti;
- **Incident: Arach Store** (27–29): la confisca e la distruzione dei capi ritenuti illegali;
- **Incident: Ring of Wisdom** (30–36): l'allarme, la quarantena, il Saryd che spara nel passaggio e crolla.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| sintassi Heliarch | **ordine marcato italiano** | «Un'ispezione di routine, stiamo facendo»: stessa voce dei Kimek/Saryd/Arach |
| `Interdictor` / `Punisher` | **invariati** | nomi di classe di nave |
| `hunger tower` | **torre della fame** | è il nome dell'edificio e del contesto |
| `gurney` | **barella** | non «lettiga»: è attrezzatura ospedaliera |
| `body bag` | **sacco per cadaveri** | il testo è esplicito, non va edulcorato |
| `keep tabs within your ship` | **tenervi d'occhio** | idiom, non «tenere schede» |
| `off'rings`-tipo | — | non presente qui |
| `"cooperating,"` / `"cooperating",` | **`"collaborazione,"` / `"collaborazione",`** | le due unità differiscono per la virgola: riprodotta, non uniformata |

## 3. Difficoltà

1. **Quattordici token**: `<origin>` ×8, `<ship>` ×5 e **`<last>` ×1** — quest'ultimo compare solo qui e il
   gioco ci mette il cognome del giocatore. Verificati **per unità**, nello stesso ordine.
2. **Ripetizione tripla 7/9/11** (l'abbordaggio): resa identica, scritta da una costante unica.
3. **Le varianti 15/17 differiscono per la virgoletta e la virgola**: `"cooperating,"` contro `"cooperating",`.
   Uniformarle sarebbe una «pulizia» che cambia due unità distinte; il `check.py` asserisce la differenza.
4. **Sette contesti in un lotto**: i tre `Departing Trouble` sono varianti della stessa scena e vanno letti
   insieme, altrimenti si traduce due volte la stessa cosa con parole diverse.
5. **`verify.py` di chiusura**: legge i `translation.json` di **tutti e cinque** i lotti del path e asserisce
   157 id distinti, 0 sovrapposizioni, 31+36+27+27+36.

## 4. Numeri osservati

```
unita' 36/36 · tab 29 · virgolette 24 = 24 · token 14 = 14 (<origin> 8, <ship> 5, <last> 1)
parole EN 2269 -> IT 2142 · rapporto 0.85 - 1.26
righe 251/462 · file 157 unita · max(line) 462 · 121 prima / 0 dopo
FAIL totale: 0 (30 controlli) · verify exit 0 (29 controlli)
sha256[:16] cc6086592132277e · file 157/157 · 5 lotti · 9964 EN -> 9138 IT
```

## 5. Stato del progetto

```
TOTALE staging: 25144 unita · 806366 EN · 764348 IT
coalition culture conversations.txt: 157/157 (100%) · 5 lotti · CHIUSO
file completi: 38 · residuo traducibile (formula state.py): 6786
residuo misurato: 7358 unità / 169675 parole su 128 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (29 controlli), invariante di file 157/157 |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 36 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il file è chiuso, la campagna no**: restano **7.358 unità / 169.675 parole** su **128 file**; il prossimo
  contratto è `HANDOFF_L98_20261018.md` (`hai culture conversations.txt`, righe 1–105).
- **Nessuna revisione umana**.
