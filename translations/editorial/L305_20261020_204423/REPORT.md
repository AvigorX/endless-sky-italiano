# REPORT — L305 (`data/quarg/quarg outfits.txt`, righe 138–243)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **23 controlli**; `verify.py` esce 0 con **24 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 10 (tutte `DESCRIPTION`) | 10 |
| parole | 510 | **529** (1,04) |
| tab | **3** | **3** |
| virgolette / segnaposto / alternative | 0 / 0 / 0 | **0 / 0 / 0** |
| apici | 2 | 6 |
| contesti | **8** (6 singole + 2 coppie + 1 seconda metà) | invariati |

Rapporto per unità **0,99 – 1,24**.

## 2. La continuità `Large Graviton Steering`

| riga | lotto | ruolo |
|---|---|---|
| **137** | L304 | **prima** metà, **senza** tab |
| **138** | L305 | **seconda** metà, **con** tab, **ritornello** identico alle quattro di L304 |

Il `check.py` riapre il `translation.json` di L304 e confronta le **cinque** occorrenze del ritornello: 55, 78, 96, 120 (L304) e 138
(qui). Una sola resa per cinque moduli.

## 3. Il lotto è un corso di astrofisica

Le quattro schede dei reattori spiegano **meccanismi fisici veri** (o quasi): pressione negativa del vuoto quantistico, antimateria,
buco nero microscopico, **radiazione di Hawking**, **disco di accrescimento**, **orizzonte degli eventi**.

Il testo italiano usa i **termini tecnici standard**, non perifrasi: «radiazione di Hawking» (non «radiazione del buco nero»), «disco
di accrescimento», «orizzonte degli eventi». Chi conosce l'astrofisica riconosce i concetti; chi non la conosce legge un testo
plausibile.

## 4. Le montagne russe dell'incertezza

| inglese | resa | grado di certezza |
|---|---|---|
| `Human engineers … were astonished` | «rimasero sbalorditi» | **fatto** |
| `rumored to be stored` | «che **si dice** sia immagazzinata» | voce |
| `seemingly in defiance of` | «**apparentemente** in spregio a» | apparenza |
| `According to little more than vague allusions` | «Secondo **poco più che vaghe allusioni**» | quasi nulla |
| `Further wild guesses` | «Altre **congetture ardite**» | congettura |
| `some have speculated` | «alcuni **hanno ipotizzato**» | ipotesi |
| `completely unknown to humanity` | «del tutto **ignoto** all'umanità» | nulla |

È la **scala epistemica** del lotto, e la resa la conserva parola per parola.

## 5. Verifica

```
check.py   23 controlli · FAIL totale: 0 · exit 0
verify.py  24 controlli · FAIL: 0 · exit 0
segmento   11 prima · 10 qui · 10 dopo la 243 · file 21/31 (67,7%)
```

**Due rossi al primo giro**, entrambi **miei**:
1. la distribuzione dei contesti attesa era `[1]*7 + [2]`, ma con **6 singole + 2 coppie** è `[1]*6 + [2, 2]`;
2. chiedevo che `Aspis`, `Ancile`, `Aegis` e `Quantum Vacuum Battery` comparissero **nel testo**: sono **nomi di pannello**, e le
   schede non si nominano mai. Sostituito con «i nomi nel testo sono invariati e nessun nome greco è italianizzato».

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 10 unità `PENDING`; **nessuna revisione umana**.
- **Nessun testo visto nel gioco**.
- **Il file resta aperto**: 21/31; restano **10 unità** (il lotto **terminale**).
