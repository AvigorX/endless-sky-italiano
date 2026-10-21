# L34 — revisione editoriale

Lotto `L34_20261018_115356` · `data/human/free worlds 0 prologue.txt` · righe 16–2502 · 703 unità ·
18.612 parole EN → 17.855 IT · `check.py` `FAIL totale: 0` · `verify.py` 27 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

`free worlds 0 prologue.txt` è il primo atto della campagna delle Free Worlds, e come i file di L32 e
L33 **finisce con il lotto**: riga 16 è la prima unità del file, riga 2502 l'ultima. La copertura
703/703 è quindi un invariante legittimo e non una coincidenza.

Il contenuto, in ordine: le ricognizioni per conto del Patto di Difesa Reciproca del Sud; l'interrogatorio
di un ufficiale della Marina senza insegne; il reclutamento di Katya Reynolds con una pistola scarica alla
testa; il trasporto di due "turisti" che sono in realtà una scienziata planetaria e un ex ufficiale
dell'intelligence in fuga; il furto legale dell'equipaggiamento di un drone da sorveglianza; la cena con
i monaci e la litania della sera; la caccia al sito dei test nucleari; l'invito formale a unirsi alle
Free Worlds e la prima battaglia per difendere Sabik.

È il lotto che **costruisce l'antagonista politico** della campagna: la Repubblica non è cattiva, è
un'istituzione che si sta comportando in modo sempre più duro, e i personaggi lo dicono esplicitamente
(unità 479: la Marina come agenti di polizia a cui viene chiesto di combattere contro chi aveva giurato
di proteggere). La traduzione non ha attenuato questa ambiguità: è il senso del testo.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 520 · LOGBOOK 59 · DIALOG 44 · VALUE 40 · DESCRIPTION 40 · UI_LABEL 0 · CONVERSATION 0
contesti 43 · tab 483 caratteri (468 unità con tab iniziale) · virgolette 1.274 · token 191
unità con parentesi quadre [a, b]: 0
unità con numero dispari di virgolette: 12
```

Tre differenze rispetto a L33 che hanno richiesto lavoro di preparazione e **non** si potevano copiare:

- **`NT` è vuoto.** In L33 erano 11 `UI_LABEL` di salto. Qui non c'è nessuna unità non traducibile:
  nessuna `label`, nessun riferimento di dato (`scene`/`thumbnail`), nessuna `CONVERSATION`. Il
  `verify.py` **asserisce** che i tre insiemi siano vuoti, così un cambio di inventario fa fallire il
  controllo invece di passare in silenzio.
- **Le parentesi quadre non ci sono.** Il controllo strutturale di L32/L33 è stato **rimosso dal
  `check.py`** (confrontare due liste vuote passa sempre: sarebbe una finta verifica) e sostituito da
  un'asserzione nel `verify.py`: `0 unità con [a, b]`. Se un lotto futuro sullo stesso gioco
  reintroducesse le parentesi, il verify di L34 diventa rosso e la sessione successiva lo scopre.
- **Dodici battute aperte.** Il sorgente apre una citazione e non la chiude sulla stessa riga; il
  `verify.py` confronta l'**insieme degli idx** con conteggio dispari, non solo il totale.

## 3. Metodo

1. `export_section.py` su righe 16–2502 → 703 unità, 43 contesti.
2. Ricognizione dei tipi, delle righe `log`, delle virgolette dispari e delle parentesi quadre **prima**
   di scrivere una riga di traduzione.
3. `check.py` derivato da L33 con `NT = set()`, `TOKEN_EXC` vuoto, controllo parentesi quadre rimosso.
4. Traduzione in 11 parti a fine missione, ognuna chiusa con `check.py --range A B` verde.
5. `check.py` completo (duplicati, copertura, tipografia, token) e `verify.py` indipendente.

Le parti: 1–75, 76–133, 134–190, 191–243, 244–309, 310–386, 387–438, 439–491, 492–551, 552–628,
629–703. Il confine è sempre a fine missione.

## 4. Le voci di questo file

Cinque voci distinte, ricavate dal testo. Nessuna è stata importata dai lotti precedenti.

**Freya Winters.** Cortesia calorosa e un registro devoto che nel testo è quasi una firma: dice
«I pray the pirates didn't give you too much trouble», dove «I pray» è un modo gentile di dire «spero».
In italiano: **«Confido»** quando la frase è una formula, «Spero» quando è un timore. Non è una scelta
stilistica arbitraria: se si traducesse sempre «prego» il personaggio sembrerebbe in preghiera in ogni
battuta, se si traducesse sempre «spero» si perderebbe l'unico tratto che la distingue dagli altri
ufficiali.

**Tomek Voigt.** Asciutto, militare, senza giri di parole; quando è arrabbiato lo dice per intero
(unità 256: le lettere alle cinque famiglie). Non usa mai un vezzeggiativo, e in italiano non ne ha.

**Katya Reynolds.** Scanzonata, sfacciata, piena di slogan e di humour fisico: punta una pistola scarica
per «testare» il giocatore, lo chiama «kid», parla di sé come di una che «combatte come una femmina di
tasso». In italiano tiene il registro colloquiale, e le battute più assurde restano assurde (unità 347).

**Mr. Eyes / Ijs Springborn.** Entusiasta, tecnico, con una parlantina da conferenza stampa; usa
«kid» anche lui, ma senza l'aggressività di Katya. Il suo lessico tecnico (isotopi, reattori, impianti)
è tradotto con termini comuni, non con gergo: chi legge deve capire il ragionamento, non ammirare la
terminologia.

**I monaci (Greg, David).** Ritmo lento, frasi semplici, nessuna fretta. La litania (unità 533–534) è
l'unico punto del lotto in cui il testo diventa **formula**, e in italiano è stata resa con la stessa
struttura ripetitiva («...buon Signore, liberaci»), non con una parafrasi.

## 5. Le parentesi quadre: perché il controllo non c'è

In L32 e L33 il controllo strutturale «gruppi e alternative» era il controllo più utile del lotto:
fermava tre errori in L33 che nessun altro controllo vedeva. Qui non serve, perché le unità con `[a, b]`
sono **zero**.

La scelta è stata fra tre possibilità, e le prime due sono sbagliate:

1. **Copiare il controllo** → confronta `[]` con `[]` su ogni unità, passa sempre, e la riga «OK» nel
   report diventa una bugia: dice che una cosa è stata verificata quando non c'era niente da verificare.
2. **Togliere il controllo e basta** → se il file cambiasse (o se un lotto futuro sullo stesso gioco
   reintroducesse la sintassi), nessuno se ne accorgerebbe.
3. **Toglierlo dal `check.py` e mettere un'asserzione nel `verify.py`**: `0 unità con [a, b]` nel
   sorgente. È la forma scelta: il controllo non finge di verificare la struttura, ma **verifica che non
   ci sia struttura da verificare**, e diventa rosso se le premesse cambiano.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| Southern Mutual Defense Pact | Patto di Difesa Reciproca del Sud | nome dell'organizzazione; reso per esteso la prima volta, poi «il Patto» |
| Free Worlds | Free Worlds | nome proprio della fazione, invariato (come «Coalition» → Coalizione, ma qui il nome è già la marca della campagna) |
| Free Worlds Council | Consiglio delle Free Worlds | |
| Dirt Belt | Fascia di Terra | regione impoverita; «cintura» sarebbe stato ambiguo |
| Paradise Planets | Mondi Paradisiaci | già fissato nei lotti precedenti |
| Rim / Core | Bordo / Nucleo | regioni galattiche |
| Thousand Eyes | Mille Occhi | nome del programma di sorveglianza |
| Mr. Eyes | Mr. Eyes | soprannome; la battuta che lo spiega (unità 413, «pronunciando il nome come "Eyes"») funziona solo se resta invariato |
| Brother Greg / Brother David | fratello Greg / fratello David | titolo monastico, minuscolo come in italiano corrente |
| the Brothers (on Harmony) | i Fratelli | comunità monastica, maiuscolo come nome proprio |
| Dereliction and Salvage Act of 2976 | Legge sull'abbandono e il recupero del 2976 | nome di legge: tradotto, perché il testo ne spiega il contenuto |
| salvage (operazione) | recupero | termine legale, coerente con il nome della legge |
| vigilanter nuclear power plant inspector | ispettore nucleare autonomo | «vigilante» in italiano evoca il giustiziere; qui è un cittadino che fa controlli |
| janitor | inserviente | |
| kid | ragazzino | usato da Katya e da Eyes, con toni diversi |

**Il registro religioso.** Tre personaggi usano parole religiose in modo diverso, e la differenza è
significativa:

- **Freya**: «I pray» è una formula di cortesia devota → «Confido» / «Spero».
- **JJ**: «I pray that we don't have to» + «God willing» è fede vera → «Prego che non dobbiamo farlo» /
  «se Dio vuole».
- **I monaci**: la litania è preghiera in senso proprio → resa come formula, non parafrasata.

**I numeri.** «400,000 credits» → «400.000 crediti», «1,100 credits per diem» → «1.100 crediti al
giorno»: separatore delle migliaia italiano, come da convenzione di progetto.

## 7. La lacuna `log`: qui la forma è quella di L32/L33

Misurato sul file, non dedotto:

- **59 righe `log`** nell'intervallo 16–2502 → **59 unità `LOGBOOK`**: corrispondenza 1:1.
- L'unità prodotta è il **testo del diario**, non la categoria.
- **5 righe** hanno la forma a tre argomenti `log "Categoria" "Nome" `testo``:

| riga | categoria | nome |
|---|---|---|
| 1622 | `People` | `Katya Reynolds` |
| 1623 | `People` | `Ijs Springborn` |
| 2308 | `People` | `Alondo Gruyere` |
| 2310 | `People` | `Freya Winters` |
| 2311 | `People` | `Jean-Jacques Soleau` |

Sono le schede biografiche dei cinque membri del Consiglio. Il testo è tradotto (unità 406, 407, 661–664);
categoria e nome restano in inglese e non sono inventariati. È la stessa forma di perdita di L32 e L33, e
l'opposto di L30 (dove la perdita era il testo).

Non è riparabile da questo lotto: `tools/l10n.py` e `state.db` sono file protetti con hash registrato.
La lacuna è documentata qui e nel checkpoint, non corretta.

## 8. Cosa è stato corretto e perché

- **118 / 394**: due inglesi diversi (`Sure, I'd be glad to do that.` / `Sure, I would be glad to.`)
  avevano lo stesso italiano. Il controllo dei duplicati — che scatta solo sul lotto **completo** — le ha
  segnalate; differenziate in «Certo, lo farò volentieri.» e «Certo, con piacere.».
- **243**: la resa breve di «It does» dava 0,67, sotto la banda comoda. Riscritta «Sì, questo risponde».
- **543**: «Altro?» dava 0,65. Riscritta «Qualcos'altro?».
- **585**: «Giusto. Proviamo.» dava 0,56, sotto il gate. Riscritta «Giusto, mi sembra ragionevole.
  Proviamo.», che è anche più vicina al tono di Katya quando sta per convincere qualcuno.
- **365**: refuso «della sottigliezza e della depistaggio» → «del depistaggio».
- **Le dodici battute aperte** sono state riprodotte, non chiuse: chiudere una citazione che il sorgente
  lascia aperta cambierebbe il testo mostrato dal gioco (e il controllo per unità lo segnala).

## 9. Controlli e limiti

`check.py` (21 controlli) verifica: copertura, unità vuote, `NT` identiche, duplicati italiano spiegati
dal sorgente, tab e virgolette per unità e come totale, token `<...>`, backtick, spazi, rapporto
lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database. **Non** contiene
il controllo delle parentesi quadre, rimosso per la ragione di §5.

`verify.py` (27 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`,
dal file sorgente su disco e da `state.db` in sola lettura, e in più asserisce che (a) non ci siano unità
non traducibili, (b) non ci siano parentesi quadre, (c) le virgolette dispari siano esattamente quelle
del sorgente, (d) le 11 parti su disco ricostruiscano `translation.json`.

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 703 unità
  `PENDING`, come da mandato.
- **Nessuna verifica nell'editor.** Il testo non è stato visto renderizzato; in particolare la litania
  dell'unità 533–534 è lunga e non è verificato come venga impaginata a schermo.
- **Il rapporto 0,71–1,69 non è un giudizio di qualità.** Dice solo che nessuna unità è stata compressa
  o gonfiata fuori misura.
