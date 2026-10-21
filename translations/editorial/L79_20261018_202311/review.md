# REVIEW — L79 · `data/successors/successor side missions.txt`

## 1. Coerenza con la linea Successors (L68–L78)

- **Casate del Popolo** era già in prosa (L45, L68) e in `NT` come `government \`People's Houses (Hostile)\``
  (L70): qui parlano per la prima volta, e la forma resta quella fissata.
- **Vecchie / Nuove Casate** entrano come opposizione esplicita: tre nomi, tre rese, nessuna sovrapposizione.
- **Il registro è nuovo**: non cerimonioso (Tiliia, Sola) né didattico (Kaatiora) — è **risentito e
  volgare**. L'inglese è contratto (`vis'tor`, `t'which`, `'round`) e la traduzione non lo addolcisce, ma non
  inventa arcaismi: usa italiano corrente con sintassi spezzata.
- **`predecessors` non compare** in questo lotto: il discorso è tutto politico, non storico.

## 2. Nodi traduttivi aperti (dichiarati)

- **`thou art doubly so`** (17): «allora lo sei due volte» — il «due volte» si riferisce all'accusa di essere
  stolto **e** ingannato; la resa mantiene l'ambiguità.
- **`when in thy back their dagger nests`** (17): «quando il loro pugnale ti niderà nella schiena» — `nests`
  come verbo è raro anche in inglese, e la resa lo tiene strano.
- **`that which was`** (25): «ciò che è stato» — non «ciò che fu»: la forma piana regge meglio la solennità.
- **`the Houses New`** (19): ordine invertito nell'inglese (per il ritmo); reso «Casate Nuove».
- **`intermediary place`** (19): «luogo intermedio» — non «scalo»: il testo dice che ci sono stati *spinti*.
- **`flight knave`** (10) e **`flighty knave`** (9? no: 10 contro 9): le due varianti sono rese una volta
  «furfante volubile» ciascuna; se un revisore volesse distinguerle, servirebbe una sfumatura diversa.

## 3. Tre virgolette dispari

| unità | inglese | italiano |
|---|---|---|
| 10 | `"Thou art the alien vis'tor paraded 'round… speaks?` | `"Sei l'alieno visitatore portato in giro… chi ti parla?` |
| 22 | `"Thou would be wise… 'friends.'` | `"Faresti bene… 'amici'.` |
| 27 | idem 22 | idem 22 |

Tutte e tre **aprono senza chiudere**. Il `verify.py` verifica l'insieme `(10, 22, 27)`, che ognuna inizi con
`"` e non finisca con `"`, e che **le altre** unità con virgolette siano bilanciate.

## 4. Duplicati

| gruppo | inglese | nota |
|---|---|---|
| 22 / 27 | stessa battuta finale | due rami della stessa scelta |
| 23 / 28 | `"Or don't. Another buried fool makes little difference."` | idem |
| 18 / 24 / 29 | `With that, the Successor leaves…` | la stessa uscita, tre volte |

Resa identica obbligatoria; nessun'altra ripetizione ammessa.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 29 unità `PENDING`.
- **Nessun caricamento nel gioco**: lo spazioporto, il reietto e la folla non sono stati visti a schermo.
- **Nessuna verifica del registro**: il risentimento politico è valutato come testo, non misurato.
- **Le tre istituzioni** (Vecchie, Nuove, Popolo) restano distinte per scelta; un revisore umano potrebbe
  volerle mappare diversamente, ma servirebbe una decisione sull'intero gioco.

## 6. Rischi residui

- **`0,75` è il minimo** (unità brevi come «(Sì.)»): dentro il gate.
- **`1,25` è il massimo**: nessuna riscrittura.
- **Il `verify.py` asserisce 116 prima / 19 dopo**: se L80 non partisse dalla 416, diventerebbe rosso.
- **Zero token** significa che questo lotto non può verificare la parità per simbolo: l'assenza è asserita, e
  un `<…>` introdotto per errore in traduzione farebbe scattare il controllo `token per unita`.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit 0 (36 controlli), sha256 `54af11093d844256` |
