# REPORT — L290 (`data/avgi/avgi culture conversations.txt`, righe 24–106)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **24 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 8 (tutte `MISSION_TEXT`) | 8 |
| parole | 468 | **450** (0,96) |
| rapporti (caratteri) | — | **1,06 – 1,17** |
| tab | 0 | **0** |
| virgolette | 10 | **10**, per unità |
| apici | 9 | 9 |
| segnaposto | 1 (`<ship>`) | **1** |
| alternative | 0 | **0** |

## 2. Il registro si inverte (di nuovo, e per una ragione)

| file | tipo di testo | controllo sul registro |
|---|---|---|
| `gegno ships.txt` (L286–L289) | schede tecniche | **nessun** «tu» (regex, lista esatta delle eccezioni) |
| `avgi culture conversations.txt` (L290) | scene e dialoghi | **≥ 5 unità su 8** con la seconda persona |

Nessuno dei due controlli è «il controllo giusto»: sono giusti **per il loro tipo di testo**. Scriverne uno solo e applicarlo a
tutto sarebbe l'errore.

## 3. Le scene ripetute

Il file contiene **due scene in doppia versione** (il gioco le usa in punti diversi):

| coppia | righe | parte condivisa | parte diversa |
|---|---|---|---|
| insegna | 82 / 86 | «Un'insegna elettronica economica, appiccicata alla parete alla meno peggio, lampeggia…» | la 86 **legge** il messaggio pubblicitario |
| protesta | 102 / 106 | **inizio** («Una fila di Avgi dall'aria arrabbiata…») e **chiusura** («…sulle loro bandiere e sui loro striscioni.») | la 106 riporta **tre slogan** |

Il test confronta le due rese con un **prefisso comune** e un **suffisso comune** calcolati a runtime:

```python
prefisso(by[5]['italian'], by[6]['italian']).startswith("Un'insegna elettronica economica")
suffisso(by[7]['italian'], by[8]['italian']) == '…sulle loro bandiere e sui loro striscioni.'
```

Se una delle due versioni fosse stata resa con parole diverse, il giocatore avrebbe visto **lo stesso posto descritto in due
modi**.

## 4. I tre slogan

| inglese | resa |
|---|---|
| `STOP CONSONANCE TAXES` | **BASTA CON LE TASSE DELLA CONSONANCE** |
| `ABOLISH MINERAL FEUDALISM` | **ABOLIAMO IL FEUDALESIMO MINERALE** |
| `STOP SENDING US TO DIE` | **SMETTETE DI MANDARCI A MORIRE** |

Maiuscolo e virgolette conservati; `Consonance` **invariato** e **femminile** («della»), come in `avgi news` (che dice «la
Consonance»).

## 5. Le parole inventate restano

`Incredulation` (imprecazione Avgi), `dee` (sostanza), `Zapchannel Ray Energy` (prodotto), `Consonance` (governo). Tutte
**invariate** e verificate **case-insensitive** (perché nello slogan `Consonance` compare in maiuscolo).

## 6. Verifica

```
check.py   24 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 8 qui · 38 dopo la 106 · 6 contesti
```

**Tre rossi al primo giro, tutti su controlli miei malformati:**

1. confrontavo il **suffisso italiano** con quello **inglese** (`== suffisso(EN, EN)`): confronto fra lingue diverse, sempre
   falso → sostituito con la chiusura attesa in italiano, verificata in **entrambe** le unità;
2. cercavo `Consonance` con la maiuscola iniziale, ma nello slogan è `CONSONANCE` → controllo reso **case-insensitive**;
3. cercavo `la Consonance` nell'unità 2 (il rifornimento), dove non c'è: la parola compare **solo** nell'unità 8, dentro lo
   slogan → controllo spostato su `DELLA CONSONANCE` (femminile) con il divieto di `DEL CONSONANCE`.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 8 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 8/46; restano **38 unità** (36 `MISSION_TEXT` + **2 `LOGBOOK`**).
- **Il registro Avgi** (frasi che **dichiarano l'emozione** prima del contenuto, come in `avgi news`) qui **non compare**: le
  scene sono descrittive. Quando comparirà, andrà ripreso dalla forma già usata.
