# L8 — Revisione editoriale del blocco `data/map planets.txt` 1082–1389

77 descrizioni, 4.534 parole inglesi → 4.486 italiane. Quarto lotto del tratto iniziale del file, nessun
ID in comune con L1–L7. Inizia con `planet:Cyreal` e si chiude a fine pianeta con `planet:Dustmaker`
(riga 1389); l'unità successiva (riga 1395) apre Dwelling of Speloog.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in gruppi nell'ordine del file (1–20, 21–45, 46–65, 66–77), rilettura del solo
italiano.

Le 77 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 77 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Avgi` | invariato | 3 → 3 | specie |
| `Hai` | invariato | 9 → 9 | il decimo "Hai" del conteggio automatico è il verbo italiano *hai* (unità 11) |
| `Unfettered` | invariato | 1 → 1 | sub-fazione Hai; tra virgolette anche in italiano (unità 10) |
| `Saryd` / `Saryds` | invariato | 3 → 3 | — |
| `Kimek`, `Arachi`, `Heliarch`, `Gegno`, `Scin`, `Korath`, `Kor Sestor`, `Quarg`, `Lunarium` | invariati | 1/2/2/7/4/5/1/1/1 | specie e fazioni |
| `Twilight Guard` | **invariato** | 1 → 1 | nome di fazione (come `Remnant`, `Heliarch`): da ratificare |
| `Coalition` | Coalizione | 2 → 2 | decisione L2 |
| `Syndicate` | Sindacato | 3 → 3 | convenzione L1 |
| `Republic` | Repubblica | 1 → 1 | — |
| `Earth` | Terra | 5 → 5 | 2 casi diretti (unità 4, 37) + 3 aggettivi `Earth-like` → "terrestre" |
| `House Ablomab` | Casata Ablomab | 1 → 1 | `house X` → Casata X |
| `Kingsburg Corporation`, `Poseidon Industries` | invariati | 1 / 1 | ragioni sociali |
| `Bulk Freighter` | **invariato** | 1 → 1 | classe di nave, come `Halite` in L7: da ratificare |
| `spaceplanes` | spazioplani | 1 → 1 | nome comune |
| `hyperdrive` / `hyperspace` | iperpropulsore / iperspazio | 1 / 2 | glossario |
| `terraforming` | terraformazione | 2 → 2 | — |
| `oil` / `petroleum` | petrolio | 2 `petroleum` + altri `oil` | una sola resa: "petrolio" |
| `Unfettered`, `Korath` ecc. | invariati | — | — |

Nomi di pianeti, stazioni, stelle e sistemi restano invariati: Cyreal, Span, Dagon, Dancer, Darkcloak,
Darkmetal, Darkrest, Darkstone, Darkwaste, Deadman's Cove, Deep, Deep Treasure, Deep Water,
Deka Dathnak, Deli Kasi, Deli Kat, Delodir, Delve, Delve of Bloptab, Bloptab's Furnace, Desi Seledrak,
Devru Kaska, Diligent Hand, Disara, Dlia Jzaur, Dokimi Range, Double Haze, Drekag Firask, Dueitch Ae,
Dueyu Eitch, Dune, Dusk Companion, Dustmaker, Mote, Sol.

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 52 | sorgente `Unlikely many other worlds` → letto come **"Unlike"** | è un refuso: la frase regge solo con "a differenza di". Segnalato, non propagato |
| 53 | sorgente `which a large base garrisoned with…` (frase agrammaticale) → "con una grande base presidiata da…" | reso il senso senza riprodurre l'inciampo sintattico |
| 43 | "una rete di travi e reti metalliche" → "un'intelaiatura di travi e maglie d'acciaio" | ripetizione di "rete" nello stesso periodo |
| 39 | bozza con ripetizione ("stilla stilla") → "arriva alla biosfera poco alla volta" | errore di stesura, non del testo |
| 8 | `moving awfully fast` → "si muovono maledettamente in fretta" | registro colloquiale della voce narrante, come in originale |
| 13 | `ingest layers of dirt and bedrock` → "inghiottono strati di terra e roccia" | evita "ingerire", troppo tecnico per un veicolo minerario |
| 24 | `Deep is a sparsely populated world` → "Deep è un mondo scarsamente popolato" | nessun fraintendimento con il nome di regione `the Deep` (unità 25 usa "dal Deep") |
| 33 | `someone has gone to the trouble` → "qualcuno si è preso la briga" | — |
| 69 | `make all of this seem very overwhelming` → "fanno sembrare tutto questo molto opprimente" | evita il calco "soverchiante" |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Twilight Guard` invariato** (1): nome di fazione. Coerente con `Remnant`/`Unfettered`/`Heliarch`, ma
   se si preferisce "Guardia del Crepuscolo" va cambiato ovunque compaia.
2. **`Bulk Freighter` invariato** (1): classe di nave. Come `Halite` (L7), le classi restano invariate;
   da ratificare una volta per tutto il corpus.
3. **`Unlikely` → "Unlike"** (1): presunto refuso del sorgente; da annotare se ricompare.
4. **Frase agrammaticale** in unità 53: resa secondo il senso; se esiste una versione corretta del
   sorgente in un branch successivo, va confrontata.
5. **`the Deep`** (unità 25) e **`Deep`** come nome di pianeta (unità 24) convivono: nessuna collisione,
   ma il contesto va sempre controllato.
6. Restano aperte: `Successors`, `Antecessors`, `caveau`, `ringroide`, `Starlit University`, `Costruttori`,
   `Key Stones`, `skyhook`, `il Rim`, `Halite`, `Cavasaa-Vasa-Tej`.

---

## 5. Esito dei controlli

```
unità 77 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4534 -> 4486 · ratio 0.93-1.20
tab 24 (tutti gli iniziali conservati) · virgolette 2 (coppia su "Unfettered", unità 10) · token <...> 0
riga grezza identica al file: 77/77 · english/kind/path/state identici al DB: 77/77
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Nessun errore rilevato dai controlli; un intervento volontario sull'unità 43 (ripetizione) dopo la prima
stesura.

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
