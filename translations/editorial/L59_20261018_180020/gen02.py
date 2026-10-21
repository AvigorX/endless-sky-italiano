# -*- coding: utf-8 -*-
# part02: unita' 12-23 (Syndicated Security Troops, Class Trip, Old Defense Turrets, Blind Landing).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
12: "Il rombo basso dei \"Tonner\", i camion pesanti per spostare truppe e rifornimenti, che scendono lungo la strada, fa voltare le teste verso i veicoli massicci ma imponenti che rallentano fino a fermarsi. Il conducente e il comandante del veicolo di testa tengono gli occhi sulla strada, attenti a qualsiasi pericolo del traffico che possa minacciare il veicolo o la loro scorta.",
13: "Le truppe nel retro di ogni tonner, invece, fanno conversazione, con il camuffamento sul viso che si scioglie per il caldo. Uno di loro ti indica, dicendo qualcosa che gli guadagna un gemito dei compagni, e decidi che probabilmente non vuoi sapere cosa ha detto.",
14: "Un gruppo di bambini ti saluta con la mano mentre scendi dalla nave, meravigliati dal veicolo spaziale in mostra mentre le loro insegnanti cercano senza successo di tenere la loro attenzione. Da lontano vedi sbiadire i colori delle loro divise mentre il gruppo passa, e nessuno di loro sembra minimamente scontento. Mentre ti avvii verso lo spazioporto, ti chiedi quanti di loro finiranno per avere una nave propria e volare tra le stelle.",
15: "Una sosta fastidiosamente lunga ti ha spinto a esplorare un po', così noleggi un'auto per un breve giro nei dintorni. Più tardi, mentre infili l'auto nel parcheggio designato per la riconsegna, il rumore inatteso di grandi motori idraulici attira la tua attenzione. Guardi una torretta enorme sollevarsi da dietro una barricata vicina e voltarsi verso il cielo, con il suo unico cannone pronto a sparare contro apparentemente nulla.",
16: "Cercando in giro una qualche spiegazione, trovi una targa sistemata lì vicino in modo comodo che dedica la torretta, e altre cinque come lei, offrendo protezione e scoraggiando la pirateria fino ad anni relativamente recenti. Non puoi fare a meno di chiederti come se la caverebbero le torrette se venissero davvero usate di nuovo.",
17: "Lo smog riempie il parabrezza mentre scendi, cercando senza successo di vedere qualcosa oltre a pochi metri davanti a te. I sistemi di pilota automatico però mostrano verde pieno su tutta la gamma di indicatori, e il controllo del traffico ha confermato l'aggancio.",
18: "(Atterra con il pilota automatico.)",
19: "(Torna in orbita.)",
20: "Lasci che il mezzo esegua l'atterraggio, fissando la foschia senza vederci nulla finché non si dirada.",
21: "A terra ne vedi la causa: campi e campi di piantagioni in fiamme. Vedi una folla in gran parte di agricoltori che blocca un gruppo più piccolo di vigili del fuoco, discutendo e cercando di impedire loro di spegnere le fiamme, mentre gli aerei passano sopra scaricando acqua e ritardanti dove serve.",
22: "Ricordi di aver visto qualcosa del genere anni fa: agricoltori che bruciavano i raccolti per rendere fertile la terra, e quanto fosse cattiva l'aria per mesi.",
23: "Non volendo fidarti di un atterraggio alla cieca in una situazione sconosciuta, torni in orbita e rientri nella coda di smistamento dello spazioporto. Un giorno di ritardo è un prezzo che vale la certezza.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
