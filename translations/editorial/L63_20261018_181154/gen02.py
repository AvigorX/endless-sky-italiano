# -*- coding: utf-8 -*-
# part02: unita' 11-37 (Earth Day Blackout).
# NB: le unita' 18, 29 e 31 hanno UNA virgoletta dispari nel sorgente: si riproducono, non si chiudono.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
11: "Mentre segui i ripetitori di tracciamento verso lo spazioporto centrale della Terra, ti rendi conto che c'è qualcosa di molto strano. Quella che era una città-spazioporto piena di vita ora è completamente immobile, e anche se è quasi mezzanotte i grattacieli enormi sono stranamente bui; non c'è una luce accesa per chilometri.",
12: "Nonostante questo, lo spazioporto sembra ancora operativo, perché le procedure automatiche di firma dei documenti di atterraggio, rifornimento e controllo dell'idoneità spaziale della nave si completano mentre atterri. Nel terminale dello spazioporto ci sono candele di cera distanziate per portare un po' di luce nei corridoi ora bui. È una vista strana per il pianeta più popoloso dello spazio umano.",
13: "(Trova qualcuno e chiedi.)",
14: "(Il blackout passerà probabilmente.)",
15: "Ti avvicini a un banco informazioni nell'atrio del terminale che, data la situazione, non sembra così affollato come ci si aspetterebbe. Dopo un momento arrivi all'addetto dietro il banco.",
16: "\"Che succede con il blackout?\"",
17: "\"Quando verrà risolto il blackout?\"",
18: "L'addetto ridacchia. \"Avrei dovuto aspettarmelo, una domanda così, dal tuo accento. Oggi è la Giornata della Terra, quando tutte le città della Terra, e dico tutte, partecipano a un blackout totale. Anche l'edificio del Parlamento oggi era spento. Ci fa pensare alle nostre origini; che un tempo vivevamo sulla terraferma senza elettricità, tutti confinati su questo unico pianeta, divisi e incerti. Certo, gente come me deve continuare a lavorare, ma per gli altri è un giorno libero per godersi quel poco di natura e di Terra che noi terrestri ci siamo lasciati, ironicamente. Hai altre domande?",
19: "\"Quando è iniziata questa tradizione?\"",
20: "\"Grazie per avermelo detto.\"",
21: "\"Beh, la mia vecchia lezione di storia mi dice che la prima Giornata della Terra è stata intorno al XX secolo, qualche anno dopo che siamo atterrati sulla Luna per la prima volta. Allora c'erano un mucchio di conflitti e dispute per le risorse e su come ci combattevamo dappertutto e scavavamo tutto per alimentare tutte quelle auto sporche e primitive, le centrali e le fabbriche che avevamo allora. Così, come dimostrazione di unità contro tutto questo, la gente ha cominciato a celebrare la bellezza naturale della Terra riportandoci al nostro passato.\"",
22: "Appena finisce, le luci del soffitto si riaccendono. \"Ah, ecco fatto. Peccato essermi perso i festeggiamenti, ma questa è la fine della Giornata della Terra e del mio turno di notte. Spero che tu abbia passato una buona Giornata della Terra, e buona notte!\"",
23: "Ti avvicini a una donna con un mucchio di borse oversize raggruppate intorno alla sedia. Sta picchiettando velocemente sul datapad, ma alza comunque lo sguardo quando ti avvicini. \"Scusa, capitano, stavo cercando di capire quando riapre la metropolitana. Lo sai?\"",
24: "\"Ne so quanto te, mi dispiace.\"",
25: "\"Forse ha a che fare con il blackout?\"",
26: "\"Ah, spengono tutto per la Giornata della Terra e poi danno per scontato che tutti noi che veniamo da fuori lo capiamo. Chi l'avrebbe detto...\"",
27: "\"La Giornata della Terra?\"",
28: "\"Spengono tutto?\"",
29: "\"Non hai visto quello che succedeva fuori mentre entravi? Ha a che fare con la Giornata della Terra. In quei tempi antichi, prima che gli umani riuscissero a lasciare questo pianeta, erano bloccati in una catena di problemi e dispute sull'energia. Sai, allora non avevano reattori a fusione. Tempi terribilmente primitivi.",
30: "way in",
31: "\"Sì, suppongo che tu abbia visto quello che succedeva fuori mentre entravi. Ha a che fare con la Giornata della Terra. In quei tempi antichi, prima che gli umani riuscissero a lasciare questo pianeta, erano bloccati in una catena di problemi e dispute sull'energia. Sai, allora non avevano reattori a fusione. Tempi terribilmente primitivi.",
32: "\"Così hanno deciso che, il 22 aprile di ogni anno, tutta la Terra sarebbe entrata in un blackout totale per simboleggiare che non avevano abbastanza energia per sostentarsi, e per ricordare loro che l'unico modo per avanzare era continuare a spingersi avanti, trovare nuove vie per l'energia, altrimenti quei blackout sarebbero diventati più lunghi e più frequenti. Affascinante, eh?\"",
33: "\"Mi sembra un po' un passo indietro.\"",
34: "\"È affascinante, grazie.\"",
35: "\"Beh, forse. Ma la Terra è così a volte. È sopravvissuta a così tanto, e senza la Giornata della Terra per ricordare ai nostri antenati che dobbiamo continuare a guardare avanti, forse non saresti sulla tua graziosa navicella, vero?\"",
36: "Le luci dello spazioporto si riaccendono mentre lo dice, e lei si volta di nuovo verso il datapad. \"Oh, è mezzanotte. Devo vedere se la metropolitana ha aperto per arrivare al mio alloggio. Buon viaggio!\"",
37: "Dopo che l'orologio supera la mezzanotte, le luci dello spazioporto si riaccendono, seguite dalle insegne e dalle luci della città intorno. Alcuni operai passano a spegnere le candele e poi le ripongono in armadi che non si vedono.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
