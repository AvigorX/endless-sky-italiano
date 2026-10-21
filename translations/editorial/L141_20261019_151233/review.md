# REVIEW — L141 · `unfettered 0 prologue.txt` (la caduta e la richiesta)

Coppie EN→IT rilette in `translation.json` (`2abdd856e427930b…`). Tutte le 20 unità sono **`PENDING`**.

## 1. Voce

- **Gli Slegati** raccontano la loro storia in un italiano **spezzato come l'originale**: «Una volta, centomila anni
  ormai passati», «come acqua salmastra, come albero rinsecchito», «Scimmia sciocca».
- **Il disprezzo** arriva per comparazione: «le scimmie sopravvivranno agli umani pensanti» — gli umani *sono* le
  scimmie, e gli Slegati lo dicono senza spiegarlo.
- **Il giocatore** resta cortese e asciutto: «"È una storia spaventosa. Grazie per avermi dedicato il tuo tempo."»
- **I Drak** sono descritti come allevatori: «la loro volontà è che la galassia sia uno zoo, piccoli resti di ogni
  specie ognuno in una gabbia separata».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Beyond wormhole` | **oltre il wormhole** | 1 |
| `dragonfolk` | **popoli-drago** | 1, 2, 4 |
| `brackish water` · `stunted tree` | **acqua salmastra** · **albero rinsecchito** | 1 |
| `Silly monkey` | **Scimmia sciocca** | 10 |
| `dumb ancestors` | **antenati ottusi** | 3, 5 |
| `brittle bones with mouth full of dirt` | **ossa fragili con la bocca piena di terra** | 7 |
| `a zoo… separate cages` | **uno zoo… gabbie separate** | 10 |
| `jump drive` | **motore di salto** | 14–18 |
| `share of the plunder` | **una parte del bottino** | 18 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il contesto è chiuso** (45/45): i lotti futuri cominciano da `Unfettered Jump Drive 1`, riga 139.
2. **La voce di diario 19 viene da L138**: se un revisore la cambia qui, deve cambiarla anche là.
3. **La variante 20 è nuova**: non è la frase di L138, e non va «allineata» per forza — è un'altra formulazione.
4. **La voce telegrafica non si normalizza**: aggiungere articoli per far «suonare» l'italiano romperebbe il registro.
5. **`jump drive` → motore di salto**: eccezione di glossario, applicata qui in un dialogo lungo; `Jump Drive`
   capitalizzato resta invece il nome del modulo nei file di navi.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 20 unità restano `PENDING`.
- **Nessuna missione giocata**: il dialogo non è stato visto a schermo.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 30,6%**: 102 unità da fare.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (25 controlli, invariante di segmento) |
