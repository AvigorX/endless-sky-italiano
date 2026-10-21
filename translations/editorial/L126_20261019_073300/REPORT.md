# REPORT — L126 · `incipias first contact.txt` (il Guardiano, i Quarg, il relitto)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| avvertimento del Guardiano | 1–23 | 22–61 | la voce incorporea, i «fiori non nati», il quadro che si dipinge, il permesso sotto sorveglianza |
| presenza del Guardiano | 24–27 | 75–99 | i due sistemi Dom'us e Hui'uc, lo stesso rimprovero |
| primo contatto | 28–29 | 117–121 | navi sconosciute, solo fruscio, il riferimento dei Quarg |
| visita ai Quarg | 30–42 | 137–156 | i Quarg cerimoniali, le due domande, l'avvertimento sui confini dello spazio |
| il relitto | 43–55 | 181–218 | la nave aliena, i cinque polpi-medusa, le tre scelte |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `unborn flowers` | **fiori non nati** | reso una volta, ripetuto identico (8 occorrenze) |
| `traveler` | **viaggiatore** | registro alto |
| `Ignoring these words is only but folly` | **Ignorare queste parole è pura follia** | non calcato |
| `turn back` · `turn around` | **torna indietro** | |
| `the continuum` | **il continuum** | |
| `Your kind is much more advanced…` | **La tua specie è molto più avanzata…** | |
| `I do not favor unsavory confrontation` | **non amo gli scontri spiacevoli** | |
| `I am the guardian of this space` | **sono il guardiano di questo spazio** | |
| `the Incipias` | **gli Incipias** | nome di specie, invariato |
| `the Quarg` | **i Quarg** | invariato |
| `Your lengthy wanderings have brought forth you here` | **I tuoi lunghi vagabondaggi ti hanno condotto fin qui** | registro cerimoniale |
| `do not perambulate across this quarter of space` | **non peregrinare per questo quarto di spazio** | |
| `a trifling interval` | **un intervallo minimo** | |
| `hail request` · `color gradients` | **richiesta di collegamento** · **gradienti di colore** | |
| `half octopod, half jellyfish` | **in parte polpi e in parte meduse** | |
| `gunner` | **artigliere** | unità 46, 50 |
| `the crate` | **la cassa** | |
| `hyperdrive` · `repair equipment` | **iperguida** · **attrezzatura di riparazione** | |

## 3. Difficoltà

1. **Le 4 `UI_LABEL`** vanno isolate: `ut divitas`, `spec inci`, `both planets`, `new species` restano identiche,
   escluse da «tutte tradotte» e verificate in un controllo loro.
2. **Due registri da tenere distinti**: Guardiano alto e arcaico, Quarg cerimoniale. Il `check.py` verifica le forme
   caratteristiche di entrambi (`follia`, `giacciono`, `viaggiatore`; `peregrinare`, `vagabondaggi`, `autorizzato`).
3. **L'unità 23 ha 3 virgolette**: il sorgente lascia una virgoletta di chiusura in più dopo il punto; riprodotta,
   non «corretta».
4. **Due firme sovrapposte**: le due voci di diario (18 e 22) hanno lo stesso inizio, perché la seconda ripete la
   prima e aggiunge una frase. Risolte con una mappa **`EXACT`** per testo completo, dichiarata, invece di allungare
   la firma a forza.
5. **65 virgolette** in 26 unità: contate per unità, con i casi a 3 e a 4.
6. **2 token nel lotti successivi** (`<first>`, `<last>`): qui zero, ma il file ne ha sette in tutto.
7. **Gate**: minimo 0,69 (unità 37, «Cerco nuove specie.»), massimo 1,44 (unità 48, l'opzione di fuga).

## 4. Numeri osservati

```
unita' 55/55 · MISSION_TEXT 48 · UI_LABEL 4 (identiche) · LOGBOOK 3 · tutte PENDING
contesti 6 (23/13/13/2/2/2) · testi distinti 52 (3 coppie ripetute)
tab 37 unita · virgolette 65 (unita 23 con 3) · token 0 · quadre 0
parole EN 1788 -> IT 1626 (0.909) · rapporto 0.69 - 1.44, media 1.01
righe 22/218 · file 55/161 (34,2%) · 0 prima / 106 dopo · confine riga 224
FAIL totale: 0 (31 controlli) · verify exit 0 (28 controlli)
sha256[:16] c928bf1d8815cac5
```

## 5. Stato del progetto

```
TOTALE staging: 26881 unita · 852750 EN · 810346 IT
incipias first contact.txt: 55/161 (34.2%) · 1 lotto · 1788 EN -> 1626 IT
file completi: quarantacinque · residuo traducibile (formula state.py): 5049
residuo misurato: 5685 unità / 124242 parole su 121 file
avanzamento: 26881/32924 unità (81,6%) · 852750/979975 parole (87,0%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 55 unità restano `PENDING`; nessuna missione è stata caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: **106 unità** residue (righe 224–439).
- **Prossimo lotto**: `HANDOFF_L127_20261019.md` — **tutto** il contesto `Help The Stranded 1` (63 unità, 1.697
  parole, **2 token** `<first>`/`<last>`, 55 unità con tab, 98 virgolette).
