# REPORT — L95 · `coalition culture conversations.txt` (terzo lotto)

## 1. Contenuto

Righe 148–190, contesto `Coalition Folklore: Kimek` (27 unità, di cui 3 etichette di salto):

- l'invito del Kimek: «Oggi in corso, un festival culturale è»; il treno per il parco (1–3);
- la savana con i campi di accampamenti e i forti sulla collina, la spiegazione delle regole (4–7);
- la domanda del giocatore («se è una fiaba, come mai può vincere chiunque?») e la risposta del menestrello:
  il vento sollevò i fiori e gli bloccò la vista proprio sul finale — così la storia ammette **due esiti** (8–10);
- la scelta della fazione, il forte dei difensori, il gilet di cuoio, i secchi di liquido scivoloso (11–17);
- la battaglia: la scelta fra cancello principale e cancello posteriore, e i tre esiti (19–24, 26–27).

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| sintassi Kimek | **ordine marcato italiano** | come Saryd e Arach: «Occupato, Capitano?», «Proteggere la nostra fattoria, dobbiamo» |
| `Spring Siege` | **Assedio di Primavera** | titolo di fiaba: si traduce, resta fra apici come nel sorgente |
| `minstrel` | **menestrello** | è il testimone della storia, non un «cantastorie» generico |
| `chitters` | **cinguetta** | i Kimek sono aviani: il verso è quello |
| `keep` (teatro militare) | **maschio** | termine tecnico del castello, fra virgolette come nel sorgente |
| `crops` / `farm` | **raccolti** / **fattoria** | fra virgolette nel sorgente perché sono di plastica |
| `battlements` | **merli** | termine architettonico corretto |
| `blue sashes` / `green strip` | **fasce blu** / **striscia verde** | il colore identifica la squadra |

## 3. Difficoltà

1. **Tre `UI_LABEL` di salto in mezzo alla prosa** (18, 23, 25): non entrano nelle parti, il costruttore le
   scrive dal sorgente e il `check.py` le elenca per indice. Una deroga generale avrebbe nascosto l'omissione.
2. **La voce Kimek è sintattica**: nove unità con ordine invertito (1, 5, 9, 10, 14). Riprodotta con italiano
   marcato ma corretto.
3. **Zero token** con 38 virgolette: controllo asserito (`tok == 0`), non omesso.
4. **Un errore mio, intercettato dall'asserzione**: nell'unità 14 avevo chiuso il periodo con una virgoletta di
   troppo (7 invece di 6). Il costruttore ha abortito prima di scrivere le parti.
5. **La ripetizione 20/27** è la stessa scelta in due rami: resa identica, verificata.

## 4. Numeri osservati

```
unita' 27/27 (24 tradotte + 3 UI_LABEL identiche) · tab 23 · virgolette 38 = 38 · token 0 = 0
parole EN 1382 -> IT 1242 · rapporto 0.75 - 1.41
righe 148/190 · file 157 unita · 67 prima / 63 dopo
FAIL totale: 0 (28 controlli) · verify exit 0 (29 controlli)
sha256[:16] 58cfe11da4d60c5c · copertura del file 94/157 (59,9%)
```

## 5. Stato del progetto

```
TOTALE staging: 25081 unita · 801849 EN · 760183 IT
coalition culture conversations.txt: 94/157 (59,9%) · 3 lotti
residuo traducibile (formula state.py): 6849 · misurato: 7416 unità / 174182 parole su 129 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (28 controlli) **e** `verify.py` exit **0** (29 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 27 unità restano `PENDING`; il gioco non è stato caricato con questa traduzione.
- **Il file non è completo**: 63 unità restano; il contratto successivo è `HANDOFF_L96_20261018.md`
  (righe 191–250, chiude il contesto `Kimek` con altre **5 etichette di salto**).
- **Nessuna revisione umana**.
