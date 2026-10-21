# STATO — L315 (`data/drak/drak culture conversations.txt`, righe 93–138)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 32/32 (100%)**, **trentaduesimo file interamente tradotto** (**91** su 167
nel progetto). `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **22 controlli**. `state.py` esce 0 (`ESITO: OK`,
8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L315_20261020_215321/` |
| file | `data/drak/drak culture conversations.txt` (**32/32 unità · 1.153 parole · righe 26–138**) |
| righe | 93–138 |
| unità | **16** — tutte `MISSION_TEXT` |
| contesti | **3** — `Korath` (6), `Quarg` (5), `Saryds` (5) |
| parole | **603 EN → 596 IT** (0,988) |
| rapporto | **0,87 – 1,27** |
| tab | **13** — tutte tranne le prime dei blocchi (93, 116, 134) |
| virgolette | **0** |
| segnaposto | **4** — `<origin>` ×2, `<ship>` ×2 (conteggio **invertito** rispetto a L314) |
| alternative | **0** |
| apici | **3 EN / 19 IT** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 32 unità · somma lotti **16+16** · 32 righe distinte · prima **26** · ultima **138** · **0 dopo** |
| `sha256[:16]` | **`bc21cf2aa1469868`** |

## Comandi

```bash
python staging/editorial/L315_20261020_215321/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L315_20261020_215321/verify.py    # FAIL: 0 (22 controlli, FILE 32/32)
```

## Tre rivelazioni, la stessa struttura di L314

| contesto | righe | unità | che cosa si vede |
|---|---|---|---|
| `Drak Revelations: Korath` | 93–98 | 6 | creature di **terra e ruggine** che costruiscono **torri a cupola** per chiudere fuori la luce, poi si fondono in **bronzo** e il calore **fa crollare tutto** |
| `Drak Revelations: Quarg` | 116–120 | 5 | un **gigante scarno** color oro pallido che picchia il suolo e cerca di scacciare l'acqua da un cimitero sconfinato: **le tombe** che non riesce a guardare |
| `Drak Revelations: Saryds` | 134–138 | 5 | una **radura** al posto del corridoio, **cervi d'acciaio** trasformati in **argento**, i giganti che **ingabbiano** piccoli animali, poi il **temporale**, i **cadaveri** e le **gabbie in frantumi** |

## Che cosa hanno in comune le tre rivelazioni

Sono **tre versioni della stessa storia**: una civiltà che **costruisce per difendersi dalla luce**, un **lutto impossibile**, una
**guerra persa**. La struttura è identica e il test la verifica:

```
prima unità  senza tab   →  il passaggio alla visione
5–6 unità    con tab     →  la visione
ultima unità con tab     →  il ritorno (abitacolo della <ship>, luci della nave, porta del tuo abitacolo)
```

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| blocchi | 6 + 5 + 5; prime senza tab (93, 116, 134), le altre 13 con la tab **in prima posizione** |
| segnaposto | identici, **conteggio invertito** (`<origin>` ×2, `<ship>` ×2) |
| vuote | **0 virgolette**, 0 alternative |
| apici | **3** in inglese, righe **120, 134, 138** |
| seconda persona | **≥3 unità per blocco**, ≥9 in tutto |
| contenuti | ruggine/cupola/bronzo/crollo · scarno/tombe/nebbia · cervi d'acciaio/argento/gabbie/fulmini/cadaveri |
| FILE | 32 unità · **16+16** · prima 26 · ultima 138 · **0 dopo** · copertura **32/32 asserita** |

## Limiti dichiarati

Nessuna approvazione (16 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in staging**,
non approvato.
