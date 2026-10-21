r"""verify.py — L177 (`data/avgi/avgi ships.txt`, 39 unita', righe 1415-2337).

Invariante di **segmento**: 44 unita' prima della riga 1415 (L174…L176), **19 dopo** la 2337, 102 nel file; confine alla
riga 2424, tipo **DESCRIPTION** (`ship:Akoustiki`) — **misurato**.
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
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (39/39)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..39 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 40)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 39 righe 1415 - 2337', len(tu) == 39 and (first, last) == (1415, 2337), (len(tu), first, last))
ck('44 unita prima della riga 1415 (L174…L176)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 44)
ck('102 unita nel file, 19 dopo la riga 2337', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 102
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 19)
ck('max(line) del file = 2770, min(line) = 120', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (120, 2770))
ck('confine alla riga 2424, tipo DESCRIPTION (misurato)', db.execute(
    'select line,kind,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (2424, 'DESCRIPTION', 'ship:Akoustiki'))
ck('tipi: 29 TEXT + 7 DESCRIPTION + 3 VALUE', collections.Counter(u['kind'] for u in su)
   == {'TEXT': 29, 'DESCRIPTION': 7, 'VALUE': 3})
ck('ZERO UI_LABEL e ZERO token',
   [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == []
   and {t for u in su for t in TAGS.findall(u['english'])} == set())
ck('i 29 TEXT sono identici al sorgente',
   not [u['idx'] for u in tu if u['kind'] == 'TEXT' and u['italian'] != u['english']])
ck('i nomi dei TEXT, contati per nome',
   collections.Counter(u['english'] for u in tu if u['kind'] == 'TEXT')
   == {'Z-333 "Spark" Fusion Torch': 11, '"Nettle" KKV': 6, '"Orchid" Nuclear Missile': 5,
       'Z-666 "Zap" Fusion Torch': 5, '"Ophrys" Nuclear Torpedo': 2})
ck('58 virgolette, 2 per TEXT in entrambe le lingue',
   sum(u['english'].count('"') for u in su) == 58 == sum(u['italian'].count('"') for u in tu)
   and all(u['italian'].count('"') == 2 for u in tu if u['kind'] == 'TEXT'))
ck('i 3 VALUE identici al sorgente',
   [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'] != u['english']] == [])
ck('2 tab iniziali: idx 19 e 20', [u['idx'] for u in su if u['english'].startswith('\t')] == [19, 20]
   == [u['idx'] for u in tu if u['italian'].startswith('\t')])
ck('ZERO apici inglesi, nessun possessivo inglese in italiano',
   sum(u['english'].count("'") for u in su) == 0
   and not [u['idx'] for u in tu if re.search(r"[A-Za-z]+'s\b", u['italian'])])
ck('15 testi distinti, 5 contesti', len({u['english'] for u in tu}) == 15
   and len({u['context'] for u in tu}) == 5)
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
ck('le parti ricostruiscono translation.json (1..39)',
   sorted(merged) == list(range(1, 40)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 1415-2337',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 83/102 unita del file (81,4%) · 44 prima / 39 nel lotto / 19 dopo · confine riga 2424 (~DESCRIPTION)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L177 superato' if not fail else 'verify L177 fallito')
raise SystemExit(0 if not fail else 1)
