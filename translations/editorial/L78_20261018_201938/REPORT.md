# REPORT — L78 · `data/successors/successor side missions.txt`

## 1. Cosa contiene il lotto

**L'incontro** (1–18). Nello spazioporto di `<origin>` due Successori stanchi trascinano un carretto di
tessuto piegato. Sono **Nnesa** e **Jaasora**, **osservatori di stelle**: vogliono andare al **bordo più
lontano della galassia**, dove «il cielo è diviso fra notte stellata e vuoto assoluto». Offrono un compenso
modesto e portano la propria attrezzatura.

**La scelta** (19–29). Due varianti dello stesso dialogo (l'una dopo l'altra nel file), poi i nomi e il
carico: il carretto è «molto più pesante di quanto sembri», e la coppia è inseparabile.

**Khosa-Kella-Oa** (30–36). Nel sistema **Maspa-Mavra** l'entusiasmo diventa soggezione: la galassia intera
è spiegata nel cielo. Il pianeta è «freddo, scuro e roccioso», indistinguibile da mille altri mondi senz'aria
— ma la stella è così fioca che «non c'è quasi bagliore». La tenda si gonfia in un **sollevatore a
repulsione** e scivola via come ghiaccio che si scioglie.

**La mappa** (37–52). Al ritorno Nnesa mostra una **mappa stellare** disegnata a mano; diversi disegni
ritraggono Jaasora invece delle stelle. Chiede da dove venga il capitano e il giocatore indica la propria
casa: tre rami (indicare `<home system>`, indicare `Sol`, indicare la distesa). Nnesa pronuncia il nome, lo
trascrive, e per `Sol` rivela il nome Successore: **Saaqa-Viirja**.

**Il congedo** (53). Jaasora paga `<payment>` e ringrazia: «È stato un viaggio vero e gioioso».

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `stargazers` | **osservatori di stelle** | appassionati, non astronomi professionisti |
| `fah soom`, `novel name` | **identiche** | `label` di salto, in `NT` |
| `Thour't` / `'tis` / `dost thou` | «Sei» / «è» / «vieni» | arcaico reso con italiano corrente, senza arcaismi finti |
| `repulsor lift` | **sollevatore a repulsione** | termine tecnico |
| `tent` / `gliding tent` | **tenda** / **tenda planante** | scivola sul pavimento, non vola |
| `a scion of the constellations` | **un erede delle costellazioni** | `scion` → «erede» (L70–L72) |
| `Saaqa-Viirja` | invariato | nome Successore di Sol |
| `Sol` | invariato | nome umano, e il testo lo mette in opposizione |

## 3. Difficoltà incontrate

1. **Due varianti dello stesso dialogo** nello stesso lotto (13/20, 15/22, 16/23): le stesse battute ripetute
   in due rami. Rese identiche e dichiarate; il controllo «duplicati italiano non spiegati» le accetta solo
   perché sono gruppi del sorgente.
2. **Due opzioni identiche** (39/41) e **due risposte identiche** (45/49): stessa scelta, stessa resa —
   l'opposto del caso L77 (22 contro 50), dove l'inglese distingueva.
3. **Nessuna virgoletta dispari**: 86, tutte pari, e il `verify.py` dichiara l'assenza.
4. **Nessun token in due unità lunghe** (30, 37): il `<ship>` c'è quattro volte, ma non dove sembra.
5. **Un refuso del sorgente** (`Thour't`): reso senza replicarlo.

## 4. Numeri osservati (output letto)

```
unita' 53/53 · copertura 53/53
tab IT 46 / EN 46 · virgolette IT 86 / EN 86 · dispari 0
token IT 13 / EN 13 (7 famiglie)
rapporto IT/EN 0.74 - 1.53
parole EN 1109 -> IT 1060
prima/ultima riga del segmento: 224/325
duplicati inglese: 5 gruppi (10 unita)
FAIL totale: 0    (31 controlli)
verify.py exit 0  (39 controlli)
sha256[:16] a0ebf1dce186051d
```

## 5. Stato del progetto dopo il lotto

```
TOTALE staging: 24710 unita · 788189 EN · 747081 IT
successor side missions.txt: 116/164 (70,7%) · 3018 EN -> 2889 IT · 2 lotti
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli) **e** `verify.py` exit **0** (39 controlli) |
