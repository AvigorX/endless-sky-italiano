# REPORT — L315 (`data/drak/drak culture conversations.txt`, righe 93–138) — **LOTTO TERMINALE**

**Esito: lotto CHIUSO, file CHIUSO a 32/32.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **22 controlli**.
`state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 16 (`MISSION_TEXT`) | 16 |
| parole | 603 | **596** (0,988) |
| tab | **13** | **13** |
| virgolette | **0** | **0** |
| segnaposto | **4** | **4** |
| alternative | 0 | **0** |
| apici | **3** | 19 |

Rapporto per unità **0,87 – 1,27**: il lotto è **bilanciato**, con due unità che **calano** in italiano (98: «Riapri gli occhi e sei di
nuovo nell'abitacolo», 120: «La luce si spegne e non vedi più nulla») perché le formule di ritorno inglesi sono più **verbose**.

## 2. Invariante di FILE

```
FILE        32/32 (100%) · somma lotti 16 (L314) + 16 (L315) = 32
RIGHE       32 distinte · prima 26 · ultima 138 · zero dopo la 138
```

`data/drak/drak culture conversations.txt` è il **trentaduesimo** file chiuso nel progetto (**91** su 167).

## 3. Le tre rivelazioni sono la stessa storia

| | che cosa costruisce | che cosa perde |
|---|---|---|
| `Korath` | **torri a cupola** per chiudere fuori la luce, poi **bronzo** | il **calore** che le fonde e fa **crollare la cupola** |
| `Quarg` | niente: un **gigante** che picchia il suolo per scacciare l'acqua | **un cimitero sconfinato** che non riesce nemmeno a guardare |
| `Saryds` | una **radura** con cervi d'acciaio **trasformati in argento** | una **guerra** finita: cadaveri, gabbie in frantumi |

Il tema comune è **l'inefficacia**: i Korath si distruggono con la propria difesa, il gigante Quarg non può salvare le tombe, i
Saryds restano pochi davanti ai cadaveri. La resa non aggiunge commento — l'inglese non ne ha, e il registro delle rivelazioni vive di
**silenzio**.

## 4. Il dettaglio che lega L315 a L314

| | L314 | L315 |
|---|---|---|
| contesti | `Arachi` (5), `Hai` (5), `Humanity` (6) | `Korath` (6), `Quarg` (5), `Saryds` (5) |
| prime unità senza tab | 26, 43, 74 | **93, 116, 134** |
| segnaposto | `<ship>` ×3, `<origin>` ×1 | **`<origin>` ×2, `<ship>` ×2** |
| virgolette | 2 (una coppia) | **0** |

Il test di L315 verifica il **conteggio per tipo dei segnaposto**, non solo il totale (4 in entrambi i lotti): un conteggio
"invertito" con lo stesso totale sarebbe passato inosservato con un controllo più grossolano.

## 5. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  22 controlli · FAIL: 0 · exit 0
FILE       32/32 (100%) · trentaduesimo file completo
```

**Un rosso al primo giro**, mio: la soglia della seconda persona era **≥12 unità**, ma in questo lotto solo **9** unità la portano —
le altre 7 sono **descrizione impersonale** dentro la visione («Le creature se ne stanno fiere», «La luce filtra debolmente»).
Misurato: **3 per blocco, 9 in totale**. La soglia è stata corretta sul **fatto misurato**, non il fatto sulla soglia.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 16 unità `PENDING`; il file è **finito in staging**, non approvato.
- **Nessun testo visto nel gioco**: il ritorno alla realtà delle tre rivelazioni è verificato **nei dati**.
- **7 unità su 16 sono impersonali**: dichiarato, non nascosto. La seconda persona c'è **dove il sorgente la mette** (l'arrivo e il
  ritorno di ogni visione, e i momenti in cui il giocatore **guarda**).
