# REVIEW — L75 · `data/successors/successor 2 ghosts aqrabe.txt`

## 1. Coerenza con la linea Successors (L68–L74)

- **Casa X / Casate / Casate del Popolo / erede / ninnolo / pietre chiave / sfera di dati / datapad /
  motore di salto / giardino di statue**: forme già fissate, nessuna reinvenzione.
- **Il registro di Tiliia** è qui al suo massimo arcaico (`thou'rt`, `shalt`, `mayst`, `shouldst`,
  `'tisn't`). Reso con il «tu» moderno formale, come da L45–L47: nessun «voi», nessun arcaismo finto.
- **L'osservatore di Kaatrij** parla in modo militare e secco («La tua aspettativa non è più accurata»,
  «Sarebbe saggio non indugiare»): nessun colore, nessuna cortesia. Il contrasto con Tiliia è nel testo,
  non aggiunto.
- **`Aqrabe I- Sola` non compare**: Tiliia cita «Aqrabe» come Casa.

## 2. Nodi traduttivi aperti (dichiarati)

- **`Kasii-Cavaasa` vs `Kasii-Cavasaa-Oa`**: il sorgente usa due grafie. L74 (stella) dice `Cavaasa`, L75
  (stazione) dice `Cavasaa-Oa`. **Non unifico**: la stazione ha un nome diverso; se un lotto futuro le
  trattasse come lo stesso oggetto, la scelta andrebbe rivista.
- **`our allies in the New`** (7): frase **tronca** in inglese — probabilmente «the New Houses», ma il testo
  non lo dice. Reso «i nostri alleati nel Nuovo», mantenendo l'ellissi invece di completarla.
- **`hast thou?.`** (17): punteggiatura doppia nel sorgente. **Riprodotta** («vero?.»), non corretta.
- **`One in every ten or so`** (28): reso «una su dieci circa», non «una ogni dieci»: il testo è vago.
- **`if it matters`** (35): «se conta», non «se importa»: è una concessione, non un dubbio.
- **`trinket`** (58): «ninnolo», come in L70–L72. In bocca a Tiliia è **sprezzante** verso Kaatrij e va
  tenuto tale.

## 3. Virgolette dispari: il caso più delicato del progetto finora

Quattro unità con **una sola** virgoletta: 5 e 7 aprono, 6 e 8 chiudono. Il gioco le mostra in sequenza,
quindi la frase si chiude solo alla seconda unità. Il `check.py` verifica:
- l'**insieme** degli indici dispari è `(5, 6, 7, 8)`, in inglese e in italiano;
- la virgoletta **chiude** nelle unità 6 e 8 e **non** in 5 e 7 (controllo ristretto alle quattro dispari:
  la prima versione guardava tutte le unità che finiscono con `"` e diventava rossa con la traduzione
  giusta, perché in un dialogo fitto quasi ogni battuta finisce così).

## 4. Il diario senza testo

L'unità 27 è la **categoria** `People` di `log "People" "Tiliia" "…"`: il `check.py` la lascia **identica**
(in `NT`) e il `verify.py` asserisce che il testo della stessa riga **non è nel lotto**. È l'**ottavo** caso
della lacuna dell'estrattore, e il primo in cui il lotto non contiene **nessuna** frase di diario tradotta.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 61 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la baia di allestimento, il giardino di statue e la nuova corazzatura
  non sono stati visti a schermo.
- **La categoria `People`** resta in inglese per scelta.
- **Nessuna verifica del registro**: i tre registri (Tiliia, l'osservatore, la voce narrante) sono valutati
  come testo.
- **Il ramo politico** (45–48) è tradotto ma non «testato» con un giocatore: la reazione di Tiliia dipende
  dal ramo scelto, e il testo è verificato solo per forma.

## 6. Rischi residui

- **`0,72` è il minimo** (unità brevi come «Un rossore divertito passa su Tiliia»): dentro il gate.
- **`1,48` è il massimo**: nessuna riscrittura necessaria.
- **Il `verify.py` asserisce 89 prima / 30 dopo**: se L76 non partisse dalla 404, diventerebbe rosso.
- **Le due grafie di Kasii-Cav…** sono una scelta dichiarata: un revisore umano potrebbe volerle unificare,
  ma servirebbe una decisione sull'intero gioco, non su questo lotto.
- **`nel Nuovo`** (7) è un'ellissi mantenuta: se in futuro il gioco rivelasse il nome completo, andrebbe
  completata in tutti i lotti.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (37 controlli), `verify.py` exit 0 (47 controlli), sha256 `83744e86d2da8682` |
