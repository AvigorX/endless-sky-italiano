# STATO — L334 (`data/human/news.txt`, righe 40–2902) — **TERMINALE, FILE INTERO** (modalità batch)

Gate generico: `check` e `verify` **exit 0**. `state.py` `ESITO: OK`. `state.db` non toccato.

| voce | valore |
|---|---|
| directory | `staging/editorial/L334_20261021_121711/` |
| righe | 40–2902 (**tutto il file**) |
| unità | **202** = **184 `NEWS` + 18 `TEXT`** |
| di cui | **164 copiate** (unità che sono **solo il delimitatore `"`**) + **38 tradotte** |
| contesti | **91** |
| parole | **716 EN → 727 IT** |
| virgolette | **228** (invariate per unità) |
| `id_ok.json` | **167** unità identiche dichiarate (164 delimitatori + `'"`, `!"`, `."`) |
| `sha256[:16]` | **`d553d288aa8897ce`** |

## Che cosa contiene

Il file è il **notiziario** del gioco: 91 blocchi, ognuno con una notizia fra virgolette. Le **164 unità** che sono solo `"` sono i
**delimitatori** delle stringhe spezzate dal formato `news` di Endless Sky: vanno **copiati** (non tradotti) e sono dichiarati in
`id_ok.json`, così il gate non li confonde con una mancata traduzione.

Le 38 unità di prosa:

- **la rete di comunicazioni** (820–828): boe ripetitrici, `TCP/IP`, `IPv4`, `DRQ`/`HSBE`, «un corridoio attraverso lo spazio»;
- **la gag dell'allarme rosso** (1804): «qualcuno ha urlato "È criptato!" … un pivello in cambusa avesse voglia di uova strapazzate»
  (il doppio senso di *scrambled* è conservato);
- **le etichette storte** (2204–2206, 2219, 2222): «Adatto al trasporto» sopra «Attenzione: esplosivo», «questo lato in alto» capovolta;
- **gli slogan** (2465–2476): «PACE FRA LE STELLE.», «MORTE FRA LE STELLE.», «TIRANNIA FRA LE STELLE.», «POVERTÀ FRA LE STELLE.»,
  «Pace, Prosperità, Progresso.», «Potere, Povertà, Orgoglio.»;
- **il limerick** (2556): «Un capitano dal passato torbido / ha attraversato questo sistema rapido / …»;
- **la propaganda CCOR** (2620–2630): «BELENOS RISPLENDE IN TUTTA LA GALASSIA», «LA CCOR RISORGERÀ», «LIBERATE IL BORDO ESTERNO»;
- **la réclame Betelgeuse** (2863, 2902), spezzata in due unità: «"Come fai a sapere che la tua nave Betelgeuse» + «compra oggi una vera
  nave Betelgeuse!"».

## Nota di strumento

`batch_lot.py` è stato esteso **minimamente** per leggere `id_ok.json`: senza, il gate segnalava come errore le 164 copie legittime. Il
controllo resta falsificabile — un'unità identica **non** dichiarata in `id_ok.json` fa ancora fallire il lotto.
