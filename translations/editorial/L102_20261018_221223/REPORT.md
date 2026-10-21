# REPORT — L102 · `quarg missions.txt` (primo lotto, primo `LOGBOOK`)

## 1. Contenuto

| contesto | righe | unità | cosa succede |
|---|---|---|---|
| `First Contact: Quarg` | 19–69 | 27 | schede di Quarg e Drak; lo spazioporto; l'incontro; il dono dei Drak; le armi del caos; il congedo |
| `First Contact: Kuwaru Efreti` | 81–117 | 21 | il Quarg arcaico, il cimitero dei Korathi, le macchine pensanti, i Korath Efreti |

## 2. Scelte

| nodo | scelta | perché |
|---|---|---|
| `Quarg` · `Drak` · `Korath` · `Korathi` · `Hai` | **invariati** | nomi di specie |
| `Korath Efreti` | **invariato**, glossato «Amici dei Korath» | è un nome proprio che il testo stesso traduce |
| `ringworld` | **mondo ad anello** | non «anello orbitale»: è la struttura dei Quarg |
| `this one` | **«questo uno»** | il Quarg parla di sé in terza persona; non è un refuso |
| `accordion / beehive / starship engine` | **fisarmonica / alveare / motore di una nave** | |
| `gold or violet irises` | **iridi d'oro o viola** | |
| `like a dog walking on its hind feet` | **come un cane che cammina sulle zampe posteriori** | |
| `very subtle lungs` | **polmoni assai delicati** | *subtle* = delicati, non «sottili» |
| `ancient roads between the stars` | **antiche vie fra le stelle** | |
| `prune away the paths` | **potano via le vie** | metafora botanica conservata |
| `Weapons of chaos` | **Armi del caos** | |
| `snuffing out stars` | **spegnere stelle** | |
| `Tearing the flesh of space and time itself` | **Strappare la carne dello spazio e del tempo stesso** | |
| `unquiet graveyard of the Korathi` | **inquieto cimitero dei Korathi** | |
| `Whither came you, and wherefore visit you us` | **Donde venite, e perché ci visitate** | sintassi arcaica riprodotta, lessico italiano corretto |
| `Ware their ships should you wander` | **Guardatevi dalle loro navi se vagate** | |
| `bring you can we no succor within the bourne of their space` | **nessun soccorso possiamo recarvi entro i confini del loro spazio** | |
| `lest awaken in you we the desire` | **che non si risvegli in voi il desiderio** | |
| `one isolates a fire one cannot extinguish` | **si isola un fuoco che non si riesce a spegnere** | |
| `Korathi` / `Korath` | **Korathi** (collettivo) / **Korath** (singolare) | distinzione del testo, mantenuta |

## 3. Difficoltà

1. **Il primo `LOGBOOK`**: le due schede sono prosa da diario, non etichette. Il `check.py` di L101 asseriva
   `LOGBOOK assente`; qui il controllo è invertito e verifica anche che le due unità siano **tradotte** e
   **lunghe** (>200 caratteri), perché un `LOGBOOK` lasciato identico passerebbe altrimenti inosservato.
2. **Due voci per la stessa specie**: il primo Quarg parla con frasi brevi e solenni e dà del **«tu»**; quello di
   Kuwaru Efreti parla in **inglese arcaico** con sintassi invertita e dà del **«voi»**. La differenza è nel
   sorgente (registro e persona) e la resa la conserva: non è un'incoerenza, è caratterizzazione.
3. **`this one`**: il Quarg si riferisce a sé in terza persona («non è un peso per questo uno parlare con te»).
   Una resa «per me» sarebbe più naturale e cancellerebbe il tratto alieno.
4. **Due token nella stessa unità** (42): `<first> <last>`, nell'ordine. Sono il nome del giocatore e il gioco li
   sostituisce — nessuno dei due va tradotto o spostato.
5. **Tre ripetizioni**: la domanda `"Who are the Drak?"` posta due volte (17 e 20) e due risposte lunghe
   ripetute (35/40, 37/38). Rese da costanti uniche nel costruttore.
6. **`Korath` / `Korathi`**: il testo usa il singolare per l'individuo e il collettivo per la specie. In italiano
   la distinzione si perde facilmente; è mantenuta («i Korathi», «un Korath»).

## 4. Numeri osservati

```
unita' 48/48 · 46 MISSION_TEXT + 2 LOGBOOK · tab 44 · virgolette 98 = 98 · token 2 = 2 · quadre 0
parole EN 1675 -> IT 1632 · rapporto 0.70 - 1.24
righe 19/117 · file 178 unita · max(line) 506 · 0 prima / 130 dopo
FAIL totale: 0 (29 controlli) · verify exit 0 (27 controlli)
sha256[:16] d1e12262951885ee · copertura file 48/178 (27,0%)
```

## 5. Stato del progetto

```
TOTALE staging: 25339 unita · 813044 EN · 770761 IT
quarg missions.txt: 48/178 (27,0%) · 1 lotto
file completi: 39 · residuo traducibile (formula state.py): 6591
residuo misurato: 7166 unità / 163003 parole su 127 file
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | tre parti, `translation.json`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (29 controlli), `verify.py` exit **0** (27 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 48 unità restano `PENDING`; il gioco non è stato caricato.
- **Il file non è completo**: 130 unità su 6 contesti; prossimo contratto `HANDOFF_L103_20261018.md` (righe
  118–249), che porta **tre tipi nuovi** in questo file: `DESCRIPTION`, `DIALOG` e `VALUE`.
- **Nessuna revisione umana**.
