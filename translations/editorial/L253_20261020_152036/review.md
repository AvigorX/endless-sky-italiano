# review.md — L253 (`data/wanderer/wanderer jobs.txt`, righe 264–442)

Registro delle decisioni editoriali del **secondo lotto** del file dei Wanderer: quattro missioni, quattordici stringhe
distinte, tre formule di pagamento.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 8 | **copiato** | `New animal found on <planet>`, `Quarantine an invasive species` |
| `DESCRIPTION` | 8 | **tradotto** | la scheda del lavoro |
| `DIALOG` | 8 | **tradotto** | le battute alla consegna |

## 2. Le quattro missioni

| missione | inglese | resa |
|---|---|---|
| **Biologists** | `These <bunks> Wanderer biologists wish to get to <destination> with their <cargo> to study a recently discovered animal species. Payment will be <payment>.` | «Questi `<bunks>` **biologi** Wanderer vogliono arrivare a `<destination>` con il loro `<cargo>` per studiare una **specie animale scoperta di recente**. Il pagamento sarà `<payment>`.» |
| **Botanists** | `… botanists … a recently discovered plant species.` | «… **botanici** … una **specie vegetale** scoperta di recente.» |
| **Harvest** | `Bring these <bunks> Wanderers to <destination> to assist in the food harvest. Payment is <payment>.` | «Porta questi `<bunks>` Wanderer a `<destination>` per aiutare nella **raccolta del cibo**. Il pagamento è `<payment>`.» |
| **Invasive (animale)** | `… to <stopovers> with their <cargo> to contain an invasive animal species. Return the Wanderers to <origin> with the animals by <date> for a payment of <payment>.` | «… a `<stopovers>` con il loro `<cargo>` per contenere una **specie animale invasiva**. Riporta i Wanderer a `<origin>` **con gli animali** entro il `<date>` in cambio di un pagamento di `<payment>`.» |
| **Invasive (pianta)** | `… an invasive plant species … with the plants …` | «… una **specie vegetale invasiva** … **con le piante** …» |

Le due battute degli invasivi, che sono **singolari** e non copie:

> «I Wanderer escono in fretta dalla tua nave con la loro attrezzatura per contenere gli animali invasivi. Dopo circa **un'ora** tornano sulla tua nave con delle gabbie che sistemano nella stiva. Ora torna a `<origin>` per il pagamento.»

> «Dopo aver liberato gli animali, ciascuno dei `<bunks>` Wanderer ti ringrazia per averlo aiutato a riportare gli animali su `<planet>` e ti consegna `<payment>`.»

## 3. Le due schede «quasi uguali»

`invasive **animal** species` e `invasive **plant** species` sono **stringhe inglesi diverse**: non sono un gruppo di
copie, e non devono avere la stessa resa. Il `verify.py` lo asserisce in due punti:

- i testi inglesi **differiscono** (`animal` / `plant`);
- le rese italiane **differiscono** («specie animale invasiva con gli animali» / «specie vegetale invasiva con le piante»).

Un controllo basato solo su «quante rese per gruppo» non le avrebbe distinte.

## 4. Tre formule di pagamento, tre tempi

| inglese | resa | unità |
|---|---|---|
| `Payment will be <payment>.` | **«Il pagamento sarà `<payment>`.»** | 2, 5, 8, 11 |
| `Payment is <payment>.` | **«Il pagamento è `<payment>`.»** | 14, 17 |
| `for a payment of <payment>.` | **«in cambio di un pagamento di `<payment>`»** | 20, 24 |

La forma segue il **tempo verbale inglese**, non una preferenza: è la regola fissata in L252 per i Wanderer e qui è
applicata senza eccezioni.

## 5. Lessico

| inglese | resa | nota |
|---|---|---|
| `contain` (una specie invasiva) | **contenere** | è il verbo della quarantena |
| `cargo hold` | **stiva** | |
| `cages` | **gabbie** | |
| `each thank you` | **ciascuno … ti ringrazia** | il plurale inglese diventa singolo italiano |
| `You wish … the best of luck` | **«Fai gli auguri ai …»** | resa identica a L252, con il verbo |
| `collect your payment` | **riscuoti il pagamento** | |
| `<stopovers>` | **`<stopovers>`** | simbolo intero, **due volte**, senza articolo davanti |

## 6. Struttura e differenze fra le due lingue

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **0** | **1** (unità 21: `un'ora`) |
| `<planet stopovers>` | **assente** | **assente** (verificato in entrambe le lingue) |

L'unico apostrofo italiano nasce da un'elisione che l'inglese non ha (`an hour`), ed è dichiarato **per unità**.
