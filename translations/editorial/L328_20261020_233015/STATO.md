# STATO — L328 (`data/_ui/help.txt`, righe 72–116) — **SECONDO DI TRE LOTTI**

**Stato: CHIUSO.** 25 unità, **11 contesti**. `check.py` esce 0 con **20 controlli**; `verify.py` esce 0 con **15 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). **Nessuna scrittura su `state.db`** (verificato anche dal `mtime`).

Anche questo lotto è una **trascrizione**: le 25 unità sono **già `APPROVED`**. La query di stato è stata fatta **prima** dell'export, come
prescrive il metodo aggiornato in L327.

| voce | valore |
|---|---|
| directory | `staging/editorial/L328_20261020_233015/` |
| file | `data/_ui/help.txt` (**113 unità**: 68 `APPROVED` + 45 `PENDING`) |
| righe | 72–116 (**seconda parte**) |
| unità | **25 `HELP`** — tutte `APPROVED` |
| contesti | **11** — `map advanced` (+`ports`, `shops`, `stars`, `danger`), `multiple ships`, `shop with multiple ships`, `player info`, `fleet management`, `ship info`, `multiple ship controls` |
| parole | **988 EN → 850 IT** (0,860) |
| rapporto | **0,81 – 1,20** |
| tab | **0** |
| virgolette | **10** su tre righe (93: 2, 105: 2, 106: 6) |
| segnaposto | **1**: `<View player info>` |
| `check.py` | **20 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **15 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di SEGMENTO**: 25 unità proprie, nessun altro lotto sulle righe, confine **119** |
| `sha256[:16]` | **`412625a95434a977`** |

**Copertura del file**: **53 su 113** unità (L327 28 + L328 25). Restano **60** unità, che sono il terzo lotto (L329).

## Comandi

```bash
python staging/editorial/L328_20261020_233015/check.py     # FAIL totale: 0 (20 controlli)
python staging/editorial/L328_20261020_233015/verify.py    # FAIL: 0 (15 controlli, SEGMENTO 72-116)
```

## La terminologia approvata: «fornitore», non «emporio»

Il testo approvato chiama l'`outfitter` **«fornitore»** (5 unità di questa finestra: 81, 83, 92, 109, 116) e il `shipyard` **«cantiere»**.
La mia convenzione precedente era `outfitter` → **«emporio»**, presa dal corpus dei lotti passati.

**Misura aggiornata sul corpus intero**:

| forma | staging (tutti i lotti) | unità `APPROVED` |
|---|---|---|
| «fornitor-» | **81** | **13** |
| «emporio» | **53** | **0** |

Dunque «fornitore» è **maggioritario** anche nello staging, e **unico** nelle unità approvate. La regola `outfitter` → «emporio» che avevo
fissato in un lotto precedente è **minoritaria** e va **corretta**: la divergenza è dichiarata qui, e non è stata «aggiustata» nel testo
approvato.

## Le etichette del pannello sono tradotte

| riga | inglese | approvato |
|---|---|---|
| 105 | `"Save Order"` | **"Salva ordine"** |
| 106 | `"Park"` | **"Parcheggia"** |
| 106 | `"Park Local"` | **"Parcheggia le locali"** |
| 106 | `"Park All"` | **"Parcheggia tutte"** |
| 93 | `"park"` (verbo) | **"parcheggiare"** |

La 106 ha **sei** virgolette: tre coppie di etichette. Il test le verifica una per una: se una sola fosse rimasta in inglese, il conteggio
non tornerebbe.

## Il segnaposto: uno solo, e non si traduce

```
EN: The player info panel can be brought up at any time by pressing <View player info>, including mid-flight.
IT: Il pannello dati pilota può essere aperto in qualsiasi momento premendo <View player info>, anche in volo.
```

Il comando resta **`<View player info>`**: è il nome del tasto, non una descrizione. Nella stessa finestra il testo usa `Shift+clic`,
`Control+clic`, `F`, `T` — tutti **letterali**.

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| centrale | **25/25** identiche alla colonna `italian` del database |
| stato | **25 `APPROVED`**, nessun cambio di stato |
| contesti | **11**, con `ports` 3, `shops` 3, `multiple ship controls` 4 |
| segnaposto | **1**, `<View player info>`, identico all'inglese |
| virgolette | **10** su **tre righe** (93, 105, 106), etichette **tradotte** |
| lessico | «fornitore», «cantiere», «scorte», «ammiraglia», «pannello dati pilota» presenti; **nessun «emporio»** |
| tasti | `Shift+clic`, `Control+clic`, `F`, `T` |
| SEGMENTO | 25 righe distinte, prima 72, ultima 116, **nessun altro lotto**, confine **119** |
| database | **nessuna scrittura** (`mtime`) |

## Limiti dichiarati

- **Il testo non è mio**: è quello approvato, trascritto **generandolo dal database** (nessuna ridigitazione), e verificato.
- **Copertura parziale dichiarata**: **53 su 113** unità del file.
- **Divergenza terminologica aperta**: `outfitter` è «fornitore» nelle unità approvate, «emporio» in 53 unità dello staging. Non è stata
  uniformata: è **dichiarata**.
- **Nessun testo visto nel gioco**.
