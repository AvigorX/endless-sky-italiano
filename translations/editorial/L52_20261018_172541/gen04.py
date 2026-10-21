# -*- coding: utf-8 -*-
# part04: unita' 110-135 (chiude `Twilight Escape 3` e il file, riga 1120).
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
110: "Atterri nello spazioporto principale di Valhalla, e Darius praticamente salta fuori dalla nave prima ancora che tocchi terra. Una rapida chiamata a un taxi automatico e vi ritrovate davanti a un vasto complesso residenziale dall'aria elegante. \"Il nostro vecchio indirizzo\", spiega. \"Eravamo ancora in affitto, ma pensavamo di comprare l'appartamento entro qualche anno.\"",
111: "Bussi alla porta dell'appartamento giusto, ma ad aprire è un uomo alto dai capelli neri. \"Salve, posso aiutarla?\" chiede con cautela.",
112: "Darius sembra distrutto. \"C'è... c'è una Katrina, qui?\"",
113: "\"Katrina? Non posso dire di aver conosciuto qualcuno con quel nome nei cinque anni che vivo qui. È un'amica sua?\"",
114: "Darius si volta con aria tetra. \"Sì. Mi scusi il disturbo, ce ne andiamo.\"",
115: "\"Non arrenderti. Probabilmente si è solo trasferita, o roba simile.\"",
116: "\"Potremmo provare a cercare le sue informazioni.\"",
117: "\"Certo che l'ha fatto. Ma non capisco perché, comprare quell'appartamento era il nostro sogno. Non ha alcun senso!\" Si ferma. \"Scusa, <first>. Sono solo nervoso.\" Sospira prima di continuare. \"Posso provare a cercarla, forse...\" si interrompe, pensieroso.",
118: "\"Ci sono registri pubblici su Valhalla?\" chiedi.",
119: "\"...Sì, proveremo con i registri. Possiamo consultarli in biblioteca.\"",
120: "Dopo un breve tragitto fino alla biblioteca, ti siedi a un tavolo mentre Darius consulta i registri pubblici. Scorre l'elenco di nomi e indirizzi e si ferma su un nome. \"Katrina... Caldwell. Il nostro cognome.\" La speranza gli si legge in faccia. \"Almeno ha tenuto il nostro cognome.\"",
121: "Dai un'occhiata all'indirizzo e lo annoti. Sembra essere più fuori città. \"Proviamo quell'indirizzo. Possiamo arrivarci entro stasera\", dici.",
122: "L'indirizzo risulta essere in campagna, e ammiri il paesaggio mentre il taxi scivola liscio lungo le strade. A differenza di Memory, qui il paesaggio è verde e rigoglioso, con colline dolci, foreste fitte e torrenti impetuosi. Scopri che l'indirizzo corrisponde a una casa accogliente sul fiume, con un grande giardino visibile accanto.",
123: "Darius non è mai stato così nervoso in vita sua, ma gli dai una spinta gentile verso la porta. Alla sua bussata non risponde nessuno, e il suo viso ricomincia a scivolare nella disperazione, ma senti una voce dal giardino.",
124: "\"Darius? Sei tu?\" Una donna dai capelli grigi esce sul portico, con gli occhi lucidi. \"Sei tornato... sapevo che eri vivo!\" esclama, correndo ad abbracciarlo. I due cominciano a parlare a una velocità che non riesci a seguire, mentre tu resti indietro un po' impacciato.",
125: "Dopo qualche minuto provi a congedarti, ma Darius non vuole. \"No, no, devo tutto a te, <first>. Sei l'unico motivo per cui sono qui.\"",
126: "Katrina ti guarda incuriosita. \"Alieni, eh? Non hai l'aria di un alieno.\"",
127: "\"Come?\"",
128: "\"È perché non lo sono.\"",
129: "\"Sì, queste tute di pelle sono fatte proprio bene.\"",
130: "Scoppia a ridere. \"Non ci crederei se me lo avesse detto chiunque altro. Insomma, gli uomini inventano ogni scusa per tornare a casa tardi, ma questa è un'altra cosa!\" Il tono diventa all'improvviso serio. \"Sarà un grattacapo sistemare tutto con il governo. Mi hanno dato i soldi per questa casa come risarcimento per la tua presunta 'morte', per quanto io abbia insistito che eri ancora vivo.\"",
131: "\"Lo sistemeremo. Tanto mi devono gli arretrati\", scherza Darius, ancora tra le braccia di Katrina.",
132: "Mentre i due si avviano alla porta, vi salutate, e Darius promette che ti terrà aggiornato sugli Avgi. Nessuno dei due ha dimenticato gli alieni che lottano per sopravvivere ai margini della galassia, e ora che conosci una via sicura per entrare e uscire dal loro spazio, puoi tornarci senza il timore di restare intrappolato.",
133: "Atterri su <planet>, ma ti accorgi che la scorta con Darius non è ancora entrata nel sistema. Meglio ripartire e aspettare che arrivi.",
134: "Ho scoperto un magnetar nel sistema Decet che può aumentare la portata del mio motore di salto, in quella che sembra l'inversione dell'effetto misterioso che mi aveva intrappolato qui.",
135: "Proprio come il motore di salto aveva reagito in modo strano al primo ingresso nello spazio Avgi, succede di nuovo, ma questa volta l'effetto è invertito. Il plasma del salto indugia in modo innaturale, come se fosse stato caricato da qualcosa di esterno. Gli strumenti indicano che il motore di salto è molto più caldo di quanto dovrebbe essere subito dopo un salto, quasi da diventare pericoloso. Forse anche la portata del motore di salto è cambiata?",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part04.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part04:', len(P), 'unita', min(P), '-', max(P))
