# REPORT — L130 · `boarding missions.txt` (Tarquin e la nave negriera)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `boarding pirate` | 1 | 417 | la scansione del relitto e la cassa di gettoni di credito |
| `Pirate Ambush` | 2 | 479 | la capsula di salvataggio, il segnale ai pirati, l'autodistruzione |
| `Pirate Mutiny` | 3–8 | 492–514 | il ragazzo di sedici anni, i superstiti, i due diari, il pagamento |
| `Slave Crew Rescue` — ingresso | 9–15 | 535–548 | quattro varianti d'ingresso (da solo, primo ufficiale, gruppo) e Tarquin che salda una paratia |
| la prima scelta | 16–38 | 550–597 | accettare, chiedere dell'equipaggio, chiedere della nave; e tre risposte di Tarquin |
| insistere | 39–53 | 599–634 | l'attacco, la fuga di Tarquin, i prigionieri persi |
| catturarlo | 54–56 | 637–642 | la cella della tua nave, oppure l'esecuzione |
| ricattarlo | 57–61 | 649–657 | il gruppo che lo tiene in scacco, e il rifiuto di chi è da solo |
| attaccarlo da solo | 62–75 | 660–686 | «acting stupid alone», buona e cattiva sorte, e il salvataggio dell'equipaggio |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `flight suits / outfits and cargo` | **dotazioni e carico** | `outfits` = moduli |
| `distress signal` · `self-destruct sequence` | **segnale di soccorso** · **sequenza di autodistruzione** | |
| `ex-pirate crew members` | **membri dell'equipaggio, ex pirati** | `DESCRIPTION` |
| `tyrannical captain` | **capitano tiranno** | |
| `forced into servitude` | **costretta in servitù** | |
| `sidearm` | **arma da fianco** | |
| `bulkhead` | **paratia** | |
| `princely sum of 350,000 credits` | **principesca somma di 350.000 crediti** | |
| `gift horse in the mouth` | **guardare in bocca al cavallo donato** | detto reso |
| `perishable goods` | **merci deperibili** | |
| `cheapskate` · `bumpkins` | **spilorcio** · **zotici** | lessico di Tarquin |
| `paying for a lesson learned` | **pagare per una lezione imparata** | |
| `Press the matter.` | **(Insisti sulla questione.)** | |
| `slave ship` | **nave negriera** | |
| `tension like a steel cable` | **teso come un cavo d'acciaio** | |
| `stonily` | **in un silenzio di pietra** | |
| `brig` | **cella** | |
| `good riddance to bad rubbish` | **che se ne sia andato al diavolo** | reso idiomatico, non letterale |
| `cold day in hell` | **un giorno freddo all'inferno** | |
| `lifeless body sprawled out` | **corpo senza vita disteso** | |
| `malnourished wretches` | **disgraziati denutriti** | |
| `galactic criminal justice database` | **database galattico della giustizia penale** | |

## 3. Difficoltà

1. **22 `UI_LABEL` in un lotto solo**: vanno elencate e verificate identiche; il controllo pretende la lista esatta,
   non «tutte tranne».
2. **Zero `VALUE`**: la cella del controllo è un'**asserzione vuota** scritta (`== {}` e `== []`), non un'omissione.
3. **L'unità 21 ha tre virgolette** (battuta non chiusa dal sorgente): riprodotta, e il controllo verifica che
   l'unica unità dispari sia quella.
4. **Quattro varianti d'ingresso** con lunghi testi quasi identici (11, 13, 15): le parti comuni sono state rese
   **identiche parola per parola** (costanti `TAIL` e `CAUTIOUS`), così il confronto tra varianti resta leggibile.
5. **Due strade con lo stesso esito** (34 e 58; 35 e 59): la resa finale è la stessa dove l'inglese è lo stesso.
6. **45 tab su 75 unità**: quasi tutti i testi sono battute indentate.
7. **Registro di Tarquin**: affettato e minaccioso insieme (`spilorcio`, `zotici`, `lezione imparata`), verificato con
   parole-spia; e il tema della tratta è esplicito (`schiavitù`, `negriera`, `prigionia`).
8. **Gate**: minimo 0,77 (unità 27, «(Insisti sulla questione.)»), massimo 1,46 (unità 71, «You turn the <origin> over
   to them…»).

## 4. Numeri osservati

```
unita' 75/75 · MISSION_TEXT 50 · UI_LABEL 22 (identiche) · CONVERSATION 1 · DESCRIPTION 1 · DIALOG 1 · VALUE 0
contesti 4 (1/1/6/67) · testi distinti 74 · tutte PENDING
tab 45 unita · virgolette 31 (unita 21 con 3) · token 19 in 5 famiglie · quadre 0
parole EN 2087 -> IT 2067 (0.990) · rapporto 0.77 - 1.46, media 1.06
righe 417/686 · file 164/240 (68,3%) · 89 prima / 76 dopo · confine riga 695
FAIL totale: 0 (30 controlli) · verify exit 0 (30 controlli)
sha256[:16] 53f6d41b0bfedb6c
```

## 5. Stato del progetto

```
TOTALE staging: 27151 unità · 858563 EN · 815888 IT
boarding missions.txt: 164/240 (68,3%) · 2 lotti · 2939 EN -> 2886 IT
file completi: quarantasei · residuo traducibile (formula state.py): 4801
residuo misurato: 5441 unità / 118524 parole su 120 file
avanzamento: 27151/32924 unità (82,5%) · 858563/979975 parole (87,6%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (30 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 75 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: resta **l'ultimo segmento** (76 unità, righe 695–959).
- **Prossimo lotto**: `HANDOFF_L131_20261019.md` — righe **695–959**, che **chiude il file**: **76 unità**, **1.632
  parole**, **2 contesti**, **74 unità con tab**, **2 virgolette**, **22 token in 2 famiglie**, **52 testi distinti**.
