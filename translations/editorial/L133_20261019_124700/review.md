# REVIEW — L133 · `unfettered side missions.txt` (la consegna con l'Anomalocaris e il duello di Mera)

Coppie EN→IT rilette in `translation.json` (`c214c835e561be8e…`). Tutte le 67 unità sono **`PENDING`**.

## 1. Voce

- **Mera** è pragmatica e sprezzante, e cambia tono a metà scena: «Ma io non credo a nulla di tutto questo. Quello che
  per me conta è che quella nave è sia resistente sia piena di preziosa tecnologia antica».
- **Gli Unfettered** insultano: «Dove credi di andare, **scimmia**?», «Il tuo disonore non conosce limiti».
- **Il capo del gruppo** è cerimonioso e minaccioso: «A volte pieghiamo le regole per i nostri amici, ma con te non è
  questo il caso».
- **La narrazione** resta al presente e al «tu»: «Lasci il cantiere e vai allo spazioporto dopo il tuo incontro».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Heritage Reclaimed` / `Ancient Claim` | **identici** | 1, 11 |
| `too many ships` | **identico** | 40, 44 |
| `ent<er> … by <date>` | **entro il <date>** | 2, 3 |
| `in the system of <system>` | **nel sistema <system>** | 12 |
| `being disabled counts as a loss` | **restare fuori uso conta come sconfitta** | 33 |
| `To the victor go the spoils` | **Al vincitore vanno le spoglie** | 33 |
| `True Hai` | **Veri Hai** | 45, 66 |
| `monkey` | **scimmia** | 39, 42, 43, 45, 46, 53, 56 |
| `forfeit` | **annullato** | 41, 42, 47, 50 |
| `ceasefire` | **cessate il fuoco** | 50 |
| `priceless artifact` | **artefatto inestimabile** | 22 |
| `bribe` | **tangente** | 48 |
| `Lightning Bug` | **Lightning Bug** | 58 |
| `Ehma Ti` · `Firelode` | **invariati** | 35, 38, 52, 55 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il file è al 95,0%**: restano 8 unità (`Undeserved Anomalocaris`), che chiudono il file al prossimo lotto.
2. **`Lightning Bug` resta inglese** come nome di modello, coerente con L125 (`Nest`, `Roost`, `Skein`).
3. **`True Hai`** è un nome di fazione: «Veri Hai», non «i veri Hai».
4. **L'incoerenza cibo/forniture mediche** è del sorgente: le due frasi restano fedeli a se stesse.
5. **Le quattro unità con virgolette dispari** (47, 48, 64, 65) non vanno «chiuse»: sono battute interrotte.
6. **I tre forfait diversi** (troppe navi, flotta in orbita, relitto non in uso) hanno testi distinti: non sono varianti
   della stessa frase e non vanno uniformati.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 67 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: il duello non è stato combattuto, e i tre forfait non sono stati «provocati».
- **Nessuna revisione umana**.
- **Il file non è completo**: restano 8 unità (righe 494–510).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (32 controlli) |
