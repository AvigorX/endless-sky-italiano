# REPORT — L75 · `data/successors/successor 2 ghosts aqrabe.txt`

## 1. Cosa contiene il lotto

**La consegna del Vujlet** (unità 1–15). Il giocatore torna a **Kasii-Cavasaa-Oa**, dove lo spazioporto è
sotto un temporale e le sporgenze «simili a vele» grondano acqua. In un hangar a cupola lo aspetta il Vujlet
di Casa Kaatrij, con una **sfera di dati** che rigurgita il messaggio di **K- I- Saajret, di Somber Sejra**:
la nave è un dono in amicizia, e la firma si ripete due volte (unità 5–6 e 7–8, con due varianti della
lettera). A bordo c'è l'**osservatore** di Kaatrij: non un archivista ma un soldato, con fucile cinetico, che
risponde alle domande senza emozione. L'interno delle navi militari Successor è descritto: plancia sepolta
sotto strati di corazza, vasca d'acqua al centro, display in metallo liquido.

**La nuova corazzatura** (16–26). Nella baia enorme di `<planet>` il Vujlet viene ri-corazzato da braccia
metalliche e droni; la corazza «per attraversare il wormhole» è la più complicata. Tiliia invita il giocatore
nel **giardino di statue**.

**Il giardino e la tradizione** (27–53). Qui Tiliia parla della **tradizione di famiglia**: nell'ultima ora
di vita, i figli decidono per il genitore un compito — un'opera, un viaggio, un cambiamento di sé. Il compito
che Tiliia ha scelto per il proprio genitore maggiore sono **le statue del giardino**. Segue la domanda del
giocatore sul perché rischiare, e — se il giocatore solleva il tema — la risposta amara sui **Successori che
non si sono comportati bene con tutti**: Tiliia trattiene la rabbia e torna al colore neutro. In ogni ramo,
il congedo è lo stesso: «raggiungici allo spazioporto quando sei pronto».

**La partenza** (54–61). Si apre la missione del **secondo giardino**, con `<capacity>` e `<system>`; nella
baia, Tiliia e l'osservatore stanno litigando («...sciocco fidarsi di un alieno»), poi l'osservatore avverte:
la corazza protegge dal calore «ma poco altro», e nei **Tangles** non conviene indugiare.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `Kasii-Cavasaa-Oa` | invariato | nome della stazione, scritto così nel sorgente |
| `Kasii-Cavaasa` | invariato | nome della stella (L74): **non** unifico le due grafie |
| `K- I- Saajret`, `Somber Sejra`, `Nnesa ti-a-Oj` | invariati | nome, luogo, nave |
| `data-sphere` | **sfera di dati** | forma già in staging (L71–L72) |
| `archivist` | **archivista** | l'osservatore non lo è, e il testo gioca su questo |
| `martial craft` | **nave da guerra** | non «nave marziale», calco |
| `liquid-metal displays` | **display in metallo liquido** | descrizione tecnica, non metafora |
| `re-armoring` | **nuova corazzatura** | «ri-corazzatura» non esiste in italiano |
| `waves upon the bright shore` | **onde sulla riva luminosa** | immagine ripetuta due volte: resa identica |
| `scions` / `trinket` | **eredi** / **ninnolo** | forme fisse da L70–L72 |
| `the People's Houses` | **le Casate del Popolo** | forma fissa da L45 |
| `diff'rent`, `others've`, `t'accomplish`, `'twas`, `'twouldn't` | forme piene | l'elisione colloquiale non ha equivalente italiano che non suoni dialettale |
| `hast thou?.` | «vero?.» | la punteggiatura doppia dell'inglese è **riprodotta**, non corretta |

## 3. Difficoltà incontrate

1. **Due battute spezzate a metà frase** (5–6, 7–8): quattro unità con **una sola virgoletta** ciascuna. La
   tentazione è chiudere le virgolette in ogni unità — sarebbe un errore: il gioco le mostra in sequenza, e
   la frase si chiude solo alla seconda. Il `verify.py` confronta l'**insieme** degli indici e **dove** chiude.
2. **La firma ripetuta** (6 e 8) è un duplicato inglese legittimo: stessa resa, dichiarata come gruppo.
3. **`LOGBOOK` = sola categoria** (27): qui **non** c'è testo da tradurre, perché `log` ha tre argomenti e
   l'estrattore prende il primo. È l'**ottavo** caso della lacuna, e il primo in cui il lotto non contiene
   nemmeno una riga di diario tradotta.
4. **Due grafie dello stesso sistema** (`Cavaasa` in L74, `Cavasaa-Oa` qui): non le unifico — il sorgente le
   distingue e la stazione ha un nome diverso dalla stella.
5. **L'inglese arcaico è al massimo** in questo lotto (`thou'rt`, `shalt`, `mayst`, `shouldst`, `'tisn't`):
   reso con il «tu» moderno formale senza perdere la solennità.
6. **Un ramo con contenuto politico** (45–48): il giocatore accusa i Successori; Tiliia trattiene la rabbia.
   La traduzione non ammorbidisce né inasprisce.

## 4. Numeri osservati (output letto)

```
unita' tradotte nell'intervallo   61/61
copertura del lotto               61/61
tab IT 51 / EN 51
virgolette IT 130 / EN 130
virgolette dispari: (5, 6, 7, 8) in inglese e in italiano
token IT 8 / EN 8   (7 famiglie)
rapporto IT/EN 0.72 - 1.48
parole EN 1889 -> IT 1796
prima/ultima riga del segmento: 259/400
duplicati inglese: 1 gruppo (6, 8)
FAIL totale: 0                     (37 controlli)
verify.py exit 0                   (47 controlli)
sha256[:16] translation.json      83744e86d2da8682
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24564 unita · 784349 EN · 743404 IT
APPROVED 364 · PENDING 32560 · totale 32924
lotti con translation.json: 79
```

`successor 2 ghosts aqrabe.txt` è coperto **150/180 (83,3%)**: restano **30 unità** dopo la riga 400.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (37 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (47 controlli) |

## 7. Un controllo mio, troppo largo

Il primo `verify.py` pretendeva che la virgoletta chiudesse **solo** nelle unità 6 e 8, ma confrontava
l'elenco di **tutte** le unità che finiscono con `"`. In un dialogo fitto quasi ogni battuta finisce così:
il controllo è diventato rosso con la traduzione giusta. L'ho ristretto alle **quattro unità dispari**, dove
la domanda ha senso, ed è tornato verde.
