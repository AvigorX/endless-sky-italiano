"""mkparts.py — L139: `data/starts.txt`, righe 365-366 (2 unita'). **CHIUDE IL FILE** a 113/113.

Le due unita' sono **nomi di equipaggiamento** del Grasshopper, non prosa:

    "Benga" Atomic Thruster
    "Biroo" Atomic Steering

Restano **identiche** al sorgente (lista `ID_OK` dichiarata, con un controllo proprio che le verifica una per una). Le
virgolette fanno parte del nome: non sono dialogo, e tradurle romperebbe il riferimento al bene di gioco.

Il `raw` del sorgente e' `\\t\\t`"Benga" Atomic Thruster`` — tab e backtick stanno **fuori** dal campo `english`, e il
game li usa per marcare il nome; per questo le unita' non hanno tab iniziale nel testo e non hanno backtick.
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
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

ID_OK = {
    1: '"Benga" Atomic Thruster',
    2: '"Biroo" Atomic Steering',
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'TEXT': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 0
assert sum(u['english'].count('"') for u in SRC) == 4
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
assert collections.Counter(u['context'] for u in SRC) == {'ship:Grasshopper': 2}
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (365, 366)
assert [ENG[1], ENG[2]] == ['"Benga" Atomic Thruster', '"Biroo" Atomic Steering']
assert sorted(ID_OK) == [1, 2]
assert all(ID_OK[k] == KEY[k] for k in ID_OK)

T = {}
for u in SRC:
    eng = u['english']
    assert ENG[u['idx']] == KEY[u['idx']], ('niente tab nel campo english', u['idx'])
    T[u['idx']] = ID_OK[u['idx']]
    assert T[u['idx']] == eng, u['idx']

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t') == 0, idx
    assert txt.count('"') == eng.count('"') == 2, (idx, txt.count('"'))
    assert TAGS.findall(txt) == [], idx
    assert txt.strip() == eng.strip(), idx
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 2, len(dup)

with open(os.path.join(PARTS, 'part01.json'), 'w', encoding='utf-8') as f:
    json.dump({str(k): T[k] for k in sorted(T)}, f, ensure_ascii=False, indent=1)
print('2 unita · 2 testi identici al sorgente (ID_OK) · 1 contesto · zero tab · 4 virgolette (parti dei nomi)')
print('zero VALUE, zero UI_LABEL, zero token: tre asserzioni vuote scritte')
