# REPORT — L96 · `coalition culture conversations.txt` (quarto lotto)

## 1. Contenuto

Righe 192–234, coda del contesto `Coalition Folklore: Kimek` (27 unità, di cui 5 etichette di salto):

- i due esiti della difesa (cancello posteriore tenuto ma cancello principale sfondato; ariete al principale e
  cancello piccolo aperto) (1–4);
- il passaggio al lato **attaccanti**: l'accampamento, la tenda da guerra, il tronco-ariete, i confini del
  «gruppo», la battuta della Kimek sul «legati al suolo» (5–7);
- la carica: la scelta fra strada principale e strada laterale (8–11);
- i tre rami d'attacco e i loro esiti: sconfitta per tempo scaduto, sconfitta con il cancello piccolo tenuto,
  vittoria quando l'ariete sfonda il principale (12–23);
- il **banchetto**: la poltiglia Kimek, il piatto Saryd, il congedo dell'organizzatore (24–27).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| sintassi Kimek | **ordine marcato italiano** | come nei lotti precedenti: «Onorate di avervi…, la nostra compagnia è» |
| `war tent` | **tenda da guerra** | fra virgolette come nel sorgente |
| `gambeson` | **farsetto imbottito** | termine storico corretto per la veste imbottita |
| `battering ram` | **ariete** | termine tecnico, non «montone» |
| `set` (confini del gioco) | **gruppo** | fra virgolette, coerente con L94 («set» di forte e accampamento) |
| `groundlocked people` | **voi legati al suolo** | i Kimek si arrampicano, gli umani no: è una battuta, non un insulto |
| `soupy, half-digested mess` | **poltiglia brodosa e parzialmente digerita** | il cibo Kimek è descritto così dal giocatore, senza edulcorarlo |
| `thorns` | **spine / barbe** | «spine» nel discorso della Kimek, «barbe» nella descrizione |

## 3. Difficoltà

1. **Cinque `UI_LABEL` di salto** in mezzo alla prosa (3, 10, 15, 17, 22): non entrano nelle parti, il
   costruttore le scrive dal sorgente, il `check.py` le elenca e le asserisce identiche.
2. **Due ripetizioni inglesi**: 12/19 (una scelta) e 14/21 (un paragrafo di 90 parole, l'assalto al cancello).
   La seconda è scritta da una costante unica nel costruttore, così non può divergere.
3. **L'unità 6 ha 12 virgolette**: la spiegazione della Kimek contiene due battute, «tenda da guerra»,
   «gruppo», «spine» e il «legati al suolo». Il conteggio è per unità.
4. **Zero token** con 26 virgolette: `tok == 0` asserito.
5. **I rami 16 e 23 hanno lo stesso incipit e finali diversi** (difensori vincono / attaccanti vincono): il
   testo condiviso è identico, il finale no — ed è il sorgente a dirlo.

## 4. Numeri osservati

```
unita' 27/27 (22 tradotte + 5 UI_LABEL identiche) · tab 22 · virgolette 26 = 26 · token 0 = 0
parole EN 2248 -> IT 2023 · rapporto 0.92 - 1.45
righe 192/234 · file 157 unita · 94 prima / 36 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (29 controlli)
sha256[:16] 0c863a3843dd5f4e · copertura del file 121/157 (77,1%)
```

## 5. Stato del progetto

```
TOTALE staging: 25108 unita · 804097 EN · 762206 IT
coalition culture conversations.txt: 121/157 (77,1%) · 4 lotti
residuo traducibile (formula state.py): 6822 · misurato: 7394 unità / 171944 parole su 129 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli) **e** `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 27 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il contesto `Kimek` è chiuso; il file no**: restano **36 unità** (righe 251–462, sette contesti brevi), che
  il contratto `HANDOFF_L97_20261018.md` raccoglie **in un solo lotto** per chiudere il file.
- **Nessuna revisione umana**.
