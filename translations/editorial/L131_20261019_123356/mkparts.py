"""mkparts.py — L131: la coda di `data/human/boarding missions.txt` (76 unita', righe 695-959). CHIUDE IL FILE.

**2 contesti**: `Turn in Tarquin` (1 `DESCRIPTION`) e `Boarding Derelict` (75 `MISSION_TEXT`). **Zero `VALUE`** e
**zero `UI_LABEL`**: due asserzioni **vuote** scritte (`== []`), non omissioni.

Forma: **74 unita' con tab**, **2 virgolette** (unita' 60, `"hostile spacecraft"`), **22 token** in **2 famiglie**
(`<origin>` 14, `<payment>` 8), **52 testi distinti su 76** — **24 ripetizioni**, il massimo finora. La ripetizione e'
la struttura del lotto: le riparazioni riuscite e fallite sono le stesse frasi su rami diversi, e la resa le rende
identiche per costruzione (resa indicizzata per indice, coerenza verificata a posteriori).
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KIND = {u['idx']: u['kind'] for u in SRC}
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

POWER_OK = ("Con qualche riparazione semplice riesci a rimettere in funzione e a far girare lisci i sistemi di "
            "alimentazione della nave.")
HULL_OK = ("Ci vuole un po', ma riesci a stabilizzare lo scafo della nave. Nel farlo trovi e ripari dei cavi rotti "
           "incassati nello scafo, che avrebbero potuto causare una sovratensione.")
COCKPIT = ("Finite le riparazioni, vai alla cabina di pilotaggio per vedere se la <origin> parte senza esplodere. "
           "Pronto a scattare verso il portello se qualcosa va storto, avvii la nave.")
SUCCESS = ("La nave vibra e prende vita. Con il fiato sospeso aspetti il suono di qualche sistema che esplode, ma non "
           "succede nulla. Successo! La nave è tua.")
VALVE_OK = ("Mentre ripari i sistemi dei motori, una valvola si apre di colpo. Per fortuna la valvola secondaria è "
            "meccanica e non ha bisogno di corrente, così si chiude da sola e impedisce al refrigerante di schizzare "
            "fuori con violenza. Con più cautela, concludi le riparazioni dei motori.")
VALVE_POWER = ("Mentre ripari i sistemi dei motori, una valvola si apre di colpo. Per fortuna hai ripristinato "
               "l'alimentazione, così la valvola secondaria si chiude da sola e impedisce al refrigerante di "
               "schizzare fuori con violenza. Con più cautela, concludi le riparazioni dei motori.")
FLEE = "(Fuggi dalla nave, temendo che le mie riparazioni l'abbiano resa più pericolosa.)"
ENG_NEXT = "(Ripara ora i motori.)"
HULL_NEXT = "(Ripara ora lo scafo.)"
POWER_NEXT = "(Ripara ora l'alimentazione.)"
ENG_REP = "(Ripara i motori.)"
HULL_REP = "(Ripara lo scafo.)"
POWER_REP = "(Ripara l'alimentazione.)"
BREAK_UP = "Torni di corsa sulla tua nave prima che la <origin> si sfaldi."
TEAR = "Appena in tempo: la <origin> comincia a sfaldarsi con violenza nel momento in cui la tua nave si sgancia."

D = {
    1: "Consegna il capitano Tarquin alle forze dell'ordine sul pianeta più vicino.",
    2: "Sali a bordo della <origin> e ti guardi attorno nel suo scafo abbandonato, che sembra in condizioni "
       "abbastanza stabili. Potresti rischiare di ripararla per un profitto maggiore, oppure recuperare ciò che puoi "
       "dalla nave e lasciare il resto.",
    3: "(Recupera ciò che puoi dalla nave.)",
    4: "(Prova a riparare la nave.)",
    5: "Deciso a puntare al colpo grosso, provi a riparare la nave.",
    6: "(Ripara prima i motori.)",
    7: "(Ripara prima lo scafo.)",
    8: "(Ripara prima l'alimentazione.)",
    9: POWER_OK,
    10: ENG_NEXT,
    11: HULL_NEXT,
    12: HULL_OK,
    13: ENG_NEXT,
    14: POWER_NEXT,
    15: HULL_OK,
    16: POWER_REP,
    17: FLEE,
    18: HULL_OK,
    19: ENG_REP,
    20: FLEE,
    21: HULL_OK,
    22: COCKPIT,
    23: SUCCESS,
    24: VALVE_OK,
    25: HULL_NEXT,
    26: POWER_NEXT,
    27: VALVE_OK,
    28: POWER_REP,
    29: FLEE,
    30: VALVE_POWER,
    31: HULL_REP,
    32: FLEE,
    33: VALVE_POWER,
    34: COCKPIT,
    35: SUCCESS,
    36: POWER_OK,
    37: ENG_REP,
    38: FLEE,
    39: POWER_OK,
    40: HULL_REP,
    41: FLEE,
    42: POWER_OK,
    43: COCKPIT,
    44: SUCCESS,
    45: "Con qualche riparazione semplice riesci a rimettere in funzione i sistemi di alimentazione della nave. Per "
        "poco. L'alimentazione si spegne di nuovo mentre una vibrazione violenta scuote la nave. " + BREAK_UP,
    46: "Mentre rattoppi un segmento di scafo noti che una deformazione si sta allargando lentamente. Peggio ancora, "
        "è una parte strutturalmente essenziale dello scafo. " + BREAK_UP,
    47: "Mentre ripari i sistemi dei motori, una valvola si apre di colpo. Senza alimentazione la valvola secondaria "
        "non può chiudersi, e il refrigerante vola incontrollato dentro lo scafo. La forza del liquido provoca una "
        "vibrazione violenta che scuote la nave. " + BREAK_UP,
    48: "Diffidente delle tue stesse riparazioni avventate, decidi di lasciare stare la nave. Però sei riuscito a "
        "tenerti un po' di rottame trovato durante i lavori, del valore di <payment>.",
    49: "I tuoi timori sembrano fondati: la <origin> comincia a sfaldarsi nel momento in cui ti sganci.",
    50: "Appena la nave comincia a vibrare e prendere vita, una forte esplosione la scuote!",
    51: "(Corri.)",
    52: "Cominci a correre nei corridoi stretti della nave. Oggetti rotolano ovunque, e altre esplosioni minacciano "
        "di farti cadere.",
    53: "(Corri nel portello.)",
    54: "(Tuffati nel portello.)",
    55: "(Scivola nel portello.)",
    56: "Mentre scivoli sul pavimento, esplosioni erompono ai tuoi due lati, e sei sicuro di sembrare un eroe "
        "d'azione mentre attraversi il portello a tutta velocità verso la salvezza. Scampato per un soffio alla morte "
        "e senza voglia di tentare la sorte, te ne vai in fretta.",
    57: "Mentre corri verso il portello, esplosioni erompono ai tuoi due lati, e sei sicuro di sembrare un eroe "
        "d'azione mentre ti apri un varco attraverso il portello verso la salvezza. Scampato per un soffio alla morte "
        "e senza voglia di tentare la sorte, te ne vai in fretta.",
    58: "Mentre ti tuffi verso il portello, esplosioni erompono ai tuoi due lati, e sei sicuro di sembrare un eroe "
        "d'azione mentre ti raccogli e rotoli attraverso il portello verso la salvezza. Scampato per un soffio alla "
        "morte e senza voglia di tentare la sorte, te ne vai in fretta.",
    59: "Nonostante tutti i tuoi sforzi per far volare davvero la nave, non ne vuole sapere. In compenso ora hai il "
        "tempo di saccheggiare e portarti via qualche modulo dalla nave a piacere. Prima di lasciare la cabina di "
        "pilotaggio trovi un gettone di credito appoggiato sui comandi, del valore di <payment>.",
    60: "Però noti una luce lampeggiante sui comandi della nave. Ti chiedi cosa possa segnalare mentre ti avvicini, "
        "e quando sei abbastanza vicino capisci che avverte dell'arrivo di \"astronavi ostili\" nel sistema. Il "
        "relitto doveva essere una trappola dei pirati, e a peggiorare le cose la nave sembra preparata a esplodere! "
        "Ora hai un buon sospetto di cosa stai affrontando mentre corri di nuovo verso la tua nave.",
    61: "Però, poco dopo, uno schermo si illumina nella cabina di pilotaggio mostrando qualcosa di strano. Guardando "
        "più da vicino capisci che è una forma di software malevolo, e sta cercando di introdursi nel sistema della "
        "tua nave!",
    62: "Corri di nuovo alla tua nave, decolli in fretta e distruggi la <origin>, ma quando riesci a eliminare il "
        "virus ha già fatto irruzione nel tuo conto bancario; il conto riporta una variazione di saldo di "
        "<payment>.",
    63: "Deciso a non rischiare, setacci in fretta la nave in cerca di rottame e moduli di valore.",
    64: "Dopo una breve ispezione della nave trovi pochi oggetti di valore, e riesci a recuperare solo una misera "
        "somma di <payment> dalla <origin>.",
    65: "Cercando per la nave scopri che vale parecchio: riesci a recuperare dalla <origin> una somma sostanziosa, "
        "del valore di <payment>.",
    66: "Nascosta sotto un pannello trovi una piccola scatola. Aprendola scopri che è piena di <payment>.",
    67: "Mentre cerchi qualcosa di valore per la nave trovi una grande custodia nera piena di 325.000 crediti. "
        "Frugando ancora trovi accanto alla custodia un registro di testo, e decidi di portarti via entrambi.",
    68: "Mentre cerchi qualcosa di valore per la nave trovi una specie di mappa infilata in un pannello. È facile da "
        "portare, e ti lascia il tempo di recuperare ancora una misera somma di <payment> dalla <origin>.",
    69: "(Fai esplodere la nave e vattene, così nessun altro potrà saccheggiarla.)",
    70: "(Prova a recuperare ancora un po' di materiale.)",
    71: "Prima di partire fai esplodere la nave, per impedire ad altri cacciatori di relitti di setacciare la nave "
        "ormai vuota.",
    72: "Provi a cercare altri oggetti di valore e per fortuna trovi materiale in più, del valore di <payment>. "
        "Però lo scafo comincia a scricchiolare e gemere, e ti costringe a tornare in fretta sulla nave.",
    73: TEAR,
    74: "Provi a cercare altri oggetti di valore ma senza successo. Però lo scafo comincia a scricchiolare e gemere, "
        "e ti costringe a tornare in fretta sulla nave.",
    75: TEAR,
    76: "Ti dirigi alla cabina di pilotaggio sperando di trovare qualcosa di valore. Non trovando nulla all'inizio, "
        "ti volti per uscire e cercare in altre parti della nave.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 75, 'DESCRIPTION': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 74
assert sum(u['english'].count('"') for u in SRC) == 2
ctx = collections.OrderedDict()
for u in SRC:
    ctx[u['context']] = ctx.get(u['context'], 0) + 1
assert len(ctx) == 2 and list(ctx.values()) == [1, 75], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {'<origin>': 14, '<payment>': 8}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == []
assert 695 == min(u['line'] for u in SRC) and 959 == max(u['line'] for u in SRC)

expected = [i for i in ENG]
assert sorted(D) == expected, (len(D), len(expected), [i for i in expected if i not in D])

T = {}
for u in SRC:
    eng = u['english']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + D[u['idx']]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1], [(k[:50], v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 52, len(dup)

for n, (lo, hi) in enumerate(((1, 26), (27, 51), (52, 76))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('76 unita (26+25+25) · 52 testi distinti (24 ripetizioni) · 1 DESCRIPTION + 75 MISSION_TEXT')
print('74 tab · 2 virgolette (unita 60) · 22 token in 2 famiglie · zero VALUE, zero UI_LABEL')
