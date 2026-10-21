# STATO — L302 (`data/remnant/remnant ships.txt`, righe 807–1291)

**Stato: CHIUSO.** Secondo lotto del file: **dodici unità** in **sei contesti** — una **terzina**, **tre coppie interne** e **due
singole** — con la **formula dell'occultamento** che qui torna **tre volte**. File a **24/38 (63,2%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L302_20261020_202611/` |
| file | `data/remnant/remnant ships.txt` (**38 unità · 1.633 parole · righe 17–1.826 · 35 `DESCRIPTION` + 3 `VALUE`**) |
| righe | 807–1291 |
| unità | **12** — **11 `DESCRIPTION` + 1 `VALUE`** |
| contesti | **6** — `Heron` (1) · `Ibis` (3) · `Merganser` (2) · `Pelican` (1) · `Penguin` (2) · `Peregrine` (3) |
| terzina | **`Peregrine` 1289/1290/1291**, tab sulla 2ª e 3ª |
| coppie | `Ibis` 892/893 · `Merganser` 981/982 · `Penguin` 1201/1202 |
| `VALUE` | **`Ibises`** (812) — **copiato** |
| parole | **486 EN → 509 IT** (1,05) |
| rapporto | **1,00 – 1,13** |
| tab | **6** — righe **807, 893, 982, 1202, 1290, 1291** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **6 EN / 15 IT** |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **12 prima** · 12 qui · **14 dopo** la 1291 |
| `sha256[:16]` | **`c01aa63657ca9588`** |

## Comandi

```bash
python staging/editorial/L302_20261020_202611/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L302_20261020_202611/verify.py    # FAIL: 0 (24 controlli)
```

## La famiglia della formula dell'occultamento

> *The cloaking technology is built into the **Merganser**'s hull; it cannot be removed or transferred to another ship.*

Compare **quattro volte** in due lotti: **`Gull`** (549, L301), **`Merganser`** (982), **`Penguin`** (1202), **`Peregrine`**
(1291). La resa è **identica a meno del nome della nave**:

> «La tecnologia di occultamento è incorporata nello scafo della **\{nave\}**; non può essere rimossa né trasferita a un'altra nave.»

Il `check.py` **riapre** `L301/translation.json`, sostituisce il nome con `X` in entrambe le versioni e confronta: se una delle
quattro divergesse, fallirebbe. È la differenza fra «la frase c'è» e «la frase è la stessa».

## La continuità di `Heron`

La **806** (L301) è la **prima** unità di `Heron`, la **807** (qui) è la **seconda**: la nave è descritta in **due lotti** ma il
contesto è **uno**. Il test verifica che la 807 inizi con la tab e che la 806 **non** la inizi — cioè che il taglio sia caduto
**dentro** il gruppo, nel punto dichiarato.

## La terzina `Peregrine`

| riga | tab | contenuto |
|---|---|---|
| 1289 | — | la **prima nave da guerra capitale** di Taely, dopo oltre un secolo |
| **1290** | `\t` | l'**omonimo**: il falco più veloce del mondo, «colpire forte e in fretta» |
| **1291** | `\t` | **l'occultamento** incorporato nello scafo |

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `hit-and-run attacks` | **attacchi mordi e fuggi** | corpus, **senza trattini** |
| `void sprites` | **spiriti del vuoto** | corpus (prosa); il nome dell'oggetto resta `Void Sprite Parts` |
| `prefect` | **prefetto** | corpus |
| `Ember Waste` | **`Ember Waste` invariato** | anomalia aperta (69 «Distesa di Braci» vs 16 inglese) |
| `capital warship` | **nave da guerra capitale** | |
| `a wing of support craft` | **uno stormo di mezzi di supporto** | |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **14 unità**.
