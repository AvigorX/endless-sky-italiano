# REPORT — L257 (`data/human/post-war reactions.txt`, righe 76–151)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 23 | 23 |
| parole | 406 | **408** (0,99) |
| tab | 22 | 22 · stesse unità · primo carattere |
| virgolette | 45 | 45 · **mappa per unità identica** |
| apici | 17 su 12 unità | 5 su 4 unità |
| segnaposto | 5 | 5 · **stesso ordine per unità** |
| contesti | 9 + 14 | 9 + 14 |

Rapporto per unità **0,82 – 1,30**: nessuna resa è stata accorciata dopo la misura, perché nessuna usciva dal gate.

## 2. I due contesti

```
unità  1– 9   mission:War Reactions: Asteroid Miners                (9)
riga  110     — la 10 apre la nuova missione, senza tab, descrizione d'ambiente
unità 10–23   mission:War Reactions: Navy and Free Worlds Captains  (14)
```

Il `check.py` verifica la **sequenza** `(9, CTX_A) (10, CTX_B)` e il conteggio `{CTX_A: 9, CTX_B: 14}`: un lotto che
attraversa un cambio di missione non può essere controllato come se il contesto fosse unico.

## 3. La citazione non chiusa (unità 12)

```
"Captain Fiona, F.S. Baobab," says the other. "We both saw you in battle against the Pug. You're the war's most accomplished captain!
```

Tre virgolette: due attorno al nome e una che **apre** la citazione lunga senza chiuderla. La resa italiana ha le stesse
tre, e i due script asseriscono `== 3` **in entrambe le lingue**, con la frase che termina in `!`. Non è una svista da
correggere: è il testo del gioco, e «aggiustarlo» cambierebbe una stringa che l'utente vede.

## 4. I segnaposto

| segnaposto | conteggio | dove |
|---|---|---|
| `<first>` | **1** | unità 1 (`Sono il capitano <first> <last>!`) |
| `<last>` | **3** | unità 1, 5 (`capitano <last>`), 11 (`capitano <last>`) |
| `<ship>` | **1** | unità 11 (`Come va la <ship>`) |

Sono **nomi del giocatore**: invariati, e senza concordanza. `<ship>` prende l'articolo **perché ce l'ha l'inglese**
(`the <ship>`); `<first>` e `<last>` no, perché sono nome e cognome. L'**ordine** per unità è confrontato, non solo il
totale.

## 5. Lessico

| inglese | resa |
|---|---|
| `the Navy` / `a Navy captain` | **la Marina** / **un capitano della Marina** |
| `Free Worlds` | **Free Worlds** (fazione, invariata) |
| `Captain Rain, R.N.S. Camuy` | **«Capitano Rain, R.N.S. Camuy»** (prefisso di registro invariato) |
| `Captain Fiona, F.S. Baobab` | **«Capitano Fiona, F.S. Baobab»** |
| `Spider Funk` | **Spider Funk** (nome della droga, invariato) |
| `illegal hallucinogenic` | **allucinogeno illegale** |
| `joint police operation` | **operazione di polizia congiunta** |
| `Stay well.` | **Stammi bene.** |
| `That's rough, buddy` | (fuori da questo lotto, riga 215: sarà L258) |

## 6. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   22 prima · 23 qui · 42 dopo la 151 · 45 righe distinte su 87 · copertura 45/87
```

Nessun difetto trovato negli script: entrambi verdi al **primo** giro, `check.py` compilato e verificato dal lint prima di
eseguirlo. L'unica correzione è stata fatta **prima** di eseguire il `verify.py`: un'asserzione di segmento che avevo scritto
in forma tautologica (`righe == righe | …`) è stata riscritta come confronto con le righe del database sotto la 152 —
un controllo che **può** fallire.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 23 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 45/87; restano 42 unità, su due missioni (`Navy and Free Worlds Captains` e `Syndicate Orphan`).
