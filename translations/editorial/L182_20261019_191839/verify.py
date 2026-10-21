r"""verify.py — L182 (`data/human/outfits.txt`, 14 unita', righe 236-387).

Invariante di **segmento**: 21 unita' prima (L180+L181), 14 nel lotto, **28 dopo** (63 - 21 - 14); confine alla riga 390,
tipo **`VALUE`** (`outfit:Luxury Accommodations`) — di nuovo un nome con le parentesi assenti, ma un `VALUE`.
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


ck('riga grezza identica al sorgente (14/14)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..14 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 15)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 14 righe 236 - 387', len(tu) == 14 and (first, last) == (236, 387), (len(tu), first, last))
ck('21 unita prima (chiuse da L180 e L181)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 21)
ck('63 unita nel file, 28 dopo la riga 387 (63 - 21 - 14)', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 63
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 28)
ck('confine alla riga 390, tipo VALUE', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (390, 'VALUE', 'outfit:Luxury Accommodations'))
ck('min(line) 15 e max(line) 606: il file non e\' ancora chiuso', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (15, 606))
ck('tipi: 13 DESCRIPTION + 1 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 13, 'VALUE': 1})
ck('1 tab (idx 10), ZERO virgolette, ZERO token',
   [u['idx'] for u in su if u['english'].startswith('\t')] == [10]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu)
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck("l VALUE e identico al sorgente (`Jump Drives (Broken)`)",
   by[1]['italian'] == by[1]['english'] == 'Jump Drives (Broken)')
ck('6 apici inglesi con le loro cause, 9 italiani: i conteggi NON coincidono',
   sum(u['english'].count("'") for u in su) == 6
   and {u['idx']: u['english'].count("'") for u in su if "'" in u['english']} == {7: 1, 8: 2, 12: 1, 14: 2}
   and sum(u['italian'].count("'") for u in tu) == 9
   and not [u['idx'] for u in tu if re.search(r"\b[A-Za-z]+'s\b", u['italian'])])
ck('14 testi distinti, 12 contesti (due con 2 unita)', len({u['english'] for u in tu}) == 14
   and len({u['context'] for u in tu}) == 12)
ck('i tre scanner condividono la frase finale (3, 4, 7)',
   [u['idx'] for u in tu if 'aumenta portata e velocità di scansione' in u['italian']] == [3, 4, 7])
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
ck('le parti ricostruiscono translation.json (1..14)',
   sorted(merged) == list(range(1, 15)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 236-387',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 35/63 unita del file (55,6%) · 21 prima / 14 nel lotto / 28 dopo · confine riga 390 (~VALUE)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L182 superato' if not fail else 'verify L182 fallito')
raise SystemExit(0 if not fail else 1)
