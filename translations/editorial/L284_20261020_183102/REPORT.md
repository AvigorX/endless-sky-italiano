# REPORT — L284 (`data/wanderer/wanderer missions.txt`, righe 93–136)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **27 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 18 (11 `MISSION_TEXT`, 2 `DESCRIPTION`, 2 `VALUE`, 2 `DIALOG`, 1 `UI_LABEL`) | 18 |
| parole | 549 | **513** (0,93) |
| tab | 8 | 8 · primo carattere |
| virgolette | 20 | **20**, per unità |
| alternative | **18** | **18**, stesse opzioni per gruppo |
| segnaposto | 12 (5 famiglie) | **12** |
| apici | 11 | 14 (`Va'ika` ×8) |

Rapporto per unità **0,90 – 1,27**.

## 2. Il contratto diceva «18 alternative, tutte con due opzioni»

Falso. **17 coppie + 1 singola**: `[disheartened?]` (unità 14) ha **una sola opzione** e il **punto interrogativo** che segnala
un'incertezza. Tradurla come coppia avrebbe aggiunto una variante che il gioco non ha; lasciarla in inglese avrebbe rotto il
testo visibile. Resa: **`[scoraggiata?]`**, una opzione, stesso segno.

Il `check.py` non si limita al totale: confronta la **distribuzione** completa delle opzioni fra le due lingue —
`[2, 2, 2, 2, 2, 2, 1, 2, …]` — e il `verify.py` la ricontrolla **unità per unità**. Un totale giusto con una struttura sbagliata
fallirebbe.

## 3. `UI_LABEL` e `VALUE`: tre copie, due regole

| unità | riga | tipo | testo | verifica |
|---|---|---|---|---|
| 7 | 108 | `UI_LABEL` | `next steps` | **identità** |
| 1 | 93 | `VALUE` | `Return to <planet>` | identità |
| 10 | 115 | `VALUE` | `Plant to <planet>` | identità, e **diverso** dall'altro |

In L283 i due `VALUE` erano **identici**; qui sono **diversi**: il test verifica entrambe le cose (identità con l'inglese e
differenza fra loro), perché «copiato» non significa «uguale agli altri».

## 4. `<npc>` femminile

Due occorrenze, entrambe controllate: «hai lasciato indietro **la** `<npc>`» (unità 12) e «insieme **alla** `<npc>`» (unità 17).
Il test verifica anche l'assenza di «il `<npc>`»: è la trappola che in passato ha prodotto «scomparso» per una nave.

## 5. Terminologia

| inglese | resa | nota |
|---|---|---|
| `equatorial lowland` | **pianura equatoriale** | |
| `dry, grassy plain` | **distesa arida ed erbosa** | |
| `soil` | **terra**, `composition` / `nature` → **composizione** / **natura** | |
| `detachment of healers/gardeners` | **distaccamento di guaritori / giardinieri** | |
| `become established` | **attecchiscano** | |
| `feather` | **piuma** | Va'ika perde una piuma: dettaglio da non perdere |
| `landing pad` | **piazzola** | |
| `Strong Wind` | **Strong Wind** | nome di nave, invariato |
| `Vara Kehi'ki`, `Solima Skarati` | **invariati** | |
| `morosely` | **quasi con tristezza** | registro | 

## 6. Verifica

```
check.py   27 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   27 prima · 18 qui · 9 dopo la 136 · 2 contesti · file 45/54 (83,3%)
```

**Due rossi al primo giro, entrambi su controlli miei:**

1. `opzioni(...) == 1` confrontava una **lista** con un intero: corretto in `len(opzioni(...)) == 1` (il controllo non poteva
   passare per costruzione);
2. dichiaravo `Va'ika` **nove** volte, misurate **otto**: corretto il numero nel controllo.

## 6-bis. Correzione preventiva del 2026-10-20

Lo stesso difetto trovato in L283 (asserire la copertura **globale** del file, 45/54) è stato corretto **prima** che L285 lo
rendesse falso: ora il test asserisce `len(seg) == 18` e `45 <= len(righe) <= 54`, e **stampa** la copertura. Il laboratorio ha
imparato la lezione sul lotto precedente, non su un rosso.

## 7. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 18 unità `PENDING`.
- **Nessun testo visto nel gioco**: le alternative sono verificate **per struttura**, non a schermo.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 45/54; resta l'**epilogo** (righe 169–182, 9 unità).
