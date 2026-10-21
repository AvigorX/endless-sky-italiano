# REPORT — L217 · `deep jobs.txt` (sesto e ultimo lotto) — **file chiuso 187/187**

## 1. Contenuto

Ventinove unità che chiudono il file: il trasporto dei **consulenti Deep Security**, la **consegna urgente** con scadenza
(`<date>`), le **spedizioni** verso le sedi della **Lionheart Industries** e della **Deep Sky**, e i **trasporti di
corridori su hovercraft** — uno singolo e uno per una squadra di `<passengers>` membri.

## 2. Difficoltà

1. **Il lotto è terminale, quindi cambia il tipo di verifica.** Non un confine, ma l'**invariante di file**: sei finestre
   (45 + 22 + 35 + 25 + 30 + 29 = **186**) più l'`UI_LABEL` della riga 683 devono coprire tutte le **187** unità. Il
   `verify.py` verifica anche che l'`UI_LABEL` **non** compaia in nessuna finestra: se un lotto futuro lo includesse, il
   conteggio tornerebbe per caso e il difetto resterebbe.
2. **56 segnaposto su 9 simboli.** È il record della campagna, e il rischio non è sbagliare il numero totale ma
   **riordinarli**. Con quindici `<destination>` e dodici `<payment>`, un controllo sul solo multiset passerebbe anche se
   un segnaposto fosse finito nella posizione sbagliata: qui il confronto è **per unità e nell'ordine**.
3. **Dodici `VALUE` restano inglesi** anche quando contengono `<planet>`, e le dodici `DESCRIPTION` vanno tradotte nello
   stesso lotto: le due regole convivono in unità adiacenti.
4. **Famiglie**: la mia prima asserzione sulle `VALUE` diceva `[1,1,1,1,2,2]`; il valore vero è `[1,1,1,2,2,5]`, perché
   «Shipment to `<planet>`» compare **cinque** volte (quattro missioni Deep Sky/Lionheart più una). Corretto il controllo,
   non il testo.
5. **Due `DIALOG` gemelli** (10 e 13): stessa scena, stessa resa — verificato.
6. **`<passengers>-member racing team`**: l'inglese usa il segnaposto come aggettivo composto, l'italiano richiede «di
   `<passengers>` membri».

## 3. Numeri osservati

```
unita' 29 · {'VALUE': 12, 'DESCRIPTION': 12, 'DIALOG': 5} · tutte PENDING
0 tab · 2 virgolette (unita' 7) · 0 apici EN / 4 IT · 56 segnaposto su 9 simboli, per unita' e in ordine
12 contesti · righe 935/1234 · 157 tradotte prima · 0 dopo (fine file)
parole 375 -> 398 · rapporto 0.88 - 1.21 (media 1.05)
FAIL totale: 0 (27 controlli) · verify exit 0 (18 controlli) · sha256[:16] 379596a8a8be9b81
FILE CHIUSO: 186 righe tradotte + 1 UI_LABEL = 187/187
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (18) con invariante di file |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 29 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna missione giocata**, nessuna schermata vista.
- **Il file è completo in staging, non nel gioco**: `deep jobs.txt` è tradotto in tutte le 186 unità traducibili e nessuna
  delle sue 187 è approvata.
