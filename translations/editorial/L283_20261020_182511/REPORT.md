# REPORT — L283 (`data/wanderer/wanderer missions.txt`, righe 42–88)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **27 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 14 (9 `MISSION_TEXT`, 2 `DESCRIPTION`, 2 `VALUE`, 1 `DIALOG`) | 14 |
| parole | 495 | **435** (0,88) |
| tab | 7 | 7 · primo carattere |
| virgolette | 18 | **18**, per unità |
| alternative `[...]` | **18** | **18**, due opzioni ciascuna |
| segnaposto | 4 (3 famiglie) | **4** |
| apici | 9 | 15 (`Va'ika` ×9) |

Rapporto per unità **0,90 – 1,07**.

## 2. Le 18 alternative

Diciotto scelte a runtime su sei unità (1, 6, 7, 10, 11, 14). Con **l'articolo fuori dalla parentesi**, ogni combinazione deve
restare corretta: è il vincolo che ha costretto tre rese meno letterali.

| inglese | resa | vincolo |
|---|---|---|
| `[plans, steps]` | **`[piani, passi]`** | maschili plurali, «i nostri» fuori |
| `[restored, healed]` | **`[ripristinato, guarito]`** | participi maschili (la pianta **è stata** …) |
| `[originates, belongs]` | **`[ha origine, appartiene]`** | due verbi al presente, stessa reggenza `a`/`in` |
| `[create, engineer]` | **`[creare, progettare]`** | infiniti |
| `[artificial, unnatural]` | **`[artificiali, innaturali]`** | agg. m.pl. con «mezzi» |
| `[grow, prosper]` | **`[crescere, prosperare]`** | infiniti |
| `[believe, suspect]` | **`[crediamo, sospettiamo]`** | 1ª pl. |
| `[damaged, destroyed]` | **`[danneggiati, distrutti]`** | agg. m.pl. con «mondi» |
| `[see, imagine]` | **`[vedere, immaginare]`** | infiniti |
| `[purpose, way]` | **`[scopo, modo]`** | maschili, «il nostro» fuori |
| `[imagine, consider]` | **`[immagineremmo, considereremmo]`** | condizionale 1ª pl. |
| `[search, visit]` | **`[cerchiamo, visitiamo]`** | 1ª pl. |
| `[territory, region]` | **`[territorio, dominio]`** | **entrambi maschili**: «nel regione» sarebbe sbagliato |
| `[rivals, foes]` | **`[rivali, nemici]`** | m.pl. |
| `[originated, grew]` | **`[abbia avuto origine, sia cresciuta]`** | congiuntivi, ausiliari diversi, posizione «lì» spostata fuori |
| `[grown, originated]` | **`[cresciuta, nata]`** | participi femminili con «sarebbe» |
| `[years, cycles]` | **`[anni, cicli]`** | m.pl. |
| `[regions, environments]` | **`[regioni, ambienti]`** | «simili» è invariabile, regge entrambi i generi |

Il `check.py` verifica numero, posizione, **due opzioni per coppia** (dividendo su `[,?]`) e che **nessuna coppia resti in
inglese**; il `verify.py` rifà il conteggio in modo indipendente e aggiunge il controllo che ogni opzione italiana **non**
coincida con l'inglese.

## 3. `VALUE` e ripetizioni

I due `VALUE` sono **`A Home for the Plant`** (missione 2 e 3): copiati **e identici fra loro**, come nel sorgente. Le due
`DESCRIPTION` sono **identiche fra loro** in inglese e in italiano — è il testo della missione ripetuto su due tappe — e il test
lo verifica **in entrambe le lingue**, così una resa divergente fra le due fallirebbe.

## 4. Terminologia

| inglese | resa | nota |
|---|---|---|
| `xenobotany` | **xenobotanica** | |
| `Keti Va'ika` | **invariato** (9 occorrenze) | |
| `Sopi Lefarkata` | **invariato** | |
| `Unfettered` | **Slegati** | forma maggioritaria del corpus |
| `steppes` | **steppe** | |
| `wing` | **ala** | i Wanderer sono alati |
| `cargo hold` | **stiva** | |
| `spaceport` | **spazioporto** | |

## 5. Verifica

```
check.py   27 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   13 prima · 14 qui · 27 dopo la 88 · 3 contesti · file 27/54 (50,0%)
```

**Un rosso al primo giro**: il controllo su `Va'ika` dichiarava 5 occorrenze, misurate **9** (unità 4, 7, 10, 11, 14 ×3).
Corretto il numero nel controllo, non la traduzione.

## 5-bis. Correzione del 2026-10-20 (dopo L284)

Il controllo sulla copertura **asseriva lo stato globale del file** (`len(righe) == 27`): era vero quando L283 è stato scritto,
e L284 — coprendo altre 18 righe — lo ha reso **falso** con il lotto corretto. Un controllo che descrive il workspace invece
del lotto è un **controllo sbagliato**: è stato sostituito da un invariante **locale e monotòno** (`len(seg) == 14` e
`27 <= len(righe) <= 54`), con la copertura **stampata** e non asserita. `verify.py` di L283 torna verde su 24 controlli.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 14 unità `PENDING`.
- **Nessun testo visto nel gioco**: le 18 alternative sono verificate **per struttura e classe grammaticale**, non a schermo —
  la correttezza di ogni combinazione è argomentata, non eseguita.
- **Nessuna revisione umana**.
- **Il file resta aperto**: 27/54.
