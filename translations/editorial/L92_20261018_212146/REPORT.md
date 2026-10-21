# REPORT — L92 · `data/successors/successor culture conversations.txt` (chiude il file)

## 1. Contenuto

Terzo e ultimo segmento, righe 230–351, cinque contesti:

- **Stage Play** (1–20): la sala all'aperto sulla costa, il rito dei contrassegni, la battuta d'apertura, i due
  riassunti della trama secondo l'attenzione del giocatore, il ritorno notturno in treno.
- **Sosrue** (21–36): il bambino e la poesia sul mostro; quattro rami di risposta e le battute del genitore, con
  le linee dorate sulla pelle che si accendono di colore.
- **Derelict Station Toy** (37–43): il modellino di navetta Kvelqde; tre scelte, tre esiti.
- **Pet Commemoration** (44–45): la targa per la salamandra domestica, con la citazione shakespeariana.
- **Armor Reconfiguration** (46): una nave da guerra delle Alte Casate e i bracci meccanici che riconfigurano
  l'armatura in metamateriale.

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `they` per Myiara | **femminile** dove l'italiano obbliga il genere | l'inglese usa `they`; la resa è dichiarata, non dedotta, e resta coerente in 11, 12, 16, 18 |
| `Deathless Myiara` (L91) | **Myiara l'Immortale** | titolo tradotto, nome proprio invariato |
| `box` (teatro) | **palco** | è il palco laterale, non un «box» |
| `token` (contrassegno) | **contrassegno** | non è un segnaposto `<…>`: è un oggetto di scena |
| `goopy` | **viscide** | consistenza, non giudizio |
| `Such stuff as dreams are made on` | **Di questa materia sono fatti i sogni** | citazione della *Tempesta* nella forma italiana corrente |
| `burbling with strange laughter` | **gorgogliando una risata strana** | `burbling` è il suono dei Successori |
| `a pastel shade of pink` | **una tonalità di rosa pastello** | il colore è della pelle, non dell'abito |

## 3. Difficoltà

1. **Due virgolette dispari nel sorgente** (unità 13 e 21): il testo teatrale apre una citazione e non la chiude.
   Il `check.py` le dichiara come unico caso ammesso e le verifica **per unità**; chiudere la citazione sarebbe
   un errore, non una correzione.
2. **Il rapporto di unità 29** era **1,95** al primo giro («Una volta ho lottato con una creatura del genere…»):
   fuori dal gate 0,55–1,90. Riscritta in «Una volta ho lottato con una, in fondo a una nebulosa.» (1,25). La
   soglia non si tocca.
3. **La ripetizione 17/20**: due punti d'uscita della stessa scena con lo stesso inglese, resa identica.
4. **Cinque contesti con tipi tutti uguali**: nessuna ambiguità di classificazione, ma le scene brevi
   (Pet Commemoration: 2 unità) vanno lette insieme alla successiva per non tagliare un dialogo.
5. **`verify.py` di chiusura**: legge i `translation.json` di **tutti** i lotti del path e asserisce 114 id
   distinti, 0 sovrapposizioni e 34+34+46 = 114. La copertura non si dimostra col solo lotto corrente.

## 4. Numeri osservati

```
unita' 46/46 · tab 42 · virgolette 48 = 48 (13 e 21 con una sola, riprodotte) · token 1 = 1 (<ship>, 41)
parole EN 1848 -> IT 1775 · rapporto 0.88 - 1.43
righe 230/351 · file 114 unita · max(line) 351 · 68 prima / 0 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (29 controlli)
sha256[:16] ac367d9586bdaad5
file: 114/114 · 3 lotti · 4063 EN -> 3873 IT · 0 sovrapposizioni
```

## 5. Stato del progetto

```
TOTALE staging: 24987 unita · 796402 EN · 755210 IT
successor culture conversations.txt: 114/114 (100%) · 3 lotti · CHIUSO
file completi: 37 · residuo traducibile (formula state.py): 6943
residuo misurato: 7507 unità / 179623 parole su 129 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli) **e** `verify.py` exit **0** (29 controlli) **e** invariante di file 114/114 |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 46 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il file è chiuso, la campagna no**: restano **7.507 unità / 179.623 parole** su **129 file**; il prossimo
  contratto è `HANDOFF_L93_20261018.md` (`coalition culture conversations.txt`, righe 1–66).
- **Nessuna revisione umana**.
