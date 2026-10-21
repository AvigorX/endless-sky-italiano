# REVIEW — L146 · `unfettered 0 prologue.txt` (la porta che si chiude: verdetto e fine del file)

Coppie EN→IT rilette in `translation.json` (`7aaadc8a4d2d1252…`). Tutte le 19 unità sono **`PENDING`**.

## 1. Voce

- **Desneeparu** giudica senza appello: «Ti nascondi? Schivi? Ti rifiuti di impadronirti delle nostre armi, quindi non
  le avrai», «Non avresti mai potuto superarmi in velocità. Hai solo mostrato paura.»
- **L'ingegnere** resta burocratico anche nel rifiuto: «Dato che non hai superato la prova, non possiamo ancora darti
  accesso alla nostra camera blindata», e poi la promessa amministrativa del perdono: «Un altro ingegnere ti aspetterà
  al portello quando sarà il caso.»
- **La narrazione** è al presente e asciutta: «Si ferma all'ultimo istante possibile, con la delusione evidente sul
  volto.»

## 2. Decisioni di resa (verificate sul file)

| EN | IT | unità |
|---|---|---|
| `back to choose` · `buy tripulse` | **identiche** | 1, 8 |
| `<as before (run)> manage to dodge` | **`<as before (run)>` riesci a schivare** | 11 |
| `<as before (flee)> run away` | **`<as before (flee)>` fuggi** | 13 |
| `<leave> The engineer…` | **`<leave>` L'ingegnere…** | 17 |
| `here on <origin>` | **qui su `<origin>`** | 9 |
| `hit and run tactics` | **tattiche mordi e fuggi** | 7 |
| `a single gun slot` | **un solo alloggiamento per arma** | 7 |
| `our vault` | **la nostra camera blindata** | 17 |
| `bell'e pronta` (`so readily presented`) | **un'arma che ti era offerta bell'e pronta** | 15 |

## 3. Nodi aperti (da non dedurre dopo)

1. **`UI_LABEL` ≠ testo traducibile**: due label identiche, verificate in un controllo dedicato, e «tutte tradotte» le
   esclude **esplicitamente**. La differenza fra «dimenticata» e «dichiarata non traducibile» sta in quel controllo.
2. **`<as before (run)>` è un simbolo unico**: le parentesi non si tolgono e non si spezzano; il token resta il primo
   elemento della frase.
3. **Zero virgolette dispari**: in questo tratto il sorgente è bilanciato, e il `verify.py` lo dice invece di tacere.
4. **Il file è chiuso**: la prova non è «ho finito le righe», è `25+20+20+30+20+13+19 = 147` calcolato, con `max(line)`
   e zero sovrapposizioni.
5. **`data/human/news.txt` non è traducibile così com'è**: 164 unità su 202 sono il delimitatore `` `"` ``, e 1.356
   righe di frase non sono nel database. Sarebbe un lotto di sole virgolette.

## 4. Cosa NON è stato fatto (dichiarato)

- **Nessuna scrittura su `state.db`**: 19 unità restano `PENDING`.
- **Nessun motore scambiato** e nessuna lama schivata nel gioco.
- **Nessuna revisione umana**.
- **`unfettered 0 prologue.txt` è chiuso al 100%**, ma **non caricato**: 147 unità in staging, zero nel gioco.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, questo file |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (26 controlli, invariante di file) |
