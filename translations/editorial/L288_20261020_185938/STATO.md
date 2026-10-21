# STATO — L288 (`data/gegno/gegno ships.txt`, righe 725–1192)

**Stato: CHIUSO.** Terzo lotto del file: **8 descrizioni** e **1 `VALUE`**, su **sette contesti**. Il contesto `ship:Gneiss` ha
**tre unità** — una copiata e due tradotte. File a **25/37 (67,6%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L288_20261020_185938/` |
| righe | 725–1192 |
| unità | **9** — 8 `DESCRIPTION` + **1 `VALUE`** (`Gneiss`, riga 983) |
| parole | **469 EN → 525 IT** (1,12) |
| rapporto | **1,00 – 1,18** (il `VALUE` a 1,00) |
| contesti | **7** — `Rhyolite` · `Eclogite` · `Diorite` · `Hornfel` · `Gneiss` ×3 · `Granulite` · `Halite` |
| coppia consecutiva | **1** — 1061–1062 (`Gneiss`) |
| tab | **1** (unità 7) |
| virgolette | **0** · apici **9 EN / 9 IT** |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 16 prima · 9 qui · **12 dopo** la 1192 |
| `sha256[:16]` | **`5b059851c79ed419`** |

## Comandi

```bash
python staging/editorial/L288_20261020_185938/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L288_20261020_185938/verify.py    # FAIL: 0 (22 controlli)
```

## Tre tipi nello stesso contesto

`ship:Gneiss` contiene **tre unità**:

| riga | tipo | trattamento |
|---|---|---|
| 983 | `VALUE` | **copiato**: `Gneiss` |
| 1061 | `DESCRIPTION` | tradotto (la scheda) |
| 1062 | `DESCRIPTION` | tradotto (la seconda metà, con il tab) |

Il test **distingue per tipo, non per contesto**: la `VALUE` è verificata per identità, le due `DESCRIPTION` per differenza. Un
controllo che filtrasse solo su `context == 'ship:Gneiss'` conterebbe tre unità «da tradurre» e fallirebbe — o, peggio,
tradurrebbe il nome della nave.

## La coppia 1061–1062

La prima metà finisce con «…sparano minacciose bordate contro la forza avversaria.»; la seconda comincia con
«**Purtroppo**, in cambio di una potenza di fuoco enorme…». Il test verifica che la seconda **non** si apra con «I Gneiss».

## Il `Halite` che continua

L'unità 9 (riga 1192) descrive il `Halite` come **velivolo sperimentale dei Gegno Scin**, «il primo velivolo da combattimento».
Ma il contesto **continua** oltre il confine: le righe **1193–1194** sono ancora `ship:Halite` e apriranno L289. Il `verify.py`
verifica che la prima unità dopo la 1192 appartenga ancora a `ship:Halite`: il confine è **dichiarato**, non assunto.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `interceptor` | **intercettore** | |
| `gunboat armed to the teeth` | **cannoniera armata fino ai denti** | |
| `hit-and-run vessel` | **vascello mordi-e-fuggi** | |
| `workhorse` | **bestia da soma** | |
| `mounting points` / `cargo pods` | **punti di attacco** / **capsule da carico** | |
| `broadside` | **bordata** | |
| `armor plating` | **corazzatura** | |
| `fighter-based craft` | **velivolo da combattimento** | |
| `pulse weapon` / `shield technology` | **tecnologia degli impulsi** / **degli scudi** | |
| `Hornfels` (plurale inglese) | **gli Hornfel** | il nome resta singolare, come nel `VALUE` |

## Limiti dichiarati

Nessuna approvazione (9 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **12 unità**.
