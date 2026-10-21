# L20 — revisione editoriale

Quinto lotto di `data/human/human missions.txt`, righe **6432–10806**, **1.676 unità**,
**40.112 parole inglesi → 38.248 italiane**, 62 contesti (60 missioni, 2 schede nave).

- Confine iniziale: riga 6432, `mission:Care Package to South 1` (prima unità libera dopo L19).
- Confine finale: riga 10806, ultima unità di `mission:Stone to Hope`. L'unità successiva
  è la riga 10812, `mission:Stone to Ice Queen`.
- Target 40.000 parole: raggiunto con **+112 parole (+0,28%)**, senza tagliare nessuna unità.
- Nessun intervallo è stato inventato: tutti i numeri vengono da `source.json`, da
  `state.db` o dai file di parte.

## 1. Sezioni e parti

19 parti, ognuna esportata, tradotta, controllata con `check.py --range` e poi riletta:

| parte | unità | righe | parole EN | contesti |
|---|---|---|---|---|
| part01 | 1–95 | 6432–6666 | 2.790 | 5 |
| part02 | 96–181 | 6668–6862 | 1.910 | 3 |
| part03 | 182–280 | 6868–7200 | 2.627 | 8 |
| part04 | 281–343 | 7202–7391 | 1.495 | 6 |
| part05 | 344–430 | 7395–7644 | 2.418 | 6 |
| part06 | 431–491 | 7647–7798 | 1.840 | 1 |
| part07 | 492–585 | 7805–8080 | 2.555 | 5 |
| part08 | 586–686 | 8081–8336 | 2.738 | 3 |
| part09 | 687–800 | 8342–8614 | 2.581 | 3 |
| part10 | 801–900 | 8615–8908 | 2.333 | 5 |
| part11 | 901–1010 | 8909–9207 | 2.829 | 6 |
| part12 | 1011–1120 | 9210–9435 | 3.091 | 3 |
| part13 | 1121–1200 | 9440–9594 | 1.749 | 1 |
| part14 | 1201–1280 | 9595–9785 | 1.719 | 2 |
| part15 | 1281–1360 | 9786–9987 | 1.331 | 2 |
| part16 | 1361–1440 | 9990–10195 | 1.598 | 2 |
| part17 | 1441–1520 | 10197–10416 | 1.329 | 4 |
| part18 | 1521–1600 | 10418–10608 | 1.745 | 3 |
| part19 | 1601–1676 | 10609–10806 | 1.434 | 7 |

**Deviazione dichiarata:** la consegna chiedeva sezioni da 3.000–5.000 parole. Le parti L20
vanno da **1.331 a 3.091 parole EN** (media 2.111), perché il taglio segue i confini delle
missioni e il controllo strutturale viene eseguito a ogni parte. È la stessa granularità di
L19 (25 parti, media 1.599 parole) e non è stata mascherata come conforme: è una scelta
editoriale con un compromesso dichiarato, non una sezione che raggiunge il target.

## 2. Confini verificati

- **10806 è fine missione**: `mission:Stone to Hope` termina lì; `mission:Stone to Ice Queen`
  comincia alla riga 10812. Nessuna unità spezzata dentro una missione.
- **6432 è il primo punto libero dopo L19**: l'unità precedente nel file è la riga 6428,
  ultima di `mission:Blind Man from Martini`, già tradotta in L19.
- Il lotto non sfora nel file successivo: `human missions.txt` contiene ancora 465 unità
  (11.046 parole) dopo la riga 10806.

## 3. Terminologia

Decisioni prese in questo lotto, applicate coerentemente in tutte le parti:

| EN | IT | nota |
|---|---|---|
| Free Worlds | Free Worlds | invariato, con articolo italiano («i Free Worlds»); coerente con L19 |
| Paradise Worlds / Paradise Planets | Mondi Paradisiaci / Pianeti Paradisiaci | come L19 |
| the Man | il Sistema | gergo per l'autorità; reso con l'equivalente italiano |
| sweatshop | fabbrica di sfruttamento | nessun equivalente italiano diretto; «laboratorio clandestino» scartato perché confonde con la clandestinità della mostra |
| the deep / the Deep | il Deep | nome di regione, invariato |
| Family-Cairn | Family-Cairn | termine culturale della tradizione Hlewagasti/Snaiwaz; tradurlo («cairn di famiglia») avrebbe perso il valore di nome proprio. Documentato qui |
| Ion Cannon (in prosa) | cannone ionico | i nomi degli outfit in prosa vengono resi in italiano descrittivo, come in L19 |
| Hroar's Haulers | Hroar's Haulers | nome di compagnia, invariato |
| Lightspeed Logistics, Syndicated Systems, Megaparsec Incorporated, Deep Security, Navy Intelligence, Republic Intelligence | invariati | nomi di entità |
| Ivaldur the Forger | Ivaldur il Falsario | epiteto tradotto, nome proprio invariato |
| Bertha, Hrodny, Mariel, Alejandra (Ale), Bunker, River, Tosti, Helm, Wynnafrith, Regina, Ivaldur, Skounce Yarling, Howard Vendeur, Artemis/August Renard, Timothy Radrickson | invariati | nomi propri |
| Star Empress, Tycho's Legacy, Shippy McShipface, It's Dark Here, What Asteroid | invariati | nomi candidati nel sondaggio pubblico: tradurli avrebbe distrutto la gag |
| the Academy, Academy of Planetary Sciences | l'Accademia / invariato | come L19 |

Unità monetarie: separatore delle migliaia all'italiana (`1.000.000`, `60.000`, `99.999`),
«crediti» minuscolo, come nei lotti precedenti.

## 4. Casi editoriali trattati

### 4.1 Kris Brecht, `they/them`
Le unità 214–253 presentano un personaggio non binario che si autodichiara con
«Kris Brecht, they/them.» La dichiarazione è **mantenuta in inglese**: è un'enunciazione
di identità, non prosa non tradotta. Di conseguenza `check.py` è stato esteso con
`TITLES = (..., 'they/them')`, con questa motivazione registrata.

Nella prosa italiana si evita l'accordo di genere riferito a Kris, senza ricorrere a
neolografie: si usano forme che non richiedono participi concordati («Kris si ferma di
colpo», «Torna l'aria sicura», «Kris univa una cortesia...»). La scelta è sistematica in
tutte le unità 208–253 e non è una svista: le forme con desinenza maschile o femminile
sono state evitate deliberatamente perché attribuirebbero un genere che il testo non dà.

### 4.2 Citazioni lasciate aperte nel sorgente
Il sorgente inglese contiene un numero **dispari** di virgolette in **40 unità** — citazione
aperta e non chiusa, quasi sempre perché il discorso continua nella riga successiva, che il
motore tratta come blocco unico. L'italiano riproduce la stessa struttura: nessuna virgoletta
aggiunta, nessuna rimossa. Elenco misurato con `source.json`:
64, 82, 83, 107, 120, 129, 173, 179, 185, 226, 309, 461, 507, 508, 555, 599, 672, 699, 701,
758, 770, 771, 772, 777, 779, 801, 806, 807, 917, 933, 1079, 1086, 1185, 1202, 1204, 1298,
1404, 1627, 1640, 1663.

### 4.3 Duplicati
`DUP_OK` è derivato dai duplicati reali del sorgente: quando l'inglese ripete la stessa
battuta in rami diversi della missione, l'italiano la ripete identica. Casi risolti perché
il sorgente **non** era identico, e la traduzione aveva appiattito la differenza:

- 832 «What if…» vs 837/844 «And if…» → «E se avessi dubbi…» / «E se mi preoccupasse…».
- 280 «Ignore him.» vs 357/577 «Ignore it.» → «(Ignalo.)» / «(Ignoralo.)».
- 377 «Head back to my ship.» vs 1093 «Go back to my ship.» / 1591 «Head back to my ship.»
  → «(Torna alla nave.)» / «(Torna alla mia nave.)» / «(Torna alla nave.)».
- 1510 «I got nothing to better to do.» vs 1550 «I've got nothing…» → differenza mantenuta.
- 1570 vs 1573: l'inglese differisce per una parola («you find» / «find»), l'italiano pure.

### 4.4 Registri
- **Contratto obbligazionario** (645–647): registro giuridico italiano, con i numeri
  invariati (`1.000.000`, `365.000`) e i nomi delle entità non tradotti.
- **Howard**: italiano commerciale, untuoso, con «lei» di cortesia anche quando la
  situazione è tesa; i suoi cedimenti (725, 794) restano secchi.
- **Hrodny**: italiano colloquiale con elisioni («'sta», «nun»), per resa del dialetto
  di classe operaia dell'originale; non è un dialetto regionale italiano specifico.
- **Timothy su Oblivion** (1115, 1130–1141): frasi spezzate dalla tosse, con la balbuzie
  resa come nell'originale («P-p-per favore», «T-t-timothy»), senza normalizzarla.
- **Tosti** (1638–1673): italiano popolare, «signore» come allocutivo, «papà» al posto di
  «padre» per tenere il registro umile.

### 4.5 Contenuti sensibili
- Uccisione del clandestino dalla camera stagna (884), fucilazione del giocatore (1161,
  1172, 1196), schiavitù e tratta (508, 535–546), disabilità e malattia terminale
  (1113–1140, 1557–1583). Nessuna edulcorazione e nessun inasprimento: si traduce quello
  che c'è, senza aggiungere disprezzo che l'originale non esprime.
- Unità 1069–1070 (invettiva contro i «porci capitalisti»): il discorso è reso nella sua
  interezza, compreso il finale in cui la sala non reagisce con rabbia ma con indifferenza.

## 5. Correzioni effettuate durante i controlli

- 40 unità con virgolette allineate al conteggio del sorgente (vedi 4.2).
- 6 gruppi di duplicati non spiegati dal sorgente (vedi 4.3).
- 137: punteggiatura («ti aspetti che ti paghi?» invece di «!»).
- 216: refuso «Limítati» corretto in «Limitati».
- 209: frase ridondante («i capelli tirati indietro all'indietro») riscritta.
- 278: «concourse» residuo inglese sostituito con «atrio».
- 517: refuso «senzaintoppi» corretto.
- Unità 1189b introdotta per errore nel file di parte 13 e rimossa prima del controllo.

## 6. Difetti degli strumenti trovati e non corretti

- `check.py` conta le virgolette come caratteri, non come coppie: un'unità con citazione
  aperta e non chiusa nel sorgente deve avere un conteggio **dispari** anche in italiano.
  È il motivo per cui 37 unità sembrano «sbagliate» a un lettore e sono invece fedeli.
  Non è stato modificato: cambiarlo avrebbe nascosto il caso.
- `check.py` non distingue «nessuna unità tradotta» da «rapporto fuori intervallo» quando
  la lista dei rapporti è vuota; il guard `bool(rs)` è stato aggiunto in fase di setup.
- `check_handoff.py` verificava costanti cablate L18→L19; riscritto in L19 per leggere i
  valori dal documento. **Toccato anche in L20**, per un difetto reale: la cella «Confine dopo»
  non sapeva esprimere un lotto che finisce con l'ultima unità del file, e falliva sempre
  (`nxt is None`) pur con un handoff corretto. Correzione minima: se la cella vale `fine file`,
  il controllo verifica che **non** esistano unità dopo la riga finale dichiarata. Tutti gli
  altri controlli sono invariati, e il file è stato riprovato su `HANDOFF_L21` (24/24 OK).

## 7. Cosa non è stato fatto

- Nessuna scrittura in `state.db`, nei batch, nel glossario, nell'inventario o negli
  output approvati: le 1.676 unità restano `PENDING`.
- Nessuna patch K4, nessuna build, nessun test di gioco, nessuna applicazione al gioco.
- Nessun rendering verificato: questo workflow non esegue il gioco.
- Nessuna modifica al repository `endless-sky` (commit `b4aa3bac3`).
