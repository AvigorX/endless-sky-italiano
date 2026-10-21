# review.md — L308 (`data/avgi/avgi weapons.txt`, righe 264–703)

Registro delle decisioni editoriali del **secondo lotto** delle armi Avgi: un laser blu, due lanciatori esterni e tre sistemi di
lancio verticale.

## 1. Che cosa raccontano queste schede

| famiglia | righe | idea centrale |
|---|---|---|
| **laser ottico** | 264/265 | `Blue Optical Laser`: «perfora la corazzatura» a forza di **shock termici**, ma **soffre la diffrazione** — danni decrescenti e **fascio invisibile**; l'ottica compensa con una **portata eccezionale** |
| **lanciatori esterni** | 515/531, 551/570 | `External Launch Rail`: **un solo siluro** su un pilone; `External Launch Tube`: **lanciatore grande** con **catapulta a coilgun** per i missili `torch` |
| **VLS** | 574/592/613–615, 618/636/657–659, 662/680/701–703 | tre **array** da **9, 18, 36 celle**: lanciatori **e** caricatori insieme, senza deposito separato |

## 2. Il laser blu è **fisica**, non fantascienza

La 264 è la scheda più **tecnica** del file:

> «Pulsando migliaia di volte al secondo, il fascio crea **shock termici e meccanici** nel materiale bersagliato… A differenza
> delle armi a fascio avanzate usate da altre specie, questo laser subisce gli effetti della **diffrazione**: i danni calano con
> la distanza e il fascio diventa **invisibile**.»

La resa conserva **tre informazioni** che l'inglese dà in forma compatta: il **meccanismo** (impulsi), il **limite** (diffrazione)
e il **paradosso** (l'ottica permette di mirare **più lontano** proprio perché il fascio è debole e invisibile al bordo).

## 3. `TEXT` e `VALUE`: nessuna traduzione, ma verifica doppia

| tipo | esempio | trattamento |
|---|---|---|
| `TEXT` | `"Ophrys" Nuclear Torpedo` | **copiato**, 2 virgolette |
| `VALUE` | `Vertical Launch Array (18)` | **copiato** |

Non è pigrizia: sono **designazioni** che il gioco mostra come **nome di munizione** o di **array**. Il test verifica **sia** la
copia **sia** il numero di virgolette per unità.

## 4. Due famiglie, un solo criterio

| famiglia | occorrenze | criterio |
|---|---|---|
| **nota munizioni** | 5 (69, 108, 615, 659, 703) | **identica** — è una **regola** che il giocatore legge in ogni pannello |
| **paragrafo VLS** | 3 (614, 658, 702) | **identico** — descrive lo **stesso meccanismo** con parole uguali |

In entrambi i casi la **ripetizione è del sorgente** e la resa la conserva: «variare per eleganza» avrebbe rotto la coerenza del
gioco.

## 5. Scelte di resa

| inglese | resa |
|---|---|
| `ideal for damaging other ships` | **ideale per danneggiare altre navi** |
| `Pulsing thousands of times each second` | **Pulsando migliaia di volte al secondo** |
| `thermal and mechanical shocks in the target material` | **shock termici e meccanici nel materiale bersagliato** |
| `enhancing its ability to drill through armor` | **migliorando la capacità di perforare la corazzatura** |
| `subject to the effects of diffraction` | **subisce gli effetti della diffrazione** |
| `the tenuous damage at the edge of the laser's reach` | **i danni tenui al limite della sua portata** |
| `a small electromagnetic catapult` | **una piccola catapulta elettromagnetica** |
| `large torch-driven missiles and torpedoes` | **missili e siluri di grandi dimensioni a propulsione torch** |
| `a coilgun-based ejection system` | **un sistema di espulsione basato su coilgun** |
| `each occupying one ton of outfit space` | **ognuna delle quali occupa una tonnellata di spazio per gli equipaggiamenti** |
| `this array's compact footprint` | **l'ingombro compatto dell'array** |
| `though the system still requires a turret mount` | **anche se il sistema richiede comunque un alloggiamento per torrette** |
| `as dual launchers and magazines` | **essendo insieme lanciatori e caricatori** |
| `disposed in a rectangular array` | **disposte in un array rettangolare** |
| `swift vertical cold-launch` | **un lancio a freddo verticale rapido** |
| `an open space comparable to a turret mount` | **uno spazio libero paragonabile a un alloggiamento per torrette** |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab | **7** (265, 614, 615, 658, 659, 702, 703) | **7** |
| virgolette | **10** (5 coppie) | **10** |
| segnaposto / alternative | **0 / 0** | **0 / 0** |
| apici | **3** | **9** |
| copiati (`TEXT` + `VALUE`) | **8** | **8**, verbatim |

## 7. Cosa resta aperto (dichiarato)

- **Nessuna approvazione**: 21 unità `PENDING`; **nessuna revisione umana**.
- **Prossimo lotto — TERMINALE**: righe **716–969** — **13 unità** (**10 `DESCRIPTION` + 2 `TEXT` + 1 `VALUE`**), **446 parole**,
  **6 contesti**, **6 tab** (717, 802, 803, 950, 951, 969), **4 virgolette**, **3 apici**. Chiude il file a **46/46**:
  **ventinovesimo file completo**. Contiene le schede delle **tre munizioni** con i **loro nomi fra virgolette nei contesti**
  (`outfit:"Nettle" KKV`, `outfit:"Orchid" Nuclear Missile`, `outfit:"Ophrys" Nuclear Torpedo`) e una `TEXT` con contesto
  `(root)`.
