# STATO — L73 · `data/successors/successor 2 ghosts aqrabe.txt`

**Lotto chiuso.** Primo lotto su un file nuovo della linea Successors: Casa Aqrabe, il reliquiario dei
«santi» e le pietre chiave quantistiche. Il file prosegue (riga 161 apre `Aqrabe 3`).

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L73_20261018_195325` |
| File | `data/successors/successor 2 ghosts aqrabe.txt` (nuovo, primo lotto) |
| Unità | **51** (righe 23–158; finestra 1–158) |
| Parti | **3** — 17 · 18 · 16 |
| Contesti | **5** — `Ghosts Aqrabe 1`, `conversation:successor keystone delivery`, `… Remnant`, `… Hai`, `… Aqrabe 2` |
| Tipi | **35 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION` + 3 `LOGBOOK` + 6 `CONVERSATION` + 1 `DIALOG`** |
| Parole | 1330 EN → 1281 IT (**0,963**) |
| Rapporto per unità | **0,72 – 1,56** (gate 0,55–1,90) |
| `NT` | **1** — unità **43**, categoria di diario `People` (resta identica) |
| `LOGBOOK` | **3** — testi **30** e **51** (forma diretta), categoria **43** (`log "People" "Tiliia" "…"`) |
| `CONVERSATION` | **6** — unità **31–36**: è il **testo visibile** del blocco, tradotto come prosa |
| `DIALOG` | **1** — unità **50**, testo di un blocco `dialog`, tradotto |
| `UI_LABEL` / `TEXT` | **0 / 0** — assenze dichiarate |
| Token `<…>` | **9** in 6 famiglie: `<ship>` 2, `<last>` 2, `<destination>` 2, `<first>` 1, `<stopovers>` 1, `<planet>` 1 |
| Tab · virgolette | **42** su 38 unità con tab iniziale · **90** (0 dispari, 0 quadre, 0 backtick) |
| Duplicati inglesi | **0 gruppi** |
| sha256 `translation.json` | `1cd04c9a55a1312c…` |
| `check.py` | **35 controlli**, `FAIL totale: 0` |
| `verify.py` | **47 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della riga 23 | **0** (il lotto apre il file) |
| Unità dopo la riga 158 | **129** |
| File | **180 unità**, `max(line) = 478` |
| Confine dopo | riga **161** apre `mission:Successors: Ghosts Aqrabe 3` |

Copertura del file: **51/180 = 28,3%**. Invariante di segmento: `(23, 158)`, 0 prima, 129 dopo.

## Cosa è stato deciso qui

1. **`CONVERSATION` è testo, non etichetta**: le sei unità sono il corpo di un blocco `conversation`,
   delimitato da backtick e già privo del delimitatore nell'`english`. Tradotte come prosa; il `verify.py`
   asserisce il **conteggio** (6) e che nessuna resti identica all'inglese.
2. **La categoria di diario `People` resta identica** (unità 43), in `NT`, come in L68: le altre categorie
   del file non sono inventariate, e tradurne una sola creerebbe una categoria doppia nel diario.
3. **`keystone` → «pietra chiave»**: forma già in staging (3 occorrenze), con «quantistica» quando
   l'inglese dice `quantum`. I nomi di missione usano la maiuscola del gioco: «Pietre Chiave Quantistiche».
4. **Aqrabe I- Sola**: nome e titolo invariati, come `Myurej M- Khiajsore`. Il personaggio parla in modo
   cerimonioso ma **ironico**; Tiliia (l'ingegnere) è più diretta e usa anch'ella il «tu» formale.
5. **`weft-weaving armor` / `multimodal armor`**: due espressioni per la stessa cosa, rese diversamente
   («corazza tessuta» / «corazza plurimodale») perché l'inglese le distingue in due unità diverse.
6. **I «santi»** sono arti recisi in un serbatoio, con voci artificiali che parlano in frammenti: la
   traduzione lascia i frammenti frammentati (unità 8–13), senza ricomporli in frasi compiute.
7. **`<stopovers>`** entra per la prima volta: parità per simbolo su una sola occorrenza.

## Verifica

```bash
cd staging/editorial/L73_20261018_195325
python check.py                 # FAIL totale: 0   (35 controlli)
python verify.py                # exit 0           (47 controlli)
```

## Prossimo passo

**L74** continua lo stesso file: righe **159–255** (prima unità alla **161**), **38 unità**, **1.106 parole**,
**2 contesti** (`Aqrabe 3` e `Aqrabe 4`), tab **28** su 28 unità, virgolette **68**, **10 token** in
4 famiglie (`<ship>` 6, `<planet>` 2, `<origin>` 1, `<destination>` 1), tipi `32 MISSION_TEXT + 2 VALUE +
2 DESCRIPTION + 1 LOGBOOK + 1 UI_LABEL`. Confine dopo: riga **259** apre `mission:Successors: Ghosts Aqrabe 5`.
