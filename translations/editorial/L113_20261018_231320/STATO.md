# STATO — L113 · `data/_ui/tooltips.txt` (**87 contesti per 96 unità**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L113_20261018_231320` |
| Righe / unità | **691–973** / **96** |
| Tipo | **96 `TUTORIAL_TIP`**, nient'altro |
| Stati | **96 `PENDING`** — misurato con `select state` e **asserito** in `mkparts.py` |
| Contesti | **87** — **nove contengono due unità** (`turning`, `outfitter: b/s/i/u/c/r`, `shipyard: b`, `capacity`) |
| Parole | **1808 EN → 1864 IT** (1,031); per unità 0,87–1,54, media 1,16 |
| Tab · token · quadre · ripetizioni | **0** · **0** · **0** · **0** |
| Virgolette | **22** (9 unità con 2, una con 4) |
| sha256 | `dc0775e3161aa2b4…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **38 controlli**, exit **0** |

## Contesti meno delle unità

Nelle prime due finestre del file ogni suggerimento aveva il suo contesto. Qui no:

| contesto | unità | cosa contiene |
|---|---|---|
| `tip:turning:` | **2** (38, 82) | la descrizione fisica della virata e la voce del pannello di consumo |
| `tip:outfitter: b` | **2** (59, 60) | «Acquista…» e la scorciatoia Shift/Control/Alt |
| `tip:outfitter: s` `i` `u` `c` `r` | **2 ciascuno** (61–70) | la stessa coppia azione + scorciatoia |
| `tip:shipyard: b` | **2** (71, 72) | «Acquista questa nave» + scorciatoia |
| `tip:capacity:` | **2** (88, 89) | capacità energetica e capacità termica |

Le altre **78** unità hanno un contesto proprio. Un `verify.py` che assume «un contesto per unità» — la forma usata
in L111 e L112 — qui **fallisce su un lotto corretto**: il controllo è scritto come «87 contesti, nove doppi, nessuno
triplo», con l'elenco dei nove.

## Le 22 virgolette

Sono le **etichette del pannello citate nel testo**, non discorso:

- unità 78–86: `Si somma alla quantità "inattiva".` — nove occorrenze di `"inattiva"`;
- unità 89: `Se il valore di "variazione netta" del calore…` e `…anche se la "variazione netta" resta sotto…` —
  **quattro** virgolette nella stessa unità, perché l'etichetta è citata due volte.

Nella finestra precedente le virgolette erano **zero**: il numero va misurato, non ereditato.

## Contenuto

- **Scudi e motori** (1–8, 23–52): protezione e resistenza agli scudi, suoni silenziosi, raccolta solare, **spinta**
  e **virata** con le rispettive dodici voci di consumo e danno.
- **Scanner** (11–22): strategico, tattico, mobilità (tre varianti), equipaggio, energia, carburante, manovra,
  telemetro, termico, armi — tutti con «la portata è proporzionale alla radice quadrata di questo valore».
- **Alloggiamenti** (53–56): torrette montabili, spazio armi.
- **Scansione del carico** (57–58): visibilità e occultamento, con la multa evitata.
- **Pannelli outfitter e shipyard** (59–76): sei azioni con la loro scorciatoia, vendita di scafi senza
  equipaggiamenti, prezzo della nave vuota e dei suoi equipaggiamenti.
- **Consumi** (77–90): inattiva, in movimento, spinta, spinta inversa, postbruciatore, virata, sparo, scudi e scafo
  insieme, riparazione, ricarica, **variazione netta**, capacità energetica e termica, picco.
- **Categorie del pannello armi** (91–96): Cannoni, Torrette, Armi secondarie, Munizioni, Sistemi, Energia.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 691 | **224** (L111+L112) |
| Unità dopo la riga 973 | **347** |
| Confine | riga **976** apre `tip:Engines:` |
| File | **667 unità**, `max(line) = 1865` |
| Copertura | **320/667 (48,0%)** |

## Verifica

```bash
cd staging/editorial/L113_20261018_231320
python mkparts.py   # 96 unità · 87 contesti · 9 doppi · tutte PENDING
python check.py     # FAIL totale: 0 (30 controlli)
python verify.py    # exit 0 (38 controlli)
```
