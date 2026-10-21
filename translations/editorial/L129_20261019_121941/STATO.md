# STATO — L129 · `data/human/boarding missions.txt` (primo lotto: 89 unità, frammenti di frase)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L129_20261019_121941` |
| Righe / unità | **15–386** / **89** — il lotto **apre** il file (0 unità prima) |
| Tipi | **48 `TEXT`** · **21 `MISSION_TEXT`** · **6 `CONVERSATION`** · **6 `VALUE`** · **6 `DESCRIPTION`** · **2 `DIALOG`** |
| Stati | **89 `PENDING`** — misurato e **asserito** in `mkparts.py` |
| Contesti | **18** — distribuzione 1/1/6/3/5/10/2/1/5/9/7/20/7/4/2/2/2/2 |
| Testi distinti | **80** per 89 unità |
| Parole | **852 EN → 819 IT** (0,961); per unità 0,56–1,80, media 1,14 |
| Tab · virgolette | **22 unità** · **10** |
| Token | **43** in **7 famiglie**: `<origin>` 17, `<destination>` 9, `<planet>` 7, `<payment>` 6, `<cargo>` 2, `<bunks>` 1, `<commodity>` 1 |
| sha256 | `fee796a7a3f4f2bd…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **30 controlli**, exit **0** — invariante di **segmento** |

## La forma nuova: i frammenti

**48 `TEXT`** su 89 non sono frasi: sono **pezzi** che il gioco concatena in una conversazione casuale.

```
${assist merchant 1} <origin>${assist merchant 2} ${assist merchant 3} <payment>${assist merchant 4}
```

| frase | unità | pezzi |
|---|---|---|
| 1-1 apertura | 3–8 | `Sapendo che` · `Poiché` · `Comprendendo che` · `Considerando che` · `Visto che` · `Sapendo come` |
| 1-2 cosa hai fatto | 9–11 | `hai cambiato rotta` · `ti sei scomodato` · `potresti aver cambiato i tuoi piani di volo` |
| 1-2 rischioso | 12–16 | `hai rischiato la vita` · `la nave` · `la tua nave` · `hai affrontato il fuoco nemico` · `il pericolo` |
| 1-3 fine | 17–26 | `per` · `al fine di` · `così che potessi` + `salvare` · `riparare` · `recuperare` · `assicurare` · `soccorrere` · `aiutare` + `il` |
| 2 | 29–34 | `, ` · ` e ` · `salvare il suo carico, ` … |
| 3 | 35–43 | `il suo` · `il` · `della nave` · `del vascello` · `sollevato` · `capitano` + `ti dà` · `ti offre` · `ti ricompensa con` |
| 4 | 44–50 | `.` · ` in segno di gratitudine.` · ` in segno di riconoscenza.` · … |

Da qui un **invariante nuovo**, che nessun lotto precedente aveva: **spazio iniziale e finale identici al sorgente**,
unità per unità. Lo spazio finale è parte del testo (`"Knowing that "`), e senza di esso la frase composta perde le
parole. Il controllo lo verifica su **89/89** unità.

## Due difetti del sorgente, riprodotti

1. Il frammento `` `the` `` (unità 26) **non ha lo spazio finale**: la composizione inglese produce `theits` e quella
   italiana `ilil`. Non si corregge: si riproduce, e si documenta (come la virgoletta in più di L126).
2. La frase composta è **sgrammaticata per costruzione** anche in inglese (`to save the, its captain gives you`):
   tradurre i frammenti non può riparare la grammatica dell'insieme.

## Quattro unità che non sono testo

| unità | cosa sono | resa |
|---|---|---|
| 1, 2 | template di `conversation`: `${assist merchant 1} <origin>…` | **identiche** |
| 27, 28 | **nomi di frase** citati da `phrase` (`assist merchant 2 simple/complex`) | **identiche** |
| 29, 44 | frammenti di sola punteggiatura (`, ` e `.`) | **identiche per necessità** |
| 51, 71, 82, 84, 86, 88 | `VALUE` (nomi di missione) | **identiche** |

Tradurre i nomi di frase romperebbe il gioco: sono **chiavi**, non testo. Il `check.py` li elenca uno per uno.

## Ripetizioni

`80` testi distinti su 89 unità: tre opzioni ripetute due volte (55/58, 56/59, 57/60) e quattro `DESCRIPTION` uguali
(83/85/87/89) più quattro `VALUE` uguali. Il controllo pretende **stesso inglese ⇒ stessa resa**, e il costruttore la
garantisce per costruzione (la resa è indicizzata per indice, non per firma).

## Perché la resa è indicizzata per unità

Con 48 frammenti brevi le **firme** sono ambigue per natura: `to ` è prefisso di `in order to `, `the` di `the `.
Una firma testuale avrebbe richiesto scelte arbitrarie; l'indice è univoco, e la coerenza si verifica a posteriori con
il confronto «stesso inglese ⇒ stessa resa». Il primo costruttore (a firme) è conservato come `mkparts1_superato.py`.

## Verifica

```bash
cd staging/editorial/L129_20261019_121941
python mkparts.py   # 89 unità · 80 testi distinti · 22 tab · 10 virgolette · 43 token
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (30 controlli)
```
