# REVIEW — L140 · `data/hai/unfettered 0 prologue.txt` (primo contatto)

Coppie EN→IT rilette in `translation.json` (`ed2e17388b122b8f…`). Tutte le 25 unità sono **`PENDING`**.

## 1. Voce

- **Gli Slegati** parlano per assoluti e per mito: «Non sono veri Hai. Noi siamo gli Hai. Gli inalterati. Eravamo
  padroni di cento mondi quando le scimmie umane non avevano ancora imparato a usare i pollici.»
- **Il disprezzo** è lessicale, non gridato: chiamano il giocatore «la scimmia», sempre al singolare e in terza persona
  («la scimmia è curiosa»).
- **Il giocatore** ha la voce asciutta dei menu di scelta: «"Hai? È così che vi chiamate?"», «"Perché mi avete
  sparato? Siete in guerra?"».
- **La narrazione** resta al presente e al «tu», con un solo verbo espressivo: «Sibila.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `giant, intelligent squirrels` | **scoiattoli giganti e intelligenti** | 1 |
| `the monkey is curious` | **la scimmia è curiosa** | 4, 11 |
| `a true Hai` · `'true Hai'` | **un vero Hai** · **'veri Hai'** | 4, 6, 13 |
| `They hiss` | **Sibila** | 15 |
| `the unaltered` · `Hai the conquerors` | **gli inalterati** · **gli Hai conquistatori** | 15–17, 20, 23 |
| `We fight to defend ourselves from extinction` | **Combattiamo per difenderci dall'estinzione** | 18, 21 |
| `your brethren` | **i tuoi simili** | 12 |
| `Unaltered. The conquerors.` | **Inalterati. I conquistatori.** | 20, 23 |

## 3. Nodi aperti (da non dedurre dopo)

1. **Il motto è una costante**: cinque occorrenze, quattro costruzioni. Se un revisore ne cambia una, le altre quattro
   restano e la litania si rompe.
2. **Le due scelte ripetute devono restare identiche**: `(Certo.)` e `(Non ora, è troppo rischioso.)` compaiono in due
   rami della stessa missione.
3. **`monkey` è un insulto, non un errore**: va reso «scimmia» e non addolcito in «umano» o «terrestre».
4. **Le virgolette singole interne** (`'veri Hai'`) non contano come doppie: il conteggio per unità è 2, non 4.
5. **La sgrammaticatura del sorgente** (`Although despite`) resta: «Sebbene, nonostante».
6. **`Hai` non si traduce e non si declina**: «gli Hai», «un vero Hai», «degli Hai».

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 25 unità restano `PENDING`.
- **Nessuna missione giocata**: il primo contatto non è stato visto a schermo.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è al 17,0%**: 122 unità da fare in quattro missioni.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (25 controlli, invariante di segmento) |
