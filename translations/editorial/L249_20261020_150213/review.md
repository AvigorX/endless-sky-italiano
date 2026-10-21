# review.md — L249 (`data/human/syndicate jobs.txt`, righe 291–431)

Registro delle decisioni editoriali del **terzo lotto** di `syndicate jobs.txt`: la ripetizione di una missione, quattro nomi
di lavoro e tre trasporti di prigionieri.

## 1. Che cosa si copia, che cosa si riprende, che cosa si traduce

| tipo | unità | trattamento |
|---|---|---|
| `VALUE` | 4 | **copiato** dall'inglese |
| `DIALOG` + `DESCRIPTION` con inglese già in L248 | **9** | **ripresi alla lettera** dal `translation.json` di L248 |
| `DIALOG` + `DESCRIPTION` nuovi | 6 | **tradotti** in questo lotto |

Le 19 unità contengono **15 stringhe distinte**: 6 vengono da L248, 9 sono nuove. Il `verify.py` verifica **entrambi** i
numeri.

## 2. Le sei unità nuove

| unità | inglese | resa |
|---|---|---|
| 12 | `Transport an indicted white-collar criminal with his assistants, lawyers, and collection of <cargo>… under "house arrest."` | «Trasporta un criminale dai colletti bianchi incriminato, con i suoi assistenti, i suoi avvocati e la sua collezione di `<cargo>`, su `<planet>`, dove attenderà il processo agli "arresti domiciliari".» |
| 13 | `The executive strolls off your ship with a sunny smile…` | «Il dirigente esce dalla tua nave con un sorriso radioso sul volto. Uno degli avvocati ti consegna il pagamento di `<payment>` mormorando minacce di querele per diffamazione…» |
| 15 | `Transport a convicted industrial saboteur to <planet> for their sentence…` | «Trasporta un sabotatore industriale condannato su `<planet>` per scontare la pena. Deve essere custodito in strutture adatte al trasferimento dei criminali.» |
| 16 | `A group of guards carry the prisoner off your ship more roughly than is strictly necessary.` | «Una squadra di guardie porta il prigioniero giù dalla tua nave con più rudezza del necessario. Ricevi il pagamento di `<payment>`.» |
| 18 | `Transport a group of <bunks> convicted corporate spies to <planet> for their sentences.` | «Trasporta un gruppo di `<bunks>` spie aziendali condannate su `<planet>` per scontare le loro pene. Devono essere tenute in strutture adatte al trasferimento dei criminali.» |
| 19 | `A group of guards lead the prisoners off your ship, chained together at the ankles.` | «Una squadra di guardie porta via i prigionieri dalla tua nave, incatenati insieme alle caviglie. Ricevi il pagamento di `<payment>`.» |

## 3. Il genere, dove il testo non lo dice

| inglese | italiano | nota |
|---|---|---|
| `for their sentence` (sabotatore) | «per scontare **la pena**» | «their» è neutro: si evita il pronome e si usa il sostantivo |
| `They must be held in suitable facilities` (spie) | «**Devono essere tenute** in strutture adatte» | «spie» è femminile, l'accordo c'è ed è **verificato** |
| `They must be held` (sabotatore) | «**Deve essere custodito**» | «sabotatore» è maschile |

## 4. La ripetizione come fatto verificabile

Nove unità esistevano già in L248. Invece di riscriverle, il generatore le legge **dal file di L248**; e il `verify.py`
**rilegge quello stesso file** e confronta:

- **10 unità** ripetono una stringa presente in L248 (contando il `VALUE`);
- **nessuna** differisce;
- **6** delle **15** stringhe distinte vengono da L248, **9** sono nuove.

Questo è il tipo di controllo che in L244 sarebbe servito e non c'era: là una nota ripetuta era stata tradotta «bene» invece
di copiata, e il difetto è emerso solo due lotti dopo.

## 5. Lessico

| inglese | resa | nota |
|---|---|---|
| `house arrest` | **arresti domiciliari** | già nel corpus; fra virgolette quando il testo le usa |
| `white-collar criminal` | **criminale dai colletti bianchi** | |
| `saboteur` | **sabotatore** | |
| `corporate spies` | **spie aziendali** | |
| `chained at the ankles` | **incatenati insieme alle caviglie** | |
| `facilities made for the transfer of criminals` | **strutture adatte al trasferimento dei criminali** | |
| `libel lawsuits` | **querele per diffamazione** | |
| `sunny smile` | **sorriso radioso** | |
| `You receive your payment of <payment>.` | **«Ricevi il pagamento di `<payment>`.»** | forma del corpus (non «incassi»: l'inglese dice `receive`) |

## 6. Struttura e differenze fra le due lingue

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **2** (unità 12) | **2** (unità 12, «"arresti domiciliari"») |
| apici | **2** (unità 2 e 8, `You'll`) | **0** — la resa è «Dovrai», senza apostrofo |

La differenza sugli apici è **dichiarata**, non lasciata implicita: è il caso in cui l'italiano è più corto, perché il
futuro italiano non ha bisogno dell'apostrofo.
