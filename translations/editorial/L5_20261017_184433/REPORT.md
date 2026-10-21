# L5 — Primo lotto del tratto iniziale di `data/map planets.txt`

**Data:** 2026-10-17 · **Esito: lotto completo, 84/84 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L5_20261017_184433/`

---

## 1. Blocco tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **17–356** |
| Posizione | **inizio del file**, tratto mai affrontato prima (righe 17–3845) |
| Unità | **84** (`DESCRIPTION`, tutte `PENDING`) |
| Parole | **4.632** inglesi → **4.578** italiane |
| Rapporto | 0,85 – 1,22 |
| Pianeti | **31** (da **Aava-Aasa-Khora** a **Arroharg**) |
| Tab di paragrafo | 33 |
| Virgolette | 14 (unità 6, 21, 27, 45) |
| Token `<...>` | 0 |

Il blocco si chiude a fine pianeta con Arroharg; l'unità 357 appartiene ancora ad Arroharg ed è esclusa,
come previsto dal confine calcolato. Nessun testo tagliato a metà, nessuna unità saltata.

**Perché conta:** L1 era partito dalla riga 3851 lasciando indietro l'inizio del file (871 unità,
48.092 parole). L5 è il primo lotto che entra in quel tratto: dopo di esso ne restano **787 unità /
~43.460 parole** (righe 357–3845).

---

## 2. Esempi rappresentativi

**Unità 1 — `planet:Aava-Aasa-Khora`**

> This planet is the collective seat of what are known as the Old Houses, the noble families who held
> territorial claims to this region of space before the collapse of the Predecessors' empire and the
> arrival of the so-called New Houses fleeing their crumbling society.

> Questo pianeta è la sede collettiva di quelle che sono note come le Vecchie Casate, le famiglie
> nobiliari che vantavano pretese territoriali su questa regione dello spazio prima del collasso
> dell'impero dei Predecessori e dell'arrivo delle cosiddette Nuove Casate, in fuga dalla loro società in
> rovina.

**Unità 6 — `planet:Ablub's Invention`**

> The day-night cycle here is at least three times as long as any of the Coalition's species are
> habituated to, so the entire city enters a "false nighttime" in the middle of the day, shuttering all
> the windows so that the locals can rest and reset their biological clocks.

> Qui il ciclo giorno-notte è almeno tre volte più lungo di quello a cui è abituata qualsiasi specie della
> Coalizione, perciò l'intera città entra in una "notte finta" a metà giornata, chiudendo tutte le
> finestre perché la gente del posto possa riposare e riallineare il proprio orologio biologico.

**Unità 27 — `planet:Albatross`**

> The sign over the spaceport bar reads, "No Gods, No Masters." Below it in slightly smaller writing is
> another sign which reads, "No Cybernetic Implants. No Badgers, Weasels, Or Polecats." You have no idea
> what a "polecat" is.

> L'insegna sopra il bar dello spazioporto recita: "Né dèi né padroni". Sotto, con caratteri un po' più
> piccoli, ce n'è un'altra che dice: "Niente impianti cibernetici. Niente tassi, donnole o polecat". Non
> hai idea di cosa sia un "polecat".

**Unità 45 — `planet:Alvorada`**

> Rumor has it that, in the deepest reaches of the complex where no pirates have yet been able to
> breach, they're still there, having adapted the system to instead direct the guerrillas in the
> reestablishment of their homeland.

> Corre voce che, nei recessi più profondi del complesso, dove nessun pirata è ancora riuscito a
> penetrare, siano ancora lì, dopo aver adattato il sistema per dirigere invece i guerriglieri nella
> ricostruzione della loro patria.

**Unità 69 — `planet:Antivli Station`**

> Whatever happened to the antimatter, it is at least certain that it did not breach its magnetic
> levitation containment tanks, as otherwise nothing of the station would be left but vapor.

> Qualunque cosa sia successo all'antimateria, è almeno certo che non ha perforato i serbatoi di
> contenimento a levitazione magnetica, altrimenti della stazione non sarebbe rimasto che vapore.

**Unità 83 — `planet:Arroharg`**

> The lower levels of the outpost seem to dig deeper into the surface of the moon, but the farther they
> go down, the more complex they become. There's no telling how deep into the moon they go, as they are
> restricted to everyone but the Quarg.

> I livelli inferiori dell'avamposto sembrano scavare sempre più a fondo nella superficie della luna, ma
> più scendono, più diventano complessi. Non si può dire quanto in profondità arrivino, perché sono
> vietati a tutti tranne che ai Quarg.

---

## 3. Interventi editoriali

Otto interventi in stesura e rilettura (dettaglio in `review.md` §3), più una correzione imposta dal
controllo: **unità 27 aveva 4 virgolette contro le 6 dell'inglese** perché avevo sciolto le virgolette
intorno a "polecat" nella frase finale; ripristinate.

| Termine | Resa | Occorrenze |
|---|---|---|
| `polecat` | **invariato** | 2 (eccezione stilistica: la battuta vive sull'opacità del termine) |
| `skyhook` | invariato | 1 |
| `regolith` | regolite | 2 |
| `antimatter` | antimateria | 9 |
| `Old Houses` / `New Houses` | Vecchie / Nuove Casate | 1 / 1 |

Nota di resa: `oil derricks` → "torri di perforazione"; `mobiles` (arte) → "sculture cinetiche";
`razed from orbit` → "polverizzato dall'orbita"; `greasy spoon diners` → "trattorie da quattro soldi".

---

## 4. Decisioni ancora aperte

1. **`polecat` invariato** (unità 27): unico inglese lasciato nel testo per non perdere la battuta. Va
   registrato come eccezione, non ripetuto altrove senza motivo.
2. **`skyhook` invariato** (unità 80): alternativa "gancio celeste", da decidere se ricorre in altri file.
3. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `longcows`,
   `Key Stones` → Pietre Chiave, `il Rim` / `the Deep`.

---

## 5. Controlli

| Controllo | Esito |
|---|---|
| Indici: 84 attesi, 84 presenti, 0 mancanti, 0 estranei | OK |
| ID univoci, allineati a `source.json` | OK |
| `raw` identica alla riga del file (84/84) | OK |
| `english`/`kind`/`path`/`state` identici al DB (84/84) | OK |
| Traduzioni vuote / duplicati EN e IT | 0 |
| Tab: totale invariato (33) e tab iniziale conservato unità per unità | OK |
| Virgolette: stesso conteggio per unità (14) | OK dopo correzione dell'unità 27 |
| Token `<...>`: multinsiemi identici (0) | OK |
| Spazi doppi / ai bordi / newline interne | OK |
| Rapporto di lunghezza 0,85–1,22 | OK |
| Tipografia: accenti sostitutivi, ellissi, caporali, em dash, apostrofi curvi | 0 |
| Parole inglesi residue / anglicismi evitabili | 0 / 0 |

`check.py`: `FAIL totale: 0` (dopo una correzione, virgolette unità 27).

---

## 6. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 | OK |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | OK |
| Batch · glossario · inventario · `tools/l10n.py` · output approvati | invariati | hash invariati | OK |
| L1–L4 | intatti | hash invariati | OK |
| Build / test / packaging | non eseguiti | non eseguiti | OK |

---

## 7. Artefatti

```
endless-sky-l10n/staging/editorial/L5_20261017_184433/
├── source.json       84 unità (idx, id, riga, contesto, inglese, delimitatore, tab, riga grezza, hash)
├── translation.json  84 unità (idx, id, riga, contesto, inglese, italiano, ratio)
├── review.md         convenzioni, 8 interventi, eccezioni (`polecat`, `skyhook`)
├── REPORT.md         questo report
├── parts/            part01 (1–21), part02 (22–42), part03 (43–63), part04 (64–84)
└── check.py, verify.py
```

---

## 8. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).
- Le 84 unità sono **tradotte in staging e restano `PENDING`**.

**Totale editoriale complessivo: 757 unità · 40.227 parole inglesi → 39.966 italiane.**
