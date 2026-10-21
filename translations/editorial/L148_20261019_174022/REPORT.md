# REPORT — L148 · `coalition jobs.txt` (il candidato, gli interpreti, i peacekeeper, i coloni Saryd)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| la cerimonia | 1 | 309 | **`DIALOG`**: gli agenti ricevono il candidato, il bonifico |
| interpreti | 2–8 | 314–362 | il `TEXT` di consegna e tre livelli di `Interpreters to <planet>` |
| peacekeeper | 9–13 | 382–409 | il `TEXT` e due livelli, con l'indagine sull'attività dei Lunarium |
| coloni Saryd | 14–16 | 429–435 | il `TEXT` dei coloni e il primo livello `Saryds to <planet>` |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Interpreters to <planet>` | **identico** | `VALUE`, **senza «the»** |
| `Heliarch agents, trained as interpreters and mediators` | **agenti Heliarch, addestrati come interpreti e mediatori** | |
| `to <destination>` | **a `<destination>`** | destinazione di missione, non `<planet>` |
| `to investigate reports of Lunarium activity` | **per indagare su segnalazioni di attività dei Lunarium** | |
| `this corps of <bunks> peacekeepers` | **questo corpo di `<bunks>` peacekeeper** | prestito, coerente col `VALUE` |
| `As part of the Interspecies Exchange Program` | **Nell'ambito del Programma di Scambio tra Specie** | |
| `transport fee` | **tariffa di trasporto** | |
| `in a small ceremony` | **con una piccola cerimonia** | |

## 3. Difficoltà

1. **`<destination>` contro `<planet>`**: due segnaposto diversi, sei e nove occorrenze, nella stessa area della frase.
   Tre controlli: multiset, ordine per unità, e due asserzioni di **assenza** incrociata (unità 4 senza `<planet>`,
   unità 2 senza `<destination>`).
2. **`VALUE` senza «the»** rispetto a L147: la differenza è nel sorgente e si dichiara, non si normalizza; un controllo
   vieta `the <planet>`.
3. **Il primo `DIALOG`**: tipo diverso, tono diverso; il `Counter` lo isola.
4. **Ripetizioni parziali**: 3 interpreti uguali, 2 peacekeeper uguali, ma i Saryd una volta sola — la resa unica vale
   per i primi due gruppi, e il `verify.py` confronta per uguaglianza.
5. **Zero tab e zero virgolette** per il secondo lotto consecutivo: asserzioni vuote scritte.
6. **Gate**: minimo **0,85**, massimo **1,12**, media **1,01**.

## 4. Numeri osservati

```
unita' 16/16 · DIALOG 1 · TEXT 3 · VALUE 6 · DESCRIPTION 6 · LOGBOOK 0 · UI_LABEL 0 · tutte PENDING
token 31 su 4 simboli: <payment> 10, <planet> 9, <bunks> 6, <destination> 6
parita per simbolo E ordine per unita · <destination> distinto da <planet> (asserzioni incrociate)
6 VALUE identici, senza «the» · 10 testi distinti · 10 contesti
tab 0 · virgolette 0 · parole EN 205 -> IT 207 (1.010) · rapporto 0.85 - 1.12, media 1.01
righe 309/435 · 30 prima / 151 dopo · confine riga 455 (Saryd Interspecies 2)
FAIL totale: 0 (27 controlli) · verify exit 0 (25 controlli)
sha256[:16] 6f4f67af7faeeb38
```

## 5. Stato del progetto

```
TOTALE staging: 27692 unità · 873548 EN · 829856 IT
coalition jobs.txt: 46/197 (23,4%) · 2 lotti
file completi: cinquanta · residuo traducibile (formula state.py): 4238
residuo misurato: 4907 unità / 103551 parole su 116 file
avanzamento: 27692/32924 unità (84,1%) · 873548/979975 parole (89,1%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27 controlli), `verify.py` exit **0** (25 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`, nessuna missione accettata nel gioco.
- **Nessuna partita avviata**: la cerimonia del candidato non è stata vista.
- **Nessuna revisione umana**.
- **`coalition jobs.txt` è al 23,4%**: restano **151 unità**.
- **Prossimo lotto**: `HANDOFF_L149_20261019.md` — righe **455–634**, **18 unità**, 246 parole, **8 `VALUE`**,
  **8 `DESCRIPTION`**, **2 `TEXT`**, **10 contesti**, **36 token** su **4 simboli**.
