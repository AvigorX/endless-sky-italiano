# REPORT — L109 · `korath missions.txt` (i morti da riportare a casa, tre generazioni perdute)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Efreti: Distress Call 2` (coda) | 338–340 | 3 | evacuazione, tre morti nel volo, messaggio dei Quarg, pagamento |
| `Efreti: Distress Call 3` | 345–376 | 12 | la delegazione, l'ologramma, i principi del clan, il rifiuto, la proposta |
| `Efreti: Distress Call 4` | 388–434 | 13 | tute ambientali, bare a forma di uovo, effetti personali, sbarco, 66 uomini da trovare |
| `Efreti: Distress Call 5` | 437–451 | 5 | squadra di recupero, `<bunks>` cuccette, gli Hai che non osano |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Recover the fallen crew of the <EDC-ship>` | **identico** | `VALUE`, nome di missione |
| `Recover the fallen of <EDC-ship>` | **identico** | `VALUE` |
| `<EDC-ship> salvage team` | **identico** | `VALUE` |
| `Recover the bodies of the dead … crew on <destination> and return them to <origin>` | **Recupera i corpi dell'equipaggio morto … su `<destination>` e riportali a `<origin>`** | `<origin>` = **partenza** |
| `Return the bodies … to <planet>` | **Riporta i corpi … su `<planet>`** | variante senza `<origin>` |
| `Hire a <bunks> member salvage team` | **Assolda una squadra di recupero di `<bunks>` persone** | `<bunks>` è un numero |
| `You need <bunks> available bunks` | **Vi servono `<bunks>` cuccette libere** | stesso token, altro ruolo |
| `Bold human!` | **Umano audace!** | Quarg cerimoniale |
| `With profuse thanks we offer you for helping` | **Con copiosa gratitudine vi ricompensiamo per aver aiutato** | il sorgente omette l'oggetto: reso con «ricompensiamo» |
| `the Efreti are reminded why they live crushed together around these few stars` | **agli Efreti si ricorda perché vivono pigiati intorno a queste poche stelle** | |
| `Salutations, far traveler` | **Salute, viaggiatore lontano** | |
| `These Korath-Friends are the princes of the clan` | **Questi Amici dei Korath sono i principi del clan** | |
| `While grateful for the living, they cannot fully mourn those that lie dead` | **Grati per i vivi, non possono però piangere del tutto coloro che giacciono morti** | |
| `They beseech you travel back` | **Vi supplicano di tornare** | |
| `the leader of the group visibly sags` | **Il capo del gruppo si affloscia visibilmente** | |
| `three generations were lost` | **sono andate perdute tre generazioni** | |
| `We offer you title to salvage` | **Vi offriamo il titolo per recuperare** | *title* = titolo di proprietà |
| `environment suits` | **tute ambientali** | |
| `Korath ships run hot` | **le navi Korath sono roventi** | |
| `fibrous, vaguely egg-shaped coffins` | **bare fibrose e vagamente a forma di uovo** | |
| `they stack together like a clutch of eggs in a nest` | **si incastrano insieme come una covata di uova in un nido** | ripetuto **identico** in 20, 21, 22 |
| `personal effects` | **effetti personali** | |
| `a cacophony of barking sounds` | **una cacofonia di suoni che abbaiano** | |
| `a data chip that vaguely reminds you of a license` | **un chip dati che vi ricorda vagamente una licenza** | |
| `at least 66 additional crew` | **almeno 66 membri d'equipaggio in più** | numero in cifre |
| `Greenwater, in Hai space` | **Greenwater, nello spazio Hai** | toponimo invariato |
| `the crossfire of the Mereti and Sestor war` | **il fuoco incrociato della guerra fra Mereti e Sestor** | |

## 3. Difficoltà

1. **`<origin>` contro `<destination>`**: due token vicini e opposti. Il controllo è **per unità** (unità 5:
   `<EDC-ship>`, `<destination>`, `<origin>` in quest'ordine) e verifica che i conteggi per token coincidano uno per
   uno: uno scambio fra i due lascerebbe il totale corretto.
2. **Due coppie di ripetizioni** (1/4 e 2/5): i due `VALUE` sono **identici per regola**, le due `DESCRIPTION`
   **identiche nel sorgente** e quindi rese identiche. Il `check.py` non può usare il criterio «nessuna
   ripetizione»: qui le ripetizioni sono **due** e vanno **dichiarate**, non vietate.
3. **Tre quasi-duplicati** (18/19, 20/21/22, 24/25): il rischio opposto. Differiscono per soggetto o coda, e
   l'italiano deve conservare la differenza; il `check.py` la verifica sull'apertura o sulla coda.
4. **`check.py` inizialmente rosso su due controlli** perché cercava `startswith` su stringhe che iniziano con il
   **tab**: corretto con `.strip()`. È la trappola già nota delle unità indentate.
5. **Unità 2, frase del Quarg lunga con due virgolette** e un periodo di quattro frasi: il registro cerimoniale
   regge solo se non si spezza in frasi brevi.
6. **`no crew helping you`** (unità 19) e **`The crew makes a last sweep`** (24) contro **`As a precaution`** (25):
   il gioco distingue le varianti per equipaggio presente o assente; l'italiano lo fa con «senza nessuno del
   vostro equipaggio ad aiutarvi» e «Per precauzione».

## 4. Numeri osservati

```
unita' 33/33 · 27 MISSION_TEXT + 3 VALUE + 3 DESCRIPTION
tab 20 · virgolette 14 = 14 (tutte binate) · token 23 = 23 in sette famiglie
quadre 0 · citazioni aperte 0 · ripetizioni: 2 coppie dichiarate (1/4, 2/5)
parole EN 1205 -> IT 1188 · rapporto 0.89 - 1.28
righe 338/451 · file 158 unita · max(line) 580 · 99 prima / 26 dopo
FAIL totale: 0 (30 controlli) · verify exit 0 (33 controlli)
sha256[:16] 6e60f04cc8291cb4 · copertura file 132/158 (83,5%)
```

## 5. Stato del progetto

```
TOTALE staging: 25601 unita · 821324 EN · 778747 IT
korath missions.txt: 132/158 (83,5%) · 4 lotti
file completi: 40 · residuo traducibile (formula state.py): 6329
residuo misurato: 6908 unità / 154731 parole su 126 file
avanzamento: 25601/32924 unità (77,8%) · 821324/979975 parole (83,8%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (33 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 33 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: **26 unità** residue in tre contesti (`Distress Call 6`, `7`, `8`); prossimo
  contratto `HANDOFF_L110_20261018.md` (righe 474–580), che **chiude** `korath missions.txt`.
- **Nessuna revisione umana**.
