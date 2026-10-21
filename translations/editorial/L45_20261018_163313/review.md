# L45 — revisione editoriale

`data/successors/successor 2 ghosts.txt` · righe 37–2167 · 680 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. Lessico fissato in questo lotto

| EN | IT | nota |
|---|---|---|
| Successors | **Successori** | invariato rispetto ai lotti precedenti |
| High Houses / New Houses | **Casate Alte** / Casate Nuove | «Casa» per `House`, con nome proprio invariato |
| Chydiyi, Myurej, Seineq, Kaatrij, Sioeora, Aqrabe | invariati | nomi delle Casate |
| Saajret, Sijra, Rijatet, Kampa, Resja, Tiliia, Khiajsore, Riijaaora | invariati | persone |
| cloak (tecnologia) | **mantello** | `cloak detector` → **rilevatore di mantelli**; `cloaking armor` → **armatura occultante** |
| cloaked / to cloak | **occultato** / **occultarsi** | participio e verbo distinti dal sostantivo |
| wormhole | **cunicolo** | `mouth of the wormhole` → **bocca del cunicolo** |
| heirloom warship | **nave da guerra di famiglia** | reso esplicito il valore di reliquia |
| keystones | **chiavi di volta** | termine già usato nei lotti Aqrabe |
| stellar metal | **metallo stellare** | invariato |
| the Tangled Shroud | **il Tangled Shroud** | nome di regione: **28 occorrenze invariate** nel corpus, tradurlo qui romperebbe la continuità |
| Shroud (da solo) | **Shroud** | invariato, 43 occorrenze storiche |
| Ribbons of Iret | **Nastri di Iret** | pennacchi bioluminescenti |
| Knight-Vassal | **Cavaliere-Vassallo** | titolo conferito a fine lotto |
| suzerainty / vassalage | **sovranità** / **vassallaggio** | registro feudale mantenuto |
| coilgun | **coilgun** | nome di arma, invariato come `GRASER` in L44 |
| debriefing | **debriefing** | prestito consolidato nella serie |

### Registro arcaico dei Successori

Il sorgente usa `thou`/`thee`/`thy`/`hast`/`'tis`/`'twould`. In italiano è reso con un registro
**sostenuto ma leggibile**: forme come «che tu voglia», «se ti servisse», «non ti ostacolerà», evitando
arcaismi lessicali (`voi` allocutivo, `deggio`) che invecchierebbero il testo. La seconda persona singolare
è mantenuta in tutto il lotto: nessuna alternanza tu/voi.

## 2. Limite dichiarato: 4 righe di diario senza testo

Le unità **195, 305, 357, 418** sono `LOGBOOK` ma il loro `english` è solo la **categoria**
(`People`, `Factions`). Il sorgente è:

```
log "People" "Saajret, of Somber Sejra" "Saajret, of Somber Sejra is an archivist, ..."
```

`tools/l10n.py` (protetto) estrae come unità la **categoria** quando il testo del diario è fra
**virgolette** invece che fra backtick. Conseguenza: quelle quattro schede di diario (Saajret, i
Successori come specie, Kampa, Resja) **non hanno testo italiano** e nel gioco comparirebbero in inglese.

- Non è stato toccato nulla: `tools/l10n.py`, `state.db`, `glossary.csv` e `inventory_fields.csv` sono
  protetti da hash (`state.py` li verifica a ogni preflight, `INTEGRITA'` OK).
- `check.py` e `verify.py` **asseriscono** la lacuna (categoria identica al sorgente, testo fuori
  dall'unità) invece di nasconderla: un test che passasse per omissione sarebbe peggio del difetto.
- Rimedio possibile in futuro: estendere l'estrattore alle forme `log "C" "N" "testo"`. Richiede una
  decisione esplicita dell'utente, perché cambia `state.db`.

## 3. Decisioni puntuali

1. **`Sirja` → `Sijra`** (unità 146, 147): il corpus ha **51 occorrenze di `Sijra` e 0 di `Sirja`**;
   il nome nel sorgente è stato scritto in due modi. Si allinea alla forma dominante, non si introduce
   una terza grafia.
2. **`(No.)` → `(No.)`** (nodo conversazione 137): l'opzione è già italiana. Forzare una variante
   («(No grazie.)») cambierebbe il senso dell'opzione. Registrato in `CONV_SAME`, non corretto a mano.
3. **`(Sì.)` vs `"I have."`** (unità 193 vs 470): il primo stesura rendeva entrambe con «Sì.»; il
   controllo duplicati ha segnalato la collisione perché l'inglese è diverso. 470 è diventato
   **«L'ho fatto.»** — la risposta breve a «hai visto questo posto?».
4. **`(Stay silent.)` / `(Remain silent.)`** (241, 377 / 608): le prime due sono identiche nel
   sorgente e restano identiche in italiano; la terza no, e diventa **(Non dire nulla.)** per non
   creare un duplicato che il sorgente non giustifica.
5. **Quadre**: i frammenti redatti usano `[...]`. In prima stesura 657 e 669 avevano **una quadra in
   più** (un `[...]` inserito per spezzare «quel pieno di fitte»). Il `check.py` ha misurato 6 vs 7 e la
   frase è stata riscritta sul conteggio esatto. Il numero di `[` e `]` è un **invariante del testo
   redatto**, non una preferenza.
6. **Battute aperte**: 15 unità terminano con una virgoletta aperta (dialoghi che continuano nell'unità
   successiva, tipico dei file `mission`). Sono **riprodotte aperte**: chiuderle cambierebbe il testo di
   gioco. Il confronto è un insieme di idx, non un conteggio generico.
7. **`What now?`** appare due volte come prosa (575) e una come `UI_LABEL` (574): la label resta
   `what now`, la battuta è «E adesso?». Non sono la stessa unità e non vanno allineate.
8. **`House Kaatrij`** come `government` (355, 467, 513) e `High Houses (Unknown)` (552): riferimenti di
   dato, restano in inglese. Nel testo narrativo la stessa entità è sempre **Casa Kaatrij**.
9. **Titoli dei file recuperati**: `"Lost"`, `"Heart"`, `"Trial"`, `"Emptiness"` → **«Persa», «Cuore»,
   «Processo», «Vuoto»**. Sono intestazioni di documento, tradotte perché leggibili come titoli e
   ripetute identiche nelle due occorrenze (651/666, 652/667, 655/668, 657/669).
10. **`no resja` / `no queru` / `no hasur`** (654, 656, 658): `UI_LABEL` di salto. Restano in inglese
    anche se sembrano prosa: sono bersagli di `goto`, tradurli romperebbe il flusso della missione.

## 4. Cosa il lotto **non** dimostra

- Non dimostra che la linea *Ghosts* sia giocabile in italiano: i 36 contesti hanno molti `goto` e
  nessuno è stato percorso nel gioco.
- Non dimostra la resa dei **16 nodi `CONVERSATION`**: sono verificati come testo (tab, token,
  virgolette), non come interfaccia.
- Non dimostra nulla sui **4 diari senza testo** (§2): restano in inglese per costruzione dello
  strumento, non per scelta editoriale.
- Il rapporto lunghezze (0,59–1,79) è dentro il gate 0,55–1,90 ma **non è un giudizio di qualità**:
  segnala solo unità fuori scala, non frasi brutte.
