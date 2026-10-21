# REPORT — L120 · `campaign events.txt` (Giorno del Ricordo, l'attentato, la secessione)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| Giorno del Ricordo | 1–6 | 28–34 | due voci di diario sugli Alphas, la commemorazione, la genetica, la pelle verde |
| Geminus e Martini | 7–12 | 132–141 | l'Arsenale distrutto, la Borsa Galattica, lo spazioporto di fortuna |
| Bourne e i Mondi Liberi | 13–16 | 145–158 | mondo industriale, capitale dei Mondi Liberi, voce di diario |
| l'attentato | 17–20 | 166–169 | la piazza, l'ultimatum, le esplosioni nucleari |
| la partenza forzata | 21–30 | 175–189 | l'ufficiale, il cannone al plasma, le risposte del giocatore |
| Martini | 31–40 | 198–214 | le nubi, l'ospedale da campo, la seconda scena |
| l'arresto | 41–46 | 218–230 | legge marziale, licenza revocata, nave perduta |
| ritorno in orbita | 47–52 | 231–242 | il telegiornale, tre chiusure alternative |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `the Alphas` | **gli Alphas** | nome di specie: **invariato** (regola delle specie) |
| `Remembrance Day` | **il Giorno del Ricordo** | ricorrenza, non nome proprio di luogo |
| `the Free Worlds` | **i Mondi Liberi** | fazione politica; fra virgolette quando il sorgente le mette |
| `Republic Navy Yard` | **Arsenale della Marina della Repubblica** | `Navy Yard` = arsenale militare |
| `Galactic Stock Exchange` | **la Borsa Galattica** | |
| `Republic Navy` · `Parliament` | **la Marina della Repubblica** · **il Parlamento** | |
| `Carrier squadron` | **squadrone di navi portatrici** | coerenza con `carriers` di L115 |
| `genetically engineered super-soldiers` | **super-soldati geneticamente modificati** | |
| `photosynthetic skin` | **pelle fotosintetica** | |
| `bogeyman story` | **una storia per spaventare i bambini** | |
| `genetic resequencing technology` | **tecnologia di riordino genetico** | |
| `viable offspring` · `enclaves` | **prole vitale** · **enclavi** | |
| `an ultimatum` | **un ultimatum** | prestito entrato nell'uso |
| `martial law` · `impounded` | **legge marziale** · **sequestrata** | |
| `Naval Reserve Command` | **Comando della Riserva Navale** | |
| `Permanently Revoked` | **«Revocata in via definitiva»** | timbro sulla licenza, fra virgolette come nel sorgente |
| `job boards` | **bacheche dei lavori** | |
| `disaster response plan` | **piano di risposta al disastro** | |
| `Paradisians` | **Paradisiani** | abitanti del pianeta Paradis |
| `hotshot captain feeling full of themself` | **un capitano presuntuoso si sente tanto importante** | |
| `frogmarched` | **portato via a forza** | |

## 3. Difficoltà

1. **Il tab è la norma**: 41 unità su 52 iniziano con `\t`. Le parti non li contengono, li antepone il costruttore;
   il controllo conta **unità** e **occorrenze per unità**.
2. **58 virgolette di dialogo**: a differenza delle chiavi `Preferences` di L115–L116, qui vanno tradotte; il
   controllo verifica il **numero per unità**, non il contenuto.
3. **Nessun `VALUE`**: il controllo dei nomi di missione è un'asserzione vuota, scritta e dichiarata.
4. **Un `LOGBOOK`**: tipo non trattato da L68; reso come voce di diario, senza imperativi di missione.
5. **Contesti 6 / 9 / 37**: il terzo assorbe 37 unità (tutta la scena su Geminus e Martini). Non si ribilancia.
6. **Registro incoerente, corretto**: l'unità 41 era al «lei» e il resto del lotto al «tu». Riscritta prima della
   verifica, e il `check.py` ora rifiuta le forme di cortesia.
7. **Una firma ambigua**: `rogue planets down south` combaciava con **due** testi (unità 27 e 37, che condividono
   l'apertura ma non l'esito). Sostituita con `here on Geminus was bombed`, unica.
8. **Un atteso sbagliato**: il `check.py` esigeva che tutti i contesti iniziassero con `mission:`, ma il file ha
   anche `event:…`. Corretto l'atteso (lista esplicita), non il dato.

## 4. Numeri osservati

```
unita' 52/52 · MISSION_TEXT 41 · DESCRIPTION 9 · LOGBOOK 2 · VALUE 0 · tutte PENDING
contesti 3 (6 / 9 / 37) · testi distinti 45 (7 coppie ripetute)
tab 41 unita · virgolette 58 (dialogo) · token 5 · quadre 0 · backtick 0
parole EN 2255 -> IT 2193 (0.972) · rapporto 0.69 - 1.39, media 1.00
righe 28/242 · file 52/150 (34,7%) · 0 prima / 98 dopo · confine riga 282
FAIL totale: 0 (32 controlli) · verify exit 0 (29 controlli)
sha256[:16] a4f3e6160ea73524
```

## 5. Stato del progetto

```
TOTALE staging: 26625 unita · 841173 EN · 798839 IT
campaign events.txt: 52/150 (34.7%) · 1 lotto · 2255 EN -> 2193 IT
file completi: quarantatre · residuo traducibile (formula state.py): 5305
residuo misurato: 5936 unità / 135809 parole su 123 file
avanzamento: 26625/32924 unità (80,9%) · 841173/979975 parole (85,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 52 unità restano `PENDING`; nessun evento è stato caricato nel gioco.
- **Nessuna revisione umana**.
- **Il file è aperto**: 98 unità residue (righe 282–3468), un segmento successivo in `HANDOFF_L121`.
- **`Alphas` resta invariato**: è una scelta di glossario, non una verifica sul gioco.
