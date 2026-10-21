# STATO — L303 (`data/remnant/remnant ships.txt`, righe 1378–1826)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 38/38 (100%)**, **ventisettesimo file interamente tradotto**
(**86** su 167 nel progetto).

| voce | valore |
|---|---|
| directory | `staging/editorial/L303_20261020_203157/` |
| file | `data/remnant/remnant ships.txt` (**38/38 unità · 1.633 parole · righe 17–1.826 · 35 `DESCRIPTION` + 3 `VALUE`**) |
| righe | 1378–1826 |
| unità | **14**, tutte `DESCRIPTION` |
| contesti | **6** — `Petrel` (3) · `Smew` (3) · `Tern` (3) · `Starling` (2) · `Swan` (2) · `Puffin` (1) |
| terzine | **`Petrel` 1378/1379/1380** · **`Smew` 1488/1489/1490** · **`Tern` 1824/1825/1826** |
| parole | **670 EN → 701 IT** (1,05) |
| rapporto | **0,99 – 1,18** |
| tab | **8** — righe **1379, 1380, 1489, 1490, 1595, 1767, 1825, 1826** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **3 EN / 12 IT** |
| ripetizione | **unità 3 e 7 identiche** (righe 1380 e 1490) + **variante droni** (1826) |
| seconda persona | **3 unità** (3, 7, 14) — avvisi di gioco |
| `check.py` | **25 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **26 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 38 unità · somma **12+12+14** · righe distinte · prima **17** · ultima **1826** · **0 dopo** |
| `sha256[:16]` | **`1c2733c4e66a7841`** |

## Comandi

```bash
python staging/editorial/L303_20261020_203157/check.py     # FAIL totale: 0 (25 controlli)
python staging/editorial/L303_20261020_203157/verify.py    # FAIL: 0 (26 controlli, FILE 38/38)
```

## Gli avvisi di gioco: due identici e una variante

| riga | unità | nave | testo |
|---|---|---|---|
| 1380 | 3 | `Petrel` | «I **caccia** non sono dotati di iperguida. Non puoi trasportare un **caccia**… una **baia di caccia**.» |
| 1490 | 7 | `Smew` | **identico** alla 1380 |
| 1826 | 14 | `Tern` | «I **droni** non sono dotati di iperguida. Non puoi trasportare un **drone**… una **baia per droni**.» |

La forma è **quella del corpus** (esiste già in altri file), non una resa nuova. Il test confronta la 1380 con la costante
`AVVISO_CACCIA` e la 1826 con `AVVISO_DRONI`, poi verifica che la variante differisca **solo** nel sostantivo e nel nome della
baia: `rsplit('una nave con una')` e confronto delle due code.

## La famiglia dell'occultamento arriva a **cinque**

`Gull` (549, L301) · `Merganser` (982) · `Penguin` (1202) · `Peregrine` (1291) (L302) · **`Starling`** (1595, qui).

Il test **riapre entrambi** i `translation.json` precedenti, sostituisce il nome della nave con `X` e confronta: cinque navi, **una
sola frase**. Non è un controllo di presenza — è un controllo di **uguaglianza a meno del nome**.

## Le tre terzine

| riga | contenuto della parte senza tab | tab | tab |
|---|---|---|---|
| `Petrel` 1378 | caccia multiruolo nato come piattaforma armata urbana | 1379 armi a medio raggio | 1380 avviso iperguida |
| `Smew` 1488 | scialuppa diventata ibrido mercantile-caccia | 1489 spazio libero in vendita | 1490 avviso iperguida |
| `Tern` 1824 | drone dal guscio spesso per i giganti gassosi | 1825 schermo senza equipaggio | 1826 avviso iperguida |

Ogni terzina chiude con lo **stesso tipo di nota pratica**: è una **struttura del file**, non una coincidenza.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `fighter bay` | **baia di caccia** | corpus (9 vs 2 «baia per caccia») |
| `drone bay` | **baia per droni** | corpus |
| `hyperdrive` | **iperguida** | corpus |
| `ramscoop` | **ramscoop** | corpus (invariato) |
| `screening ships` | **navi di schermo** | corpus |
| `lifeboats` | **scialuppe di salvataggio** | |
| `drone bays` | **baie per droni** | |
| `Archons` | **gli Archon** | corpus («l'Archon», collettivo) |
| `Ember Waste` | **`Ember Waste`** | invariato (anomalia aperta) |

## Limiti dichiarati

Nessuna approvazione (14 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
