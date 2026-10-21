# REPORT — L261 (`data/remnant/remnant jobs.txt`, righe 19–209)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **20 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 25 (11 `DIALOG` + 7 `DESCRIPTION` + 7 `VALUE`) | 25 |
| parole | 404 | **419** (1,04) |
| tab / virgolette | 0 / 0 | 0 / 0 |
| apici | 2 | 4 |
| segnaposto | 29 in 6 famiglie | 29, **stesso ordine per unità** |
| contesti | 7 | 7 |

Rapporto per unità **0,90 – 1,26**: nessuna resa fuori gate, nessuna accorciata dopo la misura.

## 2. I sette contesti, in sequenza

```
1– 4   mission:Remnant: Bounty
5– 8   mission:Remnant: Bounty 2
9–11   mission:Remnant: Broken Jump Drive job
12–15  mission:Remnant: Expanded Horizons Astral job
16–19  mission:Remnant: Expanded Horizons Astral job late
20–23  mission:Remnant: Bounty 3
24–25  mission:Remnant: Bounty 4
```

Il `check.py` verifica le **sette coppie (prima unità, ultima unità, contesto)**, non solo il numero di contesti: un lotto
che ne contenesse sette in ordine diverso passerebbe un controllo sul conteggio e fallirebbe questo.

## 3. I `VALUE` non sono «non tradotti»

| unità | inglese = italiano |
|---|---|
| 1 | `Crippled <npc model> Bounty` |
| 5 | `Troublesome <npc model> Bounty` |
| 9 | `Broken Jump Drive Delivery` |
| 12, 16 | `Research Expedition to <waypoints>` |
| 20 | `Damaged Rano'erek Bounty` |
| 24 | `Marauding Rano'erek Bounty` |

Sono i **nomi dei lavori** mostrati nella bacheca: dati, non prosa. Il test asserisce **l'identità per indice**, e in
parallelo che **tutte** le altre 18 unità siano diverse dall'inglese. I due controlli insieme distinguono «copiato perché è
un dato» da «copiato per dimenticanza».

## 4. Le due famiglie che si somigliano

`<npc model>` (2) è il **modello** della nave Korath (`Crippled <npc model> Bounty`); `<npc>` (3) è la **nave** specifica
(«aver dato la caccia alla `<npc>`», «la nave Korath `<npc>`»). Il `verify.py` verifica le due famiglie **separatamente**:
un totale di 5 non distinguerebbe un simbolo scambiato con l'altro, ed è un errore che il gioco mostrerebbe come nome di
nave al posto del modello.

## 5. Le formule

| inglese | resa | occorrenze |
|---|---|---|
| `A … Korath ship is … in Remnant territory. Hunt it down, and then return to <planet> to receive your payment of <payment>.` | «Una nave Korath … nel territorio dei Remnant. Dalle la caccia e poi torna su `<planet>` per ricevere il pagamento di `<payment>`.» | 4 (con quattro participi diversi) |
| `You have destroyed the Korath ship. You can now return to <planet> to collect your payment.` | «Hai distrutto la nave Korath. Ora puoi tornare su `<planet>` per riscuotere il pagamento.» | 3 (identiche) |
| `A Remnant military leader thanks you for hunting down …, and gives you the agreed-upon payment of <payment>.` | «Un comandante militare dei Remnant ti ringrazia per aver dato la caccia a … e ti consegna il pagamento concordato di `<payment>`.» | 2 forme (con e senza `the Korath ship`) |

I quattro participi: `crippled` → **in avaria**, `troublesome` → **sta creando problemi**, `damaged` → **danneggiata**,
`marauding` → **sta saccheggiando**. Ogni variante ha la sua resa; la parte fissa è identica, e il `check.py` verifica che i
gruppi identici abbiano **una sola** resa.

## 6. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  20 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 25 qui · 62 dopo la 209 · copertura 25/87 (28,7%)
```

Entrambi verdi al **primo** giro. L'unica correzione è stata fatta **prima** di eseguire il `verify.py`: un controllo sugli
apici usava `enumerate(tu, 1)` (la **posizione**) invece di `u['idx']` (l'**identificatore**). Oggi coincidono, ma è una
coincidenza del lotto, non una garanzia: con un lotto che parte da un indice diverso da 1 il controllo misurerebbe un'altra
cosa e resterebbe verde.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`.
- **Nessun testo visto nel gioco**.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 25/87; restano 62 unità su sei missioni ancora da vedere.
