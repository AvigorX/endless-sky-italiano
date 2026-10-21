"""mkparts.py (2ª stesura) — L129: `data/human/boarding missions.txt` (89 unita', righe 15-386).

Forma nuova: **48 `TEXT`** sono **frammenti di frase** che il gioco concatena
(`${assist merchant 1} <origin>${assist merchant 2} ${assist merchant 3} <payment>${assist merchant 4}`). Il lotto
assume percio' un invariante che i lotti precedenti non avevano: **spazi iniziali e finali identici al sorgente**,
unita' per unita' — lo spazio finale e' parte del testo, e senza di esso la frase composta si rompe.

Due difetti del sorgente si **riproducono**, non si correggono: il frammento `` the `` e' senza spazio finale (l'inglese
produce «theits», l'italiano «ilil»), e la frase composta e' sgrammaticata per costruzione in entrambe le lingue.

Quattro unita' **non sono testo** e restano identiche, elencate: le due `CONVERSATION` (1, 2) sono template `${...}` e
i due `TEXT` (27, 28) sono **nomi di frase** citati da `phrase`. Sei `VALUE` restano identici (nomi di missione).

La resa e' indicizzata **per unita'** (`D`): con 48 frammenti brevi le firme testuali sarebbero ambigue, perche' un
frammento e' spesso prefisso di un altro (`to ` dentro `in order to `). Le ripetizioni si controllano a parte:
**stesso inglese ⇒ stessa resa**, su tutte le 89 unita'.
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

D = {
    # frase 1-1: apertura
    3: "Sapendo che ",
    4: "Poiché ",
    5: "Comprendendo che ",
    6: "Considerando che ",
    7: "Visto che ",
    8: "Sapendo come ",
    # frase 1-2: cosa hai fatto
    9: "hai cambiato rotta ",
    10: "ti sei scomodato ",
    11: "potresti aver cambiato i tuoi piani di volo ",
    # frase 1-2 hazardous
    12: "hai rischiato la vita ",
    13: "hai rischiato la nave ",
    14: "hai rischiato la tua nave ",
    15: "hai affrontato il fuoco nemico ",
    16: "hai affrontato il pericolo ",
    # frase 1-3: preposizione, verbo, articolo
    17: "per ",
    18: "al fine di ",
    19: "così che potessi ",
    20: "salvare ",
    21: "riparare ",
    22: "recuperare ",
    23: "assicurare ",
    24: "soccorrere ",
    25: "aiutare ",
    26: "il",          # senza spazio finale, come il sorgente
    # frase 2
    29: ", ",
    30: " e ",
    31: "salvare il suo carico, ",
    32: "assicurare il suo carico, ",
    33: "salvare il suo equipaggio, ",
    34: "recuperare il suo equipaggio, ",
    # frase 3
    35: "il suo ",
    36: "il ",
    37: "della nave ",
    38: "del vascello ",
    39: "sollevato ",
    40: "capitano ",
    41: "ti dà",
    42: "ti offre",
    43: "ti ricompensa con",
    # frase 4
    44: ".",
    45: " in segno di gratitudine.",
    46: " in segno di riconoscenza.",
    47: " come espressione della loro gratitudine.",
    48: " in ringraziamento.",
    49: " per ringraziarti.",
    50: " per il tuo aiuto.",
    # missioni
    52: "Trasporta l'equipaggio rimasto di una nave distrutta, <bunks> persone che lavoravano sulla <origin>, fino a "
        "<destination>.",
    53: "Mentre ti avvicini alla <origin>, i tuoi sensori radar rilevano che la nave che stai assistendo sta per "
        "essere colpita in pieno da un gigantesco asteroide! In un volo normale non sarebbe un gran problema, ma una "
        "nave già gravemente danneggiata e incapace di schivare potrebbe essere distrutta del tutto.",
    54: "(Spara all'asteroide.)",
    55: "(Manovra la mia nave per fare scudo alla <origin>.)",
    56: "(Prova a riparare la <origin> così che possa schivare l'asteroide.)",
    57: "(Interrompi le manovre di attracco e vola via.)",
    58: "(Manovra la mia nave per fare scudo alla <origin>.)",
    59: "(Prova a riparare la <origin> così che possa schivare l'asteroide.)",
    60: "(Interrompi le manovre di attracco e vola via.)",
    61: "Giri la nave e attivi i propulsori, cercando di allontanarti il più possibile dalla nave in avaria. Pochi "
        "secondi dopo, l'asteroide si scontra con la <origin>, facendola a pezzi e uccidendo tutti i membri "
        "dell'equipaggio, mentre sulla superficie dell'asteroide lascia poco più che un graffio.",
    62: "Sparisci all'asteroide nel tentativo di distruggerlo, ma sembra che tu abbia solo peggiorato le cose. "
        "L'asteroide si è ormai spezzato in decine di frammenti più piccoli che volano ancora dritti verso la "
        "<origin>. Prima che tu possa reagire per rimediare all'errore, la maggior parte dei frammenti ha già "
        "colpito la <origin>, che ora si sta rapidamente depressurizzando. Non c'è altro da fare che allontanarsi a "
        "una distanza di sicurezza dalla nave che esplode...",
    63: "I colpi che spari spezzano rapidamente l'asteroide, i cui frammenti sembrano aver cambiato rotta abbastanza "
        "da mancare del tutto la <origin>. Dopo averla riparata, chiami il suo capitano, che ti ringrazia con un "
        "pagamento di 30.000 crediti.",
    64: "Attracchi alla <origin>, sperando di uscirne vivo, ma appena raggiungi il portello l'asteroide colpisce e "
        "una serie di esplosioni comincia a venire dalla nave in avaria. Riesci a raggiungere la cabina di "
        "pilotaggio e a sganciarti, ma l'equipaggio dell'altra nave non ha fatto in tempo a raggiungerti...",
    65: "Attracchi alla <origin>, sperando di uscirne vivo, ma, appena raggiungi il portello, l'asteroide colpisce e "
        "una serie di esplosioni comincia a venire dalla nave in avaria. Quando ti sganci, la maggior parte "
        "dell'equipaggio dell'altra nave è riuscita a raggiungere la tua, e ti chiede di portarli su <destination>.",
    66: "\"Va bene, non è lontano.\"",
    67: "\"Quanto potete pagarmi?\"",
    68: "\"Ho qualche centinaio di migliaia di crediti\", dice uno di loro, presumibilmente il capitano. \"Devo "
        "metterne da parte abbastanza per comprare una nuova astronave, ma riceverai comunque una paga decente.\"",
    69: "L'asteroide, dopo aver colpito il tuo scudo, si spezza in un milione di frammenti che si allontanano dalla "
        "<origin>. Dopo averla riparata, chiami il suo capitano, che ti ringrazia con un pagamento di 30.000 "
        "crediti.",
    70: "Il capitano con cui avevi parlato ti ringrazia di nuovo per aver salvato lui e il suo equipaggio, e ti "
        "consegna <payment>.",
    72: "Consegna <cargo> a <destination>. Il pagamento è <payment>.",
    73: "Quando ripari la <origin>, il capitano ti chiama. \"È la quarta volta che quasi ci lascio le penne questa "
        "settimana facendo questo lavoro! Tieni, porta questo <cargo> a <destination> e finisci il lavoro al posto "
        "mio. Hanno detto che il pagamento è <payment>.\"",
    74: "(Prendi il carico.)",
    75: "(Non prendere il carico.)",
    76: "Il capitano comincia a imprecare ad alta voce, così interrompi la comunicazione. Speriamo che arrivi a "
        "destinazione tutto intero.",
    77: "Scarichi il tuo carico di <commodity>, spieghi che il mercante che aveva accettato il lavoro ha rinunciato "
        "e ti ha passato il carico, e incassi il pagamento di <payment>.",
    78: "Il capitano della <origin> ti ringrazia per la riparazione, ma ti informa che i pirati che li hanno messi "
        "fuori uso sono solo una piccola parte di una flotta che attacca <destination>.",
    79: "Le autorità di <planet> probabilmente ti pagheranno bene se le assisti, ma potrebbe anche essere un modo "
        "facile di farti ammazzare.",
    80: "(Non unirti allo scontro.)",
    81: "(Unisciti alla flotta di difesa.)",
    83: "Sconfiggi un'incursione piratesca su <destination>.",
    85: "Sconfiggi un'incursione piratesca su <destination>.",
    87: "Sconfiggi un'incursione piratesca su <destination>.",
    89: "Sconfiggi un'incursione piratesca su <destination>.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'TEXT': 48, 'MISSION_TEXT': 21, 'VALUE': 6, 'DESCRIPTION': 6,
                                                       'CONVERSATION': 6, 'DIALOG': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 22
assert sum(u['english'].count('"') for u in SRC) == 10
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 18, len(ctx)
assert list(ctx.values()) == [1, 1, 6, 3, 5, 10, 2, 1, 5, 9, 7, 20, 7, 4, 2, 2, 2, 2], list(ctx.values())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {
    '<origin>': 17, '<destination>': 9, '<planet>': 7, '<payment>': 6, '<cargo>': 2, '<bunks>': 1, '<commodity>': 1}

# unita' che NON sono testo: template `${...}` e nomi di frase citati da `phrase`
IDENT = [1, 2, 27, 28]
assert [ENG[i] for i in IDENT] == [
    '${assist merchant 1} <origin>${assist merchant 2} ${assist merchant 3} <payment>${assist merchant 4}',
    '${assist merchant 1 hazardous} <origin>${assist merchant 2} ${assist merchant 3} <payment>${assist merchant 4}',
    'assist merchant 2 simple', 'assist merchant 2 complex']
VAL = [u['idx'] for u in SRC if u['kind'] == 'VALUE']
assert VAL == [51, 71, 82, 84, 86, 88], VAL
assert [ENG[i] for i in VAL] == ['Passengers to <planet>', 'Delivery to <planet>'] + ['Defend <planet>'] * 4

# due frammenti sono sola punteggiatura e restano identici: ',' e '.'
PUNCT = [29, 44]
assert [ENG[i] for i in PUNCT] == [', ', '.']

expected = [i for i in ENG if i not in IDENT and KIND[i] != 'VALUE']
assert sorted(D) == expected, (len(D), len(expected), [i for i in expected if i not in D],
                               [i for i in D if i not in expected])

T = {}
for u in SRC:
    eng = u['english']
    if u['idx'] in IDENT or u['kind'] == 'VALUE':
        T[u['idx']] = eng
    else:
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + D[u['idx']]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    # invariante dei frammenti: spazio iniziale e finale identici al sorgente
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx, repr(eng), repr(txt))
    assert len(txt.lstrip('\t')) - len(txt.lstrip('\t').lstrip(' ')) == \
        len(eng.lstrip('\t')) - len(eng.lstrip('\t').lstrip(' ')), ('spazio iniziale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx in IDENT or kind == 'VALUE':
        assert txt == eng, idx
    elif idx in PUNCT:            # frammenti di sola punteggiatura: identici per necessita', dichiarati
        assert txt == eng == (', ' if idx == 29 else '.'), (idx, repr(txt))
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), repr(eng))

# ripetizioni: stesso inglese ⇒ stessa resa (tre opzioni doppie, quattro DESC uguali, quattro VALUE uguali)
dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1], [(k[:40], v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 80, len(dup)

for n, (lo, hi) in enumerate(((1, 30), (31, 60), (61, 89))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('89 unita (30+30+29) · 80 testi distinti · 4 identici (2 template, 2 nomi di frase) · 6 VALUE identici')
print('spazi iniziali/finali identici su tutte le 89 unita · 22 tab · 10 virgolette · 43 token in 7 famiglie')
