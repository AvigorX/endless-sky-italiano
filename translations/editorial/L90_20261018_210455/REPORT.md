# REPORT — L90 · `data/successors/successor culture conversations.txt`

## 1. Contenuto

Sei conversazioni di cultura dei Successori, righe 23–142:

- **First Contact Exploration: Kua-Oa-Aava** (1): l'adattatore di carburante stampato sul momento da una sfera
  di metallo morfico, dopo che gli ufficiali hanno scansionato lo scafo della `<ship>`.
- **… Raaqa-Kvelq-Ryuit** (2–10): il boccone di cibo offerto su uno stecco. Rami: prendere, rifiutare,
  assaggiare (il cibo è «duro, sa di pesce»), nascondere.
- **… Iyra-Ijasa-Iret** (11): lo spazioporto sott'acqua e il salotto a più livelli.
- **… Mavra-Sol-Kvel** (12–17): la sfera di dati offerta oltre le barriere, e la vasca con la salamandra.
- **Buskers** (18–34): il terzetto che suona nella vasca, il canto tradotto a frammenti, l'applauso o il
  tentativo di ronzare.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `morphic metal sphere` | **sfera di metallo morfico** | `morphic` è la proprietà, non un colore |
| `data-sphere` | **sfera di dati** | distinta dalla sfera morfica del carburante |
| `(Take it.)` (3, 13) | **`(Prendilo.)` / `(Prendila.)`** | l'oggetto cambia genere: bastone / sfera |
| `trills warmly` | **trilla con calore** | `trill` è il verso, non un suono qualsiasi |
| `undulate` | **ondulano** | descrizione del moto dei Successori, ricorrente |
| `dull, low hum` | **cupo ronzio basso** | `dull` è timbrico |
| `lilting melody` | **melodia cadenzata** | non «allegra»: `lilting` è il ritmo |
| `rapturously` | **estatico** | non «rapito»: il movimento è fisico |
| `splittingly high note` | **nota acutissima** | `splitting` è intensità |

## 3. Difficoltà

1. **Finestra ridotta**: il contratto prevedeva 76 unità; ne ho fatte 34. Dichiarato nello `STATO.md` e qui.
2. **Tre token `<ship>`** in tre unità diverse: riprodotti identici e confrontati uno per uno.
3. **28 tab** su 34 unità: le scelte del giocatore e le continuazioni sono tutte indentate.
4. **Due coppie di inglese identico**: `(Take it.)` alle unità 3 e 13 (reso diverso per il genere dell'oggetto)
   e `(Return to my ship.)` alle 26 e 31 (reso identico). Entrambe asserite.
5. **Un errore mio nel `check.py`**: il divieto assoluto di duplicati italiani era sbagliato per queste due
   coppie; sostituito con i due controlli specifici dopo due iterazioni (confronto a `[:-1]`, poi `[:-3]` per
   il `.)` finale).

## 4. Numeri osservati

```
unita' 34/34 · tab 28 · virgolette 2 = 2 · token 3 = 3 (<ship>)
parole EN 1098 -> IT 1014 · rapporto 0.77 - 1.70
righe 23/142 · file 114 unita · max(line) 351 · 0 prima / 80 dopo
FAIL totale: 0 (27 controlli) · verify exit 0 (26 controlli)
sha256[:16] 45fd22aca9b71868
```

## 5. Stato del progetto

```
TOTALE staging: 24907 unita · 793437 EN · 752351 IT
successor culture conversations.txt: 34/114 (29,8%) · 1098 EN -> 1014 IT · 1 lotto
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli) **e** `verify.py` exit **0** (26 controlli) |

## 7. Non ancora fatto (dichiarato)

- **`review.md` assente** per questo lotto.
- **`HANDOFF_L91` non scritto**: la finestra residua del file (unità 35–76) non ha contratto.
- **Checkpoint di progetto non riallineati** ai totali di L90 (`CHECKPOINT_SESSIONE`, `CHECKPOINT_EDITORIALE`,
  `CHECKPOINT_AGENTE_SESSIONE`): fermano a L89, 24.873 unità.
