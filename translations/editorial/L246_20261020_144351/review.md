# review.md — L246 (`data/hai/hai ships.txt`, righe 1517–1860) — LOTTO TERMINALE

Registro delle decisioni editoriali dell'**ultimo lotto** di `hai ships.txt`: quattro schede, trentadue nomi da copiare,
due note rientrate.

## 1. Che cosa si copia e che cosa si traduce

| tipo | unità | trattamento | esempio |
|---|---|---|---|
| `TEXT` | 32 | **copiato** | `"Benga" Atomic Steering`, `"Basrem" Reverse Thruster` |
| `DESCRIPTION` | 5 | **tradotto** | le schede |
| `VALUE` | **0** | — | il file ne ha 2, entrambi già passati (L244) |

## 2. Le schede

| nave | inglese | resa |
|---|---|---|
| **Emperor Beetle** (2ª parte, col tab) | `\tMore than just a ship, the Emperor Beetle was built to inspire fear in its enemies…` | «\tPiù che una nave, l'Emperor Beetle è stata costruita per incutere timore nei nemici…» |
| **Solifuge** | `Impressed by the Alphas' "Giftbringer," the Unfettered endeavored to build their own fighter carrier…` | «Colpiti dal "Giftbringer" degli Alphas, gli Slegati si misero a costruire un proprio porta-caccia…» |
| **Violin Spider** | `The Hai fighter is equipped with what most humans would consider the greatest technology available…` | «Il caccia degli Hai è equipaggiato con quello che la maggior parte degli umani considererebbe la migliore tecnologia disponibile…» |
| **Violin Spider** (nota, col tab) | `\tFighters do not come equipped with a hyperdrive…` | **riprodotta dal corpus** (§3) |
| **Water Bug** | `The design of the Water Bug is almost as old as the Aphid…` | «Il progetto del Water Bug è quasi vecchio quanto l'Aphid…» |

## 3. Le due note rientrate: la regola della forma dominante

Le note che il gioco mostra **rientrate** sotto la scheda (`\t…`) non sono testi da tradurre «bene»: sono testi che
**esistono già altrove**. In questo lotto la nota sui caccia:

| resa | occorrenze nel corpus (prima di L246) |
|---|---|
| «I caccia non sono dotati di **iperguida**. … una baia **di** caccia.» | **6** |
| «I caccia non sono dotati di iperguida. … una baia **per** caccia.» | **2** |

Vince la **prima**, riprodotta **alla lettera** (tab compreso). Il `check.py` non confronta con una costante scritta da me:
calcola la forma più frequente leggendo i `translation.json` e la confronta con quella usata qui. Il giorno in cui il
corpus cambia, il controllo lo dice.

**Conseguenza sulla terminologia**: la nota usa **«iperguida»**, mentre la campagna ha fissato `hyperdrive` →
**«iperpropulsore»** altrove (L237, 35 contro 18). La divergenza **resta**, ed è dichiarata: dentro una stringa ripetuta in
mezza dozzina di lotti **vince la ripetizione**, non la preferenza lessicale. Cambiare tutte le occorrenze è un lavoro
separato, da fare con una ricerca globale e un test, non dentro un lotto.

## 4. Il difetto trovato — e la correzione su L244

In L244 avevo scritto la nota sui **droni** con una frase mia («non escono equipaggiati con un iperpropulsore…»). Il corpus
ne aveva già **7** con la forma «non sono dotati di iperguida…». Qui il conflitto è diventato **visibile**, perché la nota
gemella sui caccia è ripetuta in 8 lotti.

Correzione applicata **retroattivamente** a L244 (unità 3):

- la resa ora è quella a **7 occorrenze**, identica;
- `L244/check.py` e `verify.py` restano **verdi** (asseriscono «baia per droni» e la nota tradotta, entrambe vere);
- parole italiane `496 → 498`; `sha256[:16]` `f1ecbcda503f2d0d → 2121d513cf0c67e2`;
- `L244/REPORT.md` §5-bis documenta la correzione e la tabella delle occorrenze; `HANDOFF_L246`, `RIPRESA_L246` e
  `CHECKPOINT_EDITORIALE.md` sono stati aggiornati col nuovo hash.

**Regola che ne esce**: prima di chiudere un lotto che contiene una **frase fissa** (note, avvisi, motti, righe di
interfaccia), cercare la **stringa inglese** nei `translation.json` precedenti. Se c'è, si copia; non si traduce.

## 5. Lessico

| inglese | resa | nota |
|---|---|---|
| `fighter carrier` | **porta-caccia** | nel corpus «portatrici di caccia» (3): qui il composto breve, perché la frase è sintetica |
| `fighter bay` | **baia di caccia** | forma dominante della nota (6 su 8) |
| `jump drives` | **motori di salto** | fissato (334 occorrenze) |
| `inspire fear` | **incutere timore** | |
| `military leaders` | **capi militari** | |
| `at the front of those they command` | **in prima linea coloro che comandano** | |
| `punishment` (militare) | **punizione** | «danni subiti» avrebbe perso la metafora |
| `dish out damage of its own` | **infliggere danni propri** | |
| `aggression spike` | **impennata di aggressività** | |
| `tougher and more well-defended` | **più robusto e meglio difeso** | |
| `little brother` | **fratello minore** | |
| `comprising the bulk` | **costituisce la maggior parte** | |
| `high tech comes at a cost` | **tutta questa alta tecnologia ha un prezzo** | |
| `Unfettered` | **Slegati** | 302 occorrenze nel corpus |
| `Alphas`, `Giftbringer` | **invariati** | fazione e nome dell'arma; le virgolette restano |

## 6. Struttura e assenze

- **Nessun `VALUE`**, **zero segnaposto**, **zero tab fuori dalle unità 1 e 24**.
- **66 virgolette**: 2 per i 32 nomi + 2 intorno a `"Giftbringer"` — 33 unità con 2 virgolette, confrontate **per unità**.
- **2 apici inglesi** (`leaders'`, `Alphas'`: due possessivi) → **5 italiani** (elisioni), con la coppia per unità
  dichiarata: `[(1, 2), (30, 3)]`.
- **Nessun `'s` sopravvissuto** in nessuna delle 37 unità.
