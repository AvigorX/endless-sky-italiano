# REPORT — L147 · `coalition jobs.txt` (lavori dell'Anello: operai, volontari, materiali, forniture, un candidato)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| operai | 1–7 | 16–64 | il `TEXT` di consegna e tre livelli di `Workers to the <planet>` |
| volontari | 8–14 | 84–132 | il `TEXT` con l'agente Heliarch, tre livelli di volontari |
| materiali | 15–21 | 152–202 | la consegna dei materiali, tre livelli con `<tons>` e `<date>` |
| forniture | 22–28 | 223–271 | la donazione di `<commodity>`, tre livelli con `<origin>` |
| il candidato | 29–30 | 292–293 | `Candidate to the <planet>` e la sua descrizione |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Workers to the <planet>` | **identico** | `VALUE`, nome di lavoro in UI |
| `this crew of <bunks> workers` | **questo equipaggio di `<bunks>` operai** | |
| `the Heliarch <planet>` | **il `<planet>` degli Heliarch** | il token passa **prima** del nome di fazione |
| `maintain and expand the ringworld` | **mantenere ed espandere il mondo ad anello** | 77 occorrenze in staging |
| `in return for room and board` | **in cambio di vitto e alloggio** | |
| `by <date>` | **entro il `<date>`** | |
| `a donation from the government of <origin>` | **una donazione del governo di `<origin>`** | |
| `candidate for elevation to the rank of Heliarch` | **candidato all'elevazione al rango di Heliarch** | |
| `receive a transfer of <payment>` | **ricevi un bonifico di `<payment>`** | |
| `receive <payment> in payment` | **ricevi `<payment>` come compenso** | |

## 3. Difficoltà

1. **65 token su 7 simboli**: il conteggio globale non basta, perché `<payment>` e `<date>` sono corti e vivono in frasi
   quasi identiche. Tre controlli: multiset, ordine per unità, due conteggi nominati.
2. **I `VALUE` contengono un token**: `<planet>` fa parte del nome del lavoro. Copiarlo senza il segnaposto produrrebbe
   un lavoro diverso, quindi si verifica l'uguaglianza **con** il token.
3. **Ripetizioni triple**: quattro gruppi, una resa per gruppo, confronto per uguaglianza — non tre traduzioni parallele.
4. **`<destination>` non c'è in questa finestra**: arriva con gli interpreti (L148). Qui i simboli sono sette, e il
   `check.py` rifiuta qualunque altro.
5. **Zero tab e zero virgolette**: il primo lotto del progetto, dopo L140–L146, senza nessuno dei due. Due asserzioni
   vuote scritte, non omesse.
6. **Gate**: minimo **0,86**, massimo **1,16**, media **1,01** — testo tecnico e ripetitivo.

## 4. Numeri osservati

```
unita' 30/30 · VALUE 13 · DESCRIPTION 13 · TEXT 4 · LOGBOOK 0 · DIALOG 0 · UI_LABEL 0 · tutte PENDING
token 65 su 7 simboli: <planet> 28, <payment> 17, <bunks> 6, <tons> 6, <date> 4, <origin> 3, <commodity> 1
parita per simbolo E per unita (ordine dei simboli identico in tutte le 30)
13 VALUE identici · 4 gruppi tripli a resa unica · 14 testi distinti · 17 contesti
tab 0 · virgolette 0 · parole EN 437 -> IT 412 (0.943) · rapporto 0.86 - 1.16, media 1.01
righe 16/293 · 0 prima / 167 dopo · confine riga 309 (Heliarch Candidate)
FAIL totale: 0 (28 controlli) · verify exit 0 (27 controlli)
sha256[:16] 86d0e8e3b5fccb2f
```

## 5. Stato del progetto

```
TOTALE staging: 27676 unità · 873343 EN · 829649 IT
coalition jobs.txt: 30/197 (15,2%) · 1 lotto
file completi: cinquanta · residuo traducibile (formula state.py): 4254
residuo misurato: 4923 unità / 103756 parole su 116 file
avanzamento: 27676/32924 unità (84,1%) · 873343/979975 parole (89,1%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (27 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 30 unità `PENDING`, nessun lavoro accettato nel gioco.
- **Nessuna partita avviata**: i tre livelli di ogni modello non sono stati giocati.
- **Nessuna revisione umana**.
- **`coalition jobs.txt` è al 15,2%**: restano **167 unità**.
- **Un controllo fittizio è stato rimosso** durante il lotto: avevo scritto un `ck(..., True)` che non verificava
  nulla. Sostituito da nessun controllo, perché i due spazi finali sono già coperti dal confronto 30/30. Meglio un
  controllo in meno che uno che passa sempre.
- **Prossimo lotto**: `HANDOFF_L148_20261019.md` — righe **309–435**, **16 unità**, 205 parole, **1 `DIALOG`**,
  **3 `TEXT`**, **6 `VALUE`**, **6 `DESCRIPTION`**, **31 token** su **4 simboli** (`<payment>` 10, `<planet>` 9,
  `<bunks>` 6, `<destination>` 6).
