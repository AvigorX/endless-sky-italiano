# -*- coding: utf-8 -*-
# part04: unita' 42 (Sojourn Sunday Sales) - chiude il segmento.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

P = {
42: "Entri nello spazioporto e socchiudi gli occhi per la sorpresa, guardando folle di persone che si fanno largo tra le catene umane di code avvolte intorno all'area commerciale. Scansionando l'ambiente noti inserzioni su inserzioni di località di vacanza, tutte a uno sconto assurdamente alto. Eppure, nonostante i prezzi molto ridotti, le vacanze pubblicizzate costano ancora somme così grandi che un te più giovane non avrebbe mai potuto giustificare una spesa simile.",
}

json.dump({str(k): v for k, v in sorted(P.items())},
          open(os.path.join(HERE, 'parts', 'part04.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('part04:', len(P), 'unita', min(P), '-', max(P))
