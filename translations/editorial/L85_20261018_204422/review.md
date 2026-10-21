# REVIEW — L85 · `data/successors/predecessors.txt` (chiude il file)

## 1. Coerenza (L81–L84)

- **Myiara, Resja, Kaatrij, Alte Casate, Predecessori/Successori**: forme fisse.
- **`coilgun`** → «cannone a bobina» in prosa (coerente con L82/L84); il nome d'oggetto nei contesti resta
  inglese (decisione 259) — qui però i nomi compaiono **solo** nei contesti, non come unità.
- **`Shield Cortex`** e `cortex` restano invariati (decisione 264).

## 2. Nodi aperti

- **`Point Drive`** (unità 6, in realtà contesto di riga 728): il testo parla del «congegno» con le parole di
  Resja, ma il **nome** resta un dato. Il lettore vedrà un nome inglese e una descrizione italiana: è la
  conseguenza dichiarata della decisione 259.
- **`that pang-ridden emptiness`**: «vuoto carico di dolore». `pang` è più somatico; «fitta» avrebbe reso
  meglio il corpo, ma stonava con «vuoto».
- **`the world went away`**: «il mondo svanisce» — non «scompare», che è più neutro.
- **`easily mistaken for a sculpture`**: «facile da scambiare per una scultura» — il reattore è un oggetto
  d'arte, e la resa lo lascia ambiguo.

## 3. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 59 unità del file restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna delle sette schede è stata vista a schermo.
- **Nessun confronto con i valori**: «distrugge una piccola città» è testo, non statistica.
- **I nomi di equipaggiamento** restano in inglese.

## 4. Rischi residui

- **1,07–1,15**: tutte le unità sopra 1,00 (l'italiano è più lungo sulle perifrasi tecniche), nessuna vicina al
  gate.
- **Il `verify.py` di chiusura** è più severo: se qualcosa toccasse le righe 648–782, diventerebbe rosso.
- **Cinque lotti per un file di 59 unità**: L84 (4 unità) e L85 (7) sono piccoli perché il file alterna
  blocchi di scheda e singole righe di nome; non è una frammentazione arbitraria.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (21 controlli), `verify.py` exit 0 (29 controlli), sha256 `3fad23a16aeaa834`, **file 59/59** |
