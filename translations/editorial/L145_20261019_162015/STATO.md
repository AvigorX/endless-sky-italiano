# STATO — L145 · `unfettered 0 prologue.txt` (la loggia delle armi: il primo `LOGBOOK` e le virgolette aperte)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L145_20261019_162015` |
| Righe / unità | **423–459** / **13** — file all'**87,1%** (128/147) |
| Tipi | **12 `MISSION_TEXT`** · **1 `LOGBOOK`** (unità 3) |
| `VALUE` · `UI_LABEL` | **0** · **0** — **due asserzioni vuote scritte** |
| Token | **3** in **2 unità**: `<learned>`, `<last>` (unità 2) · `<The engineer>` (unità 5) — **case-sensitive** |
| Stati | **13 `PENDING`** — misurato e **asserito** |
| Contesto | **1** — `Jump Drive Trading`, missione **aperta** |
| Testi | **13 distinti** |
| Parole | **703 EN → 635 IT** (0,903); per unità **0,93–1,20**, media **1,03** |
| Tab · virgolette | **12 unità** · **20**, con **due dispari** (unità 12 e 13) |
| sha256 | `56b7e47a1b3a8c72…` |
| `check.py` | **32 controlli**, `FAIL totale: 0` |
| `verify.py` | **27 controlli**, exit **0** — invariante di **segmento** |

## Il primo `LOGBOOK` del tratto

L'unità 3 è l'unica non `MISSION_TEXT`:

> «Un guerriero Slegato che sa come si maneggia una lama. Messo alla prova da lei prima di ricevere l'accesso alle nuove
> armi Slegate. Sarebbe stata la fine, se lei non si fosse trattenuta.»

È **diario**, non dialogo: niente virgolette, tono da nota a margine, e il giudizio è del giocatore su se stesso. Il
`check.py` lo isola per tipo e pretende che sia **tradotto**, non solo presente.

## Tre token, di cui uno che contiene una frase

| token | unità | contesto | confronto |
|---|---|---|---|
| `<learned>` | 2 | dopo «una lama!», maiuscola che segue | esatto |
| `<last>` | 2 | «capitano `<last>`!» — cognome del giocatore | esatto |
| `<The engineer>` | 5 | **inizio di frase**: `<The engineer> ti conduce sottoterra…` | **esatto, case-sensitive** |

`<The engineer>` contiene un articolo e una maiuscola. Con un confronto `.lower()` diventerebbe `<the engineer>`: un
simbolo **diverso**, che il motore non troverebbe. Il controllo lo confronta quindi alla lettera, e in più verifica che
la variante minuscola **non** compaia.

## Due virgolette aperte, e restano aperte

Le unità 12 e 13 aprono una battuta e **non la chiudono** — è un difetto del sorgente, non un refuso di battitura:

```
"Ah, il Blaster. È prediletto da molti capitani di Shield Beetle…
"È di gran lunga la mia arma preferita fra tutte… non ti daranno più fastidio!
```

Chiuderle sarebbe un'**invenzione tipografica**: il testo originale non lo fa. Tre controlli: disparità riprodotta
(unghost 12 e 13), **nessuna virgoletta finale aggiunta**, e **stesso segno finale dell'inglese** (`!` e `.`).

## Nomi che non si traducono

`Tripulse Shredder`, `Blaster`, `Ion Cannon`, `Shield Beetle`, `Firelode`: armi, navi e mondi restano inglesi, come in
tutto lo staging (misurato: `Ion Cannon` già presente in `human missions.txt` e `remnant 1 introduction.txt`). Un
controllo **vieta** le traduzioni inventate («Distruttore», «Cannone ionico», «Scarabeo»).

## Verifica

```bash
cd staging/editorial/L145_20261019_162015
python mkparts.py   # 13 unità · 12 MISSION_TEXT + 1 LOGBOOK · 3 token · 2 dispari · 12 tab · 20 virgolette
python check.py     # FAIL totale: 0 (32 controlli)
python verify.py    # exit 0 (27 controlli, invariante di segmento)
```

**Non verificato**: nessuna arma è stata comprata nel gioco; la scena non è stata giocata.
