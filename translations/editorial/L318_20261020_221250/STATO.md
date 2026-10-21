# STATO — L318 (`data/korath/korath weapons.txt`, righe 53–603)

**Stato: CHIUSO.** Primo lotto del file: **17 unità su 39** (**43,6%**). `check.py` esce 0 con **22 controlli**; `verify.py` esce 0
con **20 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L318_20261020_221250/` |
| file | `data/korath/korath weapons.txt` (39 unità · 1.089 parole · 37 `DESCRIPTION` + 2 `VALUE`) |
| righe | 53–603 |
| unità | **17** — tutte `DESCRIPTION` |
| contesti | **15** — `Shunt-Strike Turret` e `Piercer Missile Launcher` doppi, tredici singoli |
| parole | **477 EN → 493 IT** (1,034) |
| rapporto | **0,86 – 1,28** |
| tab | **2** — 109, 473 |
| virgolette | **0** |
| segnaposto / alternative | **0 / 0** |
| apici | **3** — righe 108, 109, 472 |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** (il lotto apre il file) · 17 qui · **22 dopo** (la prossima alla 615) |
| copertura | **17/39 (43,6%)** — **stampata, non asserita** |
| `sha256[:16]` | **`3b472973d562863b`** |

## Comandi

```bash
python staging/editorial/L318_20261020_221250/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L318_20261020_221250/verify.py    # FAIL: 0 (20 controlli, 17/39)
```

## Il contratto aveva torto su un punto, e la misura l'ha corretto

Il `HANDOFF_L318` dichiarava che la riga 154 avesse **due punti finali** (`close..`), da non riprodurre. **Non è vero**: il testo
sorgente è

```
The Korath like to keep their enemies close... but not too close.
```

un'**ellissi** con i tre punti, e i «due punti» erano un **artefatto della mia anteprima troncata** nel contratto. La resa usa `...`
come tutto il progetto:

> «Ai Korath piace tenere i nemici vicini... ma non troppo.»

Il test ora verifica **l'ellissi** (tre punti presenti, nessun `..` residuo, nessun carattere `…`) e **l'assenza** di refusi
inventati. **Il workspace vince sul documento**: il contratto è stato corretto dalla misura, non il contrario.

## La nota dei rifornimenti: resa di maggioranza, e un'incoerenza misurata

La riga 473 è la nota di famiglia `Ammunition for this weapon can be restocked at any outfitter.` — **36 unità** nel database, **26**
già in staging. La resa usata qui è quella **di maggioranza**:

| resa | unità |
|---|---|
| **`Le munizioni per quest'arma possono essere rifornite presso qualsiasi emporio.`** | **16** ← usata |
| `Le munizioni di quest'arma si possono rifornire in qualsiasi emporio.` | 5 |
| `…presso qualsiasi negozio di equipaggiamenti.` | 3 |
| `…si possono rifornire in qualsiasi negozio di equipaggiamenti.` | 2 |

**Quattro rese per una frase sola**: è un'**incoerenza del corpus**, dichiarata qui e **non corretta** (un lotto non riscrive i
lotti altrui). Le due varianti con «negozio di equipaggiamenti» contraddicono anche la decisione di progetto `outfitter` →
**«emporio»**.

Il test `verify.py` verifica l'uguaglianza con un **meccanismo diverso** da `check.py`: non confronta con **una** unità scelta per
testo inglese, ma **cerca la stringa italiana** in tutti gli altri lotti e pretende che compaia **almeno due volte**.

## Le armi del lotto

| riga | arma | idea |
|---|---|---|
| 53 | `Grab-Strike Turret` | proiettili che **tirano il bersaglio verso** la nave Korath |
| 108–109 | `Shunt-Strike Turret` | sfere di **microbot** che passano gli scudi e **convertono lo scafo**; chi le lancia deve avere un **Systems Core** adeguato |
| 154 | `Banisher Grav-Turret` | «tenere i nemici vicini… ma non troppo» |
| 180 | `Expeller Grav-Ray` | la versione a bassa potenza: **respinge** dalle portanavi e dai civili |
| 211 | `Warder Anti-Missile` | difesa **antimissile** |
| 249 | `Fire-Lance` | raggio a **media portata** per i caccia |
| 287 | `Blaze-Pike Turret` | due Fire-Lance che formano una **gestalt**: una colonna più lunga, più calda, **ipnotica** |
| 327 | `Korath Inferno` | **tre** Fire-Lance in **sinergia**: il «vertice del progetto delle armi dell'Esilio» |
| 368 | `Thermal Repeater` | proiettile più piccolo e semplice; **calore** che impone pause |
| 412 | `Thermal Repeater Turret` | dardi di **plasma surriscaldato**; serve un **raffreddamento ausiliario** |
| 423–473 | `Piercer` (missile, rack, launcher) | **due testate**: la piccola apre il varco, la grande passa |
| 563 | `Korath Detainer` | **portata lunghissima** e disturbo alla **propulsione**: porta il nome dei Korath |
| 603 | `Cluster Mine` | **munizione**: ogni mina si divide in **undici** submunizioni |

## Limiti dichiarati

Nessuna approvazione (17 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **Il file non è finito**: restano
**22 unità / 612 parole** (righe 615–1222), che lo chiudono in **L319**.
