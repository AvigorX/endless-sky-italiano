# REVIEW — L152 · `coalition jobs.txt` (i Giochi, la vendita, le tre specie)

Coppie EN→IT rilette in `translation.json` (`580b5869e9f95bed…`). Tutte le 21 unità sono **`PENDING`**.

## 1. Voce

Il file cambia registro: dalla burocrazia alla **scena**.

- «Gli Heliarch ti ringraziano profusamente quando vedono che hai accettato la loro offerta… fanno spazio a un esercito
  di ingegneri che vengono a rimuovere il motore di salto di riserva dalla tua nave.»
- L'Arach: «Ci onori con tanta generosità, capitano… **Enormemente prezioso è** ogni singolo motore che potresti
  portarci.»
- Il diario: «Ho venduto un motore di salto agli Heliarch e ho ricevuto il permesso di acquistare tecnologia e navi
  civili della Coalizione.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Honor us you do with such generosity` | **Ci onori con tanta generosità** | 17 |
| `still incapable of creating our own, we are` | **ancora incapaci di crearne uno nostro siamo** | 17 |
| `Tremendously valuable, each and every drive… is` | **Enormemente prezioso è ogni singolo motore…** | 17 |
| `Sold a jump drive…` | **Ho venduto un motore di salto…** | 19 |
| `tens of billions` | **decine di miliardi** | 21 |
| `small communes` | **piccole comunità** | 20 |

## 3. Nodi aperti (da non dedurre dopo)

1. **L'inversione dell'Arach non si normalizza**: è la firma della specie, ripetuta in tutto il gioco. Due controlli la
   verificano nel testo.
2. **`LOGBOOK` in prima persona**: è un diario, non una descrizione. «Ho venduto…», non «Venne venduto…».
3. **Tab e virgolette sono del sorgente**: due unità col tab, una con le virgolette, e il controllo le confronta con
   l'inglese una per una.
4. **Indici misurati, non dedotti**: le unità con tab sono 17 e 18 (avevo scritto 9 e 10). Corretto nei tre script.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 21 unità `PENDING`.
- **Nessuna vendita effettuata nel gioco**; i `LOGBOOK` non sono stati visti nel diario.
- **Nessuna revisione umana**.
- **Eseguito in batch** con L150 e L151: contratto = piano del batch.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (25 controlli), `verify.py` exit **0** (24 controlli) |
