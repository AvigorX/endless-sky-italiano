# REVIEW — L153 · `coalition jobs.txt` (delegazione, seconda vendita, criminali)

Coppie EN→IT rilette in `translation.json` (`7b5d3d976e20fb6c…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce

- **La delegazione** parla per formule: «Un contributo del tutto inatteso, ma di grande valore è questo».
- **L'Arach** inverte: «a te le nostre armi e le nostre navi da guerra ancora non possiamo vendere».
- **Il Saryd** spiega la dottrina militare con la stessa inversione: «ben addestrato a usare le armi solo per difesa e
  solo per giustizia, è».
- **I `DIALOG` dei criminali** sono action-report asciutti: «Dopo un breve scontro a fuoco i criminali si arrendono».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Sell Jump Drive` · `Contain Criminals` | **identici** | 9, 12, 15, 18 |
| `on site` · `on the site` | **sul posto** · **sul luogo** | 13/16 · 19 |
| `to you our weapons… we still cannot sell` | **a te le nostre armi… ancora non possiamo vendere** | 4 |
| `for defense and only for justice, they are` | **per difesa e solo per giustizia, è** | 7 |
| `cut off any exits` | **tagliare ogni via di fuga** | 14 |
| `relinquishing their weapons immediately` | **consegnano subito le armi** | 20 |
| `the great Arach "Houses,"` | **le grandi "Case" Arach** | 1 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le inversioni restano**: sono la voce delle specie, e due controlli le cercano nel testo tradotto.
2. **`on site` ≠ `on the site`**: la differenza di un articolo produce due rese, e il controllo le pretende **diverse**.
3. **`Contain Criminals` è lo stesso `VALUE` in tre missioni**: la resa è identica, ma le descrizioni no.
4. **Le «Case» Arach** hanno le virgolette nel sorgente: si mantengono, e l'unità 1 ha esattamente 2 virgolette.
5. **Errore in corsa**: un'asserzione cercava «ogni è impegnato» (inesistente) invece di «ognuno è impegnato».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità `PENDING`.
- **Nessuna missione giocata**.
- **Nessuna revisione umana**.
- **Quarto lotto del batch** L150–L153.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (25 controlli) |
