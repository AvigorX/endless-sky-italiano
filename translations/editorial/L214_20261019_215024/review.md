# REVIEW — L214 · `deep jobs.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`e2d9f07af3bd3c95…`). Tutte le 35 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **`As instructed, you deliver the package to`** → «Come da istruzioni, consegni il pacco» **senza** preposizione: le sei
   alternative la portano dentro di sé («alla reception», «a un addetto», «a un negozio», «a un agente», «a una signora»,
   «a un capitano»). È l'unico modo per avere sei frasi corrette in italiano.
2. **`bored-looking spaceport security officer`** → «un addetto alla sicurezza dello spazioporto dall'aria annoiata»:
   mantiene il dettaglio umoristico senza appiattirlo in «un addetto».
3. **`elaborate curiosities store`** → «un elaborato negozio di curiosità»: «elaborato» rende *elaborate* meglio di
   «ricercato», che suggerirebbe gusto anziché complessità.
4. **`plainclothes officer`** → «un agente in borghese»: lessico italiano fisso.
5. **`minimal ID confirmation`** → «una verifica minima del documento»: rende la fretta burocratica.
6. **`Deep Security`** resta invariato: è il nome di un'organizzazione, come `Deep Sky`.
7. **`activewear`** → «abbigliamento sportivo»; **`the main drag`** → «la via principale»: registro colloquiale reso senza
   calco.
8. **`he vouched for your increased job opportunities`** (LOGBOOK) → «ha garantito per te e ti ha aperto più opportunità
   di lavoro»: la frase inglese è compressa, e in italiano va sciolta o resta ambigua.
9. **`His manner is very rehearsed`** → «Il suo modo di fare è molto impostato»: «impostato» rende l'artificio senza
   «provasse», che sarebbe un calco.
10. **`measured look`** → «uno sguardo misurato»: mantiene l'ambiguità fra calcolo e giudizio.
11. **Cortesia di Wayde**: *Please, have a seat and allow me to take a moment of your time* → «Accomodati e concedimi un
    momento del tuo tempo». Il «Lei» sarebbe stato naturale, ma il registro della campagna è unico. Perdita dichiarata.

## 2. Un punto di attenzione (non un errore)

L'apice compare **sei volte in entrambe le lingue** ma in **unità diverse**: in inglese sono contrazioni (`won't`, `I'm`,
`Don't`, `You've`), in italiano sono elisioni (`un'azienda`, `dall'aria`, `l'uomo`, `l'agente`, `l'attenzione`). Il
controllo non confronta i totali: elenca le unità, così la coincidenza numerica non maschera una differenza reale.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 35 unità `PENDING`.
- **Nessuna missione giocata**: i 15 tab sono verificati come caratteri, non visti come paragrafi a schermo.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26), `verify.py` exit **0** (19) |
