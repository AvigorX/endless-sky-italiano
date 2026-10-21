# review.md — L289 (`data/gegno/gegno ships.txt`, righe 1193–1616)

Registro delle decisioni editoriali del **lotto terminale** delle navi Gegno: la flotta **Scin** al completo.

## 1. Che cosa raccontano queste otto navi

| nave | righe | ruolo | nota |
|---|---|---|---|
| `Halite` | 1193–1194 | velivolo da combattimento | **sciame di danni istantanei**, sta sotto scudo, vive sulle **portaerei** Scin |
| `Mica` | 1234 | navetta | versione Scin dello `Shale` e dello `Slate`, **più piccola** ma «quasi due volte più veloce» |
| `Coesite` | 1288 | schermo | due supporti per torrette, «orbita e spara in movimento», schierata **in gruppi** |
| `Tridymite` | 1342 | trasporto di lusso | navi da **ricerca** per scienziati, o **private** per gli Scin di grado più alto; prototipo di **scanner** |
| `Felsic` | 1395 | multiruolo | tre supporti, capacità ampliata, «compensa l'assenza di una nave da guerra Scin dedicata» |
| `Feldspar` | 1480–1481 | portavelivoli sperimentale | «una creazione Scin che vale la pena vedere», **poderoso** e **fragile** |
| `Epidote` | 1547–1548 | ricerca e cargo pesante | **cuccette** per scienziati, **baia** per due `Halite`, tre torrette dorsali |
| `Kyanite` | 1615–1616 | piattaforma di prova | sperimentazione **delle armi**, ma «non capace di combattere» |

## 2. Il ritratto della flotta Scin

Gli Scin sono l'altra faccia dei Vi: navi **più piccole**, **sperimentali**, spesso **fragili** — «più esposti ai danni allo scafo
come ogni altra nave da guerra Scin». Il testo lo ripete tre volte in tre schede diverse, e la resa **non attenua**:

- `Feldspar` — «pericolosamente completa per le loro dimensioni», ma **fragile**;
- `Kyanite` — «non sono capaci di combattere, per quanto i loro sistemi siano esposti e per quanto poco scafo li copra»;
- `Felsic` — deve **compensare** l'assenza di una nave da guerra dedicata.

È una **dottrina diversa**, non una flotta peggiore: ricerca, velocità, sciami di velivoli.

## 3. L'istruzione di gioco

Una sola unità parla al **giocatore** invece che del mondo:

> «I velivoli da combattimento non sono dotati di iperguida. **Non puoi trasportare** un velivolo da combattimento se non hai
> nella **tua** flotta una nave con una **baia di caccia**.»

Non è un errore di registro: è il **manuale dentro il testo**. La resa la tratta come **istruzione** (frasi brevi, «puoi»,
imperativo implicito) e non come descrizione. Il `check.py` la isola come unica eccezione al registro impersonale.

## 4. I nomi che restano

`Halite` · `Mica` · `Coesite` · `Tridymite` · `Felsic` · `Feldspar` · `Epidote` · `Kyanite` · `Gegno` · `Scin` · `Vi` ·
`Shale` · `Slate` · `Schist` — tutti **invariati**, e **nessun plurale inglese** riprodotto: niente `Halites`, `Coesites`,
`Kyanites`, `Feldspars`. Il plurale lo porta l'articolo italiano («i Feldspar», «gli Epidote»).

## 5. Scelte di resa

| inglese | resa |
|---|---|
| `a swarm of instant damage` | **uno sciame di danni istantanei** |
| `while under protective shielding` | **mentre sono sotto uno scudo protettivo** |
| `the Gegno Scin's take on a shuttlecraft` | **la versione dei Gegno Scin di una navetta** |
| `as screening vessels` | **come schermo** |
| `to always be orbiting and firing on the move` | **di orbitare e sparare sempre in movimento** |
| `so they may overtake vessels much larger than them` | **così da poter sopraffare vascelli molto più grandi di loro** |
| `a small luxury transport vessel` | **un piccolo vascello di trasporto di lusso** |
| `an early prototype scanner system built into the frame` | **un primo sistema di scanner prototipale integrato nella struttura** |
| `less durability` | **minore robustezza** |
| `doubling as a secondary combat vessel` | **fungere al tempo stesso da vascello da combattimento secondario** |
| `as a testbed` | **come banco di prova** |
| `a semi-experimental platform` | **una piattaforma semi-sperimentale** |
| `the latest in Gegno plasma technology` | **la più recente tecnologia al plasma dei Gegno** |
| `keep a decent stance away from a battle` | **mantenere una buona posizione lontano dalla battaglia** |
| `the most common practice of Kyanites` | **la pratica più comune dei Kyanite** |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **5** (1193, 1194, 1481, 1548, 1616) | **5**, primo carattere |
| virgolette | **0** | **0** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **4** | **5** |
| coppie consecutive | **4** | **4** |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 37/37** in staging: **ventitreesimo file completo**.
- **Prossimo file**: `data/avgi/avgi culture conversations.txt` — righe **24–106**, **8 unità** (tutte `MISSION_TEXT`), **468
  parole**, **6 contesti**, **0 tab**, **10 virgolette**, **9 apici**, **1 segnaposto** (`<ship>`). È **dialogo**, non prosa
  tecnica: il registro torna al **«tu»** e le virgolette tornano a contare.
