# review.md — L307 (`data/avgi/avgi weapons.txt`, righe 25–203)

Registro delle decisioni editoriali del **primo lotto** delle armi Avgi: proiettili, munizioni, coilgun, torrette e laser ottici.

## 1. Che cosa raccontano queste dodici schede

| famiglia | righe | idea centrale |
|---|---|---|
| **munizioni** | 25, 38 | proiettili di **vetro metallico** iperveloci: forti contro lo scafo, **inutili contro gli scudi** a repulsione; caricatori compatti per spedizioni lunghe |
| **coilgun** | 67/68/69 | `Speckle Coilgun`: compatta, **poco sofisticata**, letale; «brilla quando una nave riesce ad avvicinarsi» |
| **torretta** | 106/107/108 | due coilgun su una **torretta agile**: «inadatta contro le armi a lungo raggio», letale da vicino |
| **generatore laser** | 173/174 | **fibra ottica drogata** lunga centinaia di chilometri; la luce viene **convogliata** alle torrette, che non devono stare vicine al generatore |
| **torretta laser** | 202/203 | la torretta contiene **solo l'ottica**: la luce arriva da altrove; serve un generatore per farla funzionare |

## 2. Il tema: la fisica del combattimento

Le schede non descrivono solo armi: spiegano **perché** funzionano o no. Il `Speck` è «facilmente fermato» dagli scudi; la
`Speckle` «squarcia corazza e scafo» ma è **respinta** contro gli scudi; la torretta è penalizzata da portata e velocità; il
generatore laser esiste **per separare** la sorgente dalla torretta.

La resa mantiene questa **causalità** con connettivi espliciti — «Data la portata limitata», «Contro gli scudi, però», «Per
questo» — che l'inglese affidava a frasi più brevi.

## 3. La nota di sistema: due armi, una regola

| riga | arma | testo |
|---|---|---|
| 69 | `Speckle Coilgun` | «Le munizioni di quest'arma si possono rifornire in qualsiasi **emporio**.» |
| 108 | `Speckle Turret` | **identico** |

`outfitter` → **emporio** (corpus). Sono **note di gioco**, non prosa: la loro funzione è **informare il giocatore**, e la forma
deve essere identica in tutto il gioco.

## 4. Il refuso che non si copia

La riga 174 ha `can altered`: **manca il verbo**. Non è una forma stilistica, è un errore di scrittura. La resa è «può essere
**modificata**», e il test verifica che `altered` **non** sopravviva.

La regola è la stessa dei refusi già incontrati: `Gypusm's` (L286) → «Gypsum's», `Although is it lightly armed` (L287) → «Sebbene
sia armata alla leggera». **Si traduce il senso, non l'errore.**

## 5. Scelte di resa

| inglese | resa |
|---|---|
| `densely-wound metallic glass slugs` | **proiettili di vetro metallico, avvolti fittamente** |
| `via hypervelocity impacts` | **grazie agli impatti iperveloci** |
| `momentum-repulsion shield systems` | **sistemi di scudi a repulsione di quantità di moto** |
| `accelerating them on a traveling wave of magnetic energy` | **accelerandoli su un'onda viaggiante di energia magnetica** |
| `as capacitors are discharged through a series of coils` | **mentre i condensatori si scaricano attraverso una serie di bobine** |
| `a deadly albeit relatively unsophisticated weapon` | **un'arma letale, anche se relativamente poco sofisticata** |
| `it can begin tearing through armor and hull` | **inizia a squarciare corazza e scafo** |
| `which shrug off its mass driver rounds` | **i suoi colpi da cannone a massa vengono respinti** |
| `mounts a pair of coilguns onto a nimble turret` | **monta una coppia di coilgun su una torretta agile** |
| `a monolithic slab of semiconductor diode` | **una lastra monolitica di diodo a semiconduttore** |
| `can be gain-switched to pulse at a variety of frequencies` | **possono essere commutate in guadagno per emettere impulsi a frequenze diverse** |
| `can be easily tapped and routed via optical fibers or mirrors` | **può essere prelevata e convogliata tramite fibre ottiche o specchi** |
| `the precise optics seems designed to hold a beam on target` | **l'ottica di precisione … sembra progettata per mantenere il fascio sul bersaglio** |
| `a typical pulsed-shot human antimissile system` | **un tipico sistema antimissile umano a raffiche pulsate** |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **6** (68, 69, 107, 108, 174, 203) | **6** |
| virgolette | **0** | **0** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **1** | **10** |
| unità ripetute | **2** (69, 108) | **2**, identiche |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`; **nessuna revisione umana**.
- **Prossimo lotto**: righe **264–703** — **21 unità**, **489 parole**, **6 contesti**, **7 tab** (265, 614, 615, 658, 659, 702,
  703), **10 virgolette**, **3 apici**. **Tipi misti**: `13 DESCRIPTION + 5 TEXT + 3 VALUE`. È il **primo lotto del progetto con
  `TEXT` e `VALUE` insieme** in un file di armi: i `VALUE` si **copiano**, i `TEXT` sono **prosa da comporre**, e le **10
  virgolette** vanno verificate **per unità**.
