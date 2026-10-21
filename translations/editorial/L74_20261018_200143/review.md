# REVIEW — L74 · `data/successors/successor 2 ghosts aqrabe.txt`

## 1. Coerenza con la linea Successors (L68–L73)

- **Casa X / Casate / Nuove Casate / Predecessori / erede / pietre chiave / wormhole**: forme fisse, nessun
  termine reinventato.
- **Il registro arcaico di Tiliia** cresce rispetto a L73 (`thee`, `thy`, `hath`, `thou needest`, `'tis`):
  reso con il «tu» moderno formale, come in L45–L47 e L68–L73. Nessun «voi» reverenziale, che
  cambierebbe il rapporto fra i due personaggi.
- **`Aqrabe I- Sola` non compare** in questo lotto: Tiliia parla a nome della Casa e cita Aqrabe come terzo
  («Aqrabe ed io conveniamo», «estraendo un favore da Aqrabe»).
- **`Kaatrij`** era già un nome noto (L45: matrimonio Chydiyi–Myurej, `Kaatrij Monoglot Prompt`): qui è la
  Casa che presta il Vujlet, e il nome resta invariato.

## 2. Nodi traduttivi aperti (dichiarati)

- **`stellar metal garden`**: reso «giardino di metallo stellare». Se un lotto futuro parlasse dei
  *giardini* come strutture autonome (non attorno a una stella), la resa andrebbe rivista.
- **`cloaking device`** (30): il testo dice «se dovessi azzardare un'ipotesi… potresti descriverlo come»,
  quindi la traduzione mantiene l'incertezza del narratore. Se il gioco rivelasse che è un'altra cosa, il
  brano resta corretto perché è un'ipotesi in voce.
- **`New Houses` → «Nuove Casate»**: forma nuova. In staging `Casate` è usato per `Houses` (L45, L68); qui
  l'aggettivo è necessario e non crea ambiguità.
- **`so what thinks thou?`**: reso «Allora, che ne pensi?» — la forma arcaica interrogativa non ha equivalente
  italiano che non suoni finto.
- **`an observer`** (38): «un osservatore», senza specificare il genere, come per Ijaset in L72.
- **`its long tendrils snaking into various ship systems like some sort of infection`**: «viticci» (non
  «tentacoli») per non confonderlo con i tentacoli dei Successori.

## 3. Due `(Retreat.)` identici

Unità **12** e **16**: stesso inglese, stessa resa «(Ritirata.)». È l'unico gruppo di duplicati del lotto.
Il `check.py` lo dichiara (`1 gruppo, 2 unità`), il `verify.py` verifica che la resa sia **identica** e che
**nessun'altra** resa si ripeta fra inglesi diversi. Le due scelte opposte sono invece distinte:
`(Press on.)` → «(Insisti.)», `(Keep going.)` → «(Continua.)».

## 4. Tipi che cambiano segno rispetto a L73

| tipo | L73 | L74 |
|---|---:|---:|
| `CONVERSATION` | 6 | **0** (dichiarato) |
| `DIALOG` | 1 | **0** (dichiarato) |
| `UI_LABEL` | 0 | **1** (unità 19) |
| `LOGBOOK` | 3 (2 testi + 1 categoria) | **1** (testo, forma diretta) |
| `VALUE` / `DESCRIPTION` | 3 / 3 | **2 / 2** |

I controlli negativi di L73 sono diventati positivi qui: è il motivo per cui ogni lotto rimisura invece di
copiare (decisione 119).

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: le 38 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la scena della stella, l'eruzione solare e il Vujlet non sono state viste
  a schermo.
- **La `label` `no shields`** resta in inglese per scelta: è un bersaglio di salto, tradurla romperebbe la
  missione.
- **Nessuna verifica del registro**: i tre registri (Tiliia cerimonioso, la voce narrante, i Successori
  studiosi) sono valutati come testo.

## 6. Rischi residui

- **`0,67` è il rapporto minimo** (unità brevi come «(Ritirata.)» con parentesi): dentro il gate, nessuna
  riscrittura.
- **`1,70` è il massimo** (unità 20, la variante senza scudi): vicino al limite alto, quindi una riscrittura
  futura di quel brano deve restare corta.
- **Il `verify.py` asserisce 51 prima / 91 dopo**: sono i conteggi veri. Se L75 non partisse dalla 259,
  diventerebbe rosso — è voluto.
- **La morte del giocatore** (unità 18) è raccontata al presente: se un lotto futuro usasse lo stesso schema
  al passato, la coerenza temporale andrebbe ricontrollata.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì — entrambi gli script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (34 controlli), `verify.py` exit 0 (44 controlli), sha256 `3928a76816c49f89` |
