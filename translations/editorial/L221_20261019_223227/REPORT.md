# REPORT — L221 · `successor ships.txt` (quarto lotto)

## 1. Contenuto

Tre navi dei Successori: la **Seiitej**, il vascello che le Alte Case usano per piccoli carichi e passeggeri e che, grazie a
velocità e interni flessibili, fa anche da pattugliatore; la **Stolsaqra**, il primo tentativo dei Successori di costruire un
intercettore così piccolo — compatto, potente, e descritto da due schede che si sovrappongono; la **Veusade**, progettata per
un solo scopo: portare otto cannoni a trascinamento a ridosso dello scafo nemico.

## 2. Difficoltà

1. **Tre formule condivise fra due schede.** Le unità 15 e 17 descrivono la stessa Stolsaqra e ripetono *sports a surprising
   amount of firepower for a ship of its size* e *plagued with power and propulsion issues*; la 17 ripete con la 16 anche
   *albeit with significantly downgraded systems compared to the military-exclusive model*. Le ho rese **una volta sola** e
   riusate identiche — altrimenti la stessa nave avrebbe due schede che si contraddicono nei dettagli tecnici.
2. **Tre tab, tutti in `DESCRIPTION`.** In L220 il tab era in un'unità; qui in tre (7, 16, 24). Contarli per unità e in
   entrambe le lingue, non dedurli dal tipo.
3. **Le 30 virgolette sono tutte nelle `TEXT`.** In L220 due erano in prosa: la regola «zero fuori dalle `TEXT`» sarebbe
   stata vera qui e falsa là. Ho misurato prima di scriverla.
4. **`drag cannon` non è un nome nel database.** Ho cercato: nessun equipaggiamento chiamato così, nessuna voce di glossario.
   Il termine vive solo in questa prosa, quindi l'ho reso — «cannoni a trascinamento» — invece di lasciarlo in inglese come un
   nome di prodotto che non è.
5. **`a challenge` / `a deathtrap`.** L'ironia sta nell'opposizione: i piloti ambiziosi la chiamano «una sfida», i capitani
   prudenti «una trappola mortale». Se si appiattisce uno dei due, la battuta sparisce.
6. **`military-exclusive model`** → «modello riservato ai militari»: non è un'esclusiva commerciale, è la versione che il
   pubblico non può comprare.

## 3. Numeri osservati

```
unita' 24 · {'TEXT': 15, 'DESCRIPTION': 7, 'VALUE': 2} · tutte PENDING
3 tab (unita' 7, 16, 24, tutte DESCRIPTION) · 30 virgolette (2 x 15 TEXT, nessuna in prosa) · 5 apici EN / 2 IT
3 contesti: Stolsaqra 10, Seiitej 7, Veusade 7 · 0 segnaposto
righe 904/1137 · 96 prima (L218+L219+L220) · 26 dopo · confine riga 1141 DESCRIPTION
17 unita' identiche all'inglese, 7 tradotte (le DESCRIPTION); tre formule condivise verificate
parole 451 -> 481 · rapporto 0.99 - 1.21 (media 1.03)
FAIL totale: 0 (28 controlli) · verify exit 0 (18 controlli) · sha256[:16] b7a2199bbf3b9e42
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json` generato dal sorgente, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 24 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna nave vista nel gioco**: «cannoni a trascinamento» è una resa coerente col testo, non verificata nel runtime.
- Restano **26 unità** nel file, tutte dopo la riga 1137: **L222 lo chiuderà**.
