# STATO — L223 · `remnant outfits.txt` (primo lotto — **file nuovo**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L223_20261019_224448` |
| Righe / unità | **48–297** / **12** — file a **12/57 (21,1%)** |
| Tipi | {'DESCRIPTION': 11, 'VALUE': 1} |
| Tab · virgolette · apici | **3** (unità 2, 4, 11) · **2** (unità 1) · **4 EN / 16 IT** |
| Segnaposto | **0** |
| Contesti | **8** — uno per equipaggiamento (Inhibitor Cannon 2, Inhibitor Turret 2, EMP Torpedo 2, EMP Torpedo Storage Bay 2, gli altri 1) |
| Parole | **463 EN → 458 IT** (0,99–1,15, media 1,08) |
| sha256 | `865540cb64989e26…` |
| Esiti | `check.py` **28** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Il rovesciamento rispetto a L222

| | `successor ships.txt` | `remnant outfits.txt` |
|---|---|---|
| composizione | 100 `TEXT` + 31 `DESCRIPTION` + 15 `VALUE` | **55 `DESCRIPTION`** + 2 `VALUE` |
| cosa si copia | i nomi (maggioranza) | **un solo `VALUE`** |
| cosa si traduce | 31 descrizioni | **tutte le 55** |
| parole per unità | ~17 | **~39** |

Il lotto L223 traduce **11 testi su 12**: il lavoro è la scrittura, non la copia, e il numero di unità non misura più lo
sforzo — **463 parole in 12 unità** contro 431 parole in 26.

## Nomi e parole comuni: la linea del lotto

Gli equipaggiamenti **restano in inglese anche nella prosa** — `Inhibitor Cannon`, `Inhibitor Turret`, `Thrasher Cannon`,
`Thrasher Turret`, `Point Defense Turret`, `EMP Torpedo Storage Bay` — perché sono gli stessi nomi che il giocatore vede nel
negozio di equipaggiamenti: tradurli creerebbe due nomi per lo stesso oggetto.

Si traducono invece le **parole comuni**: *cannon* → «cannone/cannoni», *turret* → «torretta/torrette», *torpedo* →
«siluro/siluri». Il controllo verifica **entrambi i lati**: che i nomi compaiano, e che le forme inglesi non restino come
nomi comuni fuori dai nomi.

## Cosa contiene

Le schede di sei equipaggiamenti dei Remnant: l'**Inhibitor Cannon** (nato da un'arma aliena rubata, che spinge indietro i
bersagli e interferisce con i motori), l'**Inhibitor Turret**, il **Thrasher Cannon** (ricavato per ingegneria inversa da un
proiettile energetico alieno, più danni in cambio di meno gittata), il **Thrasher Turret** (quattro cannoni su una base
rotante), il **Point Defense Turret** (copiato dai sistemi di difesa che sorvegliavano i depositi sotto Aventine) e i
**siluri EMP** con la loro stiva.

## Difficoltà

1. **Un'unità è una storia.** La 1 racconta di un esploratore attaccato e della capitana che dice: «Non torneremo a casa
   finché non ci impadroniremo di quell'arma.» La battuta è fra virgolette dritte e va resa come parlato, non come
   narrazione.
2. **`reverse engineer`** → «ricostruire con l'ingegneria inversa»: il calco «fare reverse engineering» sarebbe gergale.
3. **`interference effect` / `interfering with their engines`** → «effetto di interferenza», «interferendo con i loro
   motori»: la radice comune va tenuta, perché il nome dell'arma (`Inhibitor`) ci gioca sopra.
4. **`strong torques that previously made the use of a swiveling mount unfeasible`** → «le forti coppie che in passato
   rendevano impraticabile l'uso di un affusto girevole»: `torque` è la coppia meccanica, non «torsione».
5. **`point-defense systems`** → «sistemi di difesa puntuale»: termine tecnico, e il nome dell'equipaggiamento resta
   inglese.
6. **`Ember Waste`, `Aventine`, `Alphas`, `Remnant`** invariati: toponimi e nomi di fazione.
7. **`the Alphas would overrun human space and expand beyond it`** → «gli Alphas travolgessero lo spazio umano e lo
   superassero».

## Un errore mio, corretto prima di chiudere

Il controllo sulle parole comuni cercava la stringa «cannone» al singolare; nel testo compare solo «cannoni» (unità 3) e
l'asserzione è caduta. Aveva torto il controllo: ora cerca le forme con una regex (`cannon[ei]`, `torrett[ae]`,
`silur[oi]`) e verifica le occorrenze trovate nell'esito, così il fallimento è leggibile.

## Verifica

```bash
cd staging/editorial/L223_20261019_224448
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # FAIL: 0 (18 controlli) · 12/57 · 45 dopo la 297 · confine 298
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 12 unità `PENDING`.
