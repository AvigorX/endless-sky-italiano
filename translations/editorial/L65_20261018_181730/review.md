# REVIEW — L65 · `data/human/culture conversations.txt`

Revisione del lotto dopo la chiusura dei controlli.

## 1. Coerenza con L58–L64

- Quattro scene diverse in un solo lotto, tenute insieme dal narratore in seconda persona e dal tempo
  presente. La voce non cambia; cambia il **materiale**: cronaca di spazioporto, servizio giornalistico,
  commedia commerciale.
- Il lessico delle istituzioni resta lo stesso dei lotti precedenti: «Repubblica», «Sindacato», «Mondi del
  Paradiso», «Deep», «Free Worlds» (invariato), «Marina».

## 2. Nodi traduttivi aperti (dichiarati)

- **`Bastion`, `Argosy`, `Gatling Gun`, `Plasma Cannon`**: classi e armi del gioco, invariate. «mitragliatrice
  Gatling» rende il tipo d'arma senza tradurre il nome proprio.
- **`Delta V`** (4): nome dell'azienda, invariato.
- **`Rim`** e **`Dirt Belt`** (8): resi «Bordo» e «Cintura di Terra». Sono toponimi del gioco già usati nei
  lotti delle campagne Free Worlds; la resa è coerente con quelli, non inventata qui.
- **`Alphas`** (8): «gli Alfa», come nei lotti precedenti.
- **`Pug`** (13): invariato (specie aliena).
- **`Sestor`** (16, nell'etichetta): resta invariato dentro la chiave.
- **«Fish that's a dish»** (23, 27): il bisticcio si regge sull'omografia *dish*; in italiano funziona con
  «piatto» (recipiente e aggettivo), ed è l'unico modo per non perdere la battuta. Il cameriere la ripete
  tre volte: la traduzione mantiene la ripetizione.

## 3. Virgolette

**22 virgolette, 0 dispari.** Nessun discorso lasciato aperto in questo lotto: il dialogo del ristorante
è chiuso correttamente, e il menù usa il corsivo tipografico del sorgente (nessun apostrofo curvo).

## 4. Duplicati

1 gruppo (26/30): «No, grazie» è la stessa opzione di rifiuto in due punti dell'albero. Resa identica per
necessità dichiarata. Nessuna resa ripetuta fra unità con inglese diverso.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 43 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: verifica sui file.
- **Nessuna verifica di runtime** delle quattro varianti dell'anniversario né dei due rami del ristorante
  (29/30, 40/41).

## 6. Rischi residui

- **Le quattro etichette di stato del mondo** (`war ongoing`, `war over`, `zenith bombed`,
  `sestor beaten at farpoint`) sono chiavi: se il gioco le cambia, le varianti non si mostrano più. Sono
  elencate una per una proprio per renderle verificabili.
- **Il menù truffa** (31) elenca cifre precise (20, 30, 50, 80, 100, totale 379): i numeri sono nel testo
  e non vanno arrotondati né «corretti» — il totale è volutamente sproporzionato rispetto ai 99 crediti
  pubblicizzati, ed è la gag.
- **Il file è al 78,6%**: restano 80 unità, in gran parte `Exotic Life`.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, documenti |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (36 controlli) |
