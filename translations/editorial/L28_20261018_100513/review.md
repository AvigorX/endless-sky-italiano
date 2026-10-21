# L28 — revisione di chiusura

**Ambito:** `data/kahet/kahet missions.txt`, righe **3051–5297**, **821 unità**, **30.796 parole**, **47 contesti**.
**Esito:** `check.py` completo **`FAIL totale: 0`**, `verify.py` **24 controlli, exit 0**, `FAIL: 0`.
**Data di chiusura:** 2026-10-18.

---

## 1. Collocazione nel file

| Voce | Valore misurato |
|---|---|
| File | `data/kahet/kahet missions.txt` |
| Unità nel file | 1.738 |
| Unità nel lotto | 821 (righe 3051–5297, **fine file**) |
| Unità prima del lotto | **917** (L27) |
| Unità dopo il lotto | **0** |
| Copertura del file | **1.738 / 1.738 (100%)** |

L28 **chiude il file**: con L27 copre 1.738 unità su due lotti, zero sovrapposizioni. Per questo il suo
`verify.py` **può** asserire la copertura totale, cosa che quello di L27 non poteva fare. `kahet
missions.txt` diventa l'**ottavo file completo** dello staging.

---

## 2. Le dieci parti

| parte | unità | righe | EN | IT | IT/EN | rapporto per unità |
|---|---|---|---|---|---|---|
| part01 | 1–85 | 3051–3300 | 3.229 | 2.894 | 0,896 | 0,69–1,60 |
| part02 | 86–170 | 3301–3503 | 3.858 | 3.435 | 0,890 | 0,75–1,50 |
| part03 | 171–255 | 3504–3730 | 3.970 | 3.530 | 0,889 | 0,82–1,83 |
| part04 | 256–340 | 3731–3954 | 3.246 | 2.937 | 0,905 | 0,72–1,77 |
| part05 | 341–425 | 3960–4169 | 3.155 | 2.870 | 0,910 | 0,69–1,64 |
| part06 | 426–510 | 4170–4371 | 2.740 | 2.484 | 0,907 | 0,77–1,64 |
| part07 | 511–595 | 4372–4678 | 2.514 | 2.315 | 0,921 | 0,68–1,70 |
| part08 | 596–680 | 4679–4863 | 3.163 | 2.867 | 0,906 | 0,77–1,35 |
| part09 | 681–765 | 4864–5117 | 2.898 | 2.685 | 0,927 | 0,75–1,29 |
| part10 | 766–821 | 5118–5297 | 2.023 | 1.897 | 0,938 | 0,66–1,80 |
| **totale** | **1–821** | **3051–5297** | **30.796** | **27.914** | **0,906** | **0,66–1,83** |

---

## 3. Conteggi strutturali (verificati per unità)

| Elemento | IT | EN |
|---|---|---|
| tab iniziali | 651 | 651 |
| virgolette `"` | 1.199 | 1.199 |
| backtick | 0 | 0 |
| token `<…>` | 159 | 159 |

- **51 unità con virgolette dispari** nel sorgente: riprodotte esattamente.
- **29 gruppi di duplicati inglesi** (67 unità): italiano identico ammesso solo dentro un gruppo.
- **Nessun pronome-token**: `TOKEN_EXC` vuoto.
- **4 `UI_LABEL`** in `NT`: 198, 800, 804, 818 (bersagli di `goto`).
- **Nessuna `CONVERSATION`** in questo segmento: la ricognizione ne conta 0.

---

## 4. Famiglie lessicali nuove di questo lotto

| EN | IT | Nota |
|---|---|---|
| Swan | **Swan** | invariato, nome di classe |
| Petrel | **Petrel** | invariato |
| Tern | **Tern** | invariato |
| Peregrine | **Peregrine** | invariato |
| Smew | **Smew** | invariato |
| Merganser | **Merganser** | invariato |
| Albatross | **Albatross** | invariato |
| Ibis | **Ibis** | invariato |
| Snipes | **Snipes** | nome dei droni da ricognizione |
| Calm Sea Afire | **Calm Sea Afire** | invariato (nome proprio di nave) |
| liveship | **nave viva** | coniato qui, coerente |
| ramscoop | **ramscoop** | invariato, termine tecnico |
| Scram drive | **motore Scram** | |
| gaslining / gaslined ship | **adatta all'atmosfera** | reso come descrizione |
| Inhibitor Cannon/Turret | **Cannone/Torretta Inibitrice** | |
| Void Sprite | **spettro del vuoto** | da L24 |
| Key Stone | **Pietra Chiave** | da L24 |
| zombie satellite | **satellite zombi** | |
| barbican | **barbacane** | (se presente) |
| Ka'mar / Faes'mar / Ka'het / Ka'sei / Fetri'sei | invariati | nomi di classe |
| Balnii / Alix / Pathera / Antamesa / Baliesa / Meligara / Seraglio / Kumkapi / Viminal | invariati | toponimi |

---

## 5. Difficoltà incontrate e come sono state risolte

1. **Ramificazioni di morte** (Patir Mystery 33 e 34): il testo ha tre percorsi che terminano con la
   morte del giocatore, ciascuno con la stessa chiusura (`allarme di perforazione`, `tutto diventa nero`).
   Le chiusure identiche sono duplicate nel sorgente e quindi ammesse in italiano.
2. **Quasi-duplicati con differenze minime**: le missioni "Safety Net" hanno tre `DESCRIPTION` quasi
   identiche e tre `MISSION_TEXT` che differiscono per una frase; tradotte mantenendo la differenza.
3. **Testi troncati nel sorgente**: alcune battute chiudono la citazione senza averla aperta (unità 398,
   551, 562, 569, 647, 816). Il conteggio è riprodotto, non normalizzato.
4. **Unità 546 `What about you?`**: la resa `E tu?` dava rapporto 0,44; riscritta `E tu, invece?`.
5. **Unità 456**: passato remoto fuori registro (`Sparai`) → presente (`Sparo`).
6. **Unità 484**: refuso di stesura (`quandunque`) → `quando che sia`.
7. **Unità 176**: era rimasto l'inglese `Come promised Dusk` → `Come aveva promesso Dusk`.
8. **Unità 177**: refuso (`semiciilindrica`) → `semicilindrica`.

---

## 6. Che cosa è stato verificato e che cosa no

**Verificato:**

- `check.py`: `FAIL totale: 0` su 821/821 unità.
- `verify.py`: 24 controlli indipendenti, `FAIL: 0`, `exit=0`; copertura **1.738/1.738** asserita.
- `state.py`: `ESITO: OK`, repo `endless-sky` pulito su `b4aa3bac3`.
- `translation.json` sha256[:16] `ba932b11d8e35fb8`.

**Non verificato, dichiarato:**

- **Nessuna approvazione nel DB**: le 821 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: la traduzione non è mai stata letta da Endless Sky né vista a schermo.
- **Nessun test di gameplay** sui 47 contesti.

---

## 7. Riproducibilità

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/L28_20261018_100513/check.py    # FAIL totale: 0
python staging/editorial/L28_20261018_100513/verify.py   # 24 controlli, exit 0
python staging/editorial/tools/state.py                  # ESITO: OK
```

Prossimo lotto (L29): `data/hai/hai missions.txt`, righe 23–2696, 823 unità.

---

## 8. Stato finale

- 821 / 821 unità, 30.796 EN → 27.914 IT, rapporto **0,906**.
- `kahet missions.txt` chiuso a **1.738/1.738** (ottavo file completo).
- `verify.py` **24 controlli**, `exit 0`; `STATO.md` chiuso; handoff L29 e checkpoint aggiornati.
