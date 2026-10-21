# REVIEW — L83 · `data/successors/predecessors.txt`

## 1. Coerenza (L81–L82)

- **Resja, Myiara, Queru, Torji, Sarija, Tijra, Veusa** restano invariati: sono nomi del file.
- **La distinzione dato / prosa** regge anche qui: 8 unità identiche, 3 tradotte (decisione 259).
- **`Multimodal Armor: Regen`** non compare in questo lotto, e nessun nome di equipaggiamento è stato toccato.

## 2. Nodi aperti (dichiarati)

- **`Valkkyiara-Khorasaqran` vs `Valkkyiara-Khorasaqra`**: due grafie nel sorgente (nome dell'unità 4 e
  contesto di riga 483). Non unificate; se un lotto futuro le trattasse come lo stesso oggetto, servirebbe una
  decisione sull'intero file.
- **`cortex`**: reso «cortex» e non «corteccia» — è un termine tecnico del gioco, e la forma italiana
  «corteccia» suonerebbe biologica.
- **`endurance`**: «resistenza» (la riserva), non «autonomia»: la nave consuma scudi, non carburante.
- **`all but insignificant`**: «pressoché irrilevante»; la sfumatura letterale («tutt'altro che») sarebbe
  ambigua in italiano.

## 3. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 11 unità `PENDING`.
- **Nessun caricamento nel gioco**: le tre schede e la nave non sono state viste a schermo.
- **Nessuna traduzione dei nomi**: scelta dichiarata.
- **Nessun confronto con i valori di gioco**: «efficiente», «insignificante» sono testo, non misure.

## 4. Rischi residui

- **`1,19` è il massimo** (unità 3, la più tecnica): dentro il gate.
- **Il `verify.py` asserisce 37 prima / 11 dopo**: se L84 non partisse dalla 534, diventerebbe rosso.
- **Il rapporto complessivo del file sale a 1,027** (479 → 492) proprio per queste tre schede: è atteso, non
  un segnale di gonfiaggio.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 1 parte, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (22 controlli), `verify.py` exit 0 (27 controlli), sha256 `5c427d01bb9c39a0` |
