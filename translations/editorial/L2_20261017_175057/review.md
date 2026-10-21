# L2 — Revisione editoriale del blocco `data/map planets.txt` 4308–4781

101 descrizioni, 5.552 parole inglesi → 5.472 italiane. Continua L1 senza sovrapposizioni
(0 ID in comune, verificato).

---

## 1. Metodo

Stesso impianto di L1: lettura del contesto per pianeta, glossario consultato prima di ogni scelta,
traduzione in quattro gruppi nell'ordine del file, rilettura del solo italiano e correzione dei calchi.
Il blocco si chiude a fine pianeta (ultima descrizione di Quicksilver), senza tagliare un testo a metà.

---

## 2. Convenzioni applicate (e nuove occorrenze)

| Termine | Resa | Coerenza |
|---|---|---|
| `Remembrance Day` | invariato | convenzione L1 (1 occorrenza: unità 81) |
| `Syndicate` | Sindacato | convenzione L1 (2 occorrenze: 69, 70) |
| `Predecessors` | Predecessori | convenzione L1; nell'unità 7 il minuscolo *predecessors* indica i predecessori della stazione, non la specie, e resta "predecessori" |
| `House Sejra` | Casata Sejra | coerente con "Nuove Casate" di L1 |
| `New Houses` | — | **0 occorrenze** in questo blocco |
| `Coalition` | **Coalizione** | nuovo: parola comune, stesso criterio di `Syndicate` (5 occorrenze: 5, 7, 8, 53, 54) |
| `hyperdrive` | **iperpropulsore** | nuovo: termine tecnico, nessuna voce di glossario (3 occorrenze: 51, 91, 95) |
| `the Incursion` | **l'Incursione** | nuovo: nome di evento, con maiuscola (3 occorrenze: 17, 25, 32) |
| `Paradise World` | **Mondo Paradisiaco** | nuovo: categoria descrittiva, non nome proprio (1 occorrenza: 13) |
| `Dissonance`, `Consonance` | invariati | nomi di movimenti politici (3 + 1 occorrenze) |
| `Bunrodean`, `Arach`, `Avgi`, `Hai`, `Pug`, `Remnant`, `Ka'het`, `Incipias`, `Scin` | invariati | nomi di specie/fazioni |
| `Betelgeuse Shipyards`, `Lovelace Labs`, `Yoot Ki Magnetic Fuel Harvesting`, `The Parting Glass` | invariati | nomi di aziende e locali |
| `Pug`, `Tangled Shroud`, `Outer Limits`, `Deep`, `Anax`, `Thread` | invariati | nomi di regioni, sistemi, pianeti |

---

## 3. Correzioni fatte in rilettura

| # | Prima | Dopo | Perché |
|---|---|---|---|
| 2 | "estrarre e riestrarre" | "raccogliere ripetutamente" | "riestrarre" è innaturale |
| 48 | "santuario naturale per specie esotiche importate" | "santuario per la fauna selvatica, con specie esotiche importate" | *wildlife sanctuary* = santuario faunistico |
| 69 | "campagna marketing" | "campagna pubblicitaria" | anglicismo evitabile |
| 89 | "Ospita la Betelgeuse Shipyards" | "Ospita la sede della Betelgeuse Shipyards" | sintassi con nome aziendale inglese |
| 101 | "il tempo ululante fuori" | "il vento ululante fuori" | *howling weather*: in italiano "ulula" il vento |

---

## 4. Incoerenze da uniformare (non bloccanti)

1. **`Coalition` → Coalizione** è una decisione nuova rispetto a L1: se si ratifica, va applicata a tutto
   il corpus (occorre anche in help/tooltip futuri).
2. **`Assembly of Consonant Polities`** l'ho resa "Assemblea delle Entità Consonanti" (unità 59), mentre
   `Consonance` resta in inglese (unità 36). Se si vuole coerenza stretta, la forma è "Assemblea delle
   Entità della Consonance" oppure si traduce anche Consonance in "Consonanza". **Richiede una scelta.**
3. **`Paradise World` → Mondo Paradisiaco**: se l'etichetta compare anche nell'interfaccia, va allineata.
4. **`hyperdrive` → iperpropulsore**: verificare che non compaia come nome di equipaggiamento nella UI,
   dove servirebbe la stessa resa.
5. **`Bunrodean` al plurale** resta invariato ("i Bunrodean"), come `Hai`, `Avgi`, `Pug`. Se si preferisce
   l'adattamento ("Bunrodeani"), va deciso una volta e applicato ovunque.
6. `square dances` / `line dances` (aperte in L1) **non compaiono** in questo blocco.

---

## 5. Esito dei controlli

```
unità 101 · mancanti 0 · estranei 0 · duplicati 0
parole 5552 -> 5472 · ratio 0.89-1.27
tab 34 · virgolette 6 · token <...> 0
problemi 0
```

Unica segnalazione automatica di parola inglese: unità 80, **"The Parting Glass"** (nome proprio della
taverna) — attesa.

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
