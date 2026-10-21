# REPORT — L171 · `paradise world jobs.txt` (quinto lotto: dodici evacuazioni)

## 1. Contenuto

Dodici missioni di evacuazione da Martini dopo i bombardamenti nucleari, in coppie speculari: **residenti** (gruppo e
singolo), **famiglia / singolo di lusso**, **turisti** (singolo, coppia, famiglia, gruppo), **uomini d'affari** (gruppo e
singolo), **personale sanitario** (medici e squadra di ricerca e soccorso, entrambi «congedati»).

## 2. Scelte

| nodo | IT | unità |
|---|---|---|
| `had their <martini house> destroyed` | **ha visto la propria <martini house> distrutta** | 2, 4, 6, 8 |
| `on a luxury ship` | **su una nave di lusso** | 6, 8 |
| `to see its sights` | **per vederne le bellezze** | 10-16 |
| `conducting a business trip` | **per un viaggio di lavoro** | 18, 20 |
| `businessmen` | **uomini d'affari** | 18, 20 |
| `discharged` | **congediati** | 22, 24 |
| `search and rescue` | **ricerca e soccorso** | 24 |
| `their homes` / `their home` | **alle loro case** / **a casa loro** | 16, 18 / 22, 24 |

## 3. Difficoltà

1. **`<planet>` 28 volte**: record della campagna, su **soli 5 simboli**. Sei unità (10, 12, 14, 16) hanno **due**
   `<planet>` nello stesso testo, e il controllo verifica la sequenza, non solo il totale.
2. **10 `VALUE` distinti su 12**: le coppie sono **1/5** (`residents`) e **3/7** (`resident`), e la resa deve essere
   identica. Il plurale e il singolare invece **non** si uniformano: 2/6 dicono «Questi residenti / Trasportali», 4/8
   «Questo residente / Trasportalo».
3. **`<martini house>` 4 volte** (idx 2, 4, 6, 8): segnaposto composto, verificato intero.
4. **Il salto vuoto 988–1229**: nessuna unità per 242 righe. Il `verify.py` lo verifica invece di fidarsi del confine.
5. **Errore in corsa (mio, doppio)**: il controllo sugli apici pretendeva **0** apici in italiano; sono **2**, perché
   «uomini d'affari» ne richiede uno. Corretto legando ogni apice alla sua causa. Poi il mio patch *per riga* ha
   inghiottito una riga di codice (`TOK = ...`) e il `verify.py` è morto con `NameError: TOK` — ripristinata.
6. **Gate**: 0,90–1,03, media 1,00.

## 4. Numeri osservati

```
unita' 24 · 12 VALUE · 12 DESCRIPTION · tutte PENDING
token 55 su 5 simboli · <planet> 28 · <martini house> 4 · 0 tab · 0 virgolette
22 testi distinti · 12 contesti · righe 719/987
parole 497 -> 470 (0.946) · rapporto 0.90 - 1.03, media 1.00
FAIL totale: 0 (27 controlli) · verify exit 0 (22 controlli) · sha256[:16] d494b88bbb2ea449
SALTO VUOTO 988-1229 verificato: zero unita
```

## 5. Stato del progetto (dopo L171)

```
TOTALE staging: 28109 unità · 885104 EN · 841842 IT
paradise world jobs.txt: 113/131 (86,3%) · 5 lotti
residuo traducibile (formula state.py): 3821
endless-sky HEAD b4aa3bac3, 0 modifiche
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (22 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 24 unità `PENDING`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Quinto lotto del file**: contratto successivo in `HANDOFF_L172_20261019.md`.
