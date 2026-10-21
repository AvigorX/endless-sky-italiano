# REVIEW — L161 · `avgi outfits.txt` (lamine radiative, ramscoop, serbatoio di deuterio)

Coppie EN→IT rilette in `translation.json` (`342d227d771ad013…`). Tutte le 11 unità sono **`PENDING`**.

## 1. Voce

La voce Avgi è **tecnica e sicura di sé**: descrive materiali e campi, non emozioni. «Questo insieme modulare di
radiatori a microcanali di grafene può essere montato in modo conforme allo scafo», «un magnete al plasma conferisce a
questo ramscoop un'area di raccolta senza pari». Il lessico resta fisico: `campo magnetico quasi statico`, `corrente
oscillante e sfasata`, `sistema a zero ebollizione`.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Radiative Laminae` · `Concealment Laminae` | **identici** | 1, 4 |
| `graphene microchannel radiators` | **radiatori a microcanali di grafene** | 2 |
| `outfit space` | **spazio per gli equipaggiamenti** | 3, 6 |
| `quantum dot phased array` | **schiera in fase a punti quantici** | 5 |
| `reaction mass` | **massa di reazione** | 7 |
| `ramscoop` | **ramscoop** (invariato) | 7, 8, 9, 10 |
| `deuterium slush` | **poltiglia di deuterio** | 11 |
| `pressure vessel` | **serbatoio in pressione** | 11 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Radiative Lamina` è un contesto da 3 unità** (`VALUE` + due descrizioni): contare i contesti non basta, serve la
   distribuzione (un mio controllo diceva 2 e ha fallito sul dato).
2. **La nota sugli hardpoint è ripetuta** in due oggetti (3 e 6): la resa identica è un requisito, non una comodità.
3. **`ramscoop` non si traduce**, ma `Magnetic Scoop` e `Plasmadyne Scoop` restano nomi inglesi di oggetto: le due
   scelte convivono nello stesso testo.
4. **Zero token e zero virgolette**: due asserzioni vuote scritte, non due controlli omessi.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 11 unità `PENDING`.
- **Nessuna nave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Primo lotto di `avgi outfits.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (20 controlli) |
