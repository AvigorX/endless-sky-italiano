# L10 — Revisione editoriale del blocco `data/map planets.txt` 1826–2163

81 descrizioni, 4.549 parole inglesi → 4.567 italiane. Sesto lotto del tratto iniziale del file, nessun ID
in comune con L1–L9. Inizia con `planet:Featherweight` e si chiude a fine pianeta con `planet:Giaru Gegno`
(riga 2163); la successiva (riga 2171) apre Giiq-Oj-Sol, e tra le due righe non esistono unità.

---

## 1. Metodo

Stesso impianto dei lotti precedenti: contesto letto per pianeta, glossario e checkpoint consultati prima
di ogni scelta, traduzione in quattro gruppi nell'ordine del file (1–21, 22–41, 42–61, 62–81), rilettura
del solo italiano.

Le 81 unità sono state esportate da `state.db` (tutte `PENDING`, tutte `DESCRIPTION`); `raw` coincide con
la riga del sorgente per tutte e 81 (verificato in `verify.py`).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze EN → IT | Note |
|---|---|---:|---|
| `Quarg` | invariato | 13 → 13 | — |
| `Hai` | invariato | 8 → 8 | — |
| `Saryd` / `Kimek` / `Arach` / `Avgi` / `Gegno` / `Scin` | invariati | 2/3/1/3/3/1 | — |
| `Unfettered` | invariato | 1 → 1 | sub-fazione Hai |
| `Antecessors` / `Antecessor technology` | invariato | 2 → 2 | convenzione L3 |
| `Aberrant` / `Aberrations` | **invariato** in entrambi i casi | 1 → 2 | il plurale inglese è reso con "Aberrant" ("qualche Aberrant") per non introdurre due nomi della stessa cosa |
| `Syndicate` | Sindacato | 3 → 3 | + 1 nome proprio invariato (vedi sotto) |
| `Syndicated Shipyards` | **invariato** | 1 → 1 | ragione sociale della società cantieristica; da ratificare |
| `Republic` / `Republic Navy` | Repubblica / Marina della Repubblica | 2 → 2 | — |
| `Coalition` | Coalizione | 4 → 4 | — |
| `Earth` | Terra | 2 → 2 | — |
| `Ember Waste`, `Tangled Shroud` | invariati | 1 / 2 | nomi di regione |
| `hyperdrive` | iperpropulsore | 1 → 1 | glossario |
| `ringworld(s)` | mondo/mondi ad anello | 4 → 4 | convenzione L3d |
| `CCOR` | **invariato** (acronimo) | 3 → 3 | con il nome sciolto in italiano, vedi §3 |
| `terraforming` | terraformazione | 3 → 4 | in un caso l'inglese usa il gerundio e l'italiano richiede il sostantivo |
| `Paradise Planets` | Pianeti Paradisiaci | 1 → 1 | coerente con `Paradise World` → Mondo Paradisiaco |
| `Remembrance Day` | invariato | 1 → 1 | convenzione L1 |

Nomi propri invariati: Featherweight, Fek Rembatu, Felorap, Fenrir, Feo, Fertriery, Firefall, Firelode,
Firka Tesk, Flood, Flowing Fields, Follower, Forpelog, Foundry, Fourth Shadow, Freedom (East Mesa,
West Mesa), Frostmark, Furnace, Gagarin, Gamla, Gara Pvu, Garden Empyreal, Geminus, Gemstone, Gentle Rain,
Gestli, Geyser, Ghneoe, Gi Tiures, Giaru Gegno.

---

## 3. Intervento imposto dal controllo (un FAIL reale)

`check.py` ha segnalato **unità 47**: parola inglese residua `the`. Il nome dello Stato
`the Confederated Councils of the Outer Rim` era stato lasciato invariato, ma in italiano la locuzione
inglese lasciava visibile l'articolo. Ho quindi sciolto il nome:

> **Consigli Confederati del Bordo Esterno (CCOR)**

mantenendo invariato l'acronimo, che ricorre altre tre volte (unità 47, 48, 49). **Attenzione:** in L6
la forma breve `Confederated Councils` era stata lasciata invariata (1 occorrenza). Le due scelte ora
convivono: la correzione retroattiva di L6 non è stata fatta, perché il mandato vieta di riscrivere il
corpus già chiuso. Va ratificata (§4 punto 1).

Corretto il FAIL, `check.py` passa a `FAIL totale: 0` senza altre modifiche.

---

## 4. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 12 | testo identico a L8 unità 15 ("stazione messa fuori servizio") → **stessa resa**, senza tab iniziale | coerenza di memoria di traduzione; il sorgente qui non ha tab |
| 13 | `Dwarfed by the nearby Quarg ringworld` → "Nano accanto al vicino mondo ad anello dei Quarg" | participio assoluto, più naturale del calco "fatto nano da" |
| 40 | due cartelli tra virgolette → citazione diretta con virgolette dritte conservate | i segni tipografici restano quelli del sorgente |
| 41 | `We have brown rice.` → "Abbiamo riso integrale." | — |
| 53 | sorgente `pyramids lay at every angle` (lie/lay) → "giacciono" | il sorgente usa *lay* per *lie*: reso secondo il senso |
| 54 | sorgente `Populating the gas giant's uppermost atmosphere lay several hardy species` (frase ellittica) → "c'erano diverse specie resistenti di batteri" | resa esplicita, l'italiano non regge l'ellissi |
| 66 | `shaped like a giant tree` → "ha la forma di un albero gigantesco" | — |
| 62 | `insane project` → "progetto da pazzi" | registro colloquiale conservato |
| 65 | `spiders so large that their webs are strung from one tree to another` → resa con "tele... da un albero all'altro" | evita "tessute" |

---

## 5. Incoerenze e decisioni aperte (non bloccanti)

1. **`Confederated Councils` / `Consigli Confederati`** — L6 invariato, L10 tradotto (per necessità
   tecnica). Da ratificare e, se serve, allineare L6.
2. **`Syndicated Shipyards` invariato** (1): ragione sociale. Se si traduce, cambia almeno un altro lotto.
3. **`Aberrations` → "Aberrant"** (1): scelta di non introdurre un secondo nome. Alternativa:
   "Aberrazioni" per gli individui, "Aberrant" per la fazione.
4. **`Paradise Planets` → Pianeti Paradisiaci** (1): coerente con la voce "Mondo Paradisiaco", ancora da
   ratificare (§7 punto 3).
5. **`The Man`** (unità 40) → "il Sistema": il riferimento ironico alle autorità è reso con un termine
   italiano colloquiale equivalente.
6. Restano aperte: `Successors`, `Antecessors`, `Consonance`, `caveau`, `ringroide`, `Starlit University`,
   `Costruttori`, `Key Stones`, `skyhook`, `il Rim`, `il Nucleo`, `Halite`, `Bulk Freighter`,
   `Twilight Guard`, `Egemonia Bunrodean`.

---

## 6. Esito dei controlli

```
unità 81 · mancanti 0 · estranei 0 · vuote 0 · duplicati IT 0 · duplicati EN 0
parole 4549 -> 4567 · ratio 0.94-1.24
tab 30 (tutti gli iniziali conservati) · virgolette 12 (6 coppie: unità 40 ×2, 41, 53, 54, 55) · token <...> 0
riga grezza identica al file: 81/81 · english/kind/path/state identici al DB: 81/81
tipografia: 0 accenti sostitutivi, 0 ellissi tipografiche, 0 caporali, 0 em dash, 0 apostrofi curvi
parole inglesi residue: nessuna (dopo la correzione dell'unità 47) · anglicismi evitabili: nessuno
problemi 0
```

**Non verificato:** rendering in gioco (nessun avvio, come da mandato).
