# REPORT — L226 · `remnant outfits.txt` (quarto lotto)

## 1. Contenuto

Nove equipaggiamenti. Il **Research Laboratory**, base operativa per studiare fenomeni alieni e stellari sul posto. La
**Quantum Key Stone**, l'artefatto che sintonizza le oscillazioni quantistiche di una nave per attraversare certi wormhole
dell'Ember Waste. Il **Salvage Scanner**, nato dai sistemi di guida dei Point Defense Turrets trovati nelle camere di
Aventine. Il **Bellows-Class Afterburner**, che incarna la filosofia dei Remnant — il carburante si usa quando serve, ma
prima viene la vita —, e la famiglia dei motori: **Anvil-Class Engine** (propulsione e sterzata in un'unità sola),
**Crucible-Class Thruster** (gas ionizzato a una frazione della velocità della luce), **Forge-Class Thruster** (più potente e
più avido di energia), **Smelter-Class Thruster** (che può assorbire più dei sistemi d'arma) e **Crucible-Class Steering**.

## 2. Difficoltà

1. **Zero virgolette, e l'ho scritto.** È la prima volta in molti lotti che il lotto non ne contiene nessuna. Un `0` non
   asserito non è un fatto: il controllo lo verifica in entrambe le lingue, e fallirebbe se ne comparisse una.
2. **Tre conteggi di tab diversi in tre lotti consecutivi**: 9 (L224), 4 (L225), **3** (L226). Stesso file, stessa natura di
   testo, struttura diversa. La densità si misura sul lotto, non si porta dietro.
3. **Nove contesti su undici unità.** Solo due equipaggiamenti hanno due schede; gli altri sette una. Il controllo verifica
   che le coppie siano esattamente due — non ne inventa per abitudine.
4. **`little more than a closet`** → «poco più di un armadio»: è un giudizio di chi guarda da fuori, e va tenuto nel registro
   giusto — non «ripostiglio», che sarebbe più neutro di quanto il testo dica.
5. **`At the end of the day, it is continued life that is paramount`** → «In fin dei conti, ciò che conta è continuare a
   vivere»: `continued life` non è «vita continuata»; è la sopravvivenza come valore primo della filosofia dei Remnant.
6. **`reluctant to waste fuel … aren't afraid of using it`** → «restii a sprecare … non temono di usarlo»: la frase è
   costruita su un'opposizione, e in italiano richiede il «da un lato / dall'altro» per non perdere il ritmo.
7. **`the Remnant mostly use them`** — plurale in inglese, riferito ai sistemi di sterzata. In italiano il referente della
   frase è «questo sistema», quindi «lo usano»: differenza dichiarata, non svista.
8. **I tre punti** dell'unità 9 restano tre punti (`...`), non un carattere `…`: il controllo lo verifica.

## 3. Numeri osservati

```
unita' 11 · {'DESCRIPTION': 11} · tutte PENDING
3 tab (unita' 1, 4, 6) · ZERO virgolette in EN e IT · 3 apici EN / 8 IT · 0 segnaposto
9 contesti su 11 unita' · righe 675/864 · 36 prima (L223-L225) · 10 dopo · confine riga 884 DESCRIPTION
0 unita' identiche all'inglese, 11 tradotte
parole 445 -> 447 · rapporto 1.00 - 1.21 (media 1.08)
FAIL totale: 0 (26 controlli) · verify exit 0 (19 controlli) · sha256[:16] 7418d831f5d6ba86
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (26), `verify.py` exit **0** (19) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 11 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessun equipaggiamento visto nel gioco**: la resa del research laboratory e dei motori è testuale.
- Restano **10 unità** nel file, tutte dopo la riga 864: **L227 è terminale** e chiuderà `remnant outfits.txt` a **57/57**,
  con **1 `VALUE` da copiare** (riga 948, `Void Sprite Parts`).
