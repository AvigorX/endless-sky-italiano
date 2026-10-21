# -*- coding: utf-8 -*-
# part02: unita' 17-32 (New Holland Foibles, Trash Fire Crops).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
17: "L'odore di metallo bruciato riempie l'aria mentre percorri le strade poco affollate della città-fabbrica vicino allo spazioporto, tenendoti lontano dalla via di rifornimento principale che alimenta direttamente il porto e i suoi hangar.",
18: "Nonostante la distanza e l'assenza di traffico, però, non è affatto silenzioso. Diversi edifici industriali producono un ronzio distinguibile, e mentre indaghi senti l'eco delle molatrici nel silenzio. Girato l'angolo, trovi un vicolo che corre lungo una lunga recinzione a maglie metalliche. Oltre, vedi una folla di uomini che tagliano una nave spaziale. Pezzi cadono regolarmente a terra, e gli operai sembrano incuranti di chi sta sotto.",
19: "Anche mentre guardi, vedi una lastra di scafo oscillare pericolosamente sopra la testa di un operaio.",
20: "(Grida un avvertimento.)",
21: "(Lasciali stare.)",
22: "Gridi un avvertimento e la maggior parte degli uomini si ferma a guardarti; la lastra oscilla piano mentre chi tiene la mola incriminata socchiude gli occhi verso di te. Uno degli uomini più anziani, che ora capisci sovrintendeva almeno in parte l'attività, fa un passo avanti e ti fa un gesto con le mani come per scacciarti. \"Ehi tu, levati di torno. Abbiamo il nostro addetto alla sicurezza, non ci serve il tuo naso nei nostri affari.\"",
23: "(Contesta l'affermazione.)",
24: "(Lasciali stare.)",
25: "Fai notare che quello che vedevi non sembrava affatto sicuro, controllo o no, e l'uomo si guarda intorno un istante prima di avvicinarsi stizzito e fermarsi di fronte a te, dietro la recinzione. \"Senti, straniero\", dice, \"qui il lavoro è difficile da trovare. Quelli che lavorano qui non hanno tempo da perdere. Ma la paga è buona e almeno possiamo sfamare i nostri figli. Certo, qualcuno si fa qualche graffio e qualche livido, ma nessuno è morto sotto la mia sorveglianza, e Rik ha perso solo il dito più piccolo. Se ti va di guardare, va bene, resta lì in giro, ma lasciaci in pace, ok? Tanto qui non c'è nessuno a cui importi quello che hai da dire.\"",
26: "Ti guarda dritto negli occhi, e quando è sicuro che tu abbia capito il messaggio torna a passi pesanti dalla sua squadra, che riprende il lavoro. Li guardi smontare la nave morta finché i pezzi riempiono completamente il rimorchio che hanno con sé, poi si portano via le parti verso una fabbrica in lontananza.",
27: "Ti volti e te ne vai. Un momento dopo senti un fragore e un grido, ma quando ti volti indietro nessuno sembra essersi fatto male.",
28: "Mentre ti muovi per lo spazioporto non puoi evitare il terribile odore. È come un rogo di rifiuti, ma non vedi nessun tipo di fumo.",
29: "(Ignoralo.)",
30: "(Chiedi in giro.)",
31: "Chiedi a uno dei locali che non sembra troppo occupato. Ti informa con tristezza che c'è stato un raccolto eccezionale di banane, ma sfortunatamente altri mondi più ricchi hanno avuto un raccolto eccezionale nello stesso periodo, e non c'è posto dove vendere o conservare un surplus così grande. Gli agricoltori in difficoltà bruciano la frutta in eccesso per fare fertilizzante per la stagione successiva, e il vento ha portato l'odore per tutta la città.",
32: "Lasci l'odore misterioso ai locali e torni alle tue faccende.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
