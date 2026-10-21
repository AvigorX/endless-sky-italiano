# REPORT — L62 · `data/human/culture conversations.txt` (righe 566–611)

**Esito: CHIUSO.** 30/30 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

Una sola scena corale: `Scientists at the Pub after a Conference` (30 unità, tre blocchi di origliamento
separati dalle etichette `overheard scientists 1/2/3`).

| Blocco | Unità | Contenuto |
|---|---|---|
| Ingresso | 1–3 | Il congresso di genomica microbica, il badge caduto, la scelta di ascoltare o cercare un posto tranquillo |
| Origliamento 1 | 4–14 | Due giovani nervosi prima delle presentazioni, il consiglio di chi ha già parlato, l'occhiataccia alle «domande» che sono commenti, la polemica sulle mutazioni sinonime |
| Origliamento 2 | 15–25 | Il gruppo scaldato dall'alcol: riproducibilità del software, il computer bloccato, i colleghi «presuntuosi carismatici», il doppio rifiuto dei finanziamenti |
| Origliamento 3 | 26–30 | Insegnare come tregua dalla scrittura di progetti, il congresso che «ti invecchia di un anno», l'uscita dal pub |

## 2. Le scelte di traduzione che contano

**Il registro è quello di chi parla per lavoro, non per il lettore.** «Is there some law I don't know
about that requires every 'question' to start with…» → «Esiste qualche legge che non conosco per cui ogni
'domanda' deve cominciare con…». La traduzione mantiene il parlato sovrapposto, le interruzioni e le
ripetizioni dell'originale.

**Il gergo della ricerca** è reso con i termini che si usano davvero in italiano: `slide deck` → «le
slide», `graduate school` → «il dottorato», `grad students` → «dottorandi», `grant-writing` → «scrittura
di progetti», `post-mortem of the day's events` → «un'autopsia degli eventi della giornata» (metafora
medica già presente nell'inglese).

**La citazione dei colleghi** (19–20): «Singh ed Esterhazy sono dei gran presuntuosi» e poi «presuntuosi
carismatici». Il secondo intervento **corregge** il primo, e la traduzione mantiene la correzione
(«non sono solo presuntuosi: sono presuntuosi carismatici»).

**«Two is one and one is none»** (18) → «Due è uno e uno è niente»: è un detto dei sistemisti, resta
aforisma e non viene spiegato.

**Il badge** (1): «35th Annual» → «Trentacinquesimo Congresso». Il simbolo `°` è stato evitato perché il
controllo `caratteri non latini` lo segnala (0xB0): **il controllo ha funzionato**, la traduzione è stata
riscritta.

## 3. Difficoltà

- **Un solo caso tecnico**, già descritto: il `°`. Nessun altro simbolo rifiutato, 0 duplicati, 0 token.
- **Rapporto 1,010** complessivo (l'italiano è più lungo dell'inglese di dieci parole su 674): nessun
  outlier, il massimo per unità è 1,37.
- **Una sola parte da 30 unità**: sotto la banda 35–50, ma il contesto è chiuso e spezzarlo avrebbe
  separato l'ultimo origliamento dalla sua etichetta.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 36 controlli · exit 0
             unita 30 · righe 566-611 · 142 prima / 202 dopo · file 374 · max(line) 1122
             tipi 27 MISSION_TEXT + 3 UI_LABEL (4, 15, 26) · DIALOG/LOGBOOK/CONVERSATION/TEXT 0
             token 0 / 0 · tab 26 / 26 · virgolette 36 / 36 · dispari 0
             rapporto 0,81 - 1,37 · duplicati 0 gruppi (controllo negativo)
             parole 674 EN -> 681 IT
             sha256 translation.json 8b9f92399b32c32a…
```

## 5. Stato del progetto dopo L62

| Voce | Prima (L61) | Dopo L62 |
|---|---|---|
| File completi | 30 | 30 |
| Unità in staging | 23.971 | **24.001** |
| `culture conversations.txt` | 142/374 | **172/374 (46,0%)** |

Nessuna scrittura su `state.db`: le 30 unità restano `PENDING`.

## 6. Prossimo passo

**L63**: righe **624–711**, **37 unità**, 2 contesti (`Sol-Bound Shuttle` 10, `Earth Day Blackout` 27),
1.087 parole, tab 35, virgolette 51 con **3 dispari** (18, 29, 31), 1 `UI_LABEL` (30, `way in`), 0 token.
Confine: riga 819 apre `mission:Raider returning to Mordente-Bridi`.
