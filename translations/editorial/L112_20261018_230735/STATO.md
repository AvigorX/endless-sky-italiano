# STATO — L112 · `data/_ui/tooltips.txt` (**120 unità, tutte da tradurre**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L112_20261018_230735` |
| Righe / unità | **331–688** / **120** |
| Tipo | **120 `TUTORIAL_TIP`**, nient'altro |
| Stati | **120 `PENDING`** — misurato con `select state … group by state` **prima** di scrivere |
| Contesti | **120**, uno per suggerimento, da `tip:hull heat:` a `tip:depleted shield delay:` |
| Parole | **1813 EN → 2044 IT** (1,127); per unità 0,89–1,62, media 1,21 |
| Tab · virgolette · token · quadre · ripetizioni | **0** · **0** · **0** · **0** · **0** |
| sha256 | `3ff21c44bf59b9fc…` |
| `check.py` | **29 controlli**, `FAIL totale: 0` |
| `verify.py` | **33 controlli**, exit **0** |

## La lezione applicata: prima gli stati, poi la traduzione

Il lotto precedente aveva 52 unità già approvate su 104 e il contratto non lo diceva. Qui il primo passo è stato
misurare:

```
STATI nella finestra: {'PENDING': 120}
```

Le 52 approvate del file stanno tutte fra le righe 16 e 172; questa finestra è **tutta da tradurre**. Il
`mkparts.py` lo **asserisce** (`assert set(states.values()) == {'PENDING'}`) e abortisce se una sola unità
risultasse approvata: in quel caso si riproduce dal database, come in L111.

## Il registro è quello approvato

Le 120 unità seguono le convenzioni fissate dal blocco approvato, perché stanno negli stessi pannelli:

| convenzione | esempio in questo lotto |
|---|---|
| **«tu»** al giocatore | «…per cui **puoi** essere multato…», «…**devi** comunque pagarne la manutenzione», «…**provi** ad abbordarla» |
| **«danni da …»** plurale + «resistiti» | «Danni da ionizzazione resistiti al secondo», «Danni da disturbo resistiti al secondo» |
| **«messa fuori uso»** per *disabled* | «…dopo essere stati messi fuori uso», «una nave messa fuori uso si ripari da sola» |
| **«ammiraglia»** · «spazio equipaggiamenti» | non ricorrono qui, restano nel glossario |
| **iperguida** per *hyperdrive* | «Carburante consumato quando si salta fra sistemi con questa iperguida» |
| **ramscoop invariato** | «I ramscoop sono più efficaci vicino a una stella» |

## Tipi di danno: nove famiglie, una resa ciascuna

`ion` → **ionizzazione** · `scramble` → **disturbo** · `disruption` → **disruzione** · `slowing` → **interferenza
sui motori** · `discharge` → **scarica** · `corrosion` → **corrosione** · `leak` → **perdita di carburante** ·
`burning` → **ustione** · `piercing` → **perforazione** · `heat` → **calore**.

Le unità 13–20 sono la stessa frase con il tipo di danno sostituito: **otto varianti dello stesso stampo**, e una
sola resa sbagliata in una di esse romperebbe la simmetria che il giocatore vede in sequenza.

## Contenuto coperto

- **scafo** (1–8, 21–26): calore e carburante della riparazione, ritardo, soglia di messa fuori uso, protezione,
  moltiplicatori (anche in occultamento).
- **nave messa fuori uso** (9–20): tempo, energia, carburante, calore e **otto tipi di danno** applicati quando si
  ripara da sola.
- **equipaggiamento come merce** (27–28, 52, 60–61, 99): multa, reddito, manutenzione, costi operativi, valore di
  vendita e deprezzamento.
- **inerzia e massa** (29, 54–55): riduzione dell'inerzia, massa senza carico, massa in tonnellate.
- **scansioni** (62–66, 96): equipaggiamenti, portata, velocità, efficienza, opacità, interferenza.
- **spazio** (67–69): spazio generico, spazio occupato, spazio libero.
- **surriscaldamento** (70–71), **disturbo ottico e radar** (72–73, 77), **perforazione** (74–76).
- **rifornimento e salto** (78, 41–46, 97): ramscoop, iperguida, motore di salto, portata, costo di massa.
- **equipaggio** (79–81), **spinta inversa** (82–95), **autodistruzione** (98).
- **scudi** (100–120): energia, carburante e calore della ricarica (con ritardo e moltiplicatori), rigenerazione,
  permeabilità alta/bassa/in occultamento, robustezza totale, ritardo, scudi esauriti.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 331 | **104** (L111) |
| Unità dopo la riga 688 | **443** |
| Confine | riga **691** apre `tip:shield protection:` |
| File | **667 unità**, `max(line) = 1865` |
| Copertura | **224/667 (33,6%)** |

## Verifica

```bash
cd staging/editorial/L112_20261018_230735
python mkparts.py   # 120 unità, tutte PENDING, 0 approvate
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # exit 0 (33 controlli)
```
