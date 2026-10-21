# STATO — L229 · `korath outfits.txt` (secondo lotto)

| Voce | Valore misurato |
|---|---|
| Directory | `staging/editorial/L229_20261019_231932` |
| Righe / unità | **208–318** / **15** — file a **35/92 (38,0%)** |
| Tipi | **11 `DESCRIPTION`** · **4 `VALUE`** |
| Tab · virgolette · apici | **3** (unità 7, 10, 13) · **0** · **4 EN / 12 IT** |
| Segnaposto | **0** |
| Contesti | **8** — Asteroid/Comet/Lunar 3 unità, Planetary 2 (la seconda scheda è oltre il confine) |
| Parole | **431 EN → 442 IT** (1,00–1,21, media 1,10) |
| sha256 | `b85fa00ea11fb613…` |
| Esiti | `check.py` **27** (`FAIL totale: 0`) · `verify.py` **18** (`FAIL: 0`) |

## I tab tornano dopo lo zero

L228 aveva **zero tab** — un primato. Qui ce ne sono **3** (unità 7, 10, 13). «Zero tab» era una proprietà del **lotto**, non
del file: ereditare quel numero avrebbe fatto cercare un'assenza che non c'è.

## Tre unità quasi identiche, con un `may` di differenza

| unità | inglese | italiano |
|---|---|---|
| 7 | *…an explosion that **may** nearly melt the thruster* | «…un'esplosione che **può quasi fondere** il propulsore» |
| 10 | *…an explosion that nearly melts the thruster* | «…un'esplosione che **quasi fonde** il propulsore» |
| 13 | **identica alla 10** | **identica alla 10** |

Le unità 10 e 13 sono lo stesso paragrafo (Comet e Lunar Class); la 7 (Asteroid Class) ha il `may` in più. Il `check.py` e il
`verify.py` verificano **entrambe** le relazioni: `t[10] == t[13]` e `t[7] == t[10]` con la sola sostituzione del verbo.

## Il confine spezza una scheda — e il controllo lo registra

L'ultima unità del lotto (riga 318) e la prima dopo il confine (riga 319) sono **due schede dello stesso equipaggiamento**,
`Afterburner (Planetary Class)`. Il `verify.py` verifica che il contesto dell'ultima unità del lotto sia **lo stesso** della
prima unità esclusa: è il modo di accorgersi che la finestra è tagliata a metà di una scheda, senza doverla completare a
memoria.

## Cosa contiene

Il **Fuel Processor** (nato nella Guerra Civile Korath per non restare a secco contro gli Hai), il **Command Center** dei
Kor Efret (per pilotare le navi robotiche catturate), il **Reasoning Node** e il **Control Transceiver** (i sistemi che
governano gli automata Mereti e Kor Sestor), e i quattro **Afterburner** — Asteroid, Comet, Lunar, Planetary — che pompano
carburante per l'iperspazio surriscaldato nel flusso di plasma.

## Difficoltà

1. **`raid the Hai for supplies`** → «razziando gli Hai per procurarsi rifornimenti»: gli Hai restano invariati, l'articolo
   è italiano.
2. **`would often end up stranded after they had run out of fuel`** → «finivano spesso bloccate dopo aver esaurito il
   carburante»: `stranded` = bloccate, resa già usata in L225 e L227.
3. **`hybrid fuel storage and ramscoop device`** → «dispositivo ibrido di stoccaggio del carburante e ramscoop».
4. **`minimal, spartan Command Center`** → «Command Center minimale e spartano»: `spartan` non è «spartano» nel senso di
   austero ma proprio di essenziale, e la resa lo tiene.
5. **`override the AI and interface with the ship's controls`** → «scavalcare l'IA e interfacciarsi con i comandi della
   nave».
6. **`would make it nearly impossible to spoof the control signals`** → «rendere quasi impossibile falsificare i segnali di
   controllo».
7. **`squeeze a hyperdrive into otherwise intrasystem ships`** → «infilare un'iperguida in navi altrimenti confinate
   all'interno di un sistema». `hyperdrive` → «iperguida»: termine scelto e dichiarato, distinto da `jump drive` che resta
   invariato.
8. **`a phenomenal explosion that may nearly melt the thruster`** → «un'esplosione fenomenale che può quasi fondere il
   propulsore»: il `may` è un'eventualità, non una certezza, e la differenza con la 10 va mantenuta.

## Un errore mio, corretto prima di chiudere

Avevo scritto che i quattro `Afterburner` avevano **2 unità ciascuno**: il valore misurato è **3/3/3/2**, perché Asteroid,
Comet e Lunar comprendono anche il `VALUE` oltre alle due `DESCRIPTION`, mentre Planetary ha solo il `VALUE` e una
`DESCRIPTION` entro il confine (la seconda è alla riga 319). Il `check.py` è caduto con `FAIL 1` e ho corretto lui, non il
testo.

## Verifica

```bash
cd staging/editorial/L229_20261019_231932
python check.py     # FAIL totale: 0 (27 controlli)
python verify.py    # FAIL: 0 (18 controlli) · 35/92 · 57 dopo la 318 · confine 319
```

**Non verificato**: nessun equipaggiamento visto nel gioco; 15 unità `PENDING`.
