"""mkparts2.py — L111: costruisce `parts/part01-04.json` (104 unita', righe 16-328).

**SCOPERTA CHE CAMBIA IL LOTTO**: le prime **52** unita' sono **`APPROVED`** in `state.db` e hanno gia' il testo
italiano. Non si traducono: si **riproducono alla lettera** dal database (sola lettura). Il registro approvato
fissa le convenzioni del pannello:

- **«tu»** al giocatore («la tua nave», «puoi», «ti occulti»), non «voi»;
- **«danni da …»** al plurale («danni da ustione»), con il participio concordato («Danni da ustione resistiti al
  secondo»);
- **«quando si attiva questo postbruciatore»**, **«ammiraglia»**, **«percentuale»**, **«spazio carico»**.

Le altre **52** unita' (53-104) sono `PENDING`, tradotte in `my_pending.json` **seguendo quelle convenzioni**:
stanno nello stesso pannello, e un pannello che alterna «tu» e «voi» e' un difetto visibile.

Questo file **non** contiene il testo: lo legge da `my_pending.json` (le mie 52) e da `state.db` (le 52 approvate),
cosi' non esiste una seconda copia che possa divergere.
"""
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

MY = {int(k): v for k, v in json.load(open(os.path.join(HERE, 'my_pending.json'), encoding='utf-8')).items()}
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
state, ital = {}, {}
for u in src:
    r = db.execute('select state, italian from units where id=?', (u['id'],)).fetchone()
    state[u['idx']], ital[u['idx']] = r[0], r[1]
appr = sorted(i for i in state if state[i] == 'APPROVED')
pend = sorted(i for i in state if state[i] == 'PENDING')
assert appr == list(range(1, 53)), appr[:3] + appr[-3:]
assert pend == list(range(53, 105)) and sorted(MY) == pend, (len(pend), len(MY))
assert all(ital[i] for i in appr), 'un APPROVED senza testo italiano'

ALL = dict(MY)
for i in appr:
    ALL[i] = ital[i]

for idx, txt in ALL.items():
    assert '\t' not in txt, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    assert kind[idx] == 'TUTORIAL_TIP', (idx, kind[idx])
    if idx in appr:
        assert txt == ital[idx], 'il testo approvato va riprodotto alla lettera'
    else:
        assert txt.strip() != eng[idx].strip(), idx
        assert not re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b', txt), (idx, txt)

assert len(ALL) == 104 == len({u['idx'] for u in src})
g = {}
for u in src:
    g.setdefault(u['english'], []).append(u['idx'])
assert not [v for v in g.values() if len(v) > 1], 'nessuna ripetizione attesa'
LOW = ' '.join(ALL.values()).lower()
for term in ('massa', 'accelerazione', 'energia', 'calore', 'raffreddamento', 'carburante', 'scafo',
             'scudi', 'occultamento', 'equipaggiamento', 'tonnellate', 'equipaggio', 'danni'):
    assert term in LOW, term

os.makedirs(OUT, exist_ok=True)
chunks = [(1, 26), (27, 52), (53, 78), (79, 104)]
for n, (lo, hi) in enumerate(chunks, 1):
    d = {k: ALL[k] for k in range(lo, hi + 1)}
    assert len(d) == 26
    with open(os.path.join(OUT, 'part%02d.json' % n), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte 104 unita: %d APPROVED riprodotte + %d PENDING tradotte' % (len(appr), len(pend)))
