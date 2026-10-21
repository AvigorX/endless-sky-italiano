# -*- coding: utf-8 -*-
# part02: unita' 18-35 (Exotic Life: Ada) - chiude il lotto E il file.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
18: "Un trambusto rumoroso attira la tua attenzione mentre attraversi lo spazioporto e alzi lo sguardo: tre grossi agenti di sicurezza dei Lovelace Labs stanno circondando un pilota furibondo.",
19: "\"Ma devo scaricare il mio carico!\", sta urlando il pilota proprio in faccia a un agente che sembra del tutto imperturbabile.",
20: "\"Non qui, no\", dice lei con aria annoiata, come se affrontasse questo genere di situazione venti volte al giorno. \"Non prima che la tua nave sia decontaminata.\"",
21: "Ora sei solo uno di una folla di curiosi che circonda il gruppo in un grande cerchio. Il pilota sembra accorgersi di essere al centro dell'attenzione e decide di appellarsi alla folla.",
22: "\"Vedete cosa stanno facendo?\", urla. \"Questo è... questo è un abuso! Sono vittima di molestie!\"",
23: "L'agente non si scompone, e picchietta su un datapad mentre parla.",
24: "\"Le regole sono regole e devi seguirle come tutti gli altri.\" Alza lo sguardo, gli occhi socchiusi. \"Qui dice che il tuo carico è fatto di statuine in miniatura. E di cosa sono fatte, esattamente?\"",
25: "Il pilota sembra improvvisamente mortificato e alza le mani in segno di resa.",
26: "\"Va bene, va bene\", dice. \"Farò la procedura di decon. Ok? Hai vinto.\"",
27: "\"Di. Cosa. Sono. Fatte?\"",
28: "\"Acciaio inossidabile.\"",
29: "\"Ahia\", dice lei, ma l'espressione annoiata è sparita e sembra divertirsi. \"Dodici tonnellate di statuine e dovremo scansionarle tutte, una per una, per assicurarci che non siano contaminate. Potrebbe volerci un po'.\"",
30: "Tra qualche risatina sparsa e qualche gemito di compassione la folla comincia a disperdersi, e gli altri due agenti riportano il pilota verso la sua nave, lasciando l'agente principale a picchiettare allegramente sul datapad. Dopo qualche istante alza lo sguardo e nota che la stai guardando.",
31: "\"Teredini di Delve?\"",
32: "\"Mi è sembrato un po' duro.\"",
33: "\"È stato divertente.\"",
34: "Alza le spalle. \"Faccio solo il mio lavoro.\"",
35: "\"Uh-huh\", dice. \"Solo che ora le vediamo su navi che non sono state da nessuna parte vicino a Delve. Sembra che si stiano diffondendo.\"",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
