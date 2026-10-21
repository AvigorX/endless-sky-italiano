# STATO — L227 · `remnant outfits.txt` (quinto e **ultimo** lotto) — **FILE CHIUSO 57/57**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L227_20261019_230743` |
| Righe / unità | **884–979** / **10** — file a **57/57 (100%)** |
| Tipi | **9 `DESCRIPTION`** · **1 `VALUE`** (riga 948, `Void Sprite Parts`) |
| Tab · virgolette · apici | **2** (unità 5, 8) · **0** · **3 EN / 7 IT** |
| Segnaposto | **0** |
| Contesti | **7** — `Void Sprite Parts` 3 (con il `VALUE`), `Void Rifle` 2, gli altri 1 |
| Parole | **382 EN → 376 IT** (0,84–1,10, media 0,99) |
| sha256 | `ba3673a78c7a0d5e…` |
| Esiti | `check.py` **24** (`FAIL totale: 0`) · `verify.py` **20** (`FAIL: 0`) |

## Perché è un lotto terminale

L'ultima unità del file è la **979** e `line > 979` vale **0**. Il `verify.py` usa l'**invariante di FILE**:

```
12 (L223) + 13 (L224) + 11 (L225) + 11 (L226) + 10 (L227) = 57
```

**Questo file non ha `UI_LABEL`**: tutte le 57 unità sono traducibili, e il conto è diretto. Il controllo verifica che le
cinque finestre coprano **esattamente** le righe del database — nessun buco, nessuna sovrapposizione.

| finestra | righe | unità |
|---|---|---|
| L223 | 48–297 | 12 |
| L224 | 298–565 | 13 |
| L225 | 581–674 | 11 |
| L226 | 675–864 | 11 |
| L227 | 884–979 | 10 |
| **totale** | **48–979** | **57** |

## Torna un'unità da copiare — e non è un'incoerenza

Dopo **tre lotti consecutivi** con zero unità da copiare (L224, L225, L226), qui il `VALUE` della riga **948** riporta il
confronto a **1 identica / 9 tradotte**. Il file ha **55 `DESCRIPTION` + 2 `VALUE`**: uno dei due nomi cade in L223 (riga
224) e l'altro nel lotto terminale. La forma del confronto dipende dalla **composizione della finestra**, non da una regola
generale sul file.

Il `check.py` asserisce **entrambe** le direzioni: che l'unica identica sia il `VALUE`, e che tutte e nove le `DESCRIPTION`
siano tradotte.

## Zero virgolette, come in L226

Asserzione su un numero zero, in inglese e in italiano. Due lotti consecutivi senza virgolette dopo lotti che ne avevano
decine: il numero si misura, non si presume.

## L'ultima unità non è un equipaggiamento

`Remnant Capital License` è una **licenza**, e la sua scheda descrive un dispositivo che, picchiettato su un bordo, produce
un ronzio capace di attraversare un pianeta per chiamare le pattuglie. Registro diverso dagli altri nove testi — meno
descrittivo e più narrativo — e la resa lo rispetta.

## Cosa contiene

La **Forge-Class Steering** (avida di energia: la tecnologia dei motori dei Remnant è più avanti di quella umana), la
**Smelter-Class Steering** (di cui non si sa se sia invenzione propria o ispirata agli alieni), il **Tuning Rifle** (onde
sonore che liquefanno i tessuti), il **Void Rifle** e i suoi colpi paralizzanti, le **Void Sprite Parts** (un metro cubo di
parti, «un evento terribile e un'occasione spaventosa»), la **Remnant License** (che suona musica classica) e la
**Remnant Capital License**.

## Difficoltà

1. **`have not been able to make any new ones since the Archon stopped their harvests`** → «non sono più riusciti a
   fabbricarne di nuove da quando l'Archon ha fermato le loro raccolte»: `Archon` è un'autorità e resta invariato.
2. **`degraded into uselessness centuries ago`** → «sono diventati inutilizzabili secoli fa».
3. **`These highly effective weapons are credited with…`** → «A queste armi molto efficaci si attribuisce il merito di…»:
   la costruzione passiva inglese richiede il «si attribuisce» per non appesantire.
4. **`void sprites`** → «void sprite» invariato; **`tentacles`** → «tentacoli».
5. **`a terrible occurrence and a dreadful opportunity`** → «un evento terribile e un'occasione spaventosa»: i due aggettivi
   inglesi sono diversi (`terrible` / `dreadful`) e la resa li distingue.
6. **`nothing more and nothing less than a cubic meter`** → «Non è altro che un metro cubo»: la formula enfatica si
   conserva senza il doppio «né più né meno», che in italiano suonerebbe più solenne del testo.
7. **`IFF verifier`** → «verificatore IFF»: acronimo invariato.
8. **`produces a surprisingly beautiful blend of classical music tracks`** → «produce una fusione di brani di musica
   classica sorprendentemente bella».
9. **`should they ever become stranded`** → «qualora restino bloccati»: stessa resa di L225 («restare bloccata»), qui al
   plurale.
10. **L'italiano è più corto**: 376 parole contro 382, media 0,99 — il secondo lotto della campagna in cui il totale scende.

## Verifica

```bash
cd staging/editorial/L227_20261019_230743
python check.py     # FAIL totale: 0 (24 controlli)
python verify.py    # FAIL: 0 (20 controlli) · FILE CHIUSO 57/57
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 10 unità `PENDING`.
