# REPORT — L100 · `hai culture conversations.txt` (Academy e musical robotico)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Academy Motto` | 227–263 | 27 | spazioporto bloccato, due scelte iniziali, caffè con holo-menu, panino al burro di ghiande, il motto sul cancello e la spiegazione della cameriera |
| `Robotic Musical 1` | 278–306 | 17 | le casse animate, la pubblicità di «Le regole della nonna», il capitano mercantile che riconosce il traduttore |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Academy` | **Academy** (invariato) | nome dell'istituzione, come `ME2` e `Musical Entertainment Expo` |
| motto | «**Conoscere è guidare, studiare è conoscere, servire è studiare, guidare è servire.**» | chiasmo riprodotto nella stessa forma AB-BC-CB-CA |
| `"non-technical university"` | **«università non tecnica»** | è la resa del dispositivo, non un termine nuovo |
| `acorn butter` | **burro di ghiande** | piatto Hai ricorrente |
| `staff member` | **membro del personale** | neutro rispetto al genere, come il sorgente |
| `surcharge for eating on the terrace` | **supplemento per mangiare sulla terrazza** | |
| `comm pad` | **commpad** | grafia già usata nei lotti precedenti |
| `median strip` | **spartitraffico** | |
| `robotic caricatures of Hai` | **caricature robotiche di Hai** | |
| `animatronic Hai` | **Hai animatronici** | prestito tecnico conservato |
| `"The Grandmother's Rules"` | **"Le regole della nonna"** | titolo tradotto, virgolette dritte come nel sorgente |
| `have the time of a decade` | **vivere il decennio della propria vita** | bisticcio su *time of your life*, riprodotto nella forma italiana |
| `interactive heckling responses` | **risposte interattive alle provocazioni del pubblico** | *heckling* = apostrofare un comico |
| `73 credits` | **73 crediti** | valuta di gioco |
| `racoon-like gray around his eyes` | **un grigio da procione intorno agli occhi** | refuso del sorgente (`racoon`) non corretto |
| `merchant captains` | **capitani mercantili** | |
| `wry grin` | **sorriso sornione** | |
| `Didn't know they'd started making live translator devices!` | **Non sapevo che avessero iniziato a fare dispositivi di traduzione dal vivo!** | |

## 3. Difficoltà

1. **Quattro citazioni aperte e non chiuse** (23, 24, 39, 41): il discorso continua nell'unità successiva. Non è
   un refuso — è il modo in cui il sorgente spezza le battute lunghe. Il controllo asserisce l'insieme esatto
   (`odd == [23, 24, 39, 41]`) e che ognuna **finisca senza virgoletta**.
2. **Le virgolette non sono una per unità**: la 39 ne ha **tre** (`"…," dice. "…`), la 25 e la 40 ne hanno
   quattro, la 22 quattro con una citazione annidata in un commento del narratore. Due asserzioni della prima
   stesura davano per scontato «una virgoletta ciascuna»: **erano sbagliate** e sono state riscritte sul
   conteggio reale, non sul numero che ricordavo.
3. **Tre `UI_LABEL`** in un lotto: `field trip`, `pleasant lunch`, `finishing chat` sono etichette di salto e
   restano **identiche**. Il `check.py` verifica anche che **nessun'altra** unità sia identica al sorgente,
   così un'etichetta dimenticata o una battuta non tradotta emergono subito.
4. **Il motto è un chiasmo**: «To know is to lead, to study is to know, to serve is to study, to lead is to
   serve». Una resa più libera lo avrebbe appiattito in un elenco; la struttura A→B, B→C, C→D, D→A regge.
5. **`have the time of a decade`**: bisticcio su *the time of your life*. In italiano «il decennio della propria
   vita» conserva lo scarto e non diventa «un momento indimenticabile».

## 4. Numeri osservati

```
unita' 44/44 · 41 MISSION_TEXT + 3 UI_LABEL · tab 39 · virgolette 40 = 40 · token 1 = 1 · quadre 0
parole EN 1587 -> IT 1512 · rapporto 0.76 - 1.57
righe 227/306 · file 147 unita · max(line) 386 · 77 prima / 26 dopo
FAIL totale: 0 (30 controlli) · verify exit 0 (28 controlli)
sha256[:16] 8fb5defc43780334 · copertura file 121/147 (82,3%)
```

## 5. Stato del progetto

```
TOTALE staging: 25265 unita · 810398 EN · 768191 IT
hai culture conversations.txt: 121/147 (82,3%) · 3 lotti
file completi: 38 · residuo traducibile (formula state.py): 6669
label fuori staging: 55 · unità traducibili residue misurate: 7240 / 165649 parole su 128 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 44 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: restano **26 unità** sulle righe 321–386 (`Hai Film Release`, `Sick of Acorn
  Bread`); prossimo contratto `HANDOFF_L101_20261018.md`, che è anche **l'ultimo segmento** del file.
- **Nessuna revisione umana**.
