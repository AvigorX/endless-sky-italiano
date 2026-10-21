# STATO — L211 · `coalition news.txt` (sesto e **ultimo** lotto) — **FILE CHIUSO**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L211_20261019_213549` |
| Righe / unità | **401–496** / **16** — file a **112/112 (100%)** |
| Tipi | {'NEWS': 16} |
| Tab · virgolette · apici | **0** · **22** · **6 EN / 14 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **4** — games planet heliarch 1, games planet people 4, fangvin 6, lunarium 5 |
| Parole | **378 EN → 352 IT** (rapporto 0,98–1,32, media 1,09) |
| sha256 | `2a3bcc367bdd3978…` |
| Esiti | `check.py` **25** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Il tratto del lotto: una citazione spezzata su sei unità

Le unità **6** e **11** sono **una sola virgoletta doppia** ciascuna. La citazione si apre alla riga **458** e si chiude
alla **465**, con quattro paragrafi in mezzo (7–10) che **non** portano virgolette.

È il primo caso della campagna in cui una citazione occupa più unità: la tentazione è «normalizzare» mettendo le
virgolette a ogni paragrafo, ma cambierebbe la resa a schermo. Il controllo verifica:

- 22 virgolette con distribuzione **per unità** `2,2,2,2,2,1,0,0,0,0,1,2,2,2,2,2` in entrambe le lingue;
- le unità 6 e 11 **esattamente** `"` nei due sensi;
- le unità 7–10 **senza** virgolette.

## Perché è un lotto terminale

L'ultima unità del file è la riga **496** e `line > 496` vale **0**. Il `verify.py` usa l'**invariante di FILE**: le sei
finestre (L206 20, L207 17, L208 19, L209 21, L210 19, L211 16) devono coprire tutte le **112** righe del database, senza
buchi e senza sovrapposizioni.

| finestra | righe | unità |
|---|---|---|
| L206 | 28–94 | 20 |
| L207 | 95–176 | 17 |
| L208 | 177–246 | 19 |
| L209 | 247–308 | 21 |
| L210 | 309–400 | 19 |
| L211 | 401–496 | 16 |
| **totale** | **28–496** | **112** |

## Cosa contiene

La coda dei Giochi della Coalizione (un ex atleta, famiglie con bambini, chi tifa per un parente), il filone del libro
**'Beyond the Hyperdrive'** di **Anna Fangvin** — un'umana letta da un Saryd — e le cinque voci dell'opera di beneficenza
del **Lunarium**, che raccoglie donazioni per i mondi Kimek poveri con la mediazione delle Case Arach.

## Difficoltà

1. **La citazione spezzata** (6/11): struttura del file, non del testo.
2. **Il titolo del libro resta inglese** fra apici singoli (`'Beyond the Hyperdrive'`, due volte) e il nome proprio
   `Anna Fangvin` resta invariato: il controllo dei «residui inglesi» li **esclude**, perché sono testi da conservare.
3. **Il marcatore del registro non riconosceva `l'ho`**: la regex dei token spezza sull'apostrofo e il verbo finiva
   troncato. Aggiunto alla lista dei verbi finali.
4. **«Arach Houses» → «Case Arach»**: istituzione, come «our Houses» → «le nostre Case» in L209.
5. **Tre eccezioni al marcatore**, tutte dichiarate: le due unità strutturali (6 e 11, senza testo) e l'unità 9, che
   chiude con «gioia» come il sorgente chiude con *joy*.

## Verifica

```bash
cd staging/editorial/L211_20261019_213549
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 (19 controlli) · FILE CHIUSO 112/112
```

**Non verificato**: nessuna schermata del notiziario vista, nessuna revisione umana; 16 unità `PENDING`.
