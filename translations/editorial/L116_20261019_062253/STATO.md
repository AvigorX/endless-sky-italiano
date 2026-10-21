# STATO — L116 · `data/_ui/tooltips.txt` (**file chiuso: 667/667**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L116_20261019_062253` |
| Righe / unità | **1569–1865** / **133** |
| Tipo | **133 `TUTORIAL_TIP`**, nient'altro |
| Stati | **133 `PENDING`** — misurato con `select state` e **asserito** in `mkparts.py` |
| Contesti | **80** — 62 singole, **1 coppia**, **4 terne**, **8 quaterne**, **5 gruppi da cinque** |
| Parole | **3018 EN → 2995 IT** (0,992); per unità 0,77–1,59, media 1,09 |
| Tab · quadre | **0** · **0** |
| Token | **1 `<shift>`** (unità 55) |
| Ripetizioni | **0** (nessuna coppia di unità ha lo stesso inglese) |
| Virgolette | **144** in 66 unità (61 con 2, 4 con 4, una con 6) |
| sha256 | `9a630cfede888bed…` |
| `check.py` | **38 controlli**, `FAIL totale: 0` |
| `verify.py` | **47 controlli**, exit **0** — invariante **di file** |

## Il file si chiude

| misura | valore |
|---|---|
| Lotti su `data/_ui/tooltips.txt` | **6** (L111–L116) |
| Unità coperte | **667 / 667** — nessuna mancante, **`sovrapposti = 0`** |
| Righe | 16–1865 (`max(line) = 1865`) |
| Parole | **12.084 EN → 12.495 IT** |
| `verify.py` di questo lotto | invariante **di file**: legge i sei `translation.json` e confronta gli insiemi di `id` col database |

Il `verify.py` di L115 pretendeva un'unità successiva al segmento: qui **sarebbe rosso con il lotto giusto**.
L'invariante è cambiato perché è cambiato il fatto: il lotto non è più un segmento interno, è la coda del file.

## Contesti con spazi iniziali

I primi quattro nomi sono `tip:   Show flagship overlay`, `tip:   Show escort overlays`,
`tip:   Show enemy overlays`, `tip:   Show neutral overlays`: **tre spazi** dopo i due punti. Il checker
dell'handoff confronta il valore dopo `bare()` così com'è, quindi nella cella `Contesti` i nomi vanno copiati
esatti. Ridurli a uno spazio produce un FAIL che sembra un errore di contenuto.

## Le 144 virgolette

Sono **chiavi e valori di `Preferences`** e nomi di gamerule:

- valori di impostazione: `"off"`, `"always on"`, `"when jumping"`, `"focused"`, `"opportunistic"`,
  `"proximity"`, `"expected value"`, `"quality"`, `"value"`, `"mixed"`, `"never"`, `"frugal"`, `"always"`,
  `"flagship only"`, `"escorts only"`, `"on"`, `"series"`, `"parallel"`, `"message"`, `"both"`, `"audio"`,
  `"visual"`, `"when free"`, `"ask"`, `"friendly only"`, `"system default"`, `"none"`, `"player"`, `"all"`,
  `"ship cap"`, `"crew cap"`, `"admin cap"`, `"lock on death"`, `"delete on death"`, `"lock on takeoff"`,
  `"delete on takeoff"`, `"blindspots only"`, `"flagship"`, `"owned ships"`;
- nomi di gamerule e di comando: `"Habitable arrival distance"`, `"Minimum arrival distance"`,
  `"Restricted save loading"`, `"Single save file"`, `"Mouse turning (hold)"`,
  `"Turret aim override (hold)"`, `"Select nearest asteroid"`, `"Board selected ship"`,
  `"Fleet: Toggle ammo usage"`, `"Sell Outfits"`, `"universal ramscoop"`;
- termini tecnici citati: `"weight"`, `"mining"`, `"frugal"`, `"(unset)"`, `"administrative cost"`.

Restano **identici all'inglese** e i due script lo verificano **per unità**, confrontando i testi citati con
quelli del sorgente (nessuna eccezione in questo lotto). Le unità **122–124** hanno la **virgola dentro le
virgolette** (`"ship cap,"`): il sorgente la mette lì e la resa la riproduce.

## Contenuto

- **Sovrapposizioni di stato** (1–7): ammiraglia, scorte, nemici, neutrali, missili, torrette con angoli morti,
  scanner per asteroidi.
- **HUD e radar** (8–23): evidenziazione delle navi, rotazione dell'icona, etichette dei pianeti, mini-mappa,
  radar cliccabile, indicatore di allarme.
- **Mira e fuoco automatici** (25–33): virata col mouse, torrette col mouse, mira automatica (3 unità), fuoco
  automatico, inseguimento delle torrette.
- **Scelte automatiche** (34–50): asteroidi, priorità di abbordaggio, munizioni delle scorte, raccolta del
  detrito.
- **Caccia e flotta** (51–60): riparazione (2 strategie), ritiro dei caccia danneggiati, trasferimento del
  carico, riassunzione dell'equipaggio, parcheggio, priorità dell'ammiraglia.
- **Interfaccia e gioco** (61–93): lampeggio delle scadenze, regioni inesplorate, sistemi delle scorte e degli
  equipaggiamenti immagazzinati, scorciatoie sottolineate, aiuto, avanzamento rapido, tolleranza alle vendite,
  sincronizzazione col blocco maiuscole, zoom, scorrimento, suggerimenti, date, utili in parentesi, notifica
  della destinazione, registro salvato, salvaschermo, rifornimento delle munizioni, tema della barra, angoli
  delle finestre, conferma del tributo.
- **Regole di gioco** (94–131): svalutazione (4 voci), navi personaggio (3), NPC da estrazione, soglia frugale,
  ramscoop universale, distanze di arrivo e partenza (5), moltiplicatore delle flotte, blocco delle regole,
  immunità al fuoco incrociato (4), munizioni universali, flotte di razzia, limiti di flotta (5), morte
  permanente (5), file di salvataggio (2).
- **Pannello di abbordaggio** (132–133): oggetto nel carico, oggetto installato.

## Verifica

```bash
cd staging/editorial/L116_20261019_062253
python mkparts.py   # 133 unità · 80 contesti · 144 virgolette · 1 token · 0 ripetizioni
python check.py     # FAIL totale: 0 (38 controlli)
python verify.py    # exit 0 (47 controlli) — invariante di FILE: 667/667 coperti
```
