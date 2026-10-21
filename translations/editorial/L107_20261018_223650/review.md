# REVIEW — L107 · `korath missions.txt` (tre contesti, un Quarg che parla male)

Coppie EN→IT rilette in `translation.json` (`0c901ea4867f63e3…`).

## 1. Voce e registro

- **Il Quarg traduttore** (16, 19) non parla male per caso: il gioco lo dice. La sua voce è **storta e
  trasparente** — `orgogliosissimo`, `debitrice`, `sproporzionatamente`, `camerataggine`, `vicinata`,
  `assenziata`, `misura sanissima` — e il giocatore capisce «più o meno». Il registro è **comico senza essere
  ridicolo**: il Quarg è cortese e cerimonioso, sbaglia le parole.
- **I Korath** non parlano italiano: sibilano (`sibila in approvazione`), gesticolano (palmi in avanti, cerchi
  ampi), premono crediti nelle mani, gonfiano il petto. Il loro «dialogo» è **corpo**, e la traduzione lo lascia
  corpo.
- **Il narratore** è al «voi», come sempre, e osserva con un filo di partecipazione: «Non potete fare a meno di
  sentirvi un po' in colpa».
- **Il giocatore** ha battute brevi, da menu: `(Sì.)`, `(Sì, e restituite loro i crediti.)`, `(Seguilo nel vicolo.)`, `(Fai il sicuro e vattene.)`.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `Korath to <planet>` | **identico** | 3 | nome di missione (`VALUE`) |
| `Livestock to <planet>` | **identico** | 20 | idem |
| `A Korath family of <bunks> has paid you <payment>` | **Una famiglia Korath di <bunks> persone vi ha pagato <payment>** | 4 | `<bunks>` = numero |
| `Transport <bunks> Korath farmers and their <cargo>` | **Trasporta <bunks> agricoltori Korath e il loro <cargo>** | 21 | `DESCRIPTION`, imperativo |
| `the brightest hours of the day feel like evening` | **le ore più luminose del giorno vi sembrano sera** | 5 | |
| `a small layer of soot clings to your skin` | **sulla vostra pelle si attacca un sottile strato di fuliggine** | 5 | |
| `hunched over a cane it uses for support - probably elderly` | **curvo su un bastone che usa per sostegno, probabilmente anziano** | 6 | il trattino del sorgente diventa virgola: qui non separa un inciso |
| `erupts into a coughing fit` | **scoppia in un accesso di tosse** | 6 | |
| `They press 500 credits into your hands` | **Vi premono 500 crediti nelle mani** | 7 | |
| `shockingly low` | **scandalosamente pochi** | 7 | |
| `(Yes, and give their credits back to them.)` | **(Sì, e restituite loro i crediti.)** | 9 | |
| `they sigh in relief` | **sospira di sollievo** | 11 | |
| `their shoulders slump` | **le spalle … si abbassano** | 12, 13 | ripetuto **non** identico al sorgente: due soggetti diversi (singolare/plurale) |
| `They won't take no for an answer` | **Non accettano un no come risposta** | 12 | |
| `This fellow pridefulest` | **Questo individuo orgogliosissimo** | 16 | |
| `my indebted translation` | **la mia traduzione debitrice** | 16 | |
| `I am inclined to acquiesce his request happyfully` | **Sono incline ad acconsentire alla sua richiesta felicemente** | 16 | |
| `I disproportionately thank you for reuniting my familial` | **Ti ringrazio sproporzionatamente per aver riunificato il mio famigliare** | 16 | |
| `this gaggle would vicinitied … absenced your presence` | **questa accozzaglia sarebbe vicinata … fosse stata assenziata** | 16 | |
| `this is indicating of thankfulness of wholesomest measure` | **Questo sta a indicare gratitudine di misura sanissima** | 19 | |
| `wishes you kind travels` | **ti augura viaggi gentili** | 19 | |
| `its (rough) translation services` | **i suoi servizi di traduzione (approssimativi)** | 19 | la parentesi è del narratore, non del Quarg |
| `a wool-like fabric` | **un tessuto simile alla lana** | 22, 30, 37 | ripetuto, reso identico |
| `It raises both its palms toward you` | **Solleva entrambi i palmi verso di voi** | 22 | |
| `an alarmingly loud bleating noise` | **un belato allarmante** | 25 | |
| `Three towering Korath` | **Tre Korath torreggianti** | 28 | |
| `Whatever chance you had of getting out of this is gone now.` | **Qualunque possibilità aveste di uscirne, ora è sparita.** | 28 | |
| `to see... animals?` | **per vedere... animali?** | 29 | tre punti del sorgente, non ellissi |
| `a massive abandoned plaza` | **una enorme piazza abbandonata** | 30 | |
| `they come in a variety of brown-black colors` | **vengono in una varietà di colori bruno-neri** | 30 | |
| `a full coat of fur and an additional blanket` | **un manto folto e una coperta aggiuntiva** | 30 | |
| `This must have been the only place … keep their entire herd together` | **Questo dev'essere l'unico posto … tenere insieme tutto il gregge** | 30 | |
| `a paper map - a rare sight in the era of interstellar travel` | **una mappa di carta, una vista rara nell'era dei viaggi interstellari** | 31 | |
| `draws a circle around it with a piece of chalk` | **ci disegna intorno un cerchio con un pezzo di gesso** | 32 | |
| `spreading tarps over the floor and scattering a type of straw` | **stendendo teli sul pavimento e spargendoci sopra una specie di paglia** | 35 | |
| `interspersed with the farmers` | **intervallata dagli agricoltori** | 35 | |
| `the hefty, wool-like blankets` | **le pesanti coperte simili alla lana** | 36 | |
| `space sickness` | **mal di spazio** | 37 | |
| `shaving the wool-like fur off the animals` | **radere il pelo simile alla lana dagli animali** | 37 | |
| `the slow desertification of this planet` | **la lenta desertificazione di questo pianeta** | 38 | |
| `Setar Fort's chilling temperatures` | **le temperature gelide di Setar Fort** | 38 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il Quarg storpiato non si «corregge»** mai. Se una revisione futura normalizza `vicinata` o `assenziata`,
   distrugge la caratterizzazione e il narratore che la spiega.
2. **`(No.)` = `(No.)`**: unità 10, identica per coincidenza. Non è una dimenticanza e non autorizza altre
   identità: il controllo elenca **esattamente** 3, 10, 20.
3. **`<bunks>` è un numero, `<tons>` è un carico**: l'unità 31 li ha entrambi e la frase deve reggere con due
   numeri diversi.
4. **Zero quadre in questo lotto**: le quadre dei Wanderer restano confinate ai loro testi. Un `[` qui sarebbe un
   errore, e il controllo lo dice.
5. **Zero citazioni aperte**: qui il Quarg apre e chiude i suoi discorsi. Il conteggio per unità è pari ovunque.
6. **`...` sono tre punti**, non `…`: il gioco usa il carattere ASCII e la tipografia italiana del progetto vieta
   l'ellissi tipografica.
7. **`Kor Efret` singolare / `Kor Efreti` plurale**: il sorgente alterna, la traduzione conserva la distinzione.
8. **`Laki Nemparu` e `Setar Fort` invariati**: toponimi.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 38 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 95 unità residue su 10 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (30 controlli) |
