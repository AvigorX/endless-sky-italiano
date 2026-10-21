# Style guide — Italiano (Endless Sky IT)

Vincolante per ogni lotto. Se una regola qui non è rispettata, il lotto non è approvabile.

## 1. Registro e voce

- Il giocatore è **"tu"**. Gli equipaggi e i personaggi collettivi usano **"voi"**.
- Il capitano non è mai "il giocatore" nel testo: è "tu" o "il capitano" nelle descrizioni.
- Le fazioni parlano con il proprio registro: militare asciutto (Concordato, Repubblica), burocratico
  (Coalition/Heliarch), arcaico (Successors), tecnico (Remnant).
- Niente inglese nei testi, tranne i termini del glossario marcati invariati (`laser`, `plugin`, `radar`).
- Niente calchi: "fare un salto" non è "make a jump" → "saltare"; "prendere danno" → "subire danni".

## 2. Terminologia

- `glossary.csv` è **vincolante**. Un termine nuovo va aggiunto prima di essere usato in un lotto.
- I nomi propri di navi, pianeti, sistemi, fazioni e persone **non si traducono**, salvo decisione
  esplicita registrata nel glossario.
- I nomi descrittivi di classe (`Shuttle`, `Light Freighter`) si traducono quando sono categorie
  (`navetta`, `mercantile leggero`).
- Unità: `tonnellata/tonnellate`, `credito/crediti`, `unità` per le grandezze astratte.
- Il verbo `disable` → **neutralizzare** (una nave è "neutralizzata", non "disabilitata").

## 3. Tipografia

- Accenti sempre corretti e obbligatori: **è, é, à, ì, ò, ù, perché, città, può**.
  ⚠️ Il renderer attuale non ha i glifi accentati (audit IT-002): i testi accentati sono corretti ma
  **non visualizzabili** finché l'atlante non viene esteso. Non è ammesso scrivere "e'" al posto di "è".
- Apostrofo: quello dritto `'` è accettato dal tokenizer; quello tipografico `’` è preferibile ma
  richiede il glifo (IT-012). Nei lotti si usa `'` finché il font non è esteso.
- Virgolette: mai `"`, perché rompono il delimitatore dei dati. Se il testo deve contenere una citazione,
  usare caporali `«…»` solo dopo l'estensione del font; nel frattempo riformulare.
- Puntini di sospensione: `…` come carattere unico solo dopo IT-012; nel frattempo `...`.
- Trattino: `-` per le parole composte, `—` (em dash) per le incidentali solo dopo IT-012.
- Niente doppio spazio, niente spazio prima di `: ; , .`.

## 4. Maiuscole

- Etichette UI: **maiuscola solo alla prima parola** ("Bacheca degli incarichi", non "Bacheca Degli
  Incarichi"). Fa eccezione il trattamento dei nomi propri.
- Nomi di fazione: maiuscola (`Concordato Vetra`, `Repubblica`).
- Oggetti comuni: minuscola (`scafo`, `scudi`, `carburante`).
- Dopo i due punti: minuscola, salvo nome proprio o inizio di frase completa.

## 5. Numeri, date, unità

- Migliaia con il punto (`1.500`), decimali con la virgola (`2,5`) — **nota**: il motore formatta con la
  virgola inglese (audit IT-016); la discrepanza è nota e va risolta lato codice, non nel testo.
- Date: `14 marzo 3013` nella prosa. Nei testi che contengono `<date>` il segnaposto resta e la data la
  formatta il motore (in inglese: IT-015).
- Percentuali: `15%` senza spazio.

## 6. Struttura dei testi di gioco

- **Tab iniziale**: se l'inglese inizia con un tab, l'italiano deve iniziare con lo stesso tab
  (paragrafo indentato). Validatore: `TAB_LOST`.
- **Segnaposto** `<…>`: mai tradotti, mai spostati fuori dal contesto sintattico, mai duplicati.
  Se un segnaposto è un nome proprio (`<first>`, `<last>`, `<planet>`), l'articolo va concordato a mano.
- **Backtick**: il delimitatore non si cambia. Se la traduzione contiene `"`, va riscritta.
- Lunghezza: massimo +20% rispetto all'inglese per le etichette UI; oltre, il layout a coordinate fisse
  può troncare (IT-013). Per la prosa non c'è limite, ma la concisione è preferita.

## 7. Qualità

- Ogni frase deve poter essere riletta senza l'inglese a fianco: se serve l'inglese per capirla, è
  sbagliata.
- Non si aggiungono dettagli assenti dalla fonte, non si omettono frasi.
- I nomi dei luoghi citati devono corrispondere a quelli usati in `map planets.txt` / `map systems.txt`.
- In caso di ambiguità: si traduce la lettura più probabile e si apre un issue `AMBIGUOUS` nel batch,
  invece di indovinare in silenzio.

## 8. Cosa non si traduce

- Identificatori di oggetti (`mission`, `ship`, `planet`, `system`, `outfit`), chiavi di attributo,
  nomi di merci e categorie, `uuid`, condizioni, etichette `goto`.
- Nomi propri secondo glossario.
- Stringhe che sono solo simboli (`"`, `-`, `...`).
