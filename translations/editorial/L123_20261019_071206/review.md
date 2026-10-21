# REVIEW — L123 · `ships.txt` (dalla Aerie alla Fury)

Coppie EN→IT rilette in `translation.json` (`dce934d804256232…`). Tutte le 54 unità sono **`PENDING`**.

## 1. Voce e registro

- **Descrizioni tecniche**: presenti, con il dettaglio costruttivo («Grande e resistente come una nave capitale, ma
  con più spazio per il carico e i passeggeri di qualsiasi altra nave della Marina…»).
- **Le navi parlate da dentro il gioco**: la Barb è «più brutta della Protector», i piloti chiamano la Boxwing
  «bara volante», la Cutthroat ha «pod di motori imbullonati» — il tono resta quello del mondo, non del manuale.
- **Registro**: «tu» per il giocatore («ti chiedi dove dovrebbero stare i sistemi di alimentazione»); i nomi di
  nave restano inglesi.
- Nessun «voi» (verificato).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `fighter bay` · `drone bay` | **baia di caccia** · **baia per droni** | 15, 22, 31, 38, 41, 47 |
| `light carrier` · `carrier` | **portatrice leggera** · **portatrice** | 1, 11, 26 |
| `capital ship` · `warship` | **nave capitale** · **nave da guerra** | 26, 35, 39 |
| `turret mount` · `gun port` | **alloggiamento per torretta** · **portello del cannone** | 13, 42 |
| `shield matrix` | **matrice di scudi** | 34 |
| `Q-ship` · `intermodal containers` | **Q-ship** · **container intermodali** | 27, 32 |
| `city-ship` · `freight caravan` | **nave-città** · **carovana di merci** | 11, 24, 33 |
| `bunks` | **cuccette** | 8, 21 |
| `warlords` | **signori della guerra** | 25 |
| `"Flying Coffin"` | **"bara volante"** | 21 |
| `"governing corporate entities"` | **"entità aziendali di governo"** | 42 |
| `hyperdrive` | **iperguida** | 15, 22, 31, 38, 41, 47 |

## 3. Nodi aperti (da non dedurre dopo)

1. **I `VALUE` di un file di navi sono nomi propri al plurale**: `Argosies`, `Auxiliaries`, `Finches`, `Furies`.
   Il lotto successivo ne ha **uno solo** (`Modified Argosies`, unità 2822): stessa regola.
2. **La nota sui caccia** compare cinque volte e deve restare **identica** anche nei lotti successivi del file.
3. **`cargo` è italiano**: «modulo cargo», «cassa cargo» sono prestiti, non residui. La lista dei residui inglesi
   non lo include.
4. **I nomi di nave sono neutralizzati prima** della scansione dei residui: trenta nomi diversi, altrimenti il
   controllo sarebbe rosso su una traduzione corretta.
5. **`startswith` su unità con tab** fallisce: la nota sui caccia inizia con `\t` in tutte e cinque le occorrenze.
   Il costruttore usa `.strip().startswith(...)`.
6. **Le 16 virgolette sono citazioni di nomi** («Type F», «bara volante», «entità aziendali di governo»): si
   traducono solo quando sono prosa, e restano fra virgolette dritte come il sorgente.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 54 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna nave è stata vista; nessun nome di nave è stato verificato a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 49 unità residue (righe 2102–4266).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (29 controlli) |
