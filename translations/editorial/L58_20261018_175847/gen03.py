# -*- coding: utf-8 -*-
# part03: unita' 33-43 (Worker's Occasion, Paradise Cleaner Incident) - chiude il segmento.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
33: "Sostando a considerare un ristorante per la cena, noti un operaio locale con un pugno di crediti che guarda con desiderio il menù. I suoi vestiti sono consumati con ordine e sembrano appena spazzolati, ma è impossibile non notare le macchie e le tracce di sporco che non sono andate via. L'uomo sembra indubbiamente nervoso, e guarda la disposizione formale della sala con un'evidente mancanza di familiarità. Guardando il menù anche tu, ti rendi conto che i prezzi, per te molto accessibili, sarebbero stati irraggiungibili prima del tuo cambio di carriera.",
34: "(Offriti di pagare la cena all'uomo.)",
35: "(Compatiscilo in silenzio.)",
36: "(Sorridi all'uomo.)",
37: "Sorridi all'uomo e rifletti sul valore dei piccoli traguardi. Lui coglie il tuo sorriso con la coda dell'occhio e ti ricambia con un cenno esitante ma amichevole prima che tu torni alle tue faccende.",
38: "Entri nel ristorante e attiri l'attenzione dell'uomo, offrendoti di pagargli il pasto.",
39: "Ti riconosce come pilota e si acciglia, poi ti dice, in termini coloriti, dove puoi ficcarti quell'offerta. Mentre ti allontani, pensi a quale sarebbe la tua reazione se una persona molto più ricca ti compatisse pagandoti la cena.",
40: "Compatisci l'uomo che deve lavorare un mese intero per permetterselo e prosegui per la tua strada.",
41: "Visitare gli spazioporti di Paradise è sempre un'esperienza interessante per chi viene da fuori. In nessun altro luogo la classe è una componente così radicata della vita quotidiana. Ti ritrovi a notare persone che sembrano invisibili ai più, ma loro non incrociano mai il tuo sguardo. Sembrano sempre fare del loro meglio per non farsi notare.",
42: "In passato non avevi notato bambini che sembrassero poveri qui, ma in questa occasione ne vedi uno che rovescia un mocio e un secchio... proprio davanti a un uomo d'affari e alla sua famiglia che trascinano le valigie per lo spazioporto. Non hai mai visto qualcuno diventare così pallido come la donna delle pulizie, la madre del bambino, che si precipita a sistemare le cose prima ancora che l'uomo tiri il fiato.",
43: "Un paio di agenti di sicurezza compaiono quasi subito, prima che tu possa intervenire in un modo o nell'altro, mentre l'uomo e la sua famiglia cominciano a lamentarsi. Un agente fornisce rassicurazioni mentre l'altro sorveglia la donna delle pulizie, che porta rapidamente il figlio fuori dai guai.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part03.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part03:', len(P), 'unita', min(P), '-', max(P))
