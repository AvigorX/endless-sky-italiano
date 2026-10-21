# STATO — L111 · `data/_ui/tooltips.txt` (**52 unità già approvate** + 52 tradotte)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L111_20261018_230007` |
| Righe / unità | **16–328** / **104** |
| Tipo | **104 `TUTORIAL_TIP`**, nient'altro |
| Stati | **52 `APPROVED`** (1–52, testo già in `state.db`) + **52 `PENDING`** (53–104, tradotte qui) |
| Contesti | **104**, uno per suggerimento, da `tip:parked` a `tip:hull fuel multiplier:` |
| Parole | **1810 EN → 1848 IT** (1,021) |
| Tab · token · quadre · ripetizioni | **0** · **0** · **0** · **0** |
| Virgolette | **14**, tutte doppie (nomi di attributo e di categoria) |
| sha256 | `dee204e785c7d01b…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## La scoperta che ha cambiato il lotto

La finestra 16–328 **non era tutta da tradurre**: 52 unità erano già `APPROVED` in `state.db`, con il testo
italiano nel campo `italian`. Il contratto (`HANDOFF_L111`) diceva «104 `TUTORIAL_TIP`» senza distinguere gli
stati, e la prima versione del `check.py` falliva su «unità del lotto in PENDING» — **il controllo aveva ragione**.

Regola applicata: **il testo approvato non si riscrive, si riproduce alla lettera**. `mkparts2.py` legge le 52
approvate dal database in **sola lettura** e le mie 52 da `my_pending.json`; `check.py` e `verify.py` verificano
entrambe le cose, in modo indipendente:

| verifica | controllo |
|---|---|
| le 52 `APPROVED` | testo di staging **identico** al campo `italian` del DB, carattere per carattere |
| le 52 `PENDING` | tradotte, **diverse** dal sorgente inglese, e **senza «voi»** |

## Le convenzioni che il blocco approvato imponeva

Il testo approvato non è solo un testo: è un **registro già fissato** per lo stesso pannello. Le mie 52 unità
dovevano allinearsi, altrimenti lo stesso pannello alternerebbe due voci.

| convenzione | esempio approvato | applicazione nelle mie unità |
|---|---|---|
| **«tu»** al giocatore, non «voi» | «non puoi usarla come ammiraglia» | «L'ammiraglia e le scorte parcheggiate non contano. **Puoi** superare la capacità…» |
| **«danni da …»** al plurale | «Danni da ustione resistiti al secondo» | «Danni da corrosione resistiti al secondo», «Danni da scarica…», «Danni da disruzione…» |
| **«Protezione contro i danni da …»** + «la quantità di danni … che la nave sopporta» | unità 23 | unità 55, 62, 67, 80, 90, 95 |
| `ammiraglia` (non «nave ammiraglia») | unità 21 | unità 61 |
| «quando **si attiva** questo postbruciatore» | unità 5–18 | non ricorre nelle mie unità |

Il `check.py` verifica **l'assenza di «voi»** nelle 52 unità nuove: è l'unico modo di controllare la coerenza di
registro senza confrontare a mano 52 testi.

## Terminologia fissata (e verificata)

`mass` → **massa** · `acceleration` → **accelerazione** · `energy` → **energia** · `heat` → **calore** ·
`cooling` → **raffreddamento** · `fuel` → **carburante** · `hull` → **scafo** · `shield(s)` → **scudi/scudo** ·
`cloak/cloaking` → **occultamento/occultare** · `outfit` → **equipaggiamento** · `ton(ne)s` → **tonnellate** ·
`crew` → **equipaggio** (persone: «membri d'equipaggio») · `bunks` → **cuccette** · `ammiraglia` per *flagship*.

Tipi di danno: `burn` → **ustione** (dal blocco approvato) · `corrosion` → **corrosione** · `discharge` →
**scarica** (scudi) · `disruption` → **disruzione** (scudi) · `ion` → **ionizzazione** · `scramble` →
**disturbo** · `leakage` → **perdita** (carburante) · `slowing` → **interferenza sui motori** · `force` →
**forza d'urto**.

## Contenuto coperto

- **52 unità approvate** di `postbruciatore`, `asteroidi`, `bunks`, `cattura`, `carico`, `cloak` (con le due
  varianti `cloak` e `cloak by mass`), `raffreddamento`.
- **52 unità nuove**: `corrosione`, `costo`, `capacità della flotta`, `scarica`, `dirusione`, `resistenza`
  (drag), `bay per droni e caccia`, `capacità energetica`, `spazio motori`, `protezione da energia`,
  `detrito`, `forza d'urto`, `carburante` (5 unità), `porti per cannoni`, `dissipazione del calore`,
  `generazione di calore`, `protezione dal calore`, `capacità termica`, `scafo` (robustezza e riparazione,
  8 unità).

## Invariante di segmento (primo lotto del file)

| Voce | Valore |
|---|---|
| Unità prima della riga 16 | **0** |
| Unità dopo la riga 328 | **563** |
| Confine | riga **331** apre `tip:hull heat:` |
| File | **667 unità**, `max(line) = 1865` |
| Copertura | **104/667 (15,6%)** |

## Verifica

```bash
cd staging/editorial/L111_20261018_230007
python mkparts2.py  # 52 APPROVED riprodotte + 52 PENDING tradotte
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (28 controlli)
```
