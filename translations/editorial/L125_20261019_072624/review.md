# REVIEW — L125 · `ships.txt` (Roost, Sparrow, Star Queen, Wasp) · **file chiuso**

Coppie EN→IT rilette in `translation.json` (`e2309e1d7fee3d39…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce e registro

- **Storia del progetto**: la Saber come «potenza militare della sua epoca», lo Scout ai tempi in cui «la galassia
  era più scarsamente popolata», la Star Queen come «reperto di un periodo più pacifico».
- **Ironia del mondo**: gli Scrapper «trappole mortali in violazione di brevetto», gli Shuttle «inutili come un
  cannone blaster su uno shuttle», le Star Barge «lente e brutte».
- **Registro**: «tu» («la nave più economica che si possa comprare»); nomi di nave inglesi.
- Nessun «voi» (verificato).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `fighter-carrying containers` · `pod` | **container portacaccia** · **pod** | 1, 7 |
| `Nest` · `Roost` · `Skein` · `Type F` | invariati | 1, 7 |
| `caravan era` | **era delle carovane** | 2 |
| `patent-infringing death traps` | **trappole mortali in violazione di brevetto** | 4 |
| `as useless as a blaster cannon on a shuttlecraft` | **inutile come un cannone blaster su uno shuttle** | 6 |
| `medium-strength interceptor` | **intercettore di forza media** | 20 |
| `luxury liner` | **transatlantico di lusso** | 13 |
| `sonic vibrations` | **vibrazioni soniche** | 13 |
| `fuel cells` · `clean fusion reactors` | **celle a combustibile** · **reattori a fusione puliti** | 14 |
| `Sol Main Belt` | **Cintura Principale del Sol** | 15 |
| `Core's mineral wealth` | **ricchezza mineraria del Nucleo** | 15 |
| `undercarriage` | **sottoscocca** | 15 |
| `withering fusillade of gunfire` | **fucileria sferzante** | 19 |
| `automation technologies` | **tecnologie di automazione** | 19 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Zero `VALUE`, zero token**: due asserzioni vuote, scritte. Il prossimo file (`incipias first contact`) ha **7
  token in sette famiglie**: `<ship>`, `<first>`, `<last>`, `<planet>`, `<destination>`, `<origin>`, `<bunks>`.
2. **I nomi dei modelli restano inglesi** anche quando il testo li spiega (`Hauler II: Type F` → «Roost»).
3. **La nota sui droni** resta identica a L123/L124: il confronto è per unità (qui l'unità 17).
4. **La Star Queen** è l'unico testo «leggero» del file: registro da dépliant turistico, reso senza ironia aggiunta.
5. **Nessuna ripetizione interna**: 20 testi per 20 unità; l'unico confronto è quello con i lotti precedenti del
   file.
6. **`ships.txt` è chiuso**: 103/103 in staging, **zero** caricate nel gioco.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna nave è stata vista, nessun nome verificato a schermo.
- **Nessuna revisione umana**.
- **Il file è completo in staging, non nel gioco.**

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (29 controlli), 103/103 righe coperte |
