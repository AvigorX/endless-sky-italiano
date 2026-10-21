# review.md — L317 (`data/coalition/coalition ships.txt`, righe 1141–2195)

Registro delle decisioni editoriali del lotto che **chiude** il file Coalition: Heliarch, Kimek, Saryd.

## 1. Il file finisce con tre modi di stare nello spazio

| popolo | la nave più caratteristica | che cosa dice |
|---|---|---|
| **Heliarch** | `Neutralizer` | «appena abbastanza forte» da **tenere occupato** il nemico fino ai rinforzi |
| **Kimek** | `Spire` | **trecento** persone in cabine **progettate per un Kimek** |
| **Saryd** | `Traveler` | navi **scientifiche** diventate **case**, da un sistema all'altro |

Le tre schede raccontano **tre tattiche di sopravvivenza**: **temporeggiare**, **spostare gente**, **non fermarsi**. La resa non
aggiunge interpretazione — le tre frasi sono già **parallele** nell'inglese.

## 2. La nota ripetuta tre volte

```
Fighters do not come equipped with a hyperdrive.
You cannot carry a fighter unless you have a ship in your fleet with a fighter bay.
```

Compare **identica** in **1505, 1564, 1621** — tre navi **diverse** (`Pursuer`, `Rover`, `Stalker`). La resa è una sola:

> «I caccia non sono dotati di motore iperspaziale. Non puoi trasportare un caccia se non hai nella tua flotta una nave con una baia di
> caccia.»

Due scelte dentro una frase sola: **`hyperdrive` → «motore iperspaziale»** (non «iperspazio», che è il **luogo**), e **`fighter bay`
→ «baia di caccia»**, già fissato dal corpus (9 occorrenze contro 2).

## 3. La 1504: una nota che sembra la stessa e non lo è

Il `Pursuer` ha **due** note: la 1504 parla del **progetto Kimek** («costa meno da produrre ed è capace di seminare qualsiasi altra
nave della Coalizione»), la 1505 è la nota tecnica del caccia. Un controllo che avesse verificato «tutte le note del Pursuer sono
uguali» avrebbe dato **FAIL su un testo corretto**; uno che avesse verificato solo il **totale** delle parole non avrebbe visto nulla.

La forma giusta, adottata: **tre lati uguali** (1505 = 1564 = 1621) **e** una **disuguaglianza** esplicita (1504 ≠ 1505).

## 4. Le taglie delle tre specie diventano architettura

La riga 1753 è la più bella del file e la più difficile da rendere **senza spiegare troppo**:

> «La maggior parte dei soffitti è troppo bassa perché un Saryd possa stare in piedi dritto, e i letti sono troppo piccoli perché un
> Arach possa distendere comodamente le gambe.»

L'inglese **non** dice quanto sono alti i Saryd né quanto sono lunghi gli Arach: lo lascia dedurre. La resa fa lo stesso, e mantiene
i due **verbi fisici** distinti — *stand up straight* → «stare in piedi dritto», *stretch their legs out* → «distendere le gambe».

## 5. `Skylance`: un'arma Quarg in mano Heliarch

> «Si dice che gli Heliarch abbiano un piccolo deposito di **Skylance** Quarg rubati con cui equipaggiare i Punisher in tempo di
> guerra.»

`Skylance` resta **invariato**: è un nome d'arma Quarg, e in L306 la regola era esplicita — i nomi delle armi Quarg **non si
traducono** («Lancia delle stelle» era stato dichiarato **vietato**). Il test lo include fra i nomi da verificare.

## 6. Scelte di resa

| inglese | resa |
|---|---|
| `just strong enough to keep an enemy vessel occupied` | **appena abbastanza forti da tenere occupata una nave nemica** |
| `until reinforcements can arrive` | **finché non arrivano i rinforzi** |
| `not quite as strong or powerful as the Quarg ships that they are designed to oppose` | **non siano forti o potenti quanto le navi Quarg che sono progettati per contrastare** |
| `versatile and durable ships` | **navi versatili e resistenti** |
| `a small stash of stolen Quarg Skylances` | **un piccolo deposito di Skylance Quarg rubati** |
| `in dogfighting simulations` | **nelle simulazioni di combattimento aereo** |
| `capable of outrunning any other Coalition ship` | **capace di seminare qualsiasi altra nave della Coalizione** |
| `well-rounded ships` | **navi equilibrate** |
| `a compact fortress that can take serious punishment` | **una fortezza compatta capace di incassare colpi seri** |
| `recover faster than some warships` | **riprendersi più in fretta di alcune navi da guerra** |
| `leave much to be desired` | **lasciano molto a desiderare** |
| `constantly in need of transport ships` | **costantemente bisogno di navi di trasporto** |
| `the tiny bunk rooms` | **le minuscole cabine a cuccette** |
| `tight-knit community` | **una comunità stretta** |
| `the Kimek equivalent of a shuttle` | **l'equivalente Kimek di una navetta** |
| `putting down roots on a planet` | **mettere radici su un pianeta** |
| `cross-species friendships` | **amicizie fra specie diverse** |
| `more than ten thousand Earth years` | **più di diecimila anni terrestri** |
| `the most powerful capital ships in the Coalition fleet` | **le più potenti navi capitali della flotta della Coalizione** |
| `a different sort of job every week` | **un lavoro diverso ogni settimana** |

## 7. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **4** (1504, 1505, 1564, 1621) | **4** |
| virgolette | **0** | **0** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **1** (1753) | **7** |

## 8. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 17 unità `PENDING`; **nessuna revisione umana**.
- **Il file è chiuso a 27/27** in staging: **trentatreesimo file completo**, **92** su 167.
- **Prossimo file**: `data/korath/korath weapons.txt` — righe **53–603**, **17 unità** (tutte `DESCRIPTION`), **477 parole**,
  **15 contesti**, **2 tab** (109, 473), **0 virgolette**, **3 apici** (108, 109, 472). Attenzione al **`Cluster Mine`** (riga 603):
  è **munizione**, e la riga 473 è la **nota dei rifornimenti** che compare anche in altri file.
