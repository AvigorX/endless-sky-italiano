# review.md — L311 (`data/bunrodea/bunrodea outfits.txt`, righe 25–130)

Registro delle decisioni editoriali del primo lotto Bunrodea: **relay di scudi** e **fabbricatori di naniti**.

## 1. Il popolo che ottimizza

I Bunrodea non costruiscono il generatore di scudi **più potente**: costruiscono quello **più efficiente**. La scheda di apertura lo
dice senza giri di parole —

> «un generatore di scudi di pari dimensioni di un'altra fazione potrebbe fornire più generazione di scudi, ma i relay Bunrodea
> offrono una quantità modesta di generazione di scudi con pochissima energia»

— e la riga 69 trasforma questa filosofia in **politica interna**: i **capitani militari** e i **capitani mercantili** litigano
sullo stesso trade-off. La resa conserva il **conflitto** («fosse uno scambio da sciocchi» / «si potesse consumare meno energia»)
perché è il motivo per cui i relay sono **personalizzabili**.

## 2. Lo scambio, in due direzioni

Le quattro schede singole sono **due coppie di opposti**, e la resa le rende **speculari**:

| | guadagni | perdi |
|---|---|---|
| **booster** | forza di generazione degli scudi | efficienza energetica |
| **limiter** | efficienza energetica | forza della generazione di scudi |
| **enhancer** | forza della riparazione dello scafo | efficienza energetica |
| **limiter** (naniti) | efficienza **energetica e termica** | forza della riparazione |

L'unica **asimmetria reale** è nei limitatori dei naniti: aggiungono l'**efficienza termica**, che i limitatori dei relay non
hanno. La resa la conserva (il test verifica «energetica e termica»).

## 3. `booster` / `enhancer` / `limiter`: tre nomi, tre rese

| inglese | resa | perché |
|---|---|---|
| `booster` | **potenziatore** | il termine del corpus per i relay |
| `enhancer` | **intensificatore** | **distinto** da booster: due componenti diversi non possono avere lo stesso nome |
| `limiter` | **limitatore** | dritto, coerente |

Il rischio era usare «potenziatore» per entrambi: la riga 7 e la riga 1 sarebbero diventate **indistinguibili** in italiano
mentre in inglese sono **due oggetti diversi**.

## 4. I nomi degli oggetti restano in inglese

`Shield Relay Booster`, `Small Shield Relay`, `Nanite Enhancer`, `Small Nanite Fabricator`… **non si traducono**: sono le
**etichette dell'emporio**, e nel corpus le navi e gli equipaggiamenti si comportano così (L123: «La Lionheart Aerie è una
portatrice leggera»). Il test verifica che **ogni nome presente nell'inglese compaia identico** nell'italiano.

## 5. La nota degli upgrade: famiglia con variante

| unità | finale | resa |
|---|---|---|
| 54, 70 | `though.` | «…, **però**.» |
| 114 | `though.` | «…, **però**.» |
| 130 | `however.` | «…, **tuttavia**.» |

L'avverbio resta **in fondo**, dove sta nell'inglese: la **stessa frase ripetuta** deve restare ripetuta, e la **variante** deve
restare una variante — non due frasi diverse.

## 6. I naniti vengono dai Korath

La riga 129 è **lore**: i fabbricatori nascono dal **contatto precoce** con i Korath, e in particolare dai **microbot che camminano
sullo scafo** dei `Korath System Core`, che permettevano di riparare **senza spazioporto**. La resa:

> «I microbi che camminano sullo scafo dei Korath System Core permettevano alle navi Korath di effettuare riparazioni senza bisogno
> di uno spazioporto, una caratteristica che i Bunrodea apprezzavano per le proprie navi esploratrici.»

`Korath System Core` resta **invariato** (è un nome di equipaggiamento Korath); «microbot» diventa «microbi» **per scelta**, perché
il testo li descrive come **esseri che percorrono lo scafo** e il registro della scheda è **descrittivo**, non tecnico.

## 7. Scelte di resa

| inglese | resa |
|---|---|
| `modify its effectiveness` | **modificarne l'efficacia** |
| `at the cost of reduced energy efficiency` | **al costo di una minore efficienza energetica** |
| `impressively efficient` | **di un'efficienza impressionante** |
| `a modest amount of shield generation for only a small amount of energy` | **una quantità modesta di generazione di scudi con pochissima energia** |
| `a foolish trade` | **uno scambio da sciocchi** |
| `looking to get the most out of their reactors` | **che volevano trarre il massimo dai propri reattori** |
| `customized to the owner's liking using external components` | **personalizzare a piacimento del proprietario con componenti esterni** |
| `hull repair` | **riparazione dello scafo** |
| `energy and heat efficiency` | **efficienza energetica e termica** |
| `a steady stream of nanites` | **un flusso costante di naniti** |
| `travel across the hull of the ship` | **percorrono lo scafo della nave** |
| `was spurred on by early contact` | **fu stimolata dai primi contatti** |
| `hull-walking microbots` | **i microbi che camminano sullo scafo** |
| `a trait that the Bunrodea favored` | **una caratteristica che i Bunrodea apprezzavano** |
| `scout vessels` | **navi esploratrici** |

## 8. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **4** (54, 70, 114, 130) | **4** |
| virgolette | **0** | **0** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **1** (riga 69) | **9** |

## 9. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; **nessuna revisione umana**.
- **Il file non è finito**: **12/33**; restano **21 unità / 772 parole**.
- **Prossimo lotto (L312)**: righe **135–236** — **12 unità** (**1 `VALUE`** `Solar Batteries` da copiare + **11 `DESCRIPTION`**),
  **445 parole**, **7 contesti**, **4 tab** (160, 204, 220, 236), **2 virgolette** (una coppia, riga 235), **1 apice** (219).
  È il lotto dei **reattori**: batterie solari, celle solari, overclocker e limiter dei reattori, e **tre reattori** (`Quark`,
  `Electroweak`, `Dark`) ognuno con la **stessa nota degli upgrade** — una **famiglia di tre**, non di due.
