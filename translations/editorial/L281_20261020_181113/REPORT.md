# REPORT — L281 (`data/quarg/quarg news.txt`, righe 23–490) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO.** `check.py` esce 0 con **22 controlli**; `verify.py` esce 0 con **19 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 50 (40 `NEWS`, 10 `TEXT`) | 50 |
| — di cui delimitatori `"` | 28 | **28 copiati** (`ID_OK`) |
| — di cui prosa | 22 | **22 tradotte** |
| parole | 778 | **727** (0,93) |
| virgolette | 44 | **44**, per unità |
| tab / segnaposto | 0 / 0 | 0 / 0 |
| apici | 14 | 20 |

Rapporto delle 22 unità di prosa: **0,82 – 1,28**.

## 2. Perché il lotto non è quello del contratto

Il contratto diceva: 43 unità, righe 23–483. La misura dice: **50 unità, righe 23–490**, e la finestra contrattuale
**tagliava sette unità di prosa** (484-490) lasciando dentro quasi solo delimitatori.

La causa è la struttura del file: le notizie sono **composte da frammenti** (`word` blocks) e l'estrattore registra **solo**
le stringhe fra backtick. Perciò:

- **28 unità** sono l'unica stringa `` `"` `` (delimitatori di citazione): hanno **un solo valore possibile** e si copiano
  dichiarandole in `ID_OK`;
- **22 unità** sono prosa vera, alle righe 23, 455-465 e 481-490.

Il lotto è stato **risegato all'intero file**, che così si chiude in un colpo: 22 traduzioni + 28 copie dichiarate. **Vince il
workspace**, e il documento del contratto resta storico (dichiarava 43 unità: era sbagliato).

## 3. La lacuna dell'estrattore

I frammenti **senza backtick** — `` "Are you" ``, `` " " ``, `` "a merchant" `` — **non esistono nel database** e quindi non
sono traducibili. Le notizie composte restano in inglese in quei pezzi. Il lotto **non** tenta di riparare l'estrattore
(protetto) e **dichiara** la lacuna: il `check.py` la stampa a ogni esecuzione, e il `REPORT` la registra qui.

## 4. Il registro Quarg

I Quarg parlano in modo **formale, paziente, didattico**: spiegano perché non condividono la tecnologia, si dichiarano
dispiaciuti per la guerra, accolgono il visitatore «a patto che» non cerchi conflitto. La resa conserva la **misura** del loro
parlare e il **«tu»** del progetto:

| inglese | resa |
|---|---|
| `Do you have any questions?` | **Hai qualche domanda?** |
| `We are glad to receive visitors` | **Siamo lieti di ricevere visitatori** |
| `It is for the best that humans grow and develop on their own` | **È meglio che gli umani crescano e si sviluppino da soli** |
| `I can only hope you will all come to see reason` | **Posso solo sperare che tutti voi arriviate a ragionare** |
| `We cannot allow our equipment to be in the wrong hands` | **Non possiamo permettere che le nostre apparecchiature finiscano nelle mani sbagliate** |
| `provided you seek no conflict with anyone on our worlds` | **a patto che tu non cerchi conflitto con nessuno sui nostri mondi** |

Le dieci **istantanee** del mondo ad anello sono al **presente**, in seconda persona («Vedi», «Noti», «Lo osservi»): è lo
stesso schema del sorgente e il `check.py` verifica che le forme chiave ci siano.

## 5. Verifica

```
check.py   22 controlli · FAIL totale: 0 · exit 0
verify.py  19 controlli · FAIL: 0 · exit 0
segmento   0 prima (apre il file) · 50 qui · 0 dopo (fine file) · 10 contesti
FILE       50/50 (100%) · un solo lotto · righe distinte 50 · 23–490
```

**Primo giro verde** dopo la risegatura: le 28 copie sono confrontate per **identità** (`== '"'`), le 22 traduzioni per
**differenza**, e le 44 virgolette per **unità**.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 50 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Le notizie composte restano parzialmente in inglese**: i frammenti senza backtick non sono nel database (lacuna
  dell'estrattore, dichiarata).
- **Il file è completo al 100%** solo in staging, e solo per le unità **che l'estrattore espone**.
