# REPORT — L137 · `data/starts.txt` (terzo inizio: la Terra, il Sindacato, il mutuo schiacciante)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'inizio | 1–3 | 172–174 | nome `Escaping Squalor`, la Terra sovrappopolata, il contratto col Sindacato, Antipode, Delve |
| il diario | 4 | 195 | la licenza, la nave, «un'ultima stoccata avida» |
| la storia del mondo | 5–9 | 196–200 | **le cinque frasi rilette** da L135 |
| Delve | 10 | 202 | lo spazioporto nella caverna montana |
| il capitano | 11 | 203 | l'avvertimento: «punta a nord» |
| il cantiere | 12 | 204 | il venditore che sbuffa, la licenza necessaria |
| la banca | 13–14 | 205–206 | il cassiere, i 600.000, il 0,5%, i 706.571 di interessi |
| la firma | 15–16 | 207–209 | «Gli interessi sono tremendi», la fila per la licenza, i 480.000 rimasti |
| il ritorno | 17 | 210 | il gettone in mano, tre modelli: intercettore, mercantile leggero, trasporto |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Escaping Squalor` | **identico** | `VALUE` |
| `overpopulated world with few opportunities` | **un mondo sovrappopolato con poche opportunità** | |
| `a decent wage off of Earth` | **un salario decoroso lontano dalla Terra** | |
| `cheap frontier world` | **un mondo di frontiera economico** | |
| `crushing mortgage` | **un mutuo schiacciante** | |
| `One last greedy stab` | **Un'ultima stoccata, avida come sempre** | reso senza genere: il diario è in prima persona |
| `colossal mountain cave` | **colossale caverna montana** | |
| `Just a heads up` | **Un avvertimento** | |
| `scoffs as you approach` | **sbuffa quando ti avvicini** | |
| `his spiel` | **il suo sproloquio** | |
| `with unrestrained glee` | **con una gioia sfrenata** | |
| `Syndicated Systems Account` | **conto Syndicated Systems** | nome del prodotto, resta |
| `"Just sign here."` | **«Firmi qui.»** | cortesia dentro la battuta |
| `You can't shake the feeling` | **Non riesci a scuoterti di dosso la sensazione** | |
| `an interceptor, a light freighter, and a transport ship` | **un intercettore, un mercantile leggero e una nave da trasporto** | |

## 3. Difficoltà

1. **Cinque frasi condivise** (unità 5–9): rilette da L135 e confrontate.
2. **Cinque cifre** in convenzione italiana, con un controllo che vieta le forme inglesi.
3. **La cortesia del cassiere** («Come possiamo aiutarla?») convive con la narrazione al «tu»: il controllo tollera una
   sola forma e verifica che non si propaghi.
4. **Un diario in prima persona senza genere**: «prima della mia libertà» invece di «prima che sia libero».
5. **`Syndicated Systems` resta nome di prodotto**: tradurlo renderebbe irriconoscibile il riferimento.
6. **Il venditore che cambia tono** («Eccoti di nuovo!»): in inglese «Welcome back!» è neutro rispetto al genere del
   giocatore, e la resa lo resta.
7. **Gate**: minimo 0,85 (unità 15), massimo 1,28 (unità 17).

## 4. Numeri osservati

```
unita' 17/17 · CONVERSATION 10 · LOGBOOK 4 · DESCRIPTION 2 · VALUE 1 · UI_LABEL 0 · token 0
contesti 2 completi (3 / 14) · 12 testi propri + 5 riletti · 17 distinti
tab 8 unita · virgolette 12 (6:2, 11:2, 13:2, 14:4, 17:2), nessuna dispari · quadre 0
parole EN 802 -> IT 786 (0.980) · rapporto 0.85 - 1.28, media 1.04
righe 172/210 · 47 prima / 49 dopo · confine riga 215 (start:hai space)
FAIL totale: 0 (29 controlli) · verify exit 0 (28 controlli)
sha256[:16] 24133aaf9c9f177d
```

## 5. Stato del progetto

```
TOTALE staging: 27450 unità · 867487 EN · 824269 IT
starts.txt: 64/113 (56,6%) · 3 lotti · 2874 EN -> 2793 IT
file completi: quarantotto · residuo traducibile (formula state.py): 4480
residuo misurato: 5147 unità / 109612 parole su 118 file
avanzamento: 27450/32924 unità (83,4%) · 867487/979975 parole (88,5%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`, nessun inizio caricato nel gioco.
- **Nessuna partita avviata**: non ho visto Delve, né il cantiere, né la banca.
- **Nessuna revisione umana**.
- **`starts.txt` è al 56,6%**: restano **49 unità** (`start:hai space`, `conversation:hai intro`,
  `ship:Grasshopper`).
- **Prossimo lotto**: `HANDOFF_L138_20261019.md` — righe **215–358**, **47 unità**, 1356 parole, **2 contesti
  completi**, **2 `VALUE`** (entrambi `Hai Origins`), **32 unità con tab**, **56 virgolette** con **quattro unità
  dispari** (307, 327, 331, 335).
