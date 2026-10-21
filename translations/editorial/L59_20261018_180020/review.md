# REVIEW — L59 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli: scelte, dubbi dichiarati, rischi per chi prosegue.

## 1. Coerenza con L58

- **Stesso narratore** (seconda persona, presente, osservativo) e stesso registro quotidiano. Nessuna
  deriva cerimoniale.
- **Continuità tematica**: L58 finiva con la classe sociale allo spazioporto di Paradise; L59 la riprende
  nella scena finale (`Sojourn Sunday Sales`), dove le vacanze in svendita restano inaccessibili a chi non
  ha reddito da pilota. La resa di «a younger you» mantiene il riferimento al passato del personaggio.
- **Il lessico di L58 è stato rispettato**: «spazioporto» (non «porto spaziale»), «hangar», «crediti»,
  «Deep» invariato.

## 2. Nodi traduttivi aperti (dichiarati)

- **«katsu don»** (1): invariato. Se in futuro il glossario decidesse di tradurre i nomi dei piatti, va
  cambiato in entrambi i lotti del file.
- **«Tonner/Tonners»** (12): invariato e fra virgolette. La forma plurale inglese è nel sorgente; non è
  stata «italianizzata» perché è il nomignolo usato dai locali.
- **«retardants»** (32, 33): «ritardanti». È il termine tecnico corretto; «estinguenti» sarebbe più
  generico e meno preciso rispetto a un prodotto chimico sganciato dall'alto.
- **«overlords»** (35): «signori», fra virgolette. La scelta è deliberata: «signori» è più sinistro di
  «padroni» in questo contesto, perché è la parola che userebbe chi vuole compiacere.
- **«sending a message to a local»** (27): «manda un messaggio a un locale». «Locale» come sostantivo
  (abitante) è accettabile in italiano ma lievemente ambiguo con «locale» = esercizio commerciale. Nel
  contesto della frase non c'è ambiguità; va segnalato perché è l'unico punto del lotto in cui il
  doppio senso esiste in italiano e non in inglese.

## 3. Duplicati

**Nessuno.** È il primo lotto della serie con 0 gruppi duplicati. Il controllo `duplicati italiano non
spiegati dal sorgente` resta verde per costruzione, e in `verify.py` c'è un'asserzione **negativa**
esplicita (`len(dup_en) == 0`): senza di essa, «nessun duplicato» e «controllo non eseguito» sarebbero
indistinguibili nel referto.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 42 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime** delle due scene con scelte (18/19 e 25/26): il testo c'è, l'esito nel
  gioco no.

## 5. Rischi residui

- **Il file è aperto a 85/374.** Restano 289 unità e 27 contesti circa. Il registro fissato qui vale per
  tutto il file: se cambia qualcosa (per esempio «categoria» della lotteria di L58, o «Tonner»), va
  cambiato in tutti i lotti.
- **Le scene con scelte multiple** (Curious Waiter, Blind Landing, Forest Fire) hanno rami che il gioco
  mostra uno alla volta: la traduzione non deve presupporre che il giocatore li abbia visti tutti, e
  infatti ogni ramo è autosufficiente.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (35 controlli) |
