# STATO — L103 · `data/quarg/quarg missions.txt` (quattro tipi, e la regola sui `VALUE`)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L103_20261018_221731` |
| Righe / unità | **118–249** / **42** |
| Tipi | **28 `MISSION_TEXT`** + **8 `DIALOG`** + **3 `DESCRIPTION`** + **3 `VALUE`** |
| `VALUE` (identici) | unità **1**, **21**, **39**: `Deploy Quarg Scanners`, `Human Construction Materials` ×2 |
| Contesti | **3** in ordine di riga: `Quarg Satellites` (124–176), `Lagrange Ring: Cargo` (182–224), `Lagrange Ring: Cargo Job` (228–249) |
| Parole | **956 EN → 882 IT** (0,923); per unità 0,69–1,22 |
| Tab · virgolette | **25** · **43**, con **una citazione aperta** (unità 30) |
| Token · quadre | **19** in sei famiglie (`<destination>` 4, `<stopovers>` 3, `<cargo>` 5, `<payment>` 5, `<waypoints>` 1, `<system>` 1) · **0** |
| Ripetizioni | **5 gruppi**: 8/12, 10/13, 21/39, 22/40, 36/41 |
| sha256 | `2e3f270bdda5ce6a…` |
| `check.py` | **28 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## La regola dei `VALUE`

Le tre unità `VALUE` sono **nomi di missione e di carico**: `Deploy Quarg Scanners` è il titolo del lavoro sul
tabellone, `Human Construction Materials` è la designazione del carico. Il gioco li usa come **identificatori**:
restano **identici all'inglese**, come le `UI_LABEL` di L95–L96, e sono **asseriti uno per uno** (uguaglianza, non
esclusione). La traduzione di nomi di missione e carico è una **decisione di campagna** che richiede un inventario
globale — non si fa lotto per lotto.

`DESCRIPTION` e `DIALOG`, invece, sono testo mostrato al giocatore e sono tradotti **per intero**.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 124 | **48** (L102) |
| Unità dopo la riga 249 | **88** |
| Confine | riga **265** apre `mission:Ask Quarg About Coalition Early` |
| File | **178 unità**, `max(line) = 506` |
| Copertura | **90/178 (50,6%)** |

## Contenuto

- **`Quarg Satellites`**: la proposta del Quarg — quattro satelliti di scansione da dispiegare per proteggere gli
  umani «dall'altra parte di questa regione»; le piramidi triangolari sormontate da piramidi più piccole; i
  `DIALOG` del dispiegamento, compreso quello su **Poisonwood**, ex colonia di schiavi.
- **`Lagrange Ring: Cargo`** e **`Lagrange Ring: Cargo Job`**: la richiesta di trasporto per la prima sezione del
  **mondo ad anello** aperta ai visitatori umani, il datapad, lo scarico «sotto stretta sorveglianza» e il Quarg
  che consegna il pagamento a metà lavoro.

## Verifica

```bash
cd staging/editorial/L103_20261018_221731
python check.py   # FAIL totale: 0 (28 controlli)
python verify.py  # exit 0 (28 controlli)
```
