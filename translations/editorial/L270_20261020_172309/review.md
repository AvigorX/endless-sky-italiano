# review.md — L270 (`data/human/engines.txt`, righe 488–717)

Registro delle decisioni editoriali dell'**ultimo lotto** dei motori umani: la serie **Atomica** della Deep Sky, due
propulsori inversi, le sterzate Tyrant e Orca.

## 1. Il carattere del testo

La serie Atomica è venduta come **status**, non come prestazione: «l'invidia di ogni pilota della galassia», «il capolavoro
della Deep Sky», «un set può costare più della nave». Il testo alterna questo tono pubblicitario a un'**avvertenza tecnica**
ricorrente: energia e raffreddamento «possono facilmente annullare il vantaggio» delle dimensioni ridotte.

Conservarli entrambi era il punto: la resa non ha appiattito né la vanità né il costo.

## 2. Scelte

| inglese | resa |
|---|---|
| `the most powerful engine that will fit into your ship` | **il motore più potente che possa entrare nella tua nave** |
| `have plenty of money to burn` | **hai denaro da buttare** |
| `can easily offset the benefit of their small size` | **possono facilmente annullare il vantaggio delle loro dimensioni ridotte** |
| `have been in production for centuries, but remain a niche product` | **sono in produzione da secoli, ma restano un prodotto di nicchia** |
| `powerful enough to move any but the largest of ships` | **abbastanza potente da muovere qualsiasi nave tranne le più grandi** |
| `such performance comes at an exorbitant price` | **prestazioni simili hanno un prezzo esorbitante** |
| `you will be the envy of every pilot in the galaxy` | **sarai l'invidia di ogni pilota della galassia** |
| `No other form of propulsion that humanity has discovered` | **nessun'altra forma di propulsione scoperta dall'umanità** |
| `the most powerful engine sold in human space` | **il motore più potente venduto nello spazio umano** |
| `you may need to upgrade your ship's power and cooling systems to handle it` | **potrebbe però servirti potenziare gli impianti di energia e di raffreddamento della nave per reggere la spinta** |
| `a popular choice for high-end starships` | **una scelta popolare per le astronavi di fascia alta** |
| `if you have exhausted all your other options` | **se hai esaurito ogni altra possibilità** |
| `bounty hunters and other captains` | **i cacciatori di taglie e gli altri capitani** |
| `swapping the existing engines with a set of atomics can free up a considerable amount of space` | **sostituire i motori esistenti con un set atomico può liberare parecchio spazio** |
| `Deep Sky's crowning achievement` | **il capolavoro della Deep Sky** |
| `there are few captains who do not dream of one day installing a set of them` | **pochi capitani non sognano di installarne un set un giorno** |
| `pull fancy tricks that most are not capable of duplicating` | **eseguire acrobazie che quasi nessuno è in grado di replicare** |

## 3. I propulsori inversi: due schede, una nota

`Capybara` (unità 4-5) e `AR120` (unità 16-17) hanno **la stessa nota di montaggio** dell'X1100 di L268: «Poiché un propulsore
inverso deve essere rivolto in avanti, va installato nella sezione delle armi della nave anziché in quella dei motori.» È
un'informazione **funzionale** — senza, il giocatore non riesce a montarlo — e la ripetizione nel sorgente è voluta: la nota
sta con **ogni** oggetto, non in un manuale.

## 4. Numeri e nomi

| nome | trattamento |
|---|---|
| `Deep Sky` | **invariato** (ditta umana) |
| `A120`, `A250`, `A370`, `A520`, `A860`, `A125`, `A255`, `A375`, `A525`, `A865` | **invariati**, e nei **contesti** (che non si traducono) |
| `Capybara`, `AR120`, `Tyrant`, `Orca` | **invariati** |
| `Atomic` | **«atomico/a»**, concordato: *propulsori atomici*, *motori atomici*, *sterzata*, *set atomico* |

Un solo numero — **A860** — compare **nel testo** inglese, e resta in quello italiano. Gli altri nove vivono nel contesto:
il primo giro di controlli li cercava nel testo e falliva, il che è la prova che l'asserzione era sbagliata, non la resa.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **4** (unità 1, 3, 5, 17) | **4**, primo carattere |
| virgolette | **0** | **0** |
| apici | **7** (`you're`, `Deep Sky's` ×4, `ship's`, e uno in più) | **8** (unità 9 con tre: `l'invidia`, `Nessun'altra`, `dall'umanità`) |
| segnaposto | **0** | **0** |

## 6. Chiusura del file

`data/human/engines.txt` è **61/61** in staging: quattro lotti (L267 12, L268 15, L269 17, L270 17), righe 27–717, tutte
`PENDING`.

Cosa **non** significa: non è approvato, non è stato visto nel gioco, non è stato revisionato da una persona. Significa che
in staging **non manca nessuna unità** del file, e che `verify.py` lo dimostra sommando i quattro lotti e confrontando le
righe.
