# STATO — L106 · `data/korath/korath missions.txt` (file nuovo, **le quadre dei Wanderer**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L106_20261018_223227` |
| Righe / unità | **1–120** / **25** |
| Tipi | **22 `MISSION_TEXT`** + **1 `LOGBOOK`** (5) + **1 `VALUE`** (6, identico) + **1 `DESCRIPTION`** (7) |
| `VALUE` (identico) | unità 6: `Supplies to <planet>` — nome di missione, con un token dentro |
| `LOGBOOK` (tradotto) | unità 5: la scheda dei Korath (unità 5, riga 62) |
| Contesti | **6**: `First Contact: Korati Efreti`, `Laki Nemparu`, `Karek Fornati`, `Setar Fort`, `Discovered Korath Space`, `Setar Fort Heating` |
| Parole | **854 EN → 833 IT** (0,975); per unità 0,80–1,27 |
| Tab · virgolette | **17** · **45**, con **una citazione aperta** (unità 16) |
| Token | **13** in sei famiglie (`<planet>` 4, `<payment>` 4, `<last>` 2, `<cargo>` 1, `<destination>` 1, `<tons>` 1) |
| Quadre | **16 coppie** nelle unità 11 (3), 16 (7), 17 (1), 20 (4), 25 (1) |
| Ripetizioni | **2**: 2/3/4 (tripla), 15/19 |
| sha256 | `10952e0d80f509b5…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **29 controlli**, exit **0** |

## Le quadre dei Wanderer

`[relieved, happy]`, `[believe, assume]`, `[supplies, aid]`, `[perish? expire?]`: il dispositivo di traduzione
elenca **due rese possibili** dello stesso concetto, perché la lingua dei Wanderer non ha un equivalente diretto.
In italiano si traducono **entrambe** e la struttura resta: `[sollevato, felice]`, `[credo, suppongo]`,
`[provviste, aiuti]`, `[perire? spegnersi?]`.

Il `check.py` verifica **per unità** quante coppie ci sono e, per ognuna, che contenga **due alternative**
(virgola o punto interrogativo): una coppia con una parola sola è un errore che nessun conteggio totale
rivelerebbe.

## Invariante di segmento (primo lotto del file)

| Voce | Valore |
|---|---|
| Unità prima della riga 21 | **0** — nessun lotto precedente su questo file |
| Unità dopo la riga 119 | **133** |
| Confine | riga **126** apre `mission:Setar Fort Heating` |
| File | **158 unità**, `max(line) = 580` |
| Copertura | **25/158 (15,8%)** |

## Contenuto

- **Quattro «primi contatti»** con i Korath (unità 1–4): il saluto a mani aperte e la frase che nessuno traduce —
  `"Humani efreti, naskoor amasavarkta."` L'unità 1 dice «questa **stazione**», le altre «questo **spazioporto**»:
  non è una variante, è il primo caso che si svolge su una stazione.
- **`Discovered Korath Space`** (unità 5, `LOGBOOK`): la scheda della specie — il territorio in rovina, i **Kor
  Efreti** sotto la protezione Quarg, gli esuli che saccheggiano i mondi umani, e i due eserciti di droni
  **Kor Mereti** e **Kor Sestor** chiusi in una guerra senza fine.
- **`Setar Fort Heating`** (unità 6–25): il Wanderer che chiede di portare provviste a un pianeta che scivola in
  un'era glaciale; le domande del giocatore sul pagamento basso, il rifiuto dei Kor Efreti ad accettare la
  terraformazione per «orgoglio, onore», e il carico di indumenti caldi, serre, isolamento.

## Verifica

```bash
cd staging/editorial/L106_20261018_223227
python check.py   # FAIL totale: 0 (31 controlli)
python verify.py  # exit 0 (29 controlli)
```
