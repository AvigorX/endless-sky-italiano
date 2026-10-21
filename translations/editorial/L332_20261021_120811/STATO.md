# STATO — L332 (`data/human/south jobs.txt`, righe 15–347) — **TERMINALE, FILE INTERO**

`check.py` exit 0 (**16 controlli**), `verify.py` exit 0 (**12 controlli**), `state.py` `ESITO: OK`. Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L332_20261021_120811/` |
| righe | 15–347 (**tutto il file**) |
| unità | **40** = **14 `VALUE` + 14 `DESCRIPTION` + 8 `DIALOG` + 4 `CONVERSATION`** |
| contesti | **15** (`Pirate Occupation [0..2]`, `conversation:pirate occupation`, `Sketchy Cargo/Passenger`, `Delta V Shipment`, `Tarazed Shipyards/Systems Shipment`) |
| parole | **720 EN → 687 IT** (0,954) |
| tab / virgolette | **2** (133, 135) / **2** (solo la conversazione 131) |
| segnaposto | **66** in **8 forme** (`<planet>` 20, `<payment>` 18, `<destination>` 7, `<cargo>` 7, `<system>` 6, `<date>` 4, `<tons>`, `<fare>`) |
| invariante | **di FILE**: 40/40, prima 15, ultima 347 |
| `sha256[:16]` | **`3da37b24c5169ccc`** |

**Centotreesimo file completo** (**103** su 167). Residuo: **1.336 unità / 17.799 parole su 64 file**.

## Un rosso, ed era un **numero dichiarato a mano**

`verify.py` asseriva «52 segnaposto in totale»: la somma delle otto forme è **66** (20+18+7+7+6+4+2+2). Il totale è stato misurato e
corretto: **66**. Il resto del lotto era già corretto.

## I titoli dei lavori: tradotti, con una divergenza dichiarata

I 14 `VALUE` sono **titoli di lavoro visibili nel tabellone**, non nomi propri: «Delivery to <planet>», «Shipment to <planet>»,
«Passenger transport to <planet>», «Pirates occupying <system>». Il corpus è **spaccato**:

| stringa | copiata in inglese | tradotta |
|---|---|---|
| `Delivery to <planet>` | 14 | **13** |
| `Passenger transport to <planet>` | 3 | **12** |
| `Shipment to <planet>` | **20** | 0 |

Scelta: **tradurli tutti**, con le forme già in uso («Consegna a <planet>», «Trasporto passeggeri a <planet>») e due forme nuove
(«Spedizione a <planet>», «Pirati che occupano <system>»). La divergenza con le 20 copie di `Shipment to <planet>` è **dichiarata**: il
corpus aveva due politiche, e questo file ne adotta una sola.

## Limiti

Nessuna approvazione (40 `PENDING` invariate), nessun testo visto nel gioco, nessuna revisione umana.
