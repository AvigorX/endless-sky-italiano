# STATO — L289 (`data/gegno/gegno ships.txt`, righe 1193–1616)

**Stato: CHIUSO — LOTTO TERMINALE.** Il file è **completo: 37/37 (100%)**, **ventitreesimo file interamente tradotto** su 167.

| voce | valore |
|---|---|
| directory | `staging/editorial/L289_20261020_190559/` |
| file | `data/gegno/gegno ships.txt` (**37/37 unità · 2.036 parole · righe 53–1.616**) |
| righe | 1193–1616 |
| unità | **12**, tutte `DESCRIPTION` |
| parole | **647 EN → 718 IT** (1,11) |
| rapporto | **1,06 – 1,27** |
| contesti | **8** — `Halite` ×2 · `Mica` · `Coesite` · `Tridymite` · `Felsic` · `Feldspar` ×2 · `Epidote` ×2 · `Kyanite` ×2 |
| coppie consecutive | **4** — 1193–1194, 1480–1481, 1547–1548, 1615–1616 |
| tab | **5** (righe 1193, 1194, 1481, 1548, 1616) |
| virgolette | **0** · apici **4 EN / 5 IT** |
| segnaposto / alternative | **0 / 0** (asserzioni vuote) |
| seconda persona | **1 sola unità** (riga 1194, istruzione di gioco) |
| `check.py` | **24 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **21 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di FILE**: 37 unità · somma lotti **7+9+9+12** · righe distinte · ultima **1616** · **0 dopo** |
| `sha256[:16]` | **`82591c748393fdf3`** |

## Comandi

```bash
python staging/editorial/L289_20261020_190559/check.py     # FAIL totale: 0 (24 controlli)
python staging/editorial/L289_20261020_190559/verify.py    # FAIL: 0 (21 controlli, FILE 37/37)
```

## L'unica unità in seconda persona

Tutte le schede sono impersonali — tranne la riga **1194**:

> «I velivoli da combattimento non sono dotati di iperguida. **Non puoi trasportare** un velivolo da combattimento se non hai
> nella **tua** flotta una nave con una **baia di caccia**.»

Non è prosa di finzione: è un'**istruzione di gioco** che parla al giocatore. Il test la **dichiara** come unica eccezione
(`[u['line'] for u in tu if re.search(...)] == [1194]`) e verifica che le altre undici restino impersonali. Il registro non è
«sempre terza persona»: è **terza persona tranne dove il gioco parla al giocatore**, e la differenza va scritta.

L'istruzione usa **«baia di caccia»** — la forma maggioritaria del corpus (9 contro 2 di «baia per caccia»); il test rifiuta
l'altra.

## Il `Halite` che arriva da L288

L288 chiudeva la scheda del `Halite` con «…quasi metà dello scafo è dedicata a questi nuovi sviluppi.» L289 riprende con
«**Capaci** di portare uno sciame di danni istantanei…». Il test verifica **due** cose: che la riga 1192 di L288 esista e
finisca con «nuovi sviluppi.», e che questa unità cominci con «Capaci» e **non** con «Gli Halite».

## I cinque tab: due sulla stessa nave

`Halite` ha **entrambe** le righe rientrate (1193 e 1194); le altre coppie hanno il tab solo sulla **seconda metà**. Il test
verifica l'insieme esatto `[1193, 1194, 1481, 1548, 1616]`, non solo il numero.

## Terminologia

| inglese | resa | nota |
|---|---|---|
| `carrier craft` | **portaerei** | |
| `fighter` / `fighter bay` | **velivolo da combattimento** / **baia di caccia** | |
| `screening vessels` | **navi usate come schermo** | |
| `turret mounts` / `dorsal turrets` | **supporti per torrette** / **torrette dorsali** | |
| `testbed` / `test platform` / `test bed` | **banco di prova** / **piattaforma di prova** | |
| `scout craft` | **vascello da ricognizione** | |
| `freighter` / `cargo holds` | **cargo** / **stive** | |
| `outfits` | **equipaggiamenti** | |
| `plasma technology` | **tecnologia al plasma** | |
| `scanner instruments` | **strumenti di scansione** | |

## Limiti dichiarati

Nessuna approvazione (12 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Il file è **finito in
staging**, non approvato.
