# review.md — L281 (`data/quarg/quarg news.txt`, righe 23–490)

Registro delle decisioni editoriali del **primo e unico lotto** delle notizie dei Quarg: le loro parole al giocatore e dieci
istantanee del mondo ad anello.

## 1. Che cosa contiene il file (dopo la misura)

Il file è **composto**, non scritto in prosa continua: le notizie sono costruite da blocchi `word` con frammenti fra
virgolette, e l'estrattore espone solo le stringhe fra **backtick**. Ne restano 50 unità, di cui:

| gruppo | unità | trattamento |
|---|---|---|
| **delimitatori** (l'unica stringa `` `"` ``) | 28 | **copiati**, dichiarati `ID_OK` |
| **`news:quarg anywhere`** | 11 | **tradotti** |
| **`phrase:ringworld quarg phrases`** | 10 | **tradotti** |
| `news:anonymous quarg` (una battuta) | 1 | **tradotta** |

I frammenti **senza backtick** non sono nel database: la notizia composta resta in inglese lì, e la lacuna è dichiarata.

## 2. I Quarg che parlano

Sei battute dirette, tutte con lo stesso carattere: **pazienza didattica** e nessuna aggressività, anche quando rifiutano.

| inglese | resa |
|---|---|
| `Are you what is called a 'tourist'?` | **Sei quello che viene chiamato un 'turista'?** |
| `Hello, human. Are you enjoying your time on our world?` | **Salve, umano. Ti stai godendo il tempo passato sul nostro mondo?** |
| `we will not provide you with our technology` | **non ti forniremo la nostra tecnologia** |
| `It troubles me greatly to see how many species still cling to senseless fighting` | **Mi turba profondamente vedere quante specie si aggrappino ancora a una lotta insensata** |
| `our scientific efforts were quite fruitful` | **i nostri sforzi scientifici sono stati piuttosto fruttuosi** |
| `please report it to us … in the wrong hands` | **riferiscilo a noi … nelle mani sbagliate** |
| `You are welcome to be amongst us here, provided …` | **Sei il benvenuto fra noi, a patto che …** |

`'tourist'` è fra **apici semplici** nel sorgente: la resa li conserva, ed è il motivo per cui quell'unità ha **due** apici in
italiano.

## 3. Le dieci istantanee del mondo ad anello

Sono **quadri**, non trame: il giocatore guarda e il testo descrive. Tutte al **presente** e in **seconda persona** («Vedi»,
«Noti», «Lo osservi»), e la resa mantiene questa forma perché è quella che dà l'effetto di **istantanea**.

| unità | scena | dettaglio che non va perso |
|---|---|---|
| 41 | un adulto mostra l'anello a un piccolo | «probabilmente un bambino in anni Quarg» |
| 42 | un Quarg tocca le pareti con i palmi | «si ferma di colpo e riprende le sue faccende» |
| 43 | scorta corazzata con contenitore tubolare | gli altri **si tengono a distanza** |
| 44 | treno di carrelli da laboratorio | «passa quasi mezz'ora prima che tu veda l'ultimo» |
| 45 | centinaia seduti in silenzio | chi assiste **smette di parlare e si sposta** |
| 46 | lo sguardo negli occhi | «sbatte le palpebre una volta e prosegue» |
| 47 | conteggio dei container | il **puntino spento** sul tablet, poi ricomincia |
| 48 | scambio di equipaggi fra due navi | «senza intoppi» |
| 49 | festival del frutto simile a un'arancia | da **liscio** a **grinzoso**, da **pisello** a **cocomero** |
| 50 | il Quarg che svanisce | «il corridoio è un **vicolo cieco**» |

I dettagli **strani** (il barattolo che cambia forma, il Quarg che svanisce) sono il punto: i Quarg sono **incomprensibili**
anche quando sono gentili, e la resa non ha spiegato ciò che il testo lascia inspiegato.

## 4. Terminologia

| inglese | resa | nota |
|---|---|---|
| `ringworld` | **mondo ad anello** | forma già nel corpus |
| `hangars` / `hangar bays` | **hangar** / **baia** | |
| `cargo containers` | **container** | |
| `data pad` | **tablet** | |
| `lab carts` | **carrelli da laboratorio** | |
| `Quarg` | **Quarg** | invariato, singolare e plurale |
| `human` | **umano** | |

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **44** | **44**, per unità |
| apici | **14** | **20** |
| segnaposto | **0** | **0** |

## 6. Chiusura del file

`data/quarg/quarg news.txt` è **50/50** in staging in **un solo lotto**, righe 23–490, tutte `PENDING`.

Cosa **non** significa: non è approvato, non è stato visto nel gioco, non è stato revisionato da una persona — e le notizie
**composte** restano parzialmente in inglese nei frammenti che l'estrattore non espone.

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 50 unità `PENDING`.
- **Lacuna dell'estrattore**: frammenti senza backtick invisibili al database (dichiarata, non riparata).
- **Prossimo file**: `data/wanderer/wanderer missions.txt` — righe 16–41, **13 unità** (1 `VALUE`, 1 `DESCRIPTION`, 11
  `MISSION_TEXT`), 9 tab, 16 virgolette, 4 apici, 4 segnaposto (L282).
