# review.md — L251 (`data/human/syndicate jobs.txt`, righe 701–814) — LOTTO TERMINALE

Registro delle decisioni editoriali dell'**ultimo lotto** di `syndicate jobs.txt`: tre spedizioni identiche e due trasporti
di hovercraft.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `VALUE` | 5 | **copiato** | `Shipment to <planet>`, `Transport racer to <planet>` |
| `DESCRIPTION` | 5 | **tradotto** | la scheda del lavoro |
| `DIALOG` | 2 | **tradotto** | la battuta alla consegna |

I tre `VALUE` distinti sono nomi di lavoro; `Shipment to <planet>` contiene un **segnaposto** ed è comunque un dato: si
copia, non si adatta.

## 2. Le rese

| unità | inglese | resa |
|---|---|---|
| 2, 4, 6 | `Deliver <cargo> to <destination>, the home of Megaparsec Inc., a shipyard known for their lightweight designs.` | «Consegna `<cargo>` su `<destination>`, sede di Megaparsec Inc., un cantiere noto per i suoi progetti leggeri. Il pagamento è `<payment>`.» |
| 8 | `Deliver a pilot and their hovercraft to <destination> to attend a race by <date> for <payment>.` | «Consegna un pilota e il suo hovercraft su `<destination>` per partecipare a una gara entro il `<date>` in cambio di `<payment>`.» |
| 9 | `You drop off the pilot with their hovercraft and collect your payment of <payment>.` | «Scarichi il pilota con il suo hovercraft e incassi il pagamento di `<payment>`.» |
| 11 | `Deliver this <passengers>-member racing team and their set of <cargo> to <destination>…` | «Consegna questa squadra di `<passengers>` membri e il loro carico di `<cargo>` su `<destination>` per partecipare a una gara entro il `<date>` in cambio di `<payment>`.» |
| 12 | `You drop off the racing team with their hovercraft and collect your payment of <payment>.` | «Scarichi la squadra con i suoi hovercraft e incassi il pagamento di `<payment>`.» |

## 3. Le scelte che non sono ovvie

| punto | decisione | perché |
|---|---|---|
| `their hovercraft` (pilota) | **«il suo hovercraft»** | singolare: il pilota è uno |
| `their hovercraft` (squadra) | **«i suoi hovercraft»** | plurale: la squadra ne ha più d'uno |
| `hovercraft` | **invariato** | prestito acclimatato in italiano, nessun traducente migliore |
| `a shipyard known for their lightweight designs` | **«un cantiere noto per i suoi progetti leggeri»** | `their` riferito al cantiere: in italiano «i suoi» |
| `the home of Megaparsec Inc.` | **«sede di Megaparsec Inc.»** | forma già usata in L250 per `Syndicated Systems` |
| `their set of <cargo>` | **«il loro carico di `<cargo>`** | «set» è un anglicismo; «carico» dice la stessa cosa in italiano |
| `<passengers>-member racing team` | **«questa squadra di `<passengers>` membri»** | il segnaposto resta **prima** del nome che lo misura, come in inglese |
| `to attend a race` | **«per partecipare a una gara»** | |
| `by <date> … for <payment>` | **«entro il `<date>` in cambio di `<payment>`»** | forma fissa dei lavori a tempo |

## 4. Struttura e assenze

| cosa | inglese | italiano |
|---|---|---|
| tab | 0 | 0 |
| virgolette | 0 | 0 |
| apici | 0 | 0 |

Tre **asserzioni negative** scritte, non tre controlli saltati: `sum(...) == 0` in entrambe le lingue.

## 5. Il file chiuso

`data/human/syndicate jobs.txt` è completo in staging: **94 unità** in cinque lotti (L247–L251), **94 righe distinte**, dalla
19 alla 814. Il `verify.py` verifica che le righe dei cinque `translation.json` siano **esattamente** quelle del database.

## 6. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: le 94 unità sono `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il resto della campagna**: 2.745 unità su 96 file, il prossimo è `data/wanderer/wanderer jobs.txt` (92 unità).
