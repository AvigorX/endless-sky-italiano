# L48 — revisione editoriale

`data/avgi/avgi side missions.txt` · righe 26–499 · 180 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. La voce Avgi: la modalità dichiarata prima della frase

Gli Avgi non parlano come gli umani né come i Successori. Ogni loro battuta **comincia con
l'etichetta della modalità** e molte **finiscono con la parola che dichiara il tipo di frase**:

```
"Is this one of the humans I have heard so much about, question?"
"Amusement. The other humans had chairs made to suit your forms, they did."
"Approving. An astute observation."
```

Scelta: **riprodurre il dispositivo, non normalizzarlo**. `question` finale → **«, domanda?»**;
l'etichetta resta un sostantivo isolato («Divertimento.», «Approvazione.», «Considerazione.»,
«Sorpresa.», «Sconcerto.», «Riconoscenza.», «Contemplazione.», «Accordo.», «Interesse.»,
«Curiosità.», «Spiegazione.», «Preso atto.», «Deferenza rispettosa.», «Crepuscolo» in L49 →
«Cautela.», «Tristezza.», «Istruzione.», «Sdegno.», «Entusiasmo.», «Anticipazione.», «Fretta.»
«Allarme.»).

Perché non gli avverbi («Divertito, disse…»): l'etichetta in inglese è **una parola singola seguita da
punto**, e nel gioco funziona come una didascalia emotiva; trasformarla in avverbio la fonderebbe nella
frase e cancellerebbe la firma della specie. La traduzione resta leggibile perché l'etichetta è separata
dal punto, come nel sorgente.

**Conseguenza da conoscere**: le etichette sono **ripetute** («Divertimento.» compare molte volte). Il
controllo duplicati del `check.py` lavora sulle unità intere, non sulle singole parole, quindi non le
segnala; è corretto così.

## 2. Il gioco nel gioco: Trefoil e il Foil

`Trefoil` è un gioco da tavolo inventato, con tre triangoli colorati e un terzo colore neutro chiamato
**`the Foil`**. Scelta: **entrambi invariati**.

- `Trefoil` non ha glossa nel testo: è un nome proprio, e tradurlo («Trifoglio») inventerebbe un
  referente che il giocatore non può verificare altrove.
- `the Foil` è definito **in scena** («It — the Foil — è un attore esterno…»): il nome resta e la
  spiegazione la dà il testo, non il traduttore.
- Coerenza: nel corpus i nomi di tecnologia e di nave restano invariati (`GRASER`, `Shroud`,
  `Tangled Shroud`); un gioco alieno segue la stessa regola.

## 3. Nomi di regione e di tecnologia: la forma dominante vince

| termine | resa | motivo |
|---|---|---|
| `Twilight` | **invariato** | 10 occorrenze invariate nel corpus contro 2 «Crepuscolo» |
| `Outer Limits` | **invariato** | 4 contro 1 «Limiti Esterni» |
| `Twilight Guard` | **invariato** | nome di forza armata, come le navi |
| `Tangled Shroud` | **invariato** | 28 occorrenze già invariante (decisione 153) |
| `hyperdrive` | **invariato** | 75 contro 40 «iperguida»; i lotti recenti (L43, L44) lo tengono |
| `Aberrant` | **l'Aberrante** | descrittivo usato come nome: la maiuscola basta a segnalarlo |
| `polities` | **entità politiche**, poi **entità** | «politia» in italiano è arcaico e si legge come refuso di «polizia» |
| `Assembly of Polities` | **Assemblea delle Entità** | segue la scelta precedente, e il testo la usa come nome formale |
| `Consonance` / `Dissonance` | **la Consonanza** / **la Dissonanza** | coppia di nomi parlanti, va tradotta in coppia |
| `Freelancers` | **gli Indipendenti** | in inglese è descrittivo (coalizione contro tasse e controlli), non un nome proprio |
| `Zapchannel Ray Energy` | **invariato** | marchio commerciale truffaldino, virgolettato nel diario |
| `Wisteria`, `Nikkio`, `Aviskir`, `Anax`, `Weledos`, `Peripheria` | **invariati** | nomi propri |

## 4. Decisioni puntuali

1. **`the War`** con la maiuscola → **«la Guerra»** con la maiuscola: nel testo è un evento storico
   determinato (la guerra contro l'Aberrante), non una guerra qualsiasi.
2. **`rods from god`** non compare; compare invece `nickel-iron roidsteel`, reso **«acciaio asteroidale
   al nichel-ferro»**: il termine tecnico si spiega da sé e non introduce prestiti.
3. **`Akoustiki Excursion Vehicle`** invariato: nome di modello, come `Polari` (nave).
4. **`megatons` → «megatoni»**, `kilometers` → «chilometri», `credits` → «crediti»: unità di misura
   tradotte, cifre invariate.
5. **`Quis Nectar`** → **«Nettare Quis»**: è un cocktail, il nome del frutto alieno resta e la parola
   «nettare» è già italiana.
6. **Le due varianti della stessa scena** (bere tutto / sorseggiare; accettare / rifiutare il campione)
   sono rese **parallele e distinte**: il testo cambia esito (morte, superpoteri, rifiuto) e le
   traduzioni non sono state uniformate.
7. **Unità 21**: `That sure looks comfortable.` è sarcastico; reso con «Sembra proprio comodo.», che in
   italiano mantiene l'ironia senza aggiungere un avverbio.
8. **Unità 44**: `You're no regular so I'll start you off with a Quis Nectar.` → «Non sei un cliente
   abituale, quindi comincio con un Nettare Quis.»: `regular` è il cliente fisso, non il «normale».

## 5. Cosa il lotto **non** dimostra

- Non dimostra che la linea Avgi sia giocabile in italiano: i 2 contesti hanno molti `goto` e nessuno è
  stato percorso nel gioco.
- Non dimostra la resa **a schermo** delle etichette di modalità: sono verificate come testo, non in
  interfaccia. È il rischio principale di questa scelta (§1).
- Il rapporto lunghezze (0,60–1,30) è dentro il gate ma **non è un giudizio di qualità**.
- Il file **non è completo**: 256 unità dopo la riga 499 non sono state toccate in questo lotto.
