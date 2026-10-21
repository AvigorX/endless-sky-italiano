# review.md — L235 (`data/avgi/avgi news.txt`, righe 197–280)

Registro delle decisioni editoriali del **lotto di composizione**. Qui non si traduce una frase: si traducono i
**pezzi** che il motore incolla, e la qualità si misura sulla frase che ne esce.

## 1. La regola che governa il lotto

`source/Phrase.cpp` — `Phrase::Get()` concatena i blocchi scelti **senza aggiungere separatori**:

```cpp
for(const auto &part : sentences[Random::Int(sentences.size())]) {
    if(!part.choices.empty()) {
        const auto &choice = part.choices.Get();
        for(const auto &element : choice)
            result += element.second ? element.second->Get() : element.first;
    }
    ...
}
```

Tre conseguenze, tutte verificate dai due script:

| fatto | perché conta |
|---|---|
| i 6 prefissi finiscono con **uno spazio** | senza, il testo composto direbbe `"Cautela.Segnalato…"` |
| i 7 messaggi portano **punto e virgoletta in coda** | aggiungerli al prefisso darebbe due virgolette di apertura |
| nessun blocco aggiunge spazi da sé | lo spazio è sempre esplicito, quindi non va «normalizzato» |

Il controllo compone tutte le **42 combinazioni** (6 × 7) in inglese e in italiano e pretende, per ognuna: virgoletta in
testa, virgoletta in coda, **due** virgolette in tutto, etichetta chiusa da `. `, nessun doppio spazio, e mai una
minuscola dopo l'etichetta.

## 2. Le sei etichette del bollettino

| inglese | resa | nota |
|---|---|---|
| `Caution.` | **Cautela.** | |
| `Warning.` | **Avvertenza.** | distinta da `Alert` («Allarme»), come nell'inglese |
| `Advisement.` | **Avviso.** | è l'avviso neutro della scala; «Raccomandazione» sarebbe un consiglio, non un avviso |
| `Diligence.` | **Diligenza.** | l'inglese usa qui *diligence* come «attenzione scrupolosa»: «Prudenza» sarebbe una riscrittura |
| `Alert.` | **Allarme.** | |
| `Vigilance.` | **Vigilanza.** | |

Una nota di misura: `Avviso.` rende il rapporto dell'unità a **0,69**, cioè **dentro il gate** (0,55–1,90) ma appena
sotto la banda comoda (0,70–1,75), perché `Advisement.` è più lungo. L'alternativa che rientrerebbe nella banda
(«Raccomandazione.») cambierebbe il registro del bollettino: si tiene la parola giusta e si **dichiara** lo scarto
(precedente: L121, «Dispositivo di occultamento» a 1,80).

## 3. I sette messaggi

| inglese | resa |
|---|---|
| `Large Aberration swarm reported to have entered the Tangled Shroud.` | Segnalato un grande sciame di Aberrant entrato nel Tangled Shroud. |
| `Missing convoy reported; suspected stranded in the Tangled Shroud.` | Convoglio disperso; si sospetta bloccato nel Tangled Shroud. |
| `Missing convoy reported; suspected lost in the Tangled Shroud.` | Convoglio disperso; si sospetta perduto nel Tangled Shroud. |
| `Missing fleet reported; suspected stranded in the Tangled Shroud.` | Flotta dispersa; si sospetta bloccata nel Tangled Shroud. |
| `Missing fleet reported; suspected lost in the Tangled Shroud.` | Flotta dispersa; si sospetta perduta nel Tangled Shroud. |
| `The defensive cordon at Arche is not impenetrable. Remain vigilant.` | Il cordone difensivo di Arche non è impenetrabile. Restate vigili. |
| `Report all Aberration sightings as soon as possible.` | Segnalate ogni avvistamento di Aberrant il prima possibile. |

- Il participio segue il **genere del soggetto**: *convoglio* → bloccato/perduto, *flotta* → bloccata/perduta. Le
  quattro coppie non sono varianti stilistiche: sono accordi, e il controllo le confronta.
- **«Restate vigili»** è un imperativo plurale, non una cortesia: un bollettino parla alla popolazione, non al
  giocatore (decisione 36: il `voi` plurale non è cortesia).
- `Aberration` → **Aberrant** anche qui, come nei due lotti precedenti (decisione 25).
- `Tangled Shroud`, `Arche`: invariati.

## 4. Le due unità di punteggiatura

`news "avgi missing advisory"` inizia con un blocco che è **solo** `"` e finisce con un blocco che è **solo** `.`.
Sono unità del database, quindi si traducono: restano identiche **per necessità** e stanno in `ID_OK` con un controllo
dedicato (`== [14, 15]`, valori `"` e `.`). Non sono una deroga generale: un elenco di due indici.

## 5. La lacuna dell'inventario (dichiarata, non riparata)

Il `message` di `avgi missing advisory` è fatto di **tredici** blocchi `word` (misurati sul file, righe 229–280):

```
`"`  ·  "Caution." / "Warning." / "Alert."  ·  " "  ·  "Convoy" / "Fleet" / "Patrol" / "Independent ship" / "Scout"
     ·  " "  ·  "reported lost" / "reported missing" / …  ·  ", "  ·  "last sighted" / …  ·  " "
     ·  "leaving" / "entering" / "transiting"  ·  " "  ·  "the Ensemble system" / … / "Outpost Leto"  ·  `.`
```

Il database ne conserva **solo il primo e l'ultimo**. Le parole interne non esistono in `state.db`, quindi non sono
traducibili da nessun lotto e quella notizia resterà quasi tutta in inglese anche a staging completo.

**Perché non si ripara**: `tools/l10n.py` e `state.db` sono file protetti (hash nel manifest), e un lotto non scrive
nel database. La lacuna si documenta qui e si verifica in due modi indipendenti nel `verify.py`: una query
(`0 unità fra la riga 231 e la 279`) e una lettura del file del gioco (`Convoy` e `the Demilude system` presenti in
quell'intervallo). Quando l'inventario sarà rifatto, quelle sono le righe da aggiungere.

## 6. Struttura e tipografia

- **Zero tab**: nessun `MISSION_TEXT` in questo lotto.
- **Nessun segnaposto** `<...>`: asserzione negativa scritta.
- **Nessun apostrofo** in inglese né in italiano in tutto il lotto: il bollettino è nominale e impersonale.
- Il **punto finale sta dentro la virgoletta** (`… prima possibile."`): riprodotto.

## 7. Lacune dichiarate

- **Nessuna riga `log`**: il lotto non ne ha (0 `LOGBOOK`, fra le assenze di tipo).
- **`NT` vuoto per misura**: nessuna `UI_LABEL`, nessun riferimento di dato; il `check.py` lo scrive come asserzione.
- **La lacuna dei tredici `word`** (§5): non riparabile da un lotto.
