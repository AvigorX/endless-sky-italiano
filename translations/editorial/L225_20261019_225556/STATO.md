# STATO — L225 · `remnant outfits.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L225_20261019_225556` |
| Righe / unità | **581–674** / **11** — file a **36/57 (63,2%)** |
| Tipi | **11 `DESCRIPTION`** — nient'altro |
| Tab · virgolette · apici | **4** (unità 2, 4, 6, 10) · **2** (unità 8, le «branchie») · **3 EN / 15 IT** |
| Segnaposto | **0** |
| Contesti | **7** — Millennium/Epoch/Aeon Cell 2 a testa, NDR-114 Android 2, gli altri 1 |
| Parole | **455 EN → 461 IT** (1,04–1,15, media 1,09) |
| sha256 | `66b157150c05ada7…` |
| Esiti | `check.py` **25** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## Ancora zero unità da copiare, ma i tab dimezzati

Secondo lotto consecutivo senza niente da copiare (11 `DESCRIPTION` su 11). Ma **i tab scendono da 9 a 4** (unità 2, 4, 6,
10): la densità di L224 non si eredita. Ogni numero di struttura va **contato** sul lotto in lavorazione, perché il file —
non il lotto precedente — è la fonte.

## La famiglia di «ion», resa in quattro forme

Il tema del lotto è l'energia dei Remnant, e la parola `ion` compare in quattro costrutti che vanno tenuti distinti:

| inglese | italiano | unità |
|---|---|---|
| *ionization* | «ionizzazione» | 2 |
| *ion dissipation effects* | «effetti di dissipazione ionica» | 4 |
| *ion resistance* | «resistenza ionica» | 6 |
| *ion storms* | «tempeste ioniche» | 6 |
| *the storm* (senza aggettivo) | «la tempesta» | 6 |

La ripetizione di «ionica» è limitata a **2** occorrenze, e il controllo la misura: se l'aggettivo fosse stato ripetuto a
ogni menzione, la scheda sarebbe diventata illeggibile.

## Le «branchie» fra virgolette

L'unica coppia di virgolette del lotto è nell'unità 8: *due to their "gills," which are effectively built-in ramscoops* →
«grazie alle loro "branchie", che sono in pratica dei ramscoop integrati». Le virgolette segnalano che «branchie» è un
soprannome, non un termine tecnico — e restano dritte, come nel sorgente.

## Cosa contiene

Le tre celle di alimentazione (la **Millennium Cell** radiotermica, la **Epoch Cell** che converte quasi tutto il calore in
elettricità, la **Aeon Cell** nata dalla diffidenza verso i reattori nucleari umani), il **Thermoelectric Cooler** che è una
cella al contrario, l'**Emergency Ramscoop** per chi viaggia nell'Ember Waste con navi non dei Remnant, l'**NDR-114 Android**
mai concesso in licenza e il **Research Laboratory** che si espande in un locale della nave.

## Difficoltà

1. **`isotopes so radioactive, and so tightly packed together, that it could almost be classified as a nuclear reactor`** →
   «isotopi così radioattivi, e così strettamente addensati, da poter quasi essere classificato come reattore nucleare».
2. **`finicky and unpredictable nuclear reactors`** → «reattori nucleari capricciosi e imprevedibili».
3. **`radioisotope thermoelectric power`** → «energia termoelettrica a radioisotopi»: tre parole tecniche in fila, e ognuna
   ha un corrispettivo fisso.
4. **`wired so it can run in reverse`** → «collegato in modo da funzionare al contrario»: è un cablaggio, non un software.
5. **`their "gills," which are effectively built-in ramscoops`** → «le loro "branchie", che sono in pratica dei ramscoop
   integrati». `ramscoop` resta invariato.
6. **`without fear of getting stranded`** → «senza timore di restare bloccata»: `stranded` è rimanere a secco di carburante
   per l'iperspazio, non «naufragare».
7. **`lack of autonomous capabilities and economic benefit`** → «mancanza di capacità autonome e di vantaggio economico»:
   `economic benefit` è il ritorno per il produttore, non il prezzo.
8. **`take part in boarding actions`** → «partecipare ad azioni di abbordaggio»: `boarding` è l'arrembaggio, il termine già
   usato in L205 («arrembaggi» per `boarders`).
9. **`a fully fledged laboratory`** → «un laboratorio a tutti gli effetti».

## Un errore mio, corretto prima di chiudere

Il controllo sulla famiglia di «ion» pretendeva anche la forma singolare **«tempesta ionica»**, che nel testo non compare:
l'unità 6 dice «dalle tempeste ioniche» e poi «dalla tempesta», senza ripetere l'aggettivo. `FAIL 1`; il controllo ora
verifica le forme realmente presenti e il conteggio **2** di «ionica», che è la misura della non-ripetizione.

## Verifica

```bash
cd staging/editorial/L225_20261019_225556
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 (18 controlli) · 36/57 · 21 dopo la 674 · confine 675
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 11 unità `PENDING`.
