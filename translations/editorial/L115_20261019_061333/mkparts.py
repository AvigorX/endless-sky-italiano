"""mkparts.py — L115: valida `parts/part01-03.json` (104 unita', righe 1312-1566).

Costruttore ad asserzioni: legge `source.json`, le parti e `state.db` in sola lettura, e abortisce se una
premessa del contratto L115 non regge. Non riscrive il testo (la fonte e' il JSON): normalizza solo l'ordine
delle chiavi.

Premesse misurate e asserite:
- **104 unita'**, tutte `PENDING`, tutte `TUTORIAL_TIP`;
- **72 contesti** per 104 unita': **56** singole, **7** coppie, **5** terne, **2** quaterne, **1** da cinque
  (`Text alignment`) e **1** da sei (`Show status overlays`);
- **82 virgolette** in 38 unita' (37 con due, una con otto), e i testi fra virgolette sono **identici**
  all'inglese: sono chiavi e valori di impostazione del gioco (`Preferences::Has("Escorts expend ammo")`),
  non prosa, e tradurli romperebbe il riferimento al menu;
- **8 token** `<shift>`, una sola famiglia, parita' per unita';
- **zero tab**, **zero quadre**, **zero backtick**;
- **una ripetizione** identica: `- "fast": just uses the ship's sprite.` (unita' 89 e 92), resa identica.
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

assert sorted(T) == list(range(1, 105)) == sorted(ENG), (len(T), len(ENG))
assert all(KIND[i] == 'TUTORIAL_TIP' for i in T), collections.Counter(KIND.values())

# --- forma del sorgente -------------------------------------------------------------------
assert sum(1 for u in SRC if '\t' in u['english']) == 0
assert sum(u['english'].count('`') for u in SRC) == 0
assert sum(len(TAGS.findall(u['english'])) for u in SRC) == 8
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {'<shift>': 8}
assert not [u['idx'] for u in SRC if '[' in u['english'] or ']' in u['english']]
assert sum(u['english'].count('"') for u in SRC) == 82
quote = collections.Counter(u['english'].count('"') for u in SRC if '"' in u['english'])
assert quote == {2: 37, 8: 1}, quote

# --- contesti: 72 per 104 unita' ----------------------------------------------------------
seen = collections.Counter(u['context'] for u in SRC)
assert len(seen) == 72, len(seen)
assert collections.Counter(seen.values()) == {1: 56, 2: 7, 3: 5, 4: 2, 5: 1, 6: 1}, collections.Counter(seen.values())
rep_ctx = sorted((k, v) for k, v in seen.items() if v > 1)
assert [k for k, _ in rep_ctx if _ == 6] == ['tip:Show status overlays']
assert [k for k, _ in rep_ctx if _ == 5] == ['tip:Text alignment']

# --- ripetizioni: una sola coppia ---------------------------------------------------------
grp = collections.Counter(u['english'] for u in SRC)
dup = sorted(u['idx'] for u in SRC if grp[u['english']] > 1)
assert dup == [89, 92], dup
assert T[89] == T[92], ('coppia non identica', T[89], T[92])

# --- asserzioni per unita' ----------------------------------------------------------------
# Eccezione dichiarata: l'unita' 10 cita l'etichetta del pannello "surge", che L113 ha gia' reso
# «picco» nello stesso pannello di potenza. Tutte le altre citazioni sono chiavi/valori di
# impostazione (`Preferences::Has("Escorts expend ammo")`) e restano identiche all'inglese.
QEXC = {10: (['picco'], ['surge'])}
for idx, txt in T.items():
    assert '\t' not in txt, idx
    assert txt.count('"') == ENG[idx].count('"'), (idx, txt.count('"'), ENG[idx].count('"'))
    if idx in QEXC:
        assert (QUOTED.findall(txt), QUOTED.findall(ENG[idx])) == QEXC[idx], (idx, QUOTED.findall(txt))
    else:
        assert QUOTED.findall(txt) == QUOTED.findall(ENG[idx]), (idx, QUOTED.findall(txt), QUOTED.findall(ENG[idx]))
    assert TAGS.findall(txt) == TAGS.findall(ENG[idx]), (idx, TAGS.findall(txt), TAGS.findall(ENG[idx]))
    assert '[' not in txt and ']' not in txt and '`' not in txt, idx
    assert txt.strip() and txt.strip() != ENG[idx].strip(), idx
    assert not re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b', txt), (idx, txt)
    r = len(txt) / len(ENG[idx])
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3))

# --- parti canoniche ----------------------------------------------------------------------
for n, (lo, hi) in enumerate(((1, 35), (36, 70), (71, 104))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('104 unita (35+35+34) · 72 contesti (56/7/5/2/1/1) · 82 virgolette · 8 token <shift> · 1 coppia identica')
