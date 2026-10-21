# REPORT — L106 · `korath missions.txt` (primo contatto, scheda dei Korath, provviste per Setar Fort)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `First Contact: Korati Efreti` | 21 | 1 | il saluto a mani aperte su una **stazione** |
| `First Contact: Laki Nemparu` | 31 | 1 | lo stesso saluto, in uno **spazioporto** |
| `First Contact: Karek Fornati` | 41 | 1 | idem |
| `First Contact: Setar Fort` | 51 | 1 | idem |
| `Discovered Korath Space` | 62 | 1 (`LOGBOOK`) | la scheda dei Korath e delle loro fazioni |
| `Setar Fort Heating` | 70–119 | 20 | il Wanderer, la missione di trasporto, il pagamento basso, il carico |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Humani efreti, naskoor amasavarkta` | **invariato** | lingua Korath: non si traduce, è il parlato non capito |
| `Kor Efreti` · `Kor Mereti` · `Kor Sestor` | **invariati** | nomi di fazioni |
| `reptilian, bipedal aliens` | **alieni rettiliani e bipedi** | |
| `scarred by … a vicious civil war` | **segnati da … una feroce guerra civile** | |
| `automated war drones` | **droni da guerra automatici** | |
| `locked in an unending struggle` | **bloccati in una lotta senza fine** | |
| `Supplies to <planet>` | **identico** | nome di missione (`VALUE`), con un token dentro |
| `[relieved, happy]` | **[sollevato, felice]** | due alternative, come il dispositivo |
| `[believe, assume]` | **[credo, suppongo]** | |
| `[supplies, aid]` | **[provviste, aiuti]** | |
| `[research, information]` | **[ricerche, informazioni]** | |
| `[descent, transition]` | **[discesa, transizione]** | ripetuta due volte nella stessa unità, resa identica |
| `[pride, honor]` | **[orgoglio, onore]** | |
| `[insulation, shelter]` | **[isolamento, ripari]** | |
| `[unfortunately, sadly]` | **[purtroppo, tristemente]** | |
| `[errors, complications]` | **[errori, complicazioni]** | |
| `[purchase, acquire]` | **[comprare, acquisire]** | |
| `[reasonable, justifiable]` | **[ragionevole, giustificabile]** | |
| `[collection, menagerie]` | **[collezione, accozzaglia]** | *menagerie* è spregiativo: reso |
| `[perish? expire?]` | **[perire? spegnersi?]** | i punti interrogativi sono **dentro** le quadre |
| `[immediately, quickly]` | **[subito, in fretta]** | |
| `terraforming assistance` | **aiuto nella terraformazione** | |
| `greenhouse building material` | **materiale per costruire serre** | |
| `the one and only` | **L'unico e solo** | |

## 3. Difficoltà

1. **Sedici coppie di quadre in cinque unità**: la convenzione dei Wanderer. Il controllo è **per unità**
   (3, 7, 1, 4, 1) e, per ogni coppia, verifica che contenga **due alternative** — una coppia con una parola sola
   sarebbe un errore che nessun totale rivelerebbe.
2. **`[perish? expire?]`**: le quadre contengono **punti interrogativi**, non virgole. Il test «virgola o punto
   interrogativo» accetta entrambi i casi senza allentare il controllo.
3. **Una citazione aperta** nell'unità 16, che è anche quella con **sette** coppie di quadre: due conteggi
   indipendenti sullo stesso testo, tenuti separati.
4. **Il `VALUE` contiene un token** (`Supplies to <planet>`): resta identico, e il token va contato **dentro** il
   `VALUE` come in qualunque altra unità. Un controllo che escludesse i `VALUE` dal conteggio dei token
   perderebbe una delle quattro occorrenze di `<planet>`.
5. **Quattro `First Contact` quasi identici**: 2/3/4 sono identici, l'1 no («stazione» contro «spazioporto»). Il
   `check.py` verifica **entrambe le cose**: che 2/3/4 siano identiche e che 1 differisca.
6. **`LOGBOOK` tradotto e `VALUE` identico nello stesso lotto**: due tipi «non `MISSION_TEXT`» con regole opposte.

## 4. Numeri osservati

```
unita' 25/25 · 22 MISSION_TEXT + 1 LOGBOOK + 1 VALUE + 1 DESCRIPTION · tab 17 · virgolette 45 = 45
token 13 = 13 in sei famiglie · quadre 16 coppie (3, 7, 1, 4, 1) · due ripetizioni (2/3/4, 15/19)
parole EN 854 -> IT 833 · rapporto 0.80 - 1.27
righe 21/119 · file 158 unita · max(line) 580 · 0 prima / 133 dopo
FAIL totale: 0 (31 controlli) · verify exit 0 (29 controlli)
sha256[:16] 10952e0d80f509b5 · copertura file 25/158 (15,8%)
```

## 5. Stato del progetto

```
TOTALE staging: 25494 unita · 817640 EN · 775146 IT
korath missions.txt: 25/158 (15,8%) · 1 lotto
file completi: 40 · residuo traducibile (formula state.py): 6436
residuo misurato: 7015 unità / 158415 parole su 126 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 25 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: 133 unità su 13 contesti; prossimo contratto `HANDOFF_L107_20261018.md` (righe
  121–212), che chiude `Setar Fort Heating` e copre `Korath Family to Ringworld` e `Korath Livestock`.
- **Nessuna revisione umana**.
