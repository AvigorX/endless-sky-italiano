# REPORT — L56 · `data/gegno/gegno I corroboration.txt` (righe 29–904)

**Esito: CHIUSO.** 171/171 unità, `check.py` `FAIL totale: 0`, `verify.py` exit 0.

## 1. Che cosa contiene il lotto

Il segmento è interamente sulla linea narrativa Gegno, dopo la chiusura di `gegno intro missions.txt`
(L53–L55). Struttura:

| Contesto | Unità | Contenuto |
|---|---|---|
| `Passive-Aggressive Observations` | 1–14 | Ritorno sul pianeta desertico: navi Vi, l'intercettore, i due rami (ritirarsi / avanzare) |
| `Foreign Spectator I` | 15–15 | Flotta Vi e Scin che assiste a un duello: non interferire |
| `Brief Bystander` | 16–21 | Il pianeta-cimitero di strumenti, lo shuttle civile, il Gegno che se ne va |
| `Scin on Cyife` | 22–27 | La luna di ghiaccio, la nave Scin a forma d'uovo, i tre esiti (`saw`/`boarded`/altro) |
| `Battle over Zydee` | 28–29 | Gli Scin al lavoro, poi la flotta Vi che entra nel sistema |
| `Gegno Suspicions` | 30–60 | **Il cuore del lotto**: Adrauni, le lamentele dei Gegno, i due rami di risposta, la convocazione |
| `Return to Giaru Gegno` | 61–62 | Descrizione, messaggio in arrivo, etichetta `Convocazione dei Gegno` |
| `Gegno Anticipation` | 63–171 | L'incontro con Adrauni e il Gegno, il colloquio, i due epiloghi |

## 2. Le scelte di traduzione che contano

**La voce di Adrauni.** Nel sorgente parla con sintassi inversa («Eight revolutions you have been given
by the Gegno», «Meddled in their affairs you have, one too many times»). In italiano l'inversione non
sopravvive come costrutto: si rende con **dislocazione a sinistra + punteggiatura** («Otto rivoluzioni ti
sono state date dai Gegno per comparire sul loro mondo») e con un registro sostenuto, non con errori.
Dove il sorgente è dritto, la traduzione è dritta: nessuna inversione aggiunta (decisione 187).

**`tolerate` / `dismissed`.** Il Quarg distingue tre cose che l'italiano tende a fondere: *dismissed*
(«congedato»), *exiled* («esiliato»), *shunned* («ripudiato»). La progressione è nel testo e va mantenuta:
unità 8 «congedato», unità 12 «esiliato, o forse ripudiato».

**`Turf Wars`** resta invariato (nome proprio di un conflitto storico del mondo di gioco).
**`corsari`** per *privateers*: è il termine già usato nella linea Avgi.
**`Dueyu Eitch`** invariato: è il nome del mondo natale, non un toponimo traducibile.
**`Adrauni`** è un **titolo**, non un nome: «uno con il titolo di 'Adrauni'» (unità 47, 59), coerente in
tutto il lotto.

**I grugniti dei Gegno.** Il Gegno Vi non parla: grugnisce, sbuffa, fa gesti, e in un punto «parla con un
brontolio basso, un po' come un sussurro detto ad alta voce». Le righe in lingua Gegno
(`"Tchii ciei escitch tchii iedf teih Voordhte!"`) restano **identiche**: sono suoni, non testo da tradurre.

**I due epiloghi.** `epilogue a` (125–156) e `epilogue b` (158–169) ripetono lo stesso discorso di
Adrauni quasi parola per parola. Non si uniformano a mano: le parti comuni sono tradotte in modo
identico perché **lo sono in inglese**, e i controlli dei duplicati lo verificano (10 gruppi, 30 unità).

## 3. Difficoltà incontrate

- **`label` come chiavi.** 28 `UI_LABEL`, il massimo della serie: `ask`, `escort`, `quarg escort`,
  `no escort`, `visit a`, `visit b`, `epilogue a`, `epilogue b`, `end a`, `end b`, `dont know` (senza
  apostrofo, refuso del sorgente riprodotto), `what does home mean`. Sono identificatori di salto: una
  traduzione qui romperebbe il flusso della missione. Restano identici e sono elencati uno per uno nel
  `check.py`.
- **`DIALOG` 170/171 identiche.** È la stessa scena agganciata a due esiti. La resa è identica per
  necessità dichiarata (`CONV_SAME`), non per pigrizia: il `verify.py` confronta le due unità e lo asserisce.
- **Il primo `verify.py` era rosso per un motivo sbagliato.** Asseriva `0 prima / 287 dopo`: il valore
  giusto era **0 / 127**. Corretto prima di dichiarare il lotto chiuso.

## 4. Verifica osservata

```
check.py   → 33 controlli · FAIL totale: 0
verify.py  → 40 controlli · exit 0
             unita 171 · righe 29-904 · 0 prima / 127 dopo · file 298 · max(line) 1287
             token 12 / 12 (5 famiglie) · tab 129 / 129 · virgolette 238 / 238
             rapporto 0,57 - 1,48 · duplicati 10 gruppi (30 unita)
             parole 5.671 EN → 5.138 IT
             sha256 translation.json c2fe3862c23a294e…
```

## 5. Stato del progetto dopo L56

- File `gegno I corroboration.txt`: **171/298**.
- File completi: **29** (invariato: L56 apre, non chiude).
- Unità tradotte in staging: **23.702** (23.531 + 171).
- Nessuna scrittura su `state.db`: le 171 unità restano `PENDING`.

## 6. Prossimo passo

**L57**: righe 905–1287 (le prime unità stanno sulla 943), **127 unità**, 3 contesti —
`Gegno Intervention` 1–23, `Acquiescence` 24–104, `Gegno Asteroid Mining Prologue` 105–127 —
e **chiude il file a 298/298** (30° file completo).
