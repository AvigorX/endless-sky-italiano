# review.md — L261 (`data/remnant/remnant jobs.txt`, righe 19–209)

Registro delle decisioni editoriali del **primo lotto** dei lavori Remnant: quattro taglie Korath e due spedizioni
scientifiche, raccontate in sette missioni.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | perché |
|---|---|---|---|
| `VALUE` | **7** | **copiato** | sono i **nomi dei lavori** nella bacheca: dati |
| `DESCRIPTION` | **7** | **tradotto** | è la scheda che il giocatore legge |
| `DIALOG` | **11** | **tradotto** | sono le battute alla consegna |

L'asserzione che rende il lotto verificabile è **doppia**: ogni `VALUE` è **identico**, ogni altra unità è **diversa**. Un
solo controllo non basta: «identico» da solo ammetterebbe un lotto di sole copie, «diverso» da solo ammetterebbe un `VALUE`
tradotto per distrazione.

## 2. Le quattro taglie

| inglese | resa | nota |
|---|---|---|
| `Crippled <npc model> Bounty` | **copiato** | `crippled` = in avaria, ma il nome resta inglese |
| `Troublesome <npc model> Bounty` | **copiato** | |
| `Damaged Rano'erek Bounty` | **copiato** | `Rano'erek` è un **modello Korath**: nome proprio, apice compreso |
| `Marauding Rano'erek Bounty` | **copiato** | |

Nelle **schede** invece i quattro participi si traducono, e ognuno ha la sua sfumatura:

| inglese | resa |
|---|---|
| `A crippled Korath ship is lurking in Remnant territory.` | **«Una nave Korath in avaria si aggira nel territorio dei Remnant.»** |
| `A Korath ship is proving troublesome in Remnant territory.` | **«Una nave Korath sta creando problemi nel territorio dei Remnant.»** |
| `A damaged Korath ship is lurking in Remnant territory.` | **«Una nave Korath danneggiata si aggira nel territorio dei Remnant.»** |
| `A Korath ship is marauding through Remnant territory.` | **«Una nave Korath sta saccheggiando il territorio dei Remnant.»** |

`Hunt it down` → **«Dalle la caccia»**: la *nave* è femminile, e il corpus usa già `dare la caccia a <npc>`. Ho scelto
l'accordo corretto invece del più comodo «Dagli», che avrebbe fatto concordare il clitico con il capitano e non con la preda.

## 3. Le due spedizioni scientifiche

Le missioni `Expanded Horizons Astral job` e `… late` hanno **le stesse tre stringhe** (VALUE, DESCRIPTION, DIALOG): la
differenza sta nei **tempi** della missione, non nel testo. Le rese sono quindi **identiche**, e il `check.py` lo verifica
esplicitamente (`by[13] == by[17]`, `by[15] == by[19]`, `by[12] == by[16]`).

| inglese | resa |
|---|---|
| `Research Expedition to <waypoints>` | **copiato** |
| `Travel to <waypoints> with a Research Laboratory to collect data, then return to <destination>.` | «Raggiungi `<waypoints>` con un **Laboratorio di Ricerca** per raccogliere dati, poi torna su `<destination>`.» |
| `Your scientist unpacks the laboratory and takes the requested observations…` | «Il tuo scienziato **scarica** il laboratorio e fa le osservazioni richieste…» |
| `…hands you the logistics allotment of <payment>.` | «…ti consegna l'**indennità logistica** di `<payment>`.» |

`Research Laboratory` è il **nome di un equipaggiamento**: il corpus lo rende già **«Laboratorio di Ricerca»** (in
`remnant 1 introduction.txt`), e la forma maiuscola è quella che il giocatore vede installata sulla nave. `unpacks` →
**«scarica»**, come nella scheda dei satelliti in `human missions.txt`.

## 4. I segnaposto

| famiglia | conteggio | dove |
|---|---|---|
| `<payment>` | **10** | tutte le taglie e le due spedizioni |
| `<planet>` | **8** | schede e battute delle taglie |
| `<waypoints>` | **4** | le due spedizioni (VALUE e DESCRIPTION) |
| `<npc>` | **3** | unità 4, 8, 23 |
| **`<npc model>`** | **2** | unità 1 e 5 (`VALUE`) |
| `<destination>` | **2** | unità 13 e 17 |

`<planet>` (il pianeta dove si riscuote) e `<destination>` (quello dove si torna) **coesistono** in questo file: sono
simboli diversi, e il controllo li verifica separati e nell'**ordine** dentro ogni unità.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **2** (`Rano'erek`) | **4** (due dal nome copiato, due da `l'indennità`) |

Il file **non usa** tab né virgolette, benché contenga undici dialoghi: le battute sono prosa piana. Le due asserzioni
negative sono scritte perché un tab o una virgoletta «aggiunti» qui sarebbero un difetto, non uno stile.

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file è a 25/87**: L262 riparte dalla riga 226 e attraversa **nove** contesti, con la prima `MISSION_TEXT` del file.
