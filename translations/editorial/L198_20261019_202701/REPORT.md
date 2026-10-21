# REPORT — L198 · `hai jobs.txt` (terzo lotto, il più grande dei cinque)

## 1. Contenuto

Il lotto dei **trasporti ordinari**: cinque mestieri Hai in cerca di lavoro, undici consegne semplici, otto
urgenti con scadenza, una «crociera prigione» e la convention d'affari di Swiftsong che apre L199.
51 unità, 25 contesti, 22 `VALUE` (nomi di lavoro, inglesi per convenzione).

| blocco | unità | righe | contenuto |
|---|---|---|---|
| mestieri | 1–5 | 988–1040 | contadini, operai tessili, operai di fabbrica |
| Cargo [0]–[4] | 6–15 | 1045–1147 | `Delivery to <planet>` (VALUE) + consegna semplice |
| Bulk [0]–[2] | 16–27 | 1170–1324 | `Bulk delivery to <planet>` |
| Rush [0]–[3] | 28–35 | 1328–1399 | consegna **entro il `<date>`** |
| Large Rush [0]–[3] | 36–43 | 1418–1492 | idem, taglia grande |
| «prigionia» | 44–46 | 1514–1535 | `Hai "prison" cruise to <planet>`, cella, mance |
| Swiftsong [1]–[2] | 47–51 | 1542–1565 | convention d'affari, due `DESCRIPTION` identiche |

## 2. Difficoltà

1. **Un lotto di ripetizioni, non di prosa**: 11 copie di una stringa e 8 di un'altra. Il rischio non è tradurre male una frase, è **tradurne due versioni** della stessa. Il `check.py` elenca gli indici attesi di ciascuna famiglia e pretende una sola resa.
2. **Rese concorrenti in staging**: `Deliver <cargo>…` aveva **tre** rese (`a`/`su`, `pagamento`/`compenso`), `…by <date>…` ne aveva **due**. Nessuna è «sbagliata»; se ne sceglie **una** — `su <destination>` + `Il pagamento è` — perché è quella di L196–L197 e perché è già in staging. Il controllo verifica che la resa scelta **appartenga** all'insieme dei precedenti: non è inventata.
3. **`operai tessili`**: resa unica in staging (`Questa famiglia di <bunks> operai tessili spera…`), riusata alla lettera. Per gli operai di fabbrica si applica la stessa cornice sostituendo il mestiere — e il controllo lo verifica con una sostituzione.
4. **Apici**: 1 inglese (`it's`) contro 3 italiani (`l'esperienza`, `d'affari` ×2). Il numero non torna perché non deve: l'elisione italiana non è la contrazione inglese.
5. **Un errore di L197 emerso qui**: la frase `You wish the mining family the best of luck…` era già tradotta in L22 («…ogni fortuna… e incassi…») e in L197 ne avevo creata una variante. Ho riallineato L197, rieseguito i suoi due script (exit 0) e aggiornato lo sha in tutti i documenti che lo citano.
6. **Un secondo errore, mio, nel `verify.py`**: avevo scritto `sum(...) == 1 == 3 - 2`, cioè un confronto a catena (trappola 51). Corretto **prima** di eseguire, con due confronti espliciti.

## 3. Numeri osservati

```
unita' 51 · {'VALUE': 22, 'DESCRIPTION': 24, 'DIALOG': 5} · tutte PENDING
0 tab · 2 virgolette EN = 2 IT · 1 apice EN / 3 IT · 112 segnaposto su 7 simboli
25 contesti · righe 988/1565 · 75 unita' prima · 49 dopo · confine riga 1579 (DIALOG)
parole 472 -> 481 · rapporto 0.91 - 1.17 (media 1.05)
FAIL totale: 0 (29 controlli) · verify exit 0 (21 controlli) · sha256[:16] 7465d06d0b238ebf
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json` + `part02.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto; due correzioni fatte **prima** dell'esecuzione |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (21 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 51 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file non è chiuso**: 49 unità dopo la riga 1565, due finestre (L199, L200).
