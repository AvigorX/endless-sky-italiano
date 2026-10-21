# REPORT — L230 · `korath outfits.txt` (terzo lotto)

## 1. Contenuto

L'**Afterburner (Stellar Class)**, il più grande, con sistemi di raffreddamento attivo alimentati dall'esplosione di
carburante e plasma. I **motori Meteor Class** degli **Esuli**: più grandi, più lenti, per portare armi più grandi o più
carico. Il **Bow Drive** dei Meteor come retropulsore. I cinque **Reverser** — **Asteroid**, **Comet**, **Lunar**,
**Planetary**, **Stellar** — e i primi due **Thruster**.

## 2. Difficoltà

1. **Dieci `VALUE` e sedici `DESCRIPTION`.** È il massimo di nomi in un lotto misto della campagna. Il controllo non si
   limita al totale: verifica che le **10 identiche siano tutti e soli i `VALUE`** e le **16 tradotte tutte e sole le
   `DESCRIPTION`**.
2. **Una frase che attraversa il confine del lotto.** Le unità 1 e 4 ripetono la frase dei postbruciatori già tradotta in
   **L229 unità 10** (riga 300). Ho ripreso la resa **identica** e ho aggiunto un controllo che legge il
   `translation.json` di L229 e confronta: `by[1]['italian'] == prev[300]`. È il primo controllo **inter-lotto** della
   campagna, e nasce da un caso reale: la stessa frase descrive cinque classi di afterburner distribuite su due finestre.
3. **Cinque copie dello stesso paragrafo** (unità 11, 14, 17, 20, 23): cinque equipaggiamenti, una sola resa. Verificate
   come insieme con un solo elemento.
4. **`the Exiles`** → «gli Esuli». È un nome di fazione, ma è anche una parola inglese comune: l'ho tradotto, mentre
   `Kor Efret`, `Mereti` e `Kor Sestor` restano invariati perché non hanno un corrispettivo italiano se non una trascrizione.
   La differenza è dichiarata.
5. **`weapon space`** → «spazio per le armi»: è lo spazio installabile della nave, non un'arma specifica, e la frase
   sullo spazio «da spendere» lo rende chiaro.
6. **`it produces quite a kick`** → «produce un bel calcio»: il tono della scheda è colloquiale e va tenuto.

## 3. Un errore mio, corretto prima di chiudere

Il controllo sulle cinque copie usava `startswith` sul testo italiano, che però **inizia con un tab**: `FAIL 1`. Corretto
con `.strip()` sul lato italiano; il testo non è stato toccato, perché il tab iniziale è struttura del file e non un difetto.

## 4. Numeri osservati

```
unita' 26 · {'DESCRIPTION': 16, 'VALUE': 10} · tutte PENDING
7 tab (unita' 1, 4, 11, 14, 17, 20, 23) · ZERO virgolette · 8 apici EN / 16 IT · 0 segnaposto
11 contesti · righe 319/581 · 35 prima (L228+L229) · 31 dopo · confine riga 596 DESCRIPTION (scheda spezzata)
10 identiche (tutti e soli i VALUE), 16 tradotte (tutte e sole le DESCRIPTION)
coerenza inter-lotto verificata: unita' 1 == L229 riga 300
parole 430 -> 448 · rapporto 1.04 - 1.25 (media 1.09)
FAIL totale: 0 (27 controlli) · verify exit 0 (19 controlli) · sha256[:16] d246b4e6c38a2e78
```

## 5. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (19) |

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 26 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la resa di `reverser` → «retropulsore» è coerente col lessico dei lotti
  precedenti, non osservata nell'interfaccia.
- Restano **31 unità** nel file, **10** dopo la riga 808: L232 sarà terminale e chiuderà `korath outfits.txt` a **92/92**.
