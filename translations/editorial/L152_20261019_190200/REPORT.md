# REPORT — L152 · `coalition jobs.txt` (i Giochi, la vendita del motore, le tre specie)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| Giochi, andata | 1–7 | 1191–1243 | il `TEXT` dei passeggeri e tre livelli `Spectators to <planet>` |
| Giochi, ritorno | 8–14 | 1266–1313 | tre livelli `Passengers to <planet>` con `<origin>` e `<destination>` |
| la vendita | 15–18 | 1335–1350 | `Sell Jump Drive`, la descrizione, l'arrivo degli Heliarch, la battuta dell'Arach, il commiato |
| il diario | 19–21 | 1357–1359 | il permesso ottenuto e le schede di Saryd e Kimek |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Spectators to <planet>` · `Passengers to <planet>` · `Sell Jump Drive` | **identici** | `VALUE` |
| `in time for the Coalition Games (by <date>)` | **in tempo per i Giochi della Coalizione (entro il `<date>`)** | |
| `back to their home world of <destination>` | **sul loro mondo d'origine, `<destination>`** | |
| `an excessively reinforced container` | **un contenitore eccessivamente rinforzato** | |
| `a restricted section of the ring` | **una sezione riservata dell'anello** | |
| `Enormemente prezioso è ogni singolo motore…` | — | inversione dell'Arach conservata |
| `Sold a jump drive…` | **Ho venduto un motore di salto…** | `LOGBOOK` in prima persona |
| `tens of billions` | **decine di miliardi** | |

## 3. Difficoltà

1. **Cambio di tipo**: 3 `MISSION_TEXT` + 3 `LOGBOOK` oltre ai lavori; il `Counter(kind)` li isola e il controllo
   pretende che siano **tradotti**.
2. **La voce dell'Arach è sintatticamente straniera**: va resa con l'inversione, non «normalizzata», o il personaggio
   perde la sua caratteristica.
3. **Due unità con tab** (17, 18) e **una con le virgolette** (17): contate dal sorgente, non a mano.
4. **Errore in corsa**: le chiavi della mappa erano state scritte **con** il tab e il confronto `lstrip('\t')` non le
   trovava; riscritte senza tab, con il costruttore che li riaggiunge.
5. **Indici**: le unità con tab sono la 17 e la 18, non la 9 e la 10 come avevo scritto nel primo tentativo — corretto
   nei tre script dopo averlo **misurato** sul `source.json`.
6. **Gate**: 1,00–1,19.

## 4. Numeri osservati

```
unita' 21/21 · VALUE 7 · DESCRIPTION 7 · MISSION_TEXT 3 · LOGBOOK 3 · TEXT 1 · tutte PENDING
token 34 su 6 simboli: <planet> 10, <payment> 9, <bunks> 6, <date> 3, <origin> 3, <destination> 3
2 unita con tab (17, 18) · 1 unita con 2 virgolette (17) · 13 testi distinti · 8 contesti
parole 527 -> 531 (1.008) · rapporto 1.00 - 1.19
righe 1191/1359 · 115 prima / 61 dopo · confine riga 1360 (ancora LOGBOOK)
FAIL totale: 0 (25 controlli) · verify exit 0 (24 controlli) · sha256[:16] 580b5869e9f95bed
```

## 5. Stato del progetto (dopo L152)

```
TOTALE staging: 27782 unità · 874857 EN · 831187 IT
coalition jobs.txt: 136/197 (69,0%) · 6 lotti
residuo misurato: 4817 unità / 102242 parole su 116 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (24 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 21 unità `PENDING`.
- **Nessuna partita avviata**: la vendita del motore non è stata giocata.
- **Eseguito in batch**: contratto = piano del batch, nessun `HANDOFF_L152` separato (dichiarato qui).
- **Prossimo**: L153 dalla riga 1360 (restano 61 unità, tutte della missione `Heliarchs Buy Jump Drive Job 1`).
