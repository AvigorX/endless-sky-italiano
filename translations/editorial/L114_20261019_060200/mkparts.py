"""mkparts.py — L114: valida `parts/part01-03.json` (110 unita', righe 976-1309).

Costruttore **ad asserzioni**: legge `source.json`, le parti scritte a mano e `state.db` in sola lettura, e
abortisce se una premessa del contratto L114 non regge. Non riscrive il testo delle parti (la fonte e' il
JSON): normalizza solo l'ordine delle chiavi.

Premesse misurate e asserite:
- **110 unita'**, tutte `PENDING`, tutte `TUTORIAL_TIP`;
- **110 contesti distinti**, uno per unita' (la forma di L113 — 87 su 96 — qui sarebbe un errore);
- **zero tab**, **zero token `<...>`**, **zero quadre**, **zero backtick**;
- **12 virgolette** in 5 unita' (`19`, `38`, `52`, `66`, `85`), parita' per unita';
- **quattro coppie di ripetizioni legittime** (`/ second` contro `/ shot`), rese **identiche**:
  `17 = 64`, `18 = 65`, `19 = 66`, `36 = 83`. Qui il criterio «zero ripetizioni» di L111-L113 e' rovesciato.
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

T = {}
for f in sorted(x for x in os.listdir(PARTS) if x.endswith('.json')):
    for k, v in json.load(open(os.path.join(PARTS, f), encoding='utf-8')).items():
        assert int(k) not in T, 'chiave %s in due parti' % k
        T[int(k)] = v

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
STATES = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(STATES.values()) == {'PENDING'}, {k: v for k, v in STATES.items() if v != 'PENDING'}

assert sorted(T) == list(range(1, 111)) == sorted(ENG), (len(T), len(ENG))
assert all(KIND[i] == 'TUTORIAL_TIP' for i in T), collections.Counter(KIND.values())

# --- forma del sorgente -------------------------------------------------------------------
assert sum(1 for u in SRC if '\t' in u['english']) == 0
assert sum(u['english'].count('`') for u in SRC) == 0
assert sum(len(TAGS.findall(u['english'])) for u in SRC) == 0
assert not [u['idx'] for u in SRC if '[' in u['english'] or ']' in u['english']]
quote = {u['idx']: u['english'].count('"') for u in SRC if '"' in u['english']}
assert quote == {19: 2, 38: 2, 52: 4, 66: 2, 85: 2}, quote
assert sum(quote.values()) == 12

# --- contesti: 110 distinti, uno per unita' ----------------------------------------------
seen = collections.Counter(u['context'] for u in SRC)
assert len(seen) == 110 == len(SRC) and max(seen.values()) == 1, len(seen)

# --- ripetizioni: esattamente le quattro coppie per secondo / per colpo ------------------
grp = collections.Counter(u['english'] for u in SRC)
dup = sorted([u['idx'] for u in SRC if grp[u['english']] > 1])
assert sorted(grp.values()) == [1] * 102 + [2] * 4, grp
assert dup == [17, 18, 19, 36, 64, 65, 66, 83], dup
for a, b in ((17, 64), (18, 65), (19, 66), (36, 83)):
    assert T[a] == T[b], ('coppia non identica', a, b)

# --- asserzioni per unita' ----------------------------------------------------------------
for idx, txt in T.items():
    assert '\t' not in txt, idx
    assert txt.count('"') == ENG[idx].count('"'), (idx, txt.count('"'), ENG[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(ENG[idx]) == [], idx
    assert '[' not in txt and ']' not in txt and '`' not in txt, idx
    assert txt.strip() and txt.strip() != ENG[idx].strip(), idx
    assert not re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b', txt), (idx, txt)
    r = len(txt) / len(ENG[idx])
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3))

# --- parti canoniche -----------------------------------------------------------------------
for n in range(3):
    lo, hi = 1 + 37 * n, min(37 + 37 * n, 110)
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('110 unita (37+37+36) · 110 contesti · 12 virgolette · 4 coppie identiche · tutte PENDING')
