# REPORT — L262 (`data/remnant/remnant jobs.txt`, righe 226–490)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 29 (9 `DIALOG` + 8 `VALUE` + 7 `DESCRIPTION` + 5 `MISSION_TEXT`) | 29 |
| parole | 423 | **439** (1,04) |
| tab / virgolette | 0 / 0 | 0 / 0 |
| apici | 1 | 8 |
| segnaposto | 43 in 5 famiglie | 43, **stesso ordine per unità** |
| contesti | 9 | 9 |

Rapporto per unità **0,95 – 1,34**: nessuna resa fuori gate.

## 2. I nove contesti, in sequenza

```
226, 231            Bounty 4
238, 239, 262, 264, 267   Bounty 5
272, 273, 292       Logistics Civil Engineering
299, 300, 319       Logistics Industrial Delivery
326, 327, 347       Logistics Outfitter Delivery
354, 355, 375       Logistics Salvage Delivery
383, 384, 411, 414  Rescue
452, 453, 475, 480, 483   Rescue 1B
490                 Rescue 2   ← il VALUE che apre la missione; si chiude in L263
```

L'ultima unità del lotto è **un'apertura**, non una chiusura: la missione `Rescue 2` continua e il confine (riga 491) resta
nello **stesso** contesto. Il `verify.py` lo asserisce esplicitamente, perché «ultima unità del lotto» non significa
«missione finita».

## 3. Il riuso da L261 (controllo cross-lot)

Le unità **1** e **2** ripetono stringhe già tradotte:

| unità | inglese | resa (ripresa da L261) |
|---|---|---|
| 1 | `You have destroyed the Korath ship. You can now return to <planet> to collect your payment.` | «Hai distrutto la nave Korath. Ora puoi tornare su `<planet>` per riscuotere il pagamento.» |
| 2 | `A Remnant military leader thanks you for hunting down the Korath ship <npc>, and gives you the agreed-upon payment of <payment>.` | «Un comandante militare dei Remnant ti ringrazia per aver dato la caccia alla nave Korath `<npc>` e ti consegna il pagamento concordato di `<payment>`.» |

Il `check.py` **rilegge** `staging/editorial/L261_20261020_161448/translation.json` e pretende l'identità carattere per
carattere. È l'unico controllo del lotto che dipende da un altro lotto: senza di esso due rese diverse della stessa frase
passerebbero entrambe i controlli locali.

## 4. `Ember Waste` resta inglese

| inglese | italiano |
|---|---|
| `…outposts in the Ember Waste` | «…avamposti nell'**Ember Waste**» |

Il nome della regione compare **3** volte nel lotto e **13** volte nel corpus, **sempre invariato**. Il test vieta
esplicitamente qualunque resa («Brace», «braci»), che sarebbe un'invenzione: nessun testo del gioco la usa.

## 5. Le quattro famiglie di lavori logistici

| missione | scheda | battuta |
|---|---|---|
| Civil | «Gli ingegneri su `<planet>` hanno bisogno di una consegna di `<cargo>`. Il compenso logistico è `<payment>`.» | «Un ingegnere di progetto ispeziona `<cargo>` e autorizza il tuo pagamento di `<payment>`.» |
| Industrial | «Le squadre di progetto su `<planet>`…» | «Un tecnico di progetto ispeziona `<cargo>` e approva…» |
| Outfitter | «Le squadre di riparazione dell'emporio su `<planet>`… pezzi `<cargo>`…» | «Un tecnico delle riparazioni ispeziona i pezzi `<cargo>`…» |
| Salvage | «Consegna i componenti `<cargo>` delle recenti operazioni di recupero agli empori su `<planet>`, per studio, ripristino o riciclaggio…» | «Due tecnici delle riparazioni armati ispezionano `<cargo>`…» |

Le quattro formule sono **parallele ma non identiche**: cambia il soggetto (ingegneri, squadre di progetto, squadre di
riparazione dell'emporio, operazioni di recupero), e ognuna ha la sua resa. Il `check.py` verifica che i **gruppi identici**
abbiano una sola resa e che le quattro varianti **non** siano state appiattite su una sola.

## 6. La sottotrama del soccorso

`Rescue` e `Rescue 1B` hanno la **stessa** `DESCRIPTION` («La `<npc>` è scomparsa durante una missione di ricognizione
nell'Ember Waste. Trovala e aiutala a tornare su `<destination>`.») e la **stessa** battuta di ritorno a vuoto («Sei tornato,
ma la `<npc>` risulta ancora dispersa.»). La differenza arriva nelle `MISSION_TEXT`: in `1B` la nave **è distrutta** e il
testo diventa quello del lutto («Passi le ore successive a cercare affannosamente superstiti, con la speranza che affonda
minuto dopo minuto», «riferisci che la `<npc>` è andata perduta con tutto l'equipaggio»).

## 7. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   25 prima · 29 qui · 33 dopo la 490 · copertura 54/87 (62,1%)
```

Un rosso al primo giro, nel `check.py`: il controllo sulle fazioni cercava `Remnant` nell'unità 4 — la scheda della taglia,
dove il nome **non c'è** (dice «avamposti» e «Ember Waste»). Corretto il riferimento (unità 2 e 27), non l'asserzione. È la
**seconda volta** in due lotti (dopo L260 con `Gus`): un nome «presente nel lotto» non è un nome «presente dove lo cerco».

Nello stesso giro ho corretto, **prima** di eseguire, un controllo su `<cargo>` scritto con un gruppo regex **opzionale**:
`(?:\bdi |\bil )?<cargo>` corrisponde sempre, quindi non poteva fallire.

## 8. Due `verify.py` corretti dopo la batteria

La batteria globale ha dato **`ROSSO L261/verify.py`**: il suo controllo di copertura asseriva `len(righe) == 25` — cioè la
copertura **totale del file**, che con questo lotto è diventata 54. È la **sesta** recidiva della stessa trappola (L46→L47,
L233/L234, L235, L256→L257, ora L261→L262): riscritta sull'invariante di segmento.

**Lo stesso difetto era già nel `verify.py` di questo lotto** (`len(righe) == 54`): corretto **subito**, senza aspettare che
diventasse rosso con L263. Batteria: **`verificati=264 rossi=0`**.

## 9. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 29 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 54/87; restano 33 unità su quattro missioni.
