# REPORT — L229 · `korath outfits.txt` (secondo lotto)

## 1. Contenuto

Il **Fuel Processor**, nato nella seconda metà della **Guerra Civile Korath** per non restare a secco quando le navi
razziavano gli **Hai**. Il **Command Center** dei **Kor Efret**, installato sulle navi robotiche catturate per scavalcarne
l'IA. Il **Reasoning Node** e il **Control Transceiver**, i sistemi che governano gli automata **Mereti** e **Kor Sestor**.
E i quattro **Afterburner** — **Asteroid**, **Comet**, **Lunar**, **Planetary** — che pompano carburante per l'iperspazio
surriscaldato direttamente nel flusso di plasma, con il rischio di fondere il propulsore.

## 2. Difficoltà

1. **Tre unità quasi identiche.** Le unità 10 e 13 sono lo stesso paragrafo parola per parola; la 7 è la stessa frase con
   un `may` in più (*that **may** nearly melt* contro *that nearly melts*). Ho tradotto una volta e ricavato le altre due,
   verificando con due asserzioni distinte: `t[10] == t[13]` e `t[7] == t[10].replace('che quasi fonde', 'che può quasi
   fondere')`. Se avessi riformulato una delle tre, due classi di afterburner avrebbero descritto lo stesso fenomeno in modi
   diversi.
2. **Il confine spezza una scheda.** L'unità 15 (riga 318) e la riga 319 sono due schede dello stesso `Afterburner
   (Planetary Class)`. Non ho completato la scheda a memoria: il `verify.py` registra che il contesto dell'ultima unità del
   lotto è lo stesso della prima unità esclusa, e la seconda parte si tradurrà in L230.
3. **I tab tornano a 3** dopo lo zero di L228. «Zero tab» era la proprietà di un lotto, non del file.
4. **`hyperdrive`** → «iperguida», termine scelto e dichiarato: `jump drive` resta invariato nei lotti precedenti, e le due
   cose non vanno confuse.
5. **`spartan Command Center`** → «Command Center minimale e spartano»: `spartan` è l'essenzialità, non l'austerità.
6. **`spoof the control signals`** → «falsificare i segnali di controllo»: `spoof` è un termine tecnico preciso.

## 3. Un errore mio, corretto prima di chiudere

Avevo scritto che i quattro `Afterburner` avessero **2 unità ciascuno**. Il valore misurato è **3/3/3/2**: Asteroid, Comet e
Lunar comprendono anche il `VALUE` oltre alle due `DESCRIPTION`, mentre Planetary ha il `VALUE` e **una sola**
`DESCRIPTION` dentro il confine — la seconda è alla riga 319, fuori. Il `check.py` è caduto con `FAIL 1` e ho corretto il
controllo, non il testo. È lo stesso tipo di errore del contratto L220 (le virgolette «2 × 17»): una deduzione al posto di
una misura.

## 4. Numeri osservati

```
unita' 15 · {'DESCRIPTION': 11, 'VALUE': 4} · tutte PENDING
3 tab (unita' 7, 10, 13) · ZERO virgolette · 4 apici EN / 12 IT · 0 segnaposto
8 contesti · righe 208/318 · 20 prima (L228) · 57 dopo · confine riga 319 DESCRIPTION (scheda spezzata)
4 identiche (tutti e soli i VALUE), 11 tradotte (tutte e sole le DESCRIPTION)
parole 431 -> 442 · rapporto 1.00 - 1.21 (media 1.10)
FAIL totale: 0 (27 controlli) · verify exit 0 (18 controlli) · sha256[:16] b85fa00ea11fb613
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (18) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la resa di «iperguida» e dei postbruciatori è testuale.
- Restano **57 unità** nel file, **31** dopo la riga 581: L230 riparte dalla 319, dove c'è la seconda scheda
  dell'`Afterburner (Planetary Class)`.
