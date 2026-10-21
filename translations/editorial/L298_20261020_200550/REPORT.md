# REPORT — L298 (`data/coalition/coalition outfits.txt`, righe 202–337)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **23 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 15 (tutte `DESCRIPTION`) | 15 |
| parole | 471 | **491** (1,04) |
| tab | **5** | **5** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 7 | 6 |
| contesti | **10** (5 doppi + 5 singoli) | invariati |

Rapporto per unità **0,94 – 1,30**.

## 2. Le due scoperte del lotto

Il file cambia **soggetto** a metà: fino alla 337 sono moduli **energetici** della Coalizione, poi passano **armi e licenze**.
Qui il tema è ancora **tecnica di sopravvivenza**:

- **riparazione**: robot che si arrampicano sullo scafo (202), droni con passerelle che **interferiscono col raffreddamento**
  (218);
- **carburante**: il `Fuel Module` dei **Saryd** per non restare a secco lontano da **Saros** (246/247), il `Refueling Module`
  del **Lunarium** per non farsi ispezionare dagli Heliarch (273/274);
- **inganno**: il `Decoy Plating` che **riproduce i registri di scansione** di altre navi, con disturbatori radar come **ultima
  linea di difesa** contro i **siluri Heliarch** (259/260);
- **scudi**: il `Shield Refactor Module`, che sposta la riparazione dello scafo a **riparare i generatori** perché lavorino al
  vero limite (289/290);
- **sensori**: lo scanner della **Casa Idriss**, costruito coi dati di un **satellite perduto** (336/337).

## 3. Cinque coppie, cinque singole

| tipo | righe |
|---|---|
| coppie (2ª con `\t`) | 246/247, 259/260, 273/274, 289/290, **336/337** |
| singole | 202, 218, 232, 306, 323 |

Il test **elenca** le righe delle singole e verifica che ogni tab sia sulla **seconda** unità del contesto: né una coppia in più
né una tab fuori posto passano.

## 4. La coppia 336/337 sta sul confine

È l'ultima coppia del lotto. Dopo la 337 il file riprende alla **356** con `Small Thrust Module`: **contesto diverso**, quindi la
coppia non è spezzata. Il test verifica **entrambe** le cose — che 336 e 337 siano nel lotto, e che l'unità successiva sia di un
altro contesto.

## 5. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  23 controlli · FAIL: 0 · exit 0
segmento   15 prima · 15 qui · 19 dopo la 337 · file 30/49 (61,2%)
```

**Primo giro verde**: il contratto aveva già individuato le cinque coppie, la tab sull'ultima riga e il confine.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 15 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**: il rientro prodotto dalla tab resta **dedotto**.
- **Il file resta aperto**: 30/49; restano **19 unità**.
