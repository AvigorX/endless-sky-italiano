# STATO — L115 · `data/_ui/tooltips.txt` (**72 contesti per 104 unità**)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L115_20261019_061333` |
| Righe / unità | **1312–1566** / **104** |
| Tipo | **104 `TUTORIAL_TIP`**, nient'altro |
| Stati | **104 `PENDING`** — misurato con `select state` e **asserito** in `mkparts.py` |
| Contesti | **72** — 56 singole, **7 coppie**, **5 terne**, **2 quaterne**, **1 da cinque**, **1 da sei** |
| Parole | **1819 EN → 1839 IT** (1,011); per unità 0,88–1,74, media 1,14 |
| Tab · quadre | **0** · **0** |
| Token | **8 `<shift>`** in 8 unità (una sola famiglia) |
| Ripetizioni | **1 coppia** identica: 89/92 (`- "fast": just uses the ship's sprite.`) |
| Virgolette | **82** in 38 unità (37 con 2; l'unità **35** con 8) |
| sha256 | `1c8c5a0ff94ca5b2…` |
| `check.py` | **38 controlli**, `FAIL totale: 0` |
| `verify.py` | **47 controlli**, exit **0** |

## La forma dei contesti, misurata e non copiata

| finestra | unità | contesti | forma |
|---|---|---|---|
| L111–L112 | 104 / 120 | 104 / 120 | uno per unità |
| L113 | 96 | 87 | nove contesti con due unità |
| L114 | 110 | 110 | uno per unità |
| **L115** | **104** | **72** | **56 singole, 7 coppie, 5 terne, 2 quaterne, 1 da cinque, 1 da sei** |

Il controllo di L114 («110 contesti, max 1») su questa finestra **fallisce con la traduzione giusta**: qui vale
il `Counter` esatto, con l'elenco dei sedici contesti ripetuti (`Show status overlays` ×6, `Text alignment` ×5,
`Camera acceleration` ×4, `Parallax background` ×4, cinque gruppi da tre, sette coppie).

## Le 82 virgolette sono chiavi e valori di impostazione

Non sono prosa: sono i nomi che il gioco usa per le preferenze (`Preferences::Has("Escorts expend ammo")`,
`Preferences::Set("Text alignment", …)`) e i valori che il menu mostra (`"left"`, `"fancy"`, `"off"`,
`"always on"`). **Restano identici all'inglese**, e i due script lo verificano **per unità** confrontando i
testi fra virgolette con quelli del sorgente: 82 = 82, 38 unità, una con otto (l'unità 35, che cita due volte
`"Turret tracking"` più `"focused"` e `"opportunistic"`).

**Unica eccezione dichiarata**: l'unità 10 cita l'etichetta `"surge"`, che L113 ha già reso **«picco»** nello
stesso pannello di potenza — citarla in inglese creerebbe due nomi per la stessa voce.

## I tre registri

- **Avvisi del cantiere** (1–11): batterie, spinta e virata limitate, energia solare, carburante, iperguida,
  baie, energia insufficiente allo sparo, equipaggiamento atroce.
- **Etichette di comando** (12–58): 12 comandi di volo, 8 di selezione e interazione, 6 di pannello, 6 di
  flotta, ciascuno con la sua descrizione e le varianti `<shift>`.
- **Descrizioni di opzione** (59–104): zoom, allineamento del testo (5 varianti), carattere, modalità schermo,
  vsync, accelerazione della camera (4 varianti), carico CPU/GPU, sfocatura, grafica ridotta, caricamento
  differito, foschia, campo stellare, parallasse (4 varianti), effetti di salto, contorni delle navi (3 gruppi da
  tre), filtro delle texture (3), sovrapposizioni di stato (6).

## Invariante di segmento

| Voce | Valore |
|---|---|
| Unità prima della riga 1312 | **430** (L111–L114) |
| Unità dopo la riga 1566 | **133** |
| Confine | riga **1569** apre `tip:   Show flagship overlay` |
| File | **667 unità**, `max(line) = 1865` |
| Copertura | **534/667 (80,1%)** |

## Verifica

```bash
cd staging/editorial/L115_20261019_061333
python mkparts.py   # 104 unità · 72 contesti · 82 virgolette · 8 token · 1 coppia
python check.py     # FAIL totale: 0 (38 controlli)
python verify.py    # exit 0 (47 controlli)
```
