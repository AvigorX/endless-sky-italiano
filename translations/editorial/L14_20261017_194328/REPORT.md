# L14 — Decimo lotto del tratto iniziale di `data/map planets.txt`

**Data:** 2026-10-17 · **Esito: lotto completo, 83/83 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L14_20261017_194328/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **3239–3607** |
| Posizione | decimo tratto del settore iniziale (3239–3845) |
| Unità | **83** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **4.470** inglesi → **4.534** italiane |
| Rapporto | 0,89 – 1,20 |
| Pianeti | **30** (da **Livolua** a **Midnight Diamond**) |
| Tab di paragrafo | 27 |
| Virgolette | 14 (7 coppie: unità 1, 26, 39, 70, 79 ×2, 83) |
| Token `<...>` | 0 |

Confine pulito: l'ultima unità (riga 3607) chiude Midnight Diamond; la successiva (riga 3614) apre
Midway Emerald.

**Dopo L14 resta un solo lotto**: **L15 = 49 unità / 2.693 parole** (righe 3614–3845), che chiude il file.

---

## 2. Esempi rappresentativi

**Unità 3 — `planet:Livolua`**

> An especially-ambitious skyhook design would stretch down each day to retrieve or deposit a payload
> mounted on a kilometer-tall tower, spindly enough that it had to be reinforced with nanotube guy lines
> reaching the ground.

> Un progetto di skyhook particolarmente ambizioso scendeva ogni giorno per recuperare o depositare un
> carico montato su una torre alta un chilometro, così esile da dover essere rinforzata con tiranti in
> nanotubi che arrivavano fino al suolo.

**Unità 39 — `planet:Market of Gupta`**

> The motto of House Mallob's shipyards is "strong as the mountains, spacious as the skies," referring to
> their focus on durable hulls and high cargo capacity.

> Il motto dei cantieri della Casata Mallob è "forti come le montagne, spaziosi come i cieli", con
> riferimento al loro impegno per scafi durevoli e grande capacità di carico.

**Unità 45 — `planet:Masada`**

> Its tectonic activity ended long ago, and the eons of erosion has worn its terrain down to the bedrock.
> […] The broken remains of what might have once been cities […] hints that there is much history here -
> but no future.

> La sua attività tettonica è finita molto tempo fa, e gli eoni di erosione hanno consumato il terreno fino
> al substrato roccioso. […] I resti spezzati di quelle che forse furono città […] lasciano intuire che qui
> c'è molta storia, ma nessun futuro.

**Unità 78 — `planet:Midgard`**

> It is now home to dozens of major metropolitan areas and a population of over four billion, and is where
> you were born.

> Oggi ospita dozzine di grandi aree metropolitane e una popolazione di oltre quattro miliardi, ed è il
> mondo in cui sei nato.

*(Secondo mondo natale del giocatore incontrato dopo Greenwater in L11: differenza rispetto all'unità 76,
che non lo dice, conservata.)*

**Unità 79 — `planet:Midgard`**

> An example of this is the tradition of "tributation." Certain nights every year, the citizens of the Deep
> leave out saucers of milk and sweet bread as an offering to the 'elves:' pale, delicate beings said to
> protect the Deep.

> Un esempio è la tradizione della "tributazione". In certe notti di ogni anno i cittadini del Deep lasciano
> fuori piattini di latte e pane dolce come offerta agli 'elfi': esseri pallidi e delicati che si dice
> proteggano il Deep.

**Unità 83 — `planet:Midnight Diamond`**

> From the outer limits of the system, this planet shines brightly in tones that contrast with the local
> star's light, earning the gas giant the nickname "Midnight Star."

> Dai confini esterni del sistema questo pianeta brilla di tonalità che contrastano con la luce della stella
> locale, guadagnando al gigante gassoso il soprannome di "Stella di Mezzanotte".

---

## 3. Il controllo ha trovato un errore

**Unità 26: virgolette 2 vs 0.** L'originale dice `on platforms farther "inland,"` e la resa aveva perso le
virgolette. Ripristinate ("sulle piattaforme più **"all'interno"** atterrano le astronavi"), il controllo
torna a `FAIL totale: 0`.

---

## 4. Interventi editoriali

Tredici interventi in stesura e rilettura (dettaglio in `review.md` §4), oltre alla correzione imposta.

| Termine | Resa | Occorrenze |
|---|---|---|
| `Earth`, `Mars`, `the Moon` | Terra, Marte, la Luna | 6 / 4 / 1 |
| `House Mallob` | Casata Mallob | 3 |
| `"tributation"`, `'elves:'` | "tributazione", 'elfi': | 1 + 1 |
| `"Fourth Port"`, `"Midnight Star"` | "Quarto Porto", "Stella di Mezzanotte" | 1 / 1 |
| `skyhook` | invariato | 1 |
| `ramscoops` | raccoglitori magnetici | 1 |

Rese notevoli: `arcology` → "arcologia"; `hothouse world` → "mondo serra"; `bone dry` → "asciutta fino
all'osso"; `city-ships` → "navi-città"; `longcows` → "bovini lunghi"; `ill-behaved` → "maleducata";
`diamond rains` → "piogge di diamanti"; `dry-dock` → "bacino"; `deflector shield generators` → "generatori
di scudi deflettori".

---

## 5. Decisioni ancora aperte

1. **`"tributation"` → "tributazione"** (1): termine inventato; se ricompare in testi di missione va tenuto
   identico.
2. **`skyhook` invariato** (1): secondo uso, scelta ormai stabile.
3. **Quattro coppie di unità quasi identiche** (23/24, 36/37, 48/49, 76/78): varianti del sorgente,
   differenze conservate. In 24 "come la tua", in 78 "ed è il mondo in cui sei nato".
4. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `Consigli Confederati` (L10/L12) vs
   `Confederated Councils` (L6), `caveau`, `ringroide`, `Halite`, `Bulk Freighter`, `Costruttori`,
   `il Rim`, `il Nucleo`, `Twilight Guard`, `Egemonia Bunrodean`, `Wanderers`, istituzioni in inglese.

---

## 6. Controlli

| Controllo | Esito |
|---|---|
| Indici: 83 attesi, 83 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (83/83) | OK |
| `english`/`kind`/`path`/`state` identici al DB (83/83) | OK |
| Traduzioni vuote / duplicati EN e IT | 0 |
| Tab: totale invariato (27) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (14) | **1 → 0** dopo correzione |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,89–1,20 | OK |
| Tipografia: accenti sostitutivi, ellissi tipografiche, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | 0 / 0 |

`check.py`: `FAIL totale: 1` al primo passaggio (unità 26), **`FAIL totale: 0`** dopo la correzione.

---

## 7. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L13 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 8. Artefatti

```
endless-sky-l10n/staging/editorial/L14_20261017_194328/
├── source.json       83 unità (idx, id, riga, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json  83 unità (idx, id, riga, contesto, inglese, italiano, ratio)
├── review.md         convenzioni, 13 interventi, il FAIL e la sua correzione
├── REPORT.md         questo report
├── parts/            part01 (1–21), part02 (22–42), part03 (43–63), part04 (64–83)
└── check.py, verify.py
```

---

## 9. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 83 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 1.495 unità · 80.994 parole inglesi → 80.697 italiane.**
