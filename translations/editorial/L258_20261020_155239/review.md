# review.md — L258 (`data/human/post-war reactions.txt`, righe 152–215)

Registro delle decisioni editoriali del **terzo lotto**: la chiusura del racconto delle due sorelle e l'apertura della
missione dell'**orfano del Sindacato**.

## 1. Le due metà e il cambio di tono

| metà | registo | segnali |
|---|---|---|
| 1–11 (sorelle) | **ironico e affettuoso** | «si vanta Rain», «Ridono entrambe», «dammi un colpetto», «non mi ha impedita» |
| 12–20 (Gus) | **asciutto, d'azione** | frasi brevi, imperativi («Basta così»), descrizione fisica, paura |

Il cambio è nello **stesso** file e a un confine netto: la riga 196 apre la scena con una descrizione d'ambiente **senza
tab**, come la riga 110 in L257. La forma del sorgente (`\t` su tutto tranne l'attacco di missione) è la traccia del cambio,
e il `check.py` la usa come asserzione.

## 2. Scelte sulle sorelle

| inglese | resa | perché |
|---|---|---|
| `Not a match for a Dreadnought and an Auxiliary, though` | **«Però non è alla pari di una corazzata e di un'ausiliaria»** | `though` in coda reso in testa: l'italiano non chiude così |
| `we have a joint patrol with one ship from each state` | **«pattugliamo insieme con una nave per stato»** | `state` = Stato, non «stato» |
| `the usual assortment of hoaxes` | **«il solito campionario di bufale»** | |
| `up in arms over fear of aliens` | **«sul piede di guerra per paura degli alieni»** | ripetuto **due volte** nella stessa unità: la ripetizione è **voluta** (è la battuta) e resta |
| `being my sister didn't stop me blowing up her Cruiser!` | **«essere mia sorella non mi ha impedita di far saltare il suo incrociatore!»** | accordo al femminile: parla Fiona |
| `We rescued her ship's escape pods` | **«abbiamo recuperato le capsule della sua nave»** | il possessivo inglese diventa «della sua nave» |
| `you got a new Auxiliary commission afterwards` | **«dopo ti hanno dato il comando di una nuova ausiliaria»** | |
| `Now we escort each other's ships during investigations!` | **«Ora ci scortiamo a vicenda le navi durante le indagini!»** | |
| `Rain went off to Earth to join the Navy Academy years ago` | **«anni fa Rain è partita per la Terra per entrare all'Accademia della Marina»** | «la Terra»: nome comune, articolo |
| `Fiona stayed on Longjump and joined the local militia` | **«Fiona è rimasta su Longjump e si è unita alla milizia locale»** | `on <pianeta>` → «su» |

## 3. Scelte su Gus

| inglese | resa | perché |
|---|---|---|
| `Break it up, kids.` | **«Basta così, ragazzi.»** | idioma, non letterale |
| `(Ignore them and keep walking.)` | **«(Ignorali e continua a camminare.)»** | opzione di uscita, parentesi tonde, **tu** singolare |
| `They eye the gun in your holster and run away.` | **«Danno un'occhiata alla pistola nella tua fondina e scappano.»** | |
| `He looks about twelve years old.` | **«Dimostra una dozzina d'anni.»** | «dimostrare» per l'età apparente |
| `It takes him a few seconds to recover.` | **«Gli servono alcuni secondi per riprendersi.»** | |
| `I'm Gus.` | **«Sono Gus.»** | nel mezzo di una citazione: non si taglia |
| `Can you walk me to the repair shop?` | **«Mi accompagni all'officina?»** | |
| `Aren't you a little young to work in a repair shop?` | **«Non sei un po' giovane per lavorare in un'officina?»** | |
| `I'm in a hurry. You're on your own.` | **«Ho fretta. Arrangiati da solo.»** | |
| `That's rough, buddy, but I'm in a hurry. You're on your own.` | **«È dura, amico, ma ho fretta. Arrangiati da solo.»** | la seconda metà **si ripete identica** alla 19: è la stessa risposta, più lunga |

## 4. La citazione non chiusa (unità 5)

```
… says Fiona. Rain adds, "Only metaphorically up in arms, this time.
```

Tre virgolette. Nel sorgente la seconda citazione si apre e **non si chiude**, e la frase finisce con un punto. La resa
italiana ha le stesse tre virgolette e lo stesso punto finale, e i due script lo asseriscono: **secondo caso** del file
dopo l'unità 12 di L257. Non è una distrazione dell'estrattore: è la forma della stringa che il gioco mostra.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **19** (tutte tranne la 12) | **19**, stesse unità, primo carattere |
| virgolette | **45** | **45**, mappa per unità identica |
| apici | **18** su 10 unità | **12** su 7 unità (1, 3, 10, 12, 15, 16, 18) |
| segnaposto | **0** | **0** |

Gli apici italiani sono **più dei soliti** (12 contro i 5 di L257) perché questo lotto ha molte elisioni: `un'ausiliaria`,
`un'altra`, `all'Accademia`, `dall'area`, `l'angolo`, `dall'aria`, `d'anni`, `all'officina`, `un'occhiata` — e gli apici
inglesi invece sono contrazioni e possessivi (`we'll`, `didn't`, `ship's`, `sister's`, `I'm`, `they're`, `Aren't`).

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 20 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file è a 65/87**: L259 (righe 222–250, 15 unità) e poi L260, **terminale**, righe 253–264, 7 unità.
