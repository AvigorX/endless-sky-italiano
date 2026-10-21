# -*- coding: utf-8 -*-
# part04: unita' 103-140 (Gegno Anticipation, ramo "epilogo a").
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
103: "Camminate in silenzio per un periodo imbarazzante. La strana architettura del mondo ad anello ti rassicura poco; hai la sensazione di aver già percorso lo stesso tratto diverse volte. Qualche momento dopo cominci a seguire Adrauni e il Gegno in quella che sembra una sezione diversa, anche se stranamente più ampia delle precedenti. Prima che tu possa fare altre domande, Adrauni risponde finalmente. \"È evidente che tu possa comprendere qualcosa della tua fragile situazione. Non è più ciò che io, anzi, i Quarg, possono fare per te. È ciò che tu puoi fare per te stesso.\"",
104: "better",
105: "Adrauni parla ancora a lungo con il Gegno. La strana architettura del mondo ad anello ti rassicura poco; hai la sensazione di aver già percorso lo stesso tratto diverse volte. Qualche momento dopo cominci a seguire Adrauni e il Gegno in quella che sembra una sezione diversa, anche se stranamente più ampia delle precedenti. \"Sì, può essere che la tua partenza tempestiva sia l'esito più favorevole in questa faccenda.\" Segue un lungo silenzio imbarazzante, alla fine del quale Adrauni si ferma brevemente, sempre rivolto avanti, incrociando le braccia dietro la schiena. \"Anche se tu ed io immaginiamo che sia... improbabile.\"",
106: "visit a",
107: "Il Gegno vi lascia all'ingresso di un corridoio separato, e tu segui Adrauni fino a un'ultima tappa. Sei alla fine del tuo lungo viaggio attraverso il mondo ad anello e ti ritrovi dove hai cominciato: la struttura di attracco dove è posata la tua nave. Anche se seguire Adrauni fin qui è sembrato un labirinto vertiginoso, non puoi fare a meno di immaginare quanto sarebbe più confuso esplorare un intero mondo ad anello, considerando che questo era solo qualche minuto. Adrauni si ferma e si volta verso di te, abbassandosi un poco per parlarti all'altezza dei tuoi occhi. \"Devi cercare udienza per conto tuo, tenace. Visita il mondo natale dei Gegno, Dueyu Eitch, e presentati nel modo in cui desideri essere percepito. Solo allora troverai la risposta che cerchi.\"",
108: "epilogue a",
109: "\"Non mi impediranno di atterrare?\"",
110: "\"Non potevamo semplicemente chiedere al Gegno di prima?\"",
111: "\"Non sono sicuro che sia sicuro. Potresti scortarmi?\"",
112: "\"Grazie. Parto ora.\"",
113: "\"Al contrario, credo piuttosto che ti stiano aspettando. Ricorda che devi contattare il pianeta per l'autorizzazione.\"",
114: "ask",
115: "Adrauni riflette sulla tua domanda per qualche momento prima di rispondere. \"Ah, sì, la tua ingenuità verso la cultura Gegno mi era sfuggita solo per un attimo. La tradizione tra le femmine Scin è di dedicare al tempo di ricerca poco meno di una vita. Quella di cui parli è molto devota a noi qui, nient'altro. Perché qualsiasi questione ufficiale con i Gegno passi, deve attraversare il grande cuore della colonia.\"",
116: "escort",
117: "Adrauni sbatte le palpebre. \"Avrei sperato che tu avessi capito cosa significava la tua precedente consapevolezza.\" Guarda di lato, immerso nei pensieri, poi torna a te. \"Di norma noi Quarg visitiamo i Gegno raramente, e solo per motivi di poco conto. Se fossi accompagnato in questo momento, la percezione instabile che i Gegno hanno di te cambierebbe ancora. Immagina se i Quarg visitassero il vostro pianeta, chiamato Terra, con strani altri al seguito.\" Immagini che Adrauni faccia quello che per un Quarg sarebbe un sospiro. \"Tuttavia, sì, sono in grado di mandarti una scorta. Sii certo di questa decisione.\"",
118: "\"Sì, vorrei una scorta.\"",
119: "\"In realtà dovrei cavarmela da solo.\"",
120: "quarg escort",
121: "Adrauni risponde con esitazione. \"Ne farò richiesta alla tua partenza.\"",
122: "no escort",
123: "\"Capisco. Che sia per il meglio, allora.\"",
124: "end a",
125: "\"Buon viaggio, <first> <last>. Aspiro a che le tue audaci decisioni si addicano ai saggi nel cammino che ti attende.\" Adrauni ti fa un lungo inchino, poi lascia l'hangar. Hai la sensazione che questa possa essere stata l'ultima volta che lo incontri. Mentre torni alla nave, alcuni altri Quarg, che hanno osservato la conversazione da lontano, tornano alla loro routine come se nulla fosse. Ora tocca a te scoprire se i Gegno ti accetteranno.",
126: "negative rep",
127: "Appena atterri sul mondo ad anello, noti un gruppo di Gegno ai margini dell'hangar in cui sei posato. Hanno l'aspetto massiccio dei guerrieri Vi e, pur restando fermi, ti osservano intensamente mentre scendi dalla nave. Un piccolo gruppo di Quarg ti si avvicina e ti fa subito cenno di seguirli, scortandoti attraverso varie sale dell'anello. Alla fine sei condotto nella stanza dove hai incontrato Adrauni in passato, o forse in una identica. \"Ti prego, siediti.\"",
128: "Ti siedi, insieme ad altri due Quarg, e gli altri lasciano la stanza con la porta che si chiude alle loro spalle. Adrauni ti fissa senza espressione per un po', poi parla. \"Presumo tu comprenda quale risultato sia venuto dalle mie negoziazioni con i tediosi Gegno.\"",
129: "\"Che sono arrabbiati con me?\"",
130: "\"Che mi tollereranno?\"",
131: "\"No, non lo capisco.\"",
132: "Adrauni continua a fissarti, poi sbatte le palpebre lentamente. \"Capisco. Qual è la tua strana interpretazione del termine 'tollerare' in questo contesto?\"",
133: "\"Il permesso di atterrare sui loro mondi.\"",
134: "\"Concedermi accesso alla loro tecnologia.\"",
135: "\"Non lo so.\"",
136: "Adrauni riflette per qualche momento. \"È una risposta piuttosto umana. Per quanto noi Quarg siamo, secondo la tua definizione, minimamente tolleranti verso la tua specie, vi diamo accesso solo ad alcuni dei nostri mondi meravigliosi. Ma che dire degli umani verso gli altri? Se i Gegno, o specie di altre eccentricità, avessero libertà di accesso al vostro pianeta Terra? Con te forse sarebbe così, ma con l'umanità ansiosa certamente no.\" Uno degli altri Quarg nella stanza dice qualcosa ad Adrauni, che risponde con una conversazione nella propria lingua.",
137: "\"Non c'è modo che io possa lavorare con i Gegno?\"",
138: "\"Immagino che dovrei lasciarli stare.\"",
139: "tech",
140: "Adrauni batte i denti insieme in quella che sembra una risata, una reazione che non gli avevi mai visto fare. \"E a noi molti Quarg, tra quelli che vivono tra umani ambiziosi, abbiamo forse concesso la nostra tecnologia? Nessuno ha diritto alle invenzioni altrui in virtù di una tolleranza pretestuosa.\" Gli altri Quarg nella stanza guardano Adrauni in modo strano, dopo di che comincia con loro una conversazione nella loro lingua. Dopo qualche momento anche loro ti fissano con sguardi strani, seguiti da un silenzio imbarazzante, che Adrauni rompe parlandoti di nuovo. \"Anche con noi, i Gegno condividono ben poco di interessante.\"",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part04.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part04:', len(P), 'unita', min(P), '-', max(P))
