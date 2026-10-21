# L51 — revisione editoriale

`data/avgi/avgi 0 first contact.txt` · righe 413–869 · 152 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. Tre voci umane e due voci Avgi in un solo lotto

Il lotto è il primo in cui parlano **Darius** (umano, disilluso, si incolpa), **Sora** (umana, militare,
diretta) e **Kokkino** (Avgi, formale, militare). La differenza di registro è la cosa che il testo
costruisce, e va tenuta:

| voce | tratto del sorgente | resa |
|---|---|---|
| Darius | frasi spezzate, pause, autoaccusa («I made… a lot of mistakes») | punti di sospensione, incisi brevi, «Ho fatto... molti errori» |
| Sora | secca, ironica («A bunch of selfish cowards, they are») | «Un branco di codardi egoisti», disprezzo senza attenuanti |
| Kokkino | etichetta di modalità + «, domanda?» + linguaggio da stato maggiore | «Considerazione.», «Approvazione.», «Entusiasmo.», «Rincrescimento.» |

Il punto delicato è che **Kokkino è l'unico Avgi del lotto che non parla in modo telegrafico**. Non è
un'incoerenza: nel primo contatto (L50) gli Avgi non avevano ancora il traduttore portatile, e l'unità
119 di L50 è esattamente il dono del dispositivo. Da lì in poi parlano per etichette con sintassi
corretta. Tradurre Kokkino con lo stesso parlato rotto di unità 39 di L50 sarebbe stato un errore di
continuità, non una scelta stilistica.

## 2. Il nome di Darius: incoerenza del sorgente

Il sorgente scrive **`Darius Caldwell`** (unità 4, diario) e **`Darius Calwell`** (unità 129, 148, e in
tutto L50). Il nome proprio **non si traduce**, quindi l'italiano riproduce **entrambe le grafie**,
ciascuna dove compare. La traduzione non unifica e non corregge: se in futuro si decide di uniformare,
la decisione va presa sul corpus intero (L50 + L51), non su una singola unità, e va registrata qui.

Conseguenza pratica: una ricerca su «Calwell» nel corpus italiano trova le unità di L50 e tre di L51;
una su «Caldwell» trova solo i diari di L51. Chi cerca un personaggio deve cercare entrambe.

## 3. Le armi nucleari: il testo non le condanna

Unità 52–58: l'ammiraglio avvisa che «Atomics will be used», il giocatore può rispondere «Non sono
sicuro che le armi di genocidio mi mettano a mio agio», e l'Avgi replica «Non è che le usiamo contro
obiettivi civili». Il testo **non dà ragione a nessuno**: registra due sensibilità. La traduzione ha
tenuto questa neutralità:

- `Atomics` → **atomiche** (sostantivo comune, coerente con L49);
- `weapons of genocide` → **armi di genocidio** (non «di sterminio»: è la parola del giocatore, ed è
  un'accusa, non una descrizione);
- `you humans have some strange sensibilities` → **«voi umani avete una sensibilità strana»**;
- `Annoyance` → **Fastidio**; `Confusion` → **Confusione**; `Approval` → **Approvazione**.

Da qui viene anche il diario 47: «Gli Avgi sembrano usare con entusiasmo le armi nucleari,
contrariamente al tabù che la maggior parte degli umani vi associa» — `enthusiastically` reso
**«con entusiasmo»**, non attenuato in «volentieri».

## 4. Decisioni puntuali

1. **`space shoggoths`** (unità 25): **«shoggoth spaziali»**, con l'iniziale minuscola. È un riferimento
   lovecraftiano messo in bocca a un personaggio che disprezza gli Aberranti; tradurlo («mostri») lo
   cancellerebbe.
2. **`Fairyland`** (unità 9): **«il Paese delle Fate»**. Darius chiama così lo spazio Avgi con
   sarcasmo; la maiuscola mantiene il nomignolo.
3. **`Wardragon`** (unità 32): **Dragoguardia**. Nave Quarg non presente nel corpus: ho scelto un
   composto trasparente invece di lasciare l'inglese, perché il testo la nomina come oggetto di
   scansione e il lettore deve capire che è una nave, non una creatura.
4. **`Mule`** (unità 32) **invariato**: è una classe di nave, come `Hauler` o `Bounder`.
5. **`Deep`** (unità 4, 32, 34): **la Deep**, invariato con l'articolo. È un'organizzazione (Deep Sky è
   una ditta del corpus, ma la Deep è l'istituto di ricerca): «Sicurezza della Deep».
6. **`Assemblyman`** (unità 129, 148): **«membro dell'Assemblea»**, non «Assembleare»: il suffisso
   inglese non ha equivalente naturale e la perifrasi resta chiara.
7. **`stint in the Navy`** (unità 32): **«il mio periodo in Marina»**. `Marina` con la maiuscola: nel
   testo è la marina della Repubblica, un'istituzione.
8. **`the Core`** → **«il Nucleo»**, coerente con il corpus (le opzioni 13 e 15 lo nominano due volte
   nella stessa schermata).
9. **`angry space squirrels`** (unità 16): **«scoiattoli spaziali arrabbiati»**. È una battuta del
   giocatore e va lasciata tale; «scoiattoli spaziali incazzati» avrebbe alzato il registro rispetto
   all'inglese.
10. **`I'll hear you out.`** (unità 90, 94): **«Ti ascolto.»**. Rapporto 0,67 — è una delle unità più
    corte del lotto, e l'italiano non ha modo di allungarla senza aggiungere parole che il sorgente non
    ha.
11. **`opportune jester`** (unità 124): **«buffone capitato a proposito»**. Il commento dell'Avgi
    risponde alla battuta scema del giocatore (unità 123) e la parola `jester` è un giudizio: va tenuta.
12. **`nickel-iron`** → **«nichel-ferro»**, `price controls` → **«controlli sui prezzi»**: la
    vertenza dei minatori è economica, non militare, e il lessico resta tecnico.
13. **`the Twirl system`**, **`Peripheria Station`**, **`Feo Platform`**, **`Arche`**,
    **`Evanescence`**, **`Quintessence`**, **`Empyrean`**, **`Valhalla`**, **`Dabih`**, **`Sadr`**:
    **invariati** (nomi di sistemi e stazioni).

## 5. Il primo `NT` vuoto: cosa cambia nel metodo

Tutti i lotti da L42 a L50 avevano almeno una `UI_LABEL` da lasciare in inglese (da 3 a 35). Qui **zero**.
Il rischio non è tradurre male, è **asserire male**: un `check.py` ereditato con `NT = {12, 89, 113}`
avrebbe controllato tre unità inesistenti e sarebbe passato lo stesso, perché l'elenco vuoto è
silenzioso.

Per questo il `check.py` di L51 contiene un'asserzione in più, esplicita:

```
| unita UI_LABEL nel segmento (0 attese: NT vuoto) | ok | OK |
```

e `verify.py` aggiunge «nessuna unità del segmento e non traducibile per dichiarazione». Entrambi sono
controlli **falsificabili**: se comparisse una `UI_LABEL` non dichiarata, diventerebbero rossi.

## 6. Cosa il lotto **non** dimostra

- Non dimostra che le cinque missioni siano giocabili: i `goto` non sono stati percorsi e le condizioni
  di completamento non sono state verificate.
- Non dimostra la resa **a schermo** dei sei messaggi `dialog` di blocco, che sono la parte visibile al
  giocatore.
- Il rapporto lunghezze (0,60–1,38) è dentro il gate ma **non è un giudizio di qualità**: il minimo
  (unità 7, `"Hello there."` → «"Salve."») è un saluto corto, non una perdita di contenuto.
- Il file **non è completo**: 135 unità dopo la riga 869 non sono state toccate.
