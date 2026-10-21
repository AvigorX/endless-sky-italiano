# REPORT — L119 · `pirate jobs.txt` (difese, furti di carico, assassinii) · **file chiuso**

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| Raid on Merchants (South) | 1–4 | 2958–2993 | flotta mercantile meridionale; due dialoghi già in L118 |
| Northern Pirate Defense | 5–16 | 2994–3065 | Marina, versione pagata e non pagata, scena della difesa |
| Core Pirate Defense | 17–28 | 3066–3136 | Sindacato, idem |
| Southern Pirate Defense | 29–40 | 3137–3216 | milizia, idem |
| Cargo Theft | 41–53 | 3217–3343 | carico segreto, tre regioni, atterraggio a mani vuote |
| Assassinii politici | 54–77 | 3344–3706 | Mondi Liberi, Sindacato, Repubblica; due taglie ciascuno |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Defend <planet>` · `Convoy near <system>` · `Assassinate a political target` · `Merchants near <system>` | **identici** (`VALUE`) | nomi di missione, 4 nomi per 16 unità |
| `Defeat them to defend anarchy!` | **Sconfiggile per difendere l'anarchia!** | |
| `Many locals … collectively pay you` | **Molti abitanti … ti pagano collettivamente** | |
| `drive off the Navy` · `the Syndicate` · `the militia (forces)` | **respingere la Marina** · **il Sindacato** · **la milizia** | |
| `combat-worthy ship` | **nave in grado di combattere** | |
| `This could be an easy way to get yourself killed` | **Potrebbe essere un modo facile per farti uccidere** | |
| `(Stay here until the fight is over.)` | **(Resta qui finché la battaglia non è finita.)** | tab e parentesi conservati |
| `(Join the defense fleet.)` | **(Unisciti alla flotta di difesa.)** | |
| `take off together...` | **decollate insieme...** | tre punti ASCII, non ellissi tipografica |
| `Cargo stolen from a merchant ship…` | **Carico rubato a una nave mercantile, che…** | descrizione dell'equipaggiamento |
| `A local warlord is interested in having the cargo on the <npc>` | **Un signore della guerra locale è interessato a impossessarsi del carico della `<npc>`** | |
| `Plunder it` | **Saccheggialo** | il carico |
| `but you don't have the secret cargo!` | **ma non hai il carico segreto!** | |
| `cargo hold` | **stiva** | |
| `Assassinate them by <day>` | **Assassinalo entro `<day>`** | il politico è singolo |
| `in their ship, the <npc>` | **sulla sua nave, la `<npc>`** | |
| `Payment is <payment>. Be advised that they may have escorts / be heavily defended.` | **Il compenso è `<payment>`. Attenzione: potrebbe avere delle scorte / essere pesantemente difeso.** | |
| `slave traders` · `drug traders` | **trafficanti di schiavi** · **trafficanti di droga** | |
| `Syndicate spacenear` (sorgente) | **spazio del Sindacato vicino a** | refuso del sorgente normalizzato |

## 3. Difficoltà

1. **Prima `CONVERSATION` della campagna recente**: dodici unità in tre scene, con **9 tab iniziali** e **6
   virgolette**. Il tipo va letto come scena: la battuta d'apertura non ha tab, le tre opzioni ne hanno uno.
2. **Il tab non sta nella parte**: le parti si scrivono senza tab e il costruttore antepone
   `'\t' * (tab dell'inglese)`; il controllo verifica **unità** e **conteggio**, non la presenza.
3. **Le virgolette sono dentro le battute**, quindi vanno contate per unità (2 per scena) e non in blocco.
4. **Un contesto da una sola unità** (`outfit:Secret Cargo`): la distribuzione non è uniforme e non va
   «corretta».
5. **Refuso del sorgente**: unità 73 senza «and». Resa identica all'unità 65, **dichiarata** in `EXC`.
6. **Un conteggio sbagliato, corretto**: il primo `check.py` si aspettava **2** unità condivise con L118, ma sono
   **3** — c'è anche il nome `Merchants near <system>`. Corretto l'atteso (`[1, 3, 4]`), non il dato.
7. **Invariante di file**: il `verify.py` legge i tre `translation.json` e dimostra **279/279** righe coperte,
   `sovrapposti = 0`, `max(line) = 3706`.

## 4. Numeri osservati

```
unita' 77/77 · DIALOG 32 · DESCRIPTION 17 · VALUE 16 · CONVERSATION 12 · tutte PENDING
contesti 20 (19 da quattro, 1 da una) · testi distinti 47 (4 nomi + 43 prosa, 2 da L118)
tab 9 unita · virgolette 6 · token 106 in 6 famiglie · quadre 0 · backtick 0
parole EN 1223 -> IT 1246 (1.019) · rapporto 0.86 - 1.31, media 1.10
righe 2958/3706 · file 279/279 (100,0%) · 3 lotti · 3227 EN -> 3245 IT
FAIL totale: 0 (31 controlli) · verify exit 0 (31 controlli)
sha256[:16] 51189eab238776c8
```

## 5. Stato del progetto

```
TOTALE staging: 26573 unita · 838918 EN · 796646 IT
pirate jobs.txt: 279/279 (100.0%) · 3 lotti · FILE COMPLETO
file completi: quarantatre · residuo traducibile (formula state.py): 5357
residuo misurato: 5988 unità / 138064 parole su 123 file
avanzamento: 26573/32924 unità (80,7%) · 838918/979975 parole (85,6%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 4 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (31 controlli), `verify.py` exit **0** (31 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 77 unità restano `PENDING`; nessuna missione è stata caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file è chiuso ma non caricato**: 279 unità tradotte, zero viste nel gioco.
- **Prossimo file**: `data/human/campaign events.txt` (150 unità, 6.961 parole) — primo lotto **L120**, righe
  28–242, 52 unità, 2.255 parole (`HANDOFF_L120_20261019.md`).
