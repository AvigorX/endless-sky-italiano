# STATO — L207 · `coalition news.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L207_20261019_211444` |
| Righe / unità | **95–176** / **17** — file al **37/112 (33,0%)** |
| Tipi | {'NEWS': 17} |
| Tab · virgolette · apici | **0** · **34** (2 per unità, **tutte** citate) · **4 EN / 4 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **6** — agent 1, candidate 3, arach tourist 3, kimek tourist 3, saryd tourist 3, researcher 4 |
| Parole | **432 EN → 407 IT** (rapporto 0,91–1,22, media 1,07) |
| sha256 | `af8d352da08f8841…` |
| Esiti | `check.py` **23** (`FAIL totale: 0`) · `verify.py` **17** (`FAIL: 0`) |

## Registro: tutto il lotto è discorso Saryd

A differenza di L206 (dove due unità erano narrazione), **qui ogni unità è una citazione**: 17 su 17, 34 virgolette.
Il registro invertito si applica quindi senza eccezioni di tipo.

**14 unità su 17 finiscono con un verbo flesso.** Le tre che non lo fanno — 12, 13 e 16 — **non lo fanno nemmeno nel
sorgente**: la loro ultima frase è in ordine normale (*«If only the locals had a more civil sense of attire.»*,
*«...in the distinct architecture of some buildings here.»*, *«...so much easier to get a hold of complex
chemicals...»*). Il controllo verifica l'insieme esatto: non pretende l'inversione dove il testo non la mette.

## Cosa contiene

Sei parlanti diversi, tutti nella stessa cadenza: un agente Heliarch (i volontari in blu), un candidato Heliarch (le
prove, il *consul* Aulori), un turista Arach (le strade strette, il cibo), un turista Kimek (la carovana, i regali), un
turista Saryd (il primo viaggio, la cucina) e un ricercatore della Coalizione (il campione di sangue, Ring of Wisdom).

## Difficoltà

1. **La cadenza va mantenuta su testi diversi**: comico, burocratico, turistico, scientifico. La regola sintattica è la
   stessa, il lessico no.
2. **`consul Aulori`**: *consul* resta prestito latino, come `magister`, per non generare «console» — che in italiano è
   un apparecchio. Verificato con un'asserzione che esclude la forma sbagliata.
3. **`Ring of Wisdom`** resta in inglese: è il nome di una stazione, non un nome comune.
4. **`Arachi`** resta invariato: il sorgente usa un plurale che non è quello della fazione (`Arach`), e il testo lo mette
   in bocca al parlante.
5. **`arcology` → «arcologia»**: termine di mondo, una sola occorrenza ma destinato a tornare.
6. **Registro e cortesia insieme**: l'unità 14 in inglese dice *«would you mind?»*; in italiano ho usato «ti
   dispiacerebbe», perché il registro unico della campagna è il «tu». È l'unico punto in cui due convenzioni si
   toccano, ed è dichiarato.

## Verifica

```bash
cd staging/editorial/L207_20261019_211444
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # FAIL: 0 (17 controlli) · confine riga 177, stesso contesto
```

**Non verificato**: nessuna schermata del notiziario vista nel gioco, nessuna revisione umana; 17 unità `PENDING`.
