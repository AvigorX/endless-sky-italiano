# REPORT — L276 (`data/korath/korath ships.txt`, righe 1375–1961)

**Esito: lotto CHIUSO.** `check.py` esce 0 con **25 controlli**; `verify.py` esce 0 con **21 controlli**. `state.py` esce 0
(`ESITO: OK`, 8/8). Nessuna scrittura su `state.db`.

## 1. Misure

| voce | inglese | italiano |
|---|---|---|
| unità | 12 (tutte `DESCRIPTION`) | 12 |
| parole | 453 | **474** (1,05) |
| tab | 2 | 2 · primo carattere |
| virgolette | 2 | 2, dritte |
| apici | 2 | 7 |
| segnaposto | 0 | 0 |

Rapporto per unità **0,92 – 1,16**.

## 2. Il lotto

| nave | famiglia | che cosa dice |
|---|---|---|
| **Echo-Galleon** | Efreti | discendente delle navi-mondo: più leggero e veloce, **meno potente** |
| **Arch-Carrack** | Efreti | **mercantile**: non difende sé stesso, ma è rapido fra i pochi pianeti rimasti |
| **Charm-Shallop** | Efreti | **multiruolo**: passeggeri, estrazione; struttura leggera di ispirazione Quarg |
| **Kar Ik Vot 349** | Kor Sestor | incrociatore da battaglia: **uno vale una flotta** |
| **Tek Far 71 - Lek** | Kor Sestor | porta **dieci droni** agganciati allo scafo |
| **Tek Far 78 - Osk** | Kor Sestor | **portatrice** con agganci per **nove caccia** |
| **Tek Far 109** | Kor Sestor | portatrice pura: **senza i suoi caccia è indifesa** |
| **Met Par Tek 53** | Kor Sestor | la più piccola, ma **più grande di quasi tutte le navi capitali umane** |
| **Far Lek 14** | Kor Sestor | drone d'attacco: **scafo ultradenso** |
| **Far Osk 27** | Kor Sestor | caccia senza abitacolo: scafo più spesso, più scudi, più armi |

## 3. La formula di L275, ripresa

Unità 1: «**Le più grandi navi da produzione Korath derivano da un telaio comune e antico**, compreso questo grande vascello
degli Efreti.» Il `check.py` verifica che l'apertura sia **identica** a quella delle cinque navi da produzione di L275: è la
prova che il corpus resta coerente anche fra lotti diversi.

## 4. Robotici, non «automatici»

Le navi Kor Sestor sono **senza equipaggio**: la resa lo tiene fermo in tre punti — «navi da guerra **robotiche**», «caccia
**robotici**», «droni d'attacco **automatici**». Il `Far Osk 27` lo spiega esplicitamente: «pilotato da un computer e senza
bisogno di un abitacolo né di sistemi di supporto vitale», quindi può montare **più scafo, più scudi, più cannoni**.

## 5. Verifica

```
check.py   25 controlli · FAIL totale: 0 · exit 0
verify.py  21 controlli · FAIL: 0 · exit 0
segmento   31 prima · 12 qui · 7 dopo la 1961 · copertura 43/50 (86,0%)
```

Nessun rosso: primo giro verde, sia `check.py` sia `verify.py`. Le due note tecniche (droni e caccia) sono state riprese alla
lettera dal corpus, e il confronto con la variante più frequente è passato subito.

## 6. Cosa NON è verificato (dichiarato)

- **Nessuna approvazione**: 12 unità `PENDING`.
- **Nessun testo visto nel gioco**; **nessuna revisione umana**.
- **Il file resta aperto**: 43/50; restano le sette navi `Model`.
