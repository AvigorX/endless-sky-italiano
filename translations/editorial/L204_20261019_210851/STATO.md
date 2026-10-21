# STATO — L204 · `hai outfits.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L204_20261019_210851` |
| Righe / unità | **603–788** / **19** — file al **52/65 (80,0%)** |
| Tipi | {'DESCRIPTION': 13, 'VALUE': 6} |
| Tab · virgolette · apici | **0** · **6** (unità 15–16) · **2 EN / 6 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **13** — da `Hai Chasm Batteries` a `"Biroo" Atomic Thruster` |
| Parole | **441 EN → 454 IT** (rapporto 0,95–1,24, media 1,07) |
| sha256 | `12342441647f81f7…` |
| Esiti | `check.py` **22** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Cosa contiene

Sistemi di alimentazione Hai: cinque pacchi batterie in scala e i generatori, più i motori atomici e il set
combinato `"Baellie"`.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Hai Chasm Batteries | 1–2 | 603 | il più piccolo pacco batterie |
| Hai Fissure Batteries | 3–4 | 621 | capacità tripla |
| Hai Gorge Batteries | 5–6 | 639 | taglia media, impronta termica |
| Hai Ravine Batteries | 7–8 | 657 | densità energetica, Ion Cannon |
| Hai Valley Batteries | 9–10 | 675 | il modello più grande, raro |
| generatori a fusione · fissione | 11–12 | 692–704 | Korath, tecnologia rudimentale |
| Pebble Core · Sand Cell | 13–14 | 728–742 | reattore miniaturizzato, celle a combustibile |
| `"Baellie" Atomic Engines` | 15–16 | 775–776 | il set che il Flea non poteva portare |
| motori atomici Hai | 17–19 | 789 | efficienza, spazio umano, Shield Beetle |

## Difficoltà

1. **Sei `VALUE` con virgolette dentro il nome** (`"Baellie" Atomic Engines`): copiati alla lettera, virgolette comprese, e verificati uno per uno.
2. **Le virgolette sono nei nomi, non nella punteggiatura**: unità 15 (2) e 16 (4), tutte conservative; il controllo confronta unità per unità, non il totale.
3. **Errore d'asserzione mio**: «battery pack» compare **4** volte, non 5 — l'unità 10 dice *battery model*. Il controllo ora confronta il conteggio inglese con quello italiano.
4. **`heat footprint` → «impronta termica»**, due volte, coerente.
5. **Nomi e fazioni**: `Ion Cannon`, `Flea`, `Pebble Core`, `Sand Cell`, `Hai Shield Beetle`, `Korath`, `Deep` invariati; `Deep Sky` (azienda) invariata.

## Verifica

```bash
cd staging/editorial/L204_20261019_210851
python check.py     # FAIL totale: 0 (22 controlli)
python verify.py    # FAIL: 0 (18 controlli) · confine riga 805 con virgolette nel contesto
```

**Non verificato**: nessun equipaggiamento installato nel gioco, nessuna schermata vista, nessuna revisione umana; 19 unità `PENDING`.
