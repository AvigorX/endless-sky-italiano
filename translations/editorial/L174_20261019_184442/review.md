# REVIEW — L174 · `avgi ships.txt` (Koryfi, Melodikos, Avlaki, Harmonikos)

Coppie EN→IT rilette in `translation.json` (`c734fd303220cc1b…`). Tutte le 14 unità sono **`PENDING`**.

## 1. Voce

**Manuale tecnico con ambizione narrativa**: le astronavi `Avgi` sono descritte per storia del progetto, non per
prestazioni. La Koryfi «precede l'invenzione dell'iperguida», l'Avlaki «discende alla lontana da un rimorchiatore
solare-elettrico», l'Harmonikos «trasporta merci fra le stelle». Il tono resta **asciutto e documentale**, con un'unica
frase ironica ripetuta quattro volte: l'accelerazione «generosamente descritta come fiacca».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `light passenger transport` | **trasporto passeggeri leggero** | 1 |
| `intrasystem travel` | **viaggi intrasistemici** | 1 |
| `ample living space` | **ampi spazi abitabili** | 1 |
| `spacious centrifuge habitat` | **spazioso habitat centrifugo** | 5 |
| `mass transit between the stars` | **trasporto di massa fra le stelle** | 5 |
| `pre-hyperdrive solar-electric tug` | **rimorchiatore solare-elettrico ... all'iperguida** | 8 |
| `ad-hoc passenger transport` | **trasporto passeggeri improvvisato** | 13 |
| `artificial gravity` | **gravità artificiale** | 13 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le quattro formule dei propulsori sono una sola stringa**: se una divergerà, il controllo fallirà — ed è voluto.
2. **I tab sono parte del dato**: 8 unità ne hanno uno iniziale, e un tab in più o in meno è un errore.
3. **I possessivi inglesi non hanno equivalente italiano**: «di Koryfi» sostituisce `Koryfi's`. Non si contano gli apici.
4. **`TEXT` in questo file può essere un nome** (`Z-333 "Spark" Fusion Torch` in L175): in quel caso **non si traduce**.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 14 unità `PENDING`.
- **Nessuna astronave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto di `avgi ships.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (21 controlli) |
