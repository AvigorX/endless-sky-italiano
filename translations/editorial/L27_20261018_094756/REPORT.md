# L27 — rapporto di chiusura

| Voce | Valore |
|---|---|
| Lotto | **L27** |
| File | `data/kahet/kahet missions.txt` |
| Righe | 39–3048 |
| Unità | **917 / 917** |
| Parole EN | 35.520 |
| Parole IT | 32.640 |
| Rapporto IT/EN | **0,919** |
| Contesti | 49 |
| Parti | 11 |
| `check.py` | **`FAIL totale: 0`** |
| `verify.py` | **25 controlli, `FAIL: 0`, exit 0** |
| `state.py` | **`ESITO: OK`** |
| `translation.json` sha256[:16] | `37e09b22e11caf89` |
| Stato | **CHIUSO** il 2026-10-18 |
| Approvazione nel DB | **nessuna** (917 unità `PENDING`) |

---

## 1. Che cosa contiene il lotto

Il primo segmento di `kahet missions.txt`: la linea narrativa che parte dall'abbordaggio di un Ka'het
e arriva alla scoperta di Patir, al primo contatto con i Fetri'sei, alla cacciata della squadra in
un'altra galassia e al ritorno. In ordine:

- **Disabled Ka'het / Strange Ka'het**: la lumaca morta, l'esoscheletro, il saccheggio dei macchinari
  con il Laboratorio di Ricerca.
- **Ka'het research 1–2**: Plume, il tecnico Remnant, i soldi per il Fucile del Vuoto.
- **Patir Mystery 1–3**: l'apparizione del sistema, Taely, la sonda di ricognizione, il primo
  insediamento dei Costruttori, l'iridio.
- **Patir Mystery 4–7**: il primo contatto, Dusk, la camera di equilibrio, il Fetri'sei nella cupola,
  il ritorno in salvo (o la sua distruzione).
- **Patir Mystery 8–12**: il laboratorio mobile, il satellite, l'incidente che porta la squadra fuori
  dalla Via Lattea, Lathia, la stazione di Chanai, l'abbordaggio del Fetri'sei.
- **Patir Mystery 13–19**: il ritorno, Chilia, l'arma a segnale, il Ka'sei solitario, gli
  equipaggiamenti alieni.

---

## 2. Come è stato verificato

Tre livelli, tenuti distinti.

**IMPLEMENTATO** — 11 parti su disco, `check.py` con `FAIL totale: 0` sul lotto completo.

**ESEGUITO** — i controlli sono stati lanciati davvero, e l'output è stato letto:

```
check.py     917/917 unita · tab 718/718 · virgolette 1210/1210 · token 170/170 · FAIL totale: 0
verify.py    25 controlli · FAIL: 0 · exit=0
state.py     ESITO: OK · repo endless-sky b4aa3bac3 (modifiche: nessuna)
```

**VERIFICATO** — `verify.py` non riusa la logica di `check.py`: rilegge il file sorgente riga per riga,
confronta ogni unità con `state.db`, ricostruisce `translation.json` dalle parti su disco e verifica i
totali di tab, virgolette, backtick e token. Esce con **0** solo se tutti i 25 controlli passano.

---

## 3. Perché `verify.py` non asserisce la copertura del file

L27 **non chiude** `kahet missions.txt`: dopo la riga 3048 restano 821 unità (righe 3051–5297). Il
controllo cablato `tot_staging == tot` sarebbe stato corretto oggi e **falso** al primo lotto
successivo sullo stesso file — esattamente la regressione che ha reso rosso L25 dopo l'apertura di
L26. L'invariante usato è quindi:

- il lotto sta dentro il file (`first > 0`, `last <= maxline`);
- nessun `id` condiviso con altri lotti dello stesso file;
- la copertura è **stampata** (917 / 1.738), non asserita.

---

## 4. Numeri strutturali

| Elemento | Lotto | Sorgente |
|---|---|---|
| tab | 718 | 718 |
| virgolette | 1.210 | 1.210 |
| backtick | 0 | 0 |
| token `<…>` | 170 | 170 |
| unità con virgolette dispari | 70 | 70 (riprodotte) |
| gruppi di duplicati inglesi | 34 (81 unità) | — |
| `UI_LABEL` in `NT` | 20 | 20 |
| `CONVERSATION` tradotte | 30 | 30 |

---

## 5. Correzioni reali fatte durante il lotto

Nessun controllo è stato allentato. Le uniche modifiche sono state al testo italiano o al tab mancante:

| Unità | Problema | Correzione |
|---|---|---|
| 509 | rapporto 2,00 (`Schieramento del laboratorio`) | `Schierare il laboratorio` |
| 528 | rapporto 0,47 (`E poi?`) | `Che cosa viene dopo?` |
| 722 | rapporto 0,47 (`E io?`) | `E che cosa faccio io?` |
| 913 | rapporto 0,44 (`E tu?`) | `E tu che mi racconti?` |
| 807 | duplicato italiano con unità 157 | `Ho capito.` |
| 347 | tab aggiunto in eccesso | tab rimosso (`tab per unita` 0/1) |
| 633, 776, 797, 823, 860, 861, 866 | virgolette sorgente non bilanciate | riprodotte esattamente |

---

## 6. Che cosa non è stato verificato

- **Nessuna approvazione**: le 917 unità restano `PENDING` in `state.db`. Lo staging non approva.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky e non è mai
  stata vista a schermo. Il controllo è strutturale, non visivo.
- **Nessun test di gameplay** sui 49 contesti: la coerenza del registro è stata tenuta per lettura del
  sorgente.

---

## 7. Effetto sullo staging

| Voce | Prima di L27 | Dopo L27 |
|---|---|---|
| Unità in staging | 11.009 | **11.926** |
| Parole EN | 341.491 | **377.011** |
| Parole IT | 326.075 | **358.715** |
| Directory con `translation.json` | 30 | **31** |
| Residuo traducibile | 20.921 | **20.004** |
| File completi | 7 | **7** (nessuno nuovo: L27 non chiude il file) |

DB invariato: **APPROVED 364 · PENDING 32.560**, 32.924 unità, ultimo evento `2026-10-17T14:33:18Z`.

---

## 8. Prossimo passo

**L28** = `data/kahet/kahet missions.txt`, righe **3051–5297**: **821 unità**, 30.796 parole, apre
`Ka'het: Patir Mystery 20`. Con L28 il file arriverebbe a **1.738/1.738** e diventerebbe l'ottavo file
completo; a quel punto il `verify.py` di L28 **può** asserire la copertura totale, perché sarebbe
l'ultimo segmento.

Ripresa: unità **918**, riga **3051**, contesto `mission:Ka'het: Patir Mystery 20`.
