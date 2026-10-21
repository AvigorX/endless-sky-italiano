# REPORT — L57 · `data/gegno/gegno I corroboration.txt` (righe 943–1287)

**Esito: CHIUSO, e chiude il file a 298/298.** `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

| Contesto | Unità | Contenuto |
|---|---|---|
| `Gegno Intervention` 1–23 | 23 | L'hangar occupato, Adrauni che chiude il rapporto, «congedato / esiliato / ripudiato», il commiato |
| `Acquiescence` 24–104 | 81 | Il trasporto del guerriero Vi su Dueyu Eitch: la torre, l'ascensore a gabbia, i tamburi, il tavolo dei modelli, i due interrogatori, i due epiloghi (accettato / respinto) |
| `Gegno Asteroid Mining Prologue` 105–127 | 23 | L'unica stazione spaziale dei Gegno, il pannello dei lavori, l'estrazione di 5 tonnellate di ferro, il pagamento |

È il lotto più **scene-centrico** della serie Gegno: tre luoghi distinti (hangar, torre, stazione) e
nessun combattimento scriptato.

## 2. Le scelte di traduzione che contano

**Il lessico del rifiuto.** `dismissed`, `exiled`, `shunned` non sono sinonimi e il Quarg lo dice
esplicitamente («A more appropriate expression would be exiled, or perhaps shunned?»). In italiano:
**congedato** (unità 8), poi **esiliato / ripudiato** (unità 12). La scala non si appiattisce.

**«Eight revolutions».** Unità 8: «Otto rivoluzioni ti sono state date dai Gegno». Non «anni»: il gioco
non dice quanto duri una rivoluzione gegna, e tradurla con un'unità umana inventerebbe un dato.

**La torre.** «castle-like cities» → «città torreggianti simili a castelli»; «medieval fantasy» →
«antica fantasia medievale»; le «torch-like structures» restano torce, non lampioni: l'architettura è
descritta come antica e il lessico deve restare arcaico.

**Il tavolo dei modelli.** «display grid» → «griglia espositiva»; «models of planets and ships» →
«modelli di pianeti e navi». Il campo semantico è quello di un plastico militare, non di un ologramma.

**La voce del trio.** Parla in lingua Gegno e non viene tradotta. Il narratore riporta solo il **tono**
(«voci basse e tonanti», «un brontolio basso, un po' come un sussurro detto ad alta voce»): la traduzione
non aggiunge contenuto dove il giocatore non capisce.

**`Dueyu Eitch` e `Dueyu Earth?`.** Il primo è il nome del mondo natale (invariato). Il secondo è il
tentativo del giocatore di ripetere «Dueyu» accostandolo a «Earth»: resta ibrido, perché la scena è
costruita su quell'ibrido.

**L'estrazione.** «Mine 5 tons of iron» → «Estrai 5 tonnellate di ferro»; il `VALUE` e la `DESCRIPTION`
usano lo stesso verbo, così l'etichetta della missione e l'obiettivo coincidono.

## 3. Difficoltà incontrate

- **La finestra di export non coincide con la prima unità.** Export 905–1287, ma le righe 905–942 non
  contengono `mission`/`phrase`/`label`/`log`: la prima unità è sulla **943**. Il primo `verify.py`
  asseriva `(905, 1287)` ed era rosso. Il numero corretto è `(943, 1287)`; il controllo è rimasto.
- **`DIALOG` 22/23 identiche a 170/171 di L56.** La resa deve essere letteralmente la stessa: asserito
  confrontando la stringa esatta, non solo la lunghezza.
- **Un duplicato italiano non voluto.** Unità 52 e 58: l'inglese distingue `(Stay where I am.)` da
  `(Remain where I stand.)`, la prima stesura li aveva resi entrambi «(Resta dove sono.)». Corretto:
  58 → «(Rimango dove sono.)». Il controllo `duplicati italiano non spiegati dal sorgente` l'ha trovato.
- **Un secondo duplicato non voluto.** Unità 109 e 162: `prevent me from landing` vs `deny me from
  landing`. Resi entrambi «Non mi impediranno di atterrare?». Corretto: 162 → «Non mi negheranno il
  permesso di atterrare?».
- Entrambi gli errori sono stati trovati **dai controlli**, non dalla rilettura. È il motivo per cui i
  controlli sui duplicati vanno tenuti anche quando sembrano rumore.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 41 controlli · exit 0
             unita 127 · righe 943-1287 · 171 prima / 0 dopo · file 298 · max(line) 1287
             copertura 298/298 su L56+L57
             token 13 / 13 (6 famiglie) · tab 94 / 94 · virgolette 60 / 60
             rapporto 0,57 - 1,47 · duplicati 4 gruppi (8 unita)
             parole 4.974 EN -> 4.514 IT
             sha256 translation.json c3f3b8a9de69cfe1…
```

## 5. Stato del progetto dopo L57

| Voce | Prima (L55) | Dopo L56 | Dopo L57 |
|---|---|---|---|
| File completi | 29 | 29 | **30** |
| Unità in staging | 23.531 | 23.702 | **23.829** |
| `gegno I corroboration.txt` | 0/298 | 171/298 | **298/298** |

Nessuna scrittura su `state.db`: le 127 unità restano `PENDING`.

## 6. Prossimo passo

**L58** apre un **nuovo file**. Il comando di partenza è `next_section.py`, non il numero di riga:
il file corrente è chiuso e proseguire con `export_section.py` sullo stesso path produrrebbe un lotto vuoto.
