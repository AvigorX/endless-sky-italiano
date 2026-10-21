# REVIEW — L197 · `hai jobs.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`0ff30f8bb315b0ad…`). Tutte le 36 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`VALUE` identici all'inglese (12/12)**: `Special order from <planet stopovers>`, `Special Escort to <planet>`, `Passenger transport to <planet>`, `Transport family to <planet>`. Convenzione misurata nei lotti L117…L196.
2. **`DIALOG` tradotti (9/9)**: sono dialoghi di consegna, non nomi. Il tipo è arrivato in questo lotto e non è stato confuso con `TEXT`.
3. **`della buona società`** per *socialite*: «mondano» suonava da cronaca, «della buona società» descrive lo status senza ironia aggiunta.
4. **`smanettatore`** per *tinkerer*: «artigiano» perdeva il senso di chi traffica con la tecnologia umana; «armeggiatore» ha una connotazione negativa che l'inglese non ha.
5. **`il <commodity>`** e **`il <cargo> richiesto`**: l'articolo maschile segue i precedenti misurati (`Scarichi il <commodity>`, `il tuo carico di <commodity>`), non un'ipotesi sul nome della merce.
6. **`della <npc>`**: la scorta è una nave, e in italiano le navi sono femminili; il precedente in staging usa già `Il capitano della <npc> ti pagherà…`.
7. **`Porta <fare> su <destination>. Il pagamento è <payment>.`**: resa **identica** a quella già presente in staging per la stessa stringa. Nessuna variazione introdotta.
8. **`Il capitano della <npc> ti pagherà <payment> per una scorta che raggiunga <destination>, nello spazio umano, entro il <date>.`**: la subordinata mantiene l'ordine inglese (`scorta → destinazione → spazio umano → data`) e il congiuntivo regge il `che`.
9. **`auguri tanta fortuna`** (unità 35): resa idiomatica di *wish … the best of luck*, senza calco («augurare la migliore delle fortune» sarebbe stato pesante).
10. **`Questa famiglia di <bunks> si trasferisce…`**: niente «persone» aggiunto, come nei precedenti (`Questa famiglia di <bunks> turisti`, `una famiglia di <bunks>`).

## 2. Un controllo corretto, non un testo

Il primo `check.py` è uscito con **`FAIL totale: 1`** sulla famiglia «ordine speciale»: confrontava tutto ciò che segue
` su <planet> ` nelle unità 3, 7 e 11, ma quelle unità condividono **solo l'ultima frase** (`Vuole <cargo> da <stopovers>
entro il <date>. Il pagamento è <payment>.`). L'errore era nell'asserzione; la traduzione non è stata toccata. Il nuovo
controllo pretende: coda identica, **tre prefissi distinti**, coda presente una sola volta.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 36 unità `PENDING`.
- **Nessun lavoro accettato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**: le incoerenze del gioco si conservano.

## 4. Riallineamento al precedente esistente (dopo la prima chiusura)

`You wish the mining family the best of luck on <planet>…` era **già tradotto in L22**: «Auguri alla famiglia di
minatori ogni fortuna su <planet>, e incassi il pagamento di <payment>.». In L197 avevo creato una variante
(«Alla famiglia di minatori auguri tanta fortuna… e ritiri…») senza accorgermene, perché il primo `check.py`
confrontava con lo staging solo due stringhe.

Durante L198 il confronto con L22 ha mostrato la divergenza sulle tre varianti sorelle (minatori, contadini,
operai). L'unità 35 è stata **riportata alla resa esistente**; `check.py` e `verify.py` rieseguiti a **exit 0**;
`sha256[:16]` passa da `f03d5d9459bc4414` a `0ff30f8bb315b0ad`, e tutti i documenti che lo citano sono aggiornati
(`STATO.md`, `REPORT.md`, `HANDOFF_L198`, `RIPRESA_L198`, i due checkpoint).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, compreso il `FAIL 1` iniziale e la sua correzione |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (19 controlli) |
