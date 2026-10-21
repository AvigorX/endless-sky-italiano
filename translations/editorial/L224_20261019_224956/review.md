# REVIEW — L224 · `remnant outfits.txt` (secondo lotto)

Coppie EN→IT rilette in `translation.json` (`bee38f3d2fc80881…`). Tutte le 13 unità sono **`PENDING`**.

## 1. La riga di servizio, tre volte identica

| unità | equipaggiamento | italiano |
|---|---|---|
| 1 | `EMP Torpedo Bay` | «Le munizioni per quest'arma possono essere rifornite presso qualsiasi negozio di equipaggiamenti.» |
| 5 | `Teciimach Bay` | **identica** |
| 8 | `Teciimach Pod` | **identica** |

Tre equipaggiamenti dello stesso sistema d'arma, una sola riga di servizio. Le ho scritte una volta e confrontate con `==`
su tutti e tre i valori: una divergenza qui sarebbe invisibile a chi legge una scheda sola.

## 2. Decisioni di resa

1. **`the newest revision of the EMP Torpedo Bay, the "Teciimach,"`** → «L'ultima revisione dell'EMP Torpedo Bay, il
   "Teciimach",». I nomi restano inglesi; le virgolette attorno al nome restano dritte, come nel sorgente (2 in tutto il
   lotto).
2. **`alters each torpedoes' energy to ignore allies`** → «modifica l'energia di ogni siluro perché ignori gli alleati». Il
   refuso del sorgente (`torpedoes'` invece di `torpedo's`) **non si corregge**: si traduce per senso.
3. **`without risk of ionizing yourself or the rest of your fleet`** → «senza rischiare di ionizzare te stesso o il resto
   della tua flotta».
4. **`a clip that is a third larger`** → «un caricatore più grande di un terzo».
5. **`on-the-spot assembly techniques`** → «tecniche di assemblaggio in loco»; **`pods sacrifice multiple assembly
   systems`** → «i pod sacrificano diversi sistemi di assemblaggio».
6. **`hit-and-run tactics`** → «tattiche mordi e fuggi»; **`all ready torpedoes at once instead of in sequence`** → «tutti i
   siluri pronti in una volta invece che in sequenza».
7. **`maximizing the ion damage dealt in a single moment`** → «massimizzando i danni da ionizzazione inflitti in un solo
   momento»: `ion damage` è un tipo di danno del gioco, reso con «danni da ionizzazione».
8. **`an anomalous region subject to forces that defy conventional physics`** → «una regione anomala soggetta a forze che
   sfidano la fisica convenzionale».
9. **Il trattino del sorgente** (`space - even around a nebula`) resta un **trattino semplice fra spazi**, non un em dash:
   fedeltà alla punteggiatura del file.
10. **`is making micro-tears in the fabric of space-time, then cauterizing them together again`** → «produce micro-strappi
    nella trama dello spazio-tempo e poi li ricuce insieme».
11. **`'both.'`** → «'entrambe le cose'»: apici singoli, e la risposta resta ellittica — il lettore deve capire da solo che
    si riferisce a *strappare* e *piangere*.
12. **`Should not the Ember Waste cry…`** → «Non dovrebbe forse l'Ember Waste piangere…»: l'inversione retorica si conserva,
    perché è la chiusura del gioco di parole.
13. **`special hardpoints`** → «punti d'attacco speciali»; **`distribute them directly on an as-needed basis`** → «le
    distribuiscono direttamente in base al bisogno».
14. **`mined on the Remnant planet Viminal`** → «estratti sul pianeta dei Remnant Viminal»: `Remnant` resta, `Viminal` è un
    toponimo.
15. **`quicker dissipation of ionization`** → «più rapida dissipazione della ionizzazione»; **`ion storms`** → «tempeste
    ioniche»; **`in the Waste`** → «nella Waste».

## 3. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 13 unità `PENDING`.
- **Nessun equipaggiamento visto nel gioco**: né il Teciimach né l'Ember Tear sono stati osservati in partita, quindi la resa
  di «ionizzare» e «micro-strappi» resta una scelta testuale.
- **Nessuna correzione al refuso** `torpedoes'` del sorgente: dichiarato, non toccato.
- **Nessuna revisione umana**.

## 4. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |
