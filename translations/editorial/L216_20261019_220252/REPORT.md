# REPORT — L216 · `deep jobs.txt` (quinto lotto)

## 1. Contenuto

Trenta unità in tre blocchi. Il **dialogo con Julie Gillar** (dodici battute, tredici tab): la richiesta di trasporto
urgente a Valhalla, il datore di lavoro che è «indirettamente» la Deep Security, l'accesso alla lista dei piloti
affidabili. Il **`LOGBOOK`** che riassume l'accordo. Il **viaggio e il congedo**, con la battuta finale che spiega come
trovare altri consulenti bloccati negli spazioporti. E i **due blocchi di frammenti** della missione: come prelevare i
passeggeri (quattro modi), dove trovarli (tre luoghi) e cosa lasciano a bordo (quattro varianti).

## 2. Difficoltà

1. **`<last>` è un cognome e `<passengers>` è un numero.** Il primo non si traduce né si accorda: «capitano `<last>`» è la
   forma che regge un cognome italiano e uno straniero. Il secondo porta l'articolo come in inglese (*the `<passengers>`*),
   e la scelta è dichiarata: se il segnaposto sostituisse un numero nudo, la frase sarebbe rotta in **entrambe** le lingue,
   quindi il rischio è simmetrico e non c'è una resa migliore.
2. **Tre tipi, tre regole.** `MISSION_TEXT` con tab iniziali e dialogo; `LOGBOOK` in prosa senza tab; `TEXT` frammentati
   con composizione. Il lotto è il primo che li tiene tutti insieme, e ogni controllo è specifico per tipo.
3. **Il `LOGBOOK` ha una persona grammaticale mista**, e la mia prima asserzione lo negava. Il testo inglese dice
   *She requested emergency transport from you and showed you how to make yourself available*: apre descrivendo lei e
   poi parla al giocatore. Il controllo ora verifica **entrambe** le cose. Aveva torto l'asserzione.
4. **Le quattro varianti di dropoff sono umoristiche** (stivali sporchi, cravatta sulla maniglia, documenti accartocciati
   buttati nell'inceneritore): vanno rese con lo stesso tono asciutto, senza aggiungere spiegazioni.
5. **`soon notifies`**: qui il gioco dice *soon*, non *immediately* come in L212 e L214. La resa cambia
   («ti avvisa presto»), e il controllo verifica che la differenza non sia stata appiattita.

## 3. Numeri osservati

```
unita' 30 · {'TEXT': 15, 'MISSION_TEXT': 14, 'LOGBOOK': 1} · tutte PENDING
13 tab (1-12, 15) · 26 virgolette (2 x 13) · 15 apici EN / 9 IT
7 segnaposto su 3 simboli, identici per unita' e nello stesso ordine
3 contesti · righe 866/929 · 128 prima (127 + 1 UI_LABEL) · 29 dopo · confine riga 935 (VALUE, sei righe dopo)
parole 439 -> 443 · rapporto 0.74 - 1.44 (media 1.04)
FAIL totale: 0 (25 controlli) · verify exit 0 (19 controlli) · sha256[:16] 193651028d79b6bd
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (19) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 30 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna missione giocata**: l'articolo davanti a `<passengers>` non è mai stato visto sostituito.
- **Restano 29 unità** nel file: L217 lo chiuderà.
