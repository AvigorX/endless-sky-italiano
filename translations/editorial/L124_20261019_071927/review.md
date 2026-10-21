# REVIEW — L124 · `ships.txt` (dal Gunboat alla Raven)

Coppie EN→IT rilette in `translation.json` (`5b6c5456b299d979…`). Tutte le 29 unità sono **`PENDING`**.

## 1. Voce e registro

- **Descrizioni tecniche**: presenti, con la storia del modello quando serve («Le Hauler nacquero semplicemente
  imbullonando un abitacolo e un blocco motore a un container da carico…»).
- **Il tono del mondo**: la Hogshead è lo «spazio-bus» d'elezione, la Protector è «la nave più brutta del cielo»
  secondo una rivista, la Mule è «un guazzabuglio quanto il suo aspetto suggerisce».
- **Registro**: «tu» per il giocatore; i nomi di nave restano inglesi.
- Nessun «voi» (verificato).

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `mobile sensor platform` | **piattaforma sensoristica mobile** | 1 |
| `bounty hunting` | **caccia ai ricercati** | 6 |
| `composite fiber` | **fibra composita** | 6 |
| `space bus` | **"spazio-bus"** | 8 |
| `one-hit-wonder` | **unico successo** | 9 |
| `freelancer pilots` | **piloti "freelance"** | 10 |
| `peace among the stars` | **"pace tra le stelle"** | 20 |
| `fighter docking arms` | **bracci di attracco per caccia** | 23 |
| `Hauler I: Type F` · `Nest` | invariati (nome tecnico e soprannome) | 23 |
| `missile boat` · `missile launchers` | **lanciamissili** · **lanciatori di missili** | 28 |
| `durability to cost ratio` | **rapporto durabilità-costo** | 27 |
| `reverse thrusters` | **propulsori inversi** | 27 |
| `shield generator` | **generatore di scudi** | 27 |
| `Particle Cannons` · `Mining Laser` | invariati | 15, 16 |
| `Stars and Starships Magazine` | **la rivista Stars and Starships** | 26 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le due note tecniche** (caccia e droni) devono restare **identiche a L123**: la resa è letta da quel
   `translation.json`, e il controllo confronta le unità 12 e 17. Un lotto futuro che le tocchi diventa rosso.
2. **Un solo `VALUE`**: `Modified Argosies` è un plurale e resta inglese. Il lotto successivo **non ha `VALUE`**:
   il controllo sarà un'asserzione vuota.
3. **Tre unità con tab** (9, 12, 17): poche, e la tentazione di non controllarle è alta. Il `check.py` le elenca.
4. **Nessuna ripetizione interna**: 29 testi per 29 unità. Non c'è memoria di traduzione da confrontare dentro il
   lotto, solo quella con L123.
5. **`Nest` è un soprannome tecnico** («Hauler I: Type F»): resta inglese come i nomi di nave, e il testo lo
   spiega.
6. **`freelance` e `spazio-bus` fra virgolette dritte**: sono citazioni, non enfasi tipografica.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 29 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna nave è stata vista, nessun nome verificato a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 20 unità residue (righe 3491–4266).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 2 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (27 controlli) |
