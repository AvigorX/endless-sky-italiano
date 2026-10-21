# REVIEW — L222 · `successor ships.txt` (quinto e ultimo lotto)

Coppie EN→IT rilette in `translation.json` (`30ae0dcd3ae347d4…`). Tutte le 26 unità sono **`PENDING`**.

## 1. Le 20 unità copiate

18 `TEXT` di equipaggiamento (`"Ryuit" Fusion Core`, `"Veusa" Inductive Reverser`, `3-"Kaska" Betavoltaic Cell`…) e 2
`VALUE` (`Vujleten`, `Vujleten-Usaqri`), **generati dal sorgente** e verificati carattere per carattere.

## 2. Le due coerenze

### 2.1 Vujlet: 12 e 14

| | apertura | punteggiatura degli intercettori |
|---|---|---|
| 12 | «Con la grazia di un uccello che svolazza, la compatta Vujlet attraversa le stelle: è una nave da guerra…» | «a corto raggio **e** relativamente vulnerabili» |
| 14 | «La compatta Vujlet è una nave da guerra…» | «a corto raggio**,** relativamente vulnerabili» |

Il testo condiviso («una nave da guerra prodotta in serie dalle Alte Case… un ponte utile tra gli intercettori a corto
raggio») è **identico**, e la differenza di punteggiatura del sorgente è **conservata**. Il `verify.py` verifica tutte e
due, non solo la parte condivisa.

### 2.2 Veusade: la formula di L221

L'unità 24 di L221 (*such a narrowly-focused design makes these vessels ill-suited for multipurpose use, but they are
frequently seen as auxiliary or police craft*) e l'unità 1 di L222 dicono la stessa cosa di due navi diverse. Resa unica:
«un progetto così specializzato rende queste navi inadatte all'uso polivalente, ma vengono spesso impiegate come unità
ausiliarie o di polizia». Cambia solo il verbo finale: *intercept* → «intercettare» (L221), *catch* → «raggiungere» (L222).

## 3. Decisioni di resa

1. **`bristles with gun ports`** → «è piena di feritoie per le armi»: `bristles` è visivo, non tecnico.
2. **`just enough to saturate its hardpoints`** → «appena sufficiente … a saturare i suoi punti d'attacco». `hardpoints`
   resta «punti d'attacco», come fissato nei lotti precedenti.
3. **`with the grace of a flitting bird`** → «Con la grazia di un uccello che svolazza».
4. **`self-sufficient unit`** → «unità autosufficiente»; **`light-duty roles`** → «ruoli leggeri».
5. **`resource-intensive`** → «esigenti in risorse»; **`to build and operate`** → «da costruire e da far operare».
6. **`stealth reconnaissance vessel`** → «nave da ricognizione furtiva»; **`cloaking technology`** → «tecnologia di
   occultamento»; **`stealth equipment`** → «equipaggiamento occultante».
7. **`House Kaatrij`** → **Casa Kaatrij**; **`New Houses`** → **Nuove Case**; **`High Houses`** → **Alte Case**.
8. **`their Predecessors' domain`** → «il dominio dei Predecessori».
9. **`eighteen hundred years ago`** → «milleottocento anni fa».
10. **`consuming the power output of a large fusion reactor`** → «consumava la potenza di un grande reattore a fusione».
11. **`incorporate a ship's shielding into the cloak's operation`** → «integrare gli scudi di una nave nel funzionamento
    dell'occultamento».
12. **`a steady stream of shield energy`** → «un flusso costante di energia degli scudi»; **`higher-capacity shield grid`** →
    «rete di scudi di capacità superiore»; **`more crew to maintain it`** → «un equipaggio più numeroso per mantenerla».
13. **`draws a moderate amount of fuel and shields while active`** → «assorbe una quantità moderata di carburante e di scudi
    mentre è attiva»: descrizione di equipaggiamento, registro tecnico asciutto.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 26 unità `PENDING`.
- **Nessuna nave vista nel gioco**: il funzionamento dell'occultamento (carburante e scudi assorbiti) è tradotto dal testo,
  non osservato in partita.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29), `verify.py` exit **0** (20), file chiuso 146/146 |
