# -*- coding: utf-8 -*-
# part01: unita' 1-30 (Scientists at the Pub after a Conference) - lotto intero.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
1: "Mentre ti prendi una pausa dopo un lungo viaggio e una procedura di atterraggio che è sembrata ancora più lunga, noti un gruppo di persone entrare nel pub dove sei seduto, che arriva in fiume dal complesso congressuale dall'altra parte della strada. Differiscono per età, abbigliamento e accento, ma i più hanno un badge identico appeso a un cordoncino al collo. Ne noti uno caduto a terra, che dice \"Partecipante - 35° Congresso Pan-galattico annuale di genomica microbica interstellare e dinamica delle popolazioni\". Il gruppo prende posto a un lungo tavolo vicino a te.",
2: "(Ordina un pasto e ascolta la loro conversazione.)",
3: "(Trova un posto più tranquillo per rilassarti.)",
4: "overheard scientists 1",
5: "Frammenti di conversazione ti arrivano attraverso il chiasso del pub.",
6: "Due dei partecipanti più giovani sembrano un po' nervosi. \"Sono così contento di aver finito la mia presentazione. Ero così preoccupato di dover presentare il primo giorno, ma ora posso finalmente rilassarmi e ascoltare davvero gli altri interventi!\"",
7: "\"Oh, assolutamente! Io probabilmente non dovrei nemmeno essere qui: dovrei davvero ripassare... Oh! Cameriere, un'altra birra, per favore!\"",
8: "\"Hai le slide pronte per domani?\"",
9: "\"Sì, ma sono ancora terrorizzato. Odio parlare in pubblico.\"",
10: "\"Non preoccuparti, del tuo specifico campo ne sai più di loro. Andrà bene appena sei sul palco! E poi, il dottorato è un unico grande esercizio di parlare in pubblico. La sicurezza arriva con la pratica.\"",
11: "Un altro scienziato alza gli occhi al cielo dopo un'autopsia degli eventi della giornata. \"Esiste qualche legge che non conosco per cui ogni 'domanda' deve cominciare con 'Credo che questa non sia tanto una domanda quanto un commento...'?\"",
12: "Un'accademica esasperata parla con enfasi alla sua amica di quello che deduci essere un intervento che hanno ascoltato entrambe prima. \"Non credo affatto che le prove sui nucleotidi sostengano la loro ipotesi! Cioè, lo so che i dati proteomici potrebbero essere usati per sostenere la loro conclusione, ma stanno ignorando le mutazioni sinonime!\"",
13: "(Ordina un'altra bevanda e continua ad ascoltare.)",
14: "(Finisci il pasto e vattene.)",
15: "overheard scientists 2",
16: "La conversazione del gruppo si fa più forte, sia per la passione per l'argomento sia per l'effetto di qualche drink.",
17: "\"Guarda, l'analisi può anche essere a posto, ma se non si degnano nemmeno di fornire i numeri di versione del loro software di analisi, allora non è riproducibile e per me è un 'rifiuto' automatico.\"",
18: "Una persona sembra un po' scossa dopo aver considerato quello che sarebbe potuto succedere. \"Ci credi che il mio computer si è bloccato proprio prima che dovessi presentare? Meno male che avevo i backup. Due è uno e uno è niente.\"",
19: "Un gruppo sembra discutere di altri colleghi del campo che, presumibilmente, non sono presenti stasera. \"Singh ed Esterhazy sono dei gran presuntuosi. Il loro lavoro è discreto, credo, ma non abbastanza da giustificare le loro personalità da rockstar mancate!\"",
20: "\"Certo, ma non sono solo presuntuosi: sono presuntuosi carismatici. Il carisma attira bravi dottorandi nel loro laboratorio, che producono buoni articoli, su cui loro mettono il nome. È un ciclo di retroazione positivo.\"",
21: "Le domande di finanziamento sembrano un argomento comune. \"L'Agenzia Repubblicana per la Ricerca Medica dice che il mio lavoro è troppo teorico, ma il Dipartimento di Microbiologia dell'Università di Chiron dice che è troppo applicato!\"",
22: "\"È un bel rompicapo, davvero. Forse potresti trovare finanziamenti dall'industria? Il Sindacato potrebbe essere interessato al tuo lavoro.\"",
23: "\"Sì, ma non sono ancora sicuro di voler rinunciare alla mia libertà accademica.\"",
24: "(Finisci con i miei tempi.)",
25: "(Salda il conto il più in fretta possibile e vattene.)",
26: "overheard scientists 3",
27: "Due partecipanti confrontano le loro lamentele sulle richieste del lavoro. \"Insegnare fa schifo. Tra ore di lezione, ricevimento e preparazione delle lezioni, non resta quasi nessun tempo per la ricerca.\"",
28: "\"Che buffo! Insegnare agli studenti del triennio è la mia unica tregua dalla scrittura di progetti!\"",
29: "Un uomo socievole ma dall'aria esausta è sprofondato nella sedia. \"Questi congressi durano solo tre o quattro giorni, ma sembra sempre che ti invecchino di un anno.\"",
30: "Te ne vai dopo aver finito il pasto, riflettendo su aver origliato uno spaccato di una vita molto diversa dalla tua.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part01.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part01:', len(P), 'unita', min(P), '-', max(P))
