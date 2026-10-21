# STATO — L220 · `successor ships.txt` (terzo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L220_20261019_222539` |
| Righe / unità | **634–873** / **26** — file a **96/146 (65,8%)** |
| Tipi | {'TEXT': 16, 'DESCRIPTION': 6, 'VALUE': 4} |
| Tab · virgolette · apici | **1** (unità 24) · **34** · **2 EN / 12 IT** |
| Segnaposto | **0** |
| Contesti | **4** — `Nnesaarau` 9, `Ojde` 9, `Nnaatej` 7, `Seiitej` 1 |
| Parole | **440 EN → 487 IT** (1,00–1,16, media 1,02) |
| sha256 | `3373e098d9af319f…` |
| Esiti | `check.py` **28** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## La coppia 23/25: stesso testo, due virgolette

Le due `DESCRIPTION` dell'**Ojde** sono identiche **carattere per carattere** tranne un dettaglio: la **23** cita il nome
**fra virgolette** (`l'"Ojde"`), la **25** no (`l'Ojde`). Inglese: 374 contro 372 caratteri. La traduzione conserva
esattamente quella differenza:

```
t[23].replace('"','') == t[25]     → True, in inglese e in italiano
len(t[23]) - len(t[25])            → 2
```

Verificato sia nel `check.py` sia nel `verify.py`. Se una delle due schede venisse riformulata «per migliorarla», la stessa
nave racconterebbe due versioni diverse.

## Le 34 virgolette non sono 2 × 17

Sono **32** (2 per ognuna delle 16 `TEXT`) più **2 dentro una `DESCRIPTION`** (unità 23). Il contratto L220 lo aveva
annunciato come «da misurare»; il workspace ha confermato la riga e la distribuzione, e il controllo confronta le mappe
**per unità**, non il totale.

## L'errore mio: i nomi trascritti a mano invece che copiati

Alla prima stesura del `parts/part01.json` ho scritto **a memoria** i nomi delle `TEXT`, e **11 unità su 20** risultavano
diverse dal sorgente (`6-"Ruuv" Betavoltaic Cell` scritto come `"Ojet" Bimodal Coilgun`, `3-"Kaska"` al posto di
`1-"Uurau"`, e così via). Il confronto automatico le ha segnalate **tutte**; nessuna è passata inosservata.

Correzione strutturale, non testuale: il file ora si **genera dal sorgente** — per ogni unità `TEXT`/`VALUE` il valore è
copiato da `source.json`, e solo le 6 `DESCRIPTION` vengono dalle mie traduzioni. Da qui in avanti i nomi non si
trascrivono: si copiano con il codice. Il `check.py` verifica le 20 unità **carattere per carattere**.

## Cosa contiene

La **Nnaatej** (vascello anfibio per il passaggio oceano profondo → spazio profondo), la **Nnesaarau** (trasporto di lusso
recente e poco popolare, usato come nave da corsa), l'**Ojde** (il cargo più grande dei Successori, con due schede) e
l'apertura della scheda **Seiitej**.

## Verifica

```bash
cd staging/editorial/L220_20261019_222539
python check.py     # FAIL totale: 0 (28 controlli)
python verify.py    # FAIL: 0 (18 controlli) · 70 + 26 + 50 = 146 · confine 904 TEXT
```

**Non verificato**: nessuna nave vista nel gioco; 26 unità `PENDING`.
