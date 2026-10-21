# STATO — L201 · `hai outfits.txt` (primo lotto: **apre il file**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L201_20261019_204959` |
| Righe / unità | **27–164** / **8** — file all'**8/65 (12,3%)** |
| Tipi | {'DESCRIPTION': 8} — nessun `VALUE`, `DIALOG` o `TEXT` |
| Tab · virgolette · apici | **2** (unità 3-4) · **2** (unità 1) · **0 EN / 5 IT** |
| Segnaposto | **0** in tutto il file (asserzione negativa scritta) |
| Contesti | **6** — da `Phantom Pallet` a `Ion Cannon` |
| Parole | **450 EN → 458 IT** (rapporto 0,96–1,25, media 1,07) |
| sha256 | `76f769f988aefc73…` |
| Esiti | `check.py` **24** (`FAIL 0`, exit 0) · `verify.py` **15** (`FAIL: 0`, exit 0) |

## Cosa contiene

Sei equipaggiamenti Hai descritti in otto paragrafi: olografia, armi a impulsi e cannoni a ioni.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Phantom Pallet | 1 | 27 | olografia da contrabbando: `"olopad"`, carico finto, fantasmi per i sensori |
| Holovid Zone | 2–4 | 43–45 | tre paragrafi: tecnologia, uso quotidiano, usi illeciti |
| Pulse Cannon | 5 | 69 | ingegneria Hai: efficiente, affidabile, ben bilanciata |
| Pulse Turret | 6 | 97 | due Pulse Cannon affiancati, inseguimento dei bersagli veloci |
| Tripulse Shredder | 7 | 124 | tre cannoni in un alloggiamento, raffiche, arma «mordi e fuggi» |
| Ion Cannon | 8 | 164 | perturbazione dei sistemi elettrici, inceppamento delle armi |

## Difficoltà

1. **Zero segnaposto**: prima volta in questa serie. L'asserzione è **negativa** e va scritta (`== 0`), altrimenti «niente da controllare» e «controllo mancato» si confondono.
2. **Unità lunghe**: 450 parole in 8 unità (56 medie). Il gate 0,55–1,90 lavora su testi grandi e perdona meno degli errori di taglio.
3. **Registro tecnico**: `textured force fields`, `phase array speakers`, `single shared housing`, `pattern of fire`. Resi con termini tecnici italiani, senza calchi.
4. **Nomi di prodotto invariati**: `Phantom Pallet`, `Holovid Zone`, `Pulse Cannon`, `Tripulse Shredder`, `Deathsticks`, `Unfettered`, `Wanderer`. **`Pulse Turret` e `Ion Cannon` non compaiono nel testo** — solo nei contesti — e il `check.py` lo dichiara invece di fingere di averli verificati.
5. **Apici asimmetrici**: 0 inglesi contro 5 italiani, tutti da elisione (`l'arma`, `l'alloggiamento`, `un'arma`, `l'energia`, `l'effetto`).
6. **Un'asserzione sbagliata, corretta**: il primo `check.py` pretendeva che tutti e 9 i nomi comparissero in italiano; due non compaiono nemmeno in inglese. Corretto il controllo, non il testo.

## Verifica

```bash
cd staging/editorial/L201_20261019_204959
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # FAIL: 0 · exit 0 (15 controlli)
```

**Non verificato**: nessun equipaggiamento installato nel gioco, nessuna schermata vista, nessuna revisione umana; le 8 unità restano `PENDING`.
