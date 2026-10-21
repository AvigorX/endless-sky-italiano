# REVIEW — L96 · `coalition culture conversations.txt` (quarto lotto)

Coppie EN→IT rilette in `translation.json` (`0c863a3843dd5f4e…`).

## 1. Voce e registro

- **La Kimek organizzatrice** parla invertito come nei lotti precedenti («Honored to have you fight alongside
  us, our company is»), ma con un tono più tecnico: regole, tempi, confini. Unità con voce marcata: **6, 7, 26**.
- **Il narratore resta piano**: le tre cariche e i tre esiti sono descritti con frasi brevi, senza enfasi.
- **Il giocatore è «voi»**; nessuna forma che presupponga il genere.
- **L'organizzatore del congedo** (26) è maschile, **l'organizzatrice** della difesa è femminile: il sorgente
  alterna «he» e «she» e la traduzione lo segue.

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità | nota |
|---|---|---|---|
| `war tent` | **tenda da guerra** | 6 | fra virgolette |
| `gambeson` | **farsetto imbottito** | 5 | veste imbottita medievale |
| `battering ram` | **ariete** | 4, 6, 14, 21 | termine tecnico |
| `set` | **gruppo** | 6, 18 | fra virgolette, come in L94 |
| `groundlocked people` | **voi legati al suolo** | 6 | battuta bonaria |
| `soupy, half-digested mess` | **poltiglia brodosa e parzialmente digerita** | 24 | descrizione del giocatore |
| `bust the gate open` | **sfondare il cancello** | 13, 14, 20, 21 | verbo ricorrente |
| `latecomers of the main force` | **gli ultimi della forza principale** | 14, 21 | chi arriva con l'ariete |

## 3. Nodi aperti (da non dedurre dopo)

1. **Le cinque etichette di salto** (`defend ww`, `attack w`, `attack wr`, `attack r`, `attack rr`) restano
   identiche: sono i bersagli dei `goto` per i rami della battaglia.
2. **Il paragrafo dell'assalto** (unità 14 e 21) è identico per costruzione: una modifica va fatta nella
   costante `RAM` di `mkparts.py`.
3. **Il finale dei rami 16 e 23** distingue chi vince: non sono varianti stilistiche, sono esiti diversi.
4. **La battuta sul «legati al suolo»** è involontariamente scortese: la Kimek si corregge da sola. Non va
   ammorbidita, è caratterizzazione.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 27 unità restano `PENDING`.
- **Nessun caricamento nel gioco**: nessuna di queste scene è stata vista a schermo.
- **Nessuna revisione umana**: il lotto non è approvato.
- **Il file non è chiuso**: 36 unità restano (righe 251–462).

## 5. Rischi residui

- **Sei rami con testi lunghi e simili** (14/16/18/21/23): il rischio è che una revisione ne «uniformi» due che
  il sorgente tiene distinti. Le coppie identiche (14/21) e le divergenti (16/23) sono dichiarate.
- **Unità 6** ha 12 virgolette: una resa che unisse due battute passerebbe il totale del lotto ma sbaglierebbe
  la scena.
- **`ariete`** è usato sia per il tronco sia per la squadra che lo porta: in italiano funziona, ma va tenuto
  presente in revisione.

## 6. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28 controlli), `verify.py` exit **0** (29 controlli) |
