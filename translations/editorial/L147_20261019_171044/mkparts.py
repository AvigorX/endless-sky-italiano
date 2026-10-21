"""mkparts.py — L147: `data/coalition/coalition jobs.txt`, righe 16-293 (30 unita').

**Il lotto piu' denso di token finora**: 65 occorrenze su 7 simboli. `<payment>` (17) e `<date>` (4) sono corti e
vivono in frasi simili: la parita' si verifica **per simbolo e per unita'**, perche' un totale pari nasconderebbe uno
scambio.

I **13 `VALUE`** sono nomi di lavoro mostrati in UI (`Workers to the <planet>`): restano **identici**, token compresi,
e si verificano uno per uno. Le ripetizioni sono **triple**: stessa stringa inglese -> stessa resa, per uguaglianza.

Zero tab, zero virgolette: quattro asserzioni vuote (piu' zero `LOGBOOK`, zero `DIALOG`, zero `UI_LABEL`).
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
KEY = {i: e.rstrip() for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

D = {
    1: "Scarichi gli operai sul <planet>. Pochi minuti dopo ricevi un bonifico di <payment>.",
    2: "Workers to the <planet>",
    3: "Trasporta questo equipaggio di <bunks> operai sul <planet> degli Heliarch, dove aiuteranno negli sforzi per "
       "mantenere ed espandere il mondo ad anello. Il compenso sarà di <payment>.",
    4: "Workers to the <planet>",
    5: "Trasporta questo equipaggio di <bunks> operai sul <planet> degli Heliarch, dove aiuteranno negli sforzi per "
       "mantenere ed espandere il mondo ad anello. Il compenso sarà di <payment>.",
    6: "Workers to the <planet>",
    7: "Trasporta questo equipaggio di <bunks> operai sul <planet> degli Heliarch, dove aiuteranno negli sforzi per "
       "mantenere ed espandere il mondo ad anello. Il compenso sarà di <payment>.",
    8: "Scarichi i volontari sul <planet>, dove vengono ricevuti da un agente degli Heliarch. Pochi minuti dopo ricevi "
       "un bonifico di <payment>.",
    9: "Volunteers to the <planet>",
    10: "Il governo ti pagherà <payment> per portare questi <bunks> lavoratori volontari sul <planet>, dove daranno una "
        "mano nella costruzione in cambio di vitto e alloggio.",
    11: "Volunteers to the <planet>",
    12: "Il governo ti pagherà <payment> per portare questi <bunks> lavoratori volontari sul <planet>, dove daranno una "
        "mano nella costruzione in cambio di vitto e alloggio.",
    13: "Volunteers to the <planet>",
    14: "Il governo ti pagherà <payment> per portare questi <bunks> lavoratori volontari sul <planet>, dove daranno una "
        "mano nella costruzione in cambio di vitto e alloggio.",
    15: "Scarichi i materiali da costruzione e ricevi <payment> come compenso.",
    16: "Materials to the <planet>",
    17: "Consegna queste <tons> di materiali da costruzione sul <planet> degli Heliarch entro il <date>. Il compenso "
        "sarà di <payment>.",
    18: "Materials to the <planet>",
    19: "Consegna queste <tons> di materiali da costruzione sul <planet> degli Heliarch entro il <date>. Il compenso "
        "sarà di <payment>.",
    20: "Materials to the <planet>",
    21: "Consegna queste <tons> di materiali da costruzione sul <planet> degli Heliarch entro il <date>. Il compenso "
        "sarà di <payment>.",
    22: "Scarichi la donazione di <commodity> e ricevi <payment> come compenso.",
    23: "Supplies to the <planet>",
    24: "Questa partita di <tons> di forniture è una donazione del governo di <origin> per sostenere il <planet> degli "
        "Heliarch. Ti verranno pagati <payment> alla consegna.",
    25: "Supplies to the <planet>",
    26: "Questa partita di <tons> di forniture è una donazione del governo di <origin> per sostenere il <planet> degli "
        "Heliarch. Ti verranno pagati <payment> alla consegna.",
    27: "Supplies to the <planet>",
    28: "Questa partita di <tons> di forniture è una donazione del governo di <origin> per sostenere il <planet> degli "
        "Heliarch. Ti verranno pagati <payment> alla consegna.",
    29: "Candidate to the <planet>",
    30: "Ti verranno pagati <payment> per trasportare questo candidato all'elevazione al rango di Heliarch sul "
        "<planet> entro il <date>.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'VALUE': 13, 'DESCRIPTION': 13, 'TEXT': 4}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 0
assert sum(u['english'].count('"') for u in SRC) == 0
assert [u['idx'] for u in SRC if u['kind'] not in ('VALUE', 'DESCRIPTION', 'TEXT')] == []
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<planet>': 28, '<payment>': 17, '<bunks>': 6, '<tons>': 6, '<date>': 4, '<origin>': 3,
                     '<commodity>': 1}, dict(tok)
assert sum(tok.values()) == 65
assert len(set(u['context'] for u in SRC)) == 17
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (16, 293)
assert sorted(D) == list(range(1, 31)), [i for i in range(1, 31) if i not in D]
VAL = {u['idx']: ENG[u['idx']].rstrip() for u in SRC if u['kind'] == 'VALUE'}
assert list(VAL.values()) == ['Workers to the <planet>'] * 3 + ['Volunteers to the <planet>'] * 3 + \
    ['Materials to the <planet>'] * 3 + ['Supplies to the <planet>'] * 3 + ['Candidate to the <planet>'], list(VAL.items())
for i, v in VAL.items():
    assert D[i] == v, (i, D[i], v)

T = {u['idx']: D[u['idx']] for u in SRC}

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t') == 0, idx
    assert txt.count('"') == eng.count('"') == 0, idx
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx in VAL:
        assert txt == eng.rstrip(), idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

per = collections.Counter(t for i, txt in T.items() for t in TAGS.findall(txt))
assert dict(per) == dict(tok), (dict(per), dict(tok))
dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 14, len(dup)
assert T[3] == T[5] == T[7] and T[10] == T[12] == T[14] and T[17] == T[19] == T[21] and T[24] == T[26] == T[28]

for n, (lo, hi) in enumerate(((1, 10), (11, 20), (21, 30))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('30 unita (10+10+10) · 13 VALUE identici + 13 DESCRIPTION + 4 TEXT · 17 contesti · 14 testi distinti')
print('65 token su 7 simboli, parita 1 = 1 per simbolo e per unita · zero tab · zero virgolette')
