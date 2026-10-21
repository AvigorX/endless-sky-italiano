# REPORT — L138 · `data/starts.txt` (quarto inizio: Greenwater, il venditore Hai, la Pristine Jewel)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| l'inizio bloccato | 1–4 | 215–223 | `Hai Origins`, Greenwater, le astronavi giocattolo, «Questo inizio è bloccato» |
| l'inizio sbloccabile | 5–8 | 227–230 | lo stesso nome, la stessa premessa più breve, le condizioni di sblocco |
| il diario | 9 | 278 | l'anticipo, gli interessi esorbitanti |
| la storia del mondo | 10–17 | 279–286 | **cinque frasi rilette** da L135, poi gli Hai, gli Unfettered, gli Sheragi |
| l'arrivo | 18–20 | 288–290 | il Polo Nord, la folla, il prestito da 1,431 milioni, lo scontro con l'Hai grigio |
| il dialogo | 21–29 | 293–314 | «Stai per diventare capitano, vero?», le tre risposte, l'inchino |
| la flotta | 30–38 | 317–335 | il mazzo di chiavi, la pensione, la Pristine Jewel, il prezzo, le tre domande |
| l'affare | 39–44 | 338–351 | «Affare fatto», il tablet, le chiavi, il saluto |
| il cantiere | 45–47 | 355–358 | il chiosco di sicurezza, la firma, le porte scorrevoli |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Hai Origins` ×2 | **identico** | due `VALUE`, due inizi |
| `rich and mixed culture thanks to its climate` | **cultura ricca e mista grazie al suo clima** | |
| `toy spaceships` | **astronavi giocattolo** | |
| `down payment` | **anticipo** | |
| `giant, intelligent rodents` | **roditori giganti e intelligenti** | |
| `docile and peaceful` | **docili e pacifici** | |
| `deteriorating worlds` | **mondi in degrado** | |
| `1.431 million credits` | **1,431 milioni di crediti** | |
| `0.3%` · `4,836 credits per day` | **0,3%** · **4.836 crediti al giorno** | |
| `a gray-furred Hai wearing a flight suit` | **un Hai dal pelo grigio in tuta da volo** | |
| `Not that that should matter` | **Non che importi** | |
| `pay it forward` | **restituire il favore** | |
| `a tough ask` | **un osso duro** | |
| `a Grasshopper interceptor` | **un intercettore Grasshopper** | |
| `1.132 million credits` | **1,132 milioni di crediti** | quattro occorrenze |

## 3. Difficoltà

1. **Due `VALUE` identici**: due inizi distinti con lo stesso nome. Il controllo è una lista di coppie, e un secondo
   controllo verifica che i due inizi **non dicano la stessa cosa** sulle condizioni di sblocco.
2. **Quattro battute aperte** (26, 36, 37, 38): riprodotte, con un controllo che vieta di chiuderle.
3. **32 unità con tab su 47**: il costruttore li antepone dal sorgente, la resa si scrive senza.
4. **Cinque frasi rilette** da L135 (unità 10–14).
5. **Quattro cifre** in convenzione italiana, con un controllo che vieta le forme inglesi.
6. **Un errore mio nel controllo**, non nel testo: `by[8]['italian'].startswith('Per sbloccare...')` falliva perché
   l'unità 8 inizia con un tab. Corretto con `.lstrip('\t')`; la traduzione non è stata toccata.
7. **Gate**: minimo **0,71** (unità 42, `"Great!" He holds out a data tablet. "Just sign here..."`), massimo **1,78**
   (unità 40, `"We do!"` → «"Affare fatto!"»: l'inglese è cortissimo, e la resa italiana non può esserlo altrettanto).
   Entrambi dentro il gate `0,55–1,90`, e la soglia non è stata toccata.

## 4. Numeri osservati

```
unita' 47/47 · CONVERSATION 32 · LOGBOOK 7 · DESCRIPTION 6 · VALUE 2 · UI_LABEL 0 · token 0
contesti 2 completi (8 / 39) · 42 testi propri + 5 riletti · 45 distinti
tab 32 unita · virgolette 56 con 4 dispari (26, 36, 37, 38: una ciascuna) · quadre 0
parole EN 1356 -> IT 1295 (0.955) · rapporto 0.71 - 1.78, media 1.06
righe 215/358 · 64 prima / 2 dopo · confine riga 365 (ship:Grasshopper)
FAIL totale: 0 (32 controlli) · verify exit 0 (31 controlli)
sha256[:16] ab536b2d9a5a2c29
```

## 5. Stato del progetto

```
TOTALE staging: 27497 unità · 868843 EN · 825564 IT
starts.txt: 111/113 (98,2%) · 4 lotti · 4230 EN -> 4088 IT
file completi: quarantotto · residuo traducibile (formula state.py): 4433
residuo misurato: 5100 unità / 108256 parole su 118 file
avanzamento: 27497/32924 unità (83,5%) · 868843/979975 parole (88,7%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 5 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (31 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 47 unità `PENDING`, nessun inizio caricato nel gioco.
- **Nessuna partita avviata**: Greenwater e la scena del venditore non sono state viste.
- **Nessuna revisione umana**.
- **`starts.txt` è al 98,2%**: restano **2 unità** (`ship:Grasshopper`, righe 365–366), che **chiudono il file**.
- **Prossimo lotto**: `HANDOFF_L139_20261019.md` — righe **365–366**, **2 unità**, **2 `TEXT`** che sono **nomi di
  equipaggiamento fra virgolette** (`"Benga" Atomic Thruster`, `"Biroo" Atomic Steering`), **zero token**, **zero
  virgolette da tradurre** (le due si conservano).
