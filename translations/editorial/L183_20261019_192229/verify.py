r"""verify.py — L183 (`data/human/outfits.txt`, 15 unita', righe 390-514).

Invariante di **segmento**: 35 unita' prima (L180-L182), 15 nel lotto, **13 dopo** (63 - 35 - 15); confine alla riga 520,
tipo **`VALUE`** (`outfit:Puny`). Dopo L183 il file resta aperto con **13 unita'**.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/human/outfits.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (15/15)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..15 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 16)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 15 righe 390 - 514', len(tu) == 15 and (first, last) == (390, 514), (len(tu), first, last))
ck('35 unita prima (chiuse da L180, L181, L182)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 35)
ck('63 unita nel file, 13 dopo la riga 514 (63 - 35 - 15)', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 63
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 13)
ck('confine alla riga 520, tipo VALUE', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (520, 'VALUE', 'outfit:Puny'))
ck('tipi: 11 DESCRIPTION + 4 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 11, 'VALUE': 4})
ck('1 tab (idx 14), ZERO virgolette, ZERO token',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [14]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck('i 4 VALUE identici al sorgente (Antigrav Glasses plurale)',
   {u['idx']: u['italian'] for u in tu if u['kind'] == 'VALUE'}
   == {1: 'Luxury Accommodations', 6: 'Fragmentation Grenades', 9: 'Nerve Gas', 12: 'Antigrav Glasses'})
ck("3 apici inglesi, tutti di elisione; nessun possessivo sopravvissuto in italiano",
   sum(u['english'].count("'") for u in su) == 3
   and {u['idx']: u['english'].count("'") for u in su if "'" in u['english']} == {4: 1, 14: 1, 15: 1}
   and not [u['idx'] for u in tu if re.search(r"\b[A-Za-z]+'s\b", u['italian'])])
ck('15 testi distinti, 10 contesti (uno con 3, tre con 2, sei con 1)',
   len({u['english'] for u in tu}) == 15 and len({u['context'] for u in tu}) == 10
   and sorted(collections.Counter(u['context'] for u in tu).values()) == [1] * 6 + [2, 2, 2, 3])
ck('il Mug resta una battuta di una riga', len(by[11]['italian'].split()) <= 10)
ck('il gas nervino chiude con "..." e non con l\'ellissi tipografica',
   by[10]['italian'].endswith('...') and '\u2026' not in by[10]['italian'])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale (tab iniziale ammesso)',
   not [u['idx'] for u in tu if u['english'].rstrip('\t') != u['english'].rstrip('\t').rstrip()
        or u['italian'].rstrip('\t') != u['italian'].rstrip('\t').rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..15)',
   sorted(merged) == list(range(1, 16)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 390-514',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 50/63 unita del file (79,4%) · 35 prima / 15 nel lotto / 13 dopo · confine riga 520 (~VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L183 superato' if not fail else 'verify L183 fallito')
raise SystemExit(0 if not fail else 1)
