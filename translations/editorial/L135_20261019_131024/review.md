# REVIEW — L135 · `data/starts.txt` (gli inizi di partita)

Coppie EN→IT rilette in `translation.json` (`f897bd0f3d943382…`). Tutte le 32 unità sono **`PENDING`**.

## 1. Voce

- **La banca** è descritta con un'ironia fredda: «L'architettura della banca è quella che avresti chiamato
  "futuristica" quando sognavi che il futuro fosse meno squallido del presente». Il reso amaro arriva nella battuta del
  banchiere: «Stai prendendo in prestito 480.000 crediti… alla fine dell'anno avrai pagato... 433.567 crediti di
  interessi. Firma qui.» Sorride.
- **Il cantiere** chiude con la domanda che determina il futuro: «Quale sceglierai determinerà il tuo futuro...».
- **Le voci di diario** parlano in prima persona: «Finalmente sono riuscito a mettere insieme abbastanza soldi per
  comprare una licenza di pilota.»
- **Il secondo inizio** è più formale e ottimista: «Finiti gli studi primari, scopri che il Deep offre prestiti a basso
  interesse ai capitani che si dedicano alla prospezione e hanno voti abbastanza alti, e tu ce l'hai fatta!».

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Endless Sky` · `Deep Desire` | **identici** | 1, 17 |
| `textile mill` | **tessitura** | 2 |
| `mortgage` | **mutuo** | 2, 4 |
| `Deep` · `Dirt Belt` | **Deep** · **Dirt Belt** | 2, 6, 9, 18, 20, ecc. |
| `Syndicate` · `Paradise Worlds` | **Sindacato** · **Mondi del Paradiso** | 6–8 |
| `shoddy products` | **prodotti scadenti** | 8 |
| `their opposition to organized labor is legendary` | **la sua opposizione al sindacalismo è leggendaria** | 8 |
| `Truth in Lending statement` | **il prospetto sulla verità del prestito** | 13 |
| `Certificate of Eligibility` | **Certificato di idoneità** | 28 |
| `a red tree with branches forming the shape of a brain` | **un albero rosso i cui rami formano la sagoma di un cervello** | 27 |
| `Peace. Prosperity. Progress.` | **Pace. Prosperità. Progresso.** | 27 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`VALUE` = nome dell'inizio**: non è un nome di missione. Vale per tutti i sette inizi che restano.
2. **Zero token nell'intero file**: il controllo `== {}` va ripetuto anche nei lotti successivi, non solo qui.
3. **Cinque frasi condivise fra inizi**: se un inizio futuro le ripete, la resa deve essere **identica**, e il confronto
   si fa per stringa, non a occhio.
4. **Numeri**: convenzione italiana. Cambiano i separatori, non i valori; due controlli presidiano i due lati.
5. **`Deep` e `Dirt Belt` restano inglesi**: «Profondo» è vietato dal controllo, e non per gusto.
6. **`New Reykjavik`** è traslitterato e resta così.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 32 unità restano `PENDING`.
- **Nessuna partita avviata**: non ho visto il menu degli inizi né la scena della banca.
- **Nessuna revisione umana**.
- **`starts.txt` è al 28,3%**: 81 unità da fare (sette inizi).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (29 controlli, invariante di segmento) |
