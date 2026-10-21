# review.md — L272 (`data/dialog phrases.txt`, righe 102–172)

Registro delle decisioni editoriali dell'**ultimo lotto** delle frasi generiche: taglie, flotte pirata, contrabbando e
**tributo pacifista**.

## 1. Che cosa dicono queste frasi

Sono il **ritorno** delle missioni: il gioco avvisa il giocatore che il bersaglio è stato eliminato (o non ancora), che il
contrabbando è arrivato (o no), che una missione essenziale dei **Free Worlds** è stata fallita o rifiutata, e che una
**flotta pacifista** rifiuta il tributo.

Il registro è **duro e diretto**, senza ironia: dove il testo è brutale («gli schiavi», «merce altamente illegale»), la resa
non addolcisce.

## 2. Scelte

| inglese | resa |
|---|---|
| `You can claim the bounty payment by returning to <destination>` | **Puoi riscuotere il pagamento della taglia tornando a <destination>** |
| `gratefully pays you <payment> for eliminating the <npc>` | **ti paga <payment> con gratitudine per aver eliminato <npc>** |
| `the <npc> and its fleet has not been eliminated yet` | **<npc> e la sua flotta non sono ancora state eliminate** |
| `Hunt it down and board it before returning` | **Dalle la caccia e abbordala prima di tornare** |
| `there are still pirates circling overhead` | **ci sono ancora pirati che girano in cielo** |
| `take off and help finish them off` | **decollare e aiutare a finirli** |
| `You find the contact at the edge of the spaceport` | **Trovi il contatto ai margini dello spazioporto** |
| `You find the contact outside of the main city` | **Trovi il contatto fuori dalla città principale** |
| `moved from your ship` / `removed from your ship` | **scaricato dalla nave** / **fanno sbarcare** |
| `a reliable, no-questions-asked transporter` | **trasportatore affidabile che non fa domande** |
| `revert to the autosave or another earlier snapshot of your pilot` | **torna al salvataggio automatico o a un'altra istantanea precedente del tuo pilota** |
| `We cannot fight you, nor would we choose to. Have peace.` | **Non possiamo combatterti, né sceglieremmo di farlo. Abbi pace.** |
| `There is no need to rend the skies with your guns.` | **Non c'è bisogno di squarciare i cieli con i tuoi cannoni.** |
| `a piddling sum` | **una somma irrisoria** |
| `this rash decision` | **questa decisione avventata** |

## 3. `transporter` e la reputazione

Due frasi identiche nella parte finale (unità 12 e 15) ripetono: «Non è il modo migliore per costruirti la reputazione di
trasportatore affidabile che non fa domande.» La ripetizione nel sorgente è voluta — è il **commento del gioco** alla
condotta del giocatore, uguale che si tratti di un passeggero o di schiavi. La resa mantiene la formula **identica** nelle
due unità.

## 4. Le otto voci pacifiste

| unità | tono | resa |
|---|---|---|
| 18 | rifiuto pratico | **Questo sistema è troppo piccolo per guerre e violenza.** |
| 19 | domanda | **Perché vuoi dare inizio a uno spargimento di sangue senza senso?** |
| 20 | offerta | **Non combatteremo. Unisciti invece a noi in pace.** |
| 21 | arresa dignitosa | **Non possiamo combatterti, né sceglieremmo di farlo. Abbi pace.** |
| 22 | benedizione | **La pace sia con te, capitano. Non c'è bisogno di squarciare i cieli con i tuoi cannoni.** |
| 23 | rifiuto del tributo | **Non ti combatteremo. Non ti uccideremo. Ma non ti pagheremo nemmeno un solo credito di tributo.** |
| 24 | argomento morale | **Perché dovremmo combattere per una somma irrisoria, quando farlo causerebbe tanta morte e tanto orrore?** |
| 25 | supplica | **Ti supplichiamo di ripensare a questa decisione avventata.** |

Otto frasi **distinte**, verificate come otto rese diverse: appiattirle su un'unica formula avrebbe cancellato la varietà del
sorgente.

## 5. Segnaposto nuovi e vecchi

| segnaposto | conteggio | trattamento |
|---|---|---|
| `<npc>` | 8 | **nave → femminile**: «è stata eliminata», «la sua flotta» |
| `<planet>` | 8 | nome proprio, invariato |
| `<payment>` | 6 | «ti paga <payment>», «incassi il pagamento di <payment>» |
| `<destination>` | 4 | «tornando a <destination>», «non è mai arrivato a <destination>» |
| `<commodity>` | 3 | «il tuo carico di <commodity>» |
| `<bunks>` | **1** | **numero di cuccette**: «<bunks> schiavi» |

## 6. Struttura

| cosa | inglese | italiano |
|---|---|---|
| tab / virgolette | **0 / 0** | **0 / 0** |
| apici | **7** (`You've` ×4, `doesn't` ×2, `won't`) | **4** (`l'atterraggio`, `un'altra` ×2, `c'è`) |
| segnaposto | **30** in 6 famiglie | **30**, stesse famiglie, **per unità** |

## 7. Chiusura del file

`data/dialog phrases.txt` è **54/54** in staging: due lotti (L271 29, L272 25), righe 16–172, tutte `PENDING`.

Cosa **non** significa: non è approvato, non è stato visto nel gioco, non è stato revisionato da una persona. Significa che
in staging **non manca nessuna unità** del file — e `verify.py` lo dimostra sommando i due lotti e confrontando le righe.
