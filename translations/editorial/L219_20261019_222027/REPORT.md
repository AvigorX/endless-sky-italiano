# REPORT — L219 · `successor ships.txt` (secondo lotto)

## 1. Contenuto

Tre navi dei Successori: la **Kvelqde** (la navetta minuscola con cui i nuovi piloti fanno le prime armi), la
**Kvelqde-Khora** (la versione irrobustita dalle **Case del Popolo**, con placche aggiuntive, una seconda feritoia e la
rete di scudi potenziata, buona per una pirateria leggera) e la **Myaede** (il cargo che regge il commercio dei
Successori da prima del crollo del vecchio impero). Kvelqde e Myaede hanno **due descrizioni ciascuna**.

## 2. Difficoltà

1. **Solo 6 unità su 25 si traducono.** Le altre 19 sono nomi (`TEXT` di equipaggiamento e `VALUE` di specie) da copiare
   alla lettera: il rischio qui non è tradurre male, è **tradurre ciò che non va tradotto**. Il `check.py` confronta unità
   per unità e il `verify.py` fissa «19 identiche, 6 tradotte, e le 6 sono esattamente le `DESCRIPTION`».
2. **Le due descrizioni della stessa nave si ripetono.** Kvelqde: 7 e 9 aprono con la **stessa frase**. Myaede: 24 e 25
   condividono «né elegante né veloce» e la formula sulle armi. Ho tradotto le frasi una volta e le ho riusate identiche,
   altrimenti la stessa nave direbbe due cose diverse in due schermate. Il controllo confronta il prefisso e le due
   formule.
3. **`grandparent's watchful gaze`** → «sotto lo sguardo vigile di un nonno»: il possessivo inglese non ha genere, e
   l'italiano deve sceglierne uno. «Nonno» è la scelta, e resta dichiarata.
4. **`low-born Successors`** → «Successori di umili origini»: non «plebei», che è un termine di casta che il testo non usa.
5. **`bares enough teeth for a bit of light piracy`** → «mostra abbastanza denti per un po' di pirateria leggera»:
   l'understatement è il tono della scheda e va conservato.
6. **`hands` / `arms`**: l'inglese dice *get their arms on*; la resa «riuscire a metterci le mani» resta sull'accesso,
   senza introdurre un'arma che il testo non nomina.

## 3. Numeri osservati

```
unita' 25 · {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 3} · tutte PENDING
1 tab (unita' 8) · 32 virgolette (2 x 16) · 3 apici EN / 10 IT · 0 segnaposto
3 contesti: Kvelqde 9, Myaede 9, Kvelqde-Khora 7
righe 386/629 · 45 prima (L218) · 76 dopo · confine riga 634 (VALUE, cinque righe dopo)
19 unita' identiche all'inglese, 6 tradotte (le DESCRIPTION)
parole 467 -> 487 · rapporto 1.00 - 1.16 (media 1.02)
FAIL totale: 0 (27 controlli) · verify exit 0 (16 controlli) · sha256[:16] 26062019d4d6d536
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (27), `verify.py` exit **0** (16) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 25 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna nave vista nel gioco**, nessuna schermata di allestimento aperta.
- Restano **76 unità** nel file (50 dopo la riga 873): L220 riparte dalla 634.
