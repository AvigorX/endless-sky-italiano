# REPORT — L122 · `campaign events.txt` (memoriali, Bloodsea, Geminus, Martini) · **file chiuso**

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| memoriale di Deep | 1–2, 6–7, 33–34 | 1338–3423 | il porto, le pareti di granito, i tre stadi dell'ampliamento |
| New Iceland | 3–5, 26–28 | 1783–2902 | mondo vulcanico, maschere antipolvere, base abbandonata |
| Clink | 8–9 | 1857–1861 | colonia penale dei Mondi Liberi, miniera di terre rare |
| Poisonwood | 10–13 | 1893–1907 | porto di rottami, «The Parting Glass», ritorno della Repubblica |
| Bloodsea | 14–21 | 1941–1982 | mondo rosso, porto nuovo, gergo pirata, indipendenza |
| Albatross | 22–23 | 1989–1990 | anarchici, pirati, liberazione scettica |
| Covert | 24–25 | 2804–2821 | cartello minerario, uranio, flotta pirata |
| Geminus | 35–38 | 3439–3442 | Arsenale nuovo, spazioporto efficiente, area ristorazione |
| Martini | 39–42 | 3465–3468 | capitale nuova, vecchio spazioporto in rovina |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Free Worlds War Memorial` | **il Memoriale di Guerra dei Mondi Liberi** | |
| `granite walls engraved with the names of the fallen` | **pareti di granito incise con i nomi dei caduti** | |
| `perpetually hazy volcanic world` | **mondo vulcanico perennemente fosco** | |
| `dust masks` · `particulate matter` | **maschere antipolvere** · **particolato** | |
| `prison colony` | **colonia penale** | |
| `The Parting Glass` | **The Parting Glass** | nome di taverna, invariato |
| `hodgepodge of small metal structures` | **guazzabuglio di piccole strutture metalliche** | |
| `rhodophyte algae` | **alghe rodofite** | |
| `saw the writing on the wall` | **hanno capito come stavano le cose** | idioma reso, non calcato |
| `meat patty` | **polpetta** | |
| `protection rackets` | **organizzazioni che vendevano protezione** | |
| `weapons-grade uranium and plutonium` | **uranio e plutonio a livello militare** | |
| `Checkmate plan` | **piano "Checkmate"** | nome di operazione, invariato |
| `will-do attitude` | **atteggiamento di 'si può fare'** | apici singoli, come il sorgente |
| `deflector shields` | **scudi deflettori** | |
| `food court` | **area ristorazione** | |
| `electric carts carrying cargo` | **carrelli elettrici che trasportano merci** | |

## 3. Difficoltà

1. **Zero token**: il controllo è un'asserzione (`== {}`), non un'assenza. È il primo lotto di questo file senza
   token, e la classe di errore («token comparso dove non deve») va chiusa esplicitamente.
2. **La memoria di traduzione**: cinque unità con testo identico a L120/L121, con confronto sulla resa esatta.
   Se un lotto futuro cambia uno di quei testi, il confronto diventa rosso.
3. **Tre testi ripetuti tre volte** (porto di Deep, apertura di Bloodsea) e due due volte: **36 testi per 42
   unità**, una sola resa per testo.
4. **Cinque virgolette in tre unità**: 19 (due battute), 21 (`"indipendente"`), 32 (`"Checkmate"`); il `check.py`
   verifica **quali** unità le contengono.
5. **`The Parting Glass` resta in inglese**: la scansione dei residui inglesi ha fatto fallire il primo
   `check.py` perché il nome contiene « the »; neutralizzato prima della scansione, non allentando il controllo.
6. **`Bordo Meridionale`** (già da L121) ricompare qui nell'unità 28: coerenza mantenuta.
7. **Invariante di file**: il `verify.py` legge i tre lotti e dimostra **150/150** righe coperte,
   `sovrapposti = 0`, `max(line) = 3468`.

## 4. Numeri osservati

```
unita' 42/42 · DESCRIPTION 41 · MISSION_TEXT 1 · tutte PENDING
contesti 18 (8x2, 4x1, 4x4, 2x3) · testi distinti 36 (3 da L120/L121)
tab 21 unita · virgolette 8 (unita 19, 21, 32) · token 0 · quadre 0 · backtick 0
parole EN 2220 -> IT 2191 (0.987) · rapporto 0.86 - 1.16, media 1.04
righe 1338/3468 · file 150/150 (100,0%) · 3 lotti · 6961 EN -> 6788 IT
FAIL totale: 0 (32 controlli) · verify exit 0 (30 controlli)
sha256[:16] 3ff793b7a7ed6422
```

## 5. Stato del progetto

```
TOTALE staging: 26723 unita · 845879 EN · 803434 IT
campaign events.txt: 150/150 (100.0%) · 3 lotti · FILE COMPLETO
file completi: quarantaquattro · residuo traducibile (formula state.py): 5207
residuo misurato: 5839 unità / 131105 parole su 122 file
avanzamento: 26723/32924 unità (81,2%) · 845879/979975 parole (86,3%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (32 controlli), `verify.py` exit **0** (30 controlli, invariante di file) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: le 42 unità restano `PENDING`; nessun evento è stato caricato nel gioco.
- **Nessuna revisione umana**.
- **Il file è chiuso in staging, non nel gioco**: 150 unità tradotte, zero viste.
- **Prossimo file**: `data/human/ships.txt` (103 unità, 5.083 parole, 72 contesti) — primo lotto **L123**, righe
  78–2044, 54 unità, 2.364 parole (`HANDOFF_L123_20261019.md`).
