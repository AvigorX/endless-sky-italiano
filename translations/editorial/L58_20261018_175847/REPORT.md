# REPORT — L58 · `data/human/culture conversations.txt` (righe 25–209)

**Esito: CHIUSO.** 43/43 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

Nove **micro-scene** autonome, tutte `MISSION_TEXT`, tutte sulla vita quotidiana nei mondi umani:

| Contesto | Unità | Scena |
|---|---|---|
| `Sad Gamblers - Republic` | 1–2 | Una vincita di dodicesima categoria reinvestita subito in biglietti |
| `Sad Gamblers - Syndicate` | 3–4 | **Testo identico** alla precedente: stessa scena, fazione diversa |
| `Foiled Kidnapping Witnessed` | 5–6 | Posto di blocco, una bambina trovata nel bagagliaio |
| `Gift Store Interaction` | 7–14 | La tazza da 50 crediti: tre esiti (comprare, rimettere, non potersela permettere) |
| `New China Mourners` | 15–16 | Un funerale sotto la pioggia, il corteo, gli addetti con le pantofole |
| `New Holland Foibles` | 17–27 | La città-fabbrica, la nave smontata, l'operaio che rivendica la sicurezza del cantiere |
| `Trash Fire Crops` | 28–32 | L'odore di banane bruciate: raccolto record, mercato inesistente |
| `Worker's Occasion` | 33–40 | L'operaio davanti al menù: offrire, compatire, sorridere |
| `Paradise Cleaner Incident` | 41–43 | La donna delle pulizie e il mocio rovesciato davanti a una famiglia benestante |

## 2. Le scelte di traduzione che contano

**Il registro è quotidiano e basso, non epico.** Il lotto non ha combattimenti né cerimonie: ha un
negozio di souvenir, un ristorante, un cantiere. La sintassi italiana resta piana, con periodi brevi dove
l'inglese li ha. Nessuna inversione cerimoniale: quella appartiene ad Adrauni (L56–L57) e qui sarebbe
fuori registro.

**La classe sociale è il tema, e si rende con il lessico, non con il commento.** «a local worker with a
small handful of credits» → «un operaio locale con un pugno di crediti»; «his clothes are neatly worn and
look freshly brushed» → «i suoi vestiti sono consumati con ordine e sembrano appena spazzolati». Le
macchie che non vanno via restano macchie: non diventano «povertà».

**«Nowhere else is class such an ingrained component of daily life»** (unità 41) → «In nessun altro
luogo la classe è una componente così radicata della vita quotidiana». È la frase-tesi del lotto e non va
ammorbidita.

**Il caposquadra** (unità 22, 25) parla per frasi brevi e imperativi: «Oi you, piss off» → «Ehi tu, levati
di torno»; «we don't need your nose in our business» → «non ci serve il tuo naso nei nostri affari». Il
«Senti, straniero» traduce «Look stranger», che è un vocativo, non un'ingiunzione.

**«piss off» e «where you can stick that offer in colorful terms»** (unità 39): resi senza volgarità
esplicita — «dove puoi ficcarti quell'offerta» — perché il testo inglese allude e non nomina.

**`Rik`** (unità 25) resta invariato. **`Deep`** resta invariato: è una regione, non un aggettivo.

## 3. Difficoltà

- **Nessuna.** Il lotto è tecnicamente semplice: 0 `UI_LABEL`, 0 token, 0 virgolette dispari, 0 quadre.
  Il rischio era **solo** di registro, e i controlli non lo vedono: la verifica automatica dice che i
  simboli sono intatti, non che la voce è giusta.
- **I 3 gruppi di duplicati inglesi** (1/3, 2/4, 21/24) sono ripetizioni reali del sorgente
  (due fazioni, due scelte identiche): la resa è identica e il controllo la asserisce.
- **Il rapporto per unità** ha un minimo di 0,82 e un massimo di 1,40: nessun outlier da giustificare.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 35 controlli · exit 0
             unita 43 · righe 25-209 · 0 prima / 331 dopo · file 374 · max(line) 1122
             tipi 43 MISSION_TEXT · NT/DIALOG/LOGBOOK/CONVERSATION/TEXT 0 (assenze dichiarate)
             token 0 / 0 · tab 34 / 34 · virgolette 8 / 8 · dispari 0
             rapporto 0,82 - 1,40 · duplicati 3 gruppi (6 unita)
             parole 1.610 EN -> 1.532 IT
             sha256 translation.json 0a66e11210f15963…
```

## 5. Stato del progetto dopo L58

| Voce | Prima (L57) | Dopo L58 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 23.829 | **23.872** |
| Lotti con `translation.json` | 61 | **62** |
| `culture conversations.txt` | 0/374 | **43/374** |

Nessuna scrittura su `state.db`: le 43 unità restano `PENDING`.

## 6. Prossimo passo

**L59**: righe **225–423**, **42 unità**, 12 contesti, primo `Curious Waiter`, ultimo `Sojourn Sunday
Sales`. Non chiude il file (restano 289 unità dopo la 423).
