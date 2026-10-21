# REPORT — L332 (`south jobs.txt` 15–347) — file chiuso 40/40

`check.py` **16 controlli, FAIL 0**; `verify.py` **12 controlli, FAIL 0**; `state.db` non toccato.

| | EN | IT |
|---|---|---|
| 40 unità (14 `VALUE` + 14 `DESCRIPTION` + 8 `DIALOG` + 4 `CONVERSATION`) | 720 parole | **687** (0,954) |
| segnaposto | 66 in 8 forme | **66**, identici per unità |
| tab · virgolette | 2 · 2 | 2 · 2 |

## Che cosa racconta il file

| contesto | unità | contenuto |
|---|---|---|
| `Pirate Occupation [0..2]` | 6 | tre lavori di **difesa** contro i pirati, in scala (**piccola banda → banda → grande banda**), sempre con «il governo locale ha chiesto aiuto» |
| `conversation:pirate occupation` | 4 | la **chiamata** nello spazioporto («`<destination>` è occupato da una flotta pirata!»), due scelte e l'imbarco nella **milizia** |
| `Sketchy Cargo [0..1]` | 8 | consegna di **casse senza etichetta** in un magazzino abbandonato: «hai la sensazione di essere osservato»; paga «un uomo avvolto in un mantello» |
| `Sketchy Passenger [0..1]` | 8 | passeggeri che **sussurrano**, chiedono di atterrare **lontano dal centro** e scappano «a notevole velocità» |
| `Delta V Shipment [0..1]` | 4 | missili e motori, **Bordo Meridionale** |
| `Tarazed Shipyards Shipment [0..2]` | 6 | «uno dei più grandi cantieri navali del Sud» |
| `Tarazed Systems Shipment [0..1]` | 4 | «stimata produttrice e progettista di equipaggiamenti» |

## Scelte

- **Titoli tradotti**: «Consegna a <planet>», «Spedizione a <planet>», «Trasporto passeggeri a <planet>», «Pirati che occupano <system>».
- **`Southern Rim` → «Bordo Meridionale»** (il corpus usa «Bordo» per `Rim`).
- **`<tons>`, `<fare>`, `<cargo>`, `<payment>`** restano segnaposto: non diventano «tonnellate», «tariffa», «carico», «pagamento».
- **Le coppie `[0]` e `[1]`** hanno lo stesso inglese e quindi **la stessa resa** (verificato per le quattro coppie di `DIALOG`).
- **Le due scelte della conversazione** restano fra parentesi, con la tab iniziale: «(Non unirti allo scontro.)» / «(Unisciti alla flotta di
  difesa.)».

## Non verificato

Nessuna approvazione, nessun testo visto nel gioco, nessuna revisione umana. La divergenza sui titoli (`Shipment to <planet>` copiato 20
volte altrove) è **dichiarata**.
