# review.md — L232 (`data/korath/korath outfits.txt`, righe 809–908)

Registro delle **decisioni editoriali** del lotto terminale di `korath outfits.txt`. Ogni scelta è datata al
workspace: i termini invariati sono contati nello staging, non dedotti.

## 1. Il lotto

Dieci `DESCRIPTION`, sette schede, nessun `VALUE`. È il **primo lotto della campagna con sola prosa**: il
confronto non è più «N identiche / M tradotte» ma **0 identiche / 10 tradotte**, e la forma del controllo
cambia di conseguenza (decisione 190: il segno dell'asserzione segue il lotto, non la serie).

## 2. Terminologia ripresa dai lotti dello stesso file

| inglese | resa | precedente |
|---|---|---|
| `steering` | **sistema di sterzata** (3) | L231 unità 11, decisione del file |
| `thruster(s)` | **propulsore / propulsori** | L231 unità 18–21 |
| `gravitoplasma thrusters` | **propulsori a gravitoplasma** | L231 unità 18 («propulsori a gravitoplasma») |
| `gravitational propulsion` | **propulsione gravitazionale** | L231 unità 18–19 |
| `quantum gravity` | **gravità quantistica** | L231 unità 21 |
| `woefully inefficient` | **tristemente inefficiente** | L231 unità 11, ripresa **alla lettera** |
| `fusion reactors` | **reattori a fusione** | L230, L228 |
| `heat production` | **produzione di calore** (non «calore disperso») | il testo parla di calore *prodotto* |
| `Efreti`, `Quarg`, `Korath` | invariati (8 / 3 / 10, gli stessi conteggi dell'inglese) | L228–L231 |

La frase condivisa con L231 è stata **riletta dal suo `translation.json`**, non ricopiata a memoria:

> L231 u11 — «Questo compatto sistema di sterzata è un esempio classico della tecnologia Korath: piccolo,
> potente e tristemente inefficiente.»
>
> L232 u3 — «Un esempio classico della tecnologia Korath: piccolo, potente e tristemente inefficiente.»

La sintassi cambia perché l'inglese è diverso (`A classic example …, it is small, powerful, and woefully
inefficient.` è un'apposizione, non una copula), ma il nucleo lessicale è identico: stesso inglese → stessa
resa (regola 10).

## 3. Una divergenza dichiarata: `jump drive`

L'unità 6 dice `jump drive technology`. L231 unità 19 aveva scritto «tecnologia del **jump drive**
interstellare»; qui la resa è «tecnologia del **motore di salto**».

**Perché**: la forma dominante del corpus è italiana — **334** occorrenze di «motore/motori di salto» contro
**13** di «jump drive» (misurato su tutti i `translation.json`). La regola della forma dominante (decisione
168) vince sull'eredità del lotto precedente, e la divergenza si dichiara invece di nasconderla. Chi
riprende il corpus può allineare L231 a questa forma in un lavoro dedicato: è una modifica di una unità in
un lotto chiuso, non un effetto di L232.

## 4. Terminologia nuova o poco usata

| inglese | resa | nota |
|---|---|---|
| `torque` | **coppia torcente** | «coppia» da sola in italiano è ambigua (paio/coppia fisica): il qualificatore costa due parole e toglie il doppio senso |
| `airlock` | **camera di equilibrio** | forma dominante dello staging (76 occorrenze); `portello d'ancoraggio` compare nei lotti di abbordaggio (L117/L118) e descrive un'altra scena |
| `World-Ships` | **nave-mondo** | L33 («nave-mondo dei Korath»): il nome della classe resta italiano, come `nave viva` per `liveship` |
| `microbots` | **microbot** (invariato, 2) | L228 unità 20 («serbatoi di microbot»): nome di prodotto |
| `nutrigel` | **nutrigel** (invariato) | sostanza di prodotto, presente anche in `korath hails.txt` |
| `vat` | **vasca** | non «tino»: la vasca raccoglie il gel |
| `gargantuan` | **gargantuesche** | L27 («stazione gargantuesca») |
| `races` | **specie** | «razze» in italiano, per specie aliene, porta una connotazione che il testo non ha |
| `erroneous fears` | **timori infondati** | |
| `taboos relating to cannibalism` | **tabù legati al cannibalismo** | |
| `heavy fines` | **multe salate** | «multa» è già il termine del corpus (53 occorrenze) |
| `painful, confusing death` | **morte atroce e confusa** | `excruciating` non è «dolorosa»: è il grado massimo |

## 5. Punteggiatura riprodotta, non corretta

L'unità 10 contiene `"escape,"` con la **virgola dentro le virgolette**. In italiano la virgola starebbe
fuori, ma il criterio della campagna è riprodurre i segni del sorgente: spostarla avrebbe lasciato il
conteggio a 2 e cambiato il testo (trappola 70). Il `check.py` verifica le virgolette **per unità**
(`(10, 2)` in inglese e in italiano), non solo il totale.

## 6. Apici: 5 inglesi, 3 italiani

Non è una perdita: sono due lingue diverse (decisione 202).

| unità | EN | causa | IT | causa |
|---|---|---|---|---|
| 1 | 0 | — | 1 | `all'inefficienza` (elisione) |
| 3 | 1 | `engineers'` (possessivo) | 1 | `l'influenza` (elisione) |
| 5 | 1 | `system's` (possessivo) | 0 | — |
| 6 | 0 | — | 1 | `l'abbandono` (elisione) |
| 8 | 3 | `user's`, `aren't`, `won't` | 0 | — |

Il controllo elenca le coppie `(unità, conteggio)`, non i totali: 5 = 3 non avrebbe distinto questa
distribuzione da uno scambio.

## 7. Lacune dichiarate

- **Nessuna lacuna `log`**: il lotto non ha righe `log` (0 `LOGBOOK`, asserito nel `check.py` fra le
  assenze di tipo).
- **Nessun riferimento di dato mascherato da prosa**: le 10 unità sono descrizioni; nessun `NT` da elencare.
  Il `check.py` lo scrive come asserzione (`[u['idx'] for u in units if u['kind'] != 'DESCRIPTION'] == []`).
- **La scheda della `Microbot Defense Station` è l'unica del file con due paragrafi** (righe 907 e 908):
  la seconda unità inizia con un tab, come il sorgente.
