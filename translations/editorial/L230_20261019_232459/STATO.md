# STATO — L230 · `korath outfits.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L230_20261019_232459` |
| Righe / unità | **319–581** / **26** — file a **61/92 (66,3%)** |
| Tipi | **16 `DESCRIPTION`** · **10 `VALUE`** — massimo di nomi in un lotto misto |
| Tab · virgolette · apici | **7** (unità 1, 4, 11, 14, 17, 20, 23) · **0** · **8 EN / 16 IT** |
| Segnaposto | **0** |
| Contesti | **11** — i cinque Reverser 3 unità a testa, Planetary e Comet Thruster 1 |
| Parole | **430 EN → 448 IT** (1,04–1,25, media 1,09) |
| sha256 | `d246b4e6c38a2e78…` |
| Esiti | `check.py` **27** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Dieci nomi in un lotto solo

È il massimo di `VALUE` in un lotto misto della campagna: `Afterburners (Stellar Class)`, `Engines (Meteor Class)`,
`Bow Drives (Meteor Class)`, i cinque `Reversers` (Asteroid, Comet, Lunar, Planetary, Stellar) e i due `Thrusters`
(Asteroid, Comet). Confronto **10 identiche / 16 tradotte**, e il controllo verifica che le identiche siano **tutti e soli**
i `VALUE`.

## Due gruppi di testi ripetuti, uno attraversa il confine del lotto

1. **Unità 1 e 4** dicono la stessa frase dei postbruciatori — e quella frase è **già stata tradotta in L229**, unità 10
   (riga 300). La resa è ripresa **identica**, e il `check.py` la confronta leggendo il `translation.json` del lotto
   precedente: `by[1]['italian'] == prev[300]`. È il primo controllo **inter-lotto** della campagna, e nasce da un caso
   reale: la stessa frase compare in cinque classi di afterburner su due finestre diverse.
2. **Unità 11, 14, 17, 20 e 23** sono **cinque copie** dello stesso paragrafo (il motore installato in parte nello spazio
   armi). Cinque equipaggiamenti, una sola resa — verificata come insieme con un solo elemento.

## I tab tornano a 7

Dopo 3 (L229) e 0 (L228): tre conteggi consecutivi diversi nello stesso file. Il numero si misura sul lotto, sempre.

## Cosa contiene

L'**Afterburner (Stellar Class)** con il raffreddamento attivo alimentato dall'esplosione, i **motori Meteor Class** degli
**Esuli** (più grandi, più lenti, per portare più armi o più carico), il **Bow Drive** come retropulsore, i cinque
**Reverser** (Asteroid, Comet, Lunar, Planetary, Stellar) e i primi due **Thruster**.

## Difficoltà

1. **`the Exiles found it necessary`** → «gli Esuli ritennero necessario». `Exiles` è un nome di fazione ma è anche una
   parola inglese comune: l'ho tradotto, a differenza di `Kor Efret`, `Mereti` e `Kor Sestor` che restano invariati perché
   non hanno un corrispettivo italiano. Scelta dichiarata.
2. **`at the cost of some speed`** → «al prezzo di un po' di velocità».
3. **`acts as a reverser`** → «funge da retropulsore»: il nome dell'equipaggiamento è `Reversers (…)` e resta inglese, ma la
   parola comune nella prosa si traduce con il termine già fissato in L205.
4. **`giving Korath captains with weapon space to spare a small edge`** → «dando ai capitani Korath con spazio per le armi
   da spendere un piccolo vantaggio»: `weapon space` è lo spazio installabile, non un'arma.
5. **`yet too large to be worth sacrificing weapon space`** → «eppure troppo grande perché valga la pena sacrificargli spazio
   per le armi».
6. **`Dwarfing any reversers in human space`** → «Surclassando qualsiasi retropulsore dello spazio umano».
7. **`Being essentially a slightly altered Planetary Class engine`** → «Essendo in sostanza un motore Planetary Class
   leggermente modificato».
8. **`a reverse thrust unlike anything you've seen before`** → «una spinta all'indietro diversa da qualsiasi cosa tu abbia
   mai visto».
9. **`it produces quite a kick. But, it also draws a considerable amount of power`** → «produce un bel calcio. Ma assorbe
   anche una quantità considerevole di energia».

## Un errore mio, corretto prima di chiudere

Il controllo sulle cinque copie usava `by[11]['italian'].startswith('Questo motore…')`, ma la stringa **inizia con un tab**:
`FAIL 1`. Corretto con `.strip()` sul lato italiano. Il testo non è stato toccato: il tab iniziale è struttura del file.

## Verifica

```bash
cd staging/editorial/L230_20261019_232459
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # FAIL: 0 (19 controlli) · 61/92 · 31 dopo la 581 · confine 596
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 26 unità `PENDING`.
