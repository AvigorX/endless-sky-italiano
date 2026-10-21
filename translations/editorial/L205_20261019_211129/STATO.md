# STATO — L205 · `hai outfits.txt` (quinto e **ultimo** lotto) — **FILE CHIUSO**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L205_20261019_211129` |
| Righe / unità | **805–984** / **13** — file a **65/65 (100%)** |
| Tipi | {'DESCRIPTION': 13} |
| Tab · virgolette · apici | **1** (unità 13) · **2** (unità 3) · **1 EN / 4 IT** |
| Segnaposto | **0** (asserzione negativa scritta) |
| Contesti | **12** da 13 unità (Shield Beetle Pendant ne ha due: righe 983 e 984) |
| Parole | **520 EN → 524 IT** (rapporto 1,00–1,27, media 1,12) |
| sha256 | `968d32112e56b1d4…` |
| Esiti | `check.py` **23** (`FAIL totale: 0`) · `verify.py` **16** (`FAIL: 0`) |

## Perché è un lotto terminale

Non esiste un confine «dopo»: l'ultima unità del file è la riga **984** e `line > 984` vale **0**. Il `verify.py` usa
l'**invariante di FILE**: le cinque finestre reali (L201 8, L202 16, L203 9, L204 19, L205 13) devono coprire **tutte**
le righe del database per quel percorso — 65 distinte, nessun buco, nessuna sovrapposizione.

| finestra | righe | unità |
|---|---|---|
| L201 | 27–164 | 8 |
| L202 | 205–484 | 16 |
| L203 | 508–600 | 9 |
| L204 | 603–788 | 19 |
| L205 | 805–984 | 13 |
| **totale** | **27–984** | **65** |

## Cosa contiene

Propulsori e manovra Hai (`"Bondir"`, `"Bufaer"`, e i retropulsori `"Basrem"`, `"Benga"`, `"Biroo"`), il Pulse Rifle,
e il **ciondolo di Nanachi**: l'unità 12 descrive l'oggetto, la 13 — indentata — la teca che lo contiene.

## Difficoltà

1. **Coppia oggetto/confezione** (unità 12–13): stessa struttura di L203 (chiave di volta). Il tab è verificato in entrambe le lingue, e la continuità della 13 è dichiarata.
2. **Due virgolette dentro un nome** (`"Basrem" Reverse Thrusters`, unità 3): conservative, e il controllo verifica che stiano **nella stessa unità** in inglese e in italiano.
3. **Punteggiatura del sorgente**: i tre punti dell'unità 10 stanno **a metà frase** (`...sempre che potessero permettersi...`), non in coda; i due trattini dell'unità 13 sono trattini, non lineette. Entrambi verificati contro il conteggio inglese.
4. **«chiavi di volta quantistiche»** al plurale (unità 13): prosegue la scelta di L200/L203, mai «pietra chiave».
5. **Prima asserzione sbagliata mia**: pretendevo che l'unità 10 finisse con `...`; non finisce, perché la frase continua. Corretta contando i `...` in entrambe le lingue.

## Verifica

```bash
cd staging/editorial/L205_20261019_211129
python check.py     # FAIL totale: 0 (23 controlli)
python verify.py    # FAIL: 0 (16 controlli) · FILE CHIUSO 65/65
```

**Non verificato**: nessun equipaggiamento installato nel gioco, nessuna schermata vista, nessuna revisione umana; 13 unità `PENDING`.
