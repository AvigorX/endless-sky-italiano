# L3 — Revisione editoriale del blocco `data/map planets.txt` 4790–5121

79 descrizioni, 4.509 parole inglesi → 4.506 italiane. Continua L2 senza sovrapposizioni
(0 ID in comune con L1 e L2, verificato sull'ID completo). Il blocco inizia con la prima
descrizione di Quirinal e si chiude con il testo `spaceport` di Sardva (riga 5121), a fine pianeta.

---

## 1. Metodo

Stesso impianto di L1 e L2: lettura del contesto per pianeta, glossario consultato prima di ogni
scelta, traduzione in tre gruppi nell'ordine del file (unità 1–25, 26–50, 51–79), rilettura del
solo italiano e correzione di calchi, anglicismi e rigidità.

Le unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`) e la riga grezza
è stata riletta dal file: `raw` coincide con la riga del sorgente per tutte le 79 unità (verificato
in `verify.py`). Nessun testo è stato tagliato a metà.

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Successors` | **invariato** | 8 → 8 | fazione/specie; articolo italiano ("i Successors", "dei Successors") |
| `House Kaatrij` / `House Debdo` / `Houses` | **Casata / Casate** | 7 → 9 | convenzione L1 (`house X` → Casata X); +2 da `Arach houses` → "Casate Arach" |
| `New Houses` | **Nuove Casate** | 1 → 1 | decisione di L1, ancora da ratificare |
| `Predecessors` | **Predecessori** | 2 → 2 | eccezione deliberata del checkpoint |
| `Coalition` | **Coalizione** | 8 → 8 | decisione di L2, ancora da ratificare |
| `Earth` | **Terra** | 5 → 4 | eccezione deliberata; `Earth's traffic` → "rotte terrestri" (resa idiomatica) |
| `hyperdrive` | **iperpropulsore** | 2 → 2 | decisione di L2 |
| `Dirt Belt`, `Southern Rim`, `Deep` | **invariati** | 1 / 1 / 1 | nomi di regione |
| `the Rim` | **il Rim** (in "nel Rim") | 1 → 1 | forma breve dello stesso nome di regione |
| `Remembrance Day`, `Alpha Wars` | **invariati** | 1 / 1 | convenzione L1 |
| `Heliarch`, `Quarg`, `Kimek`, `Saryd`, `Arachi`, `Incipias`, `Bunrodea(n)`, `Korath`, `Avgi`, `Hai`, `Unfettered` | **invariati** | 17/7/11/7/4/5/3/5/2/4/1 | specie e fazioni |
| `ringworld` | **mondo ad anello** | 9 → 9 | categoria descrittiva, non nome proprio |
| `spaceport` | **spazioporto** | 25 → 25 | glossario |
| `landing pad` | **piazzola di atterraggio** | 8 → 9 | convenzione L1/L2 |
| `freighter` | **mercantile** | 2 → 3 | convenzione L1/L2 |
| `vault` | **caveau** | 6 → 6 | prestito invalso per camere blindate; nessuna voce di glossario |
| `wormhole` | **wormhole** | 1 → 1 | termine tecnico del motore, invariato |

Plurale delle specie: si usa la forma invariata con articolo e aggettivo italiani ("alcuni Saryd
particolarmente avventurosi", "i pochi Korath presenti"), coerente con la scelta di L1/L2 per
`Bunrodean`, `Hai`, `Avgi`, `Pug`.

---

## 3. Correzioni fatte in rilettura (20)

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 5 | "dovranno apprezzarlo" | "non possono che apprezzarlo" | *must appreciate*: non è un obbligo futuro |
| 7 | "Questo, il suo pianeta natale, è piccolo" | "Questo pianeta, il suo mondo natale, è piccolo" | sintassi sospesa |
| 10 | "L'antica dimora ancestrale" | "La dimora avita" | "antica"+"ancestrale" ridondante |
| 12 | "il cui nome successor" | "il cui nome nella lingua dei Successors" | "successor" come aggettivo non esiste in italiano |
| 21 | "meccanismi di standby" | "meccanismi di riserva" | anglicismo |
| 23 | "una delle più grandi fra le Casate Arach" | "una delle maggiori Casate Arach" | ripetizione di "grandi/Casate" |
| 30 | "la principale industria sia il distributore" | "sia la stazione di servizio" | *gas station* |
| 31 | "questo mondo sostiene una popolazione" | "questo mondo ospita una popolazione" | calco di *supports a population* |
| 32 | "sei oggetto di un notevole esame" | "vieni osservato con grande attenzione" | *scrutiny* |
| 38 | "la gemma più preziosa" | "il gioiello più prezioso" | *crown jewel* |
| 43 | "Il designer che ha inventato" | "L'ideatore delle uniformi" | anglicismo + sintassi |
| 44 | "riprodurre a ritroso la tecnologia" | "ricostruire la tecnologia" | *reverse engineer* reso con calco |
| 51 | "corrispondere al design delle loro navi" | "corrispondere alla foggia delle loro navi" | anglicismo |
| 58 | "bloccaggi magnetici" | "morsetti magnetici" | *clamps* |
| 59 | "ufficio marketing" | "ufficio pubblicitario" | anglicismo (coerente con L2: *marketing campaign* → "campagna pubblicitaria") |
| 60 | "conglomerati armatoriali" | "conglomerati del trasporto merci" | *shipping*: "armatoriale" è marittimo |
| 61 | "soggiogati dalla raffinatezza tecnologica" | "in soggezione davanti alla raffinatezza tecnologica" | *in awe of* non è soggezione politica |
| 64 | "Per un recente cambiamento climatico" | "A causa di un recente cambiamento climatico" | nesso causale |
| 67 | "vengono allevate piante" | "si coltivano piante" | *allevare* è per gli animali |
| 79 | "solo perché tu smetta di chiedere" | "solo per farti smettere di chiedere" | congiuntivo innaturale |

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Successors` invariato** (8 occorrenze) mentre `Predecessors` → Predecessori (2): è
   l'asimmetria più visibile del blocco, già accettata dal checkpoint (§6). Se si ratifica
   "Successori", va applicata a tutto il corpus: qui non è stata applicata.
2. **`Coalition` → Coalizione** (8) e **`New Houses` → Nuove Casate** (1): decisioni non ancora
   ratificate; usate coerentemente con L2 e L1.
3. **`the Rim` → il Rim** (1, unità 48): forma breve di `Southern Rim`, mantenuta invariata come
   nome di regione. Leggermente innaturale in italiano ("nel Rim"); alternativa: "nel Margine".
4. **`vault` → caveau** (6): scelta di registro. Alternativa italiana piena: "camera blindata" o
   "deposito". Da decidere una volta se il tema Bunrodea ricorre.
5. **`wormhole` invariato** (1): termine tecnico del motore, ma nel testo narrativo potrebbe
   diventare "varco". Segnalato, non deciso.
6. **Doppia stesura dello stesso testo** (unità 21 e 70, inglese identico: stazione in disarmo).
   Per non avere due traduzioni identiche nel lotto, la seconda usa varianti lessicali
   ("posta in disarmo", "dispone di atmosfera", "meccanismi di riserva") senza aggiungere né
   togliere contenuto. Se si preferisce la memoria di traduzione rigida (stesso inglese → stesso
   italiano), l'unità 70 va riallineata all'unità 21.
7. Restano aperte da L1/L2, **0 occorrenze in questo blocco**: `Consonance`, `Paradise World`,
   `Bunrodean` al plurale, `square dances`/`line dances`.

---

## 5. Esito dei controlli

```
unità 79 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0
parole 4509 -> 4506 · ratio 0.88-1.30
tab 24 (tutti gli iniziali conservati) · virgolette 14 · token <...> 0
riga grezza identica al file: 79/79 · english/kind/path/state identici al DB: 79/79
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

Unica ripetizione attesa: unità 21/70 condividono l'inglese (boilerplate della stazione in
disarmo); le traduzioni differiscono per varianti lessicali (punto 6 sopra).

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
