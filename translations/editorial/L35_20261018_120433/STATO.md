# L35 — stato di avanzamento (CHIUSO 2026-10-18)

Lotto `L35_20261018_120433` · `data/human/free worlds 1 start.txt` · righe 16–2343 · **663/663 unità**.
Quindicesimo file completo dello staging. Tutti i numeri sono misurati, non stimati.

## Fatto

- `source.json`: 663 unità, 37 contesti, kind 550 `MISSION_TEXT` / 33 `DESCRIPTION` / 32 `VALUE` /
  25 `LOGBOOK` / 22 `DIALOG` / **1 `UI_LABEL`**.
- `check.py` derivato da L34 con **`NT = {513, 547}`**: la `label` di salto `no casualties` (riga 1530,
  bersaglio di `goto`) e la categoria di diario `People`, l'unica riga `log` di questo file in cui
  l'inventario ha prodotto la **categoria** invece del testo. In L34 la lista era vuota: copiarla avrebbe
  fatto tradurre la label e rotto i salti.
- `TOKEN_EXC` vuoto, 13 famiglie di token di dati. Il controllo delle parentesi quadre resta **rimosso**
  (0 unità con `[a, b]`, misurato) e il `verify.py` asserisce che siano 0.
- 10 parti scritte a mano, tutte a fine missione: 1–76, 77–135, 136–194, 195–271, 272–345, 346–409,
  410–471, 472–544, 545–620, 621–663
  (76, 59, 59, 77, 74, 64, 62, 73, 76, 43). Ogni parte chiusa con `check.py --range` verde.
- `translation.json`: 663 unità, 21.140 EN → 20.273 IT (0,959), rapporto per unità 0,71–1,67,
  sha256[:16] `3a434b106edfceb3`.
- `verify.py`: **27 controlli**, `FAIL: 0`, exit 0. Copertura **663/663** asserita: il lotto è l'unico
  del file.
- `review.md`, `REPORT.md`, questo `STATO.md`.

## Regole applicate

- **Continuità di voce con L34, non ripetizione**: gli stessi personaggi (Tomek, Freya, JJ, Alondo,
  Katya, Eyes) tornano in un ruolo cambiato — il giocatore è ora un ufficiale delle Free Worlds, e il
  registro passa dalle trattative alle decisioni di comando. La voce resta quella di L34; le nuove scene
  (Tomek che urla contro il Senato, la governatrice di Poisonwood, Barmy Edward) hanno un registro
  proprio, documentato in `review.md` §4.
- **Il registro religioso è già distinto per personaggio** (decisione 109): Freya «Confido», JJ e Alondo
  «Prego», Tomek «Spero», i monaci assenti da questo file.
- **Si riproduce il sorgente**: tab 518/518 (500 unità con tab iniziale), virgolette 1.346/1.346,
  token 139/139. **Dieci unità** hanno un numero dispari di virgolette (battute aperte): riprodotte, e il
  `verify.py` confronta l'insieme degli idx.
- **Nessun controllo allentato**: 50/470 avevano lo stesso italiano con inglesi diversi
  (`what do we do now` / `what do we do next`) e sono state differenziate; 197, 278, 302, 502, 626
  riscritte per il rapporto minimo; 355 riscritta perché conteneva «shock and awe» in inglese.
- **Numeri dai file, non dalla memoria**: kind, 21 controlli di `check.py`, 27 di `verify.py` e tutti i
  totali vengono da misure.
- **Nessuna scrittura sul database**: `state.db` in sola lettura, 663 unità `PENDING`.

## Glossario del lotto (aggiunte rispetto a L34)

| inglese | italiano | nota |
|---|---|---|
| parole (prigionieri) | parola (data la parola) | istituto giuridico, reso come nel testo |
| Oathkeepers | Oathkeepers | nome del reggimento, invariato |
| Conservatory | Conservatorio | università pubblica delle Free Worlds |
| CCOR | CCOR | sigla; nome sciolto la prima volta: Consigli Confederati del Bordo Esterno |
| Plasma Turret | torretta al plasma | |
| Walloping Window-Blind, Red Nile, Terebinth | invariati | nomi di navi |
| Barmy Edward | Barmy Edward | soprannome, invariato; spiegato nel LOGB 234 |
| Barmy | — | non tradotto come aggettivo: è parte del nome |
| Quad Blaster Turrets | torrette blaster quadruple | |
| Star Barge, Falcon, Protector, Bastion, Boxwing | invariati | modelli di nave |
| Thule, Greenrock, Poisonwood, Harmony, Rust, Kraz, Longjump, Mere, Skymoot | invariati | toponimi |

## Verifica

```
check.py   → FAIL totale: 0     (21 controlli, copertura 663/663)
verify.py  → FAIL: 0, exit 0    (27 controlli)
```

Comandi:

```bash
cd ~/PROGETTI/G-DEV/GAME-SOURCE-LAB/endless-sky-l10n
python staging/editorial/L35_20261018_120433/check.py     # atteso: FAIL totale: 0
python staging/editorial/L35_20261018_120433/verify.py    # atteso: exit 0, FAIL: 0
```

## Residuo

Lo staging contiene ora **17.865 unità** su 15 file completi; il residuo misurato è **14.065 unità**
secondo la formula di `state.py` (che sottrae due volte le `UI_LABEL` già in staging: decisione 99).
Prossimo lotto: `data/human/free worlds 2 middle.txt`, righe 16–2336, 552 unità, 16.290 parole,
52 contesti, **fine file**.
