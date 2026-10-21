# STATO — L284 (`data/wanderer/wanderer missions.txt`, righe 93–136)

**Stato: CHIUSO.** Terzo lotto del file: `The Plant 4` e `The Plant 5`, con il **primo `UI_LABEL`** del file e **18
alternative** di cui **una singola**. File a **45/54 (83,3%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L284_20261020_183102/` |
| righe | 93–136 |
| unità | **18** — 11 `MISSION_TEXT` + 2 `DESCRIPTION` + 2 `VALUE` + 2 `DIALOG` + **1 `UI_LABEL`** |
| parole | **549 EN → 513 IT** (0,93) |
| rapporto | **0,90 – 1,27** (sulle 15 tradotte) |
| contesti | **2** — `The Plant 4` (93–112) · `The Plant 5` (115–136) |
| tab | **8** (unità 4, 5, 6, 8, 14, 15, 16, 18) |
| virgolette | **20**, per unità |
| **alternative `[...]`** | **18** — **17 coppie + 1 singola** (`[scoraggiata?]`) |
| segnaposto | **12** in 5 famiglie — `<planet>` 5 · `<destination>` 2 · `<origin>` 2 · `<npc>` 2 · `<first>` 1 |
| apici | **11 EN** / **14 IT** (`Va'ika` ×8) |
| copiati | **1 `UI_LABEL`** (`next steps`) + **2 `VALUE`** (diversi fra loro) |
| `check.py` | **27 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 27 prima · 18 qui · **9 dopo** la 136 |
| `sha256[:16]` | **`ed34b1008a5507c9`** |

## Comandi

```bash
python staging/editorial/L284_20261020_183102/check.py     # FAIL totale: 0 (27 controlli)
python staging/editorial/L284_20261020_183102/verify.py    # FAIL: 0 (24 controlli, 45/54)
```

## Il `UI_LABEL`: copiato, non tradotto

Riga 108, `next steps` (contesto `mission:Wanderers: Mereti: The Plant 4`). È una **etichetta di interfaccia**: il gioco la
mostra come titolo di un passo di missione, e tradurla cambierebbe un'etichetta che il database tiene in `UI_LABEL`. Il test
verifica **l'identità** (`== 'next steps'`), non la differenza — ed è la prima volta in questo file.

## La singola: `[disheartened?]`

Diciotto parentesi quadre, ma **non tutte doppie**: `[disheartened?]` ha **una sola opzione** e un **punto interrogativo** che
segnala un'incertezza del personaggio (Va'ika si corregge da sola). La resa è **`[scoraggiata?]`**: una opzione, stesso segno.
Il test confronta la **distribuzione completa** delle opzioni fra inglese e italiano —
`[2, 2, 2, 2, 2, 2, 1, 2, …]` in entrambe — così una struttura alterata fallirebbe anche se il totale restasse 18.

**Il contratto diceva «18 alternative, tutte con due opzioni»: era sbagliato.** Il workspace ha vinto, e la correzione è qui.

## `<npc>` è una nave, quindi femminile

Due occorrenze (unità 12 e 17), entrambe verificate: «hai lasciato indietro **la** `<npc>`», «insieme **alla** `<npc>`», «**Sta**
trasportando la pianta». Un «il `<npc>`» farebbe fallire il test.

## Il contenuto

- **`The Plant 4`**: una **pianura equatoriale**, «arida ed erbosa», dove si può **respirare** — e Va'ika dice «Qui
  `[crescerà, attecchirà]`». Poi la richiesta: tornare a **Vara Kehi'ki** e mandare un **distaccamento** di
  `[guaritori, giardinieri]` su `<planet>`, per riportare le piante su `<origin>` «quando sarà guarito».
- **`The Plant 5`**: la pianta caricata su una **Strong Wind** — «una piuma cade a terra» mentre Va'ika parla e si corregge:
  «non dovrei essere così `[scoraggiata?]`». Il congedo: resterà a `[sovrintendere, osservare]` il lavoro, poi partirà per
  altri mondi; «Ti ringrazio molto `[gratamente, sinceramente]` per il tuo aiuto, `<first>`».

## Limiti dichiarati

Nessuna approvazione (18 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **9 unità**: l'epilogo.
