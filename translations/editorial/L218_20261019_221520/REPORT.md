# REPORT — L218 · `successor ships.txt` (primo lotto, file nuovo)

## 1. Contenuto

Le schede di **quattro navi dei Successori**: l'**Aaulqra**, il progetto di nave da guerra più antico ancora prodotto
dalle **Alte Case**; l'**Ejniisde**, il trasporto passeggeri per i viaggi lunghi; l'**Ejniisde-Khora**, la versione
militarizzata e illegale allestita dalle **Case del Popolo**; la **Kaskhorade**, spina dorsale pesante e polivalente delle
flotte.

## 2. Difficoltà

1. **Il lotto è quasi tutto «da copiare».** Su 45 unità, **39 restano identiche all'inglese**: 35 `TEXT` che sono nomi di
   equipaggiamento (`"Ojet" Bimodal Coilgun`, `"Sjeja" Kinetic Lance`, `OC-"Mavra" Betavoltaic Cell`) e 4 `VALUE` che
   sono nomi di specie. Si traducono **solo le 6 `DESCRIPTION`**. Il rischio non è sbagliare la traduzione: è
   **tradurre per riflesso** un'unità che non va toccata, o copiarne una che andava tradotta. Il `check.py` confronta
   testo per testo, non a campione.
2. **La regola si decide dal contenuto, non dall'etichetta.** In `coalition news.txt` i `TEXT` erano citazioni e si
   traducevano; qui sono nomi. Il `verify.py` fissa il numero: **39 identici / 6 tradotti**, e le 6 tradotte devono essere
   esattamente le `DESCRIPTION`.
3. **Nomi composti**: `6-"Ruuv"`, `1-"Uurau"`, `OC-"Mavra"`, `"Ej"`. Prefisso numerico e sigla restano attaccati al
   nome, e le virgolette interne fanno parte del nome: 70 virgolette in 35 unità, due per unità.
4. **Terminologia politica**: `High Houses` → **Alte Case**, `People's Houses` → **Case del Popolo**, `Successors` →
   **Successori**. Sono nomi di istituzioni, quindi si traducono; il controllo verifica che l'inglese `High Houses` non
   resti nel testo.
5. **Apici in unità diverse fra le due lingue.** La mia prima asserzione pretendeva le stesse tre unità in inglese e in
   italiano, ed è caduta: in inglese gli apici stanno in 15, 31 e **32**; in italiano in 15, 31 e **45**. Il totale
   coincide per caso (4 e 4), la distribuzione no. Corretto il controllo con i conteggi per unità.
6. **`star liner` → «nave di linea»**, `barracks` → «camerate», `multi-layered armor` → «corazzatura multistrato».

## 3. Numeri osservati

```
unita' 45 · {'TEXT': 35, 'DESCRIPTION': 6, 'VALUE': 4} · tutte PENDING
1 tab (unita' 32) · 70 virgolette (2 x 35) · 4 apici EN / 4 IT · 0 segnaposto
4 contesti: Aaulqra 16, Kaskhorade 13, Ejniisde-Khora 9, Ejniisde 7
righe 17/381 · 0 prima (primo lotto) · 101 dopo · confine riga 386 (VALUE, cinque righe dopo)
39 unita' identiche all'inglese, 6 tradotte (le DESCRIPTION)
parole 499 -> 549 · rapporto 1.00 - 1.15 (media 1.02)
FAIL totale: 0 (28 controlli) · verify exit 0 (17 controlli) · sha256[:16] 9e3e6ea15d7e3638
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (17) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 45 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna nave vista nel gioco**: i nomi di equipaggiamento non sono stati osservati nella schermata di allestimento,
  quindi l'ipotesi «sono nomi mostrati e non prosa» è coerente col file ma **non verificata nel runtime**.
- Restano **101 unità** nel file: L219 riparte dalla riga 386.
