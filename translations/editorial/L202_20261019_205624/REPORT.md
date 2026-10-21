# REPORT — L202 · `hai outfits.txt` (secondo lotto)

## 1. Contenuto

Armi Hai in sedici unità: due prototipi ionici, la famiglia **Skipper Railgun** dei droni Flea (tre `VALUE` e tre
descrizioni), i **Tracker** con il loro deposito e la **difesa anti-missile** che li combatte.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| prototipi ionici | 1–3 | 205–240 | `Ionic Blaster`, `Ionic Turret`: meno danni, più inceppamento |
| famiglia Railgun | 4–11 | 254–309 | proiettile, rastrelliera, cannone, battuta dei piloti, nota sulle munizioni |
| Tracker e deposito | 12–13 | 361–373 | munizioni e stoccaggio |
| Tracker Pod | 14–15 | 415–416 | armi a ricerca, raggio di virata, nota sulle munizioni |
| Bullfrog | 16 | 484 | la difesa di secoli fa ancora efficace |

## 2. Difficoltà

1. **La stringa ripetuta** (11 e 15): stesso inglese, stessa resa. Il `check.py` confronta i due testi, non solo il numero di tab.
2. **Nomi propri dentro il testo**: `Skipper Railgun`, `Ion Cannon`, `Ionic Blaster`, `Tracker Pod`, `Tracker Storage Pod`, `Flea`, `Unfettered` restano inglesi anche quando la frase li declina («i proiettili **dello** Skipper Railgun», «i droni **Flea**»). Nessuna traduzione del nome, solo l'articolo italiano.
3. **`outfitter`**: il glossario è esplicito — mai il prestito, e nella prosa «negozio di equipaggiamenti». Due occorrenze, entrambe conformi.
4. **Contrazione vs elisione**: 2 apici inglesi contro 10 italiani. Il controllo elenca le unità e non pretende l'uguaglianza.
5. **Il refuso del sorgente**: *weapon jamming affects* invece di *effects*. Non si corregge il gioco: si traduce il senso («lo stesso effetto di inceppamento») e si annota.
6. **Ratio massimo 1,50** (unità 7): la frase italiana è più lunga dell'inglese. Dentro il gate, ma è il valore più alto della serie: il gate serve a questo.

## 3. Numeri osservati

```
unita' 16 · {'DESCRIPTION': 13, 'VALUE': 3} · tutte PENDING
4 tab · 0 virgolette · 2 apici EN / 10 IT · ZERO segnaposto
9 contesti · righe 205/484 · 8 prima · 41 dopo · confine riga 508
parole 436 -> 434 · rapporto 0.98 - 1.50 (media 1.12)
FAIL totale: 0 (24 controlli) · verify exit 0 (17 controlli) · sha256[:16] 2281312fe0da11a4
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (17 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file non è chiuso**: 41 unità dopo la riga 484.
