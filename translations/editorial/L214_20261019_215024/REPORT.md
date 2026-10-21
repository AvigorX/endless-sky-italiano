# REPORT — L214 · `deep jobs.txt` (terzo lotto)

## 1. Contenuto

Trentacinque unità che chiudono il filone del **pacco sicuro** e aprono la sua conseguenza narrativa. Prima la consegna
con sei destinatari diversi (reception di un'azienda tecnologica, addetto alla sicurezza annoiato, negozio di curiosità,
agente in borghese, signora su una panchina, capitano ai moli), poi cinque missioni di trasporto identiche, e infine la
**rivelazione**: un agente della **Deep Security**, **Wayde**, ferma il giocatore su una panchina e gli spiega che una
parte di quei pacchi era sua.

## 2. Difficoltà

1. **I tab sono struttura, non spaziatura.** Quindici tab, uno per unità, aprono i paragrafi dei testi di missione. Il
   controllo li verifica per unità e in posizione iniziale: un tab rimosso cambierebbe l'impaginazione, e un tab interno
   sarebbe un errore invisibile a occhio nudo.
2. **La preposizione va nell'alternativa.** *Deliver the package to* + *the reception counter*: in inglese la preposizione
   è già nel frammento d'apertura e non cambia; in italiano dipende dal genere della destinazione, quindi deve stare
   dentro le sei alternative («alla reception», «a un addetto», «a un negozio», «a un agente», «a una signora», «a un
   capitano»). Se fosse rimasta nell'apertura, cinque frasi su sei sarebbero sgrammaticate.
3. **Le sei alternative devono restare sei.** Il controllo verifica che le rese siano tutte diverse: due destinatari
   identici sarebbero una variante persa.
4. **Il registro unico «tu» incontra la cortesia.** Wayde è formale («allow me to take a moment of your time»), ma la
   campagna usa un solo registro. La scelta è «Accomodati e concedimi un momento del tuo tempo», e il controllo verifica
   che «Lei» e «Si accomodi» **non** compaiano. È una perdita consapevole: la cortesia inglese si trasforma in cordialità.
5. **Il confine è un `UI_LABEL`**, il primo della campagna: un tipo che non entra mai in staging. Il `verify.py` lo dice
   esplicitamente con un'asserzione negativa («nessun `UI_LABEL` nel lotto»), così il lotto successivo non lo cerca.

## 3. Numeri osservati

```
unita' 35 · {'MISSION_TEXT': 16, 'TEXT': 8, 'VALUE': 5, 'DESCRIPTION': 5, 'LOGBOOK': 1} · tutte PENDING
15 tab (uno per unita' nelle 21-35) · 22 virgolette (2 x 11) · 6 apici EN / 6 IT · 16 segnaposto su 3 simboli
7 contesti · righe 457/682 · 67 prima · 85 dopo · confine riga 683 (UI_LABEL)
parole 431 -> 430 · rapporto 0.74 - 1.51 (media 1.07)
FAIL totale: 0 (26 controlli) · verify exit 0 (19 controlli) · sha256[:16] e2d9f07af3bd3c95
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26), `verify.py` exit **0** (19) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 35 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna missione giocata**: l'impaginazione dei 15 tab non è stata vista a schermo, e la perdita della cortesia di
  Wayde è una scelta dichiarata, non un risultato verificabile con un test.
- **Restano 85 unità** nel file, di cui 1 `UI_LABEL` già incontrato al confine.
