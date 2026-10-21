# REPORT — L117 · `pirate jobs.txt` (lavori di contrabbando, droga e ricercati)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| contrabbando di carico | 1–12 | 20–130 | quattro varianti di `Cargo Smuggling`, con nome, descrizione e multa |
| trasporto di droga | 13–24 | 157–267 | quattro varianti di `Drug Running`, una con multa esplicita di 46.000 crediti |
| grosse partite | 25–42 | 294–475 | `Bulk Cargo Smuggling` e `Bulk Drug Running` (tre varianti ciascuno) |
| contrabbando stealth | 43–60 | 502–868 | `Stealth Cargo Smuggling` Nord, Centro, Sud (sei varianti, una chiede di atterrare lontano dallo spazioporto) |
| droga stealth | 61–78 | 949–1315 | `Stealth Drug Running` Nord, Centro, Sud (sei varianti) |
| ricercato singolo | 79–82 | 1396–1427 | `Wanted Passenger`: descrizione, fallimento (l'urlo), dialogo di consegna |
| ricercati multipli | 83–94 | 1430–1529 | tre varianti di `Wanted Passengers`, con tre fallimenti diversi (crediti nel portello, scontro a fuoco, ubriachi) |
| criminale galattico | 95–98 | 1534–1624 | `Highly Wanted Passenger (North)`: descrizione, irruzione, dialogo |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `smuggle` · `smuggling` | **contrabbando / portare di contrabbando** | |
| `run <cargo>` | **porta `<cargo>`** | è un trasporto, non una corsa |
| `planetary law enforcement` · `local law enforcement` | **forze dell'ordine planetarie / locali** | |
| `Payment is <payment>` | **Il compenso è `<payment>`** | formula ripetuta 31 volte |
| `fine` · `fined … credits` | **multa** · **multa di 46.000 crediti** | |
| `confiscated` | **confiscato** | |
| `highly illegal` | **altamente illegale** | |
| `wanted individual(s)` | **ricercato / ricercati** | nomi di missione lasciati in inglese |
| `galactic criminal` | **criminale galattico** | |
| `spaceport edge` · `outside of the main city` | **margini dello spazioporto** · **fuori dalla città principale** | |
| `airlock` · `cuffs` | **portello d'ancoraggio** · **manette** | |
| `tear gas` · `laser marks` | **gas lacrimogeno** · **segni di laser** | |
| `passed out in their bunks rooms` | **svenuti nelle loro cuccette** | `bunks` = cuccette |
| `no-questions-asked transporter` | **trasportatore affidabile che non fa domande** | |
| `battle trophies` | **trofei di battaglia** | |
| `payment is high at an amazing <payment>` | **il compenso è alto, ben `<payment>`** | |
| nomi di missione (`VALUE`) | **identici all'inglese** | decisione 259/L103 |

## 3. Difficoltà

1. **Tassonomia nuova**: quattro `kind` in un blocco (`VALUE`, `DESCRIPTION`, `MISSION_TEXT`, `DIALOG`), con i
   `VALUE` da lasciare identici e i `DIALOG` da tradurre come prosa. Il `check.py` di L116 (133 `TUTORIAL_TIP`)
   qui era rosso per costruzione.
2. **26 testi per 98 unità**: la ripetizione è del sorgente. Le rese si scrivono **una volta** e si assegnano
   per firma; il controllo verifica che ogni gruppo di inglese identico abbia **una sola** resa italiana.
3. **Errore corretto**: la prima stesura traduceva anche i nomi di missione e il `check.py` ha bocciato il lotto
   («i 31 `VALUE` sono identici al sorgente»). Correzione: seconda stesura (`mkparts2.py`) con i `VALUE` come
   identità e `UNIQ` ridotto ai 17 testi prosaici.
4. **108 token in sei famiglie**, con `<payment>` e `<cargo>` che convivono nella stessa descrizione: la parità è
   verificata per simbolo **e** per unità, con lo stesso ordine.
5. **Il dialogo singolare/plurale**: `Your <passengers> insists` e `Your <passengers> insist` sono due testi
   distinti che differiscono di una «s». Le firme usate per assegnarli devono essere `insists that` e
   `insist that`: con `insist` la firma combaciava con **entrambi** e il costruttore è abortito (giusto così).
6. **Una sola unità con virgolette** (81, l'urlo del criminale): due, e riprodotte.
7. **Gate**: minimo 0,91 (unità 81), massimo 1,22 (unità 2), media 1,02 — la prosa è più corta dell'inglese in
   modo uniforme.

## 4. Numeri osservati

```
unita' 98/98 · VALUE 31 · DESCRIPTION 31 · MISSION_TEXT 31 · DIALOG 5 · tutte PENDING
contesti 31 (26 da tre, 5 da quattro) · testi distinti 26 (9 nomi + 17 prosa)
tab 0 · virgolette 2 = 2 (unita 81) · token 108 = 108 in 6 famiglie · quadre 0 · backtick 0
parole EN 1804 -> IT 1715 (0.951) · rapporto 0.91 - 1.22, media 1.02
righe 20/1624 · file 279 unita · max(line) 3706 · 0 prima / 181 dopo
FAIL totale: 0 (29 controlli) · verify exit 0 (38 controlli)
sha256[:16] 6ed8bb0de3875183 · copertura file 98/279 (35,1%)
```

## 5. Stato del progetto

```
TOTALE staging: 26392 unita · 835942 EN · 793626 IT
pirate jobs.txt: 98/279 (35.1%) · 1 lotto · 1804 EN -> 1715 IT
file completi: quarantadue · residuo traducibile (formula state.py): 5538
residuo misurato: 6169 unità / 141040 parole su 124 file
avanzamento: 26392/32924 unità (80,2%) · 835942/979975 parole (85,3%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts2.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (38 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 98 unità restano `PENDING`; nessuna missione è stata caricata nel gioco.
- **Il file non è completo**: **181 unità** residue (righe 1627–3706); prossimo contratto
  `HANDOFF_L118_20261019.md` (104 unità, 1.753 parole, 33 contesti, 192 token in nove famiglie).
- **Nessuna revisione umana**.
