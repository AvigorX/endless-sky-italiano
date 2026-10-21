# REPORT — L94 · `coalition culture conversations.txt` (secondo lotto)

## 1. Contenuto

Righe 81–133, un solo contesto (`Coalition Folklore: Arach`, 36 unità):

- l'incontro con **Matlub** e l'invito alla serata (1–6);
- il teatro e la platea: sei ordini di balconate, telecamere per la diretta, pubblico misto (7–11);
- **prima opera, «Toccato dalla Luna»**: il minatore, il crollo della miniera, la montagna di metallo e la luna
  (12–15); la scelta se restare o andare (16–17);
- **seconda opera, «Bebliss Balbettante»**: la farsa volgare, la rivalità fra Casate, il pubblico che se ne va
  e la balconata che ride (18–20); la scelta (22–23);
- **terza opera, «Fino alla Morte»**: il giardiniere malato, il fiore avvizzito, la morte in scena (24–27); la
  scelta finale (28–29);
- la **quarta rappresentazione non annunciata**: la figura di legno, i fili staccati, il coro in una lingua
  sconosciuta (30–33); le due domande senza risposta e il congedo di Matlub (34–36).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| sintassi Arach | **ordine marcato italiano** | stessa voce dei Saryd (L93): `apprezzate le belle arti, voi?` |
| `Moonstruck` | **Toccato dalla Luna** | titolo di un'opera: si traduce, non è un nome proprio |
| `Babbling Bebliss` | **Bebliss Balbettante** | `Bebliss` è la Casata (invariata), `babbling` è la parola |
| `'Til Death` | **Fino alla Morte** | titolo-tipo dell'opera tragica |
| `soiree` | **serata** | è un evento culturale, non un «ricevimento» |
| `patrons` | **patroni** | chi paga e frequenta: non «clienti» |
| `House Chamgar` / `House Bebliss` | **Casa Chamgar** / **Casa Bebliss** | forma dominante della campagna |
| `rub two of their legs together` | **strofinano due zampe l'una contro l'altra** | è l'applauso degli Arach |
| `fly tower` | **torre scenica** | termine tecnico del palcoscenico |

## 3. Difficoltà

1. **Due gruppi di ripetizioni** (16/22 e 17/23/29): le scelte del giocatore si ripetono in rami diversi; la
   resa deve essere identica, e il `check.py` verifica i due gruppi separatamente.
2. **Le unità 1 e 7 hanno 6 virgolette**: battute lunghe con citazioni interne. Il conteggio è per unità.
3. **Nessun token** in 64 virgolette: un verde sui token senza il controllo `tok == 0` non direbbe nulla.
4. **La scena muta finale** (31–32, 150 e 183 parole): nessuna battuta, solo descrizione; il rischio è
   appiattire il ritmo — ho tenuto le frasi corte del sorgente.
5. **Il parlato di Matlub** mescola ordine marcato e lessico formale: la resa resta marcata anche quando la
   frase è breve (`Un peccato, è, che…`).

## 4. Numeri osservati

```
unita' 36/36 · tab 35 · virgolette 64 = 64 (6 nelle unita 1 e 7) · token 0 = 0
parole EN 2321 -> IT 2115 · rapporto 0.88 - 1.39
righe 81/133 · file 157 unita · 31 prima / 90 dopo
FAIL totale: 0 (29 controlli) · verify exit 0 (28 controlli)
sha256[:16] 2413e9527696c61a · copertura del file 67/157 (42,7%)
```

## 5. Stato del progetto

```
TOTALE staging: 25054 unita · 800467 EN · 758941 IT
coalition culture conversations.txt: 67/157 (42,7%) · 2 lotti
residuo traducibile (formula state.py): 6876 · misurato: 7440 unità / 175558 parole su 129 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli) **e** `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 36 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il file non è completo**: 90 unità restano; il contratto successivo è `HANDOFF_L95_20261018.md`
  (`Coalition Folklore: Kimek`, righe 134–190), che contiene **tre `UI_LABEL` di salto** da lasciare identiche.
- **Nessuna revisione umana**.
