# review.md — L269 (`data/human/engines.txt`, righe 342–487)

Registro delle decisioni editoriali del **terzo lotto** dei motori umani: la linea **al plasma** della Delta V Corporation.

## 1. Il carattere del testo

Queste schede sono **pubblicità**. La Delta V vende il plasma con una promessa e un'avvertenza: più potenza a parità di
dimensione, meno efficienza, più calore. E ci mette sopra dei **disegni sulle casse** — un levriero, un tirannosauro, un
roditore. Appiattire il tono («propulsore di piccole dimensioni») avrebbe tradito il testo; la resa lo conserva.

## 2. Scelte

| inglese | resa |
|---|---|
| `the smallest of the plasma propulsion systems` | **il più piccolo dei sistemi a propulsione al plasma** |
| `very light fighters and interceptors` | **caccia leggerissimi e intercettori** |
| `a crate decorated with a stylized cartoon of a running greyhound` | **una cassa decorata con un disegno stilizzato di un levriero in corsa** |
| `produce a significant amount of force` | **producono una notevole quantità di forza** |
| `your ship may need extra cooling systems in order to handle them` | **la tua nave, però, potrebbe aver bisogno di sistemi di raffreddamento extra per sopportarli** |
| `anything short of a full-fledged nuclear reactor` | **priva di un vero e proprio reattore nucleare** |
| `the thrust it generates is impressive` | **la spinta che genera è impressionante** |
| `a grinning Tyrannosaurus Rex with an improbable number of teeth` | **un Tyrannosaurus Rex ghignante, con un numero improbabile di denti** |
| `only a handful of ships are large enough to require an engine of this size... or to have the capacity for one` | **solo una manciata di navi è abbastanza grande da aver bisogno di un motore di questa dimensione... o da avere la capacità di ospitarne uno** |
| `a very highly caffeinated rodent` | **un roditore fin troppo carico di caffeina** |
| `the Greyhound class plasma propulsion systems are Delta V's most popular product` | **i sistemi a propulsione al plasma di classe Greyhound sono il prodotto più venduto della Delta V** |
| `all but the largest warships` | **tutte le navi da guerra tranne le più grandi** |
| `considerably more compact than the ion propulsion systems produced by the Syndicate` | **considerevolmente più compatti dei sistemi a propulsione ionica prodotti dal Sindacato** |
| `turn as quickly as a fighter` | **girare con la rapidità di un caccia** |

`... or to have the capacity for one` conserva i **tre punti** del sorgente: l'ironia sta nella pausa, non nella frase.

## 3. La nota del plasma (×8)

> «I motori al plasma sono un po' più potenti dei motori ionici della stessa dimensione, ma sono meno efficienti dal punto di
> vista energetico e producono più calore.»

Una sola resa per **otto** unità (2, 4, 6, 8, 10, 12, 14, 16): è l'informazione di **compromesso** che il giocatore deve
poter confrontare fra tutti i modelli, quindi deve essere identica parola per parola. Il `check.py` la verifica come insieme
con un solo elemento; il `verify.py` la riverifica sui tab.

## 4. Nomi propri e nomi comuni

| nome | trattamento |
|---|---|
| `Delta V Corporation`, `Delta V` | **invariato** |
| `Greyhound`, `Impala`, `Orca`, `Tyrant`, `Chipmunk` (classi) | **invariati** dove l'inglese li nomina |
| `greyhound` (il cane sulla cassa) | **levriero** |
| `Tyrannosaurus Rex` (la figura sulla cassa) | **invariato** (nome scientifico) |
| `rodent` (il disegno) | **roditore** |
| `the Syndicate` | **il Sindacato** |

La distinzione non è cosmetica: `Greyhound` nell'unità 3 **non c'è** in inglese — c'è il cane. Il primo giro di controlli li
confondeva (`1 FAIL`), ed è stato corretto **misurando l'inglese**, non allentando l'asserzione.

## 5. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **8** (unità pari) | **8**, primo carattere |
| virgolette | **0** | **0** |
| apici | **1** (`Delta V's`, unità 13) | **11** (`un po'` ×8, `L'enorme`, `l'immagine`, `un'ampia`) |
| segnaposto | **0** | **0** |

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file è a 44/61**: L270 chiude `engines.txt` con le ultime **17 unità** (Orca steering, Tyrant steering, Capybara e
  AR120 reverse, la serie **Atomica** A120–A865).
