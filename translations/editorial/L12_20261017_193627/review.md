# L12 — Revisione editoriale del blocco `data/map planets.txt` 2555–2908

88 descrizioni, 4.471 parole inglesi → 4.514 italiane. Ottavo lotto del tratto iniziale del file, nessun
ID in comune con L1–L11. Inizia con `planet:Hespair` (riga 2564) e si chiude a fine pianeta con
`planet:Kalbai` (riga 2908); la successiva (riga 2913) apre Kapnos.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–22, 23–44, 45–66, 67–88), rilettura
del solo italiano.

Le 88 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 88 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Hai` / `Quarg` / `Avgi` / `Kimek` / `Gegno` / `Successors` / `Remnant` / `Korath` | invariati | 2/5/5/6/2/4/2/1 | specie e fazioni |
| `Bunrodea(n)` | invariato | 7 → 7 | — |
| `Republic` / `Republic Navy` | Repubblica / Marina della Repubblica | 2 → 2 | — |
| `Earth` | Terra | 2 → 2 | eccezione deliberata |
| **`Jupiter`** | **Giove** | 2 → 2 | corpo reale, come `Mars` → Marte e `Earth` → Terra |
| `House Kaatrij` | Casata Kaatrij | 1 → 1 | `house X` → Casata X |
| `the Confederated Councils` / `the Councils` | Consigli Confederati / i Consigli | 1 → 1 | **terza occorrenza**: qui si allinea a L10, non a L6 (vedi §4) |
| `Politburo` | invariato | 1 → 1 | termine storico corrente anche in italiano |
| `the Deep` | il Deep | 1 → 1 | nella frase "la porta del Deep" |
| `Remembrance Day`, `the Incursion` | invariati | 2 / 2 | convenzioni consolidate |
| `cloaking` / `partial cloaking` | occultamento / occultamento parziale | 1 → 1 | nota K4 del checkpoint |
| `outfits` / `outfitter` | equipaggiamenti / equipaggiatore | 1 → 2 | due parole italiane distinte per due inglesi |
| `terraforming` | terraformazione / terraformare | 3 → 3 | — |

Nomi propri invariati: Hespair, Hestia, Hilothire, Hippocrates, Hope, Hopper, Huginn, Muninn, Humanika,
Humo, Hydra, Icefall, Icelake, Iconil, Livolua, Iddesato, Iemn Eitch, Igna, Ijra-Ea (Shimmering Veil),
Illbo Avo, Illbo Elo, Independance, Ingot, Inmost Blue, Into White, Iritoroost, Ironfirth, Makerplace,
Iyra-Ijasa-Iret, Jakobsen, Janalos, Janiculum, Jentuthro, Melenci, Paru Paru, Alvorada, Kaeyin, Kalakil,
Kalbai, Thshybothro.

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 62 / 64 | inglese **identico** ("This station was mothballed…"), italiano differenziato in due punti | il controllo segnala la coppia duplicata; la differenziazione evita due traduzioni identiche nello stesso lotto. Vedi §4 punto 2 |
| 30 | "quasi in navigabili" → "quasi **innavigabili**" | refuso di stesura, individuato in rilettura |
| 36 | "al mondoa abitabile" → "al **mondo** abitabile" | refuso di stesura, individuato in rilettura |
| 50 | `the Confederated Councils` → "i Consigli Confederati" | terza occorrenza; coerente con L10 |
| 51 | `the Councils` → "i Consigli" | ripresa anaforica del nome sciolto |
| 80 | `Great Red Spot` → "Grande Macchia Rossa" | nome proprio astronomico reale |
| 13 | `Erlenmeyer flask` → "matraccio di Erlenmeyer" | — |
| 32 | `pumpjacks and oil derricks` → "cavalletti di estrazione e torri di perforazione" | — |
| 71 | `breakwaters` → "frangiflutti" | — |
| 72 | `mind-boggling variety of insects` → "varietà inverosimile di insetti" | evita il calco "che fa girare la testa" |
| 83 | `the only word you can think of` → "l'unica parola che ti viene in mente" | — |

Nessun errore imposto dai controlli: `check.py` passa con `FAIL totale: 0`.

---

## 4. Incoerenze e decisioni aperte (non bloccanti)

1. **`Consigli Confederati` / `Bordo Esterno`**: in L12 ricompare la forma breve `the Confederated Councils`.
   Ho applicato la scelta di **L10**, non l'invariato di **L6**. Le tre scelte ora sono: L6 invariato,
   L10 e L12 tradotti. La ratifica (§7 punto 23) deve chiudere la questione e decidere se allineare L6.
2. **Unità 62 e 64 con inglese identico**: il sorgente ripete la stessa descrizione per due stazioni
   diverse (`Iritoroost` e `Ironfirth`). L'italiano dell'unità 62 è identico a quello usato in L8 (unità 15)
   e L10 (unità 12); quello dell'unità 64 varia in due punti ("segnala", "dispositivi di riserva") per non
   produrre due traduzioni identiche nello stesso lotto. Reversibile se si preferisce la ripetizione esatta.
3. **`Politburo` invariato**: resa accettata in italiano; l'alternativa è "ufficio politico".
4. **`Jupiter` → Giove** (2): prima occorrenza di un corpo reale dopo Marte e Terra. `Great Red Spot` →
   "Grande Macchia Rossa", anch'esso corrente.
5. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `caveau`, `ringroide`, `Halite`,
   `Bulk Freighter`, `Costruttori`, `Key Stones`, `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`,
   `Egemonia Bunrodean`, istituzioni lasciate in inglese.

---

## 5. Esito dei controlli

```
unità 88 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0
duplicati EN 1 (unità 62 e 64: ripetizione presente nel sorgente, documentata)
parole 4471 -> 4514 · ratio 0.89-1.28
tab 36 (tutti gli iniziali conservati) · virgolette 8 (4 coppie: unità 21, 50, 67, 83) · token <...> 0
riga grezza identica al file: 88/88 · english/kind/path/state identici al DB: 88/88
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
