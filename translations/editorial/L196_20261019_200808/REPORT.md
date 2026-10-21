# REPORT — L196 · `hai jobs.txt` (primo lotto, apre il file)

## 1. Contenuto

Sei famiglie di lavori Hai in 39 unità: si torna al registro da **listino**, dopo cinque lotti di narrazione
(`bunrodea missions.txt`). Il file si chiuderà in cinque finestre (L196…L200).

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Human Vacation | 1–4 | 15–42 | «Questo umano vuole trascorrere le vacanze sul mondo Hai di…» |
| Hai Vacation | 5–12 | 63–141 | quattro lavori; il singolo usa «strano mondo Hai», i gruppi lo ripetono |
| Wealthy Hai | 13–16 | 165–196 | «Questa ricca famiglia di `<bunks>` Hai pagherà…» |
| Hai Festival | 17–23 | 223–299 | il dialogo del pagamento (festival) e tre lavori con `<tons>` di rifornimenti |
| Unfettered Aid | 24–34 | 333–410 | cinque battute (`tributo`, `consanguinei`, `fratelli e sorelle`) e tre consegne |
| Delivery to Human Space | 35–39 | 437–489 | due consegne nello spazio umano; il nome del terzo lavoro chiude il lotto |

## 2. Difficoltà

1. **La convenzione sui `VALUE` si misura, non si assume**: 300+ occorrenze identiche nei lotti L117…L195 contro le traduzioni dei lotti L16–L18. Il nome del lavoro resta inglese.
2. **`TEXT` = prosa traducibile**: i tre `TEXT` del lotto sono dialoghi. La regola scritta «`VALUE` **e** `TEXT` restano inglesi» non regge contro i dati (§5).
3. **Nove simboli di segnaposto in 72 occorrenze**: il confronto è per **multiset di unità**; un totale globale passerebbe anche con due simboli scambiati.
4. **Quattro famiglie di ripetizioni** verificate come relazioni, non come uguaglianza globale: 8/10/12, 19/21/23, 30/32/34, 36/38.
5. **Punteggiatura del dialogo**: le virgolette inglesi (6) si conservano uguali in italiano dentro i delimitatori backtick; il punto e virgola delle due aperture diventa `:` dove l'italiano lo richiede (`ti dice:`).

## 3. Numeri osservati

```
unita' 39 · {'VALUE': 17, 'DESCRIPTION': 16, 'TEXT': 6} · tutte PENDING
0 tab · 6 virgolette EN = 6 IT · 1 apice EN / 3 IT · 72 segnaposto
20 contesti · righe 15/489 · 0 unita' prima della 15 · 136 dopo la 489
parole 499 -> 466 · rapporto 0.91 - 1.12 (media 1.02)
FAIL totale: 0 (26 controlli) · verify exit 0 (19 controlli) · sha256[:16] e69389281fc1e23f
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/`, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26 controlli), `verify.py` exit **0** (19 controlli) |

## 5. Due numeri del documento d'ingresso corretti (workspace > documento)

| voce | documento | workspace (misurato) |
|---|---|---|
| `Token` del §3 | **0** | **72 segnaposto** su 32 unità (nove simboli) |
| convenzione §4 | «`VALUE` **e** `TEXT` restano inglesi» | `VALUE` sì (17/17); `TEXT` **tradotti** (precedente L108…L152) |

Il primo era un numero sbagliato (nessun controllo di `check_handoff.py` copre i segnaposto: la parola «token»
non compare nel checker). Il secondo era una regola troppo larga: i `TEXT` identici nei lotti recenti sono
nomi di armi sotto contesti `ship:`, non prosa. Entrambi sono stati **rigenerati dai dati** prima di aprire il
lotto, e la riga `Token` del documento d'ingresso è stata corretta.

## 6. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 39 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file non è chiuso**: 136 unità dopo la riga 489, quattro finestre (L197…L200) ancora da fare.
