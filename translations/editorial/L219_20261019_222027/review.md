# REVIEW — L219 · `successor ships.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`26062019d4d6d536…`). Tutte le 25 unità sono **`PENDING`**.

## 1. Le 19 unità copiate

16 `TEXT` di equipaggiamento (`1-"Uurau" Betavoltaic Cell`, `"Aqra" Inductive Reverser`, `3-"Kaska" Betavoltaic Cell`) e
3 `VALUE` di specie (`Kvelqden`, `Kvelqden-Khora`, `Myaeden`). Nomi mostrati nel gioco: non si traducono, e il criterio è
il **ruolo**, non l'etichetta del record.

## 2. Le due coppie che devono restare coerenti

| coppia | inglese condiviso | resa unica |
|---|---|---|
| 7 / 9 | *This tiny shuttle is the smallest vessel operating in Successor space, and…* | «Questa navetta minuscola è la nave più piccola in servizio nello spazio dei Successori, e…» |
| 24 / 25 | *neither elegant nor fast* | «non è né elegante né veloce» |
| 24 / 25 | *a flexible enough weapons layout to let it fight back in a pinch* | «una disposizione delle armi abbastanza flessibile da permetterle di reagire all'occorrenza» |

Le due `DESCRIPTION` della stessa nave compaiono in schermate diverse: se divergono, il gioco racconta due storie. Il
`check.py` verifica il **prefisso identico** di 7 e 9 e la presenza delle **due formule identiche** in 24 e 25.

## 3. Decisioni di resa

1. **`get their arms on`** → «riuscire a metterci le mani»: l'inglese usa *arms* in senso figurato di accesso; tradurre
   «armi» sarebbe un falso senso.
2. **`multipurpose vessels`** → «validi vascelli polivalenti»; **`short-duration research expeditions`** → «spedizioni di
   ricerca di breve durata».
3. **`based on originals from the time of the Predecessors`** → «si basa … su originali dell'epoca dei Predecessori»:
   `Predecessors` è un popolo, va maiuscolo e si traduce.
4. **`nowhere near as advanced`** → «ben lungi dall'essere altrettanto avanzata»; **`successive iterations with more
   limited resources`** → «le iterazioni successive con risorse più limitate».
5. **`cost-efficiency and user-friendliness`** → «l'economicità e la facilità d'uso».
6. **`ruggedize`** → «irrobustire»; **`a second gun port … on the underside`** → «una seconda feritoia per le armi …
   sul ventre».
7. **`standing toe-to-toe with a production interceptor`** → «tenere testa a un intercettore di serie»: `production` qui è
   *di serie*, contrapposto all'esemplare modificato.
8. **`decaying stations and hostile worlds`** → «le stazioni in degrado e i mondi ostili».
9. **`mainstay` / `backbone`** → «pilastro» in 24, «spina dorsale» in 25: due parole inglesi diverse, due rese diverse, e
   non è incoerenza — è il testo che cambia metafora.
10. **`cemented itself as`** → «si è affermata come»; **`no less smoothly than their newer counterparts`** → «con la stessa
    scioltezza delle loro controparti più recenti».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 25 unità `PENDING`.
- **Nessuna schermata di allestimento aperta**: la classificazione dei `TEXT` come nomi resta dedotta dal file.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (16) |
