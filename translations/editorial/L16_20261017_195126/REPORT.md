# L16 — Primo lotto di `data/human/human missions.txt` (missioni)

**Data:** 2026-10-17 · **Esito: lotto completo, 181/181 unità, 0 omissioni · FAIL totale: 0**
**Directory:** `endless-sky-l10n/staging/editorial/L16_20261017_195126/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/human/human missions.txt` |
| Intervallo | righe **23–562** |
| Unità | **181** (`PENDING`) |
| Parole | **4.986** inglesi → **4.745** italiane |
| Rapporto | 0,67 – 1,61 |
| Missioni | **8** — `Raid Warning`, `Hunted Warning`, `Immigrant Workers`, `Pookie` 1–5 |
| Tab di paragrafo | 148 |
| Virgolette | 203 |
| Token `<...>` | 23 |

Il file è il più grande del corpus (4.253 unità, 104.499 parole). Questo lotto ne copre **181 unità
(4,3%)**; ne restano 4.072 dopo la riga 562.

---

## 2. Tipi di unità e trattamento

| Tipo | Unità | Trattamento |
|---|---:|---|
| `MISSION_TEXT` | 158 | tradotto |
| `LOGBOOK` | 8 | tradotto |
| `DESCRIPTION` | 4 | tradotto |
| `DIALOG` | 4 | tradotto |
| `VALUE` | 3 | `name` della missione: tradotto ("Stray Dog" → "Cane randagio"), invariato il nome proprio |
| `UI_LABEL` | 4 | **`label` di salto: identiche all'inglese** |

Le quattro etichette (`not poor`, `no bet`, `nope late`, `remember decline`) sono bersagli di `goto`:
tradurle romperebbe il flusso della missione. Sono l'unico caso in cui il controllo accetta testo non
tradotto, con elenco esplicito nel checker.

---

## 3. Collocazione e continuità

```
unita: 181 righe 23 - 562
unita successiva nel file: (568, "mission:Smuggler's Den, Part 1")
```

Il confine è a **fine missione**: l'unità 562 chiude `Pookie, Part 5`, l'unità 568 apre
`Smuggler's Den, Part 1`. Nessun dialogo tagliato a metà.

**Riga 555 — `log` tripla.** Il sorgente ha ``log `Minor People` `Puny` `A poodle ...` `` e il database la
spezza in tre unità sulla stessa riga: 176 (categoria), 177 (nome), 178 (testo). Il tripletto è verificato
da `verify.py`: `OK`. Chi applicherà le traduzioni dovrà ricomporre la riga con tutte e tre.

---

## 4. Esempi rappresentativi

**Unità 1 — apertura di `Raid Warning`**

> When you enter the spaceport at <origin>, you are almost immediately stopped by a grumpy old
> man. "Are you some kind of greenhorn, or are you asking for death?" he asks you.

> Quando entri nello spazioporto di <origin>, vieni quasi subito fermato da un vecchio burbero. "Sei una
> specie di pivello, o stai chiedendo la morte?" ti chiede.

**Unità 12 — avvertimento sui pirati**

> "Or you get more guns on that fleet or lose some cargo space. Park the ships, sell them, I don't care,
> as long as pirates don't see them, or you make the effort of stealing what you could have not worth
> their while."

> "O ti procuri più cannoni in quella flotta o ti liberi di un po' di spazio per il carico. Parcheggia le
> navi, vendile, non importa, basta che i pirati non le vedano, o che tu renda lo sforzo di rubare quello
> che potresti avere non conveniente."

**Unità 43 — l'offerta della barboncina**

> "You look like the sort of captain I can trust," she says. "My darling Pookie has been visiting her aunt
> on Shroud... Can you do that for me?"

> "Lei sembra il tipo di capitano di cui mi posso fidare," dice. "La mia adorata Pookie è andata a trovare
> sua zia su Shroud... Può farlo per me?"

**Unità 103 — la sparatoria nel complesso di corse**

> Suddenly, a gunshot rings out throughout the building. The two beasts fall over as the stagehand steps
> forward holding a shotgun.

> All'improvviso uno sparo risuona in tutto l'edificio. Le due bestie crollano mentre il macchinista
> avanza con il fucile in mano.

**Unità 175 — voce di diario**

> Saved a dog from a hound-racing ring, and tried to give her a home. However, her alleged owner rejected
> her. Eventually decided to give her up for adoption.

> Hai salvato una cagna da un anello di corse di segugi e hai cercato di darle una casa. La presunta
> padrona però l'ha rifiutata. Alla fine hai deciso di darla in adozione.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 181 attesi, 181 presenti | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (181/181) | OK |
| `english`/`kind`/`path` identici al DB (181/181) · `state = PENDING` (181/181) | OK |
| Traduzioni vuote | 0 |
| Duplicati italiano | 0 (escluso `Pookie` 40/45, nome proprio) |
| Duplicati inglese | **4** — ripetizioni del sorgente: 40/45, 120/121, 122/126, 123/125 |
| `label` lasciate identiche | 4/4 |
| Tab: 148/148, tab iniziale conservato unità per unità | OK |
| Virgolette: 203/203, stesso conteggio per unità | OK |
| Token `<...>`: multinsiemi identici (23) | OK |
| Backtick | 0/0 |
| Spazi doppi / ai bordi / newline interne | 0 |
| Rapporto di lunghezza 0,67–1,61 | OK (battute brevissime) |
| Tipografia: accenti sostitutivi, ellissi tipografiche, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | 0 / 0 |
| Tripletto `log` alla riga 555 | OK |

Due errori miei rilevati dal checker e corretti: tab iniziale di troppo su 127 e 130.

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | 364 / 32.560, `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L15 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L16_20261017_195126/
├── source.json       181 unità (idx, id, riga, tipo, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json   181 unità (…, italiano, ratio) — `kind` conservato
├── review.md          ricognizione dei tipi, convenzioni, 10 interventi, decisioni aperte
├── REPORT.md          questo report
├── parts/             part01 (1–36), part02 (37–72), part03 (73–108), part04 (109–144), part05 (145–181)
└── check.py, verify.py
```

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato): in particolare non è osservato
  come il gioco presenta le `label` non tradotte né la categoria di diario "Personaggi minori".
- Le 181 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 1.725 unità · 88.673 parole inglesi → 88.198 italiane.**
