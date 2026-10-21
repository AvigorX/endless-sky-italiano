# REVIEW — L206 · `coalition news.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`7cff828f2fb7e44b…`). Tutte le 20 unità sono **`PENDING`**.

## 1. La decisione principale: come rendere il parlato Saryd

Il sorgente marca i Saryd con **l'ordine delle parole**, non con un lessico: *«Caring for longcows, hard work it is.
Too much space they take up.»* Ho considerato tre strade.

| strada | esito | verdetto |
|---|---|---|
| italiano normale | «Occuparsi dei longcow è un duro lavoro. Occupano troppo spazio.» | **scartata**: cancella la caratterizzazione, che è il senso del testo |
| imitazione rigida parola per parola dell'inglese | «Occuparsi di longcow, duro lavoro esso è.» | **scartata**: l'italiano non ha il pronome soggetto obbligatorio, la resa diventa goffa e non «strana» |
| **inversione con mezzi italiani** | «Occuparsi dei longcow, un duro lavoro è.» | **scelta** |

La terza strada sfrutta il fatto che l'italiano ammette l'**ordine marcato**: il complemento o il predicato va in
testa, la copula chiude, il soggetto segue. Il risultato è riconoscibile senza essere incomprensibile, che è quello che
fa il sorgente in inglese.

**Regola operativa per i lotti successivi** (92 unità residue di questo file, tutte `NEWS`):
1. **narrazione** (le unità senza virgolette, che descrivono la scena) → italiano naturale;
2. **discorso diretto di Saryd o di membri della Coalizione** → inversione riprodotta;
3. **frasi brevi e motti** («Protect and serve») → resi diritti: non c'è spazio per invertire senza distruggere il motto;
4. **se il sorgente chiude in ordine normale, si chiude in ordine normale**: l'inversione non si aggiunge dove non c'è
   (unità 12, 13 e 16 di L207 lo mostrano).

## 2. Altre decisioni

1. **`Heliarch`** invariato, con l'articolo italiano: «gli Heliarch».
2. **`longcow`** invariato, singolare e plurale: è un nome di specie, non un comune.
3. **`Coalition Games` → «Giochi della Coalizione»**: nome comune di evento, come «Giochi Olimpici». Non è un nome di
   prodotto e non va conservato.
4. **`magister`** resta prestito latino: è un titolo della Coalizione e in italiano è trasparente.
5. **`food expo` → «fiera del cibo»**: «expo» in italiano è accettabile, ma qui il registro è da notiziario locale.
6. **`spaceport` → «spazioporto»**: termine già usato dalla campagna.
7. **`Saryd, Kimek, Arach, human`** → «Saryd, Kimek, Arach, umani»: le specie restano, l'umano si declina.

## 3. Un errore mio, corretto prima di chiudere

L'asserzione sui nomi includeva `Coalition Games` fra quelli da conservare; il `check.py` è caduto (`FAIL 1`). Aveva
torto l'asserzione: la resa «Giochi della Coalizione» è quella giusta e coerente con la distinzione fra nomi propri e
nomi comuni. Ho tolto il nome dalla lista e aggiunto un controllo che **verifica la scelta dichiarata**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità `PENDING`.
- **Nessuna schermata vista nel gioco**, **nessuna revisione umana**: la resa del registro Saryd è una proposta, non una
  decisione approvata. Va rivista da un editor umano prima di qualunque approvazione.
- **Nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (17) |
