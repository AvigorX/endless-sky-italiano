# REVIEW — L78 · `data/successors/successor side missions.txt`

## 1. Coerenza con la linea Successors (L68–L77)

- **Casa X / Casate / erede / Predecessori / Successori / `<home system>` / motore di salto**: forme fisse.
- **Il registro dei due osservatori** è arcaico (`thou`, `dost`, `'tis`, `Thour't`) e **informale** — non
  cerimonioso come Tiliia o Sola: sono due appassionati in gita. La traduzione usa il «tu» moderno senza
  formule di cortesia, e il contrasto resta.
- **`Saaqa-Viirja`** è il nome Successore di Sol: coerente con i nomi composti della linea
  (`Kasii-Cavaasa`, `Khosa-Kella-Oa`).

## 2. Nodi traduttivi aperti (dichiarati)

- **`stargazers`**: «osservatori di stelle». Se un lotto futuro usasse il termine per un'istituzione
  (un'Accademia di astronomia), la resa andrebbe rivista.
- **`a scion of the constellations`** (43): «un erede delle costellazioni» — Nnesa sta **scherzando** sul
  fatto che il capitano appartiene alle stelle più che a un pianeta; la resa mantiene l'ironia.
- **`Thour't truly honorable, noble alien`** (25): «Sei davvero onorevole, nobile alieno» — `noble alien` è
  affettuoso, non formale.
- **`the local star 'is so dim that there's hardly any glare!'`** (31): «così fioca che non c'è quasi alcun
  bagliore» — `glare` è il riflesso che rovina le foto, e «bagliore» lo rende.
- **`fah soom`** (47): `label` di salto, identica. Non è una parola Successore: non va interpretata.
- **`novel name`** (50): idem.

## 3. Duplicati: cinque gruppi, tutti legittimi

| gruppo | inglese | perché |
|---|---|---|
| 13 / 20 | `"The sky there's divided into star-studded night and utter void…"` | stessa battuta nei due rami |
| 15 / 22 | `"And back. And our cargo. We can give thee modest pay."` | idem |
| 16 / 23 | `"Sure, I can take you."` | stessa opzione |
| 39 / 41 | `(Indicate <home system>.)` | la stessa scelta, offerta due volte |
| 45 / 49 | `"<home system>," you reply.` | la stessa risposta, nei due rami |

Il `check.py` richiede che **quei** gruppi abbiano resa identica e che **nessun'altra** resa si ripeta fra
inglesi diversi. È l'opposto del caso L77 (22 contro 50), dove l'inglese distingueva e le rese dovevano
differire.

## 4. Tipi e assenze

| tipo | L77 | L78 |
|---|---:|---:|
| `MISSION_TEXT` | 58 | **49** |
| `UI_LABEL` | 1 | **2** (47, 50) |
| `VALUE` / `DESCRIPTION` | 2 / 2 | **1 / 1** |
| `LOGBOOK` / `DIALOG` / `CONVERSATION` / `TEXT` | 0 / 0 / 0 / 0 | **0 / 0 / 0 / 0** |

Le assenze restano le stesse del lotto precedente, ma **due** `UI_LABEL` sono nuove e vanno elencate una per
una: il controllo non dice «2», dice **quali**.

## 5. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 53 unità `PENDING`.
- **Nessun caricamento nel gioco**: il pianeta al bordo della galassia, la tenda planante e la mappa non sono
  stati visti a schermo.
- **Le due `label` restano in inglese** per scelta: sono bersagli di salto.
- **I disegni di Jaasora** nella pila di Nnesa sono nel testo: la traduzione li rende, ma nessun controllo
  misura l'ironia.

## 6. Rischi residui

- **`0,74` è il minimo** (unità brevi come «(Aspetta.)»): dentro il gate.
- **`1,53` è il massimo**: la descrizione della missione (2) è più lunga dell'inglese, come in L77 per la
  stessa ragione (i token `<…>` non si traducono ma le preposizioni sì).
- **Il `verify.py` asserisce 63 prima / 48 dopo**: se L79 non partisse dalla 336, diventerebbe rosso.
- **`osservatori di stelle`**: un revisore umano potrebbe preferire «astrofili»; servirebbe una decisione
  sull'intero gioco.

## 7. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì — 3 parti, `translation.json`, `check.py`, `verify.py`, i tre documenti |
| ESEGUITO | sì — script lanciati, output letto |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit 0 (39 controlli), sha256 `a0ebf1dce186051d` |
