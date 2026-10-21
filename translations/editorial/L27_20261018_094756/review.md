# L27 — revisione di chiusura

**Ambito:** `data/kahet/kahet missions.txt`, righe **39–3048**, **917 unità**, **35.520 parole**, **49 contesti**.
**Esito:** `check.py` completo **`FAIL totale: 0`**, `verify.py` **25 controlli, exit 0**, `FAIL: 0`.
**Data di chiusura:** 2026-10-18.

---

## 1. Collocazione nel file

| Voce | Valore misurato |
|---|---|
| File | `data/kahet/kahet missions.txt` |
| Unità nel file | 1.738 |
| Unità nel lotto | 917 (righe 39–3048) |
| Unità prima del lotto | 0 |
| Unità dopo il lotto | **821** (righe 3051–5297, 30.796 parole) |
| Prima unità dopo il lotto | `Ka'het: Patir Mystery 20` |
| Copertura del file | 917 / 1.738 (52,8%) — **stampata, non asserita** |

L27 **non chiude il file**: è il primo segmento di `kahet missions.txt`. Per questo `verify.py` usa
l'invariante di segmento (lotto dentro il file, nessuna sovrapposizione fra lotti, copertura stampata)
e **non** `tot_staging == tot`: la lezione di L25, dove la copertura cumulativa cablata rese rosso un
lotto corretto al primo lotto successivo.

---

## 2. Le undici parti

| parte | unità | righe | EN | IT | IT/EN | rapporto per unità |
|---|---|---|---|---|---|---|
| part01 | 1–85 | 39–295 | 2.862 | 2.750 | 0,961 | 0,79–1,30 |
| part02 | 86–170 | 296–511 | 3.071 | 2.898 | 0,944 | 0,72–1,50 |
| part03 | 171–255 | 513–958 | 2.735 | 2.533 | 0,926 | 0,76–1,56 |
| part04 | 256–340 | 960–1167 | 3.035 | 2.720 | 0,896 | 0,70–1,27 |
| part05 | 341–425 | 1169–1427 | 3.680 | 3.335 | 0,906 | 0,71–1,71 |
| part06 | 426–510 | 1428–1624 | 3.931 | 3.602 | 0,916 | 0,77–1,75 |
| part07 | 511–595 | 1629–1950 | 3.084 | 2.790 | 0,905 | 0,69–1,26 |
| part08 | 596–680 | 1953–2136 | 3.654 | 3.326 | 0,910 | 0,69–1,21 |
| part09 | 681–765 | 2138–2534 | 3.206 | 2.928 | 0,913 | 0,71–1,71 |
| part10 | 766–850 | 2535–2798 | 3.648 | 3.349 | 0,918 | 0,62–1,33 |
| part11 | 851–917 | 2799–3048 | 2.614 | 2.409 | 0,921 | 0,66–1,46 |
| **totale** | **1–917** | **39–3048** | **35.520** | **32.640** | **0,919** | **0,62–1,75** |

Nessuna parte è stata chiusa con un controllo allentato: due volte è stato riscritto il testo italiano
(unità 509 e 913) perché il rapporto usciva fuori dai limiti, e in nessun caso è stato toccato il
controllo.

---

## 3. Conteggi strutturali (tutti verificati per unità)

| Elemento | IT | EN |
|---|---|---|
| tab iniziali | 718 | 718 |
| virgolette `"` | 1.210 | 1.210 |
| backtick | 0 | 0 |
| token `<…>` | 170 | 170 |

- **70 unità con virgolette dispari** nel sorgente: riprodotte esattamente, mai normalizzate.
  Elenco completo ricavabile con `u['english'].count('"') % 2` su `translation.json`
  (prime: 27, 80, 120, 122, 155, 159, 172, 246, 262, 264, 279, 284, 297, 307, 308, 312, 313, 339, 351, 352).
- **34 gruppi di duplicati inglesi** (81 unità): le traduzioni italiane identiche sono ammesse solo
  dentro un gruppo con lo stesso inglese. Una collisione reale è stata trovata e corretta (unità 807,
  vedi §5).
- **Nessun pronome-token** (`<they>`, `<their>`, …): `TOKEN_EXC` è vuoto e non è stato necessario.

---

## 4. Famiglie lessicali di questo lotto

I Ka'het non sono Coalizione: la voce rovesciata di L25/L26 **non** è stata applicata, e i Remnant
parlano in italiano normale con il loro registro tecnico.

| EN | IT | Nota |
|---|---|---|
| Graveyard | **Cimitero** | costante in tutto il lotto |
| Ember Waste | **Distesa di Braci** | costante |
| Builders | **Costruttori** | costante |
| Remnant | **Remnant** | invariato |
| Ka'het / Ka'sei / Fetri'sei | invariati | nomi di specie, non si traducono |
| Maeri'het / Telis'het / Vareti'het | invariati | nomi di classe |
| Aberrant / boarded aberrant | invariati | sono `UI_LABEL` in `NT` |
| Fetri'seia | invariato | `VALUE` del `ship:Fetri'sei` |
| Starling | **Starling** | invariato (nome di nave) |
| Ibis | **Ibis** | invariato (nome di nave) |
| Ember Prism | **Prisma di Brace** | costellazione inventata |
| Ossipago wormhole | **cunicolo di Ossipago** | |
| Builder Settlement | **Insediamento dei Costruttori** | |
| airlock | **camera di equilibrio** | costante, anche nei composti |
| slug | **lumaca** | il Ka'het è una lumaca dentro un guscio |
| Ravager | **Devastatore** | arma |
| Annihilator | **Annichilatrice** | arma |
| EMP Torpedo / Disruptor | **Dispositivo EMP / Raggio Devastatore** | coerentemente con L24 |
| Shield Restorer | **Ripristinatore di Scudi** | |
| Reserve Accumulator | **Accumulatore di Riserva** | |
| Research Laboratory | **Laboratorio di Ricerca** | |
| Quantum Key Stone | **Pietra Chiave Quantistica** | da L24 |
| Void Rifle | **Fucile del Vuoto** | da L24 |
| jump drive / hyperdrive | **motore di salto / iperguida** | da L24 |
| hyperspace | **iperspazio** | |
| bunks / tons / capacity | `<bunks>` / `<tons>` / `<capacity>` | token intatti |

---

## 5. Difficoltà incontrate e come sono state risolte

1. **Virgolette dispari nel sorgente** (70 unità): riprodotte. Correzioni di conteggio avvenute solo
   quando il numero italiano era diverso da quello inglese, mai per "pulizia" tipografica.
2. **Unità 188**: il sorgente è troncato (`on anoth.`). Riprodotto con lo stesso troncamento
   (`su un altr.`), perché il testo italiano deve mantenere la lunghezza e il difetto del testo di
   partenza: non è un errore introdotto dalla traduzione.
3. **Unità 197/199/201, 204/206, 209/211, 214/216, 219/221/223/225/227**: `UI_LABEL` di `goto`
   (`all lucky`, `all telis`, `weapon maeri EMP`, …). Restano identici: sono nomi di nodo, non testo.
4. **Unità 281 `jump drive`** e **411 `skip dialog`**: `UI_LABEL`, restano identici.
5. **Unità 633**: il sorgente lascia la battuta di Dusk **aperta** (nessuna virgoletta di chiusura).
   L'italiano fa lo stesso: 5 virgolette, come il sorgente.
6. **Unità 776, 797, 823, 860, 861, 866**: il sorgente chiude la battuta **senza averla aperta**
   (una sola virgoletta finale, o tre invece di quattro). Riprodotto esattamente.
7. **Unità 605/605, 607/609, 612/616, 613/617, 832/833**: coppie quasi identiche nel sorgente
   (varianti dello stesso `goto`). Tradotte in modo distinto dove il testo inglese è distinto, e
   identico dove è identico.
8. **Unità 751/764**: `DESCRIPTION` identico in due missioni. Traduzione identica, dentro lo stesso
   gruppo di duplicati.
9. **Unità 807**: la traduzione `"Capisco."` collideva con l'unità 157 (inglese diverso). Riscritta
   `"Ho capito."` — la collisione era reale, non un falso positivo.
10. **Unità 509 `Lab deployment`**: `Schieramento del laboratorio` dava rapporto 2,00 (limite 1,75).
    Riscritta `Schierare il laboratorio`, che resta descrittiva e rientra nel rapporto.
11. **Unità 913 `What about you?`**: la resa letterale `"E tu?"` dava rapporto 0,44. Riscritta
    `"E tu che mi racconti?"`.
12. **Unità 722 `What about me?`**: stesso problema (0,47). Riscritta `"E che cosa faccio io?"`.
13. **Unità 528 `What comes next?`**: stessa famiglia (0,47). Riscritta `"Che cosa viene dopo?"`.
14. **`CONVERSATION` (30 unità)**: è testo visibile del blocco `conversation` (backtick nel `raw`,
    già rimosso in `english`). Tradotto come prosa e **non** inserito in `NT`.
15. **Tab iniziali**: 199 unità su 917 non hanno il tab (le `VALUE`, `DESCRIPTION`, `DIALOG`,
    `UI_LABEL` e il primo `MISSION_TEXT` di ogni missione). Due errori reali trovati e corretti
    (unità 347 e 34 di L26, stessa famiglia): il tab va confrontato **per unità**.

---

## 6. Che cosa è stato verificato e che cosa no

**Verificato (con exit code o stato osservato):**

- `check.py` completo: `FAIL totale: 0` su 917/917 unità, 21 controlli.
- `verify.py`: 25 controlli indipendenti, `FAIL: 0`, `exit=0`.
- `state.py`: `ESITO: OK`, repo `endless-sky` pulito su `b4aa3bac3`, nessuna modifica all'originale.
- `translation.json` sha256[:16] `37e09b22e11caf89`.

**Non verificato, e dichiarato:**

- **Nessuna approvazione nel DB**: le 917 unità restano `PENDING`. Lo staging non è approvazione.
- **Nessun rendering nel gioco**: la traduzione non è mai stata caricata da Endless Sky, né vista a
  schermo. Il testo è verificato strutturalmente, non visivamente.
- **I 49 contesti non sono stati giocati**: la coerenza di registro è stata mantenuta per lettura del
  sorgente, non per prova nel runtime.

---

## 7. Riproducibilità

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/L27_20261018_094756/check.py            # FAIL totale: 0
python staging/editorial/L27_20261018_094756/verify.py           # 25 controlli, exit 0
python staging/editorial/tools/state.py                          # ESITO: OK
```

Ripresa del lotto successivo (L28): unità **918**, riga **3051**, contesto `mission:Ka'het: Patir Mystery 20`.

---

## 8. Stato finale del lotto

- 917 / 917 unità tradotte, 0 `FAIL`.
- 35.520 parole EN → 32.640 IT, rapporto **0,919**.
- 20 `UI_LABEL` in `NT`, 30 `CONVERSATION` tradotte, 0 token persi, 0 backtick alterati.
- `verify.py` **25 controlli**, `exit 0`.
- `STATO.md` chiuso; handoff per L28 scritto; `CHECKPOINT_EDITORIALE.md` aggiornato.
