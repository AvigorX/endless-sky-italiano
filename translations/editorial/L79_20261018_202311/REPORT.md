# REPORT — L79 · `data/successors/successor side missions.txt`

## 1. Cosa contiene il lotto

**Lo spazioporto sbagliato** (1–5). Squallido, affollato, scomodo; i Successori sono sporchi e infelici, e le
poche navi atterrate portano una **tonalità di rosso più scura**. Il capitano può chiedere informazioni.

**Il reietto** (6–15). Un membro d'equipaggio coperto di bruciature risponde con voce «più bassa e più cupa»,
la pelle che cambia a ogni parola: riconosce l'alieno «portato in giro» dalle Casate — «'ospite nobile' o
'furfante volubile', a seconda di chi ti parla». Accusa il capitano di essere un altro **stolto indolente**
ingannato da promesse di ricchezza, e indica la folla: «Alle Casate non importa nulla di te, di me, o di
nessuno di loro».

**Chi sono** (16–29). Il giocatore può reagire («Non penso di essere uno stolto») e il Successore rincara:
allora lo sei due volte, perché il tuo tempo qui è breve e i tuoi pensieri sono «come quelli di un bambino»;
tieniti pure gli amici, ma ricorda le sue parole «quando il loro pugnale ti niderà nella schiena». Poi la
spiegazione: sono i **reietti delle Casate Nuove**, rimasti in questo «luogo intermedio» quando l'impero
cadde, mentre gli altri avevano ricchezze per andarsene. «Mille anni, e ancora ci dipingono con il loro
disprezzo». E infine la definizione delle **Casate del Popolo**: «non stanno dalla parte dei ricchi e di chi
ha sangue nobile, ma degli eredi veri e onesti di ciò che è stato».

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `Old Houses` / `New Houses` / `People's Houses` | **Vecchie Casate** / **Nuove Casate** / **Casate del Popolo** | tre istituzioni in opposizione, tre forme fisse |
| `outcasts` | **reietti** | più duro di «esclusi», come il tono |
| `indolent fool` / `buried fool` | **stolto indolente** / **stolto sepolto** | due insulti distinti; il secondo torna identico in 23/28 |
| `'noble guest'` / `'flighty knave'` | **'ospite nobile'** / **'furfante volubile'** | le virgolette semplici inglesi restano virgolette semplici |
| `toe the line` | **startene in riga** | idioma reso, non calcato |
| `their dagger nests` | **il loro pugnale ti niderà nella schiena** | metafora cruda, mantenuta |
| `dingy` | **squallido** | non «sporco»: è l'ambiente, non le persone |

## 3. Difficoltà incontrate

1. **Tre virgolette dispari** (10, 22, 27), tutte **aperture** senza chiusura: il `verify.py` controlla
   l'insieme, la direzione **e** che le altre unità con virgolette siano bilanciate.
2. **Tre gruppi di duplicati** (22/27, 23/28, 18/24/29): le stesse battute in rami diversi. Resa identica
   obbligatoria; il controllo rifiuta solo le ripetizioni non spiegate dal sorgente.
3. **Zero token**: la parità è `0 = 0` e va asserita — ometterla sarebbe un'omissione, non una semplificazione.
4. **Sette assenze di tipo** in un lotto di sole `MISSION_TEXT`: ognuna dichiarata separatamente.
5. **Un inglese molto contratto e volgare** (`vis'tor`, `t'which`, `'round`): reso con italiano corrente,
   senza arcaismi finti ma senza addolcire.

## 4. Numeri osservati (output letto)

```
unita' 29/29 · copertura 29/29
tab IT 28 / EN 28 · virgolette IT 33 / EN 33 · dispari (10, 22, 27)
token IT 0 / EN 0
rapporto IT/EN 0.75 - 1.25
parole EN 620 -> IT 611
prima/ultima riga del segmento: 336/381
duplicati inglese: 3 gruppi (7 unita)
FAIL totale: 0    (32 controlli)
verify.py exit 0  (36 controlli)
sha256[:16] 54af11093d844256
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24739 unita · 788809 EN · 747692 IT
successor side missions.txt: 145/164 (88,4%) · 3638 EN -> 3500 IT · 3 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli) **e** `verify.py` exit **0** (36 controlli) |
