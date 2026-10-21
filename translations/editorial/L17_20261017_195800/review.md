# L17 — Revisione editoriale: `data/human/human missions.txt` 568–980

133 unità, 4.128 parole inglesi → 3.788 italiane. 11 missioni, 214 virgolette, 66 token `<...>`.
Secondo lotto del file, stesso impianto di L16.

---

## 1. Ricognizione preliminare

| Tipo | Unità | Trattamento |
|---|---:|---|
| `MISSION_TEXT` | 95 | tradotto |
| `DIALOG` | 13 | tradotto |
| `VALUE` | 9 | `name` della missione: tradotto, tranne i token |
| `DESCRIPTION` | 9 | tradotto |
| `LOGBOOK` | 6 | tradotto |
| `UI_LABEL` | 1 | **`label "towns syndicate"`: lasciata identica** |

**Token presenti** (66, tutti conservati unità per unità): `<planet>` 18, `<payment>` 12,
`<destination>` 11, `<bunks>` 7, `<origin>` 4, `<tons>` 4, `<last>` 3, `<cargo>` 3, `<waypoints>` 3,
`<fare>` 1. Nessuna riga produce più unità: qui non ci sono `log` triple.

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze | Note |
|---|---|---:|---|
| `Syndicate` / `Syndicate world(s)` | Sindacato / mondi del Sindacato | 4 | — |
| `the Core` | il Nucleo | 1 | coerente con L9 |
| `the Rim` | il Rim | 1 | invariato, come nei lotti precedenti |
| `the Deep` | il Deep | 1 | invariato |
| `rimway` | invariato | 3 | passaggio principale dell'anello: termine d'impianto, non traducibile senza perdita |
| `Wolf-Rayet stars` | stelle Wolf-Rayet | 2 | nome scientifico |
| `There Might Be Riots` | **invariato** | 5 | nome della band |
| `Henhouse In Your Soul` | **invariato** | 1 | titolo della canzone |
| `Sad Archie` | invariato | 1 | titolo della canzone |
| `Smuggler's Den` / `Millrace` / `Hope` / `Wayfarer` / `Arabia` / `Maker` | invariati | — | toponimi |
| `Joe` / `Maria` / `Jesse` / `Leroy` / `Ulrich` / `Becca` / `Patterson` | invariati | — | nomi propri |
| `captain` (allocutivo) | Capitano | — | coerente con i lotti precedenti |
| `true love` | "vero amore" (tra virgolette) | 1 | virgolette conservate |

---

## 3. Interventi in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 101 | **tab iniziale aggiunto** | il sorgente ha il tab, la mia prima stesura no: `check.py` l'ha rilevato (tab IT 83 vs 84) |
| 128 | `"Volentieri!"` → `"Ma certo!"` | rapporto 1,75 su una battuta di 8 caratteri; "Ma certo!" resta distinta da 117 ("Certo!") e rientra nel rapporto |
| 34 / 44 | DIALOG identici (scorta non ancora arrivata) | ripetizione del sorgente; non tocco l'italiano, che resta fedele e identico |
| 1 / 35 · 55 / 66 | `name` di missione ripetuto (`Refugees to <planet>`, `Expedition to Hope`) | nome nel pannello missioni: tradotto uguale perché è lo stesso nome, non due testi diversi |
| 22 | "Gli uomini sulla porta non fanno nulla" | resa asciutta di "make no effort to stop you" |

---

## 4. Correzione al checker, dichiarata

Le unità 112, 122, 125, 126 contengono `There Might Be Riots` e `Henhouse In Your Soul`: la regex delle
parole inglesi residue segnalava `there`, `be`, `your`. Sono **titoli che restano in inglese per scelta**
(come i nomi propri), quindi il controllo ora **rimuove quei due titoli dal testo prima di scansionarlo**
(`TITLES` in `check.py`), invece di allentare la regex. L'elenco è esplicito e non copre altro: se comparisse
altro inglese, il controllo fallirebbe ancora.

Cambio minore: la riga di esito ora dice `label lasciate identiche (1)` invece di un numero fisso.

---

## 5. Decisioni aperte

1. **`towns syndicate`** (unità 88) è una `label` di salto: resta identica. Stessa scelta di L16.
2. **`rimway` invariato**: se in altri file compare come termine comune, va tenuta la stessa resa.
3. **Titoli di canzoni e nome della band invariati**: `There Might Be Riots`, `Henhouse In Your Soul`,
   `Sad Archie`. Da ratificare insieme agli altri nomi propri.
4. Restano aperte le questioni dei lotti precedenti.

---

## 6. Esito dei controlli

```
unità 133/133 · mancanti 0 · vuote 0
duplicati IT 0 (ammessi 1/35, 34/44, 55/66: nomi di missione e DIALOG ripetuti nel sorgente)
duplicati EN 4 (1/35, 34/44, 55/66, 117/128)
parole 4128 -> 3788 · ratio 0.66-1.50
tab 84/84 · virgolette 214/214 · token <...> 66/66 · backtick 0/0
label lasciate identiche: 1/1
riga grezza identica al file: 133/133 · campi DB identici: 133/133 · state PENDING: 133/133
tipografia 0 · parole inglesi residue 0 (titoli esclusi, vedi §4) · anglicismi 0
FAIL totale: 0
```

`verify.py`:

```
unita: 133 righe 568 - 980
unita successiva nel file: (985, 'mission:There Might Be Riots part 2')
unita del file dopo la riga 980: 3939 (95385 parole)
lotti su questo file: L16 (181), L17 (133)
copertura: 314 / 4253 · IN CORSO
righe con piu unita: nessuna
```

**Non verificato:** resa in gioco (nessun avvio, come da mandato).
