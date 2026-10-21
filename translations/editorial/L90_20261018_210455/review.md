# REVIEW — L90 · `data/successors/successor culture conversations.txt` (primo lotto del file)

Documento scritto **dopo** la chiusura del lotto, per colmare il gap dichiarato nel `REPORT.md` §7. I numeri
sono quelli di `translation.json` (`45fd22aca9b71868…`) e le coppie EN→IT citate sono state rilette nel file,
non ricostruite a memoria.

## 1. Coerenza con i lotti precedenti

- **Successori / Predecessori** (L81–L85, L86–L89): il registro resta quello delle conversazioni culturali —
  osservazione al presente, nessun arcaismo finto. Nel dialogo dei Successori il «tu» resta moderno anche dove
  l'inglese usa `thou` (glossario, §8 del checkpoint).
- **`<ship>`** invariato (unità 1, 10, 18): è il segnaposto del nome della nave del giocatore.
- **`spaceport`** → «spazioporto» (forma già usata in tutti i file `successors`); **`landing pad`** →
  «piazzola di atterraggio».
- **`outfit` / `equipment`**: qui non ricorrono; `datapad` e `translation device` sono oggetti, non
  equipaggiamenti, e restano rispettivamente «datapad» e «dispositivo di traduzione».
- **`data-sphere`** → «sfera di dati», distinta dalla «sfera di metallo morfico» dell'unità 1 (glossario).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `(Take it.)` | `(Prendilo.)` / `(Prendila.)` | 3 / 13 | stesso inglese, oggetto di genere diverso: bastone / sfera. Unica deroga ammessa al «duplicato identico» |
| `(Decline.)` / `(Refuse.)` | `(Rifiuta.)` / `(Non accettare.)` | 4 / 14 | due inglesi distinti, due rese distinte: non sono sinonimi nel testo (il secondo rifiuta un dono) |
| `(Try a bite.)` | `(Assaggiane un pezzo.)` | 6 | `bite` è porzione, non atto |
| `trills warmly` | `trilla con calore` | 15 | `trill` è il verso dei Successori, non un suono qualsiasi |
| `undulate` | `ondulano` | 18, 34 | moto ricorrente della specie |
| `dull, low hum` | `cupo ronzio basso` | 28, 33 | `dull` è timbrico, non «noioso» |
| `lilting melody` | `melodia cadenzata` | 21 | `lilting` è il ritmo, non l'allegria |
| `rapturously` | `estatico` | 27 | il movimento è fisico |
| `splittingly high note` | `nota acutissima` | 21 | `splitting` è intensità |
| `milling about` | `si aggirano` | 17 | non «macinano»: è il vagare nella vasca |
| `pre-arranged barriers` | `barriere predisposte` | 12 | `pre-arranged` è allestimento, non accordo |

## 3. Nodi aperti (non risolti qui, da non dedurre dopo)

1. **`(Return to my ship.)` alle unità 26 e 31** è reso identico («Torna alla mia nave.»): sono due punti di
   uscita della stessa scena con lo stesso inglese, quindi la ripetizione è legittima e nessun controllo la
   segnala come errore.
2. **Il canto tradotto a frammenti** (unità 23) non è poesia: è la trascrizione parziale del dispositivo di
   traduzione. Reso con i puntini di sospensione del sorgente e nessun tentativo di metrica.
3. **`succulent`** (unità 2) reso «succulenta»: è il nome botanico corrente, non un prestito forzato. Se il
   glossario dovesse imporre «pianta grassa», la sostituzione è meccanica e circoscritta a una unità.
4. **`datapad`** resta inglese come nome d'oggetto: non esiste un equivalente italiano altrettanto riconoscibile.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 34 unità del file restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste conversazioni è stata vista a schermo.
- **Nessuna revisione umana**: il lotto non è approvato.
- **Finestra ridotta**: il contratto `HANDOFF_L90` prevedeva 76 unità; ne sono state tradotte 34 (righe 1–142),
  con la coda dichiarata a `HANDOFF_L91`.

## 5. Rischi residui

- **28 tab su 34 unità**: un tab mancante sposta la battuta fuori dal blocco di scelta. Il `check.py` li verifica
  per indice, non solo in totale.
- **Due virgolette sole nel lotto** (unità 23): un conteggio pari può nascondere una virgoletta nel punto
  sbagliato; è stata letta a mano.
- **Coppia 3/13**: le due rese differiscono di una sola vocale finale. Una «correzione» che le uniformasse
  farebbe fallire due controlli insieme (duplicato non giustificato e genere sbagliato).

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (26 controlli), sha256 `45fd22aca9b71868` |
