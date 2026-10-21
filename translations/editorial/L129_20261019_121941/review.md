# REVIEW — L129 · `boarding missions.txt` (il mercante da assistere, l'asteroide, il carico)

Coppie EN→IT rilette in `translation.json` (`fee796a7a3f4f2bd…`). Tutte le 89 unità sono **`PENDING`**.

## 1. Voce

- **I frammenti** sono pensati per comporsi: «Sapendo che <origin> hai cambiato rotta per salvare il capitano ti dà
  <payment>.» — la frase che ne esce è sgrammaticata **come in inglese**, e questo è il criterio: il frammento non
  deve peggiorare l'insieme, non deve essere bello da solo.
- **Le missioni** sono al presente e al «tu»: «Giri la nave e attivi i propulsori, cercando di allontanarti il più
  possibile dalla nave in avaria».
- **Il capitano del carico** parla colloquiale: «È la quarta volta che quasi ci lascio le penne questa settimana
  facendo questo lavoro!».
- **Le opzioni** restano fra parentesi tonde, come nel sorgente.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Knowing that ` / `Since ` / `Understanding that ` | **Sapendo che** / **Poiché** / **Comprendendo che** | 3–5 |
| `you altered course ` | **hai cambiato rotta** | 9 |
| `you risked your life ` · `you braved enemy fire ` | **hai rischiato la vita** · **hai affrontato il fuoco nemico** | 12, 15 |
| `to ` / `in order to ` / `so that you could ` | **per** / **al fine di** / **così che potessi** | 17–19 |
| `save ` `repair ` `rescue ` `secure ` `assist ` `help ` | **salvare** **riparare** **recuperare** **assicurare** **soccorrere** **aiutare** | 20–25 |
| `the` | **il** (senza spazio finale) | 26 |
| ` and ` · `save its cargo, ` | ** e ** · **salvare il suo carico, ** | 30–31 |
| `relieved ` · `captain ` · `gives you` | **sollevato** · **capitano** · **ti dà** | 39–41 |
| ` in gratitude.` · ` in thanks.` · ` as thanks.` | **in segno di gratitudine.** · **in ringraziamento.** · **per ringraziarti.** | 45, 48, 49 |
| `Shoot the asteroid.` | **Spara all'asteroide.** | 54 |
| `Maneuver my ship to shield the <origin>.` | **Manovra la mia nave per fare scudo alla <origin>.** | 55 |
| `tearing it to shreds` | **facendola a pezzi** | 61 |
| `Most of the other ship's crew…` | **la maggior parte dell'equipaggio…** | 65 |
| `presumably the captain` | **presumibilmente il capitano** | 68 |
| `I've nearly died` | **quasi ci lascio le penne** | 73 |
| `pirate raid` | **incursione piratesca** | 83–89 |

## 3. Nodi aperti (da non dedurre dopo)

1. **I frammenti non finiscono qui**: il file ne ha altri, e la regola degli **spazi** vale per ogni lotto che tocchi
   `phrase`.
2. **I nomi di frase si riconoscono dal contesto `phrase:`** e non si traducono. Nel lotto successivo (righe 417–686)
   ci sono **22 `UI_LABEL`**: altra categoria da isolare, con la lista esatta.
3. **`the` senza spazio finale** è un difetto del sorgente riprodotto: se un lotto futuro lo «correggesse», il
   confronto con l'inglese fallirebbe e la composizione cambierebbe.
4. **Le quattro `DESCRIPTION` uguali** (`Assisting Free Worlds`, `Republic`, `Deep Security`, `Syndicate`) hanno una
   sola resa: il controllo pretende stesso inglese ⇒ stessa resa.
5. **I `VALUE` sono nomi di missione** e restano inglesi anche quando contengono token (`Defend <planet>`).
6. **Il gate sui frammenti è stretto**: `gives you` → `ti dà` sta a 0,56. Riscrivere allargando il gate sarebbe
   sbagliato: si cambia il frammento.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 89 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: le missioni non sono state viste, e la frase composta non è stata letta in partita
  (la sua composizione casuale non è verificabile in staging).
- **Nessuna revisione umana**.
- **Il file non è completo**: restano 151 unità (righe 417–959).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (30 controlli) |
