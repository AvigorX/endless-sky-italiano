# REVIEW — L103 · `quarg missions.txt` (satelliti e mondo ad anello)

Coppie EN→IT rilette in `translation.json` (`2e3f270bdda5ce6a…`).

## 1. Voce e registro

- **Il Quarg dei satelliti** (3–14): formale e cortese, dà del **«tu»** («Salute, amico umano», «Avresti per caso
  il tempo»). Quando spiega, resta asciutto: «fornire qualche misura che scoraggi ulteriori attacchi è solo una
  cortesia».
- **Il Quarg del mondo ad anello** (26–35): anche lui dà del «tu», ma è più burocratico — parla di «criteri» e
  «servizio di trasporto merci», consulta un **datapad** e chiude con «Stammi bene, umano».
- **Il narratore** (15, 37) descrive con precisione tecnica: le piramidi, i robot caricatori, le decine di
  migliaia di tonnellate. Non commenta.
- **I `DIALOG`** (16–20, 36, 41–42) sono in seconda persona plurale («Aprite la stiva», «Atterrate»): il
  giocatore è «voi», come sempre nella narrazione.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `to help humans in the other end of this region, the South` | **per aiutare gli umani dall'altra parte di questa regione, a Sud** | 7 | |
| `foolish thugs that plague this whole region` | **stolti teppisti che infestano tutta questa regione** | 11 | |
| `without even more needless slaughter` | **senza un altro inutile massacro** | 11 | |
| `is but a courtesy` | **è solo una cortesia** | 11 | |
| `loaderbots` | **robot caricatori** | 15 | |
| `triangular pyramids` | **piramidi triangolari** | 15 | |
| `roughly half your size` | **all'incirca grande la metà di voi** | 15 | |
| `drift out to the void` | **esca alla deriva nel vuoto** | 16 | |
| `former slave-colony planet` | **pianeta che fu colonia di schiavi** | 17 | |
| `demanding tribute` | **chiedono un tributo** | 19 | |
| `right at the docks` | **proprio sulla banchina** | 20 | |
| `diverts its attention to you` | **rivolge la sua attenzione a voi** | 26 | |
| `data pad` | **datapad** | 27, 34 | |
| `cargo convoys` | **convogli merci** | 27 | |
| `meets the criteria` | **soddisfa i criteri** | 27 | |
| `special open section for humans` | **sezione speciale aperta ai visitatori umani** | 31 | |
| `internal style and decoration … closer to human standards` | **stile e arredamento interno … più vicini agli standard umani** | 31 | |
| `It gestures a bow to you` | **Vi fa un inchino con un gesto** | 35 | |
| `each crate carefully accounted for` | **ogni cassa accuratamente contata** | 36, 41 | |
| `freighters and convoys` | **mercantili e convogli** | 37 | |
| `tens of thousands of tons` | **decine di migliaia di tonnellate** | 37 | |
| `hands you <payment>` | **vi consegna <payment>** | 20, 38, 42 | |

## 3. Nodi aperti (da non dedurre dopo)

1. **I tre `VALUE` sono identici all'inglese** e devono restare tali: `Deploy Quarg Scanners` (tabellone dei
   lavori) e `Human Construction Materials` (designazione del carico). Se un revisore li «traduce», il
   `check.py` e il `verify.py` di questo lotto diventano rossi — ed è il comportamento voluto.
2. **`Poisonwood`** resta invariato: è il nome di un pianeta, non un descrittore.
3. **Il datapad** è «datapad» in tutto il progetto: non alternare con «tablet» o «palmare».
4. **Le unità 8/12 e 10/13** sono la stessa battuta in due rami del dialogo: modificarne una sola romperebbe
   l'uguaglianza e il `verify.py` diventerebbe rosso.
5. **L'unità 30 non chiude la citazione**: il discorso finisce nella 31. È il quarto caso nel progetto (dopo L99,
   L100 e L103 stesso) e il `check.py` asserisce l'indice.
6. **Il mondo ad anello** è «mondo ad anello» anche qui, coerente con L102: non «anello orbitale».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 42 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**.
- **Il file non è completo**: 88 unità residue su 2 contesti.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (28 controlli) |
