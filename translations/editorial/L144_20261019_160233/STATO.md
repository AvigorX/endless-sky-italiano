# STATO — L144 · `unfettered 0 prologue.txt` (il commercio dei motori, primo tratto: la prova della lama)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L144_20261019_160233` |
| Righe / unità | **367–420** / **20** — file al **78,2%** (115/147) |
| Tipi | **20 `MISSION_TEXT`** |
| `VALUE` · `LOGBOOK` · `UI_LABEL` | **0** · **0** · **0** — **tre asserzioni vuote scritte** |
| Token | **2** — `<hood>` (unità 1) e `<learned>` (unità 20), **1 = 1 per simbolo e per unità** |
| Stati | **20 `PENDING`** — misurato e **asserito** |
| Contesto | **1** — `Jump Drive Trading` 20/20 nella finestra, missione **aperta** |
| Testi | **20 distinti** — nessuna ripetizione |
| Parole | **486 EN → 406 IT** (0,835); per unità **0,73–1,28**, media **0,96** |
| Tab · virgolette | **19 unità** · **12** (unità 8, 10, 11, 12, 13, 20) |
| sha256 | `794b9584fd67c6a0…` |
| `check.py` | **31 controlli**, `FAIL totale: 0` |
| `verify.py` | **25 controlli**, exit **0** — invariante di **segmento** |

## Arrivano i token, e non sono decorazione

Sono i **primi due segnaposto** del file, e stanno in **unità diverse**:

| token | unità | forma inglese | forma italiana |
|---|---|---|---|
| `<hood>` | 1 | `an Unfettered Hai<hood> is waiting` | «un Hai Slegato**`<hood>`** ti aspetta» — **incollato** |
| `<learned>` | 20 | `…which you did. <learned>I am Desneeparu` | «…e tu l'hai fatto. **`<learned>`**Sono Desneeparu» — **a inizio frase** |

Il primo si incolla al nome (in inglese è un suffisso: «Hai*hood*», come *warriorhood*), il secondo apre una frase dopo
un punto e regge la maiuscola che segue («<learned>I am» → «<learned>Sono»). **Un totale pari non basta**: due
segnaposto in due unità diverse danno 1 = 1 anche se fossero stati scambiati di posto, quindi il controllo verifica
**simbolo per simbolo e unità per unità**, compresa la posizione.

## La prova della lama

Il fornitore è preceduto da una prova di combattimento: l'ingegnere **lancia una lama** al giocatore appena sbarca, e chi
non reagisce non entra. Il testo lo dice con ironia — «Riconosci la stessa Slegata dell'altra volta; deve adorare
lanciare lame alla gente» — e la scelta a tre vie (afferrarla, schivarla, fuggire) finisce in una **quarta** via nel
tratto successivo.

## `outfitter` = «fornitore»

Misurato in staging: **fornitore 45** occorrenze, **equipaggiatore 2**, **armiere 1**. La resa segue la maggioranza già
approvata, non il gusto del momento.

## Verifica

```bash
cd staging/editorial/L144_20261019_160233
python mkparts.py   # 20 unità · 1 contesto · 20 distinti · (No.) identico · (Sì.) ×1 · 2 token · 19 tab · 12 virgolette
python check.py     # FAIL totale: 0 (31 controlli)
python verify.py    # exit 0 (25 controlli, invariante di segmento)
```

**Non verificato**: nessuna lama è stata schivata nel gioco — la scena non è stata giocata.
