# REVIEW — L120 · `campaign events.txt` (Giorno del Ricordo, l'attentato, la secessione)

Coppie EN→IT rilette in `translation.json` (`a4f3e6160ea73524…`). Tutte le 52 unità sono **`PENDING`**.

## 1. Voce e registro

- **Voce di diario** (`LOGBOOK`): informativa, al passato, senza imperativi («Gli Alphas furono progettati secoli
  fa come super-soldati geneticamente modificati…»).
- **Narrazione**: presente, seconda persona («Appena scendi dalla nave capisci che qualcosa non va affatto.»).
- **Dialogo**: diretto, con l'ufficiale che passa dal tono burocratico alla minaccia («Se rifiuti di obbedire, ti
  farò arrestare dalla polizia militare e la tua nave sarà sequestrata.»).
- **Un solo registro**: «tu», come i tooltip approvati. La cortesia «lei» è stata **rimossa** dall'unità 41 e il
  controllo ora la rifiuta.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `Remembrance Day` | **il Giorno del Ricordo** | 3–6 |
| `the Alphas` | **gli Alphas** (invariato) | 1–6 |
| `the Free Worlds` / `"Free Worlds,"` | **i Mondi Liberi** / **"Mondi Liberi"** | 15–19, 47–48 |
| `Republic Navy Yard` | **Arsenale della Marina della Repubblica** | 7, 19, 48 |
| `Galactic Stock Exchange` | **la Borsa Galattica** | 10, 16, 19, 37, 48 |
| `Carrier squadron` | **squadrone di navi portatrici** | 22, 47 |
| `liaison officer` | **ufficiale di collegamento** | 21–33, 41, 46, 50–52 |
| `state of emergency` | **stato di emergenza** | 27, 37, 41 |
| `under martial law` | **sotto legge marziale** | 41 |
| `Permanently Revoked` | **"Revocata in via definitiva"** | 45 |
| `pilot's license` | **licenza di pilota** | 45 |
| `Naval Reserve Command` | **Comando della Riserva Navale** | 41 |
| `field hospital` / `cots` | **ospedale da campo** / **brandine** | 32 |
| `Paradisians` | **Paradisiani** | 46, 50, 52 |
| `job boards` | **bacheche dei lavori** | 51 |
| `the galaxy is falling apart on you` | **la galassia ti sta già crollando addosso** | 20, 49, 50 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`Alphas` è invariato per decisione**, come le altre specie (Quarg, Drak, Korath): se un lotto futuro decidesse
   di italianizzarlo in «Alfa», servirebbe una decisione esplicita e il ritocco di questo lotto.
2. **Le 58 virgolette sono dialogo**: qui si traducono. Non confonderle con le chiavi `Preferences` di L115–L116,
   che restano inglesi.
3. **Il `LOGBOOK`** è un tipo raro (2 unità qui, 0 nei lotti precedenti da L68): va reso come diario, e non ha
   token di missione.
4. **`event: war begins` ha 37 unità**: è il contesto più grande finora incontrato, e il controllo non deve
   aspettarsi una distribuzione uniforme.
5. **Il registro è una verifica, non una preferenza**: il `check.py` cerca `Pensi quello|la sua nave|la farò|Senta,
   capitano` e deve restare vuoto. Se un dialogo futuro richiedesse davvero la cortesia, va dichiarato e il
   controllo va reso per-unità.
6. **Le firme delle rese**: `rogue planets down south` combaciava con due testi quasi uguali ma con esiti diversi;
   le firme corte sono un rischio misurato, non teorico.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 52 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: gli eventi non sono stati visti, e i 5 token non sono stati osservati
  sostituiti.
- **Nessuna revisione umana**.
- **Il file non è completo**: 98 unità residue (righe 282–3468).

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (29 controlli) |
