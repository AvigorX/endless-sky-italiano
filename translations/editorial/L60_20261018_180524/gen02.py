# -*- coding: utf-8 -*-
# part02: unita' 30-31 (Masquerade Hanging) - chiude il segmento.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
30: "L'odore di polvere da sparo bruciata aleggia nell'aria mentre entri in una piazza, guardando un corpo che viene fatto rotolare giù da una piattaforma rialzata. Grida e urla riempiono l'aria mentre un uomo mascherato trascina una donna attraverso la piattaforma fino al palco centrale, con una pistola vecchio stile alla tempia mentre le chiede qualcosa che non riesci a distinguere. Per fortuna l'uomo non spara: toglie l'arma dalla tempia e poi la stende con l'arma stessa.",
31: "Pochi istanti dopo la piccola folla gli permette di allontanarsi dal lato opposto rispetto a te, senza incidenti e senza spiegazioni. Non sei del tutto sicuro di cosa pensare di questa scena, mentre i corpi vengono trascinati via in fretta.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part02.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part02:', len(P), 'unita', min(P), '-', max(P))
