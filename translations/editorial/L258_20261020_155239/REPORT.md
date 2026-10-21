# REPORT — L258 (`data/human/post-war reactions.txt`, righe 152–215)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 20 | 20 |
| parole | 422 | **403** (0,95) |
| tab | 19 | 19 · stesse unità · primo carattere |
| virgolette | 45 | 45 · **mappa per unità identica** |
| apici | 18 su 10 unità | 12 su 7 unità |
| segnaposto | 0 | 0 |

Rapporto per unità **0,81 – 1,26**: nessuna resa fuori gate, nessuna accorciata dopo la misura.

## 2. I due contesti

```
unità  1–11   mission:War Reactions: Navy and Free Worlds Captains  (11)
riga  196     — la 12 apre Syndicate Orphan, senza tab, descrizione d'ambiente
unità 12–20   mission:War Reactions: Syndicate Orphan                ( 9)
```

Il `check.py` verifica la **coppia esatta** `(11, CTX_A) (12, CTX_B)` e il conteggio `{CTX_A: 11, CTX_B: 9}`.

## 3. Seconda citazione non chiusa (unità 5)

```
"Seriously, though, both the Free Worlds Senate and Republic Parliament are up in arms over fear of aliens," says Fiona. Rain adds, "Only metaphorically up in arms, this time.
```

**Tre** virgolette: due attorno alla prima battuta e una che **apre** la seconda senza chiuderla. La resa italiana ne ha tre,
e i due script asseriscono `== 3` in entrambe le lingue con la frase che finisce in `.`. È il **secondo** caso del file dopo
L257: la regola «la citazione non chiusa si riproduce» non è un'eccezione isolata, è una **forma del sorgente**.

## 4. Il testo

Due voci diverse nello stesso lotto:

1. **Le sorelle** (1–11): pattuglia congiunta fra Repubblica e Free Worlds, allarme dei parlamenti per paura degli alieni,
   il racconto della corazzata e dell'ausiliaria, le origini (Accademia della Marina; milizia di Longjump). Il tono è
   **affettuoso e ironico** («essere mia sorella non mi ha impedita di far saltare il suo incrociatore!»).
2. **Gus** (12–20): un ragazzo di circa dodici anni picchiato da tre coetanei davanti all'officina. Il registro scende a
   **asciutto e d'azione** («Basta così, ragazzi.»), con un'opzione di uscita fra parentesi («(Ignorali e continua a
   camminare.)») e due modi di rifiutare, **identici nella seconda metà**: «Ho fretta. Arrangiati da solo.» / «È dura,
   amico, ma ho fretta. Arrangiati da solo.»

## 5. Lessico

| inglese | resa |
|---|---|
| `Dreadnought` | **corazzata** |
| `Auxiliary` | **ausiliaria** |
| `Cruiser` | **incrociatore** |
| `escape pods` | **capsule di salvataggio** |
| `Navy Academy` | **Accademia della Marina** |
| `Free Worlds Senate` | **Senato dei Free Worlds** |
| `Republic Parliament` | **Parlamento della Repubblica** |
| `joint patrol` | **pattuglia congiunta** |
| `hoaxes` | **bufale** |
| `repair shop` | **officina** |
| `holster` | **fondina** |
| `scruffy-looking` | **dall'aria trasandata** |
| `That's rough, buddy` | **«È dura, amico»** |

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   45 prima · 20 qui · 22 dopo la 215 · 65 righe distinte su 87 · copertura 65/87 (74,7%)
```

Entrambi gli script verdi al **primo** giro, senza correzioni. L'invariante di file è scritto in forma **non tautologica**:
il `verify.py` confronta l'unione delle righe dei tre lotti del file con le righe del database sotto la 216, e solo dopo
stampa il totale.

## 7. Correzione dello stesso errore, due volte

La batteria globale, dopo L258, ha dato **`ROSSO L257/verify.py`**: il suo controllo di segmento elencava i lotti del file
(`[22, 23]`) e la copertura totale (45/87) — affermazioni sul **futuro**, smentite dal terzo lotto. Riscritto sull'invariante
di segmento (le righe del lotto sono esattamente 76–151).

**Lo stesso difetto era già in questo `verify.py`** (`[22, 23, 20]` e «65/87»): invece di aspettare che diventasse rosso con
L259, è stato riscritto **subito** con la stessa regola. Batteria: **`verificati=260 rossi=0`**.

La lezione, ripetuta per la quinta volta nella campagna: **un controllo che elenca i lotti esistenti non è un invariante**,
perché descrive il passato del file. Il lotto afferma **le proprie** righe; il totale del file si **stampa**.

## 8. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 65/87; restano 22 unità in **due** lotti (L259, L260 terminale).
