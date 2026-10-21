# REVIEW — L82 · `data/successors/predecessors.txt`

## 1. Coerenza con la linea (L68–L81)

- **Myiara, Resja, Iasa, Kis, Queru** sono nomi già presenti nel file e nella linea: invariati.
- **`Multimodal Armor: Regen`** resta dato (come in L81); in prosa la stessa tecnologia è «corazza
  plurimodale» (L73/L76). La distinzione è dichiarata (decisione 259).
- **Il registro** è quello delle schede antiche: solenne, con immagini violente (`sventrava`, `squarcia`,
  `famelica`). La traduzione non lo addolcisce né lo enfatizza.

## 2. Nodi traduttivi aperti (dichiarati)

- **`the foolish Myiara`**: «la sciocca Myiara» — l'aggettivo è **sprezzante**, e non è un errore di genere
  (Myiara è un nome, e il femminile è quello della parola «sciocca» riferita a una persona-nome).
- **`unknowable perception`**: «percezione inconoscibile» — reso letterale: è un'iperbole voluta.
- **`its jaws`** (15): «le sue fauci» — l'arma è descritta come bestia, e il possessivo maschile segue «Kis».
- **`Iasa was a drone ship's perfect coilgun`**: «era il cannone a bobina perfetto di una nave drone» — il
  genitivo è ambiguo in inglese; la resa sceglie l'arma *della* nave, non *per* la nave.
- **`vows`/`wishes`** nei nomi: `Vowsworn` e `Lethal Wishes` restano in inglese (dato), e non vanno confusi
  con il testo.

## 3. Un errore mio, corretto

Nel `check.py` la riga dei token era `rows.append((nome, tok == 0, tok))`: il **terzo** elemento è il booleano
che il printer legge come esito, e `0` è falso — la riga stampava `FAIL True` su un conteggio corretto.
Corretta in `str(tok), tok == 0`. Il `verify.py` non aveva lo stesso difetto perché usa `ck(nome, cond,
dettaglio)`.

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 15 unità `PENDING`.
- **Nessun caricamento nel gioco**: le schede di Queru, Iasa e Kis non sono state viste a schermo.
- **Nessuna traduzione dei nomi di equipaggiamento**: scelta dichiarata, reversibile solo insieme ai file
  degli equipaggiamenti.
- **Nessuna verifica del bilanciamento**: le note su penetrazione e danni sono tradotte come testo, non
  confrontate con i valori di gioco.

## 5. Rischi residui

- **`0,97 – 1,10`**: il lotto più compatto finora, nessuna unità vicina al gate.
- **Il `verify.py` asserisce 22 prima / 22 dopo**: se L83 non partisse dalla 446, diventerebbe rosso.
- **`Queru`** ha un nome di dato (3) e una scheda di prosa (12) nello stesso lotto: il `check.py` verifica
  entrambe le cose, e una futura revisione dei nomi dovrebbe toccare solo la 3.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit 0 (32 controlli), sha256 `3a179de373b2fe67` |
