# STATO — L152 · `coalition jobs.txt` (la vendita del motore di salto agli Heliarch e le schede delle specie)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L152_20261019_190200` |
| Righe / unità | **1191–1359** / **21** — file al **69,0%** (136/197) |
| Tipi | **7 `VALUE`** (identici) · **7 `DESCRIPTION`** · **3 `MISSION_TEXT`** · **3 `LOGBOOK`** · **1 `TEXT`** |
| `UI_LABEL` | **0** — una sola asserzione vuota |
| Token | **34** su **6** simboli |
| Contesti | **8** · **13 testi distinti** |
| Parole | **527 EN → 531 IT** (1,008); **1,00–1,19** |
| Tab · virgolette | **2 unità** (17, 18) · **1 unità** (17, la battuta dell'Arach) |
| sha256 | `580b5869e9f95bed…` |
| Esiti | `check.py` **25** (`FAIL 0`) · `verify.py` **24**, exit **0** |

## Il file cambia carattere

Fino a L151 erano avvisi di lavoro. Qui arrivano **`MISSION_TEXT`** (la scena della consegna) e **`LOGBOOK`** (il diario e
le schede di Saryd, Kimek e Arachi). Il `Counter(kind)` lo dice, e i sei testi narrativi sono verificati **come
tradotti**, non solo presenti.

## L'Arach che parla al contrario

L'Arach della Coalizione inverte l'ordine delle frasi («Honor us you do… still incapable of creating our own, we are»).
La resa conserva l'inversione:

> «Sebbene grandi progressi nello studio dei motori di salto e dei loro meccanismi abbiamo fatto, ancora incapaci di
> crearne uno nostro siamo, e mezzi per procurarcene nuove copie non abbiamo. **Enormemente prezioso è** ogni singolo
> motore che potresti portarci.»

Due controlli distinti: le **virgolette** (una sola unità, la 17) e le due inversioni chiave.

## Due unità con tab, contate dal sorgente

Le unità 17 e 18 cominciano con `\t`. Nel `mkparts.py` le chiavi della mappa sono **senza tab** e il tab lo antepone il
costruttore, contato dal sorgente: un primo tentativo aveva le chiavi **con** il tab e falliva sul confronto
`lstrip('\t')`. Corretto, e il `verify.py` verifica che le unità col tab siano le stesse due anche in italiano.

## Verifica

```bash
cd staging/editorial/L152_20261019_190200
python mkparts.py   # 21 unità · 3 MISSION_TEXT + 3 LOGBOOK · 34 token · 2 tab · 1 unità con virgolette
python check.py     # FAIL totale: 0 (25 controlli)
python verify.py    # exit 0 (24 controlli, invariante di segmento)
```

**Non verificato**: la scena della vendita non è stata giocata; i `LOGBOOK` non sono stati visti nel diario.
