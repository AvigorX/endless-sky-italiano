# REVIEW — L69 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Coerenza con L68 (stesso file, stessa linea)

- **`Casa Myurej`**, **`le Casate`**, **`Casate del Popolo`**, **`Successori`**, **`sfera di dati`**,
  **`Rintraccia`/`Cerca`**: tutte forme già fissate in L68 e riusate qui senza reinventare.
- **`Riiria`** resta femminile e «ladra»: in L68 è «ladra ben nota». Qui il complice parla di lei come di un
  capo temuto («Riiria dice…»), e i pronomi italiani concordano al femminile («cercala»).
- **Registro per personaggio**: Casa Myurej parla in modo cerimonioso (nel lotto precedente); qui c'è un
  Successore comune, spaventato, che scrive di fretta. Il suo italiano è popolare e diretto, non cerimonioso.
- **`Ojde`** è il nome della nave cargo: invariato, come i toponimi `Maspa-Viir-Kella` e `Osolaa-Uuoru`.

## 2. Nodi traduttivi aperti (dichiarati)

- **`lux filters`** (unità 23, 25): reso «filtri di lusso», che è il significato di `lux` = *luxury* dato
  dalla descrizione stessa («luxury filter units»). Se un lotto futuro introducesse `lux` come **marchio**
  (per esempio un modello di filtro), la scelta va rivista: oggi il testo lo tratta come categoria.
- **`programmed water`** (unità 20): «acqua programmata». Il concetto non è spiegato nel gioco; la resa è
  letterale e resta un tecnicismo dei Successori, non un errore da addolcire.
- **`Council pools`** (unità 20): «vasche del Consiglio». `Council` è tradotto **Consiglio** come altrove;
  il riferimento istituzionale non è specificato in questo lotto.
- **`icons'f their folly`** (unità 7): «icone della propria follia». Il genitivo dialettale inglese è
  ambiguo (le Casate vedono i relitti come icone *della loro* follia). La resa tiene il possessivo riferito
  alle Casate; se un lotto successivo chiarisse che è la follia dei rifugiati, si cambia una parola.
- **`the alien`** (unità 7): «quello straniero» — è il giocatore. In L68 la stessa parola era «uno
  straniero»; qui il complice ne parla con timore, e il registro regge.

## 3. Refuso del sorgente

Unità 12: **«Not longer after»** (per «Not long after»). La traduzione non replica l'errore («Poco dopo
aver guidato…») e il difetto è annotato qui, come prescritto: il repository del gioco resta intatto.

## 4. Duplicati, virgolette, tab

- **1 gruppo di duplicati inglesi**: `Track down Riiria` (unità 28 e 30), due missioni distinte con lo
  stesso nome. Resa identica corretta; nessuna resa ripetuta fra inglesi diversi.
- **4 virgolette** su 31 unità, **0 dispari**: due coppie (unità 7, messaggio; unità 25, scheda tecnica).
  Parità per unità verde.
- **27 tab** su **21 unità** con tab iniziale: 6 unità ne hanno due (le scelte di dialogo indentate, unità
  4, 5, 14, 15). Il costruttore li deriva dal sorgente: nessun tab scritto a mano.
- **0 quadre**, **0 backtick**: assenze dichiarate.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 31 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessun test a schermo della stazione deserta, del relitto o dei due rami.
- **Nessun allineamento** delle due `Casata Myurej` di L45 (già dichiarato in L68).
- **Nessuna verifica del registro**: la voce del complice è valutata come testo, non misurata.

## 6. Rischi residui

- **L'invariante è di segmento e cita L68**: il `verify.py` asserisce `49 unità prima della riga 118`. Se
  un lotto futuro coprisse quelle righe, il numero cambierebbe — ma è un'informazione vera e utile
  («eredita L68»), non una copertura cumulativa travestita: si controlla il **segmento**, non il totale.
- **`131 unità dopo la 197`** è cablato: se il file crescesse, diventerebbe rosso. È voluto.
- **Il manifesto** (unità 18–23) è verificato solo per struttura (tab, token, virgolette): nessun controllo
  misura la coerenza delle unità di misura con il testo della scheda tecnica.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto per intero |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (35 controlli), `verify.py` exit 0 (46 controlli), sha256 `7ab0a2bee4dc90a6` |
