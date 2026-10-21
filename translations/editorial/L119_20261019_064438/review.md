# REVIEW — L119 · `pirate jobs.txt` (difese, furti di carico, assassinii) · **file chiuso**

Coppie EN→IT rilette in `translation.json` (`51189eab238776c8…`). Tutte le 77 unità sono **`PENDING`**.

## 1. Voce e registro

- **Anarchia e difesa**: registro dei pirati, diretto, con l'imperativo al «tu» («Sconfiggile per difendere
  l'anarchia!», «Torna su `<destination>`.»).
- **Scena della difesa**: la folla parla per grida («Siamo sotto attacco! `<planet>` è sotto attacco della
  Marina!»), e la voce narrante resta al presente («All'improvviso senti voci concitate e grida fuori»).
- **Assassinii**: burocratico e distaccato («Assassinalo entro `<day>` per mandare un messaggio alla
  Repubblica. Il compenso è `<payment>`. Attenzione: potrebbe essere pesantemente difeso.»).
- Nessun «voi» (verificato nei due script).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Merchants near <system>` · `Defend <planet>` · `Convoy near <system>` · `Assassinate a political target` | **identici** | 1, 5, 9, 17, 21, 29, 33, 42, 46, 50, 54, 58, 62, 66, 70, 74 | 4 nomi per 16 unità |
| `Local Navy / Syndicate / militia forces are attacking` | **Forze della Marina / del Sindacato / della milizia … stanno attaccando** | 6, 18, 30 | |
| `The … fleets have been defeated.` | **Le flotte … sono state sconfitte.** | 7, 19, 31 | |
| `collectively pay you <payment>` | **ti pagano collettivamente `<payment>`** | 8, 20, 32 | |
| `thank you for helping to drive off the Navy` | **ti ringraziano per aver contribuito a respingere la Marina** | 12, 24, 36 | senza pagamento |
| `What if …` — grida fuori | **Siamo sotto attacco! … è sotto attacco della Marina!** | 13, 25, 37 | 2 virgolette per unità |
| `combat-worthy ship` | **nave in grado di combattere** | 13, 25, 37 | |
| `(Stay here until the fight is over.)` | **(Resta qui finché la battaglia non è finita.)** | 14, 26, 38 | tab conservato |
| `(Join the defense fleet.)` | **(Unisciti alla flotta di difesa.)** | 15, 27, 39 | tab conservato |
| `preparing to repel the … attack` | **si preparano a respingere l'attacco della Marina / del Sindacato / della milizia** | 16, 28, 40 | tab conservato |
| `Cargo stolen from a merchant ship…` | **Carico rubato a una nave mercantile, che…** | 41 | descrizione equipaggiamento |
| `A local warlord is interested in having the cargo on the <npc>` | **Un signore della guerra locale è interessato a impossessarsi del carico della `<npc>`** | 43, 47, 51 | |
| `Plunder it` | **Saccheggialo** | 43, 47, 51 | |
| `but you don't have the secret cargo!` | **ma non hai il carico segreto!** | 44, 48, 52 | |
| `take the secret cargo from your cargo hold` | **prendono il carico segreto dalla tua stiva** | 45, 49, 53 | |
| `A … politician who is worrying local …` | **Un politico … che sta preoccupando i … locali** | 55, 71, 75 | |
| `in their ship, the <npc>` | **sulla sua nave, la `<npc>`** | 55–75 | |
| `Be advised that they may have escorts / be heavily defended.` | **Attenzione: potrebbe avere delle scorte / essere pesantemente difeso.** | 55–75 | |
| `The target has been destroyed.` | **L'obiettivo è stato distrutto.** | 56, 60, 64, 68, 72, 76 | |
| `for your payment` · `for payment` | **per il tuo compenso** · **per il compenso** | 56/60/64/72 · 68/76 | differenza del sorgente riprodotta |
| `A band of slave traders / pirates / drug traders thank you` | **Una banda di trafficanti di schiavi / di pirati / di trafficanti di droga ti ringrazia** | 57, 69, 77 | |
| `thanks you for eliminating the politician that threatened them` | **per aver eliminato il politico che lo minacciava** | 61 | |
| `Syndicate spacenear` (sorgente) | **spazio del Sindacato vicino a** | 67 | refuso normalizzato |

## 3. Nodi aperti (da non dedurre dopo)

1. **`CONVERSATION` è un tipo nuovo** e cambia la forma del lotto: 12 unità, di cui **9 con tab iniziale** e 3
   con **2 virgolette** ciascuna. Il prossimo file (`campaign events.txt`) ha **41 unità con tab su 52** nel primo
   segmento: il trattamento del tab non è un caso isolato, è la norma di questo file.
2. **Un contesto da una sola unità** (`outfit:Secret Cargo`): la distribuzione dei contesti non va «resa
   uniforme»; si misura.
3. **Un doppio di resa dichiarato** (65/73, refuso «and»): il controllo ammette **uno** e solo quello. Un secondo
   doppio non dichiarato fa fallire il lotto.
4. **Le due varianti «for your payment» / «for payment»** sono distinte nel sorgente e restano distinte in
   italiano: non è una svista, è la resa fedele di due testi diversi.
5. **Il `verify.py` di questo lotto non è riusabile per il prossimo file**: l'invariante di file vale finché non
   si chiude il file nuovo. Per `campaign events.txt` serve un invariante di **segmento**.
6. **Il conteggio delle unità condivise era sbagliato** (2 invece di 3: c'era anche un nome `VALUE`): corretto
   l'atteso nel `check.py`.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 77 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: le tre scene di difesa non sono mai state viste, e i 106 token non sono stati
  osservati sostituiti.
- **Nessuna revisione umana**.
- **Il file è completo in staging, non nel gioco**: 279/279 tradotte, zero caricate.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (31 controlli), 279/279 righe coperte |
