# REPORT — L201 · `hai outfits.txt` (primo lotto, apre il file)

## 1. Contenuto

Il primo lotto di **descrizioni di equipaggiamento** della campagna: sei oggetti Hai in otto paragrafi. Si passa dal
registro dei lavori a quello delle **schede tecniche**, con frasi lunghe e terminologia specifica.

| blocco | unità | righe | contenuto |
|---|---|---|---|
| Phantom Pallet | 1 | 27 | olografia militare riciclata per il contrabbando |
| Holovid Zone | 2–4 | 43–45 | tecnologia, normalità d'uso, abuso |
| Pulse Cannon | 5 | 69 | l'ingegneria Hai che non ostenta |
| Pulse Turret | 6 | 97 | due cannoni affiancati, bersagli veloci |
| Tripulse Shredder | 7 | 124 | raffiche, calore, consumo, «mordi e fuggi» |
| Ion Cannon | 8 | 164 | disturbo elettrico e inceppamento |

## 2. Difficoltà

1. **Nessun segnaposto** e nessuna unità `VALUE`: il lotto si regge tutto sulla resa del testo. Le tre asserzioni «vuote» (0 token, 0 `VALUE`, 0 `DIALOG`) sono scritte e verificate.
2. **Tab e virgolette**: due paragrafi indentati (`Holovid Zone` 2 e 3) e due virgolette intorno a `"holopads"` → `"olopad"`. Il controllo esige che siano **le stesse unità** in entrambe le lingue, non solo lo stesso numero.
3. **Nomi di prodotto**: la tentazione è tradurre `Phantom Pallet` o `Holovid Zone`. Restano inglesi, come i nomi di navi e armi. Ma **due** dei nove nomi attesi non compaiono nel testo (`Pulse Turret`, `Ion Cannon`): il controllo verifica che i nomi **presenti** siano invariati e **dichiara** l'assenza degli altri.
4. **Un errore mio, corretto nell'asserzione**: il primo `check.py` cercava tutti e nove i nomi in italiano e falliva su due. Non era la traduzione: era il presupposto. Il nuovo controllo distingue «nome presente nell'inglese» da «nome solo nel contesto».
5. **`Ion cannons` minuscolo** → «cannoni a ioni» (testo generico); `Ion Cannon` maiuscolo sarebbe il nome del prodotto. Il controllo verifica che l'unità 8 **non** contenga il nome maiuscolo.

## 3. Numeri osservati

```
unita' 8 · {'DESCRIPTION': 8} · tutte PENDING
2 tab · 2 virgolette · 0 apici EN / 5 IT · ZERO segnaposto
6 contesti · righe 27/164 · 0 unita' prima · 57 dopo · confine riga 205
parole 450 -> 458 · rapporto 0.96 - 1.25 (media 1.07)
FAIL totale: 0 (24 controlli) · verify exit 0 (15 controlli) · sha256[:16] 76f769f988aefc73
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto (compreso il `FAIL 1` intermedio) |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit **0** (15 controlli) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 8 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun caricamento nel gioco**, **nessuna partita avviata**, **nessuna revisione umana**.
- **Il file non è chiuso**: 57 unità dopo la riga 164.
