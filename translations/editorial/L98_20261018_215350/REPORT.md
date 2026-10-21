# REPORT — L98 · `hai culture conversations.txt` (primo lotto, tre contesti)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `Theater Chat` | 26–33 | 8 | umana e Hai davanti all'annuncio di un'opera; discussione sulle interpretazioni e sulla centottantatreesima versione |
| `Musical Entertainment Expo` | 47–69 | 16 | il bar dei tifosi, il cameriere, l'industria musicale Hai e la **ME2** |
| `The Meme Wars 1` | 83–105 | 15 | ologrammi, l'anziano triangolare contro l'ortaggio, il traduttore, la guardia e la battuta dei tre principi |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Gemanari`, `Alinta` | **invariati** | nomi propri (Hai e umana) |
| `Germontian interpretation` | **interpretazione germontiana** | scuola critica in-world, aggettivo dal nome dell'autore |
| `Social Darwinist interpretation` | **interpretazione darwinista sociale** | è la traduzione che l'umana dà del termine Hai |
| `Misheep Wah'uden company` | **compagnia Misheep Wah'uden** | nome proprio di una compagnia teatrale |
| `Musical Entertainment Expo` / `ME2` | **invariati** | nome dell'evento e acronimo di settore |
| `ripple ray refractive holographic flight effects` | **effetti di volo olografici a rifrazione con raggi ondulati** | gergo tecnico inventato ma trasparente |
| `sashes and mantles · paraphernalia` | **fasce, mantelli · accessori** | |
| `root vegetable` | **ortaggio a radice** | è il *meme*; non «rapa», che è una specie precisa |
| `true and square root` | **radice vera e quadrata** | il bisticcio su «square root» passa in italiano con «quadrata» |
| `[Victory, Success]` | **[Vittoria, Successo]** | la voce del traduttore elenca alternative fra quadre: riprodotte |
| `meme war`, `meme items` | **guerra di meme**, **oggetti dei meme** | |
| `the hundred and eighty-third version` | **la centottantatreesima versione** | |
| `pop music` | **pop music** | l'Hai parla di un genere terrestre: l'anglicismo è nel testo |

## 3. Difficoltà

1. **Le quadre del traduttore**: tre coppie nell'unità 30. In L97 il `check.py` asseriva *zero* quadre; qui
   l'asserzione è di **parità** (3 = 3) e di presenza nella sola unità 30 — un controllo copiato senza
   adattarlo avrebbe bocciato una traduzione corretta.
2. **Tre ripetizioni e una quasi-ripetizione**: 20/37, 27/31, 29/39 identiche, ma **28 e 32 differiscono per
   una virgola** (`meme items and no one` / `meme items, and no one`). Nel costruttore l'asserzione che
   confrontava i conteggi di virgole era **invertita** e ha fermato la build prima che scrivesse le parti.
3. **Tre contesti con voci diverse**: la coppia umana+Hai (conversazione colta fra due amiche), il cameriere
   stanco (registro colloquiale, «Beh, vede…»), la guardia di sicurezza (istituzionale, dà del «lei»).
4. **L'unità 25** è un paragrafo unico di 190 parole con quattro oggetti consecutivi (proiettori, striscioni,
   volantini, il meme che si scioglie): la resa tiene la sequenza e non spezza la frase.
5. **`<destination>`** compare una volta e indica il pianeta dove recita la compagnia preferita di Gemanari.

## 4. Numeri osservati

```
unita' 39/39 · tab 36 · virgolette 58 = 58 · token 1 = 1 · quadre 3 = 3 (unita 30)
parole EN 1262 -> IT 1180 · rapporto 0.89 - 1.50
righe 26/105 · file 147 unita · max(line) 386 · 0 prima / 108 dopo
FAIL totale: 0 (29 controlli) · verify exit 0 (28 controlli)
sha256[:16] 8df01d63f077d9a2 · copertura file 39/147 (26,5%)
```

## 5. Stato del progetto

```
TOTALE staging: 25183 unita · 807628 EN · 765528 IT
hai culture conversations.txt: 39/147 (26,5%) · 1 lotto
file completi: 38 · residuo traducibile (formula state.py): 6747
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | due parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (28 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 39 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: 108 unità restano su 10 contesti; il prossimo contratto è
  `HANDOFF_L99_20261018.md` (righe 106–211: `Wrestling Star`, `Fencing Star`, `Mystery Sport Star`,
  `Gambling Judgment`).
- **Tre `UI_LABEL`** vivono più avanti nel file (non in questo lotto) e andranno lasciate identiche.
- **Nessuna revisione umana**.
