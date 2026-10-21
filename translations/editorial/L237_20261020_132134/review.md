# review.md — L237 (`data/avgi/avgi news.txt`, righe 369–399)

Registro delle decisioni editoriali del **quinto lotto** di `avgi news.txt`: otto fisici e sei astronomi, testo tecnico e
una battuta sul modo in cui tutti disegnano le mappe.

## 1. Le etichette

| inglese | resa | nota |
|---|---|---|
| `Gratitude.` | **Gratitudine.** | già in L236 |
| `Frustation.` (×2, **refuso del sorgente**) | **Frustrazione.** | il refuso non si trasporta |
| `Pride.` | **Orgoglio.** | |
| `Amusement.` | **Divertimento.** | in L236 era in coda e minuscolo («divertimento.»): stessa parola, posizione diversa |
| `Curiosity.` (×2) | **Curiosità.** | già in L233 |
| `Information.` | **Informazione.** | |
| `Amazement.` | **Stupore.** | distinto da `Wonder` → «Meraviglia» |
| `Instructive.` | **Istruttivo.** | |
| `Inquisitive.` | **Curioso.** | aggettivo, non sostantivo: l'inglese distingue `Curiosity` da `Inquisitive` e così l'italiano |
| `Tutelage.` | **Insegnamento.** | |
| `Frustration.` | **Frustrazione.** | scritta correttamente nel sorgente, resa identica alle due con refuso |
| `Annoyance.` | **Fastidio.** | già in L236 |

## 2. Il lessico tecnico fissato in questo lotto

| inglese | resa | nota |
|---|---|---|
| `hyperdrive` (×2) | **iperpropulsore** | forma dominante del corpus (35 contro 18 «hyperdrive») e voce di glossario |
| `wormhole` | **wormhole** (invariato) | 57 occorrenze nel corpus, termine tecnico |
| `energy shields` | **scudi energetici** | |
| `solar cell junction` | **giunzione per celle solari** | |
| `faster than light drive` | **motore più veloce della luce** | |
| `atmospheric drag` | **resistenza aerodinamica** | |
| `shed vortices` | **vortici di scia** | termine aerodinamico: i vortici che si staccano dalla scia |
| `destructively interfere` | **interferire in modo distruttivo** | interferenza costruttiva/distruttiva: registro fisico, non «farsi male» |
| `memory diamond` | **diamante di memoria** | oggetto tecnologico; cfr. «fogli di memoria» del corpus |
| `reflection nebula` | **nebulosa a riflessione** | |
| `neutron stars` | **stelle di neutroni** | |
| `supernovae` | **supernove** | plurale italiano corretto |
| `molecular cloud` | **nube molecolare** | |
| `hydrostatic equilibrium` | **equilibrio idrostatico** | |
| `stellar nursery` | **vivaio stellare** | |
| `starways` | **vie stellari** | il reticolo di collegamenti fra sistemi; nessun precedente nello staging |
| `order of magnitude` | **ordine di grandezza** | |
| `atomic bond strength` | **forza del legame atomico** | |

## 3. Il gergo galattico: tradotto, e dichiarato

L'unità 398 propone «coordinate polari» al posto dei punti cardinali e cita due direzioni galattiche:

| inglese | resa | perché |
|---|---|---|
| `'North'` / `'West'` | **'Nord'** / **'Ovest'** | punti cardinali veri: si traducono |
| `'spinward'` | **'senso di rotazione'** | nessun precedente nello staging; «spinward» non è una parola italiana e lasciarla in inglese dentro una battuta che **propone nomi migliori** la renderebbe incomprensibile |
| `'rimward'` | **'verso il bordo'** | idem, simmetrico |

Il costo è che le due etichette sono più lunghe dell'inglese; il beneficio è che l'argomento della battuta (i nomi delle
coordinate) resta leggibile. La scelta è reversibile e localizzata in una unità.

## 4. Refuso e normalizzazione

1. **`Frustation.`** (370, 371): refuso del sorgente per `Frustration.`. Si traduce il senso («Frustrazione.») e il
   refuso **non** si replica: è una svista di battitura, non una variante (cfr. decisione 183: si riproducono le
   varianti, non gli errori di digitazione).
2. **`the Twilight nebula`** (395, minuscolo) contro `The Twilight Nebula` (394, 396). Il nome dell'oggetto va con la
   maiuscola: normalizzato, con la divergenza **IT 3 / EN 2** asserita nel `verify.py`. È l'unico caso del lotto in cui
   l'italiano non riproduce la grafia inglese, e sta qui scritto perché non sembri una svista.

## 5. I nomi propri

`Twilight Nebula`, `Stream` (ammasso stellare), `Avgi`, `Aberrant` restano invariati. `Stream` è un toponimo e non
diventa «Corrente»: nel gioco è il nome di un ammasso.

## 6. Numeri, unità e misure

- `a thousand light years` → **«quasi mille anni luce»** (in lettere, come l'inglese).
- `millions of years` → **«milioni di anni»**; `Eighty years ago` → **«Ottant'anni fa»** (in lettere).
- `half the ships in the sky` → **«metà delle navi in volo»**.
- `four years` non compare; nessuna cifra in questo lotto, quindi il controllo sulle convenzioni numeriche si riduce
  all'assenza di forme inglesi (`1,000`).

## 7. Struttura e assenze

- **Zero tab**, **zero segnaposto**, **zero righe `log`**, **`NT` vuoto** per misura: quattro asserzioni negative scritte.
- **Nessun gruppo di inglese identico** dentro la finestra: le quattordici stringhe sono tutte diverse, quindi il
  controllo dei duplicati si riduce a `0 gruppi` (scritto come asserzione, non omesso).
- La finestra **non è continua**: le unità dei fisici finiscono alla 376 e quelle degli astronomi cominciano alla 394;
  le righe 377–393 non producono unità. Non è un buco di copertura.
