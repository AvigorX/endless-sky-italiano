# L17 — `data/human/human missions.txt` 568–980

**Data:** 2026-10-17 · **Esito: lotto completo, 133/133 unità, 0 omissioni · FAIL totale: 0**
**Directory:** `endless-sky-l10n/staging/editorial/L17_20261017_195800/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/human/human missions.txt` |
| Intervallo | righe **568–980** |
| Unità | **133** (`PENDING`) |
| Parole | **4.128** inglesi → **3.788** italiane |
| Rapporto | 0,66 – 1,50 |
| Missioni | **11** — `Smuggler's Den` 1 e 2, `Payment`, `Follow Up`, `Expedition to Hope` 1 e 2, `Transport Workers` A/B/C, `WR Star 1`, `There Might Be Riots 1` |
| Tab | 84 |
| Virgolette | 214 |
| Token `<...>` | 66 |

Progresso del file: **314 unità su 4.253** (7,4%). Restano 3.939 unità / 95.385 parole dopo la riga 980.

---

## 2. Tipi e trattamento

| Tipo | Unità | Trattamento |
|---|---:|---|
| `MISSION_TEXT` | 95 | tradotto |
| `DIALOG` | 13 | tradotto |
| `VALUE` | 9 | `name` della missione: tradotto, token conservati |
| `DESCRIPTION` | 9 | tradotto |
| `LOGBOOK` | 6 | tradotto |
| `UI_LABEL` | 1 | **`label "towns syndicate"` identica** |

Token conservati: `<planet>` 18 · `<payment>` 12 · `<destination>` 11 · `<bunks>` 7 · `<origin>` 4 ·
`<tons>` 4 · `<last>` 3 · `<cargo>` 3 · `<waypoints>` 3 · `<fare>` 1.

---

## 3. Esempi rappresentativi

**Unità 3 — l'agguato nel bar (apertura di `Smuggler's Den`)**

> You wander into one of several dimly lit, smoke-filled bars near your docking bay. Soon after you sit
> down, a pair of hooded figures stand up and begin moving toward you.

> Ti infili in uno dei tanti bar poco illuminati e pieni di fumo vicino alla tua piazzola di atterraggio.
> Poco dopo che ti sei seduto, due figure incappucciate si alzano e cominciano a muoversi verso di te.

**Unità 24 — il tunnel di servizio**

> Finally, you reach the back entrance, and she spins the wheel to unlock it... The floor of the corridor
> is littered with beer bottles and discarded hypodermic needles.

> Alla fine raggiungete l'ingresso sul retro, e lei gira il volante per aprirlo... Il pavimento del
> corridoio è cosparso di bottiglie di birra e aghi ipodermici abbandonati.

**Unità 61 — la spedizione a Hope**

> "My family lived on Hope back then. We want to measure how much ash is still in the air, to see how long
> it will be before the glaciers recede and the planet is habitable again."

> "La mia famiglia viveva su Hope allora. Vogliamo misurare quanta cenere è ancora nell'aria, per capire
> quanto tempo passerà prima che i ghiacciai si ritirino e il pianeta torni abitabile."

**Unità 68 — il villaggio sotto il ghiaccio**

> "That's my old house, down there," says one of the scientists, pointing to the radar picture of one of the
> buried villages. "Under thirty meters of ice, now."

> "Quella laggiù è la mia vecchia casa," dice uno degli scienziati, indicando l'immagine radar di uno dei
> villaggi sepolti. "Ora sotto trenta metri di ghiaccio."

**Unità 119 — la band assediata dai fan**

> About a half an hour later the road crew begins carting instruments and amplifiers into your cargo hold...
> It takes you a second to realize they're not angry or bent on destruction - they're just a group of crazy
> fans.

> Circa mezz'ora dopo la troupe comincia a portare strumenti e amplificatori nella stiva... Ti serve un
> secondo per capire che non sono arrabbiati né intenzionati a distruggere nulla: sono solo un gruppo di fan
> scatenati.

---

## 4. Controlli

| Controllo | Esito |
|---|---|
| Indici: 133 attesi, 133 presenti | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (133/133) | OK |
| `english`/`kind`/`path` identici al DB · `state = PENDING` | 133/133 · 133/133 |
| Traduzioni vuote | 0 |
| Duplicati italiano | 0 (ammessi i nomi di missione 1/35 e 55/66 e il DIALOG 34/44) |
| Duplicati inglese | 4 (ripetizioni del sorgente, documentate) |
| `label` lasciate identiche | 1/1 |
| Tab / virgolette / token `<...>` / backtick | 84/84 · 214/214 · 66/66 · 0/0 |
| Spazi doppi, ai bordi, newline interne | 0 |
| Rapporto di lunghezza | 0,66 – 1,50 |
| Tipografia (accenti sostitutivi, ellissi, caporali, em dash, apostrofi curvi) | 0 |
| Parole inglesi residue | 0 (titoli di band e canzoni esclusi dal controllo, vedi §5) |
| Anglicismi evitabili | 0 |

Due errori miei rilevati dal checker: tab iniziale mancante sull'unità 101 e rapporto 1,75 sull'unità 128
(battuta di 8 caratteri), corretti in "Ma certo!".

---

## 5. Correzione al checker, dichiarata

`check.py` segnalava `there`, `be`, `your` nelle unità 112, 122, 125, 126: sono dentro **`There Might Be
Riots`** e **`Henhouse In Your Soul`**, titoli che restano in inglese per scelta. Il controllo ora rimuove
quei due titoli **prima** di scansionare (`TITLES` nel codice), invece di allentare la regex: l'elenco è
esplicito, non è una deroga generale.

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | 364 / 32.560, `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L16 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L17_20261017_195800/
├── source.json       133 unità (idx, id, riga, tipo, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json   133 unità (…, italiano, ratio)
├── review.md          ricognizione, convenzioni, interventi, correzione al checker
├── REPORT.md          questo report
├── parts/             part01 (1–34), part02 (35–66), part03 (67–99), part04 (100–133)
└── check.py, verify.py
```

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 133 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 1.858 unità · 92.801 parole inglesi → 91.986 italiane.**
