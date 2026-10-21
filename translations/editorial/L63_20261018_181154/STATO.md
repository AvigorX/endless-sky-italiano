# STATO — L63 · `data/human/culture conversations.txt`

**Lotto chiuso.** 37/37 unità tradotte, righe **624–711**.

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L63_20261018_181154` |
| File | `data/human/culture conversations.txt` (sesto lotto sul file) |
| Unità | **37** (righe 624–711) |
| Parti | **2** — 10 · 27 |
| Contesti | **2** — `Sol-Bound Shuttle` 1–10, `Earth Day Blackout` 11–37 |
| Tipi | **36 `MISSION_TEXT` + 1 `UI_LABEL`** |
| Parole | 1.087 EN → 1.025 IT (**0,943**) |
| Rapporto per unità | **0,75 – 1,85** (gate 0,55–1,90) |
| `UI_LABEL` (`NT`) | **1** — unità **30**, `way in` (identica al sorgente) |
| `DIALOG` / `LOGBOOK` / `CONVERSATION` / `TEXT` | **0 / 0 / 0 / 0** — assenze dichiarate |
| Token `<…>` | **0** — assenza dichiarata |
| Tab · virgolette | **35** · **51**, con **3 virgolette dispari** (unità **18, 29, 31**) **riprodotte** |
| Duplicati inglesi | **0 gruppi** — controllo negativo |
| sha256 `translation.json` | `3535834a2a119c44…` |
| `check.py` | **33 controlli**, `FAIL totale: 0` |
| `verify.py` | **36 controlli**, exit **0** |

## Dove siamo nel file

| Voce | Valore |
|---|---|
| Unità prima della 624 | **172** (L58–L62) |
| Unità dopo la 711 | **165** |
| Copertura | **209/374 (55,9%)** |

## Cosa è stato deciso qui

1. **Tre virgolette dispari, riprodotte.** Le unità 18, 29 e 31 sono discorsi diretti **aperti e non
   chiusi** nel sorgente. Non si chiudono: si riproducono, e `verify.py` confronta l'**insieme degli
   indici** `(18, 29, 31)` fra inglese e italiano.
2. **`Luna` e `Moon`.** La capitana usa «the Moon» e il testo commenta che è «the archaic term for Luna»:
   in italiano «la Luna» non è arcaico, quindi la resa mantiene **entrambe** le parole («Luna» e il
   commento sul termine arcaico) e il commento resta leggermente paradossale come nell'originale. È un
   limite della traduzione, dichiarato, non nascosto.
3. **Registro doppio.** `Sol-Bound Shuttle` è una conversazione tra colleghi, ironica e sicura di sé («Call
   me paranoid»); `Earth Day Blackout` è una scena di folla con due interlocutori che spiegano la
   tradizione. I due registri non si uniformano.
4. **Il lessico della tradizione**: `Earth Day` → **Giornata della Terra**; `total blackout` →
   **blackout totale** (il prestito inglese è quello che userebbero i personaggi); `fusion reactors` →
   «reattori a fusione»; `supertall buildings` → «grattacieli enormi».
5. **`offworlders`** → «noi che veniamo da fuori», non «stranieri»: nel sistema Sol chi arriva da altri
   sistemi è un fuori-mondo, non un alieno.
6. **Un rapporto fuori banda corretto, non tollerato.** L'unità 27 («Earth Day?») rendeva 2,08 con
   l'articolo; resa «Giornata della Terra?» il rapporto scende a **1,85**, dentro il gate. La frase resta
   un'eco sorpresa, che è quello che è nell'inglese.

## Verifica

```bash
cd staging/editorial/L63_20261018_181154
python check.py                 # FAIL totale: 0   (33 controlli)
python verify.py                # exit 0           (36 controlli)
```

## Prossimo passo

**L64** — stesso file, righe **712–810**, **42 unità**, 2 contesti (`Burthen Triathlon` 25,
`CCOR Guerrilla Standoff` 17), 1.652 parole, tab 36, virgolette 23 con **3 dispari** (unità 35, 36, 37),
**4 `UI_LABEL`** (unità 15, 18, 22, 24), 0 token.
