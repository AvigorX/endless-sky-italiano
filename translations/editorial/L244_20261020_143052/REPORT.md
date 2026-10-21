# REPORT — L244 (`data/hai/hai ships.txt`, righe 362–885)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **33 controlli** (`FAIL totale: 0`); `verify.py` esce 0 con **25 controlli**
(invariante di segmento: 29 prima, 45 qui, 83 dopo). `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su
`state.db`: le 45 unità restano `PENDING`.

## 1. Cosa contiene il lotto

| contesto | unità | contenuto |
|---|---|---|
| `Pond Strider` | 1 `DESCRIPTION` (riga 885) | la coda della scheda lasciata aperta da L243: riparazione dei droni, conflitto con gli Slegati |
| `Flea` | 2 `TEXT` + 2 `DESCRIPTION` | il drone da combattimento e la **nota col tab** sul trasporto dei droni |
| `Geocoris` | 1 `VALUE` + 5 `TEXT` + 1 `DESCRIPTION` | il mercantile pesante costruito per rispondere ai mercantili umani |
| `Grasshopper` | 10 `TEXT` + 1 `DESCRIPTION` | ricognizione veloce, adottata da minatori e amanti del brivido |
| `Lightning Bug` | 11 `TEXT` + 1 `DESCRIPTION` | la scorta di convoglio che dà il meglio in sciame |
| `Ladybug` | 5 `TEXT` + 2 `DESCRIPTION` | la nave da esplorazione coi sensori, risvegliata dai pirati umani |

## 2. Misure

```
unità             45            (1 VALUE + 36 TEXT + 8 DESCRIPTION)
parole            466 EN -> 498 IT       rapporto 1,00 - 1,21 (media 1,02)
contesti          6
tab               1             all'inizio dell'unità 3, in inglese e in italiano
virgolette        72            = 2 × 36 nomi, nessun altro uso nel lotto
apici             0 EN / 3 IT   (unità 9, 34, 35: elisioni)
segnaposto        0             asserzione negativa scritta
copiati           37 unità      (1 VALUE + 36 nomi, identici all'inglese)
```

## 3. Le tre cose che il lotto ha di proprio

1. **Il tab è uno solo, e non è un tab di formato: è un rientro di testo.** L'unità 3 comincia con `\t` e il gioco la
   mostra **rientrata** sotto la scheda del Flea. Il controllo è **per unità** (`[(3, 1, 1)]`) e verifica che il primo
   carattere sia il tab **in entrambe le lingue**: uno `strip()` di troppo lo mangerebbe senza far cambiare i conteggi.
2. **72 virgolette, tutte nei nomi.** A differenza di L243 non c'è nessun motto: le 8 schede non citano nulla. Il
   `check.py` verifica **due cose insieme** — che le unità con virgolette siano esattamente le 36 `TEXT` (2 per una) e
   che **nessuna `DESCRIPTION`** ne contenga in nessuna delle due lingue.
3. **`Ladybug` non compare mai nel testo inglese.** Le due schede dicono «these vessels», «this ship»: il nome è nel campo
   `context`, non nella prosa. Il controllo sui nomi propri è quindi **per unità** («se l'inglese lo nomina, l'italiano lo
   conserva»), non un elenco globale — e asserisce anche che `Ladybug` sia **assente** dall'inglese, così il giorno in cui
   il sorgente cambia il controllo si accorge.

## 4. Copertura del file

```
L243   29 unità   righe  15 -  332
L244   45 unità   righe 362 -  885
---------------------------------
74 unità su 157 (47,1%)

residuo 83 unità, righe 901 - 1860
```

Confine misurato: **riga 901**, `ship:Pond Strider` — **lo stesso contesto dell'ultima unità** (885). Non è un errore: la
scheda del Pond Strider è spezzata in due blocchi dal file, e il primo lotto che la tocca (L243) l'aveva lasciata a metà.

## 5. Controlli che hanno morso

Tre rossi, tutti **nell'asserzione**:

1. il primo `check.py` dichiarava **13** nomi propri nelle schede; misurati **8** (l'elenco del controllo includeva
   `Hai` e `Sheragi`, che nella `verify.py` non c'erano). Il controllo è stato riscritto come invariante per unità, che
   non dipende da quanti nomi decido di elencare;
2. lo stesso errore nella `verify.py` (**13** contro **8**): corretto il numero, dichiarando caso per caso (Flea 1,
   Geocoris 1, Grasshopper 1, Lightning Bug 2, Pond Strider 1, Skipper Railgun 2) e il fatto che `Ladybug` è a **0 per
   testo**, non per dimenticanza;
3. un apostrofo italiano dentro un letterale a virgolette singole ha rotto il file (`SyntaxError`): trappola 99, terza
   volta in questa campagna. Il letterale è passato a virgolette doppie.

## 5-bis. Correzione retroattiva (2026-10-20, dopo L245)

La nota sui droni (unità 3) era resa con una frase **mia**: «I droni non escono equipaggiati con un iperpropulsore. Non
puoi trasportare un drone se non hai nella tua flotta una nave con una baia per droni.» In questo lotto nessun altro testo
la conteneva, quindi il `check.py` non poteva accorgersene: la divergenza è emersa in **L246**, dove la nota gemella sui
**caccia** esiste già in **8 lotti precedenti**.

Misura nel corpus:

| nota | resa | occorrenze |
|---|---|---|
| droni | «I droni **non sono dotati di iperguida**. Non puoi trasportare un drone **a meno che tu non abbia**…» | **7** |
| droni | «I droni non escono equipaggiati con un iperpropulsore…» (quella di L244) | **1** |
| caccia | «I caccia non sono dotati di iperguida… con una baia **di** caccia» | **6** |
| caccia | «…con una baia **per** caccia» | **2** |

La regola è la **forma dominante**: l'unità 3 è stata riscritta sulla resa a 7 occorrenze. Conseguenze, tutte verificate:

- `check.py` e `verify.py` **restano verdi** (entrambi asseriscono «baia per droni» e la nota tradotta: la frase dominante
  le soddisfa);
- parole italiane **496 → 498**;
- `sha256[:16]` **`f1ecbcda503f2d0d` → `2121d513cf0c67e2`**;
- i documenti che citavano il vecchio hash e il vecchio conteggio sono stati aggiornati (`STATO.md`, `REPORT.md`,
  `HANDOFF_L246`, `RIPRESA_L246`, `CHECKPOINT_EDITORIALE.md`).

**Lezione**: una nota che si ripete in mezza dozzina di lotti non si traduce «bene», si **copia** dalla resa già presente —
e il controllo va fatto **prima** di chiudere il lotto, cercando la stringa inglese nei `translation.json` precedenti.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: le 45 unità sono `PENDING`.
- **Nessuna scheda vista nel gioco**: il tab è verificato **sul carattere**, non a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 74/157 (47,1%); restano 83 unità.
