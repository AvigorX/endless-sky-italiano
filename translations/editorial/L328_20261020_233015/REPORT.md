# REPORT — L328 (`data/_ui/help.txt`, righe 72–116) — **SECONDO DI TRE LOTTI**

**Esito: lotto CHIUSO.** `check.py` esce 0 con **20 controlli**; `verify.py` esce 0 con **15 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). **Nessuna scrittura su `state.db`**.

## 1. Misure

| voce | inglese | italiano (approvato) |
|---|---|---|
| unità | 25 (`HELP`, tutte `APPROVED`) | 25 |
| parole | 988 | **850** (0,860) |
| contesti | 11 | **11** |
| segnaposto | **1** (`<View player info>`) | **1**, identico |
| virgolette | **10** (3 righe) | **10** |
| tab | **0** | **0** |

Rapporto **0,81 – 1,20**. La lingua approvata è **più corta** dell'inglese (0,86): le istruzioni tecniche inglesi usano perifrasi
(«can be brought up at any time», «will automatically plot»), l'italiano le comprime.

## 2. Invariante di SEGMENTO

```
SEGMENTO   72–116 · 25 unità proprie · 11 contesti · righe distinte
CONFINE    dopo la 116 c'è la 119 (help:fleet asteroid mining), NON inclusa
ALTRI      nessun altro lotto tocca queste righe
FILE       113 unità; con L327 la copertura sale a 53/113
```

Il test **non conta i lotti del file**: L329 deve poter arrivare senza farlo diventare rosso.

## 3. `outfitter` → «fornitore»: una convenzione da correggere

Il testo approvato usa **«fornitore»** in **5 unità** di questa finestra, e **mai** «emporio». Misura su tutto il corpus:

| forma | staging | `APPROVED` |
|---|---|---|
| «fornitor-» (fornitore/fornitori) | **81** | **13** |
| «emporio» | **53** | **0** |

Nei lotti precedenti avevo fissato `outfitter` → **«emporio»** (dichiarando che «il corpus vince»). La misura completa dice il contrario:
**«fornitore» è maggioritario**, e nelle unità approvate è **l'unica forma**. La correzione è registrata qui come **divergenza aperta**:

- **non** ritocco il testo approvato (non ne ho titolo);
- **non** ritocco i 53 «emporio» già in staging (sarebbe una riscrittura di 300+ unità fuori da un lotto);
- **L329**, che contiene 5 unità con `outfitter` **`PENDING`**, userà **«fornitore»** per coerenza col testo approvato dello stesso file.

## 4. Le etichette del pannello flotta: sei virgolette in una riga

```
106  You can also park your ships by selecting them and pressing "Park", or by pressing "Park Local" or "Park All".
     → Puoi anche parcheggiare le navi selezionandole e premendo "Parcheggia", oppure "Parcheggia le locali" o "Parcheggia tutte".
```

Tre coppie in una riga sola. Le etichette sono **tradotte** — coerentemente con L327 («Gestisci piloti», «Preferenze») — e il test le
verifica **una per una**: «Salva ordine», «Parcheggia», «Parcheggia le locali», «Parcheggia tutte».

## 5. Che cosa insegna la finestra

Le 25 unità sono **tutte istruzioni sui pannelli**, e insieme descrivono **un'interfaccia sola**:

| contesto | che cosa insegna |
|---|---|
| `map advanced` | la mappa come strumento: **rotta automatica**, `Shift+clic` per tratte multiple, `Control+clic` per selezionare senza rotta |
| `ports` | il pannello dei porti: **cliccare qualsiasi cosa** (nome, governo, righe dei pianeti, merci) ricolora la mappa; **clic destro** manda le scorte in un punto |
| `shops` | cantieri e fornitori: categorie **chiudibili**, `Shift+clic` le apre o chiude tutte, `F` per cercare |
| `stars` | la **modalità stellata** (tasto `T`): le stelle decidono quanta **energia solare** e **vento solare** c'è |
| `danger` | l'**icona di allarme** accanto al nome del sistema |
| `multiple ships` | **trascinare** le navi per riordinarle, «purché tu sia atterrato»; la prima è l'**ammiraglia** |
| `player info` | patrimonio netto, valutazione di combattimento, stipendio, licenze, diario, missioni: **<View player info>** apre tutto, anche in volo |
| `fleet management` | ordinare per colonna, **«Salva ordine»** per renderlo permanente, parcheggiare le navi |
| `ship info` | rinominare, **riordinare cannoni e torrette** trascinando, espellere carico in volo |
| `multiple ship controls` | ordini alle scorte: selezione, **clic destro** (punto vuoto / nave ostile / bersaglio amico), **gruppi di controllo** con `Control+numero` |

È il **manuale dell'interfaccia**, e la sua qualità sta in una cosa: **ogni affermazione è verificabile nel gioco**. La trascrizione la
conserva senza «migliorarla».

## 6. Cosa NON è verificato (dichiarato)

- **Il testo non è una nuova traduzione**: è quello approvato, generato **dal database** e verificato.
- **Copertura parziale**: **53 su 113** unità del file.
- **`outfitter`**: divergenza **aperta** (fornitore 81+13 contro emporio 53); non uniformata.
- **Nessun testo visto nel gioco**; nessuna revisione umana **nuova**.
