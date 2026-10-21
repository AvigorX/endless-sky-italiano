# STATO — L215 · `deep jobs.txt` (quarto lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L215_20261019_215631` |
| Righe / unità | **684–864** / **25** — file a **127/187** tradotte **+ 1 `UI_LABEL`** (67,9%) |
| Tipi | {'MISSION_TEXT': 15, 'VALUE': 5, 'DESCRIPTION': 5} |
| Tab · virgolette · apici | **14** · **29** · **14 EN / 8 IT** |
| Segnaposto | **15** su 4 simboli (`<planet>` 5, `<destination>` 5, `<payment>` 4, **`<date>` 1**) |
| Contesti | **6** — da `Deep Security Package Reveal` a `Deep Consultants` |
| Parole | **431 EN → 427 IT** (rapporto 0,93–1,22, media 1,07) |
| sha256 | `0b4212a734b678ff…` |
| Esiti | `check.py` **25** (`FAIL totale: 0`) · `verify.py` **19** (`FAIL: 0`) |

## Il tratto del lotto: una battuta da tenere in piedi

Wayde dice *at any rate* due volte — chiude l'unità 1 e apre la 2 — e il giocatore glielo fa notare nell'unità 6, **citando
la frase fra apici singoli**. Se la resa cambia espressione in uno dei tre punti, la battuta non funziona più.

Ho fissato **«in ogni caso»** e il controllo verifica che compaia **tre volte** in entrambe le lingue, che chiuda l'unità
1, che apra la 2 e che sia citato nella 6. È il primo controllo della campagna su un **legame comico** fra unità.

## La citazione su due paragrafi

L'unità 1 apre la citazione e **non la chiude**: la virgoletta singola in apertura è la convenzione del gioco per i
paragrafi successivi di una stessa battuta. Totale: **29 virgolette** con distribuzione per unità

```
1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0
```

Il controllo confronta la distribuzione **unità per unità** in entrambe le lingue, e verifica esplicitamente che l'unità 1
cominci con `"` e **non finisca** con `"`.

## Cosa contiene

La chiusura dell'incontro con **Wayde** (l'offerta di entrare nella lista dei piloti fidati, la battuta, l'addio), due
missioni di trasporto `Basic`, due `Deep Security`, e l'arrivo di **Julie** e della sua assistente, che hanno perso il
trasporto e hanno una **scadenza** (`<date>`).

## Difficoltà

1. **La battuta**, appunto: tre occorrenze legate, in due lingue.
2. **`<date>` per la prima volta**: sta solo nell'unità 22 e la resa non deve aggiungere articoli che il segnaposto non
   conosce («entro `<date>`», non «entro il `<date>`»).
3. **Registro «tu»** anche rivolgendosi a Wayde e alla donna: «Accomodati», «scusa», nessun «mi scusi».
4. **Le 10 unità di missione** hanno 3 testi di `VALUE` e 3 di `DESCRIPTION`: famiglie con dimensioni `[1, 2, 2]` in
   entrambe le lingue.
5. **L'`UI_LABEL` della riga 683 è fuori dalla finestra**: le unità prima della 684 sono **103**, non 102, e il conto
   dell'invariante diventa `127 + 1 + 59 = 187`.

## Verifica

```bash
cd staging/editorial/L215_20261019_215631
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # FAIL: 0 (19 controlli) · invariante con l'UI_LABEL
```

**Non verificato**: nessuna missione giocata, nessuna battuta letta a schermo; 25 unità `PENDING`.
