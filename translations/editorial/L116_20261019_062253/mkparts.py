"""mkparts.py — L116: valida `parts/part01-04.json` (133 unita', righe 1569-1865).

Costruttore ad asserzioni: legge `source.json`, le parti e `state.db` in sola lettura, e abortisce se una
premessa del contratto L116 non regge. Non riscrive il testo (la fonte e' il JSON): normalizza solo l'ordine
delle chiavi.

Premesse misurate e asserite:
- **133 unita'**, tutte `PENDING`, tutte `TUTORIAL_TIP` — e' **tutto il resto del file**;
- **80 contesti** per 133 unita': **62** singole, **1** coppia, **4** terne, **8** quaterne, **5** gruppi da
  cinque; i primi nomi hanno **tre spazi iniziali** (`tip:   Show flagship overlay`);
- **144 virgolette** in 66 unita' (61 con due, 4 con quattro, una con sei), e i testi fra virgolette sono
  **identici** all'inglese: sono chiavi e valori di `Preferences` (`"ship cap"`, `"off"`, `"fleet: …"`) e nomi
  di gamerule, non prosa;
- **1 token** `<shift>`, una sola famiglia;
- **zero tab**, **zero quadre**, **zero backtick**;
- **nessuna ripetizione**: il `source.json` non ha due unita' con lo stesso inglese.
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
CTX = {u['idx']: u['context'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')
QUOTED = re.compile(r'"([^"]*)"')

T = {}
for f in sorted(x for x in os.listdir(PARTS) if x.endswith('.json')):
    for k, v in json.load(open(os.path.join(PARTS, f), encoding='utf-8')).items():
        assert int(k) not in T, 'chiave %s in due parti' % k
        T[int(k)] = v

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
STATES = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(STATES.values()) == {'PENDING'}, {k: v for k, v in STATES.items() if v != 'PENDING'}

assert sorted(T) == list(range(1, 134)) == sorted(ENG), (len(T), len(ENG))
assert all(KIND[i] == 'TUTORIAL_TIP' for i in T), collections.Counter(KIND.values())

# --- forma del sorgente -------------------------------------------------------------------
assert sum(1 for u in SRC if '\t' in u['english']) == 0
assert sum(u['english'].count('`') for u in SRC) == 0
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {'<shift>': 1}
assert not [u['idx'] for u in SRC if '[' in u['english'] or ']' in u['english']]
assert sum(u['english'].count('"') for u in SRC) == 144
assert collections.Counter(u['english'].count('"') for u in SRC if '"' in u['english']) == {2: 61, 4: 4, 6: 1}
assert SRC[0]['context'] == 'tip:   Show flagship overlay'
assert SRC[-1]['context'] == 'tip:boarding: installed'

# --- contesti: 80 per 133 unita' ----------------------------------------------------------
seen = collections.Counter(u['context'] for u in SRC)
assert len(seen) == 80, len(seen)
assert collections.Counter(seen.values()) == {1: 62, 2: 1, 3: 4, 4: 8, 5: 5}, collections.Counter(seen.values())
assert max(seen.values()) == 5

# --- nessuna ripetizione ------------------------------------------------------------------
g = collections.Counter(u['english'] for u in SRC)
assert not [k for k, v in g.items() if v > 1], 'nessuna ripetizione attesa'

# --- asserzioni per unita' ----------------------------------------------------------------
for idx, txt in T.items():
    assert '\t' not in txt, idx
    assert txt.count('"') == ENG[idx].count('"'), (idx, txt.count('"'), ENG[idx].count('"'))
    assert QUOTED.findall(txt) == QUOTED.findall(ENG[idx]), (idx, QUOTED.findall(txt), QUOTED.findall(ENG[idx]))
    assert TAGS.findall(txt) == TAGS.findall(ENG[idx]), (idx, TAGS.findall(txt), TAGS.findall(ENG[idx]))
    assert '[' not in txt and ']' not in txt and '`' not in txt, idx
    assert txt.strip() and txt.strip() != ENG[idx].strip(), idx
    assert not re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b', txt), (idx, txt)
    r = len(txt) / len(ENG[idx])
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3))

# --- parti canoniche ----------------------------------------------------------------------
for n, (lo, hi) in enumerate(((1, 34), (35, 67), (68, 100), (101, 133))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('133 unita (34+33+33+33) · 80 contesti (62/1/4/8/5) · 144 virgolette · 1 token <shift> · 0 ripetizioni')
