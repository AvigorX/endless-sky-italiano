# STATO — L224 · `remnant outfits.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L224_20261019_224956` |
| Righe / unità | **298–565** / **13** — file a **25/57 (43,9%)** |
| Tipi | **13 `DESCRIPTION`** — nient'altro |
| Tab · virgolette · apici | **9** (unità 1, 3, 4, 5, 7, 8, 10, 11, 13) · **2** (unità 3) · **3 EN / 16 IT** |
| Segnaposto | **0** |
| Contesti | **5** — Teciimach Bay 4, Teciimach Pod 3, Ember Tear 3, Crystal Capacitor 2, EMP Torpedo Bay 1 |
| Parole | **472 EN → 483 IT** (0,98–1,58, media 1,22) |
| sha256 | `bee38f3d2fc80881…` |
| Esiti | `check.py` **28** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Primato: zero unità da copiare

Il lotto è **13 `DESCRIPTION` su 13**: nessun `VALUE`, nessun `TEXT`. Per la prima volta nella campagna non c'è **niente da
copiare** — il confronto «identiche / tradotte» vale **0 / 13**, ed è scritto esplicitamente in entrambi gli script. Un
`0` silenzioso sarebbe indistinguibile da un errore; un `0` asserito è un fatto misurato.

## I 9 tab: la densità più alta della campagna

Nove unità su tredici aprono con un tab (1, 3, 4, 5, 7, 8, 10, 11, 13). Nei lotti precedenti erano 1–3 per lotto. Un tab
perso in un paragrafo lungo non si nota leggendo: si nota solo contando per unità in entrambe le lingue.

## Le due coerenze

1. **Unità 1, 5 e 8 sono la stessa frase**, *Ammunition for this weapon can be restocked at any outfitter.*, per tre
   equipaggiamenti diversi (EMP Torpedo Bay, Teciimach Bay, Teciimach Pod). La resa è **identica nelle tre**, carattere per
   carattere, e il controllo confronta i tre valori con `==`.
2. **La frase sugli impulsi elettromagnetici torna da L223/12**, con un `originally` in più: «furono sviluppate
   **originariamente** dai Remnant». Stessa resa, una parola aggiunta — e il controllo verifica anche che la forma **senza**
   `originariamente` non ci sia.

## Cosa contiene

La **Teciimach Bay** (la revisione del lanciasiluri EMP: il meccanismo che risparmia gli alleati e il caricatore più grande
di un terzo), la **Teciimach Pod** (la versione per intercettori, che lancia tutti i siluri insieme per le tattiche mordi e
fuggi), l'**Ember Tear** (l'arma che produce micro-strappi nello spazio-tempo, con il tecnico che risponde *'both.'*) e il
**Crystal Capacitor** (cristalli di Viminal che immagazzinano energia e dissipano la ionizzazione).

## Difficoltà

1. **Il gioco di parole di `Ember Tear`.** Il nome può significare *strappare* o *piangere*, e il tecnico risponde
   *'both.'* — reso «'entrambe le cose'», fra **apici singoli** come il sorgente, che sono 2 dei 3 apici inglesi del lotto.
2. **`micro-tears … cauterizing them together again`** → «micro-strappi … li ricuce insieme»: la metafora chirurgica va
   tenuta, non spiegata.
3. **`ionizing yourself or the rest of your fleet`** → «ionizzare te stesso o il resto della tua flotta»: `ionizing` è
   l'effetto di gioco (ionizzazione), non un termine chimico generico.
4. **`hit-and-run tactics`** → «tattiche mordi e fuggi»; **`capital ships`** → «navi capitali».
5. **`a clip that is a third larger`** → «un caricatore più grande di un terzo»: `clip` è il caricatore, non la clip video.
6. **Le tre righe di servizio** — «Le munizioni per quest'arma possono essere rifornite presso qualsiasi negozio di
   equipaggiamenti.» — hanno rapporto 1,58, il più alto del lotto, perché `outfitter` è reso con il termine fisso «negozio di
   equipaggiamenti». È dentro il gate e dichiarato.
7. **`the Waste`** (unità 13) è l'abbreviazione di `Ember Waste` → «la Waste», invariato come il nome intero.

## Un errore mio, corretto prima di chiudere

Il controllo di coerenza cercava la parola **«originariamente» dentro l'inglese** (`'originariamente' in by[2]['english']`),
dove c'è invece `originally`: `FAIL 1`. Corretto in `'originally' in by[2]['english']`, con in più l'asserzione che la
forma senza avverbio non compaia nel testo italiano.

## Verifica

```bash
cd staging/editorial/L224_20261019_224956
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # FAIL: 0 (18 controlli) · 25/57 · 32 dopo la 565 · confine 581
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 13 unità `PENDING`.
