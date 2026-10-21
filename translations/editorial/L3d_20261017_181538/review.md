# L3d — Revisione editoriale del blocco `data/map planets.txt` 5836–6371

122 descrizioni, 6.469 parole inglesi → 6.412 italiane. Chiude il lotto L3 senza sovrapposizioni
(0 ID in comune con L1, L2, L3, L3b, L3c). Il blocco inizia con `planet:Taylor` e si chiude con
l'ultima descrizione di `planet:Varu K'est` (riga 6371).

**Perché si ferma a 6371 e non a 6370:** il checkpoint indicava 6370 come fine del lotto, ma l'unità
6371 è la seconda e ultima descrizione di Varu K'est. Fermarsi a 6370 avrebbe tagliato un pianeta in due.
La sezione si chiude quindi a fine pianeta, e il lotto L3 conta 369 unità invece di 368.

---

## 1. Metodo

Impianto identico alle sezioni precedenti: contesto letto per pianeta, glossario e checkpoint consultati
prima di ogni scelta, traduzione in cinque gruppi nell'ordine del file (1–25, 26–50, 51–75, 76–100,
101–122), rilettura del solo italiano.

Le 122 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide
con la riga del sorgente per tutte e 122 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Wanderers` | invariato | 21 → 29 | specie/fazione; l'italiano ripete l'articolo, da cui la differenza |
| `Pug` | invariato | 4 → 4 | specie |
| `Gegno`, `Vi` | invariati | 6 / 5 | specie |
| `Sheragi` | invariato | 1 → 1 | specie estinta, prima occorrenza |
| `House Garbarag` | Casata Garbarag | 1 → 1 | convenzione L1 |
| `Old Houses` / `New Houses` / `High Houses` | Vecchie / Nuove / Alte Casate | 2 / 1 / 1 | coerente con L3c |
| `longcows` | bovini lunghi | 3 → 4 | resa descrittiva, nessun neologismo |
| `cybernetics` | cibernetica (disciplina) / innesti cibernetici (oggetti) | 5 → 7 | distinzione disciplina/innesto |
| `tholins` | toline | 2 → 2 | termine chimico italiano |
| `Bulk Freighter` | mercantile pesante | 1 → 1 | convenzione L1 |
| `Centipede` | invariato | 1 → 1 | classe di nave Hai |
| `Syndicate` | Sindacato | 3 → 3 | convenzione L1 |
| `Remnant`, `Quarg`, `Hai`, `Kimek`, `Saryd`, `Bunrodea` | invariati | 1/4/2/5/1/3 | specie e fazioni |
| `Earth` | Terra | 3 → 3 | eccezione deliberata |
| `Remembrance Day`, `Alpha War`, `the Alphas` | invariati | 2 / 1 / 1 | convenzioni L1/L2 |
| `the Deep` | invariato | 3 → 3 | nome di regione |
| `galactic Rim` | il Rim | 1 → 1 | nome di regione (decisione L3 §7) |
| `spaceport` | spazioporto | 35 → 33 | glossario; unità 24 resa con "il suo scopo principale" (evita la ripetizione), unità 25 con "operai del porto" |
| `landing pad` | piazzola di atterraggio | 7 → 8 | convenzione L1/L2 |

---

## 3. Interventi fatti in stesura e rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 9 | "un aspetto più cupo di questo mondo - innumerevoli cimiteri" | "un aspetto più cupo di questo mondo: innumerevoli cimiteri" | il trattino lungo non è ammesso dal set Latin-1 |
| 22 | "ricerca cibernetica … nuove protesi cibernetiche" | "ricerca sulla cibernetica … nuovi innesti cibernetici" | distingue disciplina e oggetto |
| 53 | "l'impatto di un meteora" | "l'impatto di una meteora" | accordo di genere |
| 67 | "raffinazione del carburante del Margine galattico" | "… del Rim" | coerenza con la decisione su `the Rim` (L3 §7) |
| 86 | "… dello spazio umano - e le più costose" | "… dello spazio umano, oltre che le più costose" | riformulazione senza em dash |
| 103 | "enormi zattere vive di alghe e kelp" | "… di alghe e laminarie" | "kelp" è inglese |
| 89 | "un piatto di latte" (verifica) | invariato | *milk dish* è letterale e voluto: dettaglio surreale del testo |
| 6 | "bovino lungo … in preda agli spasmi finali" | invariato dopo verifica | *death throes* reso senza calchi |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Wanderers` invariato** (21): specie/fazione con articolo italiano. Se si ratifica un adattamento
   ("i Vaganti"), va applicato a tutto il corpus.
2. **`longcows` → bovini lunghi** (3): resa descrittiva, non un nome proprio. Se il termine diventa una
   voce di glossario, la forma va congelata.
3. **`cybernetics`**: la distinzione disciplina/innesto è una scelta di questo blocco; va mantenuta in
   tutte le descrizioni Bunrodea.
4. **`the Deep` e `il Rim`**: due nomi di regione trattati in modo diverso (uno invariato, l'altro
   tradotto). È coerente con le decisioni precedenti, ma resta un'asimmetria da ratificare.
5. Restano aperte dalle sezioni precedenti: `Successors`, `caveau`, `wormhole`, `ringroide`,
   `Starlit University`, `Antecessors`.

---

## 5. Esito dei controlli

```
unità 122 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 6469 -> 6412 · ratio 0.84-1.22
tab 35 (tutti gli iniziali conservati) · virgolette 6 · token <...> 0
riga grezza identica al file: 122/122 · english/kind/path/state identici al DB: 122/122
tipografia: 0 accenti sostitutivi, 0 ellissi, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
