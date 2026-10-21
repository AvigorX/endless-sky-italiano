# REPORT — L279 (`data/human/kestrel.txt`, righe 56–164)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **26 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 33 (tutte `MISSION_TEXT`) | 33 |
| parole | 501 | **439** (0,88) |
| tab | 32 | 32 · primo carattere |
| virgolette | 94 | **94**, per unità |
| segnaposto | 3 (3 famiglie) | **3** |
| apici | 16 | 10 |

Rapporto per unità **0,71 – 1,14**. Il minimo (0,71) è l'unità 3, dove l'inglese usa tre subordinate che l'italiano chiude in
due righe.

## 2. Il lotto

| unità | contenuto |
|---|---|
| 1-3 | istruzioni: sistema `<waypoints>`, **disabilitare senza distruggere**, perdita del pagamento |
| 4 | rientro: Atinoda chiede com'è andata (unica unità **senza** tab) |
| 5-6 | «Sì, hai costruito una nave impressionante» / «No, l'ho liquidata in fretta» |
| 7-8 | «qualche ritocco prima di produrla in serie»: **due varianti** della stessa domanda |
| 9-12 | le quattro proposte del giocatore: armi, motori, scudi e scafo, baie di caccia |
| 13-16 | le quattro risposte: ampliare la capacità, rafforzare, integrare |
| 17-32 | il nome: `Wraith`, `Grey Goose`, `Dire Wolf`, `Reaper`… e `Kestrel` **quattro volte** |
| 33 | l'epilogo: il sussulto, i **due milioni di crediti**, gli auguri |

## 3. Le 94 virgolette

Il controllo è **per unità**, non sul totale. Con 33 battute e 94 virgolette, la maggior parte delle unità ne ha **quattro**
(una citazione che contiene una domanda). Una sola virgoletta mancante lascerebbe il totale a 93 e sarebbe invisibile a un
controllo aggregato: è la trappola già incontrata in L278 e qui verificata su un campione tre volte più grande.

## 4. La gag del nome

`"La Kestrel."` compare **quattro volte** identica (unità 23, 26, 29, 32). Il `check.py` **conta** queste occorrenze e conta
anche le due di `"La Grey Goose."` e le due di `"Il Wraith."`: se una ripetizione fosse stata «variata» per eleganza, la
struttura comica si sarebbe rotta e il test sarebbe rosso.

Un dettaglio tipografico: all'unità 33 la parola è fra **apici semplici** (`'Kestrel'`), non virgolette — il sorgente li usa
per distinguere la **parola citata** dal discorso. Sono conservati, ed è il motivo per cui gli apici italiani di quell'unità
sono **due**.

## 5. Terminologia

| inglese | resa | nota |
|---|---|---|
| `mass-producing` | **produrre in serie** | |
| `a few tweaks` | **qualche ritocco** | |
| `weapon space` / `weapon capacity` | **spazio per le armi** / **capacità per le armi** | |
| `engine capacity` | **capacità dei motori** | |
| `shield matrix` | **matrice degli scudi** | |
| `fighter bays` | **baie di caccia** | forma maggioritaria del corpus (9) |
| `two million credits` | **due milioni di crediti** | |
| `your future endeavors` | **le tue future imprese** | |
| `Wraith`, `Grey Goose`, `Dire Wolf`, `Reaper`, `Falcon`, `Osprey`, `Hawk` | **invariati** | nomi di nave |

## 6. Verifica

```
check.py   26 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
segmento   16 prima · 33 qui · 2 dopo la 164 · copertura 49/51 (96,1%)
```

Primo giro **verde**, sia `check.py` sia `verify.py`: le misure strutturali (32 tab, 94 virgolette per unità, 3 segnaposto,
16/10 apici) erano state prese **prima** di scrivere gli script, e nessun rosso ha richiesto correzioni.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 33 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 49/51; restano due unità (il messaggio di `Kestrel Available` e la `DESCRIPTION` della nave).
