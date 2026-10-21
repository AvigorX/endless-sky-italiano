# REPORT — L129 · `boarding missions.txt` (il mercante da assistere, l'asteroide, il carico)

## 1. Contenuto

| blocco | unità | righe | cosa contiene |
|---|---|---|---|
| `conversation:assisting merchant` | 1–2 | 15–19 | i due template `${...}` che compongono la frase casuale |
| frasi 1-1 · 1-2 · 1-2 hazardous · 1-3 · 2 · 3 · 4 | 3–50 | 87–165 | i 48 frammenti del generatore di frase |
| `Asteroid Course` | 51–70 | 172–238 | `VALUE`, `DESCRIPTION`, l'asteroide, le quattro scelte, i cinque esiti, il pagamento |
| `Dangerous Journey` | 71–77 | 245–269 | `VALUE`, `DESCRIPTION`, il capitano che molla il carico, la consegna |
| `assisting law enforcement` | 78–81 | 274–279 | il capitano della nave riparata, la flotta pirata, le due scelte |
| `Assisting Free Worlds` · `Republic` · `Deep Security` · `Syndicate` | 82–89 | 286–386 | quattro `VALUE` uguali e quattro `DESCRIPTION` uguali |

## 2. Scelte

| nodo | IT | nota |
|---|---|---|
| `Knowing that` · `Since` · `Understanding that` | **Sapendo che** · **Poiché** · **Comprendendo che** | apertura della frase |
| `you altered course` · `you went out of your way` | **hai cambiato rotta** · **ti sei scomodato** | |
| `you risked your life` · `you braved enemy fire` | **hai rischiato la vita** · **hai affrontato il fuoco nemico** | variante rischiosa |
| `to` · `in order to` · `so that you could` | **per** · **al fine di** · **così che potessi** | |
| `save` · `repair` · `rescue` · `secure` · `assist` · `help` | **salvare** · **riparare** · **recuperare** · **assicurare** · **soccorrere** · **aiutare** | sei verbi distinti |
| `its` · `the` · `the ship's` · `the vessel's` | **il suo** · **il** · **della nave** · **del vascello** | |
| `gives you` · `offers you` · `rewards you with` | **ti dà** · **ti offre** · **ti ricompensa con** | senza spazio finale, come il sorgente |
| `in gratitude.` · `in thanks.` · `as thanks.` · `for your assistance.` | **in segno di gratitudine.** · **in ringraziamento.** · **per ringraziarti.** · **per il tuo aiuto.** | |
| `Passengers to <planet>` · `Delivery to <planet>` · `Defend <planet>` | **identici** | `VALUE` |
| `slams by a huge asteroid` | **colpita in pieno da un gigantesco asteroide** | |
| `shield the <origin>` | **fare scudo alla <origin>** | |
| `tearing it to shreds` | **facendola a pezzi** | |
| `you've only made things worse` | **hai solo peggiorato le cose** | |
| `depressurizing` | **depressurizzando** | |
| `I've nearly died` | **quasi ci lascio le penne** | registro colloquiale del capitano |
| `begins loudly swearing` | **comincia a imprecare ad alta voce** | |
| `pirate raid` | **incursione piratesca** | |

## 3. Difficoltà

1. **48 frammenti da comporre**: la resa va scelta pensando alla frase che ne uscirà, non alla parola isolata.
2. **Spazi finali**: metà dei frammenti finiscono con uno spazio, due no (`the`, `gives you`). Senza parità di spazi la
   composizione perde le parole: il controllo verifica **89/89** unità.
3. **Due difetti del sorgente riprodotti**: `the` senza spazio finale (→ `theits` / `ilil`) e frase sgrammaticata per
   costruzione. Non si correggono.
4. **Quattro unità che non sono testo** (2 template `${...}`, 2 nomi di frase): tradurle romperebbe il gioco.
5. **Due frammenti di sola punteggiatura** (`, ` e `.`): identici per necessità, dichiarati, altrimenti il controllo
   «tutte tradotte» li boccia.
6. **43 token in 7 famiglie** su 852 parole: sequenza verificata **per unità**, non solo in somma.
7. **Gate**: sei frammenti riscritti per rientrare nel 0,55–1,90 (`Since` → `Poiché`, `rescue` → `recuperare`,
   `secure` → `assicurare`, e i due composti del carico/equipaggio). Il gate non è stato allargato.
8. **80 testi distinti su 89**: tre opzioni ripetute e otto testi di missione uguali a gruppi di quattro.

## 4. Numeri osservati

```
unita' 89/89 · TEXT 48 · MISSION_TEXT 21 · CONVERSATION 6 · VALUE 6 · DESCRIPTION 6 · DIALOG 2 · tutte PENDING
contesti 18 · testi distinti 80 · 4 identici (2 template, 2 nomi di frase) · 2 punteggiatura · 6 VALUE
tab 22 unita · virgolette 10 · token 43 in 7 famiglie · spazi iniziali/finali identici 89/89
parole EN 852 -> IT 819 (0.961) · rapporto 0.56 - 1.80, media 1.14
righe 15/386 · file 89/240 (37,1%) · 0 prima / 151 dopo · confine riga 417
FAIL totale: 0 (30 controlli) · verify exit 0 (30 controlli)
sha256[:16] fee796a7a3f4f2bd
```

## 5. Stato del progetto

```
TOTALE staging: 27076 unità · 856476 EN · 813821 IT
boarding missions.txt: 89/240 (37,1%) · 1 lotto · 852 EN -> 819 IT
file completi: quarantasei · residuo traducibile (formula state.py): 4854
residuo misurato: 5494 unità / 120526 parole su 120 file
avanzamento: 27076/32924 unità (82,2%) · 856476/979975 parole (87,4%)
```

## 6. Livello raggiunto

| Livello | Raggiunto | Prova |
|---|---|---|
| IMPLEMENTATO | sì | 3 parti, `translation.json`, `mkparts.py`, `check.py`, `verify.py`, `STATO.md`, `REPORT.md`, `review.md` |
| ESEGUITO | sì | script lanciati, output letto |
| **VERIFICATO** | **sì** | `check.py` `FAIL totale: 0` (30 controlli), `verify.py` exit **0** (30 controlli) |

## 7. Non ancora fatto (dichiarato)

- **Nessuna approvazione**: 89 unità `PENDING`, nessuna missione caricata nel gioco.
- **Nessuna revisione umana**.
- **Il file non è completo**: restano **151 unità** (righe 417–959).
- **Prossimo lotto**: `HANDOFF_L130_20261019.md` — righe **417–686**: **75 unità**, **2.087 parole**, **4 contesti**,
  **22 `UI_LABEL`**, **45 unità con tab**, **31 virgolette**, **19 token in 5 famiglie**.
