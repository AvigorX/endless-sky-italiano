# REPORT — L213 · `deep jobs.txt` (secondo lotto)

## 1. Contenuto

Ventidue unità su tre filoni: **scienza** (trasporto di scienziati, dipartimento di scienziati, scorta a una nave
scientifica), **conferenza** (registrazione per chi non può partecipare) e **pacco sicuro** (prelievo con quattro
varianti di banco, luogo e aspetto).

## 2. Difficoltà

1. **Entrano i `DIALOG`.** Sette unità di prosa parlata di missione. La regola del registro Saryd **non si applica**: non
   sono voci della Coalizione, e applicarla «per abitudine» avrebbe prodotto inversioni fuori posto. Il controllo
   verifica l'assenza dei marcatori della Coalizione in quei testi: è un'asserzione negativa, non un'impressione.
2. **`<npc>` è un segnaposto che cambia funzione sintattica.** Quattro occorrenze: soggetto con articolo («La `<npc>`
   atterra accanto a te»), genitivo («il capitano della `<npc>`»), soggetto di subordinata («finché la `<npc>` non avrà
   visitato»). L'italiano richiede l'articolo e la preposizione articolata, che il segnaposto non porta con sé: la resa
   deve metterli **fuori** dal segnaposto.
3. **Il blocco di frammenti** (14–22) ha **quattro gruppi di alternative**: due banchi (bagagli, sicurezza), due luoghi
   (zona tranquilla, punto di atterraggio), tre pacchi (cassa su carrello, scatola con combinazione, pacco morbido che
   scricchiola). Ogni alternativa deve restare distinta e intercambiabile.
4. **Coerenza cross-lot verificata**: «la struttura su `<stopovers>`» deve coincidere con l'unità 45 di L212, e «Il
   pagamento è `<payment>`» con la resa di L198. Sono asserzioni, non buone intenzioni.
5. **Il confine è a quattro righe** (453 → 457) e dello **stesso tipo** (`TEXT`): un controllo che assumesse «il tipo
   cambia al confine» sarebbe passato per caso. Il `verify.py` misura riga, tipo e contesto.

## 3. Numeri osservati

```
unita' 22 · {'TEXT': 12, 'DIALOG': 7, 'DESCRIPTION': 3} · tutte PENDING
0 tab · 0 virgolette · 3 apici EN / 9 IT · 24 segnaposto su 7 simboli, identici per unita'
6 contesti · righe 333/453 · 45 prima · 120 dopo · confine riga 457 (stesso tipo, contesto diverso)
parole 436 -> 413 · rapporto 0.67 - 1.52 (il minimo e' «Tu» contro «You»)
FAIL totale: 0 (25 controlli) · verify exit 0 (18 controlli) · sha256[:16] a1c19c89ae374d9f
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (18) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 22 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna missione giocata**: la composizione dei frammenti è verificata sul testo, non a schermo.
- **Restano 120 unità** nel file, di cui 1 `UI_LABEL`; il prossimo lotto entra nei `MISSION_TEXT` e nei `LOGBOOK`.
