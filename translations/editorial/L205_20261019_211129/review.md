# REVIEW — L205 · `hai outfits.txt` (quinto e ultimo lotto)

Coppie EN→IT rilette in `translation.json` (`968d32112e56b1d4…`). Tutte le 13 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`reverse thruster` → «retropulsore»**: compatto, tecnico, e distingue il pezzo dal propulsore principale.
2. **`steering` → «sterzata»** in questo lotto (L204 aveva «propulsione e manovra» per *thruster steering set*):
   qui il contesto è la manovrabilità della nave, non un set di equipaggiamento.
3. **`atomic engines` → «motori atomici»**, **`thrusters` → «propulsori»**: distinzione mantenuta come in L204.
4. **`Deep Sky`** resta invariata (azienda); **`Unfettered Hai`** resta invariato.
5. **`outfits` → «equipaggiamenti»** (unità 9): coerente con «negozio di equipaggiamenti» del glossario.
6. **`go-to choice` → «scelta d'elezione»**: registro tecnico, evita «la scelta obbligata» che cambierebbe il senso.
7. **`boarders` → «arrembaggi»** (unità 11): rende l'azione, non le persone; «abbordatori» non è italiano corrente.
8. **`shadowbox` → «teca illuminata»** (unità 13): rende insieme la scatola e la luce interna, che l'inglese dà con
   *lit shadowbox*.
9. **I trattini dell'unità 13 restano trattini** (` - `), non lineette: il sorgente usa il trattino semplice e la
   tipografia del progetto vieta `—`/`–`.
10. **`Nanachi`** invariato: nome proprio di persona.

## 2. Un errore mio, corretto prima di chiudere

L'asserzione «l'unità 10 finisce con `...`» era **falsa**: i tre punti stanno a metà frase (*«...senza esitare...
sempre che...»*). Il testo era giusto, il controllo sbagliato. Riscritto per confrontare il numero di `...` nelle due
lingue, così l'asserzione verifica una corrispondenza invece di una posizione.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 13 unità `PENDING`; il file è tradotto, non approvato.
- **Nessun equipaggiamento installato nel gioco**, **nessun testo visto a schermo**, **nessuna revisione umana**.
- **Nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (23), `verify.py` exit **0** (16), invariante di file 65/65 |
