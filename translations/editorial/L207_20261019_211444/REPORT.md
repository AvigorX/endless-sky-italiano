# REPORT — L207 · `coalition news.txt` (secondo lotto)

## 1. Contenuto

Diciassette voci, **tutte citazioni** (34 virgolette, 2 per unità) e **tutte in registro Saryd**: un agente Heliarch,
un candidato Heliarch, un turista Arach, un turista Kimek, un turista Saryd e un ricercatore della Coalizione.

## 2. Difficoltà

1. **Il registro si applica a tutto il lotto, senza eccezioni di tipo.** In L206 due unità erano narrazione e restavano
   in italiano naturale; qui non ce n'è nessuna, e la regola vale per 17 testi su 17.
2. **La cadenza deve reggere su registri diversi**: comico (il turista che si lamenta delle strade), burocratico (il
   candidato e le sue prove), turistico (la cucina, i panorami), scientifico (il campione di sangue). La sintassi è la
   stessa; cambia il lessico, e va cambiato davvero.
3. **L'inversione non si aggiunge dove il sorgente non la mette.** Tre unità (12, 13, 16) chiudono in ordine normale
   perché in inglese chiudono così. Il controllo verifica **l'insieme esatto** delle 14 unità con chiusura verbale e
   **le tre** che non ce l'hanno: se in futuro qualcuno «corregge» una di quelle tre, il test cade.
4. **Due convenzioni che si toccano**: l'unità 14 è una richiesta cortese (*«would you mind?»*), ma la campagna usa il
   «tu» come registro unico. Ho scelto «ti dispiacerebbe» e l'ho dichiarato; è l'unico punto del lotto in cui il registro
   Saryd incontra la politica di registro del progetto.
5. **`consul Aulori`**: prestito latino, non «console». Il controllo esclude esplicitamente la forma sbagliata.

## 3. Numeri osservati

```
unita' 17 · {'NEWS': 17} · tutte PENDING
0 tab · 34 virgolette (2 per unita', tutte citate) · 4 apici EN / 4 IT · ZERO segnaposto
6 contesti · righe 95/176 · 20 prima · 75 dopo · confine riga 177 (stesso contesto)
parole 432 -> 407 · rapporto 0.91 - 1.22 (media 1.07)
registro: 14 unita' su 17 chiudono con un verbo; 12, 13, 16 no (come nel sorgente)
FAIL totale: 0 (23 controlli) · verify exit 0 (17 controlli) · sha256[:16] af8d352da08f8841
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (23), `verify.py` exit **0** (17) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna schermata vista**, **nessuna revisione umana**: la resa del registro Saryd resta una **proposta**.
- **75 unità residue** in questo file, tutte `NEWS`, quindi tutte soggette alla stessa regola.
