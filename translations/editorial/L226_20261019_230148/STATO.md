# STATO — L226 · `remnant outfits.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L226_20261019_230148` |
| Righe / unità | **675–864** / **11** — file a **47/57 (82,5%)** |
| Tipi | **11 `DESCRIPTION`** — nient'altro |
| Tab · virgolette · apici | **3** (unità 1, 4, 6) · **0** · **3 EN / 8 IT** |
| Segnaposto | **0** |
| Contesti | **9** su 11 unità — solo Salvage Scanner e Bellows-Class Afterburner ne hanno due |
| Parole | **445 EN → 447 IT** (1,00–1,21, media 1,08) |
| sha256 | `7418d831f5d6ba86…` |
| Esiti | `check.py` **26** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Zero virgolette: asserzione su un numero zero

Per la prima volta in molti lotti il lotto **non contiene virgolette**, né in inglese né in italiano. L'ho scritto come
asserzione esplicita (`== 0` in entrambe le lingue): un controllo che tace su uno zero non distingue «non ce ne sono» da
«non le ho guardate».

## I tab: 3, dopo 4 e dopo 9

| lotto | tab |
|---|---|
| L224 | 9 |
| L225 | 4 |
| **L226** | **3** |

Tre numeri diversi in tre lotti consecutivi dello stesso file. La struttura si conta **sul lotto in lavorazione**: ereditare
il conteggio precedente avrebbe prodotto o tab inventati o tab mancanti.

## Nove contesti su undici unità

Solo **Salvage Scanner** e **Bellows-Class Afterburner** hanno due unità ciascuno; gli altri sette equipaggiamenti ne hanno
una. Nei lotti precedenti le coppie erano la norma e il controllo le confrontava; qui il controllo verifica che le coppie
siano **esattamente due** e non ne inventa altre.

## Cosa contiene

Il **Research Laboratory** (la base operativa per studiare i fenomeni sul posto), la **Quantum Key Stone** (l'artefatto che
sintonizza le oscillazioni quantistiche per attraversare certi wormhole), il **Salvage Scanner** (nato dai sistemi di guida
dei Point Defense Turrets di Aventine), il **Bellows-Class Afterburner** (la filosofia dei Remnant: il carburante si usa
quando serve, ma la vita viene prima) e la famiglia dei motori — **Anvil-Class Engine**, **Crucible-Class Thruster**,
**Forge-Class Thruster**, **Smelter-Class Thruster** — con la **Crucible-Class Steering**.

## Difficoltà

1. **`little more than a closet packed with scanners and equipment`** → «poco più di un armadio stipato di scanner e
   attrezzature»: `closet` è dispregiativo, e «armadio» lo rende senza esagerare.
2. **`having advanced equipment … as well as a trained scientist`** → «disporre di attrezzature avanzate … e di uno
   scienziato addestrato»: la costruzione `amount to a strong benefit` diventa «è un vantaggio notevole».
3. **`unraveled the alien Point Defense Turrets`** → «decifrarono il funzionamento dei Point Defense Turrets alieni»: il
   nome dell'equipaggiamento resta inglese, il verbo no.
4. **`the stones are rare and valuable`** → «Le pietre sono rare e preziose»: `Quantum Key Stone` è il nome e resta, ma la
   prosa parla di «pietre».
5. **`reluctant to waste fuel, they aren't afraid of using it when needed`** → «se da un lato sono restii a sprecare
   carburante, dall'altro non temono di usarlo quando serve»: la contrapposizione richiede il «da un lato / dall'altro».
6. **`At the end of the day, it is continued life that is paramount`** → «In fin dei conti, ciò che conta è continuare a
   vivere»: rende l'idea di `continued life` senza il calco «vita continuata».
7. **`great leaps of acceleration`** → «grandi balzi di accelerazione».
8. **`only the most specialized of ships`** → «solo le navi più specializzate».
9. **`the basic ion thruster design`** → «il progetto di base del propulsore ionico».
10. **I tre punti dell'unità 9** restano tre punti (`...`), non un carattere `…`: verificato.
11. **`the Remnant mostly use them`** (plurale, riferito ai sistemi di sterzata) → «i Remnant lo usano», singolare, perché in
    italiano il referente della frase è «questo sistema». La differenza è dichiarata.

## Verifica

```bash
cd staging/editorial/L226_20261019_230148
python check.py     # FAIL totale: 0 (26 controlli)
python verify.py    # FAIL: 0 (19 controlli) · 47/57 · 10 dopo la 864 · confine 884
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 11 unità `PENDING`.
