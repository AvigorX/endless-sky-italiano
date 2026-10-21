# REPORT — L225 · `remnant outfits.txt` (terzo lotto)

## 1. Contenuto

Sette equipaggiamenti, quasi tutti legati all'energia. Le tre celle di alimentazione dei Remnant: la **Millennium Cell**,
radiotermica e quasi un reattore nucleare; la **Epoch Cell**, che converte in elettricità quasi tutto il calore dei
radioisotopi; la **Aeon Cell**, nata dalla diffidenza dei primi ingegneri verso i reattori nucleari umani. Poi il
**Thermoelectric Cooler** — una cella cablata al contrario, che consuma elettricità per raffreddare —, l'**Emergency
Ramscoop** per chi attraversa l'Ember Waste senza le «branchie» dei Remnant, l'**NDR-114 Android** mai concesso in licenza
da un produttore e il **Research Laboratory** che si espande dentro un locale della nave.

## 2. Difficoltà

1. **Secondo lotto di fila senza nulla da copiare**, eppure **i tab dimezzati**: 4 invece di 9. Se avessi ereditato il
   conteggio di L224 il `check.py` sarebbe caduto su un testo corretto — o peggio, avrei aggiunto tab dove non servivano.
   Il numero di struttura si conta sul lotto, non si porta dietro.
2. **La famiglia di «ion» in quattro forme.** `ionization`, `ion dissipation`, `ion resistance`, `ion storm`: quattro
   costrutti diversi, quattro rese diverse, e una sola parola inglese che li lega. Ho misurato la ripetizione: «ionica»
   compare **2** volte, «ionizzazione» **1**, «ioniche» **1**. Ripetere l'aggettivo a ogni menzione avrebbe reso la scheda
   illeggibile.
3. **Le «branchie» fra virgolette.** *their "gills," which are effectively built-in ramscoops*: le virgolette dicono che
   «branchie» è un soprannome, e vanno conservate. Sono le **uniche 2 virgolette** del lotto, nella stessa unità in
   entrambe le lingue.
4. **`run in reverse`** → «funzionare al contrario»: il refrigeratore è una cella al contrario, non un ciclo inverso
   termodinamico da manuale.
5. **`getting stranded`** → «restare bloccata»: a secco di carburante per l'iperspazio, non naufragata.
6. **`boarding actions`** → «azioni di abbordaggio», coerente con «arrembaggi» usato in L205 per `boarders`.
7. **`economic benefit`** → «vantaggio economico», non «beneficio»: è il ritorno che un produttore non vedeva.
8. **Rapporto molto stretto** (1,04–1,15): il testo è tecnico e l'italiano non si allunga, perché `ion` si comprime in
   «ionica» e `cell` resta nel nome inglese.

## 3. Un errore mio, corretto prima di chiudere

Il controllo pretendeva la forma singolare **«tempesta ionica»**, che l'unità 6 non usa: dice «dalle tempeste ioniche» e poi
«dalla tempesta», senza ripetere l'aggettivo — che è esattamente la scelta stilistica che volevo. `FAIL 1`; ora il controllo
verifica le forme presenti **e** il conteggio 2 di «ionica», che è la misura della non-ripetizione.

## 4. Numeri osservati

```
unita' 11 · {'DESCRIPTION': 11} · tutte PENDING
4 tab (unita' 2, 4, 6, 10) · 2 virgolette (unita' 8, le "branchie") · 3 apici EN / 15 IT · 0 segnaposto
7 contesti · righe 581/674 · 25 prima (L223+L224) · 21 dopo · confine riga 675 DESCRIPTION
0 unita' identiche all'inglese, 11 tradotte
parole 455 -> 461 · rapporto 1.04 - 1.15 (media 1.09)
FAIL totale: 0 (25 controlli) · verify exit 0 (18 controlli) · sha256[:16] 66b157150c05ada7
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (18) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 11 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la resa delle «branchie» e delle quattro forme di «ion» è testuale.
- Restano **21 unità** nel file, **10** dopo la riga 864: L226 riparte dalla 675.
