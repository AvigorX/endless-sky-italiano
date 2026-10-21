# STATO — L305 (`data/quarg/quarg outfits.txt`, righe 138–243)

**Stato: CHIUSO.** Secondo lotto del file: **dieci schede** in **otto contesti** — la **seconda metà** di
`Large Graviton Steering`, **due coppie** e **sei singole**, fra cui i **tre generatori di scudi**. File a **21/31 (67,7%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L305_20261020_204423/` |
| file | `data/quarg/quarg outfits.txt` (**31 unità · 1.506 parole · righe 37–579 · 31 `DESCRIPTION`**) |
| righe | 138–243 |
| unità | **10**, tutte `DESCRIPTION` |
| contesti | **8** — 6 singole + 2 coppie + la 2ª metà di `Large Graviton Steering` |
| coppie | `Singularity Core` 180/181 · `Quasar Core` 195/196 |
| singole | `Quantum Vacuum Battery` 153 · `Antimatter Core` 166 · `Aspis` 213 · `Ancile` 228 · `Aegis` 243 |
| parole | **510 EN → 529 IT** (1,04) |
| rapporto | **0,99 – 1,24** |
| tab | **3** — righe **138, 181, 196** |
| virgolette / segnaposto / alternative | **0 / 0 / 0** (asserzioni vuote) |
| apici | **2 EN / 6 IT** |
| `check.py` | **23 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **24 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **11 prima** · 10 qui · **10 dopo** la 243 |
| `sha256[:16]` | **`f067a63cbdd8ea64`** |

## Comandi

```bash
python staging/editorial/L305_20261020_204423/check.py     # FAIL totale: 0 (23 controlli)
python staging/editorial/L305_20261020_204423/verify.py    # FAIL: 0 (24 controlli)
```

## La continuità 137/138

La **137** (L304) è la **prima** metà di `Large Graviton Steering`, la **138** (qui) la **seconda**, con la tab. Il test verifica la
coppia **sui due lati** e confronta il **ritornello** con le quattro unità identiche di L304: la resa è **una sola**.

## I reattori: il lotto parla di astrofisica

| riga | oggetto | idea |
|---|---|---|
| 153 | **batteria** | energia da **radere al suolo una piccola città**, immagazzinata nella **pressione negativa del vuoto quantistico**; si **raffredda** mentre si scarica, «in spregio alla termodinamica» |
| 166 | **nucleo di antimateria** | i Quarg ne producono abbastanza per **navi civili**, in un **involucro semplice ed elegante** |
| 180/181 | **nucleo a singolarità** | un **buco nero microscopico** alimentato da un filo di massa; la **radiazione di Hawking** cresce man mano che si restringe; «scienziati e complottisti» dicono che i Quarg **ingannano le leggi della fisica** per farlo pesare poco |
| 195/196 | **nucleo quasar** | il buco nero riceve massa sufficiente a formare un **disco di accrescimento**; meno efficiente, ma la **densità di potenza** vale il compromesso |

## I tre scudi: nomi greci, testo invariato

`Aspis` (213), `Ancile` (228), `Aegis` (243) sono **schede singole** e **non nominano se stesse** nel testo: dicono «questo generatore
di scudi Quarg». Il test verifica che i nomi **non** vengano italianizzati («Aspide», «Egida») e che il testo parli di **Quarg** e dei
nuclei per nome.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `black hole` | **buco nero** | |
| `Hawking radiation` | **radiazione di Hawking** | |
| `event horizon` | **orizzonte degli eventi** | |
| `accretion disk` | **disco di accrescimento** | |
| `quantum vacuum pressure` | **pressione del vuoto quantistico** | |
| `waste heat` | **calore di scarto** | |
| `shield generators` | **generatori di scudi** | corpus |

## Limiti dichiarati

Nessuna approvazione (10 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **10 unità**: il
prossimo lotto è **terminale**.
