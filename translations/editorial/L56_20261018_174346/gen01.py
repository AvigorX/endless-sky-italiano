# -*- coding: utf-8 -*-
# part01: unita' 1-27 (Passive-Aggressive Observations, Foreign Spectator, Brief Bystander, Scin on Cyife).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Mentre navighi i cieli di questo mondo desertico, rilevi letture sotterranee simili a quelle del pianeta dove hai incontrato per la prima volta un Gegno Vi. Probabilmente anche questo mondo ospita la stessa specie, o una simile, di grandi creature serpentine che affrontasti allora. Alla fine ti imbatti in un grande vascello Gegno Vi posato sulla superficie; a differenza del tuo incontro precedente, però, la nave non è sprofondata nel deserto: dev'essere atterrata qui di recente. Un gruppo di guerrieri Vi sta uscendo e si sta disponendo lì vicino, e mentre lo fanno compaiono sopra di te altre due navi Gegno.",
2: "(Vattene.)",
3: "(Continua a osservare.)",
4: "Le navi in avvicinamento scendono verso la superficie senza dedicarti attenzione. Una è dello stesso modello di quella a terra, probabilmente un trasporto. L'altra invece sembra una specie di intercettore, anche se è decisamente più grande di qualcosa come uno Sparrow dello spazio umano, forse persino delle dimensioni di un Headhunter.",
5: "Considerando che il pianeta ospita altri di quei mostri di prima, e che i Vi sono qui in forze, forse è meglio andarsene ora prima che la situazione sfugga di nuovo di mano.",
6: "(Vattene.)",
7: "(Avvicinati alla zona di atterraggio.)",
8: "Dai gas e ti dirigi verso la zona di atterraggio dei Vi. Mentre il trasporto ha già toccato terra, l'intercettore, ancora in fase di atterraggio, si gira di colpo verso di te mentre ti avvicini. A differenza delle navi da guerra Scin che hai affrontato pochi giorni fa, più reattive alla tua presenza che dirette, i Vi qui si stanno facendo in quattro per avvicinare la tua nave. Un momento dopo ricevi quella che suona come una chiamata rabbiosa dall'intercettore.",
9: "\"Tchii ciei escitch tchii iedf teih Voordhte!\"",
10: "(Vattene subito.)",
11: "(Continua.)",
12: "Decidi che è meglio non invadere oltre lo spazio dei Vi: non si può sapere cosa farebbero se continuassi. Quando ti allontani, l'intercettore scatta brevemente in avanti verso di te, stizzito, e continua a osservarti finché non hai lasciato la zona. Mentre gli Scin sembravano più aperti all'interazione, i Vi ne sono chiaramente contrari.",
13: "Decidi di continuare a volare verso i Vi senza dare ascolto al loro avvertimento. Senza esitare, l'intercettore comincia a caricare verso di te e le navi a terra si preparano al decollo. Persino alcuni soldati Vi a terra gridano e gesticolano verso la tua nave con le armi. A quanto pare i Vi non tollerano più la tua presenza.",
14: "Decidi di ritirarti dalla zona, e le navi proseguono verso la superficie come se tu non fossi mai stato lì. Che potessero essere ostili o no, immischiarsi in quella che potrebbe essere un'esercitazione militare può essere pericoloso, soprattutto con i Vi.",
15: "Entrando nel sistema noti al centro una flotta Vi e una Scin, anche se nessuna delle due attacca l'altra. Stanno invece osservando due navi, una per parte, che sembrano sfidarsi. Forse è una sorta di evento cerimoniale tra le fazioni Gegno. Meglio non interferire.",
16: "La presenza di vecchi strumenti di registrazione sparsi sulla superficie di questo pianeta sembra contraddire il disinteresse con cui i Gegno paiono trattarlo. Nonostante si trovi nel sistema natale dei Gegno, Heutesl, il pianeta è apparentemente deserto. Tuttavia, dato che non è sotto stretto controllo Gegno, è un buon posto dove fermarsi, e sembrano non accorgersi né interessarsi del tuo atterraggio.",
17: "Però, mentre voli in cerchio, noti un piccolo shuttle Gegno parcheggiato a terra. Il colore marrone chiaro dello scafo suggerisce che sia un mezzo civile, ma cosa ci faccia qui è ignoto.",
18: "(Indaga.)",
19: "(Lasciali stare.)",
20: "Dirigi la nave verso lo shuttle e, avvicinandoti, riesci a vedere un Gegno a terra che armeggia con uno dei dispositivi vicini. Mentre ti avvicini, smette di lavorare e torna al suo shuttle, decollando poco dopo. Sembra che non fosse interessato a un eventuale contatto con te.",
21: "Atterrando accanto al satellite, scendi a dare un'occhiata. Il dispositivo è indistinguibile dagli altri che hai visto finora. L'unico tratto notevole sembra essere la sua età avanzata.",
22: "Non c'è niente di molto interessante su questa luna fredda e inospitale in mezzo al nulla. C'è però qualcosa di un po' strano nella superficie di Cyife. Parte della luce rifratta attraverso la superficie sembra dissolversi o riflettersi in schemi strani. Anche se sembra ghiaccio, un esame più attento rivela che piccole chiazze del terreno sono fatte di un altro tipo di materiale cristallino. In lontananza c'è qualcosa che spicca davvero su questo mondo: una grande struttura a forma di uovo con una tonalità verde.",
23: "Avvicinandoti abbastanza, l'oggetto oblungo si rivela una grande nave Gegno con i colori della fazione Scin. Cosa ci faccia così lontano dal loro spazio natale è un mistero, come la luna su cui è posata. Dopo qualche secondo si lancia nell'atmosfera e lascia la luna. Non sembra essere rimasto nulla dove era parcheggiata, né traccia di cosa stessero facendo gli Scin qui.",
24: "saw epidote",
25: "Avvicinandoti abbastanza, l'oggetto oblungo si rivela una grande nave Gegno Scin, simile a quella incontrata durante un'interazione con gli Scin tempo fa. Cosa ci faccia così lontano dal loro spazio natale è un mistero, come la luna su cui è posata. O almeno lo era: dopo qualche secondo si lancia nell'atmosfera e lascia la luna.",
26: "boarded epidote",
27: "Avvicinandoti abbastanza, l'oggetto oblungo si rivela una delle grandi navi da ricerca degli Scin, dello stesso tipo di quella in cui sei entrato durante un'interazione con gli Scin tempo fa. È possibile che gli Scin abbiano trovato il mistero di Cyife abbastanza interessante da viaggiare così lontano dal loro spazio natale. Non lo saprai mai con certezza: dopo qualche secondo la nave si lancia nell'atmosfera e scompare nello spazio. Non sembrano aver lasciato nulla.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
