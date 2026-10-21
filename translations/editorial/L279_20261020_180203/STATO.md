# STATO — L279 (`data/human/kestrel.txt`, righe 56–164)

**Stato: CHIUSO.** Secondo lotto del file: **33 `MISSION_TEXT`** del colloquio tecnico e della **sceneggiata del nome**. Il file è
aperto a **49/51 (96,1%)**.

| voce | valore |
|---|---|
| directory | `staging/editorial/L279_20261020_180203/` |
| file | `data/human/kestrel.txt` (51 unità · 1.064 parole · righe 15–402) |
| righe | 56–164 |
| unità | **33** — tutte `MISSION_TEXT` |
| parole | **501 EN → 439 IT** (0,88) |
| rapporto | **0,71 – 1,14** |
| contesti | **1** — `mission:Kestrel Testing` |
| tab | **32** (tutte tranne la 4: la narrazione dell'incontro) |
| virgolette | **94**, con lo **stesso numero per unità** |
| segnaposto | **3** — `<waypoints>` 1 · `<first>` 1 · `<last>` 1 |
| apici | **16 EN** su 11 unità / **10 IT** su 8 unità |
| `check.py` | **26 controlli, `FAIL totale: 0`**, exit 0 |
| `verify.py` | **22 controlli, `FAIL: 0`**, exit 0 |
| invariante | **di segmento**: 16 prima · 33 qui · **2 dopo** la 164 |
| `sha256[:16]` | **`291865dbb02348f9`** |

## Comandi

```bash
python staging/editorial/L279_20261020_180203/check.py     # FAIL totale: 0 (26 controlli)
python staging/editorial/L279_20261020_180203/verify.py    # FAIL: 0 (22 controlli, 49/51)
```

## La scena in tre atti

1. **le istruzioni** (unità 1-3): dove si collauda (`<waypoints>`), cosa fare — **disabilitare senza distruggere** — e cosa si
   perde se si distrugge o si ruba la nave;
2. **il ritorno** (4-16): Atinoda chiede com'è andata, poi **quattro domande sul progetto** (armi, motori, scudi e scafo, baie
   di caccia) e quattro risposte che promettono ritocchi;
3. **il nome** (17-33): il giocatore propone `Wraith`, `Grey Goose`, `Dire Wolf`, `Reaper` e — **quattro volte** — `Kestrel`,
   che alla fine fa **sussultare** Atinoda: «è quello!».

## Il cuore comico

Atinoda rifiuta i nomi uno per uno con una motivazione **diversa** ogni volta (animali, poi uccelli, poi «troppo»), mentre il
giocatore ripete ostinatamente la stessa proposta. La resa mantiene la **ripetizione identica** — `"La Kestrel."` quattro
volte — perché è la struttura della gag: il `check.py` conta le quattro occorrenze, non solo la presenza del nome.

## Limiti dichiarati

Nessuna approvazione (33 unità `PENDING`), nessun testo visto nel gioco, nessuna revisione umana. Restano **2 unità** (L280,
terminale).
