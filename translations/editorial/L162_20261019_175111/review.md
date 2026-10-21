# REVIEW — L162 · `avgi outfits.txt` (serbatoi, sensori, scudi)

Coppie EN→IT rilette in `translation.json` (`2a85b71584753049…`). Tutte le 10 unità sono **`PENDING`**.

## 1. Voce

La voce Avgi resta **tecnica e leggermente autoironica** quando parla dei propri limiti: «un generatore che si può
definire generosamente anemico», «c'è un limite a quanto si può spingere una visione incompleta della fisica di base
che sta dietro agli scudi, e questo generatore quel limite lo sfiora».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `insulated pressure vessel` | **serbatoio in pressione coibentato** | 1 |
| `minimum intrusion into space reserved for other systems` | **invadendo il meno possibile lo spazio riservato agli altri sistemi** | 1 |
| `coolant lines` | **condotte del refrigerante** | 2 |
| `ranged, and tracked` | **localizzate e seguite** | 3 |
| `low microkelvins` | **microkelvin bassi** | 4 |
| `shielded ships` | **navi scudate** | 5 |
| `superconducting magnets` | **magneti superconduttori** | 7 |
| `enormous superconducting coils` | **enormi bobine superconduttrici** | 10 |

## 3. Nodi aperti (da non dedurre dopo)

1. **I nomi degli scudi non sono nel testo**: `Diffuse Deflector` e `Specular Deflector` esistono solo come contesti.
   Il controllo deve distinguerli per contenuto, non per stringa.
2. **Il lessico di L161 si riusa e si verifica**: `poltiglia di deuterio`, `criorefrigeratori` compaiono in idx 1 e un
   controllo lo pretende, così un lotto non può divergere dal precedente.
3. **Nessun `VALUE`**: le asserzioni vuote (`[]`) sono scritte, e questo è un controllo in più, non in meno.
4. **`Deep` resta invariato** come nome di regione, coerente con L155.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 10 unità `PENDING`.
- **Nessuna nave vista a schermo**, **nessuna partita avviata**.
- **Nessuna revisione umana**.
- **Secondo lotto di `avgi outfits.txt`**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (18 controlli) |
