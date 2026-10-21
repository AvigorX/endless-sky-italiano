# REPORT — L211 · `coalition news.txt` (sesto e ultimo lotto) — **file chiuso 112/112**

## 1. Contenuto

Sedici voci che chiudono il file: la coda dei Giochi (un ex atleta diventato organizzatore, famiglie con bambini, chi
tifa per un parente), il filone del libro **'Beyond the Hyperdrive'** di **Anna Fangvin** — un'umana letta e apprezzata
da un Saryd — e le cinque voci dell'opera di beneficenza del **Lunarium**, che porta beni essenziali nei mondi Kimek
poveri con il sostegno delle Case Arach.

## 2. Difficoltà

1. **La citazione spezzata è il problema strutturale del lotto.** Le unità 6 e 11 sono una sola virgoletta doppia
   ciascuna: la citazione si apre alla riga 458 e si chiude alla 465, e i quattro paragrafi centrali non hanno
   virgolette. La soluzione «pulita» — mettere le virgolette a ogni paragrafo — avrebbe cambiato la resa a schermo. Il
   controllo verifica la distribuzione **per unità** in entrambe le lingue, e che 6 e 11 siano **esattamente** `"`.
2. **Il lotto è terminale, quindi cambia il tipo di verifica**: non un confine, ma l'**invariante di file**. Le sei
   finestre devono coprire tutte le 112 righe del database. Una riga dimenticata fa cadere il controllo.
3. **Il marcatore del registro aveva un buco**: la regex dei token spezza sull'apostrofo, quindi «l'ho» non veniva
   riconosciuto come verbo e l'unità 7 risultava un'eccezione falsa. Aggiunto `l'ho` alla lista.
4. **Il controllo dei residui inglesi segnalava il titolo del libro**: «Beyond the Hyperdrive» contiene ` the `.
   Il titolo e il nome proprio vengono **esclusi esplicitamente** dalla scansione, perché sono testi da conservare, non
   residui.
5. **Tre eccezioni al registro**, tutte motivate: 6 e 11 non hanno testo; l'unità 9 chiude con «gioia» come il sorgente
   chiude con *joy*.

## 3. Numeri osservati

```
unita' 16 · {'NEWS': 16} · tutte PENDING
0 tab · 22 virgolette con distribuzione 2,2,2,2,2,1,0,0,0,0,1,2,2,2,2,2 · 6 apici EN / 14 IT · ZERO segnaposto
4 contesti · righe 401/496 · 96 prima · 0 dopo (fine file)
parole 378 -> 352 · rapporto 0.98 - 1.32 (media 1.09)
FAIL totale: 0 (25 controlli) · verify exit 0 (19 controlli) · sha256[:16] 2a3bcc367bdd3978
FILE CHIUSO: 112/112 righe distinte, nessun buco, nessuna sovrapposizione
```

## 4. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | `parts/part01.json`, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (25), `verify.py` exit **0** (19) con invariante di file |

## 5. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`, nessuna scrittura su `state.db`.
- **Nessuna schermata vista**, **nessuna revisione umana**.
- **Il file è completo in staging, non nel gioco**: `coalition news.txt` è tradotto al 100% e nessuna delle sue 112 unità
  è approvata.
