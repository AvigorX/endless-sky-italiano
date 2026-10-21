# STATO — L162 · `avgi outfits.txt` (serbatoi criogenici, sensori e scudi degli Avgi)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L162_20261019_175111` |
| Righe / unità | **112–193** / **10** — file al **21/63 (33,3%)** |
| Tipi | **10 `DESCRIPTION`** · **0 `VALUE`** |
| `UI_LABEL` | **0** — asserzione vuota scritta |
| Token | **0** — asserzione vuota scritta |
| Contesti | **6** (Cryogenic 1, Heatsink 1, Multispectral 2, Spectrometer 2, Diffuse 2, Specular 2) · **10 testi distinti** |
| Parole | **565 EN → 601 IT** (1,064); **1,01–1,22**, media **1,09** |
| Tab · virgolette | **4 unità** · **0** |
| sha256 | `2a85b71584753049…` |
| Esiti | `check.py` **24** (`FAIL 0`) · `verify.py` **18**, exit **0** |

## Cosa contiene

| blocco | unità | righe | contenuto |
|---|---|---|---|
| serbatoi | 1-2 | 112-125 | `Cryogenic Deuterium Tank`, `Heatsink Partition` |
| sensori | 3-6 | 139-159 | `Multispectral Scanner` (2 unità), `Spectrometer Array` (2 unità) |
| scudi | 7-10 | 175-193 | `Diffuse Deflector` (2 unità), `Specular Deflector` (2 unità) |

## Rese che contano

| EN | IT |
|---|---|
| `insulated pressure vessel` | **serbatoio in pressione coibentato** |
| `deuterium slush tank` | **serbatoio a poltiglia di deuterio** (lessico di L161) |
| `lithium hydride nanofluid` | **nanofluido di idruro di litio** |
| `phased array radar` | **radar a schiera in fase** |
| `neutron-detecting helium-3 tubes` | **tubi all'elio-3 per la rilevazione dei neutroni** |
| `spectral signatures` | **firme spettrali** |
| `superconducting magnetic energy storage` | **accumulo superconduttivo di energia magnetica** |
| `anemic generator` | **generatore anemico** |

## Verifica

```bash
cd staging/editorial/L162_20261019_175111
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # exit 0 (18 controlli)
```

**Segmento**: 11 unità prima della riga 112, 10 nel lotto, 42 dopo la 193; confine alla riga 209.

**Non verificato**: nessuna nave o equipaggiamento visto a schermo; i testi non sono stati caricati nel gioco.
