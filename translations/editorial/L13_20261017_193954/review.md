# L13 — Revisione editoriale del blocco `data/map planets.txt` 2913–3231

79 descrizioni, 4.585 parole inglesi → 4.592 italiane. Nono lotto del tratto iniziale del file, nessun ID
in comune con L1–L12. Inizia con `planet:Kapnos` e si chiude a fine pianeta con `planet:Limejog`
(riga 3231); la successiva (riga 3239) apre Livolua.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–20, 21–40, 41–60, 61–79), rilettura
del solo italiano.

Le 79 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 79 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Successors` | invariato | 24 → 24 | convenzione L7 |
| `Predecessors` | Predecessori | 3 → 3 | §6 del checkpoint; `Predecessors' empire` → "impero dei Predecessori" |
| `Korath`, `Kor Sestor`, `Quarg`, `Kimek`, `Avgi`, `Antecessors`, `Remnant` | invariati | 13/2/8/3/3/1/1 | — |
| `Wanderers` | **invariato** | 6 → 6 | fazione nuova: trattata come `Remnant`/`Heliarch`, da ratificare |
| `Hai` | invariato | 2 → 2 | la terza occorrenza del conteggio è il verbo italiano *hai* |
| `High Houses` / `New Houses` / `Old Houses` | Alte / Nuove / Vecchie Casate | 2 / 3 / 3 | — |
| `House Aqrabe`, `House Kaatriij` | Casata Aqrabe, Casata Kaatriij | 2 → 2 | attenzione: qui il sorgente scrive **Kaatriij** (doppia i), mentre L12 scriveva `Kaatrij` |
| `"People's Houses"` | "Casate del Popolo" | 1 → 1 | virgolette conservate |
| `Key Stones` | Pietre Chiave | 2 → 2 | §7 del checkpoint |
| `ringworld(s)` | mondo/mondi ad anello | 5 → 5 | — |
| `Milky Way` | Via Lattea | 3 → 3 | — |
| `Sol system` | sistema solare | 1 → 1 | `Sol` resta invariato come nome della stella |
| `Lagrangian point` | punto di Lagrange | 1 → 1 | — |
| `super-Earth` | super-Terra | 1 → 1 | termine astronomico corrente |
| `Hai-Korath war` | guerra Hai-Korath | 1 → 1 | — |

Nomi propri invariati: Kapnos, Karek Fornati, Kasi-Osolaa-Sossa, Kasichara Fet, Kasii-Cavasaa-Oa,
Kasii-Tuur-Saqru, Katkradol, Kella-Uuoru-Sossa, Keneska Fek, Kessel Sepret, Khora-Uurau-Uuoru,
Khora-Vasa-Reyyaa, Khosa-Kella-Oa, Ki Patek Ka, Kisarra, Korati Efreti, Korbatri Eska, Kort Kehai,
Kort Vek'kri, Kraken, Kua-Oa-Aava, Kuj-Sol-Nnesa, Kumkapi, Kuwaru Efreti, Lagrange, Laki Nemparu,
Lenz's Loop, Letis'sei, Leviathan, Lichen, Limejog, Viminal, Peresedersi, Kochab, Palavret, Aava-Aasa-Khora.

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 11 | "chiacchiere **ozose**" → "oziose" | refuso mio, corretto prima dei controlli |
| 61 | "un Quarg **emerga** all'improvviso" → "un Quarg **spunta**" | concordanza: il verbo era al congiuntivo senza reggente |
| 1 | `"gas torus"` → "toro di gas" | termine astronomico; virgolette conservate |
| 3 | `"sand seas"` → "mari di sabbia" | — |
| 16 | `what human scientists would call a "super-Earth"` → "quella che gli scienziati umani chiamerebbero una super-Terra" | — |
| 19 / 20 | due varianti quasi identiche dello stesso spazioporto | differenze conservate ("Un paio di piccoli droni" / "Uno stormo di piccoli droni") |
| 33 | `"hunger towers"` → "torri della fame" | — |
| 37 | `Kissara` (grafia del sorgente) → **Kisarra** | refuso del sorgente: il pianeta è `Kisarra` nel nome del nodo e nell'unità 35. Quarto refuso incontrato |
| 63 | `so far beyond anything human beings have ever attempted to build` → "così al di là di qualsiasi cosa gli esseri umani abbiano mai tentato di costruire" | resa letterale ma naturale |
| 69 | `cannon-like structures` → "strutture simili a cannoni" | — |
| 72 | `you get some small satisfaction` → "ricavi una piccola soddisfazione" | — |

Nessun errore imposto dai controlli: `check.py` passa con `FAIL totale: 0` al primo tentativo.

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`House Kaatriij` vs `House Kaatrij`**: il sorgente alterna le due grafie (L12 `Kaatrij`, L13
   `Kaatriij`). Ho mantenuto quella di ciascuna unità senza normalizzare, perché non è chiaro quale sia
   corretta. Da decidere: se è un refuso, va corretto in entrambi i lotti.
2. **`Wanderers` invariato** (6): fazione nuova. Coerente con `Remnant`/`Heliarch`/`Unfettered`, ma va
   ratificato, e con esso `Wanderer spaceport` → "spazioporto dei Wanderers".
3. **`Kissara` → `Kisarra`** (1): quarto refuso del sorgente dopo `Cavasaa-Vasa-Tej` (L7), `Unlikely` (L8) e
   `Kasii-Cavasaa` (L9).
4. **`Lenz's Loop` invariato** (1): nome proprio con apostrofo inglese; l'apostrofo è dritto, quindi
   compatibile con la regola tipografica.
5. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `Consigli Confederati` (L10/L12) vs
   `Confederated Councils` (L6), `caveau`, `ringroide`, `Halite`, `Bulk Freighter`, `Costruttori`,
   `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`, `Egemonia Bunrodean`, istituzioni in inglese.

---

## 5. Esito dei controlli

```
unità 79 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4585 -> 4592 · ratio 0.92-1.21
tab 21 (tutti gli iniziali conservati) · virgolette 12 (6 coppie) · token <...> 0
riga grezza identica al file: 79/79 · english/kind/path/state identici al DB: 79/79
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
