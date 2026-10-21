# L46 — revisione editoriale

`data/successors/successor 1 prologue.txt` · righe 24–664 · 221 unità · chiuso il 2026-10-18.
Questo file registra le **decisioni di traduzione** e i **limiti osservati**, non le lodi.

## 1. La voce dei Successori: registro arcaico senza arcaismi lessicali

Il sorgente fa parlare Sieasej e Riijaaora in un inglese arcaico marcato: `thou`, `thee`, `thy`, `hast`,
`'tis`, `'twere`, `t'shall`, contrazioni con l'apostrofo in mezzo alle parole (`reach'd`, `possess'd`,
`spoil't`, `swaddled`), oltre a una sintassi latineggiante («that's noble in reason, infinite in
faculty»).

Scelta: **seconda persona singolare più sintassi sostenuta**, senza lessico arcaico italiano.

| tratto del sorgente | resa | perché |
|---|---|---|
| `thou` / `thee` / `thy` | **tu / ti / tuo** | la seconda persona singolare è già marcata rispetto all'inglese moderno |
| `'tis` / `'twere` | **è / era** oppure **«È un mondo…»** a inizio frase | l'italiano non ha contrazione equivalente; riprodurla sarebbe caricatura |
| `thou may'st` / `thou should'st` | **puoi / dovresti** | l'arcaismo inglese è morfologico, non semantico |
| sintassi latineggiante | **ordine marcato ma leggibile**: «Perché la vita è cosa rara e preziosa…» | mantiene solennità senza oscurità |
| `prithee note` | **«Ma sappi»** | l'invocativo arcaico non ha corrispettivo che non suoni finto |
| `fair captain` / `fair citizen` | **«onesto capitano» / «onesto cittadino»** | `fair` qui è allocutivo cortese, non «giusto» |

La scelta è coerente con L45, dove la stessa voce era già stata resa così: **non** si introduce qui un
registro diverso per lo stesso popolo.

## 2. Limite dichiarato: la scheda di Sieasej resta in inglese

L'unità **62** è un `LOGBOOK` ma il suo `english` è solo la categoria (`People`). Sorgente:

```
log "People" "Sieasej" "Sieasej is a Successor scholar of historical linguistics ..."
```

`tools/l10n.py` (protetto) estrae come unità la **categoria** quando il testo del diario è fra
**virgolette** invece che fra backtick. Conseguenza: la scheda di Sieasej nel diario di bordo **non ha
testo italiano** e nel gioco comparirebbe in inglese.

- Non è stato toccato nulla: `tools/l10n.py`, `state.db`, `glossary.csv`, `inventory_fields.csv` sono
  protetti da hash (`state.py` → `INTEGRITA'` OK).
- `check.py` e `verify.py` **asseriscono** la lacuna (categoria identica, testo fuori dall'unità) invece
  di nasconderla: è lo stesso difetto già documentato in L45 per le unità 195/305/357/418, qui si ripete.
- È il **quinto** caso della serie. Se si vuole ripararlo serve una decisione esplicita dell'utente,
  perché cambia `state.db`.

## 3. Decisioni puntuali

1. **`House Sioeora` → «Casa Sioeora», `scion` → «erede».** Il titolo nobiliare dei Successori è
   `scion`, non `heir`: la resa «erede» mantiene il rapporto con la Casata ed è già usata nei lotti
   precedenti per Myurej e Chydiyi. Il plurale collettivo `the scions` → **«gli eredi»**.
2. **`the Graveyard` invariato.** Il corpus ha **372** occorrenze di `Graveyard` contro **49** di
   «Cimitero» (tutte in L27/L28): la forma dominante vince, e cambiarla qui creerebbe una terza variante.
3. **`the scar` → «la cicatrice».** Non è un nome proprio di regione ma una descrizione (la fascia di
   stelle distorta): la maiuscola nel sorgente non è un titolo. Diverso da `the Scar` (85 occorrenze
   invariate nel corpus come nome di regione), che qui non compare.
4. **`Kijran-Riitaa` / `Kijra-pet` / `Kijran-Khora` invariati.** Sono nomi di specie con morfologia
   aliena; il testo stesso li spiega («the Kijra-'pets'»), quindi la spiegazione resta nel dialogo e il
   nome resta intatto. `Kijra-pet` mantiene il trattino.
5. **`iret` invariato.** Grado onorifico («scholar of the third iret»): tradurlo con «rango» perderebbe
   il termine istituzionale, come già deciso per `Casate Alte`.
6. **`translator` → «traduttore»** quando è il dispositivo; «tradurre» resta il verbo. In L45 il
   dispositivo era «dispositivo di traduzione»: qui ricorre la forma breve perché il testo la usa come
   nome comune («the use of a translator»).
7. **`<a tranq h2h long>` e `<tranq h2h>`** sono token di dato (armi): restano identici. L'unità 135
   aggiunge il token rispetto alla 133: la differenza è nel sorgente, non nella traduzione.
8. **Le unità 42 e 48 sono identiche in inglese** e restano identiche in italiano, come le coppie
   36/49, 38/51, 41/52, 65/68, 82/97, 89/92, 90/93 e il gruppo 9/77/84. Il controllo duplicati non segnala
   nulla perché il sorgente le giustifica: **non** si forza una variazione per far tacere lo strumento.
9. **`(Say nothing.)` tre volte** (9, 77, 84): stesso inglese, stessa resa («Non dire nulla.»). In L45
   la resa equivalente era su unità diverse; qui la ripetizione è voluta dal sorgente.
10. **`Shoot them.` → «Spara loro.»** e `(Shoot them with my sidearm.)` → «Sparagli con l'arma da
    fianco.»: il primo è un ordine secco che uccide il giocatore, il secondo un'azione di combattimento;
    la differenza di registro è nel testo.

## 4. Cosa il lotto **non** dimostra

- Non dimostra che la linea *First Contact* sia giocabile in italiano: i 6 contesti hanno molti `goto` e
  nessuno è stato percorso nel gioco.
- Non dimostra la resa del registro arcaico **a schermo**: la verifica è testuale (tab, virgolette,
  token, exit code), non una lettura in-game dei dialoghi con Sieasej e Riijaaora.
- Non dimostra nulla sulla scheda di diario di Sieasej (§2): resta in inglese per costruzione dello
  strumento.
- Il rapporto lunghezze (0,74–1,38) è dentro il gate 0,55–1,90 ma **non è un giudizio di qualità**.
- Il file **non è completo**: 124 unità dopo la riga 664 non sono state toccate.
