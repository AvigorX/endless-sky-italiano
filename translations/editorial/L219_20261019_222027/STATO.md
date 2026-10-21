# STATO — L219 · `successor ships.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L219_20261019_222027` |
| Righe / unità | **386–629** / **25** — file a **70/146 (47,9%)** |
| Tipi | {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 3} |
| Tab · virgolette · apici | **1** (unità 8) · **32** (2 × 16) · **3 EN / 10 IT** |
| Segnaposto | **0** |
| Contesti | **3** — `Kvelqde` 9, `Myaede` 9, `Kvelqde-Khora` 7 |
| Parole | **467 EN → 487 IT** (1,00–1,16, media 1,02) |
| sha256 | `26062019d4d6d536…` |
| Esiti | `check.py` **27** (`FAIL totale: 0`) · `verify.py` **16** (`FAIL: 0`) |

## La regola del file, applicata una seconda volta

**19 unità su 25 restano identiche all'inglese** (16 `TEXT` di equipaggiamento, 3 `VALUE` di specie) e **6 `DESCRIPTION`
si traducono**. Il `check.py` verifica il rapporto **per unità**, non a campione, e il `verify.py` fissa che le unità
tradotte siano **esattamente** le sei `DESCRIPTION`.

## Il tratto nuovo del lotto: due schede per nave, e le frasi condivise

Kvelqde e Myaede hanno **due `DESCRIPTION` ciascuna** — la prima introduttiva, la seconda più circostanziata — e le due
versioni **si ripetono a vicenda**:

| coppia | frase condivisa | resa fissa |
|---|---|---|
| 7 / 9 | *This tiny shuttle is the smallest vessel operating in Successor space, and…* | «Questa navetta minuscola è la nave più piccola in servizio nello spazio dei Successori, e…» |
| 24 / 25 | *neither elegant nor fast … flexible enough weapons layout to let it fight back in a pinch* | «non è né elegante né veloce … una disposizione delle armi abbastanza flessibile da permetterle di reagire all'occorrenza» |

Se una delle due versioni cambia, la stessa nave racconta due cose diverse in due schermate. Il controllo confronta il
**prefisso** delle unità 7 e 9 e le **due formule** delle unità 24 e 25.

## Cosa contiene

La **Kvelqde** (navetta minuscola, la prima nave dei piloti dei Successori), la **Kvelqde-Khora** (la versione irrobustita
dalle Case del Popolo, con una seconda feritoia e la rete di scudi potenziata) e la **Myaede** (il cargo che regge il
commercio dei Successori dal crollo del vecchio impero).

## Difficoltà

1. **`get their arms on`** non è `get their hands on`: il testo dice *arms*, e la resa «riuscire a metterci le mani»
   conserva l'idea dell'accesso senza inventare un'arma che non c'è.
2. **`nostalgia genealogica`**: `a familial Myaede is often passed down through the lineage of spacefaring low-born
   Successors … under a grandparent's watchful gaze` → «tramandata lungo la discendenza dei Successori di umili origini che
   viaggiano nello spazio … sotto lo sguardo vigile di un nonno». `low-born` è «di umili origini», non «plebeo».
3. **`bares enough teeth for a bit of light piracy`** → «mostra abbastanza denti per un po' di pirateria leggera»: l'ironia
   sta nell'understatement e va lasciata.
4. **`decaying stations and hostile worlds of southwestern Successor space`** → «le stazioni in degrado e i mondi ostili
   dello spazio sudoccidentale dei Successori».
5. **Apici**: 3 in inglese (*People's*, *grandparent's*, *you've*) e **10** in italiano su cinque unità (elisioni e
   apostrofi: `dell'epoca`, `l'incarnazione`, `dall'essere`, `l'economicità`, `d'uso`, `d'attacco`, `all'estrazione`,
   `all'occorrenza`). Totale e distribuzione **non coincidono**, ed è atteso: il controllo confronta le coppie.

## Verifica

```bash
cd staging/editorial/L219_20261019_222027
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # FAIL: 0 (16 controlli) · 45 + 25 + 76 = 146 · confine 634
```

**Non verificato**: nessuna nave vista nel gioco; 25 unità `PENDING`.
