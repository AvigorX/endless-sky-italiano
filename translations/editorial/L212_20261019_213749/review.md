# REVIEW — L212 · `deep jobs.txt` (primo lotto)

Coppie EN→IT rilette in `translation.json` (`d3561b72157dd31c…`). Tutte le 45 unità sono **`PENDING`**.

## 1. Decisioni di resa

1. **«Come da istruzioni, tu»** per *As instructed, you*: il «tu» esplicito chiude il frammento e permette la
   concatenazione con «apri …», che altrimenti resterebbe sospeso.
2. **«Tu»** per *You* (unità 2): è l'alternativa breve del primo frammento, e va resa come frammento autonomo.
3. **Frammenti all'infinito no, alla seconda persona sì** («apri», «lasci», «seppellisci», «consegni», «getti»): la frase
   composta è la voce del narratore che descrive le azioni del giocatore, e in italiano regge la seconda persona.
4. **`deposit box` → «cassetta di sicurezza»**, **`storage locker` → «armadietto di deposito»**: due cose diverse, e
   l'italiano le distingue.
5. **`out in the middle of nowhere` → «in mezzo al nulla»**: idiomatico, non letterale.
6. **`rickety-looking wooden tower` → «torre di legno che sembra cadere a pezzi»**: rende *rickety* senza «traballante»,
   che su una torre suona strano.
7. **`job board` → «bacheca delle missioni»**: termine fissato, usato anche in L210.
8. **`VALUE` invariati** («Mystery delivery to <planet>», «Mystery retrieval from <planet stopovers>»): sono i nomi
   mostrati nella bacheca, e la regola della campagna li vuole inglesi.
9. **`DESCRIPTION` con la resa di L198**: «Consegna un pacco su <destination>. Il pagamento è <payment>.» — nessuna
   variante nuova, per non aprire una seconda convenzione nello stesso file.
10. **`research notes analyzed` → «note di ricerca … analizzate»**: passivo mantenuto, perché il soggetto è il gruppo di
    scienziati che *ha bisogno* dell'analisi, non chi la esegue.

## 2. Un errore mio, corretto prima di chiudere

Avevo scritto che le `DESCRIPTION` formano **due** famiglie; sono **tre**, perché accanto alle sette copie di «Deliver a
package…» ci sono il recupero (unità 44) e il trasporto di scienziati (unità 45). Il controllo ora verifica le
**dimensioni dei gruppi** (`[1, 1, 7]`), non un numero di famiglie che avevo indovinato.

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 45 unità `PENDING`.
- **Nessuna missione giocata**: la composizione dei frammenti è verificata **sul testo**, non osservata a schermo. È il
  limite più serio del lotto: un frammento può essere corretto in isolamento e comporre male.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (26), `verify.py` exit **0** (19) |
