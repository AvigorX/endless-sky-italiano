# STATO — L107 · `data/korath/korath missions.txt` (**il Quarg che parla male**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L107_20261018_223650` |
| Righe / unità | **121–212** / **38** |
| Tipi | **34 `MISSION_TEXT`** + **2 `VALUE`** + **2 `DESCRIPTION`** |
| `VALUE` (identici) | 3 `Korath to <planet>` · 20 `Livestock to <planet>` |
| `DESCRIPTION` (tradotte) | 4 (famiglia Korath) · 21 (bestiame) |
| Contesti | **3**: coda di `Setar Fort Heating` (126–127), `Korath Family to Ringworld` (130–169), `Korath Livestock` (172–212) |
| Parole | **1742 EN → 1683 IT** (0,966); per unità 0,79–1,29 |
| Tab · virgolette | **29** · **20**, tutte binate: **zero citazioni aperte** |
| Token | **21** in sei famiglie (`<planet>` 12, **`<bunks>` 3**, `<payment>` 2, `<destination>` 2, `<cargo>` 1, `<tons>` 1) |
| Quadre · ripetizioni | **0** · **0** — asseriti vuoti |
| sha256 | `0c901ea4867f63e3…` |
| `check.py` | **27 controlli**, `FAIL totale: 0` |
| `verify.py` | **30 controlli**, exit **0** |

## Il nodo del lotto: il Quarg che parla male

L'unità 16 è un Quarg che **non padroneggia la lingua** del giocatore e la storpa: *pridefulest*,
*happyfully*, *supplants*, *vicinitied*, *absenced*. Non è un refuso del sorgente: è **caratterizzazione**, e il
narratore lo dice («does not seem to have an especially strong grasp of your language»).

La resa italiana inventa parole trasparenti sulla stessa radice — **orgogliosissimo**, **sproporzionatamente**,
**camerataggine**, **vicinata**, **assenziata** — in modo che la frase resti **comprensibile ma sbagliata**.
Tradurla in italiano corretto cancellerebbe la scena; tradurla in italiano incomprensibile la renderebbe illeggibile.

## Firma dell'unità 16 (quattro virgolette, due discorsi annidati)

```
"Questo individuo orgogliosissimo ha dichiarato che riguardava con reverenza la mia traduzione
debitrice e chiede che il mio uso di essa sia preferito. Sono incline ad acconsentire alla sua
richiesta felicemente." … "Il camerata dice: 'Ti ringrazio sproporzionatamente per aver
riunificato il mio famigliare, in servizio fatidico alla nostra camerataggia.' …"
```

## Il resto

- **`Korath Family to Ringworld`** (unità 3–19): la foschia di **Laki Nemparu**, la famiglia di tre (bambino e
  anziano col bastone), i **500 crediti** scandalosamente bassi, il rifiuto del denaro che il Korath non accetta
  («gonfiano il petto e vi spingono di nuovo i crediti in mano»), la partita a palla nella stiva, la riunione
  allo spazioporto e la traduzione approssimativa del Quarg.
- **`Korath Livestock`** (unità 20–38): il Kor Efret che porta il giocatore in un vicolo, i tre Korath che
  bloccano la fuga, e poi **le «pecore» a sei zampe** — cinque volte più grandi, con una coperta di lana addosso
  come i loro pastori. La mappa di carta, i **10.000 crediti** disegnati col gesso (200 × 5 cerchi + 9 cerchi
  grandi), il carico, il viaggio di un salto con il mal di spazio dei Korath, la vendita della lana e i **4.100 +
  5.900 crediti** che tornano.

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 126 | **25** (solo L106) |
| Unità dopo la riga 212 | **95** |
| Confine | riga **216** apre `phrase:kor efret small package offer` |
| File | **158 unità**, `max(line) = 580` |
| Copertura | **63/158 (39,9%)** |

## Verifica

```bash
cd staging/editorial/L107_20261018_223650
python check.py   # FAIL totale: 0 (27 controlli)
python verify.py  # exit 0 (30 controlli)
```
