r"""verify.py — L178 (`data/avgi/avgi ships.txt`, 14 unita', righe 2424-2667).

Invariante di **segmento**: 83 unita' prima della riga 2424 (L174…L177), **5 dopo** la 2667, 102 nel file; confine alla
riga 2716, tipo **`DESCRIPTION`** (`ship:Optikon`) — **misurato**. Dopo questo lotto restano 5 unita': il file si chiude
in L179.
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
PATH = 'data/avgi/avgi ships.txt'
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
ck('unita: 14 righe 2424 - 2667', len(tu) == 14 and (first, last) == (2424, 2667), (len(tu), first, last))
ck('83 unita prima della riga 2424 (L174…L177)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 83)
ck('102 unita nel file, 5 dopo la riga 2667', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 102
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 5)
ck('max(line) del file = 2770, min(line) = 120', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (120, 2770))
ck('confine alla riga 2716, tipo DESCRIPTION (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (2716, 'DESCRIPTION', 'ship:Optikon'))
ck('tipi: 10 DESCRIPTION + 3 TEXT + 1 VALUE', collections.Counter(u['kind'] for u in su)
   == {'DESCRIPTION': 10, 'TEXT': 3, 'VALUE': 1})
ck('ZERO UI_LABEL e ZERO token',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck('i 3 TEXT sono identici al sorgente',
   not [u['idx'] for u in tu if u['kind'] == 'TEXT' and u['italian'] != u['english']])
ck('6 virgolette, 2 per TEXT', sum(u['english'].count('"') for u in su) == 6
   == sum(u['italian'].count('"') for u in tu)
   and all(u['italian'].count('"') == 2 for u in tu if u['kind'] == 'TEXT'))
ck('il VALUE e identico al sorgente',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('6 tab iniziali: idx 2, 4, 5, 10, 13, 14', [u['idx'] for u in su if u['english'].startswith('\t')]
   == [2, 4, 5, 10, 13, 14] == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('boilerplate Fighters (2/5) e Drones (10/14) identici, e distinti fra loro',
   by[2]['italian'] == by[5]['italian'] and by[10]['italian'] == by[14]['italian']
   and by[2]['italian'] != by[10]['italian']
   and 'caccia' in by[2]['italian'] and 'droni' in by[10]['italian'])
ck('ZERO apici inglesi, nessun possessivo inglese in italiano',
   sum(u['english'].count("'") for u in su) == 0
   and not [u['idx'] for u in tu if re.search(r"[A-Za-z]+'s\b", u['italian'])])
ck('12 testi distinti, 4 contesti', len({u['english'] for u in tu}) == 12
   and len({u['context'] for u in tu}) == 4)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('nessuno spazio finale, tab iniziale ammesso',
   not [u['idx'] for u in tu
        if u['english'].rstrip('\t') != u['english'].rstrip('\t').rstrip()
        or u['italian'].rstrip('\t') != u['italian'].rstrip('\t').rstrip()])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu if u['kind'] == 'DESCRIPTION']
ck('rapporto nel gate (solo DESCRIPTION)', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le parti ricostruiscono translation.json (1..14)',
   sorted(merged) == list(range(1, 15)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 2424-2667',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 97/102 unita del file (95,1%) · 83 prima / 14 nel lotto / 5 dopo · confine riga 2716 (~DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L178 superato' if not fail else 'verify L178 fallito')
raise SystemExit(0 if not fail else 1)
