# REPORT — L212 · `deep jobs.txt` (primo lotto)

## 1. Contenuto

Quarantacinque unità che aprono un file nuovo. Il nucleo è la **missione del cubo misterioso**: il giocatore riceve
istruzioni anonime, preleva un cubo nero di due centimetri in un magazzino o in un armadietto, si accorge di essere
osservato, e consegna il cubo nel modo più strano possibile (sul bordo di una strada, dietro una torre di legno, in una
presa d'aria, alla prima mendicante). Poi le prime missioni di lavoro: consegna di un pacco, recupero, trasporto di
scienziati.

## 2. Difficoltà

1. **Il file è fatto di frammenti, non di frasi.** 28 unità `TEXT` sono pezzi che il gioco concatena. «Come da
   istruzioni, tu» + «apri una cassetta di sicurezza» + «in un magazzino anonimo e disabitato» + «e prelevi il pacco
   misterioso.» La resa di ogni pezzo è vincolata dal fatto che deve comporre con gli altri, e i pezzi sono
   intercambiabili (cassetta o armadietto; magazzino o punto di atterraggio).
2. **La composizione si verifica su un marcatore misurabile**: la maiuscola iniziale di ogni frammento. Un frammento
   inglese che inizia minuscolo deve iniziare minuscolo anche in italiano; se no, la concatenazione produce «…disabitato.
   E prelevi…» con un punto e una maiuscola dove il testo deve scorrere.
3. **31 segnaposto su 6 simboli.** Il controllo confronta il multiset **per unità**: un totale corretto può nascondere un
   `<payment>` spostato dall'unità 20 all'unità 28, e il gioco mostrerebbe il pagamento nel posto sbagliato.
4. **8 `VALUE` restano inglesi**: sono i nomi delle missioni nella bacheca. Convivono con 9 `DESCRIPTION` tradotte nello
   stesso lotto — la distinzione va mantenuta senza scivolare.
5. **Le famiglie**: 7 copie di «Mystery delivery to <planet>» e 7 di «Deliver a package to <destination>…». Il controllo
   verifica le **dimensioni dei gruppi** in entrambe le lingue: se una copia divergesse, le dimensioni cambierebbero.
6. **Lo spazio iniziale delle unità 19 e 27** fa parte della stringa: è lì perché la concatenazione lo richiede, e va
   conservato in italiano.

## 3. Numeri osservati

```
unita' 45 · {'TEXT': 28, 'VALUE': 8, 'DESCRIPTION': 9} · tutte PENDING
0 tab · 4 virgolette (19, 27) · 31 segnaposto su 6 simboli, identici per unita'
12 contesti · righe 16/322 · 0 prima · 142 dopo · confine riga 333 (DIALOG, il tipo cambia)
parole 442 -> 454 · rapporto 0.67 - 1.75 (frammenti di due parole)
FAIL totale: 0 (26 controlli) · verify exit 0 (19 controlli) · sha256[:16] d3561b72157dd31c
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26), `verify.py` exit **0** (19) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 45 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna missione giocata**: non ho visto il cubo raccolto né le frasi comporre a schermo. La composizione è
  verificata **sul testo**, non nel runtime: è il limite più serio di questo lotto, e va detto.
- **Restano 142 unità** nel file, di cui 1 `UI_LABEL` non traducibile.
