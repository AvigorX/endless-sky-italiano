# REVIEW — L56 · `data/gegno/gegno I corroboration.txt`

Revisione del lotto dopo la chiusura dei controlli. Non è un giudizio letterario: è la lista di ciò che
si è scelto, di ciò che resta dubbio e di ciò che va tenuto presente quando il file verrà approvato.

## 1. Coerenza interna

**Registro.** Il lotto tiene un solo narratore (seconda persona, presente) e una sola voce Quarg —
Adrauni — con sintassi sostenuta e inversione dove il sorgente la ha. Il narratore non commenta il
giocatore: dove l'inglese dice «It is now up to you to try and figure out some sort of common ground»,
l'italiano resta sullo stesso piano («Ora tocca a te cercare una qualche base comune con i Gegno»), senza
aggiungere enfasi.

**Tempi verbali.** Gli epiloghi usano il passato prossimo per le azioni compiute e il presente per le
descrizioni. È coerente con L53–L55 sullo stesso universo Gegno.

**Terminologia fissa.** `Dueyu Eitch` (mondo natale, invariato) · `Adrauni` (titolo, non nome) ·
`Turf Wars` (invariato) · `corsari` (privateers) · `mondo ad anello` (ringworld) · `varco` (gateway, da
decisione 182) · `Scin` / `Vi` (fazioni, invariati) · `Quarg` (invariato) · `Sparrow`, `Headhunter`,
`Mule` (classi di nave, invariate).

## 2. Nodi traduttivi aperti (dichiarati, non risolti a forza)

- **«revolution»** per il tempo gegno (unità 8, «otto rivoluzioni»): è un'unità di calendario aliena non
  definita dal gioco. Reso con «rivoluzioni» e non con «anni»: cambiare darebbe un'informazione che il
  sorgente non dà.
- **«in some notable capacities we still are»** (unità 15): reso «In alcune notevoli capacità lo siamo
  ancora». La formula è goffa in inglese e resta leggermente goffa in italiano — è la voce del personaggio.
- **«Gegno culture is to hold all as a great home»** (unità 12): reso «La cultura Gegno considera tutto
  come un'unica grande casa». Il senso è quello; la sintassi ellittica dell'originale non è replicabile
  senza rompere l'italiano.
- **`dont know`** (unità 143, `label`): il refuso del sorgente (apostrofo mancante) **resta**: è una chiave.
- **«Eyuu idu keiou ghynem uf, 'Dueyu.'»** (unità 92): la riga in lingua Gegno resta identica, ma la
  parola `Dueyu` fra apici è la stessa che il giocatore ha appena pronunciato: la resa italiana la
  mantiene identica, perché il giocatore la sta citando.

## 3. Duplicati

10 gruppi, 30 unità. Tre categorie:

1. **Ripetizioni di scena** (170/171: stessa scena, due esiti) → resa identica, verificata.
2. **Ripetizioni di dialogo nel ramo «epilogo»** (125–169): Adrauni ripete lo stesso discorso con
   variazioni minime. Rese identiche **solo** dove l'inglese è identico.
3. **Ripetizioni di descrizione** (`negative rep`, e le due varianti del risveglio in hangar): identiche
   per necessità, perché il testo inglese è identico.

Nessun duplicato italiano fra unità con inglese diverso: il controllo lo asserisce (33 controlli di
`check.py` includono la riga `duplicati italiano non spiegati dal sorgente`).

## 4. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`.** Le 171 unità restano `PENDING`: lo staging non è approvazione.
- **Nessun caricamento nel gioco.** `translation.json` non è stato importato: la verifica è sui file.
- **Nessuna deroga generica sui riferimenti di dato.** I 12 token `<…>` sono verificati uno per uno come
  multiset, non «in generale».
- **Nessun ritocco ai file protetti** (`tools/l10n.py`, `glossary.csv`, `staging/inventory_fields.csv`).

## 5. Rischi per il prossimo lotto

- **L57 chiude il file.** Lì l'invariante «di file» torna legittimo e va asserito insieme: 0 dopo la
  1287, `max(line) = 1287`, copertura 298/298 su L56+L57 (decisione 181).
- **`DIALOG` 22/23 ripetono 170/171 di L56.** La resa deve essere **la stessa stringa**: se L57 la
  cambia, la coerenza interna del file si rompe. Va asserito esplicitamente in `verify.py`.
- **Il primo esito di `verify.py` di L57 sarà probabilmente rosso sulla prima riga**: la finestra di
  export parte dalla 905 ma la prima unità sta sulla **943**. Non è un errore del gioco: è il numero da
  correggere nel controllo.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 5 parti, `translation.json`, `check.py`, `verify.py` |
| ESEGUITO | sì — `check.py` e `verify.py` lanciati, output letto |
| VERIFICATO | sì — `check.py` `FAIL totale: 0` (33 controlli), `verify.py` exit 0 (40 controlli) |
