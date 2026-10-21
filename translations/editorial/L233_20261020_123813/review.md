# review.md — L233 (`data/avgi/avgi news.txt`, righe 32–91)

Registro delle decisioni editoriali del **primo lotto** di `avgi news.txt`. Il file è di tipo `NEWS`: ventidue
dichiarazioni di Avgi sotto assedio, ognuna introdotta dall'**etichetta di modalità** della specie (decisione 167).

## 1. Le 22 etichette: riprodotte, non liquefatte

| inglese | resa | nota |
|---|---|---|
| `Dejection.` | **Scoramento.** | «Deiezione» in italiano è un termine clinico: sbagliato per un'emozione |
| `Rejection.` | **Rifiuto.** | |
| `Remembrance.` (×2) | **Ricordo.** (×2) | l'inglese ripete l'etichetta in due notizie distinte: la ripetizione si conserva |
| `Guilt.` | **Colpa.** | |
| `Worry.` | **Preoccupazione.** | |
| `Sorrow.` | **Dolore.** | «Tristezza» è riservato a `Sadness` |
| `Anger.` | **Rabbia.** | |
| `Curiosity.` | **Curiosità.** | |
| `Satisfaction.` | **Soddisfazione.** | |
| `Optimism.` | **Ottimismo.** | |
| `Relief.` | **Sollievo.** | |
| `Frustration.` (×2) | **Frustrazione.** (×2) | due notizie diverse, stesso stato: ripetizione conservata |
| `Appeasing.` | **Placazione.** | il mercante che placa la folla: «accondiscendenza» suonava morale, «placazione» descrive l'atto |
| `Exasperation.` | **Esasperazione.** | distinta da `Frustration`, come nell'inglese |
| `Wonder.` | **Meraviglia.** | |
| `Confusion.` | **Confusione.** | |
| `Sadness.` | **Tristezza.** | distinta da `Sorrow` |
| `Hurt.` | **Offesa.** | il torto subito, non la ferita fisica: chi parla è un cucciolo Avgi |
| `Loss.` | **Perdita.** | |
| `Despair.` | **Disperazione.** | |

Le etichette sono **la firma della specie**: appiattirle in avverbi («Tristemente, la mia famiglia…») renderebbe gli
Avgi indistinguibili dagli altri popoli, come già stabilito in L48. Il `check.py` confronta la lista completa delle 22
etichette, non un campione.

## 2. `Aberrations`, `Aberration`, `Aberrant`: un nome solo

L'inglese alterna tre forme per la stessa cosa:
- `the Aberrations` (plurale, unità 3) → **gli Aberrant**
- `the Aberrant` (collettivo, unità 4, 6, 9, 13, 16, 22) → **gli Aberrant**
- `an Aberration` (singolare, unità 10) → **un Aberrant**

Resa unica, come da decisione 25 (`Aberrations` → «Aberrant», un solo nome per la fazione e per i suoi individui). Il
controllo vieta esplicitamente «Aberrazione»: sette occorrenze italiane contro cinque inglesi più le due forme
singolari/plurali della stessa radice.

## 3. Nomi e istituzioni

| inglese | resa | perché |
|---|---|---|
| `the Consonance` | **la Consonance** (3) | invariato: forma del corpus (L2, L19, L48), decisione aperta 2 |
| `the Avgi` | **gli Avgi** (3) | specie, invariata |
| `the Tangled Shroud` / `the Shroud` | **il Tangled Shroud** (2) / **lo Shroud** (2) | invariato (31 occorrenze nello staging); la forma breve è quella del testo |
| `the Anax system` | **il sistema Anax** | toponimo invariato |
| `the Nisos Cylinder` | **il Cilindro Nisos** | `Cylinder` come nome di habitat si traduce: precedente «Cilindro Mordente» (L15), «habitat cilindrici» (3 nello staging) |
| `skyhooks` | **skyhook** (1) | invariato (3 occorrenze, anche al plurale) |
| `the Assembly` | **l'Assemblea** (1) | tradotto: 42 occorrenze di «Assemblea» nello staging |
| `our core planets` | **i nostri pianeti del Nucleo** | `the Core` → «il Nucleo» (decisione 21) |
| `cylinder habitats` | **habitat cilindrici** (2) | forma già in staging |

## 4. Lessico

| inglese | resa | nota |
|---|---|---|
| `ground-to-orbit laser batteries` | **batterie laser terra-orbita** | coppia di sostantivi con trattino, come in italiano tecnico |
| `surface-to-orbit nuclear missiles` | **missili nucleari superficie-orbita** | idem |
| `run a blockade` | **forzare un blocco** | «condurre un blocco» avrebbe invertito il senso: chi parla è chi lo attraversa |
| `smuggle more people out` | **portare più persone di contrabbando fuori** | «contrabbando» è il termine del corpus per gli esseri umani |
| `set an evacuation quota` | **fissare una quota di evacuazione** | |
| `with the naked eye` | **a occhio nudo** | |
| `Twelve million Avgi` | **Dodici milioni di Avgi** | il sorgente scrive in lettere e in lettere resta |
| `Less than one in six made it out alive` | **Meno di uno su sei ne è uscito vivo** | |
| `weighed down by the ground itself` | **oppresso dal suolo stesso** | «schiacciato dal peso» aggiungeva un'immagine che il testo non ha |
| `the homeworlds` | **i mondi d'origine** | |
| `those Aberrant` (disprezzo) | **quegli Aberrant** | il dimostrativo sprezzante si conserva |

## 5. Apici: 12 inglesi, 5 italiani

L'inglese contrae in nove unità (`I've`, `wouldn't`, `We'd`, `can't`, `aren't`, `We're`, `it's`, `don't`, `I'll`),
l'italiano elide in cinque (`All'inizio`, `l'assedio`, `l'Assemblea`, `d'origine`, `Com'è`). 12 contro 5 non è una
perdita: è la lingua (decisione 202). Il controllo confronta le coppie `(unità, conteggio)`.

## 6. Struttura

- **Ogni unità è una citazione intera**: `"…"`, 2 virgolette per unità, 44 in tutto. A differenza di
  `coalition news.txt` (L206–L211), dove la citazione si spezzava su più unità e il controllo era una distribuzione,
  qui il criterio è per unità e il `verify.py` verifica anche che ogni stringa **cominci e finisca** con le virgolette.
- **Zero tab**: nessun `MISSION_TEXT`, nessun separatore di paragrafo. Asserzione negativa scritta in entrambi gli
  script.
- **Punto finale dentro le virgolette**: riprodotto, come nel sorgente.

## 7. Avvertenza per i lotti successivi dello stesso file

Le righe **197–202** contengono unità di **una sola parola** (`"Caution. `, `"Warning. `, `"Advisement. `,
`"Diligence. `, `"Alert. `, `"Vigilance. `) che il gioco **concatena** con i messaggi delle righe 204–210: sono
frammenti, non citazioni, e la maiuscola e lo spazio finale fanno parte della stringa. Alla riga **177** compare
inoltre il dispositivo della domanda Avgi in forma esplicita (`…, question?`), che si riproduce come etichetta di
modalità della frase (decisione 167).

## 8. Lacune dichiarate

- **Nessuna lacuna `log`**: il lotto non ha righe `log` (0 `LOGBOOK`, asserito fra le assenze di tipo).
- **Nessun riferimento di dato**: le 22 unità sono testo; `NT` è vuoto per misura, non per abitudine, e il `check.py`
  lo scrive come asserzione (`[u['idx'] for u in units if u['kind'] != 'NEWS'] == []`).
