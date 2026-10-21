# REVIEW — L227 · `remnant outfits.txt` (quinto e ultimo lotto)

Coppie EN→IT rilette in `translation.json` (`ba3673a78c7a0d5e…`). Tutte le 10 unità sono **`PENDING`**.

## 1. Il confronto torna a 1 / 9

| | unità |
|---|---|
| identiche all'inglese | **1** — il `VALUE` della riga 948, `Void Sprite Parts` |
| tradotte | **9** — tutte le `DESCRIPTION` |

Dopo tre lotti a zero identiche, il numero cambia perché cambia la **composizione della finestra**, non la regola. Il
controllo asserisce che l'unica identica sia il `VALUE`: un «1» generico potrebbe nascondere una descrizione dimenticata in
inglese.

## 2. Decisioni di resa

1. **`insolitamente avido di energia`** per *unusually power-hungry*: stesso aggettivo usato in L226 per *power-hungry*, per
   continuità nella famiglia dei motori.
2. **`It's unclear whether … or whether they are partly inspired by alien technology`** → «Non è chiaro se … o se siano in
   parte ispirati a tecnologia aliena»: l'incertezza è il contenuto della scheda.
3. **`destabilize the weaker internal tissue … and liquefies them`** → «destabilizzare i tessuti interni più deboli … e
   liquefarli».
4. **`void sprites`** → «void sprite» (invariato, come `Void Sprite Parts`); **`tentacles`** → «tentacoli».
5. **`the Archon stopped their harvests`** → «l'Archon ha fermato le loro raccolte»: `harvests` sono le raccolte di
   tentacoli, non un raccolto agricolo.
6. **`degraded into uselessness centuries ago`** → «sono diventati inutilizzabili secoli fa».
7. **`are credited with helping … safeguard their refuges from ground-based threats`** → «si attribuisce il merito di aver
   aiutato … a proteggere i loro rifugi dalle minacce terrestri».
8. **`a beam that has a strong paralyzing effect on the nervous system`** → «un raggio che ha un forte effetto paralizzante
   sul sistema nervoso».
9. **`an area of effect that penetrates walls and other solid objects`** → «un'area di effetto che penetra pareti e altri
   oggetti solidi».
10. **`nothing more and nothing less than a cubic meter`** → «Non è altro che un metro cubo»: la formula inglese è enfatica,
    e «né più né meno» in italiano suonerebbe più solenne del registro della scheda.
11. **`a terrible occurrence and a dreadful opportunity`** → «un evento terribile e un'occasione spaventosa».
12. **`if it had been handled properly`** → «se fosse stato trattato come si deve»; **`little more than the value of the
    compounds contained within`** → «poco più del valore dei composti che contiene».
13. **`IFF verifier`** → «verificatore IFF»; **`mechanically click with every adjustment`** → «scattano meccanicamente a
    ogni regolazione».
14. **`a surprisingly beautiful blend of classical music tracks`** → «una fusione di brani di musica classica
    sorprendentemente bella».
15. **`seemingly innocuous at first`** → «all'apparenza innocuo»; **`tapping either edge produces a brief, faint hum`** →
    «picchiettando su uno dei due bordi si produce un breve e debole ronzio».
16. **`should they ever become stranded`** → «qualora restino bloccati»: stessa resa di L225, al plurale.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 10 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: nessuna delle dieci schede è stata osservata in partita.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24), `verify.py` exit **0** (20), file chiuso 57/57 |
