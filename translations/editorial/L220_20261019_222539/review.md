# REVIEW — L220 · `successor ships.txt` (terzo lotto)

Coppie EN→IT rilette in `translation.json` (`3373e098d9af319f…`). Tutte le 26 unità sono **`PENDING`**.

## 1. Regola di produzione: i nomi si copiano con il codice

Su 26 unità, **20 sono nomi** (16 `TEXT` di equipaggiamento, 4 `VALUE` di specie). Non vengono trascritti: `parts/part01.json`
si **genera** da `source.json`, prendendo `english` per ogni unità `TEXT`/`VALUE` e le mie traduzioni solo per le 6
`DESCRIPTION`. Il motivo è misurato: alla prima stesura avevo trascritto a mano e **11 unità su 20** erano sbagliate.

## 2. La coppia 23/25

| | inglese | italiano |
|---|---|---|
| 23 | …, the **"Ojde"** is still substantially smaller… | …, l'**"Ojde"** è comunque molto più piccolo… |
| 25 | …, the Ojde is still substantially smaller… | …, l'Ojde è comunque molto più piccolo… |

Togliendo le virgolette i due testi coincidono, in inglese e in italiano, e la differenza di lunghezza è **2** in entrambe le
lingue. L'elisione sta **fuori** dalle virgolette (`l'"Ojde"`), perché le virgolette citano il nome e non l'articolo.

## 3. Decisioni di resa

1. **`amphibious nature`** → «natura anfibia»; **`pressure-stable hull`** → «scafo … stabile alla pressione».
2. **`built-in maintenance systems`** → «sistemi di manutenzione integrati»; **`resistance to corrosion and slowing
   effects`** → «resistenza alla corrosione e agli effetti di rallentamento» (`slowing` è un effetto di gioco).
3. **`heavy and expensive ship for its size`** → «una nave pesante e costosa per le sue dimensioni»; **`well worth it`** →
   «ne valgano ampiamente la pena».
4. **`House Chydiyi's shipyards`** → «i cantieri della Casa Chydiyi»: la Casa si traduce, il nome no.
5. **`hotshot pilots swear by these ships`** → «alcuni piloti spericolati giurano su queste navi».
6. **`restrictive internals`** → «interni poco flessibili»: spazi di equipaggiamento limitati, non arredi.
7. **`luxury craft of some sort`** → «imbarcazioni di lusso di qualche tipo»: il testo è una **deduzione** di chi osserva,
   e la resa mantiene l'incertezza.
8. **`time-tested Myaede`** → «la collaudata Myaede»: riferimento alla scheda di L219, che usa la stessa nave.
9. **`assemble a large-scale transport operation`** → «mettere in piedi un'operazione di trasporto su larga scala».
10. **`facilities which can effectively tend to them`** → «strutture in grado di prendersene cura efficacemente»:
    `facilities` sono gli impianti dello spazioporto, come fissato nei lotti precedenti.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 26 unità `PENDING`.
- **Nessuna nave vista nel gioco**: la classificazione dei `TEXT` come nomi resta dedotta dal file.
- **Nessuna revisione umana**, **nessuna correzione al sorgente**.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (28), `verify.py` exit **0** (18) |
