# STATO — L276 (`data/korath/korath ships.txt`, righe 1375–1961)

**Stato: CHIUSO.** Quarto lotto del file: **12 `DESCRIPTION`** su **dieci navi** — tre Efreti e sette Kor Sestor robotiche. Il
file è aperto a **43/50 (86,0%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L276_20261020_174654/` |
| file | `data/korath/korath ships.txt` (50 unità · 2.049 parole · righe 95–2363) |
| righe | 1375–1961 |
| unità | **12** — tutte `DESCRIPTION` |
| parole | **453 EN → 474 IT** (1,05) |
| rapporto | **0,92 – 1,16** |
| contesti | **10** — `Echo-Galleon`, `Arch-Carrack`, `Charm-Shallop`, `Kar Ik Vot 349`, `Tek Far 71 - Lek`, `Tek Far 78 - Osk`, `Tek Far 109`, `Met Par Tek 53`, `Far Lek 14`, `Far Osk 27` |
| tab | **2** (unità 10, 12) |
| virgolette | **2** (unità 1, `"navi-mondo"`), dritte |
| apici | **2 EN** (`Efreti's`) / **7 IT** su 6 unità |
| segnaposto | **0** (asserzione negativa) |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 31 prima · 12 qui · **7 dopo** la 1961 |
| `sha256[:16]` | **`34f555cb0f44679d`** |

## Comandi

```bash
python staging/editorial/L276_20261020_174654/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L276_20261020_174654/verify.py    # FAIL: 0 (21 controlli, 43/50)
```

## Due famiglie di navi

- **Efreti** (tre navi): vivono **sotto la protezione dei Quarg**, non provvedono alla propria difesa, trasportano civili e
  merci. Il loro `Echo-Galleon` è il **discendente** delle vecchie navi-mondo: più leggero e più veloce, ma **meno potente**
  delle controparti dell'Esilio.
- **Kor Sestor** (sette navi): **robotiche**. Il `Kar Ik Vot 349` è «la più grande e letale»; le tre portatrici
  (`Tek Far 71 - Lek`, `78 - Osk`, `109`) reggono flotte di caccia e droni; `Met Par Tek 53` è la più piccola ma **più grande
  di quasi tutte le navi capitali umane**.

## Le due note tecniche, riprese dal corpus

Le unità 10 e 12 sono le note «senza iperguida» di droni e caccia, **identiche** a stringhe già presenti decine di volte. Il
`check.py` le confronta con la resa **più frequente** dello staging: «baia per droni» (9) e «baia di caccia» (8, contro 2
varianti «baia per caccia»).

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **7 unità** (L277,
terminale).
