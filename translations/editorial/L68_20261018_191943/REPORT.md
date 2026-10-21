# REPORT — L68 · `data/successors/successor 2 ghosts myurej.txt`

## 1. Cosa contiene il lotto

Il primo incontro con **Casa Myurej**: due ufficiali militari prelevano il giocatore in uno spazioporto e
lo portano in un albergo dove, dietro un paravento di tessuto, una voce cerimoniosa gli affida un incarico.
Sono stati rubati i doni di nozze destinati agli eredi di Myurej e Chydiyi; il colpevole è **Riiria**, delle
«Casate del Popolo». Il lotto copre: l'arruolamento (unità 3–19), i due rami di rifiuto/richiesta di
chiarimenti (17–19), il diario (23–24), l'arrivo su **Kasii-Tuur-Saqru** (26–31), la ricognizione della
stazione (32–34, con la trasmissione di Riiria), il capitano mercante di Casa Myurej (35–46) e il congedo
(47–49). È una scena **completa**: si chiude con il giocatore che segna sulla mappa la stazione disabitata
dove cercare Riiria.

Un solo contesto (`Successors: Ghosts Myurej 1`), 49 unità su 49 righe distinte: nessuna riga produce più
di una unità, quindi la ricomposizione è uno-a-uno e non serve il tripletto dei `log` a tre unità.

## 2. Scelte editoriali

| nodo | scelta | perché |
|---|---|---|
| `thou / thee / thy / dost / shalt` | **«tu» moderno, sintassi formale** | è il precedente misurato di L45–L47 sullo stesso popolo; l'arcaismo italiano («voi», «codesto») sarebbe un registro che il progetto non usa |
| `House Myurej` | **`Casa Myurej`** | `Casa Kaatrij` 51, `Casa Sioeora` 8, `Casa Myurej` 4 in L45, contro 2 `Casata Myurej` |
| `the People's Houses` | **`Casate del Popolo`** | forma già presente in staging (L45) |
| `the Old` | **`i Vecchi`** | indica le Casate antiche; «Antichi» nel gioco è un'altra fazione |
| `Kvelqden`, `Myaede`, `Riiria`, `Riijaaora`, `Kasii-Tuur-Saqru`, `Vade-Osolaa-Kaska` | **invariati** | nomi propri: non si traducono, non si unificano |
| `data-sphere` | **`sfera di dati`** | occorrenze già in staging (Casa Kaatrij) |
| `translation device` | **`dispositivo di traduzione`** | idem, quattro occorrenze precedenti |
| `Four hundred thousand credits` | **`Quattrocentomila crediti`** | nel parlato si scrive in lettere; `400.000 crediti` resta nelle unità descrittive |
| `knav(e)` | **`farabutto`** | dispregiativo coerente nei tre punti (12, 42) |
| `golden child` | **`rampollo viziato`** | idioma reso, non letterale |
| `cant of an arm` | **`il cenno di un braccio`** | i Successori hanno più braccia: il gesto è un accenno, non un «canto» |
| `hollow stations`, `broken spires` | **`stazioni cave`, `guglie spezzate`** | immagine di relitti orbitali, non di «stazioni vuote» |
| `the quarry` | **`la preda`** | registro venatorio coerente con «striscerei là» |

La voce cerimoniosa di Myurej e quella popolare di Riiria sono tenute distinte: la prima usa periodi lunghi
e «desidera avvalersi dei tuoi servigi», la seconda grida per contrazioni («se vengono a prendere noi…»).
Il capitano mercante è sarcastico e usa lo stesso «tu» formale degli altri Successori, ma con lessico
commerciale («rotte», «carichi», «remunerativo»).

## 3. Difficoltà incontrate

1. **`log` a tre argomenti fra virgolette** (unità 23): l'estrattore protetto inventaria la **categoria**
   (`People`), non il testo. Il `check.py` ha dovuto separare `LOG_CAT` da `LOG_TEXT`, altrimenti il
   controllo «righe log di testo tradotte» falliva su una unità che **deve** restare in inglese.
2. **Forma di `log` nuova**: le regex delle forme di L67 (`tre argomenti con backtick`, `backtick`,
   `diretta`) non coprivano `log "A" "B" "C"`. Aggiunta la quarta forma; il controllo asserisce che le
   quattro forme **esauriscano** l'insieme `LOG`.
3. **`13 token` nell'handoff era sbagliato** (§4): tre famiglie su cinque compaiono in unità diverse, e il
   totale vero è 10. Il primo `check.py` scritto sui numeri dell'handoff avrebbe asserito 13 e sarebbe
   stato rosso con la traduzione giusta.
4. **Due gruppi di duplicati inglesi** (15/21 e 16/22): sono le stesse due battute di scelta ripetute nei
   due rami della conversazione. La resa italiana identica è legittima **perché l'inglese è identico**;
   il controllo dei duplicati distingue «stesso inglese» da «inglesi diversi con resa uguale».
5. **Due righe di `check.py` che mentivano su un `--range`**: i controlli «distribuzione dei tipi»,
   «VALUE/DESCRIPTION» e «token per simbolo» erano calcolati sul segmento selezionato, quindi su
   `--range 1 25` fallivano pur essendo il lotto corretto. Spostati sull'intero lotto: un controllo che
   non può fallire non è un controllo, ma un controllo che fallisce su un lotto sano è rumore.

## 4. Numeri osservati (output letto, non dedotto)

```
unita' tradotte nell'intervallo   49/49
copertura del lotto               49/49
tab IT 42 / EN 42
virgolette IT 90 / EN 90
token IT 10 / EN 10
rapporto IT/EN 0.61 - 1.50
parole EN 1502 -> IT 1447
prima/ultima riga del segmento: 16/113
duplicati inglese: 2 gruppi (4 unita)
FAIL totale: 0                     (37 controlli)
verify.py exit 0                   (46 controlli)
sha256[:16] translation.json      eaafbeb6e504c701
```

Stato del progetto dopo il lotto (misurato con `state.py`, che legge i `translation.json`):

```
TOTALE staging: 24252 unita · 774914 EN · 734368 IT
APPROVED 364 · PENDING 32560 · totale 32924
residuo traducibile: 7678 unita (PENDING 32560 - staging 24252 - label 630)
lotti con translation.json: 72
```

## 5. Stato del progetto

- **Trentaduesimo file** con almeno un lotto in staging; `successor 2 ghosts myurej.txt` è coperto
  **49/211 unità** (23,2%), con **162 unità** che restano dopo la riga 113.
- **Lo staging non è approvazione**: nessuna scrittura su `state.db`, nessun caricamento nel gioco, il
  repository originale è a `b4aa3bac3` senza modifiche.
- `state.py` → `ESITO: OK`, `INTEGRITA'` tutta `OK` dopo il lotto.

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 2 parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`/`REPORT.md`/`review.md` |
| ESEGUITO | sì | `check.py` e `verify.py` lanciati, output letto per intero |
| **VERIFICATO** | **sì** | `check.py` → `FAIL totale: 0` (37 controlli) **e** `verify.py` → `FAIL: 0`, exit **0** (46 controlli) |
