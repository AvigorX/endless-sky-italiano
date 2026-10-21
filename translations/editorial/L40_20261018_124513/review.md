# L40 — revisione editoriale

Lotto `L40_20261018_124513` · `data/human/free worlds side plots.txt` · righe 18–888 · 211 unità ·
5.683 parole EN → 5.339 IT · `check.py` `FAIL totale: 0` · `verify.py` 29 controlli, exit 0.

Questo documento registra **le decisioni**, non i numeri: i numeri stanno in `REPORT.md` e sono
rigenerabili con i due comandi di verifica.

---

## 1. Che cosa copre il lotto

Nove trame secondarie delle Free Worlds, non legate all'arco principale: il convoglio per l'ampliamento
del New Port di Zug; il monastero di Harmony e il consiglio del monaco David sulla pirateria; il
trasporto di Ijs e degli Anderson per fondare il Conservatorio; i mercantili per l'equipaggiamento di
terraformazione; il Memoriale di Guerra delle Free Worlds; due prove d'arma di Barmy Edward (il
lanciafiamme); il furto della tecnologia dei ramscoop nel Deep; il reclutamento e le tre missioni del
Branco di Lupi contro i convogli di cibo; la scorta del reattore per i Dreadnought; e infine la
conversazione con un capitano della milizia sulla perdita di Greenrock.

Sono **trame accessorie** con personaggi che il giocatore non ha mai visto: il registro non si eredita
dalla campagna principale, si ricostruisce ogni volta.

## 2. Ricognizione (misurata sul `source.json`, non dedotta)

```
MISSION_TEXT 154 · DIALOG 19 · VALUE 15 · DESCRIPTION 15 · LOGBOOK 7 · UI_LABEL 1 · CONVERSATION 0
contesti 19 · tab 133 · virgolette 352 · token 59
unità con numero dispari di virgolette: 2 (56, 202)
unità con quadre: 0
righe `log`: 7 → 7 unità LOGBOOK (1:1)
prima unità alla riga 18 (non 16)
```

Tre fatti che hanno richiesto preparazione e **non** si potevano copiare da L39:

- **`UI_LABEL` torna a 1** (in L39 era 0): la `label` di salto `brower death`, bersaglio di `goto`.
  `NT = {80}`. Copiare la lista vuota avrebbe lasciato la label in inglese e rotto il salto.
- **Due battute aperte** (56, 202): in L39 non ce n'erano, e il `verify.py` confrontava insiemi vuoti.
  Qui l'insieme ha due elementi e va confrontato davvero.
- **Il file inizia a riga 18**: la coppia `(18, 888)` è una misura, asserita nel `verify.py`.

## 3. Metodo

1. `export_section.py` su righe 18–888 → 211 unità, 19 contesti.
2. Ricognizione dei tipi, del `raw` della `UI_LABEL`, delle righe `log`, delle virgolette dispari.
3. `check.py` derivato da L39 con `NT = {80}`.
4. Traduzione in 4 parti a fine contesto (1–66, 67–112, 113–166, 167–211), ognuna chiusa con
   `check.py --range` verde.
5. `check.py` completo e `verify.py` indipendente.

## 4. Le voci di questo lotto

**Il monaco David (Harmony).** Registro piano, senza predicazione: risponde alle domande e non fa
sermoni. La sua battuta migliore è l'autoironia sul monachesimo come «forma di anarchismo utopico»
(unità 32), resa senza ammiccamenti. Il congedo (39) è duro e breve: «Non finirà, non finché non
sterminerete ogni singola persona su quei pianeti.»

**Rex e Fido (Branco di Lupi).** Due registri opposti: Rex è il giovane che argomenta e vuole convincere
(«pensa a quante vite si salveranno»), Fido è il vecchio che non parla quasi mai e quando lo fa mette la
mappa sul tavolo. La traduzione ha tenuto la differenza: Rex fa frasi lunghe e condizionali, Fido una
sola frase per intervento.

**L'Agente Falco.** Il cospiratore teatrale: parla per formule («spregevoli plutocrati», «coraggioso
insorto») e il testo dice esplicitamente che sembra aver provato il discorso. Reso senza mitigare il
ridicolo: è un uomo che si sta divertendo.

**Il capitano della milizia (Greenrock).** Il registro più amaro del file: parla per ricordi e per
recriminazioni, e la sua battuta più lunga (unità 204) è un fiume di rancore contro il Senato. In
italiano ho tenuto la sintassi lunga e le subordinate, senza spezzarla.

**Barmy Edward.** Identico a L36/L39: entusiasmo, mani strofinate, metafore da officina. Le due prove
d'arma (il lanciafiamme) hanno lo stesso ritmo e la stessa insistenza sul «non distruggerla».

**Ijs Springborn.** Il professore che fonda un'università: impaziente, entusiasta, e capace di
un'autoironia amara («mi chiedo se non sia solo una manovra per tenermi fuori dai piedi»).

## 5. Il tema: la fame come arma

Le tre missioni del Branco di Lupi pongono la domanda più scomoda del lotto: affamare la Repubblica per
fermare la guerra. Il testo dà a Rex l'argomento consequenzialista («quante battaglie sanguinose si
eviteranno») e al giocatore la replica deontologica («se usiamo tattiche così riprovevoli... la società
che costruiremo sarà corrotta quanto quella vecchia»).

La traduzione ha tenuto **entrambi gli argomenti alla stessa altezza**, senza far sembrare "giusto" un
ramo: le due risposte (158 e 159) hanno la stessa lunghezza e lo stesso tono. Il `LOGBOOK` 165 descrive
l'esito senza commentarlo.

## 6. Decisioni lessicali

| inglese | italiano | perché |
|---|---|---|
| wolf pack (gergo pirata) | branco di lupi | il testo stesso lo spiega (unità 144); la maiuscola resta solo nel nome del gruppo |
| Bulk Freighter / Auxiliary | mercantile pesante / ausiliario | modelli di nave, tradotti perché descrittivi |
| Ramscoop / Catalytic Ramscoop | ramscoop / Ramscoop Catalitico | equipaggiamento, come nei lotti precedenti |
| Deep Sky, Delta V Corporation | Deep Sky, Delta V Corporation | nomi di azienda, invariati |
| Agent Falco | Agente Falco | pseudonimo: tradotto perché il testo lo presenta come nome fittizio |
| Paradise Planets | Mondi Paradisiaci | glossario |
| breadbasket of the galaxy | il granaio della galassia | metafora, resa letterale |
| Southern Rim | Bordo Meridionale | glossario |
| MSGT (grado) | SGT MAGGIORE | grado militare reso in italiano, in maiuscolo |
| brower death | brower death | `label` di salto, invariata |

**I numeri**: nessun importo fisso; il file usa `<payment>` nove volte come token di dato.

## 7. La lacuna `log`: qui non perde niente

Misurato: **7 righe `log` → 7 unità `LOGBOOK`** (1:1), nessuna forma a tre argomenti, nessuna categoria
emersa. L'inventario è completo rispetto al file; la lacuna generale resta in `tools/l10n.py` (protetto).

## 8. Cosa è stato corretto e perché

- **33**: `"Of course."` reso con «Certo.» stava sotto la banda comoda (0,69); riscritto «Certamente.»
  per stare sopra 0,70 senza cambiare registro.
- **77**: `"Is there anything else you need me to do?"` reso troppo corto (0,66); riscritto «C'è
  qualcos'altro che devo fare per te?».
- **15 / 65 / 69 / 190**: sono quattro varianti quasi identiche dello stesso messaggio, e gli inglesi
  differiscono solo per «the»/«your» o per il punto finale. Rese con tre formulazioni distinte
  («una parte del convoglio», «una parte del tuo convoglio», «Sei arrivato... senza punto finale») perché
  il controllo dei duplicati le vede come unità diverse.
- **202**: battuta aperta dal sorgente (una sola virgoletta): riprodotta senza chiuderla.
- **79–84**: il memoriale di guerra usa rientri crescenti (unità 82 ha due tab, 83 ne ha tre) e un nome
  in maiuscolo. Il costruttore ha conservato i tab e la traduzione il maiuscolo: «SGT MAGGIORE IRENE
  BROWER».

## 9. Controlli e limiti

`check.py` (22 controlli): copertura, unità vuote, `NT` identiche, duplicati italiano spiegati dal
sorgente, tab e virgolette per unità e come totale, quadre per unità, token `<...>`, backtick, spazi,
rapporto lunghezze, tipografia, caratteri non latini, parole inglesi residue, stato del database.

`verify.py` (29 controlli) **non riusa** la logica di `check.py`: ricostruisce tutto da `source.json`, dal
file sorgente e da `state.db` in sola lettura, e in più asserisce (a) che l'unica `UI_LABEL` sia la 80,
(b) che non ci siano `CONVERSATION` (asserzione di assenza), (c) che non ci siano quadre, (d) che le
virgolette dispari siano esattamente 56 e 202, (e) che le 4 parti ricostruiscano `translation.json`,
(f) la copertura totale 211/211 e la coppia di righe (18, 888).

Limiti, dichiarati:

- **Il lotto non è nel gioco.** Nessuna approvazione nel database, nessun caricamento: 211 unità
  `PENDING`.
- **Nessuna verifica nell'editor.** In particolare non è verificato come vengano resi a schermo i rientri
  multiple del memoriale (79–84).
- **Il rapporto 0,72–1,61 non è un giudizio di qualità.**
