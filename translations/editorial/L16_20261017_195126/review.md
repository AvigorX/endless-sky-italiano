# L16 — Revisione editoriale: primo lotto di `data/human/human missions.txt` (23–562)

181 unità, 4.986 parole inglesi → 4.745 italiane. **Cambio di genere testuale**: dalle descrizioni di
pianeta alle missioni — dialogo, scelte del giocatore, testi di diario. Il lotto contiene 8 missioni
(`Raid Warning`, `Hunted Warning`, `Immigrant Workers`, `Pookie` parti 1–5) e 203 caratteri di virgoletta.

---

## 1. Ricognizione preliminare (fatta una volta, prima di tradurre)

| Tipo | Unità | Trattamento |
|---|---:|---|
| `MISSION_TEXT` | 158 | prosa e battute: tradotto |
| `LOGBOOK` | 8 | testo di diario: tradotto |
| `DESCRIPTION` | 4 | descrizione della missione nel pannello: tradotto |
| `DIALOG` | 4 | testo mostrato al completamento: tradotto |
| `VALUE` | 3 | `name "Pookie"` / `name "Stray Dog"`: nome mostrato, tradotto tranne il nome proprio |
| `UI_LABEL` | 4 | **`label`**: etichette di salto, **lasciate identiche** |

Le quattro `UI_LABEL` sono `label "not poor"`, `label "no bet"`, `label "nope late"`,
`label "remember decline"`: sono bersagli di `goto`, non testo per il giocatore. Tradurle romperebbe il
salto. Restano identiche all'inglese e sono l'unico caso in cui la verifica accetta una stringa non
tradotta (elenco esplicito in `check.py`, controllo `label lasciate identiche (4)`).

**Riga `log` tripla** (riga 555): il sorgente contiene
``log `Minor People` `Puny` `A poodle who was a former racer...` `` e il database la spezza in **tre unità
sulla stessa riga** — 176 categoria, 177 nome, 178 testo. Il tripletto è verificato in `verify.py`.

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze | Note |
|---|---|---:|---|
| `Dirt Belt` | invariato | 3 | regione, come nei lotti precedenti |
| `Paradise Worlds` | Mondi Paradisiaci | 3 | coerente con L10/L15 |
| `East Mesa Indoor Racing Complex` | invariato | 1 | insegna al neon di un locale |
| `Antette and Co. Animal Adoption Agency` | Agenzia di Adozione Animali Antette e Co. | 1 | — |
| `bounty hunter` | cacciatore di taglie | 1 | — |
| `spaceport` / `landing pad` | spazioporto / piazzola di atterraggio | 7 / — | — |
| `Pookie` / `Puny` / `Bleedbug` / `Doom` / `Zinc` | invariati | — | nomi di animali |
| `Walters` / `Pemefrey` / `George` / `Samantha` | invariati | — | nomi propri |
| `Pocahontas` | invariato | 2 | nome completo del cane, citato in dialogo |
| `spacing you` | "mandandoti nello spazio" | 1 | giro di parole per l'esecuzione nello spazio |
| `New Iceland` | invariato | 1 | pianeta |
| `hound race` / `hound-racing ring` | corsa dei segugi / anello di corse di segugi | 4 | — |

Nomi di nave e di classe non compaiono. `Freedom`, `Zenith`, `Shroud` sono pianeti e restano invariati.

---

## 3. Interventi fatti in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 127 / 130 | tab iniziale **rimosso** | il sorgente non ha tab su queste due unità; l'avevo aggiunto per abitudine, `check.py` l'ha rilevato (tab 150 vs 148) |
| 120 / 121 | inglese identico → italiano differenziato | il sorgente ripete il passo sul portare Puny a bordo; due rese distinte ("Prendi Puny in braccio…" / "Sollevi Puny…") |
| 122 / 126 | idem | ripetizione del passo sulla puntata persa |
| 123 / 125 | idem | ripetizione del passo sullo scacciare Puny |
| 40 / 45 | `Pookie` identico in entrambi | è il `name` della missione: nome proprio, non traducibile; documentato come duplicato ammesso |
| 5 / 6 / 11 | virgoletta di apertura **non chiusa** | il sorgente apre il discorso e non lo chiude su quella riga: riprodotto esattamente (1 virgoletta per unità) |
| 69 | "il corpo di Bleedbug" + virgoletta chiusa | controllo del conteggio virgolette (2 esatte) |
| 176 | `Minor People` → "Personaggi minori" | intestazione di categoria nel diario, mostrata al giocatore |
| 177 | `Puny` invariato | nome proprio |
| 56 | `Stray Dog` → "Cane randagio" | `name` della missione, mostrato nell'elenco |

---

## 4. Decisioni aperte (non bloccanti)

1. **`Minor People` → "Personaggi minori"** (176): categoria di diario. Se il gioco usasse la categoria
   come chiave di raggruppamento, la traduzione spezzerebbe il gruppo. In Endless Sky le voci di `log`
   sono testo, non chiavi, ma **non è verificato nel runtime** (nessun avvio, da mandato). Decisione
   reversibile: l'unità è isolata e ha un `raw` proprio.
2. **`label` non tradotte** (84, 86, 107, 124): scelta obbligata. Se in futuro si volesse tradurle servirebbe
   una patch al caricatore, non una traduzione.
3. **Nomi di animali e di persone invariati**: `Doom`, `Bleedbug`, `Zinc`, `Zinc` resta anche nel titolo
   dell'insegna. Da ratificare insieme agli altri nomi propri.
4. Restano aperte le questioni dei lotti precedenti (`Successors`, `Consonance`, `caveau`, `ringroide`,
   `Halite`, `Bulk Freighter`, `Costruttori`, `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`,
   `Egemonia Bunrodean`, `Wanderers`, `void sprites`, `Laser a impulsi`, `Consigli Confederati`).

---

## 5. Esito dei controlli

```
unità 181/181 · mancanti 0 · vuote 0 · duplicati IT 1 ammesso (Pookie, nome proprio)
duplicati EN 4 (righe ripetute nel sorgente: 40/45, 120/121, 122/126, 123/125)
parole 4986 -> 4745 · ratio 0.67-1.61 (battute brevissime)
tab 148/148 · virgolette 203/203 · token <...> 23/23 · backtick 0/0
label lasciate identiche: 4/4
riga grezza identica al file: 181/181 · campi DB identici: 181/181 · state PENDING: 181/181
tipografia 0 · parole inglesi residue 0 · anglicismi 0
FAIL totale: 0
```

`verify.py`:

```
unita: 181 righe 23 - 562
unita successiva nel file: (568, "mission:Smuggler's Den, Part 1")
data/human/human missions.txt: 4253 unita totali, ultima riga 11777
unita del file dopo la riga 562: 4072 (99513 parole)
copertura: 181 / 4253 · stato IN CORSO
tripletto log alla riga 555: OK
```

**Non verificato:** resa in gioco di missioni, scelte e voci di diario (nessun avvio, come da mandato).
