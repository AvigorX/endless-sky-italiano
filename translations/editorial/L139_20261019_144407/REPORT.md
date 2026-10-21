# REPORT — L139 · `data/starts.txt` (due nomi di equipaggiamento: **chiude il file a 113/113**)

## 1. Contenuto

| unità | riga | sorgente | resa | perché |
|---|---|---|---|---|
| 1 | 365 | `"Benga" Atomic Thruster` | **identico** | nome del propulsore |
| 2 | 366 | `"Biroo" Atomic Steering` | **identico** | nome del timone |

Nessun testo narrativo: il contesto è `ship:Grasshopper`, la nave che il venditore Hai consegna in L138. Le due unità
sono i riferimenti ai pezzi installati di serie.

## 2. Scelte

| nodo | decisione | nota |
|---|---|---|
| `"Benga"` · `"Biroo"` | **invariati** | nomi dei produttori |
| `Atomic Thruster` · `Atomic Steering` | **invariati** | nomi di modello, non descrizioni |
| virgolette | **conservate** | fanno parte del nome, non sono dialogo |
| tab e backtick del `raw` | **fuori dal testo** | il campo `english` non li contiene: il lotto ha zero tab |

Tradurre «Atomic Thruster» in «Propulsore Atomico» avrebbe rotto il riferimento al bene di gioco e la coerenza con
`data/human/outfits.txt`, dove questi nomi restano inglesi.

## 3. Difficoltà

1. **Lotto di 2 unità**: un `check.py` copiato da L138 (47 unità) fallirebbe su tutto; i numeri si misurano sull'export.
2. **Identità come scelta, non come omissione**: i due testi stanno in `ID_OK` con un controllo dedicato; senza,
   «tutte tradotte» li avrebbe bocciati e la scorciatoia sarebbe stata escluderli dai controlli.
3. **Tab e backtick nel `raw`, non nel testo**: un controllo verifica che `english` non inizi con tab (0 attese).
4. **Quattro virgolette che non si traducono**: due per nome, verificate per unità.
5. **Invariante di file**: il `verify.py` somma i cinque lotti (32 + 15 + 17 + 47 + 2 = 113) invece di fidarsi di un
   totale scritto a mano.
6. **Un errore mio nello strumento, non nel lotto**: il controllo «nessun altro lotto rivendica righe di starts.txt»
   falliva perché i percorsi erano costruiti con `staging/editorial` (barra) e confrontati con `staging\editorial`
   (backslash). Corretto con `os.path.abspath(...)`; la traduzione non è stata toccata.

## 4. Numeri osservati

```
unita' 2/2 · TEXT 2 · VALUE 0 · UI_LABEL 0 · token 0 · tutte PENDING
contesto 1 (ship:Grasshopper) · testi 2, identici al sorgente
tab 0 · virgolette 4 (2 + 2) · quadre 0 · backtick 0
parole EN 6 -> IT 6 (1.00) · rapporto 1.00
righe 365/366 · 111 prima / 0 dopo · FILE CHIUSO 113/113
FAIL totale: 0 (21 controlli) · verify exit 0 (22 controlli)
sha256[:16] 1ceb216ebf1e03c6
```

## 5. Stato del progetto

```
TOTALE staging: 27499 unità · 868849 EN · 825570 IT
starts.txt: 113/113 (100,0%) · 5 lotti · 4236 EN -> 4094 IT
file completi: quarantanove · residuo traducibile (formula state.py): 4431
residuo misurato: 5098 unità / 108250 parole su 117 file
avanzamento: 27499/32924 unità (83,5%) · 868849/979975 parole (88,7%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 1 parte, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (21 controlli), `verify.py` exit **0** (22 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 2 unità `PENDING`, nessuna nave caricata nel gioco.
- **Nessuna partita avviata**: i nomi dei propulsori non sono stati visti a schermo.
- **Nessuna revisione umana**.
- **Prossimo file**: `data/hai/unfettered 0 prologue.txt` (**147 unità · 4.052 parole · 5 contesti**), che apre con
  `mission:First Contact: Unfettered`.
- **Prossimo lotto**: `HANDOFF_L140_20261019.md` — righe **22–81**, **25 unità**, 405 parole, **1 contesto**,
  **25 `MISSION_TEXT`**, **23 unità con tab**, **50 virgolette**, **zero token**.
