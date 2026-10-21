# STATO — L319 (`data/korath/korath weapons.txt`, righe 615–1222)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 39/39 (100%)**, **trentaquattresimo file interamente tradotto** (**93** su
167 nel progetto). `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0 (`ESITO: OK`,
8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L319_20261020_221933/` |
| file | `data/korath/korath weapons.txt` (**39/39 unità · 1.089 parole · righe 53–1222**) |
| righe | 615–1222 |
| unità | **22** — **20 `DESCRIPTION` + 2 `VALUE`** |
| contesti | **15** — `Firelight Missile Bank` ×3, quattro doppi, dieci singoli |
| parole | **612 EN → 643 IT** (1,051) |
| rapporto | **0,93 – 1,27** |
| tab | **5** — 659, 930, 1050, 1051, 1222 (**due nello stesso contesto**) |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **4 EN su 3 unità** / 11 IT |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 39 unità · somma lotti **17+22** · 39 righe distinte · prima **53** · ultima **1222** · **0 dopo** |
| `sha256[:16]` | **`d1ca5ae4de7938e8`** |

## Comandi

```bash
python staging/editorial/L319_20261020_221933/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L319_20261020_221933/verify.py    # FAIL: 0 (22 controlli, FILE 39/39)
```

## Le due famiglie, e come si citano

| famiglia | che cosa | dove |
|---|---|---|
| **`Firelight`** | missili: il reattore resta **attivo al minimo** per essere pronto al lancio | `Storage Rack`, `Missile`, `Missile Bank` |
| **`Firestorm`** | torpedini: **nessuna schermatura** del reattore, **nessuna sicurezza** | `Torpedo` (VALUE + scheda), `Torpedo Rack`, `Battery` (VALUE + scheda + nota) |

E si **citano a vicenda**, cosa che il test verifica:

- il `Firelight` nasce dal `Firestorm Torpedo` (1049): «gli ingegneri Korath hanno potuto creare il Firelight riducendo
  ulteriormente l'elemento reattore»;
- il `Firestorm Battery` (1221) è «**meno raffinato** della più recente versione Firelight».

Sono **due generazioni** della stessa idea: la **vecchia** senza protezioni, la **nuova** miniaturizzata.

## La nota dei rifornimenti: **tre volte** in un lotto

Compare alle righe **659, 1051, 1222** — tre contesti diversi (`Cluster Mine Layer`, `Firelight Missile Bank`, `Firestorm Battery`).
La resa è **la stessa di L318** (che è la **di maggioranza** del corpus, 16 su 26):

> «Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.»

`check.py` la verifica per **uguaglianza con le tre unità del lotto + la stringa attesa**; `verify.py` con un **meccanismo diverso**:
cerca la **stringa italiana** in tutti gli altri lotti e pretende **≥2 occorrenze** (misurate: **16+**). Se qualcuno avesse inventato
una resa nuova, `verify.py` avrebbe contato 0.

## Due tab nello stesso contesto

`Firelight Missile Bank` (1050 e 1051) porta **due** righe con la tab: la nota tecnica del lancio e la nota delle munizioni. In
L311/L312/L313 ogni contesto aveva **una sola** nota; qui la configurazione è nuova e il test verifica **entrambe** le righe e che il
contesto coincida.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| `VALUE` | `Firestorm Torpedoes`, `Firestorm Batteries` **copiati per identità** |
| nota ×3 | identica nelle tre; resa **già presente** nel corpus |
| tab | righe esatte `[659, 930, 1050, 1051, 1222]`, due nello stesso contesto |
| famiglie | `Firelight` cita `Firestorm`, `Firestorm Battery` cita `Firelight` |
| nomi | 12 nomi **invariati** dove compaiono |
| contenuti | mina non dispiegata (658), scudi attivi (743), campo di lancio (930), bocche e artigli (1145), Plasma Core (1221) |
| vuote | 0 virgolette, 0 segnaposto, 0 alternative |
| FILE | 39 unità · **17+22** · prima 53 · ultima 1222 · **0 dopo** · copertura **39/39 asserita** |

## Limiti dichiarati

Nessuna approvazione (22 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato.
