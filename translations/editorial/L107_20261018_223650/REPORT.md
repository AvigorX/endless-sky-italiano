# REPORT — L107 · `korath missions.txt` (famiglia Korath verso il mondo ad anello, bestiame a sei zampe)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Setar Fort Heating` (coda) | 126–127 | 2 | lo scarico delle provviste, la folla intorno alle attrezzature, il pagamento |
| `Korath Family to Ringworld` | 130–169 | 17 | la foschia di Laki Nemparu, i 500 crediti, il rifiuto, il viaggio, la riunione, il Quarg che traduce |
| `Korath Livestock` | 172–212 | 19 | il vicolo, i tre Korath, le «pecore» a sei zampe, i 10.000 crediti col gesso, la lana venduta |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Korath to <planet>` · `Livestock to <planet>` | **identici** | nomi di missione (`VALUE`), con un token dentro |
| `A Korath family of <bunks>` | **Una famiglia Korath di <bunks> persone** | `<bunks>` è un **numero**: in italiano regge «di … persone» |
| `Kor Efret` (singolare) | **Kor Efret** | il sorgente usa il singolare, il plurale è `Kor Efreti` |
| `smog` | **foschia** | *smog* industriale, non nebbia: reso con il termine che dice sporco |
| `soot` | **fuliggine** | |
| `hiss approvingly` | **sibilano in segno di approvazione** | i Korath sibilano, non parlano |
| `Kor Efret` `coughing fit` | **accesso di tosse** | |
| `bunks` (cuccette della nave) | **cuccette** | distinto dal token `<bunks>` = posti |
| `You show them to their bunks... and the shower.` | **Li accompagnate alle loro cuccette... e alla doccia.** | i puntini sono **tre punti** del sorgente, non ellissi tipografica |
| `pridefulest` | **orgogliosissimo** | superlativo sbagliato ma trasparente |
| `indebted translation` | **traduzione debitrice** | calco del parlato storto |
| `happyfully` | **felicemente** | avverbio giusto al posto di quello inventato: il Quarg sbaglia **lessico**, non morfologia |
| `vicinitied … absenced` | **sarebbe vicinata … fosse stata assenziata** | verbi inventati da *vicino* e *assente* |
| `gaggle` | **accozzaglia** | |
| `camaraderie` | **camerataggine** | |
| `in fateful service to our camaraderie` | **in servizio fatidico alla nostra camerataggine** | ordine storto conservato |
| `The rusting buildings` | **Gli edifici arrugginiti** | |
| `five times larger, six legs` | **cinque volte più grandi, sei zampe** | |
| `brown-black colors` | **colori bruno-neri** | |
| `huddled in small groups` | **accalcate in piccoli gruppi** | |
| `bleat` | **belano** | |
| `muggers` | **rapinatori** | |
| `paper map` | **mappa di carta** | |
| `tarps` | **teli** | |
| `straw` | **paglia** | |
| `space sickness` | **mal di spazio** | |
| `one-jump trip` | **viaggio di un salto** | |
| `climate-controlled ship` | **nave a clima controllato** | |

## 3. Difficoltà

1. **Il Quarg che parla male (unità 16)** è il nodo editoriale del lotto: quattro virgolette, due discorsi
   annidati, e un inglese **deliberatamente storpiato**. La regola adottata: **parole inventate ma trasparenti**
   (`vicinata`, `assenziata`, `camerataggine`, `sproporzionatamente`), sintassi storta, nessuna perdita di
   comprensibilità. Il narratore conferma che il Quarg parla male, quindi la resa non è una scelta arbitraria.
2. **`(No.)` = `(No.)`**: l'unità 10 è **identica** al sorgente per coincidenza linguistica, come l'unità 3 di
   L104. Eccezione **nominata** nel `check.py` e nel `verify.py`, non permesso generico.
3. **Due `VALUE` identici e due `DESCRIPTION` tradotte** nello stesso lotto: le regole sono opposte e vanno
   scritte **per indice** (3 e 20 identici; 4 e 21 tradotti).
4. **`<bunks>` in un `DESCRIPTION` e in un `MISSION_TEXT`**: il token indica un numero di posti, e in italiano
   regge «di <bunks> persone» — ma solo se resta **un numero**, mai una parola.
5. **Token `<bunks>` distinto da `<tons>`**, entrambi nell'unità 31: posti letto contro carico. Il `check.py`
   verifica le **famiglie** separatamente e l'unità che li contiene entrambi.
6. **Zero quadre, zero citazioni aperte, zero ripetizioni**: tutte e tre le assenze sono **asserite vuote** — il
   lotto precedente aveva 16 coppie di quadre e una citazione aperta, e un controllo copiato avrebbe reso rosso
   un lotto corretto.
7. **Il confine è un `phrase:`** e non un `mission:`: nel `verify.py` l'asserzione è sull'intera tupla
   `(216, 'phrase:kor efret small package offer')`.

## 4. Numeri osservati

```
unita' 38/38 · 34 MISSION_TEXT + 2 VALUE + 2 DESCRIPTION · tab 29 · virgolette 20 = 20 (tutte binate)
token 21 = 21 in sei famiglie (<planet> 12, <bunks> 3, <payment> 2, <destination> 2, <cargo> 1, <tons> 1)
quadre 0 · citazioni aperte 0 · ripetizioni 0 · identiche: 3, 20 (VALUE) + 10 (No.)
parole EN 1742 -> IT 1683 · rapporto 0.79 - 1.29
righe 126/212 · file 158 unita · max(line) 580 · 25 prima / 95 dopo
FAIL totale: 0 (27 controlli) · verify exit 0 (30 controlli)
sha256[:16] 0c901ea4867f63e3 · copertura file 63/158 (39,9%)
```

## 5. Stato del progetto

```
TOTALE staging: 25532 unita · 819382 EN · 776829 IT
korath missions.txt: 63/158 (39,9%) · 2 lotti
file completi: 40 · residuo traducibile (formula state.py): 6398
residuo misurato: 6977 unità / 156673 parole su 126 file
avanzamento: 25532/32924 unità (77,5%) · 819382/979975 parole (83,6%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (30 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 38 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: 95 unità su 10 contesti; prossimo contratto `HANDOFF_L108_20261018.md` (righe
  216–335), che contiene il blocco `phrase:` composto a frammenti.
- **Nessuna revisione umana**.
