# STATO — L222 · `successor ships.txt` (quinto e **ultimo** lotto) — **FILE CHIUSO 146/146**

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L222_20261019_223852` |
| Righe / unità | **1141–1338** / **26** — file a **146/146 (100%)** |
| Tipi | {'TEXT': 18, 'DESCRIPTION': 6, 'VALUE': 2} |
| Tab · virgolette · apici | **2** (unità 13, 26) · **36** (2 × 18) · **5 EN / 8 IT** |
| Segnaposto | **0** |
| Contesti | **3** — `Vujlet` 13, `Vujlet-Usaqri` 12, `Veusade` 1 |
| Parole | **431 EN → 472 IT** (1,00–1,21, media 1,03) |
| sha256 | `30ae0dcd3ae347d4…` |
| Esiti | `check.py` **29** (`FAIL totale: 0`) · `verify.py` **20** (`FAIL: 0`) |

## Perché è un lotto terminale

L'ultima unità del file è la **1338** e `line > 1338` vale **0**. Il `verify.py` usa l'**invariante di FILE**:

```
45 (L218) + 25 (L219) + 26 (L220) + 24 (L221) + 26 (L222) = 146
```

**Questo file non ha `UI_LABEL`**: a differenza di `deep jobs.txt`, dove la riga 683 restava fuori dalle finestre, qui tutte
le 146 unità sono traducibili e il conto è diretto. Il controllo verifica che le cinque finestre coprano **esattamente** le
righe del database — nessun buco, nessuna sovrapposizione.

| finestra | righe | unità |
|---|---|---|
| L218 | 17–381 | 45 |
| L219 | 386–629 | 25 |
| L220 | 634–873 | 26 |
| L221 | 904–1137 | 24 |
| L222 | 1141–1338 | 26 |
| **totale** | **17–1338** | **146** |

## Le due coerenze del lotto

1. **Unità 12 e 14 — la stessa scheda della Vujlet.** La 14 è la 12 senza l'apertura participiale (*Navigating the stars with
   the grace of a flitting bird*), e nel resto **differisce solo per due virgole**:

   | | inglese | italiano |
   |---|---|---|
   | 12 | *short-ranged **and** relatively vulnerable interceptors, and larger…* | «a corto raggio **e** relativamente vulnerabili, e le navi…» |
   | 14 | *short-ranged**,** relatively vulnerable interceptors, and larger…* | «a corto raggio**,** relativamente vulnerabili, e le navi…» |

   Il testo condiviso è identico; la differenza di punteggiatura è **conservata e verificata**.

2. **Unità 1 — la formula della Veusade torna da L221.** *Such a narrowly-focused design makes these ships ill-suited for
   multipurpose use, but they are frequently seen as auxiliary or police craft* era già stata resa nell'unità 24 di L221:
   la resa qui è la stessa («un progetto così specializzato rende queste navi inadatte all'uso polivalente, ma vengono
   spesso impiegate come unità ausiliarie o di polizia»), con *catch* → «raggiungere» dove L221 diceva *intercept* →
   «intercettare».

## Cosa contiene

La **Veusade** (la scheda completa: feritoie per le armi, capacità appena sufficiente a saturare i punti d'attacco con
cannoni a trascinamento), la **Vujlet** (nave da guerra leggera prodotta in serie dalle Alte Case, nata come ricognitore
furtivo della Casa Kaatrij) e la **Vujlet-Usaqri** (la variante con occultamento integrato e rete di scudi potenziata).

## Difficoltà

1. **`New Houses`** → **Nuove Case**: una terza famiglia di Case, distinta dalle Alte e dalle Case del Popolo. Il controllo
   verifica che `New Houses` non resti in inglese.
2. **`cloaking technology`** → «tecnologia di occultamento»; `stealth reconnaissance vessel` → «nave da ricognizione
   furtiva»; `stealth equipment` → «equipaggiamento occultante».
3. **`shield grid`** → «rete di scudi», coerente con la stessa resa usata in L219–L221.
4. **`eighteen hundred years`** → «milleottocento anni» (non «diciottomila»: è 1.800).
5. **`the power output of a large fusion reactor`** → «la potenza di un grande reattore a fusione».
6. **`Only once … was it made truly practical`** → «Solo quando … questo divenne davvero praticabile».
7. **`a useful bridge between … and …`** → «un ponte utile tra … e …»: la metafora dello scafo-ponti si conserva.
8. **`resource-intensive`** → «esigenti in risorse».

## Verifica

```bash
cd staging/editorial/L222_20261019_223852
python check.py     # FAIL totale: 0 (29 controlli)
python verify.py    # FAIL: 0 (20 controlli) · FILE CHIUSO 146/146
```

**Non verificato**: nessuna nave vista nel gioco; 26 unità `PENDING`.
