# REPORT — L209 · `coalition news.txt` (quarto lotto)

## 1. Contenuto

Ventuno voci. Nove sono **tre testi ripetuti tre volte** sotto contesti civilian diversi (Arach, Kimek, Saryd): lo stesso
commento sull'arresto dei terroristi, sull'ora del giorno nelle trasmissioni e sulla partenza di un amico per Ring of
Wisdom, attribuito a tre specie diverse. Le altre dodici sono specifiche: un mercante che invidia i jump drive, un
fratello diventato Heliarch, le Case confuse dai turisti, una sorella che impara l'Arachi, i bambini che si arrampicano,
e un venditore con dolci, arazzi e portachiavi.

## 2. Difficoltà

1. **Nove unità sono tre stringhe per tre.** La resa deve essere identica dentro ogni famiglia, e le famiglie devono
   coincidere fra inglese e italiano. Il `check.py` costruisce le partizioni per testo e le confronta: se una copia
   divergesse, il raggruppamento cambierebbe e il controllo cadrebbe. Non è una verifica «a occhio», è una verifica
   strutturale.
2. **Il registro Saryd si applica anche a chi non è Saryd.** L'unità 8 è di un civile Arach, la 13 di un civile Saryd,
   la 19 di un venditore: la cadenza è quella della Coalizione, non della specie. Ho mantenuto l'inversione in tutte le
   21 unità, perché tutte sono discorso diretto.
3. **Le eccezioni al marcatore sono quattro, non una.** 17 unità chiudono con un verbo flesso; la famiglia 5/10/15 chiude
   con «mai...» (il sorgente chiude con *never can...*), e l'unità 21 con «crediti!» (*credits!*). Il controllo nomina
   tutte e quattro invece di limitarsi a contare.
4. **Due asserzioni mie sbagliate.** La prima: davo per scontato che i contesti civilian avessero il prefisso
   `coalition`; il database dice `arach civilian`, `kimek civilian`, `saryd civilian`. La seconda: cercavo `'field trip'`
   mentre il testo inglese ha `'field trip,'` — la virgola sta **dentro** le virgolette. In entrambi i casi ho corretto
   l'asserzione, non il testo; la seconda ora verifica anche che gli apici siano **due per lato** nelle due lingue.

## 3. Numeri osservati

```
unita' 21 · {'NEWS': 21} · tutte PENDING
0 tab · 42 virgolette (2 per unita') · 2 apici EN / 7 IT · ZERO segnaposto
5 contesti · righe 247/308 · 56 prima · 35 dopo · confine riga 309 (stesso contesto)
famiglie: 4/9/14, 5/10/15, 6/11/16 — identiche nelle due lingue, nessuna copia divergente
parole 432 -> 450 · rapporto 0.93 - 1.26 (media 1.09)
FAIL totale: 0 (24 controlli) · verify exit 0 (19 controlli) · sha256[:16] 7e550942341d014e
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (24), `verify.py` exit **0** (19) |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 21 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna schermata vista**, **nessuna revisione umana**: il registro resta una proposta.
- **Restano 35 unità** in questo file (836 parole): L210 e L211, che chiuderà `coalition news.txt`.
