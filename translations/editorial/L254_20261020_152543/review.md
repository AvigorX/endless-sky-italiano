# review.md — L254 (`data/wanderer/wanderer jobs.txt`, righe 458–888)

Registro delle decisioni editoriali del **terzo lotto** del file dei Wanderer: diciotto nomi di lavoro, un blocco `phrase`,
due schede generiche ripetute otto e quattro volte.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 18 | **copiato** | `Delivery to <planet>`, `Rush delivery to <planet>`, `Captured Unfettered to <planet>` |
| `DESCRIPTION` | 18 | **tradotto** | la scheda del lavoro |
| `DIALOG` | 4 | **tradotto** | le battute alla consegna |
| `TEXT` | 1 | **tradotto** | il blocco `phrase:wanderer cargo delivery payment` |

## 2. Il `TEXT` e il blocco `phrase`

> `You drop off your cargo of <commodity>. The Wanderers thank you and you collect your payment of <payment>.`
> «Scarichi il tuo carico di `<commodity>`. I Wanderer ti ringraziano e incassi il pagamento di `<payment>`.»

Il contesto di questa unità è **`phrase:wanderer cargo delivery payment`**, non una missione: è un **blocco di frase** che il
gioco compone quando consegni un carico. Va quindi:

- **tradotto** (è prosa, non un nome);
- verificato come **frase intera** (inizia con il verbo, finisce con il punto) — un frammento spezzerebbe la composizione;
- tenuto **separato** dagli altri tipi nel `check.py`, perché il suo contesto non è `mission:` e un controllo che assumesse
  «tutto è missione» lo salterebbe senza dirlo.

## 3. Le schede generiche e la forma dominante

| inglese | resa | occorrenze nel corpus | copie nel lotto |
|---|---|---|---|
| `Deliver <cargo> to <destination>. Payment is <payment>.` | «Consegna `<cargo>` su `<destination>`. Il pagamento è `<payment>`.» | **39** | **8** |
| `Deliver <cargo> to <destination> by <date>. Payment is <payment>.` | «Consegna `<cargo>` su `<destination>` entro il `<date>`. Il pagamento è `<payment>`.» | **17** | **4** |
| `Deliver <cargo> to the Kor Efreti on <destination>. Payment is <payment>.` | «Consegna `<cargo>` ai Kor Efreti su `<destination>`. Il pagamento è `<payment>`.» | **0** (nuova) | **3** |

Per le prime due il controllo **calcola a runtime** quale resa è la più frequente nel corpus e la confronta con quella usata
qui: nessuna costante scritta a mano, e se il corpus cambia il test lo segnala.

## 4. I nomi di lavoro restano inglesi (divergenza dichiarata)

| inglese | resa qui | storia nel corpus |
|---|---|---|
| `Delivery to <planet>` | **copiato** | 13 «Consegna a `<planet>`», 6 lasciati inglesi |
| `Rush delivery to <planet>` | **copiato** | 13 inglesi, 9 «Consegna urgente a `<planet>`», 2 «su» |
| `Bulk delivery to <planet>` | **copiato** | 3 inglesi, 4 «Consegna all'ingrosso a `<planet>`» |

Il `VALUE` è il **nome del lavoro** che il gioco mostra nella bacheca: il corpus ha una storia **divergente** (lotti antichi
lo traducevano, i recenti lo copiano). Questo lotto applica la regola dei lotti recenti — **copia** — e dichiara la
divergenza invece di mescolare le due politiche nelle stesse 18 unità. Unificarle è un lavoro separato, da fare con una
ricerca globale e un test.

## 5. Lessico

| inglese | resa | nota |
|---|---|---|
| `captured Unfettered soldiers` | **soldati Slegati catturati** | `Unfettered` sopravvive **solo** nel `VALUE` |
| `suitable facilities to transport them` | **strutture adatte al loro trasporto** | |
| `the local governor` | **il governatore locale** | |
| `the capital city` | **la capitale** | |
| `They expect a comfortable journey` | **«Si aspetta un viaggio confortevole»** | `they` singolare: si evita il pronome di genere |
| `terraforming experts` | **esperti di terraformazione** | |
| `Kor Efret world` / `Korath` | **mondo Kor Efret** / **Korath** | nomi invariati |
| `containers of some sort` | **una specie di contenitori** | |
| `plant elsewhere` | **perché le piantino altrove** | |
| `to contain the invasive plant` | **per contenere la pianta invasiva** | variante **pianta** della gemella animale di L253 |
| `for assisting them in keeping the plants on <planet>` | **per averlo aiutato a tenere le piante su `<planet>`** | `each … thank you` → singolare italiano, come in L253 |

## 6. Struttura e differenze fra le due lingue

| cosa | inglese | italiano |
|---|---|---|
| tab | **0** | **0** |
| virgolette | **0** | **0** |
| apici | **3** (unità 29: `you'll`; unità 41: `it's`, `they've`) | **1** (unità 1: `un'ora`) |
| `Unfettered` | 2 (uno nel `VALUE`, uno nella prosa) | **1**, solo nel `VALUE` |

L'italiano **non** usa il futuro contratto (`you'll`, `it's`, `they've`): tre apici inglesi diventano zero, e l'unico
apostrofo italiano nasce da un'elisione estranea all'inglese (`an hour` → «un'ora»). La differenza è **elencata per unità**.
