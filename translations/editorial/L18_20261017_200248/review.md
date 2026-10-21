# L18 — Revisione editoriale: `data/human/human missions.txt` 985–1806

187 unità, 4.255 parole inglesi → 4.050 italiane. 17 missioni + **un blocco `phrase`**. Terzo lotto del
file, e il primo che contiene un tipo nuovo (`TEXT`): la ricognizione è stata fatta prima di tradurre.

---

## 1. Ricognizione e classificazione (27 `TEXT` + 3 `UI_LABEL`)

### 1.1 Le 3 `UI_LABEL` — non traducibili

| idx | riga | `raw` | contenuto |
|---:|---:|---|---|
| 124 | 1572 | `label "shoot and die"` | etichetta di salto |
| 131 | 1587 | `label "more money"` | etichetta di salto |
| 137 | 1600 | `label "shoot and live"` | etichetta di salto |

Sono bersagli di `goto` nella sequenza `Shady passenger transport 3 - double cross`. Tradurle romperebbe il
flusso della missione. Restano identiche, elencate in `check.py` (`NT`).

### 1.2 Le 27 `TEXT` — frammenti di una `phrase`, traducibili con vincoli

Tutte e 27 appartengono allo stesso contesto, `phrase:generic human package offer`, e stanno dentro un blocco
`phrase` del sorgente (righe 1719–1760 circa). **Non sono frasi indipendenti**: sono le opzioni di **11 slot**
che il motore concatena per costruire l'offerta della missione "pacco generico".

| Slot | Opzioni | Unità | Trattamento |
|---|---:|---|---|
| 1 soggetto | 5 | 154–158 | tradotto |
| 2 spazio | 1 | — | ` ` (solo spazio: non è un'unità del database) |
| 3 verbo | 5 | 159–163 | tradotto |
| 4 virgoletta di apertura | 1 | 164 (` "`) | **identico** (pura punteggiatura) |
| 5 saluto | 4 | 165–168 | tradotto |
| 6 spazio | 1 | — | ` ` |
| 7 frase | 4 | 169–172 | tradotto |
| 8 spazio | 1 | — | ` ` |
| 9 domanda | 4 | 173–176 | tradotto |
| 10 pagamento | 3 | 177–179 | tradotto (spazio iniziale conservato) |
| 11 virgoletta di chiusura | 1 | 180 (`"`) | **identico** |

Verifica strutturale: `verify.py` confronta le opzioni non vuote del blocco (27) con le unità `TEXT` (27) e
controlla che tutte le righe stiano dentro il blocco. **Esito: OK.**

**Le decisioni che il formato impone** (documentate perché non ovvie):

1. **Lo spazio fa parte del testo.** Le unità 164, 177, 178, 179 iniziano con uno spazio, e gli slot 2, 6, 8
   sono spazi puri. `check.py` non vieta più in assoluto lo spazio iniziale: ora **confronta la firma dello
   spazio** (iniziale e finale) con il sorgente, unità per unità.
2. **La maiuscola dopo il saluto.** Lo slot 7 inizia con la maiuscola, e in inglese funziona sempre perché il
   pronome "I" è maiuscolo. In italiano no: dopo un saluto che finisce con la virgola ("Capitano,") la
   maiuscola sarebbe un errore. Soluzione: **tutti i saluti italiani finiscono con il punto**, così lo slot
   successivo può iniziare con la maiuscola in ogni combinazione:
   - 165 `Captain,` → **"Capitano."** (la forma più breve che chiude il periodo: 8 → 9 caratteri)
   - 166 `Excuse me, Captain.` → "Mi scusi, Capitano."
   - 167 `Sorry to interrupt, but` → **"Scusi se la disturbo."** (perde il "ma", necessario per chiudere il periodo)
   - 168 `Hey there, Captain.` → "Ehi, Capitano."
3. **Accordo di genere nei verbi.** I soggetti sono di genere diverso (uomo, donna, sconosciuto…), quindi i
   verbi degli slot 3 sono alla terza persona senza participi concordati: "spunta", "ti si avvicina e dice",
   "ti ferma e chiede". Un participio concordato ("avvicinatosi") romperebbe metà delle combinazioni.

Frase composta, prima opzione di ogni slot (misurata da `check.py`):

```
EN: A local appears from seemingly nowhere to ask, "Captain, I have a small package that needs to get to
    <planet> by <day>. Are you able to carry it for me? I'll give you <payment> for the effort."
IT: Uno del posto spunta dal nulla e chiede, "Capitano. Ho un pacchetto che deve arrivare su <planet> entro
    <day>. Riesce a portarlo per me? Le darò <payment> per il disturbo."
```

`check.py` compone la frase in inglese e in italiano e verifica su entrambe: nessuno spazio doppio, nessuno
spazio prima della punteggiatura, virgolette pari, nessuna minuscola dopo il punto; sull'italiano anche
nessuna maiuscola dopo la virgola (in inglese il pronome "I" renderebbe il test falso).

---

## 2. Convenzioni applicate

| Termine | Resa | Occorrenze | Note |
|---|---|---:|---|
| `There Might Be Riots` | invariato | 12 | nome della band |
| `Trouble on the Tarmac Tour`, `Songs for the End of Civilization`, `Gluttony` | invariati | 1+1+1 | titoli di tour, album e canzone |
| `Syndicate` | Sindacato | 4 | — |
| `Lovelace Labs` | invariato | 1 | azienda |
| `Republic Intelligence` | Intelligence della Repubblica | 1 | — |
| `the Hai` / `Hai space` | gli Hai / spazio degli Hai | 4 | specie, invariata |
| `Allhome`, `Pilot` | invariati | 2+1 | toponimi |
| `wormhole` | invariato | 1 | — |
| `Mondi Paradisiaci` | — | 1 | coerente con L10/L15 |
| `the Rim` / `the Deep` | invariati | 1 / 0 | — |
| `shuttle` | shuttle | 1 | mezzo generico |
| `Argosy Modificata` | `Modified Argosy` | 1 | classe di nave: da verificare contro il glossario quando si tradurranno le navi |
| `bounty` | taglia | 2 | — |
| `drugs` / `recreational pharmaceuticals` | droghe / "farmaci ricreativi" | vari | virgolette conservate |
| `Rescue Miners` | Soccorso ai minatori | 2 | `name` di missione |
| `Courier` | — | — | `name` resi come "Consegna urgente su <planet>", "Pacchetto per <planet>", "Documenti per <planet>" |

---

## 3. Interventi in stesura e rilettura

| # | Intervento | Perché |
|---|---|---|
| 5 / 32 | `(Non adesso.)` → 32 diventa **`(Non ora.)`** | stesso inglese `(Not right now.)` in due missioni: italiano differenziato |
| 154 | "Un abitante del posto" → **"Uno del posto"** | rapporto 3,00 su un frammento di 7 caratteri; "uno del posto" è più naturale e resta distinto da 156 |
| 165 | "Capitano, mi scusi." → **"Capitano."** | rapporto 2,38; forma minima che chiude comunque il periodo (§1.2) |
| 25 | "dove la gente erano scoiattoli giganti" → "dove gli abitanti erano scoiattoli giganti" | errore di accordo, corretto in rilettura |
| 25 | "Gli è piaciuta anche la nostra musica" → "Anche a loro è piaciuta la nostra musica" | "gli" plurale è colloquiale |
| 66 / 67 | tolti gli articoli davanti al nome della band | "i There Might Be Riots" è innaturale; in 66 le virgolette restano |
| 111 / 116 | "Devi esserti fatto una bella reputazione" → "Vuol dire che in certi ambienti la tua reputazione ti precede" / "hai già un certo nome" | participio concordato al maschile su un soggetto di genere ignoto |
| 126 | "una Argosy" → "un'Argosy" | elisione |
| 139 | "Riparato dietro la poltrona" → "Riparandoti dietro la poltrona" | participio sospeso, sostituito con gerundio |
| 14 | "quello che immagin -di certo- sia gas" → "quello che immagini sia gas" | frase rotta in prima stesura |

Due difetti li ha trovati il checker, non l'occhio: il duplicato italiano 5/32 e i due rapporti fuori scala
(154, 165).

---

## 4. Decisioni aperte

1. **Ordine e punteggiatura della `phrase`**: la frase italiana dipende dal fatto che tutti i saluti chiudano
   con il punto. Se in futuro si cambia un saluto, va ricomposta e ritestata (`check.py` lo fa da solo).
2. **`Argosy Modificata`**: nome di classe di nave reso come prodotto. Da verificare contro `glossary.csv`
   quando si tradurranno i file delle navi — potrebbe dover restare `Modified Argosy`.
3. **Titoli musicali invariati** (`There Might Be Riots`, `Songs for the End of Civilization`, `Gluttony`,
   `Trouble on the Tarmac Tour`): scelta coerente con L17, elencata in `TITLES` dentro `check.py`.
4. Restano aperte le questioni dei lotti precedenti (`Successors`, `Consonance`, `caveau`, `ringroide`,
   `Halite`, `Bulk Freighter`, `Costruttori`, `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`,
   `Egemonia Bunrodean`, `Wanderers`, `void sprites`, `Laser a impulsi`, `Consigli Confederati`, `rimway`).

---

## 5. Esito dei controlli

```
unità 187/187 · mancanti 0 · vuote 0
non traducibili lasciate identiche: 5/5 (3 label + 2 frammenti di punteggiatura)
duplicati IT 0 · duplicati EN 16 (tutti ripetizioni del sorgente, elencate)
parole 4255 -> 4050 · ratio 0.65-1.86
tab 81/81 · virgolette 191/191 · token <...> 109/109 · backtick 0/0
spazio iniziale/finale come il sorgente: ok
phrase: 11 slot · EN composto pulito · IT composto pulito
riga grezza identica al file: 187/187 · campi DB identici: 187/187 · state PENDING: 187/187
tipografia 0 · parole inglesi residue 0 (titoli esclusi) · anglicismi 0
FAIL totale: 0
```

`verify.py`: 187 unità righe 985–1806 · unità successiva 1811 `mission:Courier 4` · copertura del file
**501 / 4.253** · 27 frammenti `TEXT` tutti dentro il blocco `phrase` · opzioni non vuote 27 = unità 27.

**Non verificato:** resa in gioco — in particolare **come il motore compone materialmente la `phrase`**
(scelta casuale delle opzioni e ordine degli slot). La composizione è verificata sui dati, non nel runtime.
