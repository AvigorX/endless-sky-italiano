# STATO — L314 (`data/drak/drak culture conversations.txt`, righe 26–79)

**Stato: CHIUSO.** Primo lotto del file: **16 unità su 32** (**50,0%**). `check.py` esce 0 con **22 controlli**; `verify.py` esce 0
con **20 controlli**. `state.py` esce 0 (`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

| voce | valore |
|---|---|
| directory | `staging/editorial/L314_20261020_214658/` |
| file | `data/drak/drak culture conversations.txt` (32 unità · 1.153 parole · 32 `MISSION_TEXT`) |
| righe | 26–79 |
| unità | **16** — tutte `MISSION_TEXT` |
| contesti | **3** — **tre visioni**: `Arachi` (5), `Hai` (5), `Humanity` (6) |
| parole | **550 EN → 556 IT** (1,011) |
| rapporto | **0,77 – 1,29** |
| tab | **13** — tutte tranne le prime dei tre blocchi (26, 43, 74) |
| virgolette | **2** — una coppia, riga **44** (`"islands"` → `"isole"`) |
| segnaposto | **4** — `<ship>` ×3, `<origin>` ×1, **identici** |
| alternative | **0** |
| apici | **6 EN / 14 IT** |
| `check.py` | **22 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **20 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: **0 prima** (il lotto apre il file) · 16 qui · **16 dopo** (la prossima alla 93) |
| copertura | **16/32 (50,0%)** — **stampata, non asserita** |
| `sha256[:16]` | **`162eb068dd20a5d2`** |

## Comandi

```bash
python staging/editorial/L314_20261020_214658/check.py     # FAIL totale: 0 (22 controlli)
python staging/editorial/L314_20261020_214658/verify.py    # FAIL: 0 (20 controlli, 16/32)
```

## Tre visioni, tre blocchi

| contesto | righe | unità | prima unità | che cosa si vede |
|---|---|---|---|---|
| `Drak Revelations: Arachi` | 26–30 | 5 | **26, senza tab** | un pianeta di **nuvole**, i **tunnel** sotto la superficie, la **marcia** che rimbomba sopra, le creature corazzate che si lanciano contro un gigante color oro pallido |
| `Drak Revelations: Hai` | 43–47 | 5 | **43, senza tab** | un **arcipelago** in una **pozzanghera**: vascelli fra le «isole», il calore che bolle i mari, le onde che tentano di **spegnere il sole** |
| `Drak Revelations: Humanity` | 74–79 | 6 | **74, senza tab** | una **culla** sospesa nel buio: un **masso**, le **fiamme rosso sangue**, la **battaglia** di entità senza forma, il **risveglio nel letto** |

## La struttura che il test difende

```
26  (senza tab)  ┐                      43  (senza tab)  ┐                     74  (senza tab)  ┐
27–30  (tab)     ┘ Arachi               44–47  (tab)     ┘ Hai                 75–79  (tab)     ┘ Humanity
```

- **13 tab**, righe esatte `[27, 28, 29, 30, 44, 45, 46, 47, 75, 76, 77, 78, 79]`;
- **le prime tre unità non hanno tab**, e il test verifica anche che **l'inglese** non l'abbia (nessuna tab aggiunta a mano);
- **una sola coppia di virgolette**, nella riga **44**: le «isole» sono la metafora della pozzanghera, e la virgoletta **è del
  sorgente**;
- **4 segnaposto**, verificati **per tipo** (`<ship>` ×3, `<origin>` ×1).

## Cosa il test pretende

| oggetto | verifica |
|---|---|
| blocchi | 5 + 5 + 6 unità; prima senza tab, le altre con |
| segnaposto | identici, con il **conteggio per tipo** |
| virgolette | **2**, nella sola riga 44 |
| apici | **6** in inglese, uno per unità (26, 27, 30, 43, 75, 77) |
| seconda persona | **≥3 unità per blocco**, ≥12 in tutto: è la voce della visione |
| svelamenti | «sottoterra» (26), «normale» (47), «letto» (79) |
| immagini | culla / masso / fiamme / entità senza forma; arcipelago / onde che inghiottono; nuvole / tunnel / marcia |
| segmento | 0 prima · 16 qui · **16 dopo** (minima 93) |

## Limiti dichiarati

Nessuna approvazione (16 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. **Il file non è finito**: restano
**16 unità / 603 parole** (righe 93–138), che lo chiudono in **L315**.
