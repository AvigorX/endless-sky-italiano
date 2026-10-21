# REPORT — L197 · `hai jobs.txt` (secondo lotto)

## 1. Contenuto

Il lotto passa dal listino «vacanze» al listino **ordini e trasporti**: tre tipi di ordine speciale Hai, quattro
taglie di scorta verso lo spazio umano, tre taglie di trasporto passeggeri, due famiglie in trasloco e due
mestieri in cerca di lavoro. 36 unità, 15 contesti, **nove `DIALOG`** e nessun `TEXT`.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| consegna residua | 1 | 492 | chiude il filo aperto dal confine di L196 |
| ordini speciali | 2–13 | 516–601 | «Un Hai della buona società…», «Un Hai gourmet…», «Uno smanettatore Hai…» |
| scorte | 14–21 | 606–756 | quattro taglie, una sola resa |
| passeggeri | 22–27 | 811–862 | `Porta <fare> su <destination>` |
| famiglie | 28–33 | 883–936 | trasloco e sbarco |
| minatori/contadini | 34–36 | 941–967 | stessa cornice, mestiere diverso |

## 2. Difficoltà

1. **`DIALOG` al posto di `TEXT`**: nove unità con contesto proprio, tradotte tutte; il tipo si misura dall'export, non si assume dal lotto precedente.
2. **`<planet stopovers>` contiene uno spazio**: il confronto dei segnaposto usa `<[^<>]+>` e il **multiset per unità** (81 su 11 simboli).
3. **Coerenza con lo staging esistente**: due stringhe erano già tradotte. Il controllo `prior_italians()` legge i `translation.json` degli altri lotti e pretende la **stessa resa** — non una variante «migliore».
4. **Un'asserzione sbagliata, corretta**: il primo `check.py` confrontava tutto ciò che segue `<planet>` nelle tre unità «ordine speciale», ma la parte condivisa è solo l'ultima frase. Ha fallito con `FAIL 1`; è stato corretto **il controllo** (coda condivisa + tre prefissi distinti), non il testo.
5. **Nomi e oggetti**: `smanettatore` per *tinkerer*, `della buona società` per *socialite*, `spazioporto`, `bancali di carico`, `scorta`, `il <commodity>` come nei lotti precedenti.

## 3. Numeri osservati

```
unita' 36 · {'VALUE': 12, 'DESCRIPTION': 15, 'DIALOG': 9} · tutte PENDING
0 tab · 0 virgolette · 0 apici · 81 segnaposto su 11 simboli
15 contesti · righe 492/967 · 39 unita' prima · 100 dopo · confine riga 988 (DIALOG)
parole 488 -> 462 · rapporto 0.86 - 1.14 (media 1.02)
FAIL totale: 0 (29 controlli) · verify exit 0 (19 controlli) · sha256[:16] 0ff30f8bb315b0ad
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto (compreso il `FAIL 1` iniziale) |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (19 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 36 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file non è chiuso**: 100 unità dopo la riga 967, tre finestre (L198…L200).
