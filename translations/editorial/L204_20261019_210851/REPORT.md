# REPORT — L204 · `hai outfits.txt` (quarto lotto)

## 1. Contenuto

Diciannove unità: una **scala di cinque pacchi batterie** (dal più piccolo al più grande), **due generatori**
(fusione miniaturizzata e fissione), **due reattori** (Pebble Core, Sand Cell) e **tre descrizioni dei motori
atomici Hai**, con il set `"Baellie"` che nasce perché il Flea non poteva portare il `"Basrem"`.

## 2. Difficoltà

1. **Virgolette dentro i nomi.** Il lotto ha 6 virgolette e nessuna è punteggiatura: 2 in un `VALUE`
   (`"Baellie" Atomic Engines`), 4 nel testo dell'unità 16, dove la frase cita due nomi di prodotto. Copiate alla
   lettera e confrontate unità per unità.
2. **Un errore d'asserzione mio, non del testo.** Avevo scritto `pacco batterie == 5`; il valore reale è **4**, perché
   l'unità 10 dice *battery model* e non *battery pack*. Il controllo ora lega i due conteggi:
   `IT_ALL.count('pacco batterie') == 4 == EN_ALL.count('battery pack')`. È il tipo di asserzione che preferisco:
   se una delle due lingue cambia, il controllo cade.
3. **Le cinque batterie sono una progressione**, non cinque testi indipendenti: il controllo verifica che ogni unità
   porti il proprio gradino di capacità («più piccolo», «più che tripla», «taglia media», «grandi dimensioni»,
   «modello di batteria più grande»).
4. **Gli apici crescono da 2 a 6** per elisione italiana (`dell'energia`, `l'energia`, `l'impronta` due volte,
   `All'insaputa`, `un'efficienza`): legati alle unità, non al totale.

## 3. Numeri osservati

```
unita' 19 · {'DESCRIPTION': 13, 'VALUE': 6} · tutte PENDING
0 tab · 6 virgolette (unita' 15, 16) · 2 apici EN / 6 IT · ZERO segnaposto
13 contesti · righe 603/788 · 33 prima · 13 dopo · confine riga 805 (DESCRIPTION, virgolette nel contesto)
parole 441 -> 454 · rapporto 0.95 - 1.24 (media 1.07)
FAIL totale: 0 (22 controlli) · verify exit 0 (18 controlli) · sha256[:16] 12342441647f81f7
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (22), `verify.py` exit **0** (18) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 19 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna revisione umana**.
- **Il file non è chiuso a questo punto**: restano 13 unità (chiuse da L205).
