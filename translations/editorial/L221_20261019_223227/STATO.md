# STATO — L221 · `successor ships.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L221_20261019_223227` |
| Righe / unità | **904–1137** / **24** — file a **120/146 (82,2%)** |
| Tipi | {'TEXT': 15, 'DESCRIPTION': 7, 'VALUE': 2} |
| Tab · virgolette · apici | **3** (unità 7, 16, 24 — tutte `DESCRIPTION`) · **30** (2 × 15) · **5 EN / 2 IT** |
| Segnaposto | **0** |
| Contesti | **3** — `Stolsaqra` 10, `Seiitej` 7, `Veusade` 7 |
| Parole | **451 EN → 481 IT** (0,99–1,21, media 1,03) |
| sha256 | `b7a2199bbf3b9e42…` |
| Esiti | `check.py` **28** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Il tratto del lotto: tre schede quasi parallele

Le `DESCRIPTION` della **Stolsaqra** (unità 15 e 17) sono due versioni della stessa scheda e condividono tre formule; la 17
le condivide in parte anche con la 16:

| formula inglese | resa unica |
|---|---|
| *sports a surprising amount of firepower for a ship of its size* | «sfoggia una potenza di fuoco sorprendente per una nave delle sue dimensioni» |
| *plagued with power and propulsion issues* | «afflitto da problemi di energia e propulsione» |
| *albeit with significantly downgraded systems compared to the military-exclusive model* | «anche se con sistemi notevolmente depotenziati rispetto al modello riservato ai militari» |

Il `check.py` e il `verify.py` verificano tutte e tre le formule **in entrambe le unità** che le portano.

## Tab e virgolette: il contrario di L220

- **3 tab, tutti in `DESCRIPTION`** (unità 7, 16, 24) — in L220 il tab era in una sola unità, una `DESCRIPTION` al 24.
- **30 virgolette = 2 × 15 `TEXT`, nessuna in prosa** — in L220 due virgolette stavano dentro una `DESCRIPTION`.
- **Apici**: 5 in inglese (unità 6, 7, 17, 23, 24 — possessivi: *High Houses'*, *ship's*, *Successors'*, *Predecessors'*) e
  **2** in italiano (16 *l'unica*, 24 *all'uso*). Totale e distribuzione diversi: il controllo confronta le coppie.

Nessuna di queste tre cose è stata dedotta dal tipo: sono state **misurate** prima di scrivere il controllo.

## Cosa contiene

La **Seiitej** (nave da carico leggero delle Alte Case, usata anche come pattugliatore), la **Stolsaqra** (l'intercettore dei
Successori: compatto, potente, e «una trappola mortale» secondo i capitani prudenti) e la **Veusade** (otto cannoni a
trascinamento, progettata per avvicinarsi allo scafo nemico).

## Difficoltà

1. **`drag cannon` non esiste nel database come nome di equipaggiamento**: il termine vive solo in questa prosa. Reso «cannoni
   a trascinamento», coerente con «effetti di rallentamento» fissato in L220.
2. **`a charge for ambitious pilots and a deathtrap for prudent captains`** → «una sfida» per i primi, «una trappola mortale»
   per i secondi: il testo è ironico e l'ironia sta nell'opposizione fra i due aggettivi.
3. **`military-exclusive model`** → «modello riservato ai militari», non «esclusiva militare».
4. **`narrowly-focused design`** → «progetto così specializzato»; **`ill-suited for multipurpose use`** → «inadatte all'uso
   polivalente».
5. **`Blessed with the honor of being named with the Successor word for swiftness`** → «Onorata di portare il nome che nella
   lingua dei Successori significa rapidità».
6. **`catches and kills ships many times their size`** → «raggiungendo e distruggendo navi molte volte più grandi».

## Verifica

```bash
cd staging/editorial/L221_20261019_223227
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # FAIL: 0 (18 controlli) · 96 + 24 + 26 = 146 · confine 1141 DESCRIPTION
```

**Non verificato**: nessuna nave vista nel gioco; 24 unità `PENDING`.
