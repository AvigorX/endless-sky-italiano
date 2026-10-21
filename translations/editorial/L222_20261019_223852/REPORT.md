# REPORT — L222 · `successor ships.txt` (quinto e ultimo lotto) — **file chiuso 146/146**

## 1. Contenuto

Tre schede: la **Veusade** (feritoie per le armi, capacità appena sufficiente a saturare i punti d'attacco con cannoni a
trascinamento, impiegata come unità ausiliaria o di polizia), la **Vujlet** (nave da guerra leggera prodotta in serie dalle
Alte Case, nata come ricognitore furtivo della **Casa Kaatrij**, con due schede quasi identiche) e la **Vujlet-Usaqri** (la
variante con occultamento integrato nello scafo e rete di scudi di capacità superiore).

## 2. Difficoltà

1. **Le due schede della Vujlet sono quasi lo stesso testo.** La 14 è la 12 senza l'apertura participiale (*Navigating the
   stars with the grace of a flitting bird*), e nel resto differisce per **due virgole**: *short-ranged **and** relatively
   vulnerable* contro *short-ranged**,** relatively vulnerable*. Ho tradotto una volta e conservato la differenza
   («a corto raggio **e** relativamente vulnerabili» / «a corto raggio**,** relativamente vulnerabili»): il `check.py` e il
   `verify.py` verificano **entrambe** le cose — il testo condiviso identico **e** la punteggiatura diversa. Se avessi
   normalizzato, la seconda scheda avrebbe perso l'unica differenza che ha.
2. **Una formula che torna da L221.** L'unità 24 di L221 diceva *such a narrowly-focused design makes these vessels ill-suited
   for multipurpose use…*; qui la stessa frase descrive la Veusade. La resa è la stessa, con *catch* → «raggiungere» dove
   L221 diceva *intercept* → «intercettare». Due navi diverse, stessa formula: la formula resta una.
3. **`New Houses`** → **Nuove Case**: un terzo raggruppamento, dopo le Alte Case e le Case del Popolo. Se avessi reso
   «nuove case» in minuscolo, sarebbe sembrato un errore di battitura.
4. **`eighteen hundred years`** → «milleottocento anni». È il tipo di numero che si sbaglia per distrazione (diciottomila).
5. **`cloak` / `cloaking` / `stealth`**: tre parole inglesi per tre concetti vicini. Ho tenuto la distinzione —
   «occultamento» per la tecnologia, «ricognizione furtiva» per il ruolo, «equipaggiamento occultante» per il materiale —
   invece di appiattirle tutte su «furtivo».
6. **`shield grid`** → «rete di scudi», la stessa resa di L219–L221: la coerenza fra file si mantiene sulle unità di
   equipaggiamento condivise.

## 3. Numeri osservati

```
unita' 26 · {'TEXT': 18, 'DESCRIPTION': 6, 'VALUE': 2} · tutte PENDING
2 tab (unita' 13, 26, entrambe DESCRIPTION) · 36 virgolette (2 x 18 TEXT, nessuna in prosa) · 5 apici EN / 8 IT
3 contesti: Vujlet 13, Vujlet-Usaqri 12, Veusade 1 · 0 segnaposto
righe 1141/1338 · 120 prima (L218-L221) · 0 dopo (fine file)
20 unita' identiche all'inglese, 6 tradotte (le DESCRIPTION); coerenze 12/14 e con L221 verificate
parole 431 -> 472 · rapporto 1.00 - 1.21 (media 1.03)
FAIL totale: 0 (29 controlli) · verify exit 0 (20 controlli) · sha256[:16] 30ae0dcd3ae347d4
FILE CHIUSO: 45 + 25 + 26 + 24 + 26 = 146/146, nessun UI_LABEL nel file
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json` generato dal sorgente, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29), `verify.py` exit **0** (20) con invariante di file |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 26 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna nave vista nel gioco**, nessuna schermata di allestimento aperta.
- **Il file è completo in staging, non nel gioco**: `successor ships.txt` è tradotto in tutte le 146 unità e nessuna è
  approvata.
