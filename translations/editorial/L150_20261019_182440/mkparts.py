"""mkparts.py — L150: `data/coalition/coalition jobs.txt`, righe 639-794 (14 unita').

Due famiglie quasi identiche (turisti in partenza e in rientro) che differiscono per **due parole** («bring them to» /
«bring them home to»): la resa non si copia, si costruisce sul testo di ciascuna. Arriva **`<commodity>`**, una sola
volta su 33 token: si perde a occhio, quindi la parita' e' per simbolo.
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

OUT = ("Questi <bunks> turisti ti pagheranno <payment> per portarli a <destination> e desiderano viaggiare su una nave "
       "molto confortevole. Il compenso decade se non arrivano entro il <date>.")
HOME = ("Questi <bunks> turisti ti pagheranno <payment> per riportarli a casa a <destination> e desiderano viaggiare "
        "su una nave molto confortevole. Il compenso decade se non arrivano entro il <date>.")

D = {
    1: "Vacationers to <planet>",
    2: OUT,
    3: "Vacationers to <planet>",
    4: OUT,
    5: "Vacationers to <planet>",
    6: OUT,
    7: "I turisti ti ringraziano per averli riportati a casa e ti pagano <payment>.",
    8: "Vacationers to <planet>",
    9: HOME,
    10: "Vacationers to <planet>",
    11: HOME,
    12: "Vacationers to <planet>",
    13: HOME,
    14: "Il destinatario ti ringrazia per aver portato il <commodity> qui così in fretta e ti paga <payment>.",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'VALUE': 6, 'DESCRIPTION': 6, 'TEXT': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 0
assert sum(u['english'].count('"') for u in SRC) == 0
assert [u['idx'] for u in SRC if u['kind'] in ('LOGBOOK', 'DIALOG', 'UI_LABEL')] == []
assert len(set(u['context'] for u in SRC)) == 8
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<payment>': 8, '<planet>': 6, '<bunks>': 6, '<destination>': 6, '<date>': 6,
                     '<commodity>': 1}, dict(tok)
assert sum(tok.values()) == 33 and tok['<commodity>'] == 1
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (639, 794)
assert sorted(D) == list(range(1, 15)), [i for i in range(1, 15) if i not in D]
VAL = {u['idx']: ENG[u['idx']].rstrip() for u in SRC if u['kind'] == 'VALUE'}
assert set(VAL.values()) == {'Vacationers to <planet>'} and len(VAL) == 6
for i, v in VAL.items():
    assert D[i] == v, (i, D[i], v)
# le due famiglie differiscono solo per «home»
assert ENG[2].replace('bring them to', 'bring them home to') == ENG[9]
assert ENG[2] != ENG[9] and ENG[7] != ENG[14]

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
assert len(dup) == 5, len(dup)
assert T[2] == T[4] == T[6] == OUT and T[9] == T[11] == T[13] == HOME
assert T[2] != T[9], 'la variante «home» deve avere una resa diversa'

for n, (lo, hi) in enumerate(((1, 6), (7, 10), (11, 14))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('14 unita (6+4+4) · 6 VALUE + 6 DESCRIPTION + 2 TEXT · 8 contesti · 5 testi distinti')
print('33 token su 6 simboli, <commodity> UNA sola volta · zero tab · zero virgolette')
