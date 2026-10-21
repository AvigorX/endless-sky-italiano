# REPORT — L127 · `incipias first contact.txt` (il traduttore dei Quarg, il primo contatto, la stazione)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| il `VALUE` e la descrizione | 1–2 | 224–225 | nome e descrizione della missione |
| il Quarg e la richiesta | 3–23 | 233–265 | l'incontro sul pianeta, la richiesta di aiuto, le due obiezioni, il divieto di dare tecnologia |
| il traduttore | 24–36 | 270–289 | il diario, la scatola d'argento, le istruzioni, l'avvertimento, l'insistenza |
| il primo messaggio | 37–46 | 294–305 | la trasmissione, l'attesa, il canale che si apre, la mappa |
| la stazione | 47–53 | 307–315 | i due diari, i tubi pieni di nebbia, i cinque davanti alla folla |
| le domande degli Incipias | 54–63 | 316–331 | «sei l'unico essere-esterno?», la nave bloccata, l'acquisto |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Seek help from the Incipias` | **identico** | `VALUE`, nome di missione |
| `this one` | **questo uno** | terza persona del Quarg, 7 volte |
| `world-traveler` | **viaggiatore-di-mondi** | composto con trattino |
| `intention-goal` | **intenzione-scopo** | |
| `capital-station` | **stazione-capitale** | |
| `outer-being` | **essere-esterno** | |
| `far-stranger` | **straniero-lontano** | |
| `not-danger` | **non-pericolo** | «renderti un non-pericolo» |
| `situation-opportunity` | **situazione-opportunità** | |
| `air-planet` | **pianeta-d'aria** | il gigante gassoso |
| `system-places` | **luoghi-sistema** | |
| `future-time` | **futuro-tempo** | |
| `out-question you more` | **interrogare-oltre voi** | |
| `interlopers` | **intrusi** | |
| `held council with` | **tenuto consiglio con** | |
| `nonplussed` | **perplesso** | |
| `dissemination` | **modo di diffondere i messaggi** | la comunicazione per luce |
| `clammy` · `tumultuous planets` | **turbolenti** | |
| `sleek silver box` | **scatola d'argento levigata** | |
| `clicks its teeth` | **batte rapidamente i denti** | |
| `hail` · `docking ports` | **richiesta di collegamento** · **portelli di attracco** | |
| `bulbous section` · `scale-like structures` | **sezione bulbosa** · **strutture simili a scaglie** | |
| `eight undulating, dexterous-looking tentacles` | **otto tentacoli ondulanti dall'aria abile** | |
| `airlock` | **portello** | coerente con L126 |

## 3. Difficoltà

1. **Un solo contesto per 63 unità**: nessun confine interno, il lotto è la scena intera. La cella `Contesti` degli
   handoff va scritta `da X a X` (il checker esige quattro backtick).
2. **`VALUE` unico** fra 62 testi prosaici: `VAL == [1]` più confronto stringa, non «tutti tranne».
3. **Due token in una sola unità** (38): parità per simbolo **e** per unità; lo dice il controllo, non la somma.
4. **98 virgolette**, nessuna unità dispari — qui il sorgente è simmetrico, al contrario dell'unità 23 di L126.
5. **Il Quarg usa due persone**: la terza (`this one`) e la prima plurale (`we`, `our wrath`). Entrambe restano, e il
   `check.py` pretende almeno sei «questo uno».
6. **Lo stile degli Incipias** non è prosa italiana: è un composto con trattino per concetto. Sei composti verificati.
7. **«Vi saluto»** è un **voi plurale** (gli Incipias sono una folla), non cortesia: il controllo vieta solo `Lei/lei`
   e i possessivi maiuscoli, e dichiara il perché. La prima stesura del controllo bocciava «Le tue intenzioni»
   perché prendeva l'articolo `Le` per cortesia.
8. **Gate**: minimo 0,65 (unità 5, «(Non ora.)»), massimo 1,36 (unità 33, «Certo. Lascia che faccia il lavoro.»).

## 4. Numeri osservati

```
unita' 63/63 · MISSION_TEXT 58 · LOGBOOK 3 · VALUE 1 (identico) · DESCRIPTION 1 · tutte PENDING
contesti 1 (63 unita) · testi distinti 63 · nessuna ripetizione
tab 55 unita · virgolette 98 (nessuna dispari) · token 2 (unita 38) · quadre 0
parole EN 1697 -> IT 1556 (0.917) · rapporto 0.65 - 1.36, media 1.01
righe 224/331 · file 118/161 (73,3%) · 55 prima / 43 dopo · confine riga 343
FAIL totale: 0 (30 controlli) · verify exit 0 (28 controlli)
sha256[:16] d811d1921f891627
```

## 5. Stato del progetto

```
TOTALE staging: 26944 unità · 854447 EN · 811902 IT
incipias first contact.txt: 118/161 (73,3%) · 2 lotti · 3485 EN -> 3182 IT
file completi: quarantacinque · residuo traducibile (formula state.py): 4986
residuo misurato: 5622 unità / 122545 parole su 121 file
avanzamento: 26944/32924 unità (81,8%) · 854447/979975 parole (87,2%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 63 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: restano **43 unità** (righe 343–439), in tre contesti.
- **Prossimo lotto**: `HANDOFF_L128_20261019.md` — la **coda** del file: `Fix Saves Missing Language` (2),
  `No Help For The Stranded` (1), `Help The Stranded 2` (40), righe **343–439**, **1.177 parole**. **Chiude il
  file**, quindi invariante di **file**.
