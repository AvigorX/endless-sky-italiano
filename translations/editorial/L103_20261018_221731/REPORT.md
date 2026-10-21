# REPORT — L103 · `quarg missions.txt` (satelliti, mondo ad anello, e quattro tipi in un lotto)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Quarg Satellites` | 124–176 | 20 | la proposta del Quarg, le domande del giocatore, il dispiegamento dei quattro satelliti e gli esiti |
| `Lagrange Ring: Cargo` | 182–224 | 18 | la richiesta di trasporto, il datapad, il carico e il pagamento |
| `Lagrange Ring: Cargo Job` | 228–249 | 4 | la variante del lavoro: descrizione, carico, pagamento |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `VALUE` | **identici all'inglese** | nomi di missione e di carico = riferimenti di dato (vedi §3.1) |
| `scanning satellites` | **satelliti di scansione** | |
| `triangular pyramids … tipped with another, smaller triangular pyramid` | **piramidi triangolari … sormontata da un'altra piramide triangolare più piccola** | la ricorsione è nel testo e si sente |
| `foolish thugs` | **stolti teppisti** | |
| `needless slaughter` | **inutile massacro** | |
| `but a courtesy` | **solo una cortesia** | |
| `deter further attacks` | **scoraggi ulteriori attacchi** | |
| `data pad` | **datapad** | grafia già usata altrove |
| `cargo space` · `proper defenses` | **spazio di carico** · **difese adeguate** | |
| `under strict supervision` | **sotto stretta sorveglianza** | |
| `meticulous` | **meticoloso** | |
| `former slave-colony planet` · `Poisonwood` | **pianeta che fu colonia di schiavi** · **Poisonwood** invariato | nome proprio |
| `demanding tribute` | **chiedono un tributo** | |
| `ringworld` | **mondo ad anello** | coerente con L102 |
| `internal style and decoration` | **stile e arredamento interno** | |

## 3. Difficoltà

1. **I `VALUE` e la regola**: sono tre unità che **sembrano** testo e non lo sono. La prima stesura del `check.py`
   li avrebbe inclusi nel controllo «tutte tradotte» e il lotto sarebbe diventato rosso su una scelta corretta.
   Il controllo è scritto come **uguaglianza per indice** (`italian == english` per 1, 21, 39) e in più verifica
   che **nessun'altra** unità sia identica: così un `VALUE` tradotto per sbaglio e una battuta non tradotta
   emergono entrambi.
2. **Cinque citazioni aperte** non ci sono, ma **una sì**: l'unità 30 chiude la battuta nell'unità 31. Il
   controllo asserisce `odd == [30]` e che l'unità **finisca senza virgoletta**.
3. **Diciannove token in sei famiglie**: `<cargo>`, `<payment>`, `<stopovers>`, `<destination>`, `<waypoints>`,
   `<system>`. Due di queste (`<waypoints>`, `<system>`) compaiono **una volta sola**: il controllo le verifica
   **per famiglia**, non solo nel totale — un `<system>` perso in mezzo a cinque `<cargo>` non si sarebbe visto.
4. **I `DESCRIPTION` sono quasi identici fra i due lavori** (22 e 40): resi dalla stessa costante, così non
   possono divergere. Lo stesso per i `DIALOG` 36/41.
5. **Le due domande ripetute** (8/12 e 10/13) sono rami diversi dello stesso dialogo: la resa è identica per
   costruzione, non per disciplina.

## 4. Numeri osservati

```
unita' 42/42 · 28 MISSION_TEXT + 8 DIALOG + 3 DESCRIPTION + 3 VALUE (identici)
tab 25 · virgolette 43 = 43 (una aperta, unita 30) · token 19 = 19 in sei famiglie · quadre 0
parole EN 956 -> IT 882 · rapporto 0.69 - 1.22
righe 124/249 · file 178 unita · max(line) 506 · 48 prima / 88 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (28 controlli)
sha256[:16] 2e3f270bdda5ce6a · copertura file 90/178 (50,6%)
```

## 5. Stato del progetto

```
TOTALE staging: 25381 unita · 814000 EN · 771643 IT
quarg missions.txt: 90/178 (50,6%) · 2 lotti
file completi: 39 · residuo traducibile (formula state.py): 6549
residuo misurato: 7124 unità / 162047 parole su 127 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 42 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: 88 unità su 2 contesti (`Ask Quarg About Coalition Early`, `Quarg Pug Arfecta
  Warning`); prossimo contratto `HANDOFF_L104_20261018.md` (righe 250–334).
- **La decisione sui nomi di missione e carico resta aperta**: è di campagna, richiede un inventario globale.
- **Nessuna revisione umana**.
