# REPORT — L74 · `data/successors/successor 2 ghosts aqrabe.txt`

## 1. Cosa contiene il lotto

**La proposta del giardino stellare** (unità 1–10). Tiliia ha studiato le pietre chiave: sono «oscillatori
che cantano all'unisono con le increspature del wormhole». Per amplificarne l'effetto servono **metalli
rari**, coltivati nei **giardini di metallo stellare** che orbitano attorno alla stella **Kasii-Cavaasa**,
dentro i **Tangles**. Quaranta tonnellate basterebbero a rifornire tutte le **Nuove Casate** e a rendere
obsoleta la corazza per attraversare i wormhole. La nave del giocatore, dicono, potrebbe farcela: gli scudi
avviseranno prima di cedere.

**L'immersione** (11–21). La nave protesta; gli allarmi suonano; lo scafo comincia a bruciarsi. Due scelte:
ritirarsi (14, 21: log del tentativo fallito) o insistere (15–18). Insistendo, **un'eruzione solare
vaporizza la nave e tutti a bordo** — il giocatore, Tiliia, i loro atomi «fra le stelle fredde e
indifferenti». La variante senza scudi (20) porta al **cedimento termico** e al rientro forzato.

**Il ritorno** (22–25). Tiliia sparisce nei dati per tutto il viaggio, poi sbarca e si fa circondare da
studiosi; chiede al giocatore di tornare allo spazioporto al tramonto. Il personale di terra commenta lo
scafo bruciacchiato. Si apre la missione del **Vujlet modificato** di Casa Kaatrij.

**Il verdetto e il prestito** (26–38). Nel giardino di statue Tiliia dà «notizie, una cattiva e una buona»:
la nave del giocatore non è adatta, ma **Casa Kaatrij** può prestare un **Vujlet** modificato — lo schema
sulla tavoletta mostra un congegno impiantato con viticci che si insinuano nei sistemi, forse un
**dispositivo di occultamento**. Tiliia sospetta che Kaatrij ne ricavi un favore da Aqrabe, e alla fine
aggiunge che Kaatrij vuole mandare **un osservatore**.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `stellar metal garden` | **giardino di metallo stellare** | «stellar metal» è un materiale, non un aggettivo: la resa lo tiene distinto dalla stella |
| `Kasii-Cavaasa`, `Tangles`, `Vujlet`/`Vujleten` | invariati | nomi di sistema, regione e nave |
| `New Houses` | **Nuove Casate** | coerente con `Casa X` / `Casate` fissati in L45 e L68–L73 |
| `quantum keystones` | **pietre chiave quantistiche** | forma fissa da L73 |
| `wormhole-crossing armor` | **corazza per attraversare i wormhole** | evita il calco «corazza attraversa-wormhole» |
| `thee / thy / hath / thou needest / 'tis` | «tu» moderno formale | regola fissata in L45–L47, verificata in L68–L73 |
| `(Retreat.)` ×2 | **(Ritirata.)** | stesso inglese, stessa resa: è un gruppo dichiarato |
| `(Press on.)` / `(Keep going.)` | **(Insisti.)** / **(Continua.)** | due inglesi distinti restano distinti |
| `no shields` | **identico** | nome di nodo di salto, in `NT` |
| `cloaking device` | **dispositivo di occultamento** | termine tecnico ricorrente nel gioco |
| `fleet liaison` | **ufficiale di collegamento con la flotta** | non «collegamento di flotta», che suona militare in modo diverso |
| `solar flare` | **eruzione solare** | termine corrente, non «brillamento» |

## 3. Difficoltà incontrate

1. **L'inglese arcaico di Tiliia** è più fitto che in L73 (`thou needest`, `hath`, `'tis`, `so what thinks
   thou?`). Reso con il «tu» moderno formale, come da regola: nessun «tu hai» arcaico, nessun «dèi».
2. **Due unità identiche** (12 e 16, `(Retreat.)`) in due missioni diverse: la tentazione è differenziarle
   per non «ripetersi». Sarebbe un errore — l'inglese è lo stesso e il giocatore vede lo stesso pulsante.
3. **Virgolette dispari assenti** qui (68, tutte pari) ma **quattro unità dispari in L75** (5–8): il
   controllo va riscritto là, non copiato da qui.
4. **Un `LOGBOOK` di forma diretta** (21) e una `label` (19) nello stesso lotto: due controlli positivi con
   forme diverse dallo stesso `raw`.
5. **Il finale catastrofico** (18) è una morte del giocatore raccontata in terza persona al presente: la resa
   mantiene il ritmo della frase lunga, senza spezzarla in frasi brevi.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   38/38
copertura del lotto               38/38
tab IT 28 / EN 28
virgolette IT 68 / EN 68
token IT 10 / EN 10
rapporto IT/EN 0.67 - 1.70
parole EN 1106 -> IT 1077
prima/ultima riga del segmento: 161/255
duplicati inglese: 1 gruppo (2 unita: 12, 16)
FAIL totale: 0                     (34 controlli)
verify.py exit 0                   (44 controlli)
sha256[:16] translation.json      3928a76816c49f89
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24503 unita · 782460 EN · 741608 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 78
```

`successor 2 ghosts aqrabe.txt` è coperto **89/180 (49,4%)**: restano **91 unità** dopo la riga 255.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (34 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (44 controlli) |

## 7. Errore mio, corretto prima di chiudere

Avevo scritto nel `verify.py` «94 unità dopo la riga 255». Il workspace dice **91** (180 − 51 − 38): lo
script è diventato rosso con la traduzione giusta, l'ho corretto sul numero misurato e non sul documento.
