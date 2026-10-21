# -*- coding: utf-8 -*-
# part02: unita' 41-76 (resto di `Twilight Escape 1`).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
41: "\"Il capitano <last>. Sono rimasto bloccato qui, proprio come voi.\"",
42: "\"<first>. Piacere di conoscerti.\"",
43: "Spieghi in fretta come sei finito nello spazio Avgi, e Leon annuisce. \"Questo spiega le domande che faceva il buon capitano\", dice, indicando Darius con un cenno. \"Ho passato anni a raccogliere queste informazioni, dalla versione ufficiale ai pettegolezzi raccolti negli angoli più remoti dello spazio Avgi.\"",
44: "Si sporge in avanti. \"Allora, prima di dirtelo, una condizione. Ho passato mesi a cercare una nave che mi portasse a... beh, vedrai. Ma non molti capitani sono disposti a portare le loro navi fuori dal Tangled Shroud e attraverso il blocco degli Aberranti, quindi se questo porta da qualche parte, voglio una cuccetta sulla tua nave.\"",
45: "\"Affare fatto.\"",
46: "\"Niente affare.\"",
47: "Apri la bocca per rispondere, ma Darius ti precede. \"Certo, Leon.\"",
48: "\"Bene. Il succo è più o meno questo: l'Incursione non è venuta dal nulla. Tutti dicono che sono arrivati da oltre i limiti estremi dell'esplorazione Avgi, ma non è del tutto vero. I primi a incontrarli sono stati una nave esploratrice, abbattuta in pochi minuti dalle loro armi. Ma non prima di aver inviato una sola trasmissione confusa alla nave gemella, che è fuggita indietro verso il resto degli Avgi.\"",
49: "Fa una pausa e beve quello che sembra acqua. \"Dicevano di aver trovato una specie di varco, un antico manufatto alieno costruito da una specie Antecessors sconosciuta. In qualche modo l'avevano attivato, ed è da lì che sono arrivati i primi Aberranti.\"",
50: "\"E vorresti usare questo varco come via d'uscita?\"",
51: "\"Dove pensi che porti questo varco?\"",
52: "\"Non so dove porti, ma sarà un posto diverso dallo spazio Avgi. Magari un posto dove il tuo motore di salto funziona, e allora potremmo alla fine tornare nello spazio umano. In ogni caso è meglio che stare qui a girarci i pollici per altri sei anni.\"",
53: "\"Dov'è questo varco?\" chiede Darius.",
54: "\"Gli Aberranti sono arrivati da est, oltre i limiti estremi del Twilight. Un luogo che gli Avgi hanno sempre fatto fatica a esplorare, per via di strane tempeste energetiche che periodicamente ionizzano interi sistemi. Ma a quanto pare si riconosce da una nebulosa rossa che lo pervade, così come il Twilight è circondato da un ammasso di nebulose blu.\"",
55: "\"Ho sentito parlare di quella zona. Si chiama Ember Waste.\"",
56: "\"Può riportarci nello spazio umano?\" chiede Leon, e tu annuisci.",
57: "unknown ember waste",
58: "\"Allora non ha senso aspettare. Se c'è una possibilità, anche piccola, vale la pena verificarla\", dice Darius, speranzoso per la prima volta da quando lo conosci.",
59: "Speri solo che la sua speranza non sia falsa, per il bene di entrambi.",
60: "Mentre le fiamme viola del motore di salto svaniscono, Darius, Sora e Leon restano senza parole. Per la prima volta in sei anni sono tornati nello spazio umano.",
61: "\"Eh, te l'avevo detto che ce l'avremmo fatta.\"",
62: "\"Siamo fuori. E ora dove andiamo?\"",
63: "Leon fissa il vuoto per un momento, poi impreca. \"Quel dannato magnetar era lì tutto il tempo? Sono stato lì per anni. Anni!\"",
64: "\"Ci siamo stati tutti. E non avresti potuto farci nulla senza il motore di salto di <first>\", gli ricorda Sora.",
65: "\"<first>\", dice Darius con la voce tremante. \"Portaci alla Deep, per favore. Devo vedere casa mia. E mia moglie.\"",
66: "\"Prima lasciami su Vinci\", interviene Leon. \"Devo rimettere in ordine la mia vita, e lì c'è qualcuno con cui devo parlare di tutta questa storia. Tanto è sulla strada per la Deep.\"",
67: "Sono riuscito a fuggire dal Twilight insieme agli umani che vi erano bloccati.",
68: "Leon è estremamente grato per averlo aiutato a tornare nello spazio umano. Vuole parlare degli Avgi con un contatto su Vinci e chiede di restare in contatto.",
69: "Il gruppo è silenzioso mentre posi la <ship> sulla piazzola. Noti Sora che guarda fuori dalla finestra mentre Darius si fissa le mani. Quanto a Leon, era pronto a scendere già prima che entraste in atmosfera, e cammina avanti e indietro vicino al portello finché non lo apri.",
70: "\"Vado a prendere una boccata d'aria\", dice Sora, comparendo all'improvviso davanti a un Leon indignato e trascinandosi dietro un Darius riluttante. \"Saremo allo spazioporto, quindi cerca di non partire senza di noi.\"",
71: "Leon, rassegnato a uscire per ultimo, si ferma appena prima di lasciare la <ship> e si volta verso di te. \"<first>. Grazie.\" È insolitamente serio: per un momento la sua solita aria di disprezzo per il mondo non c'è.",
72: "\"Non c'è di che.\"",
73: "\"Sono contento di aver potuto aiutare.\"",
74: "\"No, davvero. Mi aspettavo di morire laggiù, con quegli Avgi. Sei anni... non so come ringraziarti, ma se mai ti trovi in zona e hai bisogno di qualcosa, non esitare a chiamarmi.\" Detto questo ti stringe la mano e si avvia nella direzione presa da Sora e Darius, verso lo spazioporto di Vinci.",
75: "Ricordati di incontrare Darius e Sora allo spazioporto prima di lasciare Vinci.",
76: "Atterri su <planet>, ma ti accorgi che la scorta con Darius, Sora e Leon non è ancora entrata nel sistema. Meglio ripartire e aspettare che arrivi.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
