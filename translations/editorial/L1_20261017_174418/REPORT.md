# L1 — Traduzione editoriale del primo blocco

**Data:** 2026-10-17 · **Esito: blocco completo, 120/120 unità, 0 omissioni**
**Directory:** `endless-sky-l10n/staging/editorial/L1_20261017_174418/`

---

## 1. Cosa è stato tradotto

| Voce | Valore |
|---|---|
| File | `data/map planets.txt` |
| Intervallo | righe **3851–4295** (contigue) |
| Unità | **120** (tutte `DESCRIPTION`, tutte `PENDING`) |
| Parole | **5.230** inglesi → **5.167** italiane |
| Rapporto di lunghezza | 0,87 – 1,24 |
| Con tab di paragrafo | 63 |
| Con virgolette | 5 |
| Con token dinamici | **0** |

Il blocco è un capitolo coerente: le descrizioni dei pianeti da **Neriene** a **Oblivion**, in ordine di
file. Nessuna unità approvata è stata inclusa, nessun duplicato (verificato: 0 testi ripetuti), tutte
visibili al giocatore nel pannello del pianeta.

**Perché questo blocco:** il criterio chiedeva contenuti lineari e una sezione trattabile come capitolo.
Ho misurato i candidati: solo `_ui/tooltips.txt` offriva blocchi contigui ampi, ma sono formule tecniche
ripetitive; `map planets.txt` offre 120 descrizioni in 445 righe, con lore e registro narrativo, senza
token dinamici — la scelta più adatta alla prova editoriale. Il secondo candidato per densità
(`human/jobs.txt`) mescola registri e ha struttura più frammentata.

---

## 2. Esempi rappresentativi

**Unità 14 — `planet:New Boston`**

> New Boston is a completely unremarkable world... except, of course, for the fact that you happen to
> have been born here.

> New Boston è un mondo del tutto insignificante... tranne, naturalmente, per il fatto che ci sei nato tu.

**Unità 45 — `planet:New Iceland`**

> Almost as soon as you stepped off your ship, your eyes began to sting. You try to breathe as
> shallowly as possible.

> Quasi appena sei sceso dalla nave, gli occhi hanno cominciato a bruciarti. Cerchi di respirare il più
> superficialmente possibile.

**Unità 54 — `planet:New Kansas`**

> However, unwary travelers hiking through the idyllic countryside have been known to be attacked by
> savage packs of feral sheep, so this world is not without unique dangers of its own.

> Tuttavia, viaggiatori incauti che camminano per questa campagna idilliaca sono stati aggrediti da
> branchi selvatici di pecore inselvatichite: questo mondo ha anche i suoi pericoli peculiari.

**Unità 88 — `planet:New Washington`**

> Rats, accidentally introduced by the settlers, also flourish here. A small, nearly deserted cafeteria
> is selling stew and mashed potatoes. You are almost certain the stew is made with rat meat.

> Anche i ratti, introdotti per caso dai coloni, prosperano. Una piccola mensa quasi deserta vende
> stufato e purè di patate. Sei quasi certo che lo stufato sia fatto con carne di ratto.

**Unità 110 — `planet:O-Vasa-Oa`**

> Many within the New Houses object to that moniker, arguing that their family lines are in fact the
> more extensive and noble and that they should be categorized by that, rather than their time of arrival.

> Molti tra le Nuove Casate contestano quel nomignolo, sostenendo che le loro stirpi sono in realtà più
> ramificate e più nobili e che dovrebbero essere classificate in base a questo, non al momento del loro
> arrivo.

---

## 3. Controlli eseguiti

Controllo temporaneo (`assemble_and_check.py`), nessun database, nessuno stato, nessuna regola nuova.
Risultato in `check_results.json`.

| Controllo | Esito |
|---|---|
| ID e indici: 120 attesi, 120 presenti, 0 duplicati, 0 estranei | ✅ |
| Nessuna traduzione vuota | ✅ |
| Tab: numero invariato e tab di paragrafo iniziale conservato (63 unità) | ✅ |
| Virgolette: stesso conteggio per unità (5 unità con dialoghi/citazioni) | ✅ |
| Token `<...>`: multinsiemi identici (0 attesi, 0 trovati) | ✅ |
| Spazi doppi e spazi ai bordi | ✅ |
| Rapporto di lunghezza 0,87–1,24 (nessun troncamento, nessuna espansione sospetta) | ✅ |
| **Problemi totali** | **0** |

Due segnalazioni automatiche di "parola inglese residua" (unità 5 e 6) sono i nomi propri
**"The Grange"**: attese, verificate a mano, non errori.

---

## 4. Revisione editoriale

Rilettura del solo italiano con 11 correzioni, documentate in `review.md` §4 (calchi rimossi:
"abbastanza povero che" → "così povero che", "città tentacolari" → "sconfinate", "colture da fibra" →
"piante da fibra", ecc.).

Nomi propri: pianeti, fazioni e regioni restano in inglese secondo il glossario; `Mars`/`Earth` diventano
Marte/Terra perché sono corpi reali; `Syndicate` è reso "Sindacato" (parola comune); `Bulk Freighters` →
"mercantili pesanti" (classe descrittiva). Dettaglio in `review.md` §2.

---

## 5. Ambiguità rimaste aperte

1. **`New Houses` → "Nuove Casate"**: scelta mia, da ratificare se altrove è trattato come nome proprio.
2. **`Remembrance Day` invariato**: se si decide di tradurre le ricorrenze, va fatto in tutto il corpus.
3. **`Syndicate` → "Sindacato"**: nessun precedente approvato, decisione di universo da confermare.
4. **`square dances` / `line dances`** (unità 5): "quadriglie e danze in fila" è la resa meno straniante,
   ma il riferimento culturale resta americano.
5. **Termini di K4**: `discharge`, `disruption`, `scrambling` **non compaiono** in questo blocco
   (verificato). Le decisioni terminologiche restano aperte e non sono state toccate.

---

## 6. Unità non tradotte

**Nessuna.** 120 selezionate, 120 tradotte. Non ci sono state unità scartate per struttura ambigua,
token dubbi o testo non traducibile.

---

## 7. Integrità

| Voce | Atteso | Osservato | Esito |
|---|---|---|---|
| `endless-sky` HEAD / modifiche | `b4aa3bac3` / 0 | identico / 0 righe | ✅ |
| `endless-sky-mingw` | 4 file `M` (patch UTF-8 preesistente) | 4 file `M` | ✅ |
| `state.db` | 364 / 32.560, nessuna scrittura | `9125282973ddc8b9`, ultimo evento `14:33:18Z` | ✅ |
| Batch | B001–B006 | B001–B006, nessun B007 | ✅ |
| `glossary.csv` | invariato | `94e785f68be271d8` | ✅ |
| `staging/inventory_fields.csv` | invariato | `c9d8bc651cd70c56` | ✅ |
| `tools/l10n.py` | invariato (patch K4 non applicata) | `743c6a3f8c217f35` | ✅ |
| Output approvati | 3 hash del checkpoint | `5912ad73…` · `2cf104fe…` · `1e010853…` | ✅ |
| Build / test / packaging | non eseguiti | non eseguiti | ✅ |
| Traduzioni applicate al gioco | nessuna | nessuna | ✅ |

Nessuna patch K4 è stata applicata. Nessun file del gioco è stato modificato: il testo tradotto vive
solo in `translation.json`.

---

## 8. Artefatti

```
endless-sky-l10n/staging/editorial/L1_20261017_174418/
├── source.json              120 unità: id, path, riga, contesto, inglese, delimitatore, riga grezza
├── translation.json         120 unità: id, riga, inglese, italiano, ratio
├── review.md                decisioni, correzioni, ambiguità
├── check_results.json       esiti dei controlli
├── REPORT.md                questo report
├── parts/part01..04.json    traduzioni per gruppo (tracciabilità del lavoro)
├── export_source.py         esporta il blocco (sola lettura)
└── assemble_and_check.py    assembla e controlla (nessun DB, nessuno stato)
```

Ogni voce di `translation.json` conserva `line` e `raw` (in `source.json`), quindi si risale
esattamente alla riga originale del file. Riproduzione:

```bash
cd endless-sky-l10n/staging/editorial/L1_20261017_174418
python export_source.py        # 120 unità, 5230 parole
python assemble_and_check.py   # exit 0, 0 problemi
```

---

## 9. Cosa non è stato fatto

- Nessuna applicazione al gioco, nessun batch, nessuna build, nessun packaging.
- Nessuna modifica a `state.db`, glossario, inventario, output approvati, sorgenti o dati.
- **Rendering non verificato** (nessun avvio del gioco, come da mandato).

Pronto per la revisione: il passo successivo può essere un secondo blocco con lo stesso metodo, oppure
la ratifica delle quattro decisioni di §5 prima di allargare il volume.
