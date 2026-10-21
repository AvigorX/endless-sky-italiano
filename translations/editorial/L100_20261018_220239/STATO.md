# STATO — L100 · `data/hai/hai culture conversations.txt`

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L100_20261018_220239` |
| Righe / unità | **212–320** / **44** |
| Tipi | **41 `MISSION_TEXT`** + **3 `UI_LABEL`** (`field trip`, `pleasant lunch`, `finishing chat`) |
| Contesti | **2** in ordine di riga: `Academy Motto` (227–263), `Robotic Musical 1` (278–306) |
| Parole | **1587 EN → 1512 IT** (0,953); per unità 0,76–1,57 |
| Tab · virgolette | **39** · **40**, con **quattro citazioni aperte e non chiuse** (unità 23, 24, 39, 41) |
| Token · quadre | **1** (`<last>`, unità 40) · **0** |
| Ripetizioni | **nessuna** (asserita vuota) |
| sha256 | `8fb5defc43780334…` |
| `check.py` | **30 controlli**, `FAIL totale: 0` |
| `verify.py` | **28 controlli**, exit **0** |

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 227 | **77** (L98 + L99) |
| Unità dopo la riga 306 | **26** |
| Confine | riga **321** apre `mission:Hai Film Release` |
| File | **147 unità**, `max(line) = 386` |
| Copertura | **121/147 (82,3%)** |

## Contenuto

**Academy Motto**: lo spazioporto bloccato per sette ore, la scelta fra la console di gioco e una passeggiata in
città, il caffè con l'ologramma che chiede se ordinare dal tavolo o da una persona, il panino con **burro di
ghiande**, il cartello «Niente contenuti meme qui, per favore», e il **motto dell'Academy** sul cancello:
«Conoscere è guidare, studiare è conoscere, servire è studiare, guidare è servire». La cameriera spiega che il
motto non è al contrario — le Academy controllano i diplomati e possono revocare le qualifiche.

**Robotic Musical 1**: le casse che prendono vita nel viale dello spazioporto, sei caricature robotiche di Hai, il
traduttore che non riesce a stare dietro ai giochi di parole, la pubblicità di «**Le regole della nonna**», e il
capitano mercantile che riconosce il dispositivo di traduzione e poi il giocatore: «lei è il Capitano `<last>`!».

## Verifica

```bash
cd staging/editorial/L100_20261018_220239
python check.py   # FAIL totale: 0 (30 controlli)
python verify.py  # exit 0 (28 controlli)
```
