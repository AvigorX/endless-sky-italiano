# -*- coding: utf-8 -*-
# part01: unita' 1-40 (`Dissonance Outreach` + inizio di `Twilight Escape 1`). Niente tab: li mette check.py.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Apertura alla Dissonanza",
2: "Porta Hriso su <destination> per negoziare con i minatori del posto. Potrebbe servirti contattare la stazione per ottenere il permesso di attracco.",
3: "Ti serve <capacity> per trasportare Darius, Sora e Hriso.",
4: "Hriso è un diplomatico Avgi che negozia con i dissidenti scontenti del dominio della Consonanza. Leale alla Consonanza, sembra però provare una certa simpatia per il movimento della Dissonanza e per le sue posizioni.",
5: "Sora ha una visione negativa della Dissonanza e di chi, secondo lei, non contribuisce allo sforzo bellico contro gli Aberranti.",
6: "L'adesione alla Consonanza varia molto tra le diverse entità politiche Avgi, e una parte significativa degli Avgi sfuggiti agli Aberranti non ne riconosce la legittimità.",
7: "La Dissonanza è un termine ombrello per i vari gruppi e individui che non accettano la Consonanza come governo unitario degli Avgi. Dagli anarchici alle corporazioni dissidenti, la Dissonanza è un movimento ampio e variegato, non un gruppo centralizzato.",
8: "Hriso si rivela un Avgi giallo-arancio di mezza età. \"Entusiasmo. Un vero piacere conoscerla, capitano <first> <last>. Non vedo l'ora di averla con me durante queste trattative.\"",
9: "\"Gli Avgi non sono uniti sotto la Consonanza?\"",
10: "\"Con chi state negoziando, esattamente?\"",
11: "Vibra in una risata. \"Si può solo sperare che la nostra specie sia così unita. No, l'adesione alla Consonanza è del tutto volontaria, e molte entità politiche hanno scelto di andare per conto proprio anche con la crisi in corso. Rincrescimento. L'evacuazione iniziale nel Tangled Shroud è stata quanto meno disordinata, visto che gran parte di quella regione era, ed è ancora, senza mappe. Molti capitani hanno portato le loro navi su rotte diverse, incontrandosi e formando alleanze solo per sopravvivere. In un certo senso è un miracolo che la Consonanza sia riuscita a ricostituirsi.\"",
12: "\"Le entità politiche non del tutto allineate alla Consonanza sono in gran parte indipendenti tra loro, ma il loro movimento è stato etichettato collettivamente come 'Dissonanza'. Imperativo. Capisca bene, non siamo nemici, né direi che proviamo rancore. La Dissonanza commercia con noi e di fatto rispetta i regolamenti approvati dall'Assemblea, e ognuno di loro vuole spazzare via gli Aberranti dal nostro spazio quanto tutti gli altri.\"",
13: "Ti guarda dritto. \"Le persone con cui negozieremo in questo viaggio sono ancora leali alla Consonanza, semplicemente scontente dei controlli sui prezzi di certi minerali. Necessari perché la Twilight Guard possa ampliare la flotta\", spiega.",
14: "Sora dice: \"Continuo a pensare che siano un branco di codardi. La vostra specie è minacciata e lasciate che siano altri a combattere? E poi vi lamentate del prezzo che possono pagare per il ferro? Che razza di persona lo fa?\"",
15: "Hriso agita le ali. \"Rimprovero. Il tipo che deve comunque mantenersi e pagare i macchinari di precisione che non può produrre da sé. Ma ne parleremo dopo. Per ora, partiamo il prima possibile.\"",
16: "Ho accettato di trasportare Hriso a una stazione mineraria della Dissonanza nel Tangled Shroud, mentre Darius e Sora seguono una pista che potrebbe aiutarmi a fuggire dal Twilight.",
17: "Fuga dal Twilight",
18: "Trova una via d'uscita dal Twilight. Conviene guardare all'estremo est, dove è cominciata l'Incursione.",
19: "Ti serve <capacity> sulla <ship> per trasportare Darius, Sora e Leon.",
20: "Ho sentito parlare di una possibile via d'uscita dal Twilight. A quanto pare gli Aberranti hanno invaso passando per una catena di sistemi che si estende a est, e benché nessuna nave Avgi sia riuscita a esplorare la zona dopo l'Incursione, Leon pensa che da lì possa esserci una via di ritorno allo spazio umano.",
21: "Minatori indipendenti, collettivi e corporazioni sono ugualmente scontenti dei controlli che la Consonanza ha imposto sui prezzi dei minerali estratti dagli asteroidi. La Consonanza sostiene che siano necessari per l'austerità dell'economia di guerra e per il bisogno di materie prime, ma i prezzi artificialmente bassi rendono difficile sopravvivere e guadagnarsi da vivere.",
22: "Leon era uno scienziato a bordo della nave di Darius quando rimase intrappolata nel Twilight. A differenza di Sora, incolpa senz'altro Darius dell'essere rimasto bloccato con gli Avgi. Un po' sgarbato, sembra però aver fatto diverse conoscenze preziose ed essere vicino a scoprire una via di ritorno allo spazio umano.",
23: "L'Avamposto Tekis è una grande stazione costruita dentro un asteroide largo diversi chilometri, con una rete di tubi e habitat che si incrociano sulla superficie. Porti la <ship> in un hangar angusto scavato nella roccia e scendi con Hriso, che si dirige subito verso un luogo d'incontro prestabilito. Noti che molti Avgi dell'avamposto fissano te, Darius e Sora: probabilmente è la loro prima volta che vedono un umano.",
24: "Entrate insieme in una grande sala conferenze rotonda, con le pareti di roccia levigata. Lì aspettano una manciata di Avgi di età diverse, che cominciano subito a parlare con Hriso nella loro lingua.",
25: "Uno di loro ti guarda e dice: \"Dispiacere. Quindi pensate che una dimostrazione di sostegno da parte degli alieni ci smuova? Avevamo capito che foste qui per riconsiderare le vostre posizioni, non per irrigidirle.\"",
26: "\"Di cosa stanno parlando?\"",
27: "(Resta in silenzio.)",
28: "\"Rimprovero. Il capitano <last> non è qui dalla 'mia' parte, né da nessun'altra: è solo un osservatore curioso dei nostri modi.\" Hriso si volta verso di te. \"Considerazione. Suppongo che si chieda di cosa stiamo parlando. La gilda mineraria locale dice che non può sostenere le proprie attività con il prezzo del ferro imposto dalla Consonanza, visto che non compriamo abbastanza metalli più rari come il titanio per compensare.\"",
29: "\"È una stupidaggine\", dice Sora. \"Senza acciaio a buon mercato non potremmo continuare a espandere Peripheria né costruire il Cilindro Aktina.\"",
30: "Hriso non traduce, e torna a conversare con i minatori. Sora tira fuori un traduttore tutto suo e ascolta con attenzione la conversazione, ma Darius ti prende in disparte. \"Ho parlato con un paio di persone mentre venivamo qui, e dicono che c'è qualcuno che sa di più sui primi giorni dopo l'Incursione. Andiamo.\"",
31: "\"Cosa ti hanno detto?\" chiedi.",
32: "\"A quanto pare è uno che dobbiamo incontrare di persona\", borbotta. \"Non mi piace, ma non credo sia niente di pericoloso. Solo scomodo.\" Ti congedi e vai con Darius.",
33: "In breve vi ritrovate in una specie di mensa, con dozzine di Avgi che sorseggiano bevande colorate. Darius si blocca quando nota un uomo basso seduto su uno sgabello grezzo, l'unico posto a sedere in stile umano della sala, insieme a qualche Avgi.",
34: "\"Darius. Non mi aspettavo di vederti qui\", dice. \"E cos'è questa storia, un altro umano nello spazio Avgi?\"",
35: "Darius ci mette un po' a rispondere. \"Leon. Ne è passato di tempo.\"",
36: "Leon sbuffa. \"A dir poco. Sora è con te, o sei strisciato fin qui da solo?\"",
37: "\"Sta aiutando in delle trattative.\"",
38: "(Lascia parlare Darius.)",
39: "\"È con uno della Consonanza, a negoziare con i minatori qui\", dice Darius.",
40: "\"E chi è questo?\" dice Leon guardandoti. \"Come sei finito qui, proprio qui?\"",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
