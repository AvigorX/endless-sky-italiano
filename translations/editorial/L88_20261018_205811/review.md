# REVIEW — L88 · `data/successors/successor outfits.txt`

## 1. Coerenza (L86–L87)

- **propulsori di manovra**, **bimodale**, **stellator**, **cortex**: identici ai due lotti precedenti.
- **`outfit`** → «equipaggiamento» in prosa; `outfit:` nei contesti.
- **Veusa**: nome di serie, invariato (compare anche come `"Veusa" Inductive Thruster` in L87? No: in L87 i
  contesti erano `Aqra`; `Veusa` appare qui per la prima volta come serie completa).

## 2. Nodi aperti

- **`reverse thruster`**: «propulsore di retro». L'alternativa «invertitore di spinta» è più tecnica, ma il
  gioco usa `reverse thruster` anche per le navi piccole.
- **`pulsed inductive`**: la serie `Veusa` è «pulsata», le altre no. Il testo inglese lo dice solo per lei, e la
  resa lo conserva.
- **`Successori invertebrati`**: è il primo riferimento alla biologia dei Successori in questi lotti; se un
  lotto futuro desse una descrizione contrastante, andrebbe rivisto qui.
- **`g-force`**: «forza g», non «forza di gravità» — l'inglese intende l'accelerazione.

## 3. Cosa NON è stato fatto

- **Nessuna scrittura su `state.db`**: 10 unità `PENDING`.
- **Nessun caricamento nel gioco**: le schede non sono state viste a schermo.
- **Nessun confronto con le statistiche**: «il più grande» e «molto più agili» sono testo.

## 4. Rischi residui

- **`0,91` è il minimo del file** (unità 2, la frase breve sul retro): dentro il gate, ma è il primo valore sotto
  1,00 in questo file.
- **Il duplicato 2/6/10**: se un lotto futuro cambiasse la resa di una delle tre, il file diventerebbe
  incoerente; la scelta è dichiarata qui.
- **Il `verify.py` asserisce 34 prima / 12 dopo**: L89 deve partire dalla 574 e chiudere il file.

## 5. Esito

| Livello | Raggiunto |
|---|---|
| IMPLEMENTATO | sì |
| ESEGUITO | sì |
| **VERIFICATO** | sì — `check.py` `FAIL totale: 0` (24 controlli), `verify.py` exit 0 (24 controlli), sha256 `40dafd350a29f440` |
