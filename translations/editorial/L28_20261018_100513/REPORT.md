# L28 — rapporto di chiusura

| Voce | Valore |
|---|---|
| Lotto | **L28** |
| File | `data/kahet/kahet missions.txt` |
| Righe | 3051–5297 (fine file) |
| Unità | **821 / 821** |
| Parole EN | 30.796 |
| Parole IT | 27.914 |
| Rapporto IT/EN | **0,906** |
| Contesti | 47 |
| Parti | 10 |
| `check.py` | **`FAIL totale: 0`** |
| `verify.py` | **24 controlli, `FAIL: 0`, exit 0** |
| `state.py` | **`ESITO: OK`** |
| `translation.json` sha256[:16] | `ba932b11d8e35fb8` |
| Stato | **CHIUSO** il 2026-10-18 |
| Approvazione nel DB | **nessuna** (821 unità `PENDING`) |

---

## 1. Che cosa contiene il lotto

La coda delle missioni Ka'het, dal ritorno a Patir fino all'arco dei Tern e delle sonde atmosferiche:

- **Patir Mystery 20–24**: la scialuppa Petrel, il gigante gassoso Pacili, la simulazione di emergenza,
  il trasporto del laboratorio, il primo contatto fallito con la sonda dei Costruttori.
- **Patir Mystery 25–28**: l'esplorazione di Chanai con i campioni, la teoria della replica, la flotta
  cisterna degli Swan, il test del Peregrine.
- **Patir Mystery 29–33**: il compito Korath, l'analisi di Ssil Vida, l'equipaggiamento umano come chiave,
  il primo contatto con il planetoide di Lathia e i suoi esiti, comprese le ramificazioni di morte.
- **Patir Mystery 34–38**: il ritorno con le tute danneggiate, la creatura che cerca di avviare la nave,
  la partenza di Dusk, le missioni "Safety Net" e le spedizioni a resistenza media e lunga.
- **Voice From The Past 0–6**: il satellite "zombi", il segnale dei Costruttori, Gavriil, l'avamposto
  su Kumkapi, la luna Alix e la quarantena.
- **Cloud Probe 1–5**: i quattro Tern nei giganti gassosi del Cimitero, la scorta allo Swan.
- **Lightning in a Bottle 1–5 + epilogo**: le tempeste ioniche, le mongolfiere dei Costruttori, la
  cattura con i Peregrine, il regalo finale.

---

## 2. Come è stato verificato

**IMPLEMENTATO** — 10 parti su disco, `check.py` con `FAIL totale: 0`.

**ESEGUITO** — i controlli sono stati lanciati davvero:

```
check.py     821/821 unita · tab 651/651 · virgolette 1199/1199 · token 159/159 · FAIL totale: 0
verify.py    24 controlli · FAIL: 0 · exit=0
state.py     ESITO: OK · repo endless-sky b4aa3bac3 (modifiche: nessuna)
```

**VERIFICATO** — `verify.py` rilegge il file sorgente riga per riga, confronta ogni unità con `state.db`,
ricostruisce `translation.json` dalle parti e **asserisce la copertura totale 1.738/1.738** con due
lotti e zero sovrapposizioni. Esce con **0** solo se tutti i 24 controlli passano.

---

## 3. Chiusura del file

| Lotto | Righe | Unità |
|---|---|---|
| L27 | 39–3048 | 917 |
| L28 | 3051–5297 | 821 |
| **totale** | **39–5297** | **1.738 / 1.738** |

`kahet missions.txt` è l'**ottavo file completo** dello staging, insieme a `map planets.txt`,
`human missions.txt`, `intro missions.txt`, `jobs.txt`, `deep missions.txt`,
`remnant 1 introduction.txt` e `coalition missions.txt`.

---

## 4. Numeri strutturali

| Elemento | Lotto | Sorgente |
|---|---|---|
| tab | 651 | 651 |
| virgolette | 1.199 | 1.199 |
| backtick | 0 | 0 |
| token `<…>` | 159 | 159 |
| unità con virgolette dispari | 51 | 51 (riprodotte) |
| gruppi di duplicati inglesi | 29 (67 unità) | — |
| `UI_LABEL` in `NT` | 4 | 4 |
| `CONVERSATION` | 0 | 0 |

---

## 5. Correzioni reali fatte durante il lotto

| Unità | Problema | Correzione |
|---|---|---|
| 546 | rapporto 0,44 (`E tu?`) | `E tu, invece?` |
| 456 | passato remoto fuori registro | `Sparo tre colpi` |
| 484 | refuso di stesura (`quandunque`) | `quando che sia` |
| 176 | inglese residuo (`promised`) | `aveva promesso` |
| 177 | refuso (`semiciilindrica`) | `semicilindrica` |
| 198, 800, 804, 818 | `UI_LABEL` | restano identiche (in `NT`) |

Nessun controllo è stato allentato.

---

## 6. Che cosa non è stato verificato

- **Nessuna approvazione**: 821 unità `PENDING` in `state.db`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky.
- **Nessun test di gameplay** sui 47 contesti.

---

## 7. Effetto sullo staging

| Voce | Prima di L28 | Dopo L28 |
|---|---|---|
| Unità in staging | 11.926 | **12.747** |
| Parole EN | 377.011 | **407.807** |
| Parole IT | 358.715 | **386.629** |
| Directory con `translation.json` | 31 | **32** |
| Residuo traducibile | 20.004 | **19.183** |
| File completi | 7 | **8** (`kahet missions.txt` a 1.738/1.738) |
| `kahet missions.txt` | 917 / 1.738 (52,8%) | **1.738 / 1.738 (100%)** |

DB invariato: **APPROVED 364 · PENDING 32.560**, 32.924 unità, ultimo evento `2026-10-17T14:33:18Z`.

---

## 8. Prossimo passo

**L29** = `data/hai/hai missions.txt`, righe **23–2696**: **823 unità**, 23.926 parole, 54 contesti,
da `First Contact: Hai` a `Acorn Delights: Part 5`, **fine file**. È il prossimo file completo
candidato: 823 unità in un solo lotto, con la copertura totale asseribile nel `verify.py`.

Ripresa: unità **1**, riga **23**, contesto `mission:First Contact: Hai`.
