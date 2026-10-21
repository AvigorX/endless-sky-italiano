# -*- coding: utf-8 -*-
# part02: unita' 28-60 (Battle over Zydee + Gegno Suspicions).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
28: "Per quanto questo pianeta sia disabitato, ci sono più di qualche nave Gegno Scin parcheggiata sulla superficie. Sembra che sia in corso un'operazione per continuare a costruire le infrastrutture già edificate in passato, e gli Scin, instancabili, dedicano al tuo arrivo poca o nessuna attenzione.",
29: "Pochi momenti dopo, però, gli Scin cominciano all'improvviso a correre verso le loro navi. Per quanto ne sai, non ti sei avvicinato abbastanza da allarmarli. Cominciano a decollare uno dopo l'altro in fretta, ma non verso di te: i sensori della <ship> rilevano all'improvviso una grande flotta Gegno Vi che entra nel sistema. Pare che questo posto stia diventando un campo di battaglia, e finirci in mezzo è probabilmente da evitare.",
30: "Dopo le tue procedure post-attracco entri nel mondo ad anello e non puoi fare a meno di sentire che qualcosa non va. Di solito i Quarg qui camminano svelti, concentrati sui loro compiti, ma per qualche ragione intorno ce ne sono meno del solito. In più, quelli che incroci a volte parlano tra loro, e a volte guardano nella tua direzione anche solo per un istante. La cosa che salta più all'occhio è l'assoluta assenza di Gegno nella zona che stai visitando.",
31: "Qualche minuto dopo, mentre ti fai strada nell'interno immacolato dell'anello, senti una voce chiamarti da uno dei vari corridoi che si diramano. Voltandoti riconosci l'abbigliamento inconfondibile del Quarg che ti ha aiutato in passato, insieme a qualche altro. \"Di nuovo saluti casuali, <first> <last>. Potremmo avere un momento significativo della tua attenzione?\"",
32: "\"Certo.\"",
33: "\"Quanto ci vorrà?\"",
34: "\"Tanto quanto serve, perché questa faccenda ha un'importanza simbolica\", dice, con un tono leggermente più alto.",
35: "Segui il gruppo di Quarg in una sala più piccola, simile a quella che hai visitato prima. O forse ogni volta ne hai visitata una diversa, considerando quanto è incomprensibilmente grande un mondo ad anello. Quando ti siedi, il Quarg di prima ti guarda per un momento, guarda il tavolo, poi torna a guardare te.",
36: "\"In passato ti ho offerto suggerimenti di cauta interazione riguardo ai Gegno. Ci è stato segnalato un certo numero di ulteriori incontri che hai avuto, anche se sembrano di natura minima. In quei casi è stato riferito che te ne sei andato in tempo, cosa di cui siamo notevolmente grati. Tuttavia\", continua il Quarg, \"nonostante i tuoi sforzi nelle cautele raccomandate, alcune figure Gegno di rango significativo hanno espresso frustrazione per le tue apparizioni marginali. Ci hanno chiesto della possibilità di inutili recidive.\"",
37: "\"Perché li frustra?\"",
38: "\"Non ho fatto loro alcun male.\"",
39: "\"È stata più una coincidenza che altro.\"",
40: "\"Vorrei saperne di più su di loro.\"",
41: "\"Non serve invocare la violenza per fare molto male a un altro. Per quanto pure possano essere le intenzioni, anche la più piccola azione inconsapevole può rapidamente trasformarsi in una non prevista né desiderata.\" Il Quarg riflette per un momento.",
42: "\"Persino una mera coincidenza può causare un risultato non voluto né previsto da chi l'ha innescata. Tutte le cose viventi devono la propria esistenza a serie di coincidenze arbitrarie.\" Il Quarg riflette per un momento.",
43: "\"Non sempre il desiderio di sapere porta a occasioni piacevoli. Le creature più curiose possono facilmente farsi male quando sono ignare della natura dei propri interessi.\" Il Quarg riflette per un momento.",
44: "\"Immagina, se vuoi, che durante i conflitti sostanziali che gli umani chiamano Turf Wars, uno strano alieno giungesse nello spazio umano. Noi Quarg assistemmo con dolore a quel conflitto pericoloso: fu un tempo di grande spreco, di pericolo funesto e di sgradevole diffidenza tra l'umanità. I Gegno sono in uno stato di vulnerabilità notevolmente paragonabile a quel tempo, e l'introduzione di estranei non si addirebbe al caso. La verità è che alcuni Gegno di riguardo ci hanno contattato in merito alle tue passate presenze, e c'è stata una manifestazione di preoccupazione per le tue intenzioni non dichiarate.\" Dopo una breve pausa il Quarg ti guarda in modo strano, e non sai cosa pensare. \"Tuttavia, inaspettatamente, in alcune rare occasioni ci è stato chiesto con curiosità delle tue origini, un'esperienza che non ci è molto familiare con i Gegno.\"",
45: "Il Quarg lascia la sedia e ti fa cenno di fare lo stesso.",
46: "(Alzati.)",
47: "\"La nostra migliore raccomandazione è di evitare ulteriori contatti nel prossimo futuro. Intanto tenteremo una negoziazione molto attenta con la loro gerarchia per trovare i termini di una base di accettazione della tua presenza. Se troveremo un'intesa, riceverai comunicazione da uno con il titolo di 'Adrauni', come è stato conferito a me.\"",
48: "Il resto dei Quarg, che hanno ascoltato la conversazione con attenzione per tutto il tempo, comincia a scortarti fuori dalla stanza. Se i Gegno sono disposti ad arrivare a contattare i Quarg per le tue apparizioni, allora è davvero una faccenda importante per loro. Per il momento è probabilmente meglio lasciare che i Quarg trovino una qualche soluzione con i Gegno mentre tu te ne stai a distanza.",
49: "negative rep",
50: "\"In passato ti ho offerto suggerimenti di cauta interazione riguardo ai Gegno. Tuttavia siamo sempre più consapevoli di avvenimenti correlati a loro che ti riguardano. Pare che eventi conseguenti si siano davvero verificati. Non spesso in passato fummo avvicinati dai Gegno, ma in alcune notevoli occasioni figure di rilievo ci hanno cercato per informarsi, soprattutto a causa di circostanze violente.\" Il Quarg ti fissa a lungo, aspettando una qualche risposta.",
51: "\"Mi hanno attaccato loro per primi.\"",
52: "\"Volevo attirare la loro attenzione.\"",
53: "\"La violenza accade continuamente nello spazio umano, ma i Quarg non sembrano interessati.\"",
54: "Il Quarg continua a guardarti per un po' prima di rispondere. \"In base ad alcuni principi, posso vedere ragioni perché essi siano... inclini... a farlo. Tuttavia farlo in questo caso non si allineerebbe agli interessi dei loro anziani, né lo farebbe alcuna fabbricazione.\" Il Quarg sbatte le palpebre, poi riflette per un momento.",
55: "Il Quarg sbatte le palpebre. \"E hai trovato una soluzione adeguata al tuo... problema... scatenando ostilità non provocate?\" Poi continua a fissarti in quella che supponi essere un'aria giudicante per un tempo imbarazzante, prima di distogliere lo sguardo per riflettere tra sé.",
56: "Il Quarg prende un lungo momento per riflettere sulla tua affermazione, come se non si aspettasse una risposta simile. \"Certo, è noto che il conflitto sia comunemente naturale tra voi litigiosi umani. Ma questa faccenda è di altro genere.\" Poi pensa di nuovo tra sé per un po'.",
57: "\"Immagina, se vuoi, che durante i conflitti sostanziali che gli umani chiamano Turf Wars, un alieno ostile giungesse nello spazio umano. Noi Quarg assistemmo con dolore a quel conflitto pericoloso: fu un tempo di grande spreco, di pericolo funesto e di sgradevole diffidenza tra l'umanità. I Gegno sono in uno stato di vulnerabilità notevolmente paragonabile a quel tempo, e l'introduzione di ancor più ostilità non si addirebbe al caso, soprattutto da parte di estranei. Siamo stati contattati da numerosi Gegno di alto rango e desideriamo che questa resti una faccenda di sole cautele più severe, ma purtroppo i Gegno la ritengono una questione che va oltre l'attenzione.\" Il Quarg lascia la sedia e ti fa cenno di fare lo stesso.",
58: "(Alzati.)",
59: "\"Ti si raccomanda di lasciare lo spazio Gegno da questo momento decisivo. Intanto tenteremo una negoziazione molto attenta con la loro gerarchia per arrivare ai termini di una tolleranza accettabile. Se troveremo un'intesa, riceverai comunicazione da uno con il titolo di 'Adrauni', come è stato conferito a me.\"",
60: "Mentre il resto dei Quarg ti scorta fuori dalla stanza, il Quarg di nome 'Adrauni' ti si rivolge un'ultima volta. \"Eviti qualsiasi ulteriore tendenza violenta, capitano.\" Se i Gegno sono disposti ad arrivare a contattare i Quarg, allora è davvero una faccenda importante per loro. Per il momento è probabilmente meglio ascoltare gli avvertimenti dei Quarg, questa volta, e lasciare lo spazio Gegno finché non si trovi una soluzione, sempre che ci sia.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
