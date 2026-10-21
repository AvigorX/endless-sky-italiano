# L23 — stato di avanzamento (CHIUSO il 2026-10-17)

`data/human/deep missions.txt`, righe 16–4293, **1.355 unità**, 38.724 parole, 83 contesti.

## Fatto

| parte | unità | righe | esito |
|---|---|---|---|
| part01 | 1–90 | 16–532 | `check.py --range 1 90` verde |
| part02 | 91–180 | 533–841 | `check.py --range 91 180` verde |
| part03 | 181–270 | 895–1046 | `check.py --range 181 270` verde |
| part04 | 271–360 | 1153–1431 | `check.py --range 271 360` verde |
| part05 | 361–450 | 1432–1824 | `check.py --range 361 450` verde |
| part06 | 451–540 | 1825–2332 | `check.py --range 451 540` verde |
| part07 | 541–630 | 2333–2663 | `check.py --range 541 630` verde |
| part08 | 631–720 | 2664–2818 | `check.py --range 631 720` verde |
| part09 | 721–810 | 2819–2886 | `check.py --range 721 810` verde |
| part10 | 811–900 | 2887–3112 | `check.py --range 811 900` verde |
| part11 | 901–990 | 3113–3238 | `check.py --range 901 990` verde |
| part12 | 991–1080 | 3239–3451 | `check.py --range 991 1080` verde |
| part13 | 1081–1170 | 3452–3671 | `check.py --range 1081 1170` verde |
| part14 | 1171–1260 | 3672–3990 | `check.py --range 1171 1260` verde |
| part15 | 1261–1355 | 3992–4293 | `check.py --range 1261 1355` verde |

**1.355 / 1.355 unità · 38.724 EN → 36.319 IT (file completo)**

```bash
python staging/editorial/L23_20261017_211741/check.py       # atteso: FAIL totale: 0
python staging/editorial/L23_20261017_211741/verify.py      # atteso: exit 0
```

Misure dell'esecuzione completa (lette, non dedotte): tab **1064/1064**, virgolette **1816/1816**,
token **280/280**, backtick 0/0, rapporto 0,58–1,65, nessuna parola inglese residua.
Tab / virgolette dichiarati in `check_handoff.py` per il lotto attivo: **1.043 unità con tab
iniziale** / 1.816 virgolette — non è il totale dei caratteri tab (trappola 16 dell'handoff).

## Chiusura

Lotto chiuso il **2026-10-17** con `check.py` `FAIL totale: 0` e `verify.py` exit 0 (22 controlli).
Artefatti di chiusura in questa directory: `review.md`, `REPORT.md`, `verify.py`.
`translation.json` sha256[:16] **f745dd523ff32319** (dopo l'ultima esecuzione di `check.py`).

Nessuna unità è stata approvata nel database: le 1.355 unità restano `PENDING` (lo staging non è
approvazione). Il rendering nel gioco **non è stato eseguito**: non è verificato.

Il lotto successivo è **L24**, `data/remnant/remnant 1 introduction.txt` (1.250 unità, 41.087
parole, file intero): punto di partenza e comandi in `HANDOFF_L24_20261017.md` §4.2.

## Regole specifiche di questo file

1. **Virgolette esterne: sì** (come `human missions.txt`). Le interne si scrivono `\"`.
2. **`NT` = 30 unità**: 22 `UI_LABEL`, 2 `TEXT` (nomi di equipaggiamento della Bactrian),
   6 **`label` di condizione dentro `conversation`**: 373 `on first mission`, 375 `knew before`,
   383 `didn't know before`, 386 `know now`, 389 `on second mission`, 404 `still don't know`.
   Sono bersagli di `goto`: restano identiche. Si riconoscono perché sono stringhe corte e
   minuscole dentro un blocco `conversation`.
3. **`TITLES`** contiene i nomi che restano in inglese: `There Might Be Riots`,
   `Songs for the End of Civilization`, `Trouble on the Tarmac`, `Bactrian`, `Deep`, `Dirt Belt`,
   `Far North`, `Core`, `Rim`, `Earth Day`.
4. **Citazioni dal conteggio dispari** (una sola virgoletta, citazione mai chiusa nel sorgente):
   `68`, `79`, `178`, `183`, `199`, `285`, `286`, `291`, `292`, `303`, `308`, `332`, `376`, `379`,
   `382`, `384`, `434`, `457`, `465`, `499`, `776`, `825`, `932`, `933`, `971`, `1002`, `1007`,
   `1010`, `1031`, `1057`, `1067`, `1069`, `1074`. Si **riproducono**: non si chiudono d'ufficio.
   Il numero atteso è `english.count('"')`, da controllare prima di scrivere la parte.
5. **Niente trattini lunghi (—)**: rifiutati dal controllo tipografico. Usare parentesi o virgole.
6. **Nomi propri**: Belzebù (Beelzebub), Sicurezza del Deep (Deep Security), Behemoth, Bounder,
   Raven, Quicksilver, Mule, Corvette, Aerie, Star Barge, Incrociatori (Cruisers), Remnant,
   Distesa di Braci (Ember Waste), Mondi Paradisiaci, Sindacato.
7. **`they` neutro**: dove l'inglese usa `they` per una persona non identificata si usa una
   perifrasi («è responsabile», «sono dispositivi»), non un genere forzato.
8. **Famiglia delle pietre**: `Elf-Stone → Pietra-Elfica`, `God-Stone → Pietra-Divina`,
   `Goddess-Stone → Pietra della Dea`, `Ran-Stone → Pietra di Ran`. Invariati: `Family-Cairn`,
   `Setstokkr`, `Pietre-Jotun` (Jotun-Stones).
9. **`Ice-Crawler` → «cingolato del ghiaccio»**: veicolo narrativo, non un identificatore di
   nave/outfit (verificato nel repository).
10. **`Transport Union` → «Unione dei Trasporti»**: «Sindacato» resta la fazione (Syndicate).
11. **Hjlod parla con articoli caduti e frasi brevi**, come l'Ondurdis di L21a («Io da qui»,
    «Tu hai domande?»). L'inglese storpiato (`velcome`, `vork`, `veapon`) non si trasporta: il
    controllo delle parole residue lo rifiuterebbe.

## Decisioni già prese

- **Belzebub → Belzebù**; **Beelzebub's ship** = «la nave di Belzebù».
- **Lovelace Labs, Tarazed Corporation, Kraz Cybernetics, Betelgeuse Shipyards**: nomi propri,
  invariati (al massimo con l'articolo italiano: «la Lovelace Labs»).
- **Millennium Cell, Cannone Inibitore (Inhibitor Cannon), Classe Forgia (Forge-Class)**:
  nomi di equipaggiamento tradotti dove descrittivi, invariati dove sono nomi commerciali.
- **«Il Sif di <origin>»**: nome del locale, con articolo italiano.
- **Intelligenza artificiale** per «AI» (unità 321), non l'acronimo inglese.
- **`Il Conto dell'Avventuriero`** (unità 1023) per *The Adventurer's Due*: il nome del ristorante di
  Helsingor è un gioco di parole su *due* e in italiano «conto» lo conserva.
- **«Skadenga» resta invariato** come etnonimo collettivo in tutti i composti: `Una casa per gli
  Skadenga` (770), `Trasporto per gli Skadenga` (1051).

## Cosa manca

Nulla su questo file: `data/human/deep missions.txt` è **completo** (1.355/1.355, righe 16–4293,
zero unità prima della 16 e dopo la 4293). Prossimo lotto: **L24** — `data/remnant/remnant 1
introduction.txt`, 1.250 unità, 41.087 parole, file intero.
