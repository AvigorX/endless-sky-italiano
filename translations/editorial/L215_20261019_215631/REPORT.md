# REPORT — L215 · `deep jobs.txt` (quarto lotto)

## 1. Contenuto

Venticinque unità in due blocchi. Il primo chiude l'incontro con **Wayde**, l'agente della Deep Security: l'offerta di
entrare nella lista dei piloti fidati, la battuta sul *«at any rate»* detto due volte, l'addio con il saluto appena
accennato. Il secondo apre due missioni `Basic` e due `Deep Security` e introduce **Julie** con la sua assistente, che
hanno perso il trasporto e hanno una scadenza.

## 2. Difficoltà

1. **Una battuta va tradotta come un sistema, non come frasi.** *At any rate* compare tre volte: alla fine dell'unità 1,
   all'inizio della 2 e — citato fra apici — nell'unità 6, dove il giocatore dice «l'hai detto due volte». Se la resa
   cambia espressione in uno dei tre punti, il gioco perde il senso. Ho fissato **«in ogni caso»** e il controllo verifica
   le tre occorrenze **in entrambe le lingue**, più la posizione (chiusura dell'1, apertura della 2, citazione nella 6).
2. **La citazione su due paragrafi.** L'unità 1 apre il discorso e non lo chiude: è la convenzione del file per i
   paragrafi successivi. La distribuzione delle 29 virgolette è verificata unità per unità, e c'è un'asserzione apposita
   («l'unità 1 comincia con `"` e non finisce con `"`»).
3. **`<date>` per la prima volta.** Il segnaposto sta solo nell'unità 22, e la resa deve evitare l'articolo: «entro
   `<date>`», non «entro il `<date>`», perché non sappiamo se il gioco sostituirà una data o una durata.
4. **L'`UI_LABEL` della riga 683.** Non è nel lotto e non si traduce. Questo cambia il conto dell'invariante: le unità
   prima della 684 sono **103** (102 tradotte + 1 label), e la somma che torna a 187 è `127 + 1 + 59`. Il `verify.py` lo
   dichiara, e c'è un controllo che nessuna riga vada persa.
5. **Registro unico «tu»** anche con Wayde e con la donna: «scusa», non «mi scusi». Verificato con un'asserzione
   negativa che cerca «Lei», «mi scusi» e «Si accomodi».

## 3. Numeri osservati

```
unita' 25 · {'MISSION_TEXT': 15, 'VALUE': 5, 'DESCRIPTION': 5} · tutte PENDING
14 tab (1-12, 24-25) · 29 virgolette con distribuzione per unita' · 14 apici EN / 8 IT
15 segnaposto su 4 simboli, con <date> solo nell'unita' 22
6 contesti · righe 684/864 · 103 prima (di cui 1 UI_LABEL) · 59 dopo · confine riga 866
parole 431 -> 427 · rapporto 0.93 - 1.22 (media 1.07)
FAIL totale: 0 (25 controlli) · verify exit 0 (19 controlli) · sha256[:16] 0b4212a734b678ff
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (19) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna missione giocata**: la battuta è verificata sul testo, non letta a schermo.
- **Restano 59 unità** nel file, più l'`UI_LABEL` della 683 che non si traduce.
