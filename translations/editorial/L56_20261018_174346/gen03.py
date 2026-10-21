# -*- coding: utf-8 -*-
# part03: unita' 61-102 (Return to Giaru Gegno + inizio di Gegno Anticipation).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
61: "Il Quarg noto come Adrauni ti ha convocato di nuovo su <destination>.",
62: "C'è un messaggio in arrivo sul tuo dispositivo di comunicazione. \"Saluti, umano <first> <last>. Questo messaggio viene dal Quarg di nome Adrauni. Torna su <planet> alla prima occasione che ti è data.\"",
63: "Convocazione dei Gegno",
64: "Presentati ai Gegno su <destination> entro i prossimi 8 giorni, dove scoprirai se hai un futuro con loro.",
65: "Appena atterri sul mondo ad anello, ti accoglie un piccolo gruppo di Quarg che ti fa subito cenno di seguirli. Ti scortano attraverso varie sale dell'anello, che sembrano ancora prive di qualsiasi Gegno. In fondo al corridoio successivo vedi Adrauni che ti aspetta, e accanto a lui un Gegno con un abbigliamento di forma strana. Quando li raggiungi, gli altri Quarg si dirigono altrove e Adrauni comincia a camminare lungo un altro corridoio. \"Ti prego, concediti di accompagnarci.\"",
66: "Mentre li segui, Adrauni comincia a parlare tendendo un braccio. \"Se puoi, come dicono gli umani, assecondami: cosa sospetti sia stato il risultato delle mie negoziazioni con i Gegno?\"",
67: "\"Che mi accetteranno?\"",
68: "\"Che non vogliono avere niente a che fare con me?\"",
69: "\"Non lo so.\"",
70: "Dopo una breve pausa Adrauni si volta verso il Gegno, mormora qualcosa nella loro lingua, poi ti risponde. \"Capisco. E quale proponi che sia la ragione?\"",
71: "\"Li ho aiutati prima, e potrei aiutarli ora.\"",
72: "\"Pensavo che avreste potuto convincerli.\"",
73: "\"Non lo so.\"",
74: "Adrauni riflette per qualche momento mentre continuate a camminare nell'interno impeccabile del mondo ad anello. \"È una risposta piuttosto umana. Tuttavia non confondere il tuo valore nell'assistenza con il loro. Anche se fornissi ai Gegno un aiuto benefico, una risposta benevola in cambio non è necessaria. A questo punto hai dato ascolto ai miei avvertimenti, eppure stai semplicemente facendo ciò che i Gegno desideravano dall'inizio: lasciarli stare.\"",
75: "\"Forse è meglio che li lasci stare.\"",
76: "\"Deve esserci qualcosa che posso fare.\"",
77: "convince",
78: "Adrauni ti lancia un'occhiataccia continuando attraverso il mondo ad anello. \"Non ricordi la mia precedente menzione che noi Quarg abbiamo tentato simili persuasioni? Non è in nostra capacità convincere i Gegno di nulla. Sono molto devoti ai propri, e supererebbero ogni confine per opporsi a un consiglio, anche da noi Quarg.\"",
79: "\"Forse è meglio che li lasci stare.\"",
80: "\"Deve esserci qualcosa che posso fare.\"",
81: "deny me",
82: "Dopo una breve pausa Adrauni si volta verso il Gegno, mormora qualcosa nella loro lingua, poi ti risponde. \"Capisco. E quale proponi che sia la ragione?\"",
83: "\"Per come si comportano con me.\"",
84: "\"Da quello che mi hai detto prima.\"",
85: "\"Non lo so.\"",
86: "\"Certo, i Gegno sono diffidenti verso di te, che manchi di cautela.\" Passano alcuni secondi, e Adrauni lancia uno sguardo strano verso il Gegno. Non sai cosa stia pensando. Il Gegno sembra fare una domanda nella loro lingua, ma non riceve risposta. Adrauni tace ancora per un po' prima di parlare di nuovo. \"Nonostante questo, ti sei trovato in situazioni precarie in cui noi non siamo stati. Noi come specie abbiamo abbracciato il contatto con i Gegno; tu, però, resti l'unico umano qui. Forse è lì che sta un'implicazione notevole di distinzione.\"",
87: "\"Stai dicendo che c'è qualcosa che posso fare?\"",
88: "\"Non sono sicuro di capire.\"",
89: "before",
90: "\"Capisco.\" Adrauni sbatte le palpebre lentamente fissandoti. È quasi come se fosse sorpreso, o almeno non si aspettasse quella risposta. \"È saggio che tu segua la mia fortunata istruzione. Se non fosse così, forse non sarei io a parlare con te in questo momento. O forse non ci sarebbe nessuno.\" Poi guarda di nuovo avanti mentre continuate la passeggiata, lasciandoti a pensare a quelle parole. \"Purtroppo i Quarg non sono in grado di aiutarti ulteriormente in questa delicata faccenda. Se ricordi, abbiamo tentato un precedente consiglio con i Gegno, ma sono legati ai loro modi, anche se questo significa opporsi incredibilmente a noi Quarg.\"",
91: "\"Forse è meglio che li lasci stare.\"",
92: "\"Deve esserci qualcosa che posso fare.\"",
93: "unsure",
94: "Adrauni si volta brevemente verso di te, ti fissa senza espressione, poi si rivolge al Gegno e mormora qualcosa nella loro lingua prima di risponderti. \"E perché mai sei incerto?\"",
95: "\"Non ero sicuro che avreste potuto convincerli.\"",
96: "\"Non so niente di loro.\"",
97: "Dopo una pausa Adrauni si volta verso di te, ti lancia un'occhiataccia e poi guarda di nuovo avanti mentre proseguite tutti e tre attraverso l'anello. \"Una conclusione piuttosto importante, non è vero? Molte volte l'ho detto: i Gegno non sono ciò di cui considererei gli umani possedere conoscenza. Se tu ne sapessi di più, temo che anche allora i Gegno non desidererebbero, come si dice in umano, la camerateria?\" Il Gegno fa allora una domanda nella loro lingua, e Adrauni avvia con lui una conversazione piuttosto lunga.",
98: "\"Forse è meglio che li lasci stare.\"",
99: "\"Deve esserci qualcosa che posso fare.\"",
100: "interest",
101: "Il Quarg si volta di nuovo verso di te. \"Sei qui non per capriccio della tua specie fanatica, ma per tua richiesta. Le azioni che compi possono essere di un umano, ma non sono volute dall'umanità.\" Sbattendo le palpebre lentamente, Adrauni si volta verso il Gegno che cammina al suo fianco e avvia con lui una conversazione piuttosto lunga.",
102: "understand",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part03.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part03:', len(P), 'unita', min(P), '-', max(P))
