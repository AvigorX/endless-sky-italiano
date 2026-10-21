# review.md — L252 (`data/wanderer/wanderer jobs.txt`, righe 15–261)

Registro delle decisioni editoriali del **primo lotto** del file dei Wanderer: cinque lavori, dodici gruppi di testo
ripetuto, nessun segno tipografico da conservare.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 10 | **copiato** | `Wanderer workers to <planet>`, `Spike in pollution on <planet>` |
| `DESCRIPTION` | 10 | **tradotto** | la scheda del lavoro |
| `DIALOG` | 6 | **tradotto** | la battuta alla consegna |

## 2. Le cinque missioni

| missione | inglese | resa |
|---|---|---|
| **Workers** | `These <bunks> Wanderer workers require transportation to <destination>. They will pay you <payment> to take them there.` | «Questi `<bunks>` lavoratori Wanderer hanno bisogno di un trasporto fino a `<destination>`. Ti pagheranno `<payment>` per portarli fin là.» |
| **Farmers** | `… <bunks> Wanderer farmers …` | «Questi `<bunks>` **agricoltori** Wanderer…» |
| **Younglings** | `… are looking for transport to <destination> to learn more about the Wanderer terraforming process. The adult with them will pay you <payment>.` | «Questi `<bunks>` piccoli Wanderer cercano un trasporto fino a `<destination>` per saperne di più sul **processo di terraformazione** dei Wanderer. L'adulto che li accompagna ti pagherà `<payment>`.» |
| **Scientists (Pollution)** | `… with their <cargo> by <date> to investigate a strange spike in atmospheric pollutants. Payment will be <payment>.` | «… con il loro `<cargo>` entro il `<date>` per indagare su uno strano **picco di inquinanti atmosferici**. Il pagamento sarà `<payment>`.» |
| **Scientists (Phenomenon)** | `… to observe a rare natural phenomenon.` | «… per osservare un **raro fenomeno naturale**.» |

La battuta comune degli scienziati:

> `You wish the scientists the best of luck on <planet> as they carry their scientific equipment off of your ship and hand you your payment of <payment>.`
> «**Fai gli auguri** agli scienziati su `<planet>` mentre portano fuori la loro attrezzatura scientifica e ti consegnano il pagamento di `<payment>`.»

## 3. La ripetizione, contata

| gruppo | copie |
|---|---|
| `Wanderer workers to <planet>` (e la sua scheda) | 2 + 2 |
| `Wanderer farmers to <planet>` (e la sua scheda) | 2 + 2 |
| `Wanderer younglings to <planet>`, scheda, battuta | 2 + 2 + 2 |
| `Spike in pollution on <planet>`, scheda, battuta | 2 + 2 + 2 |
| `Natural phenomenon on <planet>`, scheda, battuta | 2 + 2 + 2 |

In tutto **12 gruppi**: 11 con due copie e **1 con quattro** (la battuta degli scienziati, che serve due missioni × due
contesti). Una resa per gruppo, e la **distribuzione delle molteplicità è asserita** (`[2] × 11 + [4]`).

## 4. `Wanderer`: nome invariato

Il corpus alterna due plurali: «i **Wanderer**» (315 occorrenze) e «i **Wanderers**» (290). Vince la forma **invariata** —
più frequente e più semplice — e il `verify.py` asserisce che `Wanderers` **non compaia** nella traduzione.

Nomi propri invariati: `Wanderer`, e i nomi di pianeta che stanno nei segnaposto.

## 5. «Payment will be» e la scelta del lessico

| inglese | resa scelta | occorrenze nel corpus |
|---|---|---|
| `Payment will be <payment>.` | **«Il pagamento sarà `<payment>`.»** | la forma «compenso» e quella «pagamento» sono 3 e 3: **pareggio** |
| `Payment is <payment>.` | «Il pagamento è `<payment>`.» | 56 |

A parità di occorrenze si sceglie la forma **coerente col resto del file** («pagamento»), e la divergenza con «compenso»
è **dichiarata** qui: unificarle è un lavoro separato, da fare con una ricerca globale e un test.

## 6. Struttura e differenze fra le due lingue

| cosa | inglese | italiano |
|---|---|---|
| tab | 0 | 0 |
| virgolette | 0 | 0 |
| apici | **0** | **4** (unità 10, 11, 13, 14: `L'adulto`, `dall'altra parte`) |

L'inglese non usa **nessun** apostrofo; l'italiano ne ha quattro, tutti elisioni. La differenza è elencata **per unità**.
