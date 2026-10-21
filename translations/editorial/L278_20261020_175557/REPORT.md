# REPORT — L278 (`data/human/kestrel.txt`, righe 15–54)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 16 (14 `MISSION_TEXT`, 1 `DESCRIPTION`, 1 `VALUE`) | 16 |
| parole | 458 | **422** (0,92) |
| tab | 13 | 13 · primo carattere |
| virgolette | 42 | **42**, per unità |
| segnaposto | 5 (3 famiglie) | **5** |
| apici | 4 | 9 |

Rapporto per unità **0,86 – 1,12**. L'italiano è più **corto** dell'inglese: i dialoghi inglesi usano molte formule
perifrastiche («would you be willing to help us test out»), che in italiano si chiudono in meno parole.

## 2. Il lotto

| unità | battuta |
|---|---|
| 1 | `VALUE` **Warship Testing** (copiato) |
| 2 | `DESCRIPTION`: vai a `<waypoints>`, **disabilita** il prototipo, non distruggerlo |
| 3 | Atinoda riconosce il giocatore e si presenta |
| 4-5 | due risposte del giocatore («Dimmene di più» / «non ho tempo») |
| 6 | il racconto: crisi, viaggio, comune anarchica, **capanna del sudore**, la visione |
| 7-8 | «Affascinante» / «C'erano sostanze illecite…?» |
| 9-10 | due varianti quasi identiche di «Ma poi ho visto un'altra cosa» |
| 11 | la **nave scura** contro il vascello dallo **scafo rosso maculato** → nasce la Kestrel |
| 12-13 | «Ne sarei felice» / «E cosa riceverò in cambio?» |
| 14 | pagamento + diritto al **primo esemplare di serie** |
| 15-16 | «Mi sembra giusto» / le **liberatorie** |

## 3. Le 42 virgolette, una per una

Il controllo non si limita al totale: confronta il numero di virgolette **unità per unità**. Con 16 battute e 42 virgolette
totali, un errore su una singola unità (una virgoletta dimenticata) lascerebbe il totale a 41 e sarebbe visibile solo con il
controllo per unità — che è quello che il `check.py` e il `verify.py` fanno entrambi.

Le virgolette sono **dritte**, come nel sorgente: nessun caporale, nessuna conversione tipografica.

## 4. La regola del collaudo

`disable`, non `destroy`: la `DESCRIPTION` lo dice due volte (comando e avvertimento). La resa usa **«disabilitare»** e
**«Non distruggere»**, con la conseguenza esplicita («o perderai il pagamento e l'occasione di comprarne una»). È la stessa
distinzione già fissata nella missione della Dathnak A'awoj: sbagliarla rende la missione **incompletabile**.

## 5. Terminologia

| inglese | resa | nota |
|---|---|---|
| `prototype warship` | **nave da guerra prototipo** | |
| `non-destructive testing` | **test non distruttivi** | |
| `production line` | **linea di produzione** | |
| `waivers of liability` | **liberatorie** | termine legale italiano |
| `name and likeness` | **nome e la tua immagine** | |
| `vision quest` | **ricerca di visione** | termine antropologico |
| `sweat lodge` | **capanna del sudore** | |
| `anarchist commune` | **comune anarchica** | |
| `mottled red hull` | **scafo rosso maculato** | |
| `Tarazed Corporation`, `Wayfarer`, `Charles Atinoda`, `Welsh Corgi` | **invariati** | nomi propri |

## 6. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 16 qui · 35 dopo la 54 · copertura 16/51 (31,4%)
```

Due rossi al primo giro, entrambi su **asserzioni mie**:

1. la ricerca della cortesia (`Lei`) usava `\b(Le |La |Lei…)\b`, che colpiva anche «**Le tue** imprese» — forma corretta del
   «tu». Ristretto a `Lei|Senta|desidera`;
2. dichiaravo il file `righe 15-500`; il database dice **402**. Corretto il numero.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 16/51.
