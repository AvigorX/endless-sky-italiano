# L19 — Revisione editoriale: `data/human/human missions.txt` 1811–6428

**1.611 unità · 39.968 parole inglesi → 37.324 italiane · 70 missioni + 3 `event` · 9 sezioni.**
Quarto lotto del file. Target editoriale della sessione: ~40.000 parole sorgente (raddoppio del target
precedente di ~20.000). Deviazione: **−32 parole (−0,08%)**, interamente dovuta ai confini reali delle
missioni (vedi §1).

---

## 1. Confine del lotto: perché finisce a 6428 e non a 6484

`next_section.py` con `lo=40000 hi=44000` propone **1811–6484 (1636 unità, 40.689 parole)**, ma la riga 6484
cade **dentro** la missione `Care Package to South 1` (6432–6494): il confine violerebbe la regola «fine
missione». Il primo confine utile è **6428**, dove si chiude `Blind Man from Martini` e la riga 6432 apre
`Care Package to South 1`.

Il primo export (`L19_20261017_201342`, righe 1811–6484) è stato **scartato** senza produrre traduzioni e
lasciato sul posto con un `NOTE.md` che ne spiega il motivo: è la prova che la ricognizione ha corretto il
confine prima di scrivere, non dopo.

**Sezioni misurate** (confini da `next_section.py`, 4.000–5.000 parole ciascuna):

| Sezione | Righe | Unità | Parole EN | Parti |
|---|---|---:|---:|---|
| 1 | 1811–2375 | 180 | 4.821 | part01–04 |
| 2 | 2381–2815 | 131 | 4.233 | part05–07 |
| 3 | 2821–3343 | 144 | 4.086 | part08–11 |
| 4 | 3348–3894 | 176 | 4.077 | part12–13 |
| 5 | 3901–4473 | 226 | 4.018 | part14–16 |
| 6 | 4493–4968 | 168 | 4.043 | part17–18 |
| 7 | 4972–5422 | 223 | 5.942 | part19–21 |
| 8 | 5428–5830 | 172 | 4.047 | part22–23 |
| 9 | 5846–6428 | 191 | 4.701 | part24–25 |

La sezione 7 supera la soglia alta (5.942) perché il contesto `Dangerous Games 2` è una singola missione da
oltre 5.000 parole: spezzarla avrebbe diviso un'unità narrativa con 71 `UI_LABEL` interne.

---

## 2. Ricognizione e classificazione

| Tipo | Unità | Traducibile | Nota |
|---|---:|---|---|
| `MISSION_TEXT` | 1.359 | sì | prosa e opzioni con tab iniziale |
| `DESCRIPTION` | 71 | sì | schede pianeta (`event`) e descrizioni di missione |
| `VALUE` | 60 | sì con cautela | `name` mostrato al giocatore |
| `DIALOG` | 59 | sì | testi di atterraggio e di inseguimento scorte |
| `LOGBOOK` | 23 | sì | diario in prima persona |
| `UI_LABEL` | **39** | **no** | `label`, bersaglio di `goto` |

Nessun `TEXT`, nessuna `phrase`, **nessuna riga con più di un'unità** (in questo tratto non ci sono `log`):
il blocco di composizione di L18 non serve e `check.py` non lo contiene.

Le 39 `label` sono state verificate una per una (kind nel DB, `raw` nel sorgente, uso come bersaglio nella
missione) e restano **identiche**: `paradise accept`, `final decline`, `hello too`, `help request`,
`refrigerate`, `invited`, `internal`, `killed anglerfish`, `disabled anglerfish`, `caught anglerfish`,
`passed tarazed`, `orbiting tarazed`, `human space`, `hai start`, `next steps`, `walks away`, `zero deal`,
`counter deal`, `pay up`, `first game watch`, `first game play`, `second game play`, `second game watch`,
`hands up`, `riddle two`, `roll call`, `riddle three`, `sub pods`, `all dead`, `some survive`,
`only player`, `can't make it in time`, `can't take package`, `picture failure`, `picture success`,
`didn't take picture`, `security job`, `come along`, `atomic bombings`.
Sono elencate in `check.py` (`NT`) e `verify.py` ne ricontrolla identità e kind.

### 2.1 Il caso nuovo: 23 unità con citazione non chiusa

Ventitré unità hanno un numero **dispari** di virgolette nel sorgente: la battuta si chiude nell'unità
successiva (lettera di Diana, messaggio di Amy, botta e risposta del signor Smith, discorso del funzionario
della Marina, lettera anonima, racconto di Douglas). Il conteggio per unità è stato **riprodotto
esattamente**, non «corretto». Unità: 207, 208, 209, 257, 320, 446, 481, 482, 491, 512, 530, 576, 577, 702,
961, 962, 963, 968, 969, 970, 1440, 1587, 1591.

---

## 3. Il punto editoriale del lotto: acrostico e indovinelli

`Dangerous Games 2` contiene tre indovinelli che guidano la navigazione sott'acqua. Il primo è un
**acrostico**: le iniziali delle cinque righe inglesi compongono `N-O-R-T-H`, e la riga finale («Heed the
beginnings to live») dice al giocatore di guardare gli inizi. Un acrostico non è ornamentale: è il
meccanismo. La resa italiana conserva **le stesse cinque iniziali**:

| # | Inglese | Italiano | Iniziale |
|---|---|---|---|
| 1 | No other path may you take | Nessun'altra via ti è concessa | **N** |
| 2 | Oiled skins flash and flicker | Oliate pelli guizzano e lampeggiano | **O** |
| 3 | Razor spikes grow from the deep | Rasoi di spine sorgono dal profondo | **R** |
| 4 | Titanic walls crush and smash | Titaniche pareti schiacciano e frantumano | **T** |
| 5 | Heed the beginnings to live | Hai da badare agli inizi, se vuoi vivere | **H** |

**Perdita dichiarata:** il secondo indovinello inglese gioca su *beast / bee* («Go to beast that has no
bee»), e l'italiano non ha un gioco equivalente fra «bestia» e «ape». Ho tradotto il senso letterale
(«Va' dalla bestia che ape non ha») e il commento del capitano («Un poeta, questo scrittore, proprio no»),
perdendo il bisticcio: **il gioco di parole è intraducibile senza riscrivere l'indovinello**, e riscriverlo
avrebbe rotto il rapporto con la soluzione (la rotta a est). Anche la rima dei distici è caduta: ho
privilegiato il contenuto, che qui è funzionale al gameplay.

---

## 4. Convenzioni applicate

| Termine | Resa | Occorrenze | Note |
|---|---|---:|---|
| `Free Worlds` | **invariato** («i Free Worlds») | 18 | fazione: nomi di fazione invariati (§6 del checkpoint) |
| `Paradise Worlds` / `Paradise Planets` | Mondi Paradisiaci / Pianeti Paradisiaci | 4 / 5 | coerente con L10, L15, L18 |
| `Republic` / `Navy` | Repubblica / Marina | molte | già consolidato |
| `Syndicate` / `Syndicated Security` | Sindacato / Sicurezza del Sindacato | molte | — |
| `Syndicated Shipyards`, `Southbound Shipyards` | invariati | 1 / 4 | ragioni sociali |
| `Academy of Planetary Sciences` | invariato | 2 | istituzione (decisione 27) |
| `the Academy` (forma breve) | l'Accademia | 3 | nome ufficiale in inglese, riferimento breve in italiano |
| `Alexandria Station`, `University of New Sydney`, `University of Chiron` | invariati | 5 / 5 / 1 | istituzioni e stazioni |
| `Hauler`, `Firebird`, `Bounder`, `Vanguard`, `Argosy`, `Quicksilver`, `Frigate`, `Polecats` | invariati | — | classi di nave (decisione 17) |
| `Dragonriders` | **Cavalcaladri** | 13 | nome che il gruppo si dà da solo: tradotto come nomignolo, non come classe |
| `subpods` | sottopodi | 29 | apparecchi dei passeggeri |
| `quoijuu`, `scyllae`, `taniwhales`, `morgawrii` | invariati | 2 / 1 / 1 / 1 | nomi di creature aliene |
| `Core` | Core | 9 | il dispositivo su cui è caricata una mente |
| `Limping Pappa`, `Enrico Snake`, `Karengo`, `Ci`, `Mister Smith`, `Diana Howl`, `Riley`, `Douglas Pears` | invariati | — | nomi propri |
| `Remembrance Day` | invariato | 2 | già consolidati |
| `wormhole` | invariato | 21 | termine tecnico (decisione 11) |
| `interference plating` | piastre di interferenza | 1 | descrizione, non nome di equipaggiamento nel testo |
| `Mistress Marionette` | invariato | 1 | nome d'arte |
| `Mafia` / `mafia` | Mafia / mafia | 1 / 1 | la differenza di maiuscola del sorgente è riprodotta |
| `Mr. Smith` | signor Smith | 4 | — |

**Registro:** il giocatore è «tu»; i funzionari (ufficiale della Marina, impiegato del Sindacato, addetta
del Sindacato, receptionist) usano «lei»; Amy, Diana, Karengo, Gaint, il bibliotecario usano «tu». Cygnet
Brig (trafficante di schiavi) parla con elisioni e sintassi popolare («sennò si passano le malattie l'uno
con l'altro»), senza cadere in un dialetto regionale specifico: la scelta è deliberata, per non spostare il
personaggio in un'Italia che nel gioco non esiste.

---

## 5. Interventi in stesura e rilettura

| # | Unità | Intervento | Perché |
|---|---|---|---|
| 1 | 9 | «Farò caricare la bestia sulla tua nave dai miei uomini» → «Ordinerò ai miei uomini di caricarla subito sulla tua nave» | ordine delle parole innaturale in italiano |
| 2 | 16 | «Ci dicono che… dicono» → «Sentiamo dire che… dicono» | ripetizione del verbo nello stesso periodo |
| 3 | 131 | Amy passa dal «lei» al «tu» → «puoi raggiungermi… da darti» | registro: Amy dà del tu al capitano in tutte le altre unità |
| 4 | 1572 | «Andrà tutto bene» (ratio 0,54) → «Vedrà che andrà tutto bene» (0,75) | unità breve sotto soglia: allungata con una forma di cortesia, non con un riempitivo |
| 5 | 1102 | `а` cirillico in «echeggiа» → `a` latina | refuso introdotto in stesura; ora c'è un controllo dedicato |
| 6 | 687 / 693 | «scagnozzi della Mafia» / «della mafia» | l'inglese differisce solo per la maiuscola: riprodotta |
| 7 | 391 | «Va bene, gliela consegno» → «D'accordo, gliela consegno» | 368 e 391 hanno inglese diverso («Okay» / «Alright») |
| 8 | 714 | «Ne ho sentite abbastanza» → «Basta così» | idem: 708 e 714 hanno inglese diverso |
| 9 | 932 | «Va bene, posso portarti» → «E va bene, ti porto» | idem: 927 «Okay» / 932 «Fine» |
| 10 | 1174 | «(Scappa.)» → «(Fuggi.)» | 119/122 dicono «Run away», 1174 dice «Run» |
| 11 | 1212 | «(Avvicinati.)» → «(Avvicinati di più.)» | 14 dice «Approach them», 1212 «Move closer» |
| 12 | 126 | «Che cosa facciamo adesso?» → «Che cosa facciamo?» | 199 dice «What do we do now?» |
| 13 | 946 | «Spiacente, sono molto impegnato adesso» → «sono davvero molto impegnato» | 655/665 dicono «too busy right now», 946 «really busy right now» |
| 14 | 1253 | «(Ignala.)» → «(La ignoro.)» | 774 dice «Ignore it» (oggetto), 1253 «Ignore her» (persona) |
| 15 | 1321 | «(Torna alla mia nave.)» → «(Ritorno alla mia nave.)» | 440 dice «Return to my ship», 1321 «Go back to my ship» |
| 16 | 1468 | «non vado in quella direzione» → «non sono diretto in quella direzione» | 415 dice «traveling», 1468 «heading» |
| 17 | 1605 | «Va bene» → «D'accordo» | 945 dice «Okay», 1605 «Alright» |
| 18 | 61 | virgoletta di chiusura in più | errore di stesura, trovato da `check.py` |
| 19 | 23 unità | firma delle virgolette allineata al sorgente | citazioni aperte e non chiuse (§2.1) |

I punti 6–17 sono **duplicati italiani su inglese diverso**: il controllo li ha segnalati tutti, e la
correzione è stata lessicale, mai una deroga al controllo. I punti 1–5 li ha trovati la rilettura.

---

## 6. Decisioni aperte

1. **Acrostico N-O-R-T-H**: conservato con parole italiane che iniziano per N, O, R, T, H. È una scelta
   visibile al giocatore: se in futuro si cambia una riga, l'indovinello smette di funzionare. Il test
   esiste solo nei dati, non nel runtime.
2. **Secondo indovinello**: il bisticcio *beast/bee* è perduto (§3). Se si vuole recuperarlo serve
   riscrivere l'indovinello e la soluzione, cioè cambiare il gameplay: **non l'ho fatto**.
3. **`Free Worlds` invariato** con articolo italiano («i Free Worlds»): è la prima volta che la fazione
   compare in un lotto tradotto. Da ratificare una volta per tutto il corpus (come `Wanderers`, `Remnant`).
4. **`Dragonriders` → Cavalcaladri**: nomignolo coniato dai personaggi, non classe di nave. Se si preferisce
   l'invariato, la modifica è locale (12 unità, sezioni 7).
5. **`subpods` → sottopodi**: termine mai comparso prima nei lotti tradotti (`first game` a parte la `label`
   `sub pods`). Da allineare quando si tradurranno i file degli equipaggiamenti.
6. **`Core` invariato**: nome del dispositivo. Coerente con `the Core` → «il Nucleo»? No: `the Core` è la
   regione galattica (decisione 21), il `Core` qui è un oggetto. La differenza è documentata perché
   altrimenti sembrerebbe un'incoerenza.
7. **`piastre di interferenza`** per `interference plating`: descrizione, non nome di equipaggiamento. Da
   verificare contro i file degli outfit.
8. Restano aperte le questioni dei lotti precedenti (`Successors`, `Consonance`, `caveau`, `ringroide`,
   `Halite`, `Bulk Freighter`, `Costruttori`, `skyhook`, `il Rim`, `il Nucleo`, `Twilight Guard`,
   `Egemonia Bunrodean`, `Wanderers`, `void sprites`, `Laser a impulsi`, `Consigli Confederati`, `rimway`).

---

## 7. Esito dei controlli

```
unità 1611/1611 · mancanti 0 · vuote 0
non traducibili lasciate identiche: 39/39 (label)
duplicati italiani non spiegati dal sorgente: 0 · gruppi inglesi ripetuti nel sorgente: 90 (215 unità)
parole 39.968 → 37.324 · ratio 0,57–1,88
tab 1.236/1.236 · virgolette 2.321/2.321 · token <...> 489/489 · backtick 0/0
spazio iniziale/finale come il sorgente: ok · spazi doppi: 0
tipografia 0 · caratteri non latini 0 · inglese residuo 0 (istituzioni e classi escluse)
state.db 364/32.560 · unità del lotto fuori da PENDING: 0
FAIL totale: 0
```

`verify.py` (indipendente): 17 controlli, tutti OK, exit 0 — riga grezza identica al file per 1.611 unità,
campi DB identici, `state = PENDING`, 39 label identiche con kind `UI_LABEL`, unità successiva riga 6432
`mission:Care Package to South 1`, copertura del file **2.112 / 4.253**.

**Non verificato:** resa in gioco. Nessun avvio, nessuna build, nessun packaging: per mandato. In
particolare non è verificato come il motore presenti le 39 `label`, gli acrostici né i testi con citazioni
non chiuse.

---

## 8. Deviazione dal target

| Voce | Valore |
|---|---|
| Target | ~40.000 parole sorgente |
| Misurato | **39.968** |
| Deviazione | **−32 parole (−0,08%)** |
| Causa | confine a fine missione: 6484 tagliava `Care Package to South 1` |

La granularità interna è rimasta quella consolidata: 9 sezioni da 4.018–5.942 parole, 25 gruppi di
traduzione da 27 a 115 unità (media 64), rilettura e controllo dopo ogni sezione.

---

## 9. Correzione dello strumento condiviso `check_handoff.py` (documentata)

**Difetto riprodotto.** A L19 chiuso, l'handoff corrente è `HANDOFF_L20_20261017.md`. Lo strumento, nella
versione precedente, confrontava il documento con **valori cablati** della transizione L18→L19 (la stringa
`501/ 4253 unità`, il blocco fisso `1811–2375`, il residuo a 3.752 unità). Eseguito sul documento nuovo
usciva **1 con 8 FAIL su 29** — non perché il documento fosse sbagliato, ma perché descriveva il lotto
successivo. Output misurato prima della correzione:

```
copertura missions      FAIL (2112, 4253, 49.659…)
residuo missions        FAIL (3752, 91126)
L19 righe / unità / parole / contesti / confine / tab-virgolette   FAIL
FAIL: 8 / 29 — HANDOFF da rigenerare
```

**Correzione minima.** I valori attesi ora si **leggono dal documento** (regex sulle righe in stile
`state.py` e parsing per riga della tabella del prossimo lotto) e si confrontano con il workspace: stesse
verifiche, nessuna allentata. Se un numero non è nel documento il controllo **fallisce** (l'omissione non
può produrre un verde). Il file default è l'`HANDOFF_*.md` più recente. Le tre uscite `_ui` restano coperte
da `state.py`, che le confronta con `protected.sha256`.

**Verifica della correzione (falsificabilità).** Tre prove eseguite e misurate:

| Prova | Esito atteso | Esito osservato |
|---|---|---|
| documento corrente, non modificato | 0 FAIL | **0 FAIL / 30, exit 0** |
| unità del prossimo lotto alterata (1.676 → 1.600) | FAIL su quella riga | **FAIL 1 / 30, exit 1** |
| riga «Unità» della tabella rimossa | FAIL (tabella incompleta) | **FAIL 1 / 25, exit 1** |
| totale dello staging alterato (3.656 → 3.000) | FAIL | **FAIL 1 / 30, exit 1** |

La versione precedente è conservata come `staging/editorial/tools/check_handoff.py.bak_L19` per confronto.
Nessun altro strumento condiviso è stato toccato: `state.py`, `export_section.py`, `next_section.py` e
`protected.sha256` sono invariati (lo conferma `state.py`, exit 0).
