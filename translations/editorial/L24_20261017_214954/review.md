# review.md — L24 · `data/remnant/remnant 1 introduction.txt` (Endless Sky IT)

**Unità** 1.250 (righe 23–3923, file completo) · **contesti** 68 · **parole** 41.087 EN → 38.140 IT
(rapporto complessivo **0,928**; estremi per unità 0,57–1,86) · **parti** 14.
Traduzione eseguita in sessione, senza servizi esterni né sub-agenti.

## 1. Struttura e tipi di unità

| tipo | unità | cosa sono | trattamento |
|---|---:|---|---|
| `MISSION_TEXT` | 1.008 | prosa di missione, con `\t` iniziale e virgolette esterne | tradotte |
| `VALUE` | 52 | nomi di missione (`name "…"`) | tradotti (52/52) |
| `DESCRIPTION` | 52 | istruzioni di missione, con `<destination>`, `<cargo>`, `<payment>` | tradotte, token intatti |
| `CONVERSATION` | 44 | dialoghi a nodi (Taely in mensa, Dawn, Eon) | tradotti |
| `UI_LABEL` | 43 | nomi di nodo, bersagli di `goto` | **identiche** |
| `DIALOG` | 28 | avvisi di sistema («Sei tornato su `<planet>`, ma…») | tradotti |
| `LOGBOOK` | 22 | voci di diario su Taely, Chilia, Plume, Dawn | tradotte |
| `TEXT` | 1 | l'avviso sul motore di salto rotto (unità 786) | tradotto |

`NT` = **43**: tutte e sole le `UI_LABEL`, enumerate una per una. Nessun `label` di condizione
dentro `conversation` in questo file, quindi `NT` coincide con `kind == UI_LABEL`. `TOKEN_EXC` vuoto:
il sorgente non contiene pronomi-token (`<they>`, `<their>`, …).

## 2. Casi linguistici nuovi

1. **I Remnant non parlano: cantano.** Il verbo inglese `chant` è reso in modo differenziato e
   coerente per tutto il lotto: **intona** (registro neutro), **trilla** (entusiasmo, sorpresa),
   **canta** (frase compiuta, annunci), **gorgheggia** (dubbio, riflessione). Il tono di voce è
   indicato dal verbo, non da avverbi aggiunti.
2. **Lingua dei segni.** `sign` → **segna**, `signs` → **segni**, «risponde a segni», «con un gesto
   che credi significhi…». Il giocatore impara i segni nel corso del lotto (unità 652): la traduzione
   mantiene l'incertezza («credi si traduca con», «che sospetti sia») invece di spiegare.
3. **Sette voci distinte**, ognuna con un registro riconoscibile: **Torza** (prefetto, burocrate
   asciutto, frasi brevi e congedi formulari), **Taely** (ingegnera, tecnica e concreta, «Al punto»),
   **Chilia** (militare, autoconsapevole, sintassi piana), **Plume** (xenobiologo, esclamativo, note
   che «si perdono su un tono mesto»), **Aeolus** (logistica, discorso economico, metafore
   commerciali), **Dawn** (giovane ricercatrice, entusiasta, si corregge), **Eon** (entusiasta delle
   navi, divaga e si scusa).
4. **Formule dei Remnant.** `May the Embers burn bright for you` → «Che le Braci brucino luminose per
   te» (congedo standard); `Embers guide your path` → «Che le Braci guidino il tuo cammino»;
   `may the Embers watch over you` → «che le Braci veglino su di te». Le tre varianti restano distinte
   perché lo sono nel sorgente.
5. **`Seeker`** → **Cercatrice** (unità 1107–1110): titolo informale di rispetto per gli esploratori
   dello spazio profondo, con la spiegazione di Dawn conservata («un titolo che sia aspiro a
   guadagnarmi sia sento di non meritare ancora»).
6. **Simbionti** (unità 1017–1027, 1081–1117): il lessico resta fisiologico e non horror («simbionte»,
   «si attaccano a zone diverse del corpo», «mangiamo per due»), perché il testo insiste sul rapporto
   simbiotico e non sulla mostruosità.
7. **Numerazione esadecimale** (unità 1187–1217): i Remnant contano in base 16. Le stringhe del
   sorgente con lettere nelle cifre sono riprodotte **alla lettera** (`2.B1`, `F4240`, `E8D4A51000`,
   `2710`, `61A8`, `2730`): non sono refusi da correggere, sono il testo originale. La spiegazione
   della base 16 (unità 1205) è tradotta per intero, compreso l'esempio `F = 15`.

## 3. Terminologia (decisioni di questo lotto)

| inglese | italiano | nota |
|---|---|---|
| `Key Stone` | Pietra Chiave | famiglia coerente con L23 |
| `Quantum Key Stone` | Pietra Chiave Quantistica | |
| `Keystones` | Pietre-Chiave | plurale con trattino, come da glossario |
| `Threshold` | Threshold | invariato: nome proprio dell'anomalia |
| `void sprites` | spettri del vuoto | |
| `Archon`, `Drak`, `Puffin`, `Penguin`, `Ibis`, `Starling`, `Albatross`, `Pelican`, `Gull` | invariati | nomi di nave o di entità |
| `Void Rifle` | Fucile del Vuoto | arma costruita dal tentacolo |
| `jump drive` / `hyperdrive` | motore di salto / iperguida | |
| `ramscoop` | ramscoop | nome dell'apparecchiatura |
| `Heat Shunt`, `Systems Core` | Derivatore Termico, Nucleo di Sistema | `outfit` |
| `supercapacitor` | supercondensatore | |
| `IFF`, `Quantum Entangled Communicator` | IFF, Comunicatore a Entanglement Quantistico | |
| `Quarg`, `Hai` | invariati | specie |
| `Ember Waste` | Distesa di Braci | |
| `ancestral space` | spazio ancestrale | maiuscolo solo come nome proprio |
| `outfitter` | fornitore di equipaggiamento | anche `logistics office` → ufficio logistico |
| `'Shadow Hope'` | «Speranza d'Ombra» | nome dato da Taely, traducibile |
| `Plume`, `Taely`, `Chilia`, `Torza`, `Aeolus`, `Dawn`, `Eon` | invariati | nomi propri |

## 4. Ripetizioni e duplicati

- **78 gruppi / 195 unità** con inglese identico nel file: l'italiano identico è ammesso solo lì
  (`DUP_OK` deriva dal sorgente). Casi tipici: le sei risposte «(Not now.)», le dodici «(Yes.)»,
  i cinque `Broken Jump Drive Delivery`, i tre «You've plundered another broken jump drive…».
- **Duplicati falsi, corretti a mano** (l'italiano non può coincidere dove l'inglese differisce):
  108 vs 194 (`helping you out` / `helping you`), 655 vs 119/158 (`Sorry, not interested.` /
  `Sorry, I'm not interested.`), 883 vs 684 (`I would rather not.` / `I'd rather not.`),
  1132 vs 888 (`Alright, let's get going.` / `Okay, let's go.`), 1240 vs 922/927
  (`(Nod.)` / `(Nod affirmatively.)`).

## 5. Correzioni fatte durante il lotto

| unità | difetto | correzione |
|---|---|---|
| 47 | frase sul pasto abbondante ereditata dalla 20, assente nell'inglese | rimossa |
| 61, 114 | rapporto di lunghezza sotto la soglia | riscritte più esplicite |
| 108 | duplicato italiano con 194 | riscritta |
| 489 | tab iniziale perso (`tab IT 84 / EN 85`) | tab ripristinato |
| 618 | 4 virgolette contro 3 del sorgente (citazione mai chiusa) | chiusura rimossa |
| 655 | duplicato italiano con 119/158 | «Mi spiace, non mi interessa.» |
| 657 | `Be', viaggi…` flaggato come parola inglese `be` | «Beh, viaggi…» |
| 883 | duplicato italiano con 684 | «Preferirei proprio di no.» |
| 911 | 4 virgolette contro 3 del sorgente | chiusura rimossa |
| 1132 | duplicato italiano con 888 | «Bene, mettiamoci in cammino.» |
| 1240 | duplicato con 922/927; poi rapporto 3,00 | «(Fai cenno.)» (rapporto 1,86) |

**41 unità con virgolette dispari** nel sorgente (23, 68, 72, 74, 78, 79, 120, 234, 250, 251, 307, 332,
380, 382, 411, 412, 418, 435, 452, 492, 495, 496, 618, 723, 727, 728, 747, 801, 816, 830, 844, 880,
911, 920, 938, 988, 1072, 1074, 1104, 1116, 1133): il conteggio è stato **riprodotto**, non
normalizzato.

## 6. Limiti noti (non correggibili dallo staging)

1. **`<compared>` (unità 373)** non è una parola: è una sostituzione definita nei dati del gioco
   (`remnant 1 introduction.txt` riga 966), con due varianti in **inglese** che questo workflow non
   può modificare. L'italiano tiene il segnaposto all'inizio della frase (`<compared>: rispetto
   all'architettura…`), con resa imperfetta nella seconda variante. Va segnalato a chi cura i dati del
   gioco, non «aggiustato» traducendo il token.
2. **Cifre anomale** (unità 1067: `3F6290` masse solari, `24D2` gradi Kelvin) riprodotte alla lettera:
   sono esadecimali nel testo originale, non errori di trascrizione.
3. **`'Shadow Hope'`** tradotto in «Speranza d'Ombra»: è un nome proprio che il giocatore può
   rinominare, quindi la traduzione non rompe nulla; resta una scelta, non un obbligo.

## 7. Esito dei controlli (misurato)

`check.py` (lotto completo): **`FAIL totale: 0`** · copertura **1250/1250** · tab **931/931** ·
virgolette **2111/2111** · token **255/255** · backtick 0/0 · nessuna parola inglese residua ·
tipografia pulita (nessun trattino lungo) · rapporto 0,57–1,86 · `state.db` 364/32560 con tutte le
unità del lotto `PENDING`.

`verify.py` (indipendente): **24 controlli, exit 0**. Include riga grezza identica al file su tutte le
1.250 unità, `english`/`kind`/`path` identici al database, file completo (23–3923, nulla prima né
dopo), copertura dello staging 1250/1250 da un solo lotto, `NT` identiche, token in parità esatta,
assenza di trattini lunghi, ricostruzione di `translation.json` dalle 14 parti.

`translation.json` sha256[:16] **92e4737d1b55d9dc** (dopo l'ultima esecuzione di `check.py`).

## 8. Cosa **non** è stato fatto

- **Rendering nel gioco**: non eseguito. La resa delle accentate dipende dall'atlante bitmap del font
  e resta **non verificata**. Nessuna riga di questo lotto è stata vista a schermo.
- **Database**: nessuna unità è stata approvata; lo staging non è approvazione (`APPROVED` resta 364).
- **Build e packaging**: non eseguiti.
- **Revisione umana**: il lotto è stato riletto in sessione, unità per unità, ma non da un revisore
  terzo. I controlli strutturali non certificano la qualità della lingua.
