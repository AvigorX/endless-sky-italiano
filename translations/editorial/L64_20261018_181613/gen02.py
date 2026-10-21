# -*- coding: utf-8 -*-
# part02: unita' 26-42 (CCOR Guerrilla Standoff).
# NB: le unita' 35, 36 e 37 hanno UNA virgoletta dispari nel sorgente: si riproducono, non si chiudono.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
26: "Ogni mappa dello spazio umano mette Gagarin nella lista dei porti pirata loschi e a proprio rischio, che farebbero pensare alle fosse di combattimento di Greenrock e ai bazar di attrezzature di Freedom. Eppure appare molto simile a qualsiasi altro spazioporto vecchio e un po' malconcio del Sud, solo su scala molto più grande. Essendo il centro dell'esteso sistema di trasporti del pianeta, sembra che ti stia facendo largo tra migliaia di gagariani e forestieri in ogni atrio e corridoio di questo spazioporto, mentre loro fanno lo stesso per prendere le coincidenze dentro e fuori dal pianeta.",
27: "Ma mentre ti fai strada nella sala centrale, noti che dove ti aspetteresti la massima attività tutto si è fermato. Persino i carrelli a gravità zero sempre in movimento, carichi di merci e rifornimenti, sono fermi e immobili, e l'attenzione di tutti è rivolta a una specie di trambusto proprio al centro dello spazioporto.",
28: "(Dai un'occhiata.)",
29: "(Torna alla mia nave.)",
30: "Passando negli spazi della folla già formata finisci accanto a un gendarme dello spazioporto. Sembra che dovrebbe essere di pattuglia ma è troppo impegnato a guardare la distrazione per fare il suo lavoro in questo momento. Guardando oltre la ringhiera accanto a lui, vedi prima l'enorme e stranamente vuoto spazio al centro della sala, poi una squadra di uomini in tuta da lavoro armati di trapani e spazzole. Intorno a loro c'è un cordone di guerriglieri nelle loro uniformi CCOR color rosa, che valutano il pubblico e la sicurezza dello spazioporto intorno a loro con fucili e pistole.",
31: "I guerriglieri-pittori stanno finendo in fretta i ritocchi di quella che sembra una statua dell'emblema bordeaux e bianco dei Consigli Confederati, mentre un mucchio di macerie accanto suggerisce che al suo posto stava un simbolo del governo locale. Quando si scostano dalla statua, un uomo solo, in un'uniforme molto più curata di quella degli altri, fa un passo avanti davanti al loro lavoro. Senti l'aria raffreddarsi mentre alza la testa per parlare.",
32: "(Ascolta.)",
33: "(Allontanati prima che faccia il discorso.)",
34: "Non vedi nessuna attrezzatura di amplificazione, eppure la sua voce riempie la sala senza sforzo.",
35: "\"Gagariani e forestieri. Capitani e viaggiatori. Militari e contadini.",
36: "\"I mondi del Bordo Esterno, e anzi quelli della Repubblica e dell'intera umanità, sono stati e continuano a essere depredati e devastati da un profitto spietato.",
37: "\"I dirigenti del Sindacato e la nobiltà terriera dei Mondi del Paradiso rubano il lavoro di decine di miliardi di uomini, donne e bambini, da Prime a Foundry; da Valhalla alla Terra; da Bourne a Hestia, e oltre. E per quasi un secolo hanno cospirato per imporre i loro piani sui nostri mondi! L'insurrezione aziendale di Novo Minho e le guerre tra bande nel nord del Bordo Esterno sono un'estensione evidente del braccio di gente come Alastair Korban, che porta solo a ulteriore sofferenza e amara distruzione nella nostra regione!",
38: "\"Ma c'è ancora speranza. Possiamo portare all'indipendenza di Gagarin e unire questo mondo perduto in mano agli oligarchi sponsorizzati dal Sindacato, ai loro accoliti e ai funzionari burattini. Possiamo riunire il Bordo Esterno e restituire la prosperità che ci è stata rubata. Possiamo formare nuovi Consigli Confederati e far brillare di nuovo la luce di Belenos su tutta la galassia!\"",
39: "I gendarmi si guardano intorno e valutano la reazione della folla intorno a loro mentre l'uomo conclude il discorso tra applausi sparsi. L'oratore scende e ordina ai suoi guerriglieri di mettersi in formazione prima di farli marciare fuori dalla folla ancora immobile e nel retro di un furgone militare bordeaux e impolverato che non avevi notato prima, lasciando i resti della vecchia statua sparsi intorno allo spazio vuoto.",
40: "Ti volti e vedi il gendarme accanto al quale eri finito. Incrocia il tuo sguardo e riconosce la tua aria da forestiero.",
41: "\"Solo un'interruzione quotidiana, capitano\", dice. \"Solo nostalgici della vecchia causa. Ne abbiamo una dozzina di questi incidenti al mese.\" Sembra essere interrotto da un ronzio del ricevitore radio al fianco e si allontana a passi lunghi nella folla, lasciandoti sulla balaustra.",
42: "Lentamente ma in modo costante, lo spazioporto esce dallo shock e riprende lo slancio di prima, anche se voltandoti passi davanti a due camion con il marchio del governo e montati con gru, quasi certamente lì per portare via la statua appena installata e ripulire il disordine lasciato dai guerriglieri.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
